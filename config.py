"""
Configuration file for Crop Disease Detection App
Customize these settings to match your model and requirements
"""

# Model Configuration
MODEL_PATH = "crop_disease_model.h5"
MODEL_INPUT_SIZE = (224, 224)  # (height, width)
MODEL_FRAMEWORK = "tensorflow"

# Disease Classes - Update according to your model
DISEASE_CLASSES = [
    "Healthy",
    "Early Blight",
    "Late Blight",
    "Powdery Mildew",
    "Leaf Spot",
    "Rust"
]

# Confidence Threshold (0.0 - 1.0)
MIN_CONFIDENCE_THRESHOLD = 0.5

# Image Upload Settings
ALLOWED_IMAGE_FORMATS = ["jpg", "jpeg", "png", "bmp"]
MAX_UPLOAD_SIZE_MB = 10

# Display Settings
APP_TITLE = "Crop Disease Detection System"
APP_ICON = "🌾"

# Preprocessing Settings
IMAGE_NORMALIZATION = True
NORMALIZE_VALUE = 255.0

# Disease Information Database
DISEASE_INFO_DB = {
    "Healthy": {
        "description": "The crop appears to be healthy with no visible disease symptoms.",
        "treatment": "Continue regular crop maintenance and monitoring.",
        "severity": "None",
        "common_crops": ["All"]
    },
    "Early Blight": {
        "description": "Fungal disease affecting primarily lower leaves. Causes brown spots with concentric rings.",
        "treatment": "Remove affected leaves, improve air circulation, apply copper-based fungicides.",
        "severity": "Medium",
        "common_crops": ["Tomato", "Potato"]
    },
    "Late Blight": {
        "description": "Severe fungal infection that can quickly spread. Causes water-soaked spots on leaves and stems.",
        "treatment": "Apply copper or mancozeb fungicides immediately, remove infected plants.",
        "severity": "High",
        "common_crops": ["Tomato", "Potato"]
    },
    "Powdery Mildew": {
        "description": "Fungal disease causing white powdery coating on leaves, stems, and flowers.",
        "treatment": "Use sulfur-based fungicides, improve air circulation, reduce humidity.",
        "severity": "Medium",
        "common_crops": ["Cucumber", "Squash", "Beans"]
    },
    "Leaf Spot": {
        "description": "Various fungal or bacterial diseases causing dark spots on leaves with yellow halos.",
        "treatment": "Remove infected leaves, apply appropriate fungicides, ensure good drainage.",
        "severity": "Low-Medium",
        "common_crops": ["Beet", "Carrot", "Lettuce"]
    },
    "Rust": {
        "description": "Fungal disease causing rusty-brown pustules on the underside of leaves.",
        "treatment": "Apply sulfur or copper fungicides, improve air circulation, remove infected leaves.",
        "severity": "Medium",
        "common_crops": ["Beans", "Corn"]
    }
}

# Logging Settings
ENABLE_LOGGING = True
LOG_FILE = "app_logs.txt"

# Demo Mode Settings (when model is not available)
DEMO_MODE_ENABLED = True
DEMO_PREDICTIONS = [
    ("Healthy", 0.92),
    ("Early Blight", 0.87),
    ("Late Blight", 0.79),
    ("Powdery Mildew", 0.85),
    ("Leaf Spot", 0.81),
]
