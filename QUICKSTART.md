# 🌾 Quick Start Guide

## 5-Minute Setup

### Step 1: Navigate to the Project Directory
```bash
cd "d:\MIT\Python\Sharvari\Python workspace\crop_disease_detection_app"
```

### Step 2: Install Dependencies

**Option A: Automatic Setup (Windows)**
```bash
run_app.bat
```
This will install dependencies and launch the app automatically.

**Option B: Automatic Setup (Linux/Mac)**
```bash
chmod +x run_app.sh
./run_app.sh
```

**Option C: Manual Setup**
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Step 3: Open Your Browser
The app will automatically open at `http://localhost:8501`

---

## First Time Using the App?

### Try in Demo Mode
1. **No model needed!** The app works in demo mode
2. Go to "📸 Upload Image" tab
3. Upload any crop/plant image
4. Click "🔍 Analyze Image"
5. See simulated results

### Add Your Own Model Later
1. Train or download a TensorFlow model
2. Save as `crop_disease_model.h5`
3. Place in the project folder
4. Click "🔄 Load/Reload Model" in the sidebar
5. Your model is ready to use!

---

## Project Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `model_handler.py` | Handles model loading and predictions |
| `utils.py` | Image preprocessing functions |
| `config.py` | Configuration settings |
| `requirements.txt` | Python dependencies |
| `setup.py` | Automated setup script |
| `run_app.bat` | Quick launcher (Windows) |
| `run_app.sh` | Quick launcher (Linux/Mac) |
| `README.md` | Complete documentation |

---

## Key Features

✨ **Easy to Use**
- Simple web interface
- No coding required
- Intuitive navigation

📸 **Multiple Input Methods**
- Upload images
- Capture from webcam
- Support for JPG, PNG, BMP

🤖 **AI-Powered**
- TensorFlow/Keras integration
- Real-time predictions
- Confidence scoring

📊 **Disease Detection**
- Early Blight
- Late Blight
- Powdery Mildew
- Leaf Spot
- Rust
- And more...

---

## Common Tasks

### Use Webcam
1. Go to "🎥 Webcam Capture" tab
2. Click camera icon
3. Capture image
4. Click "🔍 Analyze Webcam Image"

### Upload Image
1. Go to "📸 Upload Image" tab
2. Click "Browse files"
3. Select image
4. Click "🔍 Analyze Image"

### Load Your Model
1. Click "Load/Reload Model" in sidebar
2. Enter path to your model
3. Wait for confirmation
4. Model is ready!

### Search Diseases
1. Go to "📊 Information" tab
2. Expand any disease section
3. View description and treatment

---

## Troubleshooting

### Issue: "Model file not found"
**Solution:** The app is in demo mode. Upload an image to test!

### Issue: Webcam not working
**Solution:** 
- Check camera permissions
- Try different browser
- Ensure no other app uses camera

### Issue: Slow predictions
**Solution:**
- Reduce image resolution
- Close other applications
- Check Python version (3.8+)

### Issue: Dependencies won't install
**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

---

## Next Steps

1. ✅ Run the app in demo mode
2. ✅ Test with sample images
3. 📚 Read disease information
4. 🤖 Train your own model
5. 📤 Add your model to the app
6. 🚀 Deploy for production

---

## Need Help?

- Check `README.md` for detailed documentation
- Review `config.py` for configuration options
- Examine `model_handler.py` for model integration details

---

**Ready to detect crop diseases?** 🌾  
Launch the app: `streamlit run app.py`
