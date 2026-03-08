"""
Authentication Handler - Manages user registration, login, and password security
"""

import bcrypt
import json
import os
from datetime import datetime


class AuthHandler:
    """Handles user authentication, registration, and login"""
    
    def __init__(self, users_db_path="users_database.json"):
        """
        Initialize auth handler
        
        Args:
            users_db_path (str): Path to the JSON file storing user data
        """
        self.users_db_path = users_db_path
        self._initialize_database()
    
    def _initialize_database(self):
        """Create database file if it doesn't exist"""
        if not os.path.exists(self.users_db_path):
            with open(self.users_db_path, 'w') as f:
                json.dump({}, f)
    
    def _load_users(self):
        """Load all users from database"""
        try:
            with open(self.users_db_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def _save_users(self, users):
        """Save users to database"""
        with open(self.users_db_path, 'w') as f:
            json.dump(users, f, indent=4)
    
    def hash_password(self, password):
        """
        Hash a password using bcrypt
        
        Args:
            password (str): Plain text password
        
        Returns:
            str: Hashed password
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, password, hashed_password):
        """
        Verify a password against its hash
        
        Args:
            password (str): Plain text password
            hashed_password (str): Hashed password from database
        
        Returns:
            bool: True if password matches, False otherwise
        """
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        except:
            return False
    
    def register_user(self, username, email, password, confirm_password):
        """
        Register a new user
        
        Args:
            username (str): Username
            email (str): Email address
            password (str): Password
            confirm_password (str): Password confirmation
        
        Returns:
            tuple: (success: bool, message: str)
        """
        # Validate inputs
        if not username or not email or not password:
            return False, "❌ All fields are required"
        
        if len(username) < 3:
            return False, "❌ Username must be at least 3 characters"
        
        if len(password) < 6:
            return False, "❌ Password must be at least 6 characters"
        
        if password != confirm_password:
            return False, "❌ Passwords do not match"
        
        if "@" not in email or "." not in email:
            return False, "❌ Invalid email format"
        
        # Check if user already exists
        users = self._load_users()
        if username in users:
            return False, "❌ Username already exists"
        
        if any(user['email'] == email for user in users.values()):
            return False, "❌ Email already registered"
        
        # Create new user
        hashed_pwd = self.hash_password(password)
        users[username] = {
            'email': email,
            'password': hashed_pwd,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'analysis_history': [],
            'total_analyses': 0,
            'is_admin': False
        }
        
        self._save_users(users)
        return True, "✅ Registration successful! Please log in."
    
    def login_user(self, username, password):
        """
        Login a user
        
        Args:
            username (str): Username
            password (str): Password
        
        Returns:
            tuple: (success: bool, message: str, user_data: dict or None)
        """
        if not username or not password:
            return False, "❌ Username and password required", None
        
        users = self._load_users()
        
        if username not in users:
            return False, "❌ Username not found", None
        
        user = users[username]
        if self.verify_password(password, user['password']):
            return True, "✅ Login successful!", user
        else:
            return False, "❌ Incorrect password", None
    
    def user_exists(self, username):
        """Check if user exists"""
        users = self._load_users()
        return username in users
    
    def get_user_info(self, username):
        """Get user information"""
        users = self._load_users()
        if username in users:
            user = users[username].copy()
            user.pop('password', None)  # Don't expose password
            return user
        return None
    
    def save_analysis(self, username, disease_label, confidence, image_path=None):
        """
        Save an analysis to user's history
        
        Args:
            username (str): Username
            disease_label (str): Detected disease
            confidence (float): Confidence score
            image_path (str): Path to analyzed image (optional)
        
        Returns:
            bool: Success status
        """
        users = self._load_users()
        
        if username not in users:
            return False
        
        analysis = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'disease': disease_label,
            'confidence': float(confidence),
            'image_path': image_path
        }
        
        users[username]['analysis_history'].append(analysis)
        users[username]['total_analyses'] = len(users[username]['analysis_history'])
        
        self._save_users(users)
        return True
    
    def get_user_history(self, username, limit=10):
        """
        Get user's analysis history
        
        Args:
            username (str): Username
            limit (int): Maximum number of records to return
        
        Returns:
            list: Analysis history (most recent first)
        """
        users = self._load_users()
        
        if username not in users:
            return []
        
        history = users[username].get('analysis_history', [])
        return history[-limit:][::-1]  # Return last 'limit' items in reverse order
    
    def update_password(self, username, old_password, new_password):
        """
        Update user password
        
        Args:
            username (str): Username
            old_password (str): Current password
            new_password (str): New password
        
        Returns:
            tuple: (success: bool, message: str)
        """
        users = self._load_users()
        
        if username not in users:
            return False, "❌ User not found"
        
        user = users[username]
        if not self.verify_password(old_password, user['password']):
            return False, "❌ Current password is incorrect"
        
        if len(new_password) < 6:
            return False, "❌ New password must be at least 6 characters"
        
        user['password'] = self.hash_password(new_password)
        self._save_users(users)
        
        return True, "✅ Password updated successfully"
    
    def delete_account(self, username, password):
        """
        Delete user account
        
        Args:
            username (str): Username
            password (str): Password confirmation
        
        Returns:
            tuple: (success: bool, message: str)
        """
        users = self._load_users()
        
        if username not in users:
            return False, "❌ User not found"
        
        user = users[username]
        if not self.verify_password(password, user['password']):
            return False, "❌ Incorrect password"
        
        del users[username]
        self._save_users(users)
        
        return True, "✅ Account deleted successfully"
    
    def create_admin_user(self, username, email, password):
        """
        Create an admin user (for setup purposes)
        
        Args:
            username (str): Username
            email (str): Email address
            password (str): Password
        
        Returns:
            tuple: (success: bool, message: str)
        """
        # Validate inputs
        if not username or not email or not password:
            return False, "❌ All fields are required"
        
        if len(username) < 3:
            return False, "❌ Username must be at least 3 characters"
        
        if len(password) < 6:
            return False, "❌ Password must be at least 6 characters"
        
        # Check if user already exists
        users = self._load_users()
        if username in users:
            return False, "❌ Username already exists"
        
        if any(user['email'] == email for user in users.values()):
            return False, "❌ Email already registered"
        
        # Create admin user
        hashed_pwd = self.hash_password(password)
        users[username] = {
            'email': email,
            'password': hashed_pwd,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'analysis_history': [],
            'total_analyses': 0,
            'is_admin': True
        }
        
        self._save_users(users)
        return True, f"✅ Admin user '{username}' created successfully"
    
    def is_admin(self, username):
        """
        Check if user is an admin
        
        Args:
            username (str): Username
        
        Returns:
            bool: True if admin, False otherwise
        """
        users = self._load_users()
        if username not in users:
            return False
        return users[username].get('is_admin', False)
    
    def make_admin(self, username):
        """
        Promote user to admin
        
        Args:
            username (str): Username
        
        Returns:
            tuple: (success: bool, message: str)
        """
        users = self._load_users()
        if username not in users:
            return False, "❌ User not found"
        
        users[username]['is_admin'] = True
        self._save_users(users)
        return True, f"✅ User '{username}' is now an admin"
    
    def remove_admin(self, username):
        """
        Remove admin privileges from user
        
        Args:
            username (str): Username
        
        Returns:
            tuple: (success: bool, message: str)
        """
        users = self._load_users()
        if username not in users:
            return False, "❌ User not found"
        
        users[username]['is_admin'] = False
        self._save_users(users)
        return True, f"✅ Admin privileges removed from '{username}'"
    
    def get_all_users(self):
        """
        Get list of all users (admin only)
        
        Returns:
            dict: All users without passwords
        """
        users = self._load_users()
        for user in users.values():
            user.pop('password', None)
        return users
