"""
Admin User Creation Script
Run this script to create an admin user for the Crop Disease Detection application

Usage:
    python create_admin.py                    # Interactive mode
    python create_admin.py username email password  # Command-line mode
"""

import sys
import getpass
from auth_handler import AuthHandler


def interactive_mode():
    """Create an admin user interactively"""
    
    print("\n" + "="*60)
    print("🌾 Crop Disease Detection Application - Admin Setup")
    print("="*60 + "\n")
    
    auth = AuthHandler()
    
    # Check if admin already exists
    users = auth._load_users()
    admin_exists = any(user.get('is_admin', False) for user in users.values())
    
    if admin_exists and len(users) > 0:
        print("⚠️  Admin user(s) already exist in the system")
        print(f"   Current users: {list(users.keys())}\n")
    
    print("Enter details for the new admin user:\n")
    
    # Get username
    while True:
        username = input("📝 Username (minimum 3 characters): ").strip()
        if len(username) < 3:
            print("   ❌ Username must be at least 3 characters\n")
            continue
        if username in users:
            print(f"   ❌ Username '{username}' already exists\n")
            continue
        break
    
    # Get email
    while True:
        email = input("📧 Email address: ").strip()
        if "@" not in email or "." not in email:
            print("   ❌ Invalid email format\n")
            continue
        if any(user['email'] == email for user in users.values()):
            print(f"   ❌ Email '{email}' already registered\n")
            continue
        break
    
    # Get password
    while True:
        password = getpass.getpass("🔐 Password (minimum 6 characters): ")
        if len(password) < 6:
            print("   ❌ Password must be at least 6 characters\n")
            continue
        
        confirm = getpass.getpass("🔐 Confirm password: ")
        if password != confirm:
            print("   ❌ Passwords do not match\n")
            continue
        break
    
    create_admin_account(username, email, password)


def create_admin_account(username, email, password):
    """Create admin account with given credentials"""
    
    print("\n⏳ Creating admin user...")
    auth = AuthHandler()
    success, message = auth.create_admin_user(username, email, password)
    
    if success:
        print(f"\n✅ {message}")
        print("\n" + "="*60)
        print("Admin Account Created Successfully!")
        print("="*60)
        print(f"\nAdmin Username: {username}")
        print(f"Admin Email: {email}")
        print(f"Is Admin: Yes\n")
        print("You can now log in to the application with these credentials.")
        print("Run the app with: streamlit run app.py\n")
    else:
        print(f"\n❌ {message}")
        sys.exit(1)


def main():
    """Main entry point"""
    
    if len(sys.argv) == 4:
        # Command-line mode
        username, email, password = sys.argv[1], sys.argv[2], sys.argv[3]
        create_admin_account(username, email, password)
    elif len(sys.argv) == 1:
        # Interactive mode
        try:
            interactive_mode()
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled by user")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            sys.exit(1)
    else:
        print("\n❌ Invalid arguments")
        print("\nUsage:")
        print("  Interactive: python create_admin.py")
        print("  Command-line: python create_admin.py <username> <email> <password>\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
