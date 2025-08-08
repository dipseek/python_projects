#!/usr/bin/env python3
"""
Test script to verify that all fixed Python files work correctly
"""

import subprocess
import sys
import os

def test_file(filename, description):
    """Test a Python file and return success status"""
    print(f"\n{'='*60}")
    print(f"Testing: {filename}")
    print(f"Description: {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            [sys.executable, filename],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ SUCCESS")
            if result.stdout:
                print("Output:")
                print(result.stdout)
        else:
            print("❌ FAILED")
            if result.stderr:
                print("Error:")
                print(result.stderr)
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT - Script took too long to execute")
        return False
    except Exception as e:
        print(f"💥 EXCEPTION: {e}")
        return False

def main():
    """Test all fixed files"""
    print("🧪 Testing Fixed Python Files")
    print("="*60)
    
    # List of files to test
    test_files = [
        ("read-ram-fixed.py", "RAM reading functionality"),
        ("send_email-fixed.py", "Email sending demonstration"),
        ("send-sms-fixed.py", "SMS sending demonstration"),
        ("search-web-fixed.py", "Web search functionality"),
    ]
    
    passed = 0
    total = len(test_files)
    
    for filename, description in test_files:
        if os.path.exists(filename):
            if test_file(filename, description):
                passed += 1
        else:
            print(f"\n❌ File not found: {filename}")
    
    print(f"\n{'='*60}")
    print(f"📊 Test Results: {passed}/{total} files passed")
    print(f"{'='*60}")
    
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print("⚠️  Some tests failed. Check the output above.")

if __name__ == "__main__":
    main()
