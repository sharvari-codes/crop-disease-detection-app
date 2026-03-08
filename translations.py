"""
Language Translation Module
Supports: English, Marathi, Hindi
"""

TRANSLATIONS = {
    "en": {
        # Login & Auth
        "secure_login": "Secure Login",
        "welcome_back": "Welcome back!",
        "username": "Username",
        "password": "Password",
        "login": "Login",
        "register": "Register",
        "create_account": "Create Your Account",
        "join_community": "Join our farming community!",
        "email": "Email",
        "confirm_password": "Confirm Password",
        "create_button": "Create Account",
        
        # Main App
        "crop_disease_detection": "Crop Disease Detection",
        "detection_system": "Crop Disease Detection System",
        "ai_health_monitoring": "AI-Powered Agricultural Health Monitoring System",
        "identify_diseases": "Identify crop diseases using AI-powered image analysis",
        
        # Tabs
        "upload_image": "📸 Upload Image",
        "webcam": "📷 Webcam Capture",
        "information": "ℹ️ Information",
        "history": "📊 Analysis History",
        
        # Upload Tab
        "upload_crop_image": "Upload Crop Image",
        "choose_image": "Choose an image file",
        "upload_help": "Upload a clear image of the affected crop",
        "analyze": "🔍 Analyze Image",
        
        # Configuration
        "configuration": "Configuration",
        "model_config": "Model Configuration",
        "model_path": "Model File Path (.h5)",
        "load_model": "Load/Reload Model",
        "confidence_threshold": "Confidence Threshold",
        "about": "About",
        
        # Messages
        "processing": "Processing...",
        "loading_model": "Loading model...",
        "model_success": "Model loaded successfully!",
        "demo_mode": "Using demo mode (no model file found)",
        "upload_error": "Error uploading image",
        "select_image": "Please select an image first",
        
        # Disease Info
        "disease": "Disease",
        "confidence": "Confidence",
        "severity": "Severity",
        "treatment": "Treatment",
        "description": "Description",
        "healthy": "Healthy",
        "early_blight": "Early Blight",
        "late_blight": "Late Blight",
        "powdery_mildew": "Powdery Mildew",
        "leaf_spot": "Leaf Spot",
        "rust": "Rust",
        
        # Profile
        "profile": "Profile",
        "logout": "Logout",
        "logged_in": "Logged In",
        
        # Footer
        "secure_data": "Your data is secure with bcrypt password hashing",
        "app_info": "This app uses deep learning to detect crop diseases from images. Upload an image or use your webcam. The AI will analyze and predict diseases. Get recommendations for treatment.",
        
        # Language
        "language": "🌐 Language",
        "select_language": "Select Language",
    },
    
    "mr": {
        # Login & Auth
        "secure_login": "सुरक्षित लॉगिन",
        "welcome_back": "पुन्हा स्वागतम!",
        "username": "वापरकर्ता नाव",
        "password": "पासवर्ड",
        "login": "लॉगिन",
        "register": "नोंदणी",
        "create_account": "आपले खाते तयार करा",
        "join_community": "आमच्या शेती समुदायात सामील व्हा!",
        "email": "ईमेल",
        "confirm_password": "पासवर्ड पुष्टी करा",
        "create_button": "खाते तयार करा",
        
        # Main App
        "crop_disease_detection": "पिक रोग शोध",
        "detection_system": "पिक रोग शोध प्रणाली",
        "ai_health_monitoring": "कृत्रिम बुद्धिमत्ता-चालित कृषी स्वास्थ्य निरीक्षण प्रणाली",
        "identify_diseases": "AI-संचालित प्रतिमा विश्लेषण वापरून पिक रोग ओळखा",
        
        # Tabs
        "upload_image": "📸 प्रतिमा अपलोड करा",
        "webcam": "📷 वेबकैम कॅप्चर",
        "information": "ℹ️ माहिती",
        "history": "📊 विश्लेषण इतिहास",
        
        # Upload Tab
        "upload_crop_image": "पिकाची प्रतिमा अपलोड करा",
        "choose_image": "प्रतिमा फाइल निवडा",
        "upload_help": "प्रभावित पिकाची स्पष्ट प्रतिमा अपलोड करा",
        "analyze": "🔍 प्रतिमा विश्लेषण करा",
        
        # Configuration
        "configuration": "कॉन्फिगरेशन",
        "model_config": "मॉडेल कॉन्फिगरेशन",
        "model_path": "मॉडेल फाइल पाथ (.h5)",
        "load_model": "मॉडेल लोड/रीलोड करा",
        "confidence_threshold": "विश्वास थ्रेशोल्ड",
        "about": "विषय",
        
        # Messages
        "processing": "प्रक्रिया चल रही आहे...",
        "loading_model": "मॉडेल लोड होत आहे...",
        "model_success": "मॉडेल यशस्वीरित्या लोड झाला!",
        "demo_mode": "डेमो मोड वापरत आहे (मॉडेल फाइल आढळली नाही)",
        "upload_error": "प्रतिमा अपलोड करण्यात त्रुटी",
        "select_image": "कृपया प्रथम प्रतिमा निवडा",
        
        # Disease Info
        "disease": "रोग",
        "confidence": "विश्वास",
        "severity": "गंभीरता",
        "treatment": "उपचार",
        "description": "वर्णन",
        "healthy": "स्वस्थ",
        "early_blight": "सुरुवातीचा अंगमारा",
        "late_blight": "उशीरा अंगमारा",
        "powdery_mildew": "पावडरी का",
        "leaf_spot": "पत्र्याचा डाग",
        "rust": "जंग",
        
        # Profile
        "profile": "प्रोफाइल",
        "logout": "बाहेर पडा",
        "logged_in": "लॉगिन केलेले",
        
        # Footer
        "secure_data": "आपला डेटा bcrypt पासवर्ड हॅशिंग सह सुरक्षित आहे",
        "app_info": "हा अ‍ॅप प्रतिमांपासून पिक रोग शोधण्यासाठी गहन शिक्षण वापरतो. प्रतिमा अपलोड करा किंवा आपल्या वेबकैमचा वापर करा. AI विश्लेषण करेल आणि रोगांचा अचूक अंदाज लावेल. उपचारासाठी शिफारसी मिळवा.",
        
        # Language
        "language": "🌐 भाषा",
        "select_language": "भाषा निवडा",
    },
    
    "hi": {
        # Login & Auth
        "secure_login": "सुरक्षित लॉगिन",
        "welcome_back": "स्वागत है!",
        "username": "उपयोगकर्ता नाम",
        "password": "पासवर्ड",
        "login": "लॉगिन",
        "register": "पंजीकरण",
        "create_account": "अपना खाता बनाएं",
        "join_community": "हमारे कृषि समुदाय में शामिल हों!",
        "email": "ईमेल",
        "confirm_password": "पासवर्ड की पुष्टि करें",
        "create_button": "खाता बनाएं",
        
        # Main App
        "crop_disease_detection": "फसल रोग पहचान",
        "detection_system": "फसल रोग पहचान प्रणाली",
        "ai_health_monitoring": "कृत्रिम बुद्धिमत्ता द्वारा संचालित कृषि स्वास्थ्य निगरानी प्रणाली",
        "identify_diseases": "AI-संचालित छवि विश्लेषण का उपयोग करके फसल रोगों की पहचान करें",
        
        # Tabs
        "upload_image": "📸 छवि अपलोड करें",
        "webcam": "📷 वेबकैम कैप्चर",
        "information": "ℹ️ जानकारी",
        "history": "📊 विश्लेषण इतिहास",
        
        # Upload Tab
        "upload_crop_image": "फसल की छवि अपलोड करें",
        "choose_image": "एक छवि फाइल चुनें",
        "upload_help": "प्रभावित फसल की स्पष्ट छवि अपलोड करें",
        "analyze": "🔍 छवि का विश्लेषण करें",
        
        # Configuration
        "configuration": "कॉन्फ़िगरेशन",
        "model_config": "मॉडल कॉन्फ़िगरेशन",
        "model_path": "मॉडल फाइल पाथ (.h5)",
        "load_model": "मॉडल लोड/रीलोड करें",
        "confidence_threshold": "आत्मविश्वास थ्रेशोल्ड",
        "about": "परिचय",
        
        # Messages
        "processing": "प्रक्रिया चल रही है...",
        "loading_model": "मॉडल लोड हो रहा है...",
        "model_success": "मॉडल सफलतापूर्वक लोड हो गया!",
        "demo_mode": "डेमो मोड का उपयोग कर रहे हैं (मॉडल फाइल नहीं मिली)",
        "upload_error": "छवि अपलोड करने में त्रुटि",
        "select_image": "कृपया पहले एक छवि चुनें",
        
        # Disease Info
        "disease": "रोग",
        "confidence": "आत्मविश्वास",
        "severity": "गंभीरता",
        "treatment": "उपचार",
        "description": "विवरण",
        "healthy": "स्वस्थ",
        "early_blight": "प्रारंभिक अंगमारी",
        "late_blight": "देर से अंगमारी",
        "powdery_mildew": "पाउडरी फफूंद",
        "leaf_spot": "पत्ती धब्बा",
        "rust": "जंग",
        
        # Profile
        "profile": "प्रोफाइल",
        "logout": "लॉग आउट",
        "logged_in": "लॉगिन किया गया",
        
        # Footer
        "secure_data": "आपका डेटा bcrypt पासवर्ड हैशिंग के साथ सुरक्षित है",
        "app_info": "यह ऐप छवियों से फसल रोगों की पहचान करने के लिए गहन शिक्षण का उपयोग करता है। छवि अपलोड करें या अपने वेबकैम का उपयोग करें। AI विश्लेषण करेगा और रोगों की भविष्यवाणी करेगा। उपचार के लिए सिफारिशें प्राप्त करें।",
        
        # Language
        "language": "🌐 भाषा",
        "select_language": "भाषा चुनें",
    }
}

def get_text(key, language="en"):
    """Get translated text for a key"""
    if language not in TRANSLATIONS:
        language = "en"
    
    return TRANSLATIONS[language].get(key, TRANSLATIONS["en"].get(key, key))

def get_all_translations(language="en"):
    """Get all translations for a language"""
    if language not in TRANSLATIONS:
        language = "en"
    return TRANSLATIONS[language]
