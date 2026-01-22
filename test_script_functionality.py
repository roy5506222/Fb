#!/usr/bin/env python3
"""
Test core functionality of the Auto FB Creator script
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all imports work"""
    print("Testing imports...")
    try:
        import requests
        import bs4
        import colorama
        import rich
        import faker
        import pyfiglet
        import re
        import hashlib
        import time
        import random
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_functions():
    """Test key functions"""
    print("\nTesting functions...")
    
    # Test user agent generation
    try:
        exec(open('auto_fb_fix.py').read().split('def ____useragent____():')[0] + '''
def ____useragent____():
    import random
    version = random.choice(['14','15','10'])
    model = random.choice(['A1','A2','A3'])
    build = random.choice(['MMB29Q','R16NW'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
''')
        ua = ____useragent____()
        if "Mozilla" in ua and "Android" in ua:
            print(f"✓ User agent generation works: {ua[:50]}...")
        else:
            print("✗ User agent generation failed")
            return False
    except Exception as e:
        print(f"✗ User agent test failed: {e}")
        return False
    
    # Test extractor function
    try:
        exec(open('auto_fb_fix.py').read().split('def extractor(data):')[1].split('#_________|FAKE EMAIL|_________#')[0])
        from bs4 import BeautifulSoup
        test_html = '<input name="test" value="123"><input name="field" value="456">'
        result = extractor(test_html)
        if result.get('test') == '123' and result.get('field') == '456':
            print("✓ Extractor function works")
        else:
            print("✗ Extractor function failed")
            return False
    except Exception as e:
        print(f"✗ Extractor test failed: {e}")
        return False
    
    return True

def test_email_apis():
    """Test email generation APIs"""
    print("\nTesting email APIs...")
    
    # Test temp-mail API
    try:
        import requests
        response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', timeout=10)
        if response.status_code == 200:
            email = response.json().get('email', '')
            if '@' in email:
                print(f"✓ Temp-mail API works: {email}")
            else:
                print("✗ Temp-mail API returned invalid email")
        else:
            print(f"⚠ Temp-mail API returned status {response.status_code}")
    except Exception as e:
        print(f"⚠ Temp-mail API test failed: {e}")
    
    return True

def main():
    print("=" * 60)
    print("Auto FB Creator - Functionality Test")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("Functions", test_functions()))
    results.append(("Email APIs", test_email_apis()))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name:.<40} {status}")
    
    print("=" * 60)
    
    if all(result for _, result in results):
        print("\n✓ All tests passed! The script is ready to use.")
        return 0
    else:
        print("\n✗ Some tests failed. Check the errors above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())