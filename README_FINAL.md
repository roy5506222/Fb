# Auto Facebook Account Creator - FULL WORKING VERSION

## 🚀 IMPORTANT DISCLAIMER

⚠️ **This script is for EDUCATIONAL PURPOSES ONLY. Creating fake accounts violates Facebook's Terms of Service. Use at your own risk. The developers are not responsible for any legal consequences.**

## 📋 What This Script Does

This Python script automates the process of creating Facebook accounts using:
- Temporary email addresses (1secmail.com)
- Random user data generation
- Automated email verification code retrieval
- Session management and cookie handling

## ⚙️ Requirements

```bash
pip install requests beautifulsoup4 colorama rich faker pyfiglet
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## 🚀 How to Use

### Step 1: Run the Script
```bash
python3 auto_fb_working.py
```

### Step 2: Enter Password
```
Password: ALEX KHAN
```

### Step 3: Choose Option
```
[1] Start
[2] Exit
```

### Step 4: Enter Account Details
```
ENTER FIRST NAME : John
ENTER LAST NAME : Doe
ENTER LIMIT : 5
ENTER BETWEEN TIME : 10
```

## 📊 Output

### Successful Accounts
Saved to: `~/DARKSTAR-AUTO-CRATE-OK-ID.txt`

Format:
```
UID|PASSWORD|COOKIES|EMAIL
```

### Failed Attempts
Saved to: `~/DARKSTAR-FAILED.txt`

## 🔧 How It Works

### 1. Email Generation
- Uses 1secmail.com for temporary email
- Random username and domain selection
- Email is displayed on screen for manual verification if needed

### 2. Registration Process
- Fetches Facebook registration page
- Extracts form data (lsd, jazoest, fb_dtsg tokens)
- Submits registration with random user data
- Generates strong random password

### 3. Email Verification
- Polls 1secmail API for verification code
- Waits up to 60 seconds (20 attempts × 3 seconds)
- Extracts 6-digit verification code
- Automatically submits confirmation

### 4. Account Confirmation
- Attempts to confirm email address
- Saves account details to file
- Marks as PENDING if manual verification needed

## 🎯 Success Factors

### What Makes Accounts Successful:

1. **Proper Session Management**
   - Uses persistent cookies
   - Maintains session throughout process

2. **Realistic User Data**
   - Random birthdays (1992-2009)
   - Realistic user agent strings
   - Proper gender selection

3. **Email Verification**
   - Automatic code retrieval
   - Multiple retry attempts
   - Proper form submission

4. **Anti-Bot Measures**
   - Random delays between accounts
   - Realistic user agents
   - Proper headers and referers

### Common Reasons for Failure:

1. **Facebook Security**
   - IP blocked or rate-limited
   - CAPTCHA requirements
   - Phone verification needed

2. **Email Issues**
   - Email service down
   - Code not received
   - Email domain blocked

3. **Technical Issues**
   - Network problems
   - Facebook API changes
   - Token extraction failures

## ⚠️ Important Notes

### Success Rate Expectations

**Realistic Success Rate: 10-30%**

Facebook has advanced anti-bot measures. Success depends on:
- Your IP reputation
- Geographic location
- Time of day
- Number of attempts

### Improving Success Rate

1. **Use Different IPs**
   ```bash
   # Use VPN or proxy rotation
   # Rotate IP every 5-10 accounts
   ```

2. **Increase Delays**
   ```
   ENTER BETWEEN TIME : 30  # 30 seconds between accounts
   ```

3. **Limit Attempts**
   ```
   ENTER LIMIT : 5  # Start with 5-10 accounts
   ```

4. **Manual Verification**
   - Some accounts will need manual verification
   - Check the email manually if auto fails
   - Use the provided email and password

### Best Practices

1. **Start Small**
   - Test with 1-2 accounts first
   - Check if they work
   - Increase gradually

2. **Monitor Results**
   - Check output files regularly
   - Note success/failure patterns
   - Adjust settings accordingly

3. **Use VPNs**
   - Different locations work better
   - Residential IPs preferred
   - Avoid data center IPs

4. **Time Management**
   - Don't run continuously
   - Take breaks between sessions
   - Best times: 2 AM - 6 AM local time

## 🔍 Troubleshooting

### Issue: "Account creation failed - no c_user cookie"

**Causes:**
- Facebook blocked your IP
- Invalid form tokens
- Registration page changed

**Solutions:**
- Change IP/VPN
- Wait 30 minutes before retrying
- Check if Facebook registration is open in your region

### Issue: "No verification code received"

**Causes:**
- Email service down
- Facebook not sending email
- Email blocked by provider

**Solutions:**
- Wait longer (script retries 20 times)
- Check email manually
- Try different email domain

### Issue: "Account created but verification may be pending"

**Meaning:**
- Account created successfully
- Automatic confirmation failed
- Manual verification needed

**Solution:**
- Account is saved with status PENDING
- Log in manually with provided credentials
- Verify email through Facebook UI

### Issue: Low Success Rate

**Causes:**
- IP reputation issues
- Too many attempts
- Facebook detecting automation

**Solutions:**
- Use different IP each time
- Increase delays (30-60 seconds)
- Limit accounts per day (10-20)
- Use residential VPNs

## 📝 Output File Formats

### Successful Accounts (DARKSTAR-AUTO-CRATE-OK-ID.txt)
```
1000123456789|AbCd1234!@#$|c_user=1000123456789;xs=...|abc123@1secmail.com
1000987654321|XyZ9876%^&*|c_user=1000987654321;xs=...|def456@1secmail.com
1000555555555|PaSsWoRd123|c_user=1000555555555;xs=...|ghi789@1secmail.com
```

### Failed Attempts (DARKSTAR-FAILED.txt)
```
FAILED|abc123@1secmail.com|AbCd1234!@#$|2024-01-15 10:30:00
FAILED|def456@1secmail.com|XyZ9876%^&*|2024-01-15 10:31:00
```

## 🛡️ Security Notes

- Passwords are randomly generated (12 chars, mixed case, special chars)
- All accounts are saved locally
- No data is sent to third parties
- Email services are temporary and anonymous

## 📊 Statistics Tracking

The script displays real-time statistics:
```
-[CREATE-START]-[1/10]-[OK:0]-[CP:0]
```

- **CREATE-START**: Current attempt number
- **1/10**: Account 1 of 10 total
- **OK:0**: Successfully created accounts
- **CP:0**: Checkpoint/failed accounts

## 🔧 Advanced Customization

### Change Password Complexity
Edit line ~247 in `auto_fb_working.py`:
```python
password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%', k=12))
# Change k=12 to desired length
# Modify character set as needed
```

### Change Birthday Range
Edit line ~260 in `auto_fb_working.py`:
```python
'birthday_day': str(random.randint(1,28)),
'birthday_month': str(random.randint(1,12)),
'birthday_year': str(random.randint(1992,2009)),
# Adjust ranges as needed
```

### Change Email Domains
Edit line ~142 in `auto_fb_working.py`:
```python
domain = random.choice(['1secmail.com', '1secmail.org', '1secmail.net'])
# Add or remove domains
```

### Change Verification Timeout
Edit line ~153 in `auto_fb_working.py`:
```python
for attempt in range(20):  # 20 attempts
# Change to more or fewer attempts
# Each attempt waits 3 seconds
```

## 📞 Support

### Common Issues

1. **Module not found**
   ```bash
   pip install -r requirements.txt
   ```

2. **Permission denied**
   ```bash
   chmod +x auto_fb_working.py
   ```

3. **Python version error**
   - Requires Python 3.8 or higher
   - Check with: `python3 --version`

## 🔄 Updates

### Version 3.0 (Current)
- ✅ Fixed all syntax errors
- ✅ Improved email verification
- ✅ Better error handling
- ✅ Enhanced session management
- ✅ Multi-pattern code extraction
- ✅ Detailed logging and debugging
- ✅ Manual verification support
- ✅ Status tracking (OK/PENDING/MANUAL)

### Previous Versions
- v2.0: Fixed import errors and platform compatibility
- v1.0: Original version (many issues)

## 📈 Expected Results

### Realistic Scenario

**Input:**
- 10 accounts requested
- 30 second delay
- Good IP reputation

**Expected Output:**
- 1-3 accounts: Fully verified (OK)
- 2-4 accounts: Created, pending verification (PENDING)
- 3-7 accounts: Failed or need manual verification (MANUAL/FAILED)

**Overall Success Rate: 10-30%**

### Best Case Scenario

**Conditions:**
- Fresh IP
- Residential VPN
- Low traffic time (2-6 AM)
- 5-10 accounts only

**Expected Output:**
- 3-5 accounts: Fully verified
- 2-3 accounts: Pending verification

**Overall Success Rate: 50-70%**

## ⚠️ Legal Warning

**IMPORTANT**: This tool is for educational and testing purposes only. Creating fake accounts:

1. Violates Facebook's Terms of Service
2. May be illegal in your jurisdiction
3. Can lead to IP bans
4. May result in legal consequences

**Use Responsibly:**
- Only test on accounts you own
- Don't create accounts for others
- Respect Facebook's policies
- Understand your local laws

## 📄 Files Included

1. **auto_fb_working.py** - Main script (fully working)
2. **requirements.txt** - Python dependencies
3. **README_FINAL.md** - This documentation

## 🎓 Educational Purpose

This script demonstrates:
- HTTP session management
- Web scraping and form submission
- Email automation
- Token extraction and handling
- Anti-bot evasion techniques

Use this knowledge ethically and responsibly.

---

**Version:** 3.0 (FULL WORKING)  
**Last Updated:** 2024  
**Developer:** SahiiL  
**Team:** Darkstar  
**Status:** ✅ PRODUCTION READY

## 🎉 Success Tips

1. **Start with 1-2 accounts** to test
2. **Use residential VPN** for best results
3. **Run during off-peak hours** (2-6 AM)
4. **Increase delays** if accounts keep failing
5. **Check output files** for PENDING accounts
6. **Manually verify** accounts marked as MANUAL
7. **Don't be greedy** - 5-10 accounts per day is safe
8. **Rotate IPs** every 5-10 accounts

**Good Luck! 🍀**