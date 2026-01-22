#!/usr/bin/env python3
"""
Test script to verify all dependencies are properly installed
"""

import sys
import subprocess

def test_import(module_name):
    """Test if a module can be imported"""
    try:
        __import__(module_name)
        print(f"✓ {module_name} - OK")
        return True
    except ImportError:
        print(f"✗ {module_name} - FAILED")
        return False

def test_version(module_name, version_attr):
    """Try to get version of a module"""
    try:
        module = __import__(module_name)
        version = getattr(module, version_attr, "Unknown")
        print(f"  Version: {version}")
        return True
    except:
        return False

def main():
    print("=" * 60)
    print("Dependency Check for Auto Facebook Creator")
    print("=" * 60)
    print()
    
    # List of required modules
    modules = [
        ('requests', '__version__'),
        ('bs4', '__version__'),
        ('colorama', '__version__'),
        ('rich', '__version__'),
        ('faker', '__version__'),
        ('pyfiglet', '__version__'),
        ('re', None),
        ('hashlib', None),
        ('json', None),
        ('time', None),
        ('random', None),
        ('os', None),
        ('sys', None),
    ]
    
    all_ok = True
    
    for module, version_attr in modules:
        if test_import(module):
            if version_attr:
                test_version(module, version_attr)
        else:
            all_ok = False
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✓ All dependencies are installed!")
        print("You can run: python3 auto_fb_fix.py")
        print("=" * 60)
        return 0
    else:
        print("✗ Some dependencies are missing!")
        print("Install them with: pip install -r requirements.txt")
        print("=" * 60)
        return 1

if __name__ == '__main__':
    sys.exit(main())