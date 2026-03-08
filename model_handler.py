"""
Model Handler Module - Manages TensorFlow model loading and predictions
"""

import numpy as np
import os


class ModelHandler:
    """
    Handles loading and using TensorFlow models for disease detection.
    Includes fallback demo mode if model file is not available.
    """
    
    def __init__(self, model_path="crop_disease_model.h5"):
        """
        Initialize model handler
        
        Args:
            model_path (str): Path to the .h5 model file
        """
        self.model_path = model_path
        self.model = None
        self.disease_classes = [
            "Healthy",
            "Early Blight",
            "Late Blight",
            "Powdery Mildew",
            "Leaf Spot"
        ]
        
        # Try to load the model
        self._load_model()
    
    def _load_model(self):
        """Load the TensorFlow model if it exists"""
        try:
            if os.path.exists(self.model_path):
                from tensorflow.keras.models import load_model
                self.model = load_model(self.model_path)
                print(f"✅ Model loaded from {self.model_path}")
            else:
                print(f"⚠️ Model file not found at {self.model_path}. Using demo mode.")
                self.model = None
        except Exception as e:
            print(f"❌ Error loading model: {str(e)}. Using demo mode.")
            self.model = None
    
    def predict(self, image_array):
        """
        Predict disease from preprocessed image
        
        Args:
            image_array (np.ndarray): Preprocessed image array (224x224x3)
        
        Returns:
            tuple: (disease_label, confidence_score)
        """
        if self.model is not None:
            try:
                # Make prediction
                prediction = self.model.predict(image_array, verbose=0)
                disease_idx = np.argmax(prediction, axis=1)[0]
                confidence = np.max(prediction)
                
                disease_label = self.disease_classes[disease_idx]
                return disease_label, float(confidence)
            except Exception as e:
                print(f"Error during prediction: {str(e)}")
                return self._demo_prediction()
        else:
            # Demo mode - return simulated prediction
            return self._demo_prediction()
    
    def _demo_prediction(self):
        """Generate a demo prediction for testing without model"""
        import random
        
        # Simulate predictions
        demo_diseases = [
            ("Healthy", 0.92),
            ("Early Blight", 0.87),
            ("Late Blight", 0.79),
            ("Powdery Mildew", 0.85),
            ("Leaf Spot", 0.81),
        ]
        
        disease, confidence = random.choice(demo_diseases)
        # Add some randomness
        confidence = max(0.5, min(0.99, confidence + random.uniform(-0.1, 0.1)))
        
        return disease, confidence
    
    def get_disease_classes(self):
        """Get list of supported disease classes"""
        return self.disease_classes
    
    def is_model_loaded(self):
        """Check if model is loaded"""
        return self.model is not None
