"""
Quick Setup and Installation Script
Run this to set up the Crop Disease Detection app
"""

import os
import subprocess
import sys


def install_dependencies():
    """Install required packages"""
    print("\n" + "="*50)
    print("Installing dependencies...")
    print("="*50 + "\n")
    
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("\n✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("\n❌ Failed to install dependencies")
        return False


def create_model_placeholder():
    """Create a placeholder for model file"""
    print("\n" + "="*50)
    print("Checking for model file...")
    print("="*50 + "\n")
    
    model_file = "crop_disease_model.h5"
    
    if os.path.exists(model_file):
        print(f"✅ Model file found: {model_file}")
    else:
        print(f"⚠️  Model file not found: {model_file}")
        print("    The app will run in DEMO MODE with simulated predictions")
        print("\n📌 To add your model:")
        print("    1. Train a TensorFlow model with disease classification")
        print("    2. Save it as 'crop_disease_model.h5'")
        print("    3. Place it in this directory")
        print("    4. Restart the app and load the model from sidebar")


def check_python_version():
    """Check if Python version is compatible"""
    print("\n" + "="*50)
    print("Checking Python version...")
    print("="*50 + "\n")
    
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 8:
        print("✅ Python version compatible!")
        return True
    else:
        print("❌ Python 3.8 or higher required")
        return False


def launch_app():
    """Launch the Streamlit app"""
    print("\n" + "="*50)
    print("Launching Crop Disease Detection App...")
    print("="*50 + "\n")
    
    print("The app will open at: http://localhost:8501")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.call(["streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n\n✅ App closed successfully")
    except FileNotFoundError:
        print("❌ Streamlit not found. Please ensure it's installed.")


def main():
    """Main setup function"""
    print("\n")
    print("🌾 "*15)
    print("CROP DISEASE DETECTION SYSTEM - SETUP")
    print("🌾 "*15)
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Setup failed: Incompatible Python version")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed: Could not install dependencies")
        sys.exit(1)
    
    # Check for model
    create_model_placeholder()
    
    # Ask to launch app
    print("\n" + "="*50)
    response = input("Launch the app now? (y/n): ").lower().strip()
    
    if response == 'y' or response == 'yes':
        launch_app()
    else:
        print("\n✅ Setup complete!")
        print("To launch the app later, run: streamlit run app.py")


if __name__ == "__main__":
    main()
