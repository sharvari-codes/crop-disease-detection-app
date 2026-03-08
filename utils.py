"""
Utility Functions - Image preprocessing and disease information
"""

import cv2
import numpy as np
from PIL import Image


def preprocess_image(image_input):
    """
    Preprocess image for model input
    
    Args:
        image_input: PIL Image or numpy array
    
    Returns:
        np.ndarray: Preprocessed image ready for model (1, 224, 224, 3)
    """
    # Validate input
    if image_input is None:
        raise ValueError("Image input cannot be None")
    
    # Convert PIL Image to numpy array if needed
    if isinstance(image_input, Image.Image):
        img = np.array(image_input)
    else:
        img = image_input
    
    # Check if image is empty
    if img is None or img.size == 0:
        raise ValueError("Image array is empty")
    
    # Ensure image is in RGB format
    if len(img.shape) == 2:  # Grayscale
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif len(img.shape) == 3 and img.shape[2] == 4:  # RGBA
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    
    # Resize to model input size
    img = cv2.resize(img, (224, 224))
    
    # Normalize pixel values
    img = img.astype(np.float32) / 255.0
    
    # Add batch dimension
    img = np.expand_dims(img, axis=0)
    
    return img


def get_disease_info(disease_name):
    """
    Get disease information and treatment recommendations
    
    Args:
        disease_name (str): Name of the disease
    
    Returns:
        dict: Disease information including description and treatment
    """
    disease_database = {
        "Healthy": {
            "description": "The crop appears to be healthy with no visible disease symptoms.",
            "treatment": "Continue regular crop maintenance and monitoring.",
            "severity": "None"
        },
        "Early Blight": {
            "description": "Fungal disease affecting primarily lower leaves. Causes brown spots with concentric rings.",
            "treatment": "Remove affected leaves, improve air circulation, apply copper-based fungicides, ensure proper spacing.",
            "severity": "Medium",
            "common_crops": ["Tomato", "Potato"]
        },
        "Late Blight": {
            "description": "Severe fungal infection that can quickly spread. Causes water-soaked spots on leaves and stems.",
            "treatment": "Apply copper or mancozeb fungicides immediately, remove infected plants, ensure good air circulation, avoid overhead watering.",
            "severity": "High",
            "common_crops": ["Tomato", "Potato"]
        },
        "Powdery Mildew": {
            "description": "Fungal disease causing white powdery coating on leaves, stems, and flowers.",
            "treatment": "Use sulfur-based fungicides, improve air circulation, reduce humidity, prune affected areas.",
            "severity": "Medium",
            "common_crops": ["Cucumber", "Squash", "Beans"]
        },
        "Leaf Spot": {
            "description": "Various fungal or bacterial diseases causing dark spots on leaves with yellow halos.",
            "treatment": "Remove infected leaves, apply appropriate fungicides, ensure good drainage, water at soil level only.",
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
    
    return disease_database.get(disease_name, {
        "description": "Unknown disease",
        "treatment": "consult with agricultural expert",
        "severity": "Unknown"
    })


def get_image_stats(image_array):
    """
    Get statistics about the image for quality assessment
    
    Args:
        image_array (np.ndarray): Image array
    
    Returns:
        dict: Image statistics
    """
    stats = {
        "shape": image_array.shape,
        "mean_pixel_value": np.mean(image_array),
        "std_pixel_value": np.std(image_array),
        "min_pixel_value": np.min(image_array),
        "max_pixel_value": np.max(image_array)
    }
    return stats


def calculate_confidence_level(confidence_score):
    """
    Categorize confidence score into levels
    
    Args:
        confidence_score (float): Confidence score (0-1)
    
    Returns:
        str: Confidence level
    """
    if confidence_score >= 0.9:
        return "Very High"
    elif confidence_score >= 0.8:
        return "High"
    elif confidence_score >= 0.7:
        return "Medium"
    elif confidence_score >= 0.6:
        return "Low"
    else:
        return "Very Low"
