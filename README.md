# 🌾 Crop Disease Detection System

A prototype application for detecting crop diseases using deep learning and computer vision.

## Features

- **Multiple Input Methods**
  - Upload image files (JPG, PNG, BMP)
  - Capture images using webcam
  
- **AI-Powered Analysis**
  - Real-time disease classification
  - Confidence scoring
  - Disease information and treatment recommendations

- **User-Friendly Interface**
  - Web-based UI using Streamlit
  - Responsive design
  - Easy navigation with tabs

- **🌐 Multi-Language Support** ⭐ NEW
  - **English** (Default)
  - **Marathi** (मराठी)
  - **Hindi** (हिंदी)
  - **Kannada** (ಕನ್ನಡ) ✨ NEW
  - Switch languages anytime in the app
  - Perfect for Indian farmers and agricultural experts

- **Supported Diseases**
  - Healthy crops
  - Early Blight
  - Late Blight
  - Powdery Mildew
  - Leaf Spot
  - Rust

## Requirements

- Python 3.8 or higher
- TensorFlow 2.14+
- OpenCV
- Streamlit
- NumPy
- Pillow

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install streamlit==1.28.1 opencv-python==4.8.1.78 tensorflow==2.14.0 numpy==1.24.3 pillow==10.0.1
```

### 2. Prepare Your Model

Place your pre-trained TensorFlow model file in the project directory:
```
crop_disease_detection_app/
├── crop_disease_model.h5  (your trained model)
├── app.py
├── model_handler.py
├── utils.py
└── requirements.txt
```

**Model Requirements:**
- Input shape: 224x224x3 (RGB images)
- Output shape: Number of disease classes
- Format: TensorFlow .h5 format

## Running the Application

### Start the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

### Demo Mode

If you don't have a trained model yet, the app will run in **demo mode** with simulated predictions. This allows you to test the interface and workflow.

## Usage

### Option 1: Upload Image
1. Go to "📸 Upload Image" tab
2. Click "Browse files" and select an image
3. Click "🔍 Analyze Image"
4. Review the results and treatment recommendations

### Option 2: Webcam Capture
1. Go to "🎥 Webcam Capture" tab
2. Click "Take a picture" button
3. Position the crop clearly in the frame and capture
4. Click "🔍 Analyze Webcam Image"
5. Review the results

### Option 3: Learn More
- Visit "📊 Information" tab for usage guide and disease information

## Project Structure

```
crop_disease_detection_app/
│
├── app.py                 # Main Streamlit application
├── model_handler.py       # Model loading and prediction
├── utils.py              # Utility functions for image processing
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## How It Works

1. **Image Input**: User uploads or captures a crop image
2. **Preprocessing**: Image is resized to 224x224 and normalized
3. **Model Prediction**: TensorFlow model classifies the disease
4. **Post-processing**: Confidence score is calculated
5. **Output**: Disease type, confidence, and treatment info are displayed

## Image Requirements for Best Results

- **Resolution**: 480p or higher
- **Lighting**: Natural daylight, avoid shadows
- **Focus**: Clearly visible diseased area
- **Background**: Minimal background distraction
- **Angle**: Direct view of affected leaves/areas

## Creating a Trained Model

To train your own model:

1. Collect disease image dataset
2. Split into train/validation/test sets
3. Use TensorFlow/Keras to build and train model
4. Save as .h5 format
5. Place in project directory

Example training structure:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2,2)),
    # ... more layers ...
    Dense(128, activation='relu'),
    Dense(5, activation='softmax')  # 5 disease classes
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_data, train_labels, epochs=20, validation_data=(val_data, val_labels))
model.save('crop_disease_model.h5')
```

## Configuration

### Model Path
In the sidebar, you can specify the path to your model:
- Default: `crop_disease_model.h5`
- Click "🔄 Load/Reload Model" to load a different model

### Confidence Threshold
Adjust the minimum confidence score (0.0 - 1.0) to filter predictions

## Troubleshooting

### Model not loading
- Check if `crop_disease_model.h5` exists in the project directory
- Verify the file path is correct
- Ensure the model is in TensorFlow 2.x format

### Webcam not working
- Check camera permissions
- Try a different browser
- Ensure no other app is using the camera

### Slow predictions
- Reduce image resolution
- Use GPU if available (CUDA)
- Check system resources

## Future Enhancements

- [ ] Batch image processing
- [ ] Model performance metrics
- [ ] Treatment severity levels
- [ ] Historical prediction tracking
- [ ] Multi-language support
- [ ] Export analysis reports
- [ ] Integration with weather data
- [ ] Mobile app version

## Notes

- This is a prototype application
- Always verify AI predictions with expert consultation
- Regularly update and retrain the model with new data
- Keep backup of trained models

## Contact & Support

For issues or improvements, please refer to documentation or consult with agricultural experts.

---

**Version**: 1.0  
**Last Updated**: 2026-03-08  
**Status**: Prototype

