# 🌐 Multi-Language Support Guide

## Supported Languages

The Crop Disease Detection App now supports **4 languages**:

| Language | Code | Status | Region |
|----------|------|--------|--------|
| **English** | `en` | ✅ Default | Universal |
| **Marathi** | `mr` | ✅ Supported | Maharashtra |
| **Hindi** | `hi` | ✅ Supported | North India |
| **Kannada** | `kn` | ✅ NEW | Karnataka |

---

## How to Change Language

### In Login Page
1. Look at the **top-right corner**
2. Find the **🌐 Language** dropdown
3. Select your preferred language:
   - **English** (English)
   - **मराठी** (Marathi)
   - **हिंदी** (Hindi)
   - **ಕನ್ನಡ** (Kannada) ✨ NEW
4. The entire login interface will update instantly

### In Main App
1. Once logged in, go to the **left sidebar**
2. Find **🌐 ಭಾಷೆ** (Language) selector
3. Select your language from the dropdown
4. All app content will switch to selected language instantly

### Kannada Language Specifics
- **Script**: Kannada (ಕನ್ನಡ) - Native script
- **Region**: Karnataka, South India
- **Speakers**: Farmers in Karnataka region
- **Features**: Full UI translation, disease names, treatment info

---

## What's Translated

### ✅ Fully Translated:
- Login & Registration forms
- All buttons and labels
- Sidebar menu items
- Tab names
- Disease names and descriptions
- Error and success messages
- Configuration options
- User profile section

### Example Translations:

| English | Marathi | Hindi | Kannada |
|---------|---------|-------|----------|
| Welcome back! | पुन्हा स्वागतम! | स्वागत है! | ಸ್ವಾಗತ! |
| Username | वापरकर्ता नाव | उपयोगकर्ता नाम | ಬಳಕೆದಾರ ಹೆಸರು |
| Password | पासवर्ड | पासवर्ड | ಪಾಸ್‌ವರ್ಡ್ |
| Upload Image | प्रतिमा अपलोड करा | छवि अपलोड करें | ಚಿತ್ರ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ |
| Analyze Image | प्रतिमा विश्लेषण करा | छवि का विश्लेषण करें | ಚಿತ್ರವನ್ನು ವಿಶ್ಲೇಷಿಸಿ |
| Crop Disease Detection | पिक रोग शोध | फसल रोग पहचान | ಬೆಳೆ ರೋಗ ಸನಿಹ |
| Disease | रोग | रोग | ರೋಗ |
| Treatment | उपचार | उपचार | ಚಿಕಿತ್ಸೆ |
| Healthy | स्वस्थ | स्वस्थ | ಆರೋಗ್ಯಕರ |

---

## How It Works

The language support is implemented using a `translations.py` module that:

1. **Stores all text** in a dictionary organized by language
2. **Provides a function** `get_text(key, language)` to retrieve translations
3. **Maintains session state** for language preference
4. **Includes language selector** in both login and main app

### Code Example:
```python
from translations import get_text

lang = st.session_state.language
text = get_text("welcome_back", lang)  # Returns translated text
```

---

## Adding New Translations

To add another language, edit `translations.py`:

```python
TRANSLATIONS = {
    "en": { ... },
    "mr": { ... },
    "hi": { ... },
    "your_lang_code": {
        "welcome_back": "Your translation here",
        "username": "Your translation",
        # ... add all keys
    }
}
```

Then add the language to the selector:
```python
{"en": "English", "mr": "मराठी", "hi": "हिंदी", "your_code": "Your Language"}
```

---

## Current Translation Keys

All available keys in the translation system:

### Authentication
- `secure_login`, `welcome_back`, `username`, `password`, `login`
- `register`, `create_account`, `join_community`, `email`
- `confirm_password`, `create_button`

### Main App
- `crop_disease_detection`, `detection_system`, `ai_health_monitoring`
- `identify_diseases`, `configuration`, `model_config`, `model_path`
- `load_model`, `confidence_threshold`, `about`

### Tabs
- `upload_image`, `webcam`, `information`, `history`

### Messages
- `processing`, `loading_model`, `model_success`, `demo_mode`
- `upload_error`, `select_image`

