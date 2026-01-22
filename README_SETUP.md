# Auto Facebook Account Creator - Fixed Version

## 🚀 Quick Installation Guide

### Prerequisites
- Python 3.8 or higher
- Linux/Unix system (tested on Debian/Ubuntu)
- Internet connection

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install requests beautifulsoup4 colorama rich faker pyfiglet
```

### Step 2: Run the Script
```bash
python3 auto_fb_fix.py
```

## 🔧 What Was Fixed?

### 1. **Import Issues Resolved**
- Removed duplicate imports
- Added missing `re` module import
- Fixed `fake_email` module conflicts
- Cleaned up import statements

### 2. **Platform Compatibility**
- Fixed Android-specific commands (`am start`)
- Replaced `/sdcard/` paths with cross-platform paths
- Added proper error handling for different OS
- Made file paths work on Linux/Windows/Mac

### 3. **Email API Improvements**
- Added fallback to 1secmail if temp-mail API fails
- Improved error handling for email generation
- Added timeout for API calls
- Better retry logic for verification codes

### 4. **Code Quality Improvements**
- Removed duplicate code blocks
- Added proper error handling
- Improved variable naming
- Added timeout to all network requests
- Better logging and error messages

### 5. **Logic Fixes**
- Fixed `check_permission()` duplicate call
- Fixed `check_password()` return value handling
- Added proper retry mechanism for verification codes
- Improved session management

### 6. **Security & Reliability**
- Added timeout to all requests (30 seconds)
- Better exception handling
- Improved cookie management
- Added proper error messages

## 📝 Usage Instructions

### First Time Setup
1. Run the script: `python3 auto_fb_fix.py`
2. Wait for approval system check (if enabled)
3. Enter password: `ALEX KHAN` (you can change this in the code)
4. Choose option [1] to start creating accounts

### Account Creation Process
1. Enter first name
2. Enter last name
3. Enter number of accounts to create
4. Enter delay between account creation (in seconds)
5. Script will automatically:
   - Generate fake email
   - Register account on Facebook
   - Wait for verification code
   - Confirm email and save account credentials

### Output
- Successful accounts saved to: `~/DARKSTAR-AUTO-CRATE-OK-ID.txt`
- Format: `UID|PASSWORD|COOKIES`

## ⚠️ Important Notes

### Approval System
- The script checks for approval from a GitHub list
- To disable approval check, modify the `check_permission()` function
- Current approval URL: `https://github.com/Darkstar-xd/Termux-Loader-Approval/blob/main/Approval.txt`

### Email Services
- Primary: temp-mail.io API
- Fallback: 1secmail.com
- Both services are free and don't require registration

### Rate Limiting
- Facebook has strict anti-bot measures
- Use delays between account creation (recommended: 10-30 seconds)
- Consider using VPNs for multiple accounts
- Too many attempts may lead to IP bans

### File Output
- Linux/Mac: `~/DARKSTAR-AUTO-CRATE-OK-ID.txt` (home directory)
- Windows: `C:\Users\<username>\DARKSTAR-AUTO-CRATE-OK-ID.txt`

## 🔧 Customization

### Change Password
Edit line ~109 in `auto_fb_fix.py`:
```python
password = "ALEX KHAN"  # Change to your desired password
```

### Change Approval URL
Edit line ~40 in `auto_fb_fix.py`:
```python
GITHUB_APPROVAL_URL = "https://github.com/Darkstar-xd/Termux-Loader-Approval/blob/main/Approval.txt"
```

### Disable Approval Check
Comment out or remove these lines from `main()`:
```python
unique_key = get_unique_id()
check_permission(unique_key)
```

### Change Output Directory
Edit line ~477 in `auto_fb_fix.py`:
```python
output_dir = os.path.expanduser('~')  # Change to your desired directory
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Install missing packages:
```bash
pip install -r requirements.txt
```

### Issue: "Failed to fetch approval list"
**Solution:** 
- Check internet connection
- GitHub may be blocked in your region
- Disable approval check (see customization section)

### Issue: "Error generating email"
**Solution:**
- Wait a few seconds and retry
- Temp-mail may be down, script will use 1secmail fallback
- Check internet connection

### Issue: "No verification code received"
**Solution:**
- Wait longer (script retries 10 times with 5-second delays)
- Check email service status
- Try different email domains

### Issue: "Account creation failed"
**Solution:**
- Facebook may have blocked your IP
- Use VPN/proxy
- Increase delay between attempts
- Check if Facebook registration is open in your region

## 📊 Performance Tips

1. **Delay Settings:**
   - Safe: 20-30 seconds between accounts
   - Fast: 5-10 seconds (risk of bans)
   - Very Fast: 1-3 seconds (high risk)

2. **Account Limits:**
   - Per IP: 10-50 accounts/day
   - Per day: 100-200 accounts with VPN rotation

3. **Best Practices:**
   - Use different user agents
   - Rotate IPs if creating many accounts
   - Monitor success/failure rates
   - Take breaks between sessions

## 🛡️ Disclaimer

This script is for educational purposes only. Creating fake accounts violates Facebook's Terms of Service. Use responsibly and at your own risk.

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Verify all dependencies are installed
- Ensure internet connection is stable

## 🔄 Updates

### Fixed in This Version
- ✅ Import errors resolved
- ✅ Platform compatibility improved
- ✅ Email API with fallback
- ✅ Better error handling
- ✅ Added request timeouts
- ✅ Improved code structure
- ✅ Fixed logic bugs
- ✅ Better retry mechanisms

---

**Version:** 2.0 (Fixed)  
**Last Updated:** 2024  
**Developer:** SahiiL  
**Team:** Darkstar