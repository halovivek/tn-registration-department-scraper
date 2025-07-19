#!/usr/bin/env python3
"""
Configuration file for TN Registration Scraper
Modify these settings to customize the scraper behavior
"""

# Website Configuration
WEBSITE_URL = "http://www.tnreginet.gov.in"
TARGET_LANGUAGE = "English"

# Browser Configuration
BROWSER_CONFIG = {
    "headless": False,  # Set to True to run browser in background
    "window_size": "1920,1080",
    "timeout": 30,  # Seconds to wait for elements
    "implicit_wait": 10,  # Seconds for implicit wait
    "page_load_timeout": 60  # Seconds to wait for page load
}

# Output Configuration
OUTPUT_CONFIG = {
    "excel_filename": "tnreginet_data.xlsx",
    "summary_filename": "tnreginet_data_summary.txt",
    "log_filename": "tnreginet_scraper.log",
    "create_summary": True,
    "create_excel": True
}

# Scraping Configuration
SCRAPING_CONFIG = {
    "delay_between_selections": 2,  # Seconds to wait between dropdown selections
    "max_retries": 3,  # Maximum retries for failed operations
    "retry_delay": 5,  # Seconds to wait between retries
    "screenshot_on_error": True  # Take screenshot when errors occur
}

# Element Selectors (XPath and CSS selectors)
SELECTORS = {
    "language": [
        "//a[contains(text(), 'English')]",
        "//button[contains(text(), 'English')]",
        "//span[contains(text(), 'English')]",
        "//div[contains(text(), 'English')]",
        "//a[@href*='english' or @href*='English']",
        "//select[@name='language']//option[contains(text(), 'English')]"
    ],
    "eservices": [
        "//a[contains(text(), 'E-services') or contains(text(), 'E-Services')]",
        "//span[contains(text(), 'E-services') or contains(text(), 'E-Services')]",
        "//div[contains(text(), 'E-services') or contains(text(), 'E-Services')]",
        "//li[contains(text(), 'E-services') or contains(text(), 'E-Services')]"
    ],
    "encumbrance": [
        "//a[contains(text(), 'Encumbrance') or contains(text(), 'encumbrance')]",
        "//span[contains(text(), 'Encumbrance') or contains(text(), 'encumbrance')]",
        "//div[contains(text(), 'Encumbrance') or contains(text(), 'encumbrance')]"
    ],
    "view_ec": [
        "//a[contains(text(), 'View EC') or contains(text(), 'view ec')]",
        "//span[contains(text(), 'View EC') or contains(text(), 'view ec')]",
        "//div[contains(text(), 'View EC') or contains(text(), 'view ec')]"
    ],
    "zone_dropdown": [
        "//select[contains(@name, 'zone') or contains(@id, 'zone')]",
        "//select[contains(@name, 'Zone') or contains(@id, 'Zone')]",
        "//select[contains(@class, 'zone')]"
    ],
    "district_dropdown": [
        "//select[contains(@name, 'district') or contains(@id, 'district')]",
        "//select[contains(@name, 'District') or contains(@id, 'District')]",
        "//select[contains(@class, 'district')]"
    ],
    "sub_register_dropdown": [
        "//select[contains(@name, 'sub') or contains(@id, 'sub') or contains(@name, 'register') or contains(@id, 'register')]",
        "//select[contains(@name, 'Sub') or contains(@id, 'Sub') or contains(@name, 'Register') or contains(@id, 'Register')]",
        "//select[contains(@class, 'sub') or contains(@class, 'register')]"
    ],
    "village_dropdown": [
        "//select[contains(@name, 'village') or contains(@id, 'village')]",
        "//select[contains(@name, 'Village') or contains(@id, 'Village')]",
        "//select[contains(@class, 'village')]"
    ]
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "console_output": True,
    "file_output": True
}

# Excel Configuration
EXCEL_CONFIG = {
    "sheet_names": {
        "form": "Form",
        "lists": "Lists"
    },
    "headers": ["Zone", "District", "Sub Register Office", "Village"],
    "header_style": {
        "font_bold": True,
        "font_size": 12,
        "fill_color": "366092",
        "alignment": "center"
    },
    "max_dropdown_rows": 1000  # Maximum rows for dropdown validation
}

# Data Validation
DATA_VALIDATION = {
    "skip_empty_options": True,
    "skip_placeholder_options": ["select", "choose", "--select--", "--choose--", "---"],
    "trim_whitespace": True,
    "remove_duplicates": True
}

# Error Handling
ERROR_HANDLING = {
    "continue_on_error": True,  # Continue scraping even if some zones/districts fail
    "save_partial_data": True,  # Save data even if scraping is incomplete
    "screenshot_on_error": True,
    "detailed_error_logging": True
}

# Custom User Agent (optional)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Proxy Configuration (if needed)
PROXY_CONFIG = {
    "enabled": False,
    "http_proxy": "",
    "https_proxy": "",
    "no_proxy": "localhost,127.0.0.1"
}

def get_chrome_options():
    """Get Chrome options based on configuration"""
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    
    if BROWSER_CONFIG["headless"]:
        options.add_argument("--headless")
    
    options.add_argument(f"--window-size={BROWSER_CONFIG['window_size']}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-agent={USER_AGENT}")
    
    if PROXY_CONFIG["enabled"]:
        if PROXY_CONFIG["http_proxy"]:
            options.add_argument(f"--proxy-server={PROXY_CONFIG['http_proxy']}")
    
    return options

def validate_config():
    """Validate configuration settings"""
    errors = []
    
    # Validate timeout values
    if BROWSER_CONFIG["timeout"] <= 0:
        errors.append("Browser timeout must be positive")
    
    if SCRAPING_CONFIG["delay_between_selections"] < 0:
        errors.append("Delay between selections cannot be negative")
    
    # Validate file names
    if not OUTPUT_CONFIG["excel_filename"].endswith('.xlsx'):
        errors.append("Excel filename must end with .xlsx")
    
    # Validate selectors
    for selector_type, selectors in SELECTORS.items():
        if not selectors or not isinstance(selectors, list):
            errors.append(f"Selectors for {selector_type} must be a non-empty list")
    
    return errors

if __name__ == "__main__":
    # Validate configuration when run directly
    errors = validate_config()
    if errors:
        print("Configuration Errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Configuration is valid!")
        
    print("\nCurrent Configuration:")
    print(f"Website URL: {WEBSITE_URL}")
    print(f"Headless Mode: {BROWSER_CONFIG['headless']}")
    print(f"Output Excel: {OUTPUT_CONFIG['excel_filename']}")
    print(f"Timeout: {BROWSER_CONFIG['timeout']} seconds")
