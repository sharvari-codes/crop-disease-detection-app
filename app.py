import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
from model_handler import ModelHandler
from utils import preprocess_image, get_disease_info
from auth_handler import AuthHandler
from translations import get_text, get_all_translations

# Initialize auth handler
auth = AuthHandler()

# Set page configuration
st.set_page_config(
    page_title="Crop Disease Detection",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS with refined green color palette and professional styling
st.markdown("""
    <style>
    /* Color Variables */
    :root {
        --primary-green: #2E7D32;      /* Deep Forest Green */
        --secondary-green: #1B5E20;    /* Very Dark Green */
        --accent-green: #43A047;       /* Vibrant Green */
        --light-green: #A5D6A7;        /* Light Green */
        --pale-green: #E8F5E9;         /* Pale Green */
        --surface-green: #C8E6C9;      /* Surface Green */
    }
    
    /* Background styling */
    body {
        background: #FFFFFF !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .stApp {
        background: #FFFFFF !important;
    }
    
    [data-testid="stAppViewContainer"] {
        background: #FFFFFF !important;
    }
    
    [data-testid="stDecoration"] {
        background: #FFFFFF !important;
    }
    
    /* Main container */
    .main {
        padding: 2rem 1rem;
        background: #FFFFFF !important;
    }
    
    /* Header styling */
    .header {
        color: #43A047;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        letter-spacing: 1px;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
        border-left: 5px solid #43A047;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(67, 160, 71, 0.15);
        transition: all 0.3s ease;
    }
    
    .info-box:hover {
        box-shadow: 0 6px 20px rgba(67, 160, 71, 0.25);
        transform: translateY(-2px);
    }
    
    /* Authentication box */
    .auth-box {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FFFF 100%);
        border-radius: 15px;
        padding: 2.5rem;
        margin: 2rem auto;
        max-width: 450px;
        box-shadow: 0 10px 40px rgba(46, 125, 50, 0.2);
        border: 1px solid rgba(67, 160, 71, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #43A047 0%, #2E7D32 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(67, 160, 71, 0.3);
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(67, 160, 71, 0.4);
        transform: translateY(-2px);
        background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);
    }
    
    /* Form inputs */
    .stTextInput > div > div > input,
    .stPasswordInput > div > div > input {
        background-color: #F5F5F5;
        border: 2px solid #E0E0E0;
        border-radius: 8px;
        padding: 0.6rem 0.8rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stPasswordInput > div > div > input:focus {
        border-color: #43A047;
        box-shadow: 0 0 10px rgba(67, 160, 71, 0.2);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(90deg, rgba(67, 160, 71, 0.1) 0%, rgba(67, 160, 71, 0.05) 100%);
        border-radius: 10px;
        padding: 0.5rem;
    }
    
    .stTabs [aria-selected="true"] > div {
        background: linear-gradient(135deg, #43A047 0%, #2E7D32 100%);
        color: white;
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Card styling */
    .stMetric {
        background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(67, 160, 71, 0.15);
        border-left: 4px solid #43A047;
    }
    
    /* Success messages */
    .stSuccess {
        background: linear-gradient(135deg, #C8E6C9 0%, #A5D6A7 100%) !important;
        border-left: 5px solid #43A047 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 15px rgba(67, 160, 71, 0.2) !important;
    }
    
    /* Error messages */
    .stError {
        background: linear-gradient(135deg, #FFCDD2 0%, #EF9A9A 100%) !important;
        border-left: 5px solid #F44336 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 15px rgba(244, 67, 54, 0.2) !important;
    }
    
    /* Warning messages */
    .stWarning {
        background: linear-gradient(135deg, #FFF9C4 0%, #FFF59D 100%) !important;
        border-left: 5px solid #FBC02D !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 15px rgba(251, 192, 45, 0.2) !important;
    }
    
    /* Info messages */
    .stInfo {
        background: linear-gradient(135deg, #B3E5FC 0%, #81D4FA 100%) !important;
        border-left: 5px solid #03A9F4 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 15px rgba(3, 169, 244, 0.2) !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #E8F5E9 0%, #F1F8E9 100%);
        border-radius: 8px;
        border-left: 4px solid #43A047;
    }
    
    .streamlit-expanderContent {
        background: linear-gradient(135deg, #F5FFF5 0%, #FFFEF5 100%);
        border-radius: 0 0 8px 8px;
        border-left: 4px solid #43A047;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: #FFFFFF;
        box-shadow: 2px 0 15px rgba(0, 0, 0, 0.1);
    }
    
    [data-testid="stSidebar"] > div > div {
        background: transparent;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .streamlit-expanderHeader,
    [data-testid="stSidebar"] .stMarkdown {
        color: #333333 !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #43A047 !important;
        text-shadow: none;
    }
    
    /* Divider styling */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #43A047, transparent);
        margin: 2rem 0;
    }
    
    /* Login page styling */
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: #FFFFFF;
    }
    
    .login-content {
        text-align: center;
        color: #333333;
    }
    
    .login-title {
        color: #43A047;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: none;
        margin-bottom: 1rem;
    }
    
    .login-subtitle {
        color: #666666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        opacity: 1;
    }
    
    /* Form title styling */
    .form-title {
        color: #2E7D32;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }
    
    /* Dark text for login labels */
    .stTextInput label,
    .stPasswordInput label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    
    /* Welcome back and form headers dark */
    .stForm h4 {
        color: #1a1a1a !important;
        font-weight: 700 !important;
    }
    
    /* Section divider */
    .section-divider {
        border: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #43A047, transparent);
        margin: 1.5rem 0;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .header {
            font-size: 2rem;
        }
        
        .auth-box {
            margin: 1rem 0.5rem;
            padding: 1.5rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False
if 'predictions' not in st.session_state:
    st.session_state.predictions = None
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = "login"  # "login" or "register"
if 'language' not in st.session_state:
    st.session_state.language = "en"  # "en", "mr", "hi"


def show_login_page():
    """Display login and registration interface"""
    
    lang = st.session_state.language
    t = lambda key: get_text(key, lang)
    
    # Language selector at top
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        selected_lang = st.selectbox(
            t("language"),
            options=["en", "mr", "hi", "kn"],
            format_func=lambda x: {"en": "English", "mr": "मराठी", "hi": "हिंदी", "kn": "ಕನ್ನಡ"}[x],
            key="lang_selector",
            label_visibility="collapsed"
        )
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()
    
    # Decorative header
    st.markdown(f"""
        <div style="text-align: center; margin: 3rem 0 2rem 0;">
            <h1 style="color: #43A047; font-size: 2.8rem; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); margin: 0;">
                {t("crop_disease_detection")}
            </h1>
            <p style="color: #A5D6A7; font-size: 1.2rem; margin-top: 0.5rem; font-weight: 300;">
                {t("ai_health_monitoring")}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("---")
        
        # Auth mode toggle with enhanced styling
        auth_col1, auth_col2 = st.columns(2)
        with auth_col1:
            if st.button(t("login"), use_container_width=True, key="login_btn"):
                st.session_state.auth_mode = "login"
        with auth_col2:
            if st.button(t("register"), use_container_width=True, key="register_btn"):
                st.session_state.auth_mode = "register"
        
        st.markdown("---")
        
        if st.session_state.auth_mode == "login":
            st.markdown(f"""
                <div style="text-align: center; margin: 1.5rem 0;">
                    <h3 style="color: #43A047; margin-top: 0.5rem;">{t("secure_login")}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            with st.form("login_form"):
                st.markdown(f"<h4 style='color: #1a1a1a; font-weight: 700;'>{t("welcome_back")}</h4>", unsafe_allow_html=True)
                username = st.text_input(t("username"), placeholder=t("username"))
                password = st.text_input(t("password"), type="password", placeholder=t("password"))
                
                submit_btn = st.form_submit_button(t("login"), use_container_width=True)
                
                if submit_btn:
                    if username and password:
                        success, message, user_data = auth.login_user(username, password)
                        if success:
                            st.session_state.logged_in = True
                            st.session_state.username = username
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                    else:
                        st.warning("Please enter both username and password")
        
        else:  # register mode
            st.markdown(f"""
                <div style="text-align: center; margin: 1.5rem 0;">
                    <h3 style="color: #43A047; margin-top: 0.5rem;">{t("create_account")}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            with st.form("register_form"):
                st.markdown(f"<h4 style='color: #1a1a1a; font-weight: 700;'>{t("join_community")}</h4>", unsafe_allow_html=True)
                new_username = st.text_input(t("username"), placeholder=t("username"))
                new_email = st.text_input(t("email"), placeholder=t("email"))
                new_password = st.text_input(t("password"), type="password", placeholder=t("password"))
                confirm_password = st.text_input(t("confirm_password"), type="password", placeholder=t("confirm_password"))
                
                register_btn = st.form_submit_button(t("create_button"), use_container_width=True)
                
                if register_btn:
                    success, message = auth.register_user(new_username, new_email, new_password, confirm_password)
                    if success:
                        st.success(message)
                        st.info(t("create_account"))
                        st.session_state.auth_mode = "login"
                        st.rerun()
                    else:
                        st.error(message)
        
        st.markdown("---")
        st.markdown(f"""
            <div style="text-align: center; margin-top: 2rem;">
                <p style='color: #A5D6A7; font-size: 0.9rem; margin-bottom: 1rem;'>
                    {t("secure_data")}
                </p>
            </div>
        """, unsafe_allow_html=True)


def show_main_app():
    """Display main application"""
    
    lang = st.session_state.language
    t = lambda key: get_text(key, lang)
    
    # Language selector in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**{t('language')}**")
    selected_lang = st.sidebar.selectbox(
        t("select_language"),
        options=["en", "mr", "hi", "kn"],
        format_func=lambda x: {"en": "English", "mr": "मराठी", "hi": "हिंदी", "kn": "ಕನ್ನಡ"}[x],
        key="app_lang_selector",
        label_visibility="collapsed"
    )
    if selected_lang != st.session_state.language:
        st.session_state.language = selected_lang
        st.rerun()
    
    st.sidebar.markdown("---")
    
    # User info and logout in sidebar with decorative styling
    st.sidebar.markdown(f"""
        <div style="text-align: center; padding: 1rem;">
            <p style="color: #43A047; font-size: 1.1rem; font-weight: 600; margin: 0;">
                {st.session_state.username}
            </p>
            <p style="color: #A5D6A7; font-size: 0.85rem; margin: 0.5rem 0 0 0;">{t("logged_in")}</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button(t("profile"), use_container_width=True):
            st.session_state.current_page = "profile"
    with col2:
        if st.button(t("logout"), use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
    
    st.markdown("---")
    
    # Header with decorative elements
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 class="header">{t("detection_system")}</h1>
            <p style="text-align: center; color: #A5D6A7; font-size: 1.1rem;">
                {t("identify_diseases")}
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title(t("configuration"))
    st.sidebar.markdown("---")

    # Load Model Section with styled header
    st.sidebar.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(67, 160, 71, 0.1) 0%, rgba(67, 160, 71, 0.05) 100%); 
                    border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
            <h4 style="color: #43A047; margin-top: 0;">{t("model_config")}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    model_path = st.sidebar.text_input(
        t("model_path"),
        value="crop_disease_model.h5",
        help="Path to your pre-trained TensorFlow model"
    )

    if st.sidebar.button(t("load_model"), use_container_width=True):
        with st.spinner(t("loading_model")):
            try:
                model_handler = ModelHandler(model_path)
                st.session_state.model_loaded = model_handler.model is not None
                if st.session_state.model_loaded:
                    st.sidebar.success(t("model_success"))
                else:
                    st.sidebar.warning(t("demo_mode"))
                    st.session_state.model_loaded = False
            except Exception as e:
                st.sidebar.error(f"Error loading model: {str(e)}")
                st.session_state.model_loaded = False

    confidence_threshold = st.sidebar.slider(
        t("confidence_threshold"),
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="Minimum confidence score to display prediction"
    )

    st.sidebar.markdown("---")
    st.sidebar.subheader(t("about"))
    st.sidebar.info(t("app_info"))

    # Main content
    tab1, tab2, tab3, tab4 = st.tabs([t("upload_image"), t("webcam"), t("information"), t("history")])

    # Tab 1: Upload Image
    with tab1:
        st.subheader(t("upload_crop_image"))
        
        uploaded_file = st.file_uploader(
            t("choose_image"),
            type=["jpg", "jpeg", "png", "bmp"],
            help=t("upload_help")
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Original Image**")
                image = Image.open(uploaded_file)
                st.image(image, use_column_width=True)
            
            # Analyze image
            if st.button("Analyze Image", key="analyze_btn"):
                with st.spinner("Analyzing image..."):
                    try:
                        # Preprocess image (PIL Image passed directly)
                        processed_img = preprocess_image(image)
                        
                        # Get predictions
                        model_handler = ModelHandler(model_path) if not st.session_state.model_loaded else model_handler
                        disease_label, confidence = model_handler.predict(processed_img)
                        
                        st.session_state.predictions = {
                            'label': disease_label,
                            'confidence': confidence
                        }
                        
                        # Save analysis to user history
                        auth.save_analysis(st.session_state.username, disease_label, confidence)
                        
                        # Display results
                        with col2:
                            st.markdown("**Analysis Results**")
                            st.metric("Disease", disease_label)
                            st.metric("Confidence", f"{confidence:.2%}")
                            
                            if confidence >= confidence_threshold:
                                st.success("Prediction confidence is good!")
                            else:
                                st.warning(f"Confidence below threshold ({confidence_threshold:.0%}). Consider uploading a clearer image.")
                        
                        # Disease information
                        disease_info = get_disease_info(disease_label)
                        if disease_info:
                            st.markdown("---")
                            st.markdown("### Disease Information")
                            col1, col2 = st.columns(2)
                            with col1:
                                st.info(f"**Description:** {disease_info['description']}")
                            with col2:
                                st.info(f"**Recommendation:** {disease_info['treatment']}")
                            
                    except Exception as e:
                        st.error(f"Error during analysis: {str(e)}")

    # Tab 2: Webcam Capture
    with tab2:
        st.subheader("Capture Image from Webcam")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Camera Feed**")
            camera_input = st.camera_input("Take a picture")
        
        if camera_input is not None:
            with col2:
                st.markdown("**Captured Image**")
                st.image(camera_input)
                
                if st.button("Analyze Webcam Image", key="analyze_webcam"):
                    with st.spinner("Analyzing captured image..."):
                        try:
                            # Convert captured image to array
                            image = Image.open(camera_input)
                            processed_img = preprocess_image(image)
                            
                            # Get predictions
                            model_handler = ModelHandler(model_path)
                            disease_label, confidence = model_handler.predict(processed_img)
                            
                            # Save analysis to user history
                            auth.save_analysis(st.session_state.username, disease_label, confidence)
                            
                            # Display results
                            st.markdown("---")
                            st.markdown("### Analysis Results")
                            col_res1, col_res2 = st.columns(2)
                            
                            with col_res1:
                                st.metric("Disease", disease_label)
                            with col_res2:
                                st.metric("Confidence", f"{confidence:.2%}")
                            
                            # Disease information
                            disease_info = get_disease_info(disease_label)
                            if disease_info:
                                st.markdown("---")
                                st.markdown("### Disease Information")
                                st.info(f"**Description:** {disease_info['description']}")
                                st.success(f"**Treatment:** {disease_info['treatment']}")
                                
                        except Exception as e:
                            st.error(f"Error analyzing webcam image: {str(e)}")

    # Tab 3: Information & Guide
    with tab3:
        st.subheader("How to Use This App")
        
        st.markdown("""
        ### 🌾 Crop Disease Detection Guide
        
        **Step 1: Prepare Your Image**
        - Take a clear photo of the affected crop
        - Ensure good lighting
        - Include the diseased area in the frame
        
        **Step 2: Upload or Capture**
        - Choose between uploading an existing image or capturing from webcam
        - Use the "Upload Image" tab for saved photos
        - Use the "Webcam Capture" tab for real-time photography
        
        **Step 3: Analyze**
        - Click the "Analyze Image" button
        - Wait for the AI model to process the image
        
        **Step 4: Review Results**
        - Check the detected disease type
        - Review the confidence score
        - Read treatment recommendations
        
        ### 🎯 Supported Diseases
        """)
        
        # Display disease database
        disease_db = {
            "Healthy": {"description": "No disease detected", "treatment": "Continue regular maintenance"},
            "Early Blight": {"description": "Fungal disease affecting tomato leaves", "treatment": "Use fungicides, remove affected leaves"},
            "Late Blight": {"description": "Severe fungal infection in potatoes/tomatoes", "treatment": "Apply copper-based fungicides"},
            "Powdery Mildew": {"description": "White powdery coating on leaves", "treatment": "Use sulfur-based treatments"},
            "Leaf Spot": {"description": "Dark spots on crop leaves", "treatment": "Remove infected leaves, improve air circulation"},
        }
        
        for disease, info in disease_db.items():
            with st.expander(f"{disease}"):
                st.write(f"**Description:** {info['description']}")
                st.write(f"**Treatment:** {info['treatment']}")
        
        st.markdown("---")
        st.markdown("""
            ### Model Information
            - **Input Size:** 224x224 pixels
            - **Framework:** TensorFlow/Keras
            - **Output:** Disease classification with confidence score
            
            ### Tips for Best Results
            - Use natural lighting
            - Avoid shadows and reflections
            - Capture the entire diseased area
            - Use high-resolution images when possible
            """)

    # Tab 4: Analysis History
    with tab4:
        st.subheader("Your Analysis History")
        
        user_info = auth.get_user_info(st.session_state.username)
        
        if user_info:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Analyses", user_info.get('total_analyses', 0))
            with col2:
                st.metric("Account Created", user_info.get('created_at', 'N/A'))
            with col3:
                st.metric("Email", user_info.get('email', 'N/A'))
        
        st.markdown("---")
        
        history = auth.get_user_history(st.session_state.username, limit=20)
        
        if history:
            st.write(f"Recent Analyses ({len(history)} records)")
            
            # Create a table of analyses
            for i, analysis in enumerate(history, 1):
                col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
                
                with col1:
                    st.text(analysis.get('timestamp', 'N/A'))
                with col2:
                    st.text(analysis.get('disease', 'N/A'))
                with col3:
                    confidence = analysis.get('confidence', 0)
                    st.text(f"{confidence:.1%}")
                with col4:
                    st.caption(f"#{i}")
        else:
            st.info("No analysis history yet. Start analyzing crop images!")

    # Footer with creative design
    st.markdown("---")
    st.markdown(f"""
        <div style="text-align: center; padding: 2rem 1rem; background: linear-gradient(180deg, rgba(67, 160, 71, 0.05) 0%, rgba(67, 160, 71, 0.02) 100%); border-radius: 10px; margin-top: 2rem;">
            <h4 style="color: #43A047; margin: 0.5rem 0;">Crop Disease Detection System v1.0</h4>
            <p style="color: #A5D6A7; margin: 0.3rem 0; font-size: 0.95rem;">AI-Powered Agricultural Health Monitoring</p>
            <hr style="margin: 1rem 0; opacity: 0.3;">
            <p style="color: #A5D6A7; margin: 0; font-size: 0.85rem;">
                <strong>User:</strong> {st.session_state.username} | 
                <strong>Purpose:</strong> Crop Health Monitoring
            </p>
            <p style="color: #81C784; margin-top: 0.8rem; font-size: 0.8rem; opacity: 0.8;">
                Developed for precision agriculture and sustainable farming practices
            </p>
        </div>
    """, unsafe_allow_html=True)


# Main app logic
if st.session_state.logged_in:
    show_main_app()
else:
    show_login_page()
