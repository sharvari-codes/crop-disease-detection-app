# 🌐 Multi-Language Support Guide

## Supported Languages

The Crop Disease Detection App now supports **3 languages**:

| Language | Code | Status |
|----------|------|--------|
| **English** | `en` | ✅ Default |
| **Marathi** | `mr` | ✅ Supported |
| **Hindi** | `hi` | ✅ Supported |

---

## How to Change Language

### In Login Page
1. Look at the **top-right corner**
2. Find the **🌐 Language** dropdown
3. Select your preferred language:
   - **English** (English)
   - **मराठी** (Marathi)
   - **हिंदी** (Hindi)
4. The entire login interface will update instantly

### In Main App
1. Once logged in, go to the **left sidebar**
2. Find **🌐 भाषा / भाषा** (Language) selector
3. Select your language
4. All app content will switch to selected language

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

| English | Marathi | Hindi |
|---------|---------|-------|
| Welcome back! | पुन्हा स्वागतम! | स्वागत है! |
| Username | वापरकर्ता नाव | उपयोगकर्ता नाम |
| Password | पासवर्ड | पासवर्ड |
| Upload Image | प्रतिमा अपलोड करा | छवि अपलोड करें |
| Analyze Image | प्रतिमा विश्लेषण करा | छवि का विश्लेषण करें |
| Crop Disease Detection | पिक रोग शोध | फसल रोग पहचान |

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
- [ ] More Indic languages (Tamil, Telugu, Kannada, Bengali)
- [ ] Regional disease names
- [ ] Translated disease treatment information
- [ ] Multi-language disease descriptions
- [ ] Language preference saved in user profile

---

**Enjoy using the Crop Disease Detection App in your preferred language!** 🌾
