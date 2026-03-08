# 🌾 Admin User Setup Guide

## Admin Account Created

An admin user has been successfully created for the Crop Disease Detection application.

### Admin Credentials

| Field | Value |
|-------|-------|
| **Username** | `admin` |
| **Email** | `admin@crophealth.com` |
| **Password** | `Admin@12345` |
| **Role** | Administrator |

## How to Use

### 1. Start the Application
```bash
streamlit run app.py
```

### 2. Login to Application
- Use the **Login** tab on the authentication page
- Enter the admin username and password
- Click "Login"

### 3. Admin Features (Upcoming)
The following admin features can be implemented:
- View all users
- Manage user accounts
- View analytics and statistics
- System settings and configuration
- User activity logs

## Creating Additional Admin Users

To create another admin user with command-line arguments:

```bash
python create_admin.py <username> <email> <password>
```

**Example:**
```bash
python create_admin.py superadmin superadmin@example.com MySecurePassword123
```

## Interactive Mode

To create an admin user interactively:

```bash
python create_admin.py
```

You will be prompted to enter:
- Username (minimum 3 characters)
- Email address
- Password (minimum 6 characters)
- Confirm password

## User Database

User data is stored in `users_database.json` with encrypted passwords using bcrypt hashing.

**Security Features:**
- ✅ Passwords hashed with bcrypt
- ✅ No plain-text password storage
- ✅ Secure password verification
- ✅ User role management

## Security Best Practices

### Important Security Notes:

1. **Change Default Password**: Change the admin password after first login
2. **Protect Database**: Keep `users_database.json` secure and backed up
3. **Strong Passwords**: Use strong, unique passwords for all accounts
4. **Regular Backups**: Backup your user database regularly
5. **Access Control**: Limit admin account access to authorized personnel

### How to Change Admin Password (After Login in App):

- Go to your user profile
- Select "Change Password"
- Enter current password and new password
- Confirm new password
- Save changes

## Troubleshooting

### Admin User Already Exists
If you see a message that the username already exists:
- Admin user is already created
- You can login with existing credentials
- To create a different admin: use a new username

### Password Requirements
- Minimum 6 characters
- Must match confirmation entry
- Can contain special characters

### Email Validation
- Must contain @ symbol
- Must contain . (dot) for domain
- Must be unique in the system

## Multiple Admins

You can create multiple admin accounts:

```bash
python create_admin.py admin2 admin2@crophealth.com SecurePass123
python create_admin.py admin3 admin3@crophealth.com Another@Pass456
```

Each admin account has:
- Independent credentials
- Full administrative privileges
- Separate analysis history and settings

## Next Steps

1. ✅ Admin user created
2. Start the Streamlit app: `streamlit run app.py`
3. Login with admin credentials
4. Explore the application
5. Create regular user accounts for other users
6. (Optional) Add admin-specific features in the application

---

**Need Help?** Check the main README.md for application features and usage guide.
