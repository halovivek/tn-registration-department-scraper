#!/usr/bin/env python3
"""
Test script to verify the setup and basic functionality
"""

import sys
import subprocess
import importlib

def test_python_version():
    """Test if Python version is compatible"""
    print("Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.7+")
        return False

def test_package_installation():
    """Test if required packages are installed"""
    print("\nTesting package installations...")
    
    required_packages = {
        'selenium': 'selenium',
        'openpyxl': 'openpyxl',
        'webdriver_manager': 'webdriver-manager'
    }
    
    all_installed = True
    
    for package_name, pip_name in required_packages.items():
        try:
            importlib.import_module(package_name)
            print(f"✓ {pip_name} - Installed")
        except ImportError:
            print(f"✗ {pip_name} - Not installed")
            print(f"  Install with: pip install {pip_name}")
            all_installed = False
    
    return all_installed

def test_chrome_availability():
    """Test if Chrome browser is available"""
    print("\nTesting Chrome browser availability...")
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(
            service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        
        # Test basic functionality
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        
        print("✓ Chrome browser and WebDriver - Working")
        print(f"  Test page title: {title}")
        return True
        
    except Exception as e:
        print(f"✗ Chrome browser or WebDriver - Error: {str(e)}")
        print("  Make sure Chrome browser is installed")
        return False

def test_internet_connection():
    """Test internet connectivity"""
    print("\nTesting internet connection...")
    
    try:
        import urllib.request
        urllib.request.urlopen('https://www.google.com', timeout=10)
        print("✓ Internet connection - Available")
        return True
    except Exception as e:
        print(f"✗ Internet connection - Error: {str(e)}")
        return False

def test_target_website():
    """Test if target website is accessible"""
    print("\nTesting target website accessibility...")
    
    try:
        import urllib.request
        response = urllib.request.urlopen('http://www.tnreginet.gov.in', timeout=15)
        if response.getcode() == 200:
            print("✓ www.tnreginet.gov.in - Accessible")
            return True
        else:
            print(f"✗ www.tnreginet.gov.in - HTTP {response.getcode()}")
            return False
    except Exception as e:
        print(f"✗ www.tnreginet.gov.in - Error: {str(e)}")
        print("  The website might be temporarily unavailable")
        return False

def main():
    """Run all tests"""
    print("TN Registration Scraper - Setup Test")
    print("=" * 40)
    
    tests = [
        test_python_version,
        test_package_installation,
        test_internet_connection,
        test_target_website,
        test_chrome_availability
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed with error: {str(e)}")
            results.append(False)
    
    print("\n" + "=" * 40)
    print("Test Summary:")
    print(f"Passed: {sum(results)}/{len(results)}")
    
    if all(results):
        print("✓ All tests passed! You can run the scraper.")
        print("\nTo run the scraper:")
        print("python tnreginet_scraper.py")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("1. Install missing packages: pip install -r requirements.txt")
        print("2. Install Chrome browser")
        print("3. Check internet connection")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
