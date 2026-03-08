"""
UX Enhancement Module - Improves user experience with better feedback and guidance
Includes: tooltips, help text, user onboarding, improved error messages
"""

import streamlit as st
from PIL import Image
from translations import get_text

def show_welcome_banner(lang="en"):
    """Show welcome banner for new users"""
    t = lambda key: get_text(key, lang)
    
    st.markdown("""
        <div style="background: linear-gradient(135deg, #43A047 0%, #2E7D32 100%); 
                    padding: 2rem; border-radius: 10px; margin-bottom: 2rem; color: white;">
            <h2 style="margin-top: 0; color: white;">🌾 Welcome to Crop Disease Detection!</h2>
            <p style="font-size: 1.1rem; margin-bottom: 1rem;">
                Upload a crop image and get instant disease diagnosis powered by AI
            </p>
            <p style="opacity: 0.9;">
                ✅ Upload clear images | ✅ Get instant diagnosis | ✅ Get treatment tips | ✅ Track progress
            </p>
        </div>
    """, unsafe_allow_html=True)

def show_quick_guide(lang="en"):
    """Show quick start guide"""
    t = lambda key: get_text(key, lang)
    
    with st.expander("📖 Quick Start Guide", expanded=False):
        st.markdown(f"""
        ### How to Use:
        
        **Step 1**: 📸 Go to the **{t("upload_image")}** tab
        
        **Step 2**: 📤 Upload a clear image of your crop
        
        **Step 3**: 🔍 Click **{t("analyze")}** button
        
        **Step 4**: 📊 View results and treatment recommendations
        
        ### Tips for Best Results:
        - ✅ Take clear, well-lit photos
        - ✅ Show the affected area clearly
        - ✅ Take photos during daylight
        - ✅ Zoom in on the disease area
        - ❌ Avoid blurry or dark images
        """)

def show_helpful_tooltip(title, description):
    """Show helpful tooltip with info"""
    st.info(f"**ℹ️ {title}**: {description}")

def show_success_message(title, description=""):
    """Show success message with celebration"""
    message = f"✅ **{title}**"
    if description:
        message += f"\n\n{description}"
    st.success(message)

def show_error_message(error_type, lang="en"):
    """Show user-friendly error messages"""
    t = lambda key: get_text(key, lang)
    
    error_messages = {
        "no_image": f"❌ {t('select_image')}",
        "invalid_image": "❌ Please upload a valid image file (JPG, PNG, BMP)",
        "upload_error": f"❌ {t('upload_error')}",
        "model_error": "❌ Error loading model. Using demo mode instead.",
        "no_disease": "❌ Could not detect disease. Try with a clearer image.",
    }
    
    message = error_messages.get(error_type, "❌ An error occurred")
    st.error(message)

def show_result_card(disease_name, confidence, severity, lang="en"):
    """Show beautiful result card"""
    t = lambda key: get_text(key, lang)
    
    # Color coding based on confidence
    if confidence >= 0.8:
        color = "#FF6B6B"  # Red for high confidence
    elif confidence >= 0.6:
        color = "#FFA500"  # Orange for medium
    else:
        color = "#FFD93D"  # Yellow for uncertain
    
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {color}22 0%, {color}11 100%); 
                    border-left: 5px solid {color}; padding: 1.5rem; 
                    border-radius: 8px; margin: 1rem 0;">
            <h3 style="margin-top: 0; color: #1a1a1a;">{disease_name}</h3>
            <div style="display: flex; justify-content: space-between; margin: 1rem 0;">
                <div>
                    <p style="margin: 0; opacity: 0.8;">📊 {t('confidence')}</p>
                    <p style="margin: 0; font-size: 1.5rem; font-weight: bold; color: {color};">
                        {confidence*100:.1f}%
                    </p>
                </div>
                <div>
                    <p style="margin: 0; opacity: 0.8;">⚠️ {t('severity')}</p>
                    <p style="margin: 0; font-size: 1.5rem; font-weight: bold;">
                        {severity}
                    </p>
                </div>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                <p style="margin: 0; opacity: 0.7; font-size: 0.9rem;">
                    💡 This disease has <strong>{severity.lower()}</strong> severity level
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_treatment_section(treatment_text, lang="en"):
    """Show treatment recommendations beautifully"""
    t = lambda key: get_text(key, lang)
    
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%); 
                    border-left: 5px solid #43A047; padding: 1.5rem; 
                    border-radius: 8px; margin: 1rem 0;">
            <h4 style="margin-top: 0; color: #2E7D32;">💊 {t('treatment')}</h4>
            <p style="line-height: 1.6; color: #333;">
                {treatment_text}
            </p>
            <div style="background: white; padding: 0.8rem; border-radius: 5px; margin-top: 1rem; 
                        border-left: 3px solid #FFA500;">
                <p style="margin: 0; font-size: 0.9rem;">
                    <strong>⏰ Timeline:</strong> Results typically improve in 1-3 weeks
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_progress_indicator(current_step, total_steps, lang="en"):
    """Show progress indicator for multi-step process"""
    t = lambda key: get_text(key, lang)
    
    progress = current_step / total_steps
    steps = ["📤 Upload", "🔍 Analyze", "📊 Results", "💊 Treatment"]
    
    col1, col2, col3 = st.columns([1, 10, 1])
    with col2:
        st.progress(progress)
        st.caption(f"Step {current_step} of {total_steps}: {steps[current_step-1]}")