### Disease Info
- `disease`, `confidence`, `severity`, `treatment`, `description`
- `healthy`, `early_blight`, `late_blight`, `powdery_mildew`
- `leaf_spot`, `rust`

### Profile
- `profile`, `logout`, `logged_in`

### Language
- `language`, `select_language`

---

## Language Files

- **`translations.py`** - Main translation module with all language dictionaries
- **`app.py`** - Main app that uses translations (updated to support multi-lang)

---

## Kannada Language - Detailed Information

### About Kannada
- **Name**: ಕನ್ನಡ (Kannada)
- **Family**: Dravidian language family
- **Native Speakers**: ~60 million in Karnataka
- **Script**: Kannada script (ಕನ್ನಡ ಲಿಪಿ)
- **Region**: Karnataka State, South India
- **Agricultural Zone**: Tropical and subtropical crops

### Kannada Translations in the App

#### Login & Registration
| English | Kannada |
|---------|---------|
| Secure Login | ಸುರಕ್ಷಿತ ಲಾಗಿನ್ |
| Create Account | ನಿಮ್ಮ ಖಾತೆ ರಚಿಸಿ |
| Join our community | ನಮ್ಮ ಕೃಷಿ ಸಮುದಾಯಕ್ಕೆ ಸೇರಿಕೊಳ್ಳಿ |
| Username | ಬಳಕೆದಾರ ಹೆಸರು |
| Password | ಪಾಸ್‌ವರ್ಡ್ |

#### Disease Names (Kannada)
| English | Kannada |
|---------|---------|
| Early Blight | ಆರಂಭಿಕ ಅಂಗಮಾರ |
| Late Blight | ತಡವಾದ ಅಂಗಮಾರ |
| Powdery Mildew | ಪೌಡರಿ ಫಂಗಸ್ |
| Leaf Spot | ಎಲೆಯ ಚುಕ್ಕೆ |
| Rust | ಈರುಳ್ಳಿ |
| Healthy | ಆರೋಗ್ಯಕರ |

#### App Features (Kannada)
| English | Kannada |
|---------|---------|
| Upload Image | ಚಿತ್ರ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ |
| Analyze Image | ಚಿತ್ರವನ್ನು ವಿಶ್ಲೇಷಿಸಿ |
| Configuration | ಸಂರಚನೆ |
| Load Model | ಮಾದರಿ ಲೋಡ್ ಮಾಡಿ |
| Profile | ಪ್ರೊಫೈಲ್ |
| Logout | ಲಾಗ್ ಔಟ್ |
| Treatment | ಚಿಕಿತ್ಸೆ |

### Language Code Usage
```python
# Kannada language code
"kn"  # Represents Kannada language

# Full selector example
{"en": "English", "mr": "मराठी", "hi": "हिंदी", "kn": "ಕನ್ನಡ"}
```

---

## Tips

- ✅ Your language preference is saved for the session
- ✅ Change language anytime using the selector
- ✅ All interfaces update instantly
- ✅ Works offline (no internet required)

---

## Troubleshooting

**Q: Language selector not showing?**
- A: Make sure you're using the latest version of `app.py` with translations import

**Q: Text not translated?**
- A: Check that the key exists in `translations.py` for your language

**Q: Want to add more languages?**
- A: Edit `translations.py` and add your language code and translations

---

## Future Enhancements

Potential additions:
- [ ] More Indic languages (Tamil, Telugu, Bengali)
- [ ] Regional disease names in local languages
- [ ] Localized treatment recommendations
- [ ] Multi-language disease descriptions with regional variations
- [ ] Language preference saved in user profile
- [ ] Voice output for disease detection results
- [ ] Regional farming tips and seasonal advisories
- [ ] Integration with agricultural extension services per region

### Current Coverage
- **Total Languages**: 4 (English, Marathi, Hindi, Kannada)
- **Translation Keys**: 60+ UI elements and features
- **Disease Names**: All translated
- **Regional Support**: 4 major Indian states/regions

---

**Enjoy using the Crop Disease Detection App in your preferred language!** 🌾
✨ **Supporting Indian Farmers Across Multiple States in Their Native Languages!** ✨
