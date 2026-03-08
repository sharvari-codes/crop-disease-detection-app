"""
User Preferences Module - Manage user settings and preferences
Saves user preferences like language, theme, notification settings
"""

import json
import os
from datetime import datetime

PREFERENCES_DIR = "user_preferences"

def ensure_preferences_dir():
    """Ensure preferences directory exists"""
    if not os.path.exists(PREFERENCES_DIR):
        os.makedirs(PREFERENCES_DIR)

def get_user_preferences(username):
    """
    Load user preferences from file
    Returns default preferences if user has none
    """
    ensure_preferences_dir()
    
    pref_file = os.path.join(PREFERENCES_DIR, f"{username}_prefs.json")
    
    # Default preferences
    default_prefs = {
        "language": "en",
        "theme": "light",
        "notifications": True,
        "email_reports": False,
        "auto_save_results": True,
        "favorite_crops": [],
        "disease_interests": [],
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    
    if os.path.exists(pref_file):
        try:
            with open(pref_file, 'r', encoding='utf-8') as f:
                saved_prefs = json.load(f)
                # Merge with defaults to ensure all keys exist
                default_prefs.update(saved_prefs)
                return default_prefs
        except Exception as e:
            print(f"Error loading preferences: {e}")
            return default_prefs
    
    return default_prefs

def save_user_preferences(username, preferences):
    """
    Save user preferences to file
    """
    ensure_preferences_dir()
    
    pref_file = os.path.join(PREFERENCES_DIR, f"{username}_prefs.json")
    
    # Update timestamp
    preferences['updated_at'] = datetime.now().isoformat()
    
    try:
        with open(pref_file, 'w', encoding='utf-8') as f:
            json.dump(preferences, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving preferences: {e}")
        return False

def update_language_preference(username, language):
    """Update user's language preference"""
    prefs = get_user_preferences(username)
    prefs['language'] = language
    return save_user_preferences(username, prefs)

def update_theme_preference(username, theme):
    """Update user's theme preference"""
    prefs = get_user_preferences(username)
    prefs['theme'] = theme
    return save_user_preferences(username, prefs)

def update_notification_preference(username, enabled):
    """Update notification preference"""
    prefs = get_user_preferences(username)
    prefs['notifications'] = enabled
    return save_user_preferences(username, prefs)

def toggle_email_reports(username):
    """Toggle email reports preference"""
    prefs = get_user_preferences(username)
    prefs['email_reports'] = not prefs.get('email_reports', False)
    return save_user_preferences(username, prefs)

def add_favorite_crop(username, crop_name):
    """Add crop to favorites"""
    prefs = get_user_preferences(username)
    if crop_name not in prefs.get('favorite_crops', []):
        prefs['favorite_crops'].append(crop_name)
    return save_user_preferences(username, prefs)

def remove_favorite_crop(username, crop_name):
    """Remove crop from favorites"""
    prefs = get_user_preferences(username)
    if crop_name in prefs.get('favorite_crops', []):
        prefs['favorite_crops'].remove(crop_name)
    return save_user_preferences(username, prefs)

def add_disease_interest(username, disease_name):
    """Add disease to interests"""
    prefs = get_user_preferences(username)
    if disease_name not in prefs.get('disease_interests', []):
        prefs['disease_interests'].append(disease_name)
    return save_user_preferences(username, prefs)

def export_preferences(username):
    """Export user preferences as JSON string"""
    prefs = get_user_preferences(username)
    return json.dumps(prefs, indent=4)

def import_preferences(username, prefs_json):
    """Import user preferences from JSON string"""
    try:
        prefs = json.loads(prefs_json)
        return save_user_preferences(username, prefs)
    except Exception as e:
        print(f"Error importing preferences: {e}")
        return False