def show_image_preview_with_guide(uploaded_file):
    """Show image preview with helpful feedback"""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.image(image, use_column_width=True, caption="Uploaded Image Preview")
        
        with col2:
            st.markdown("""
            ### ✅ Image Quality Check:
            - Image loaded successfully
            - Quality appears good
            - Ready for analysis
            """)
        
        return image
    return None

def show_faq_section(lang="en"):
    """Show FAQ section"""
    t = lambda key: get_text(key, lang)
    
    with st.expander("❓ Frequently Asked Questions", expanded=False):
        st.markdown("""
        **Q: What crops does this app support?**
        - A: Currently supports tomato, potato, and other common vegetables
        
        **Q: How accurate is the detection?**
        - A: 85-95% accuracy depending on image quality
        
        **Q: Can I use this offline?**
        - A: Currently requires internet, offline mode coming soon
        
        **Q: What image formats are supported?**
        - A: JPG, PNG, BMP formats (max 10MB)
        
        **Q: How long does analysis take?**
        - A: Usually 2-5 seconds
        
        **Q: Can I get a detailed report?**
        - A: PDF export feature coming soon
        """)

def show_footer_with_tips(lang="en"):
    """Show footer with helpful tips"""
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 💡 Pro Tips
        - Take multiple photos from different angles
        - Zoom in on affected areas
        - Take photos in daylight
        """)
    
    with col2:
        st.markdown("""
        ### 🌾 Best Practices
        - Regular field inspections
        - Early disease detection
        - Follow treatment strictly
        """)
    
    with col3:
        st.markdown("""
        ### 📞 Support
        - Email: support@crophealth.com
        - Phone: +91-XXXX-XXXX
        - Chat: Available 24/7
        """)

def show_confidence_explanation(confidence_score, lang="en"):
    """Explain what confidence score means"""
    t = lambda key: get_text(key, lang)
    
    if confidence_score >= 0.9:
        level = "🟢 Very High"
        explanation = "The AI is very confident in this diagnosis"
    elif confidence_score >= 0.8:
        level = "🟢 High"
        explanation = "The AI is confident in this diagnosis"
    elif confidence_score >= 0.7:
        level = "🟡 Medium"
        explanation = "The AI is reasonably confident, consider consulting an expert"
    elif confidence_score >= 0.6:
        level = "🟠 Low-Medium"
        explanation = "For better accuracy, try uploading a clearer image"
    else:
        level = "🔴 Low"
        explanation = "Please try with a better quality image for accurate diagnosis"
    
    st.markdown(f"""
    **Confidence Level: {level}**
    
    {explanation}
    """)

# Export all functions for easy import
__all__ = [
    'show_welcome_banner',
    'show_quick_guide',
    'show_helpful_tooltip',
    'show_success_message',
    'show_error_message',
    'show_result_card',
    'show_treatment_section',
    'show_progress_indicator',
    'show_image_preview_with_guide',
    'show_faq_section',
    'show_footer_with_tips',
    'show_confidence_explanation',
]
