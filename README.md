# TN Registration Department Web Scraper

This comprehensive Python automation project uses Selenium to extract hierarchical dropdown data from the Tamil Nadu Registration Department website (www.tnreginet.gov.in) and creates Excel files with the extracted data.

## 🚀 Features

- **Automated Navigation**: Navigates through the website to reach the Encumbrance Certificate (EC) page
- **Language Selection**: Automatically selects English language
- **Hierarchical Data Extraction**: Extracts Zone → District → Sub Register Office → Village relationships
- **Excel Generation**: Creates Excel files with extracted data and basic dropdown functionality
- **Error Handling**: Comprehensive error handling with detailed logging
- **Data Summary**: Generates text summaries of all extracted data
- **Configuration Management**: Customizable settings through configuration files
- **Multiple Script Versions**: Basic and enhanced versions with different feature sets
- **Interactive Runner**: Easy-to-use menu system for running different components

## 📁 Project Structure

```
tnreginet-scraper/
├── requirements.txt                    # Python dependencies
├── config.py                          # Configuration settings
├── tnreginet_scraper.py               # Basic scraper script
├── tnreginet_scraper_enhanced.py      # Enhanced scraper with config support
├── test_setup.py                      # Setup validation script
├── run_scraper.py                     # Interactive runner script
└── README.md                          # This file
```

## 📋 Prerequisites

- Python 3.7 or higher
- Chrome browser installed
- Internet connection
- Windows, macOS, or Linux

## 🛠️ Installation

### Quick Start

1. **Download/Clone the project files**

2. **Run the interactive setup**:
   ```bash
   python run_scraper.py
   ```
   Then select option 1 to install requirements.

### Manual Installation

1. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the setup**:
   ```bash
   python test_setup.py
   ```

## 🎯 Usage

### Interactive Menu (Recommended)

```bash
python run_scraper.py
```

This will show an interactive menu with options to:
1. Install Requirements
2. Run Setup Test
3. Show Configuration
4. Run Basic Scraper
5. Run Enhanced Scraper (Recommended)
6. Exit

### Command Line Usage

```bash
# Install requirements
python run_scraper.py --install

# Run setup test
python run_scraper.py --test

# Show configuration
python run_scraper.py --config

# Run basic scraper
python run_scraper.py --basic

# Run enhanced scraper
python run_scraper.py --enhanced
```

### Direct Script Execution

```bash
# Basic version
python tnreginet_scraper.py

# Enhanced version (recommended)
python tnreginet_scraper_enhanced.py
```

## 📊 Script Versions

### Basic Scraper (`tnreginet_scraper.py`)
- Core functionality
- Fixed configuration
- Basic error handling
- Simple Excel output

### Enhanced Scraper (`tnreginet_scraper_enhanced.py`)
- **Recommended version**
- Configurable through `config.py`
- Advanced error handling and recovery
- Detailed logging
- Screenshot capture on errors
- Retry mechanisms
- Better Excel formatting

## ⚙️ Configuration

The enhanced scraper uses `config.py` for customization:

### Key Configuration Options

```python
# Browser settings
BROWSER_CONFIG = {
    "headless": False,          # Set to True for background execution
    "timeout": 30,              # Element wait timeout
    "window_size": "1920,1080"  # Browser window size
}

# Output settings
OUTPUT_CONFIG = {
    "excel_filename": "tnreginet_data.xlsx",
    "summary_filename": "tnreginet_data_summary.txt",
    "create_summary": True,
    "create_excel": True
}

# Scraping behavior
SCRAPING_CONFIG = {
    "delay_between_selections": 2,  # Delay between dropdown selections
    "max_retries": 3,               # Retry attempts for failed operations
    "screenshot_on_error": True     # Capture screenshots on errors
}
```

## 📄 Output Files

### 1. Excel File (`tnreginet_data.xlsx`)
- **Form Sheet**: User interface with headers and zone dropdown
- **Lists Sheet**: All extracted data organized in columns
- **Named Ranges**: Excel named ranges for potential cascading dropdowns
- **Instructions**: Usage guidelines within the file

### 2. Summary File (`tnreginet_data_summary.txt`)
- Human-readable hierarchical data structure
- Complete Zone → District → Sub Register → Villages mapping
- Extraction statistics and timestamps

### 3. Log File (`tnreginet_scraper.log`)
- Detailed execution logs with timestamps
- Error messages and debugging information
- Progress tracking for each extraction step

### 4. Screenshots (on errors)
- Automatic screenshot capture when errors occur
- Timestamped filenames for easy identification
- Helpful for debugging website structure changes

## 🔧 Customization

### Modifying Selectors

Update element selectors in `config.py`:

```python
SELECTORS = {
    "zone_dropdown": [
        "//select[contains(@name, 'zone')]",
        "//select[contains(@id, 'zone')]"
    ],
    # Add more selectors as needed
}
```

### Changing Output Format

The scripts can be easily modified for different output formats:

```python
# JSON output
import json
with open('data.json', 'w') as f:
    json.dump(self.data, f, indent=2)

# CSV output
import pandas as pd
df = pd.DataFrame(flattened_data)
df.to_csv('data.csv', index=False)
```

### Adding New Data Fields

1. Update dropdown selectors in `config.py`
2. Modify the extraction logic in the scraper
3. Update Excel generation to include new fields

## 🐛 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| ChromeDriver not found | Script auto-downloads ChromeDriver; ensure Chrome is installed |
| Website structure changed | Update selectors in `config.py` |
| Network timeouts | Increase timeout values in configuration |
| Element not found | Check website manually and update selectors |
| Permission errors | Run with appropriate permissions or use virtual environment |

### Debug Mode

1. **Enable verbose logging**:
   ```python
   LOGGING_CONFIG["level"] = "DEBUG"
   ```

2. **Disable headless mode**:
   ```python
   BROWSER_CONFIG["headless"] = False
   ```

3. **Enable screenshots**:
   ```python
   SCRAPING_CONFIG["screenshot_on_error"] = True
   ```

### Getting Help

1. Check the log file for detailed error information
2. Run the setup test: `python test_setup.py`
3. Verify configuration: `python config.py`
4. Check if the website is accessible manually

## 📊 Data Structure

The extracted data follows this hierarchical structure:

```json
{
    "Zone1": {
        "District1": {
            "SubRegister1": ["Village1", "Village2", "Village3"],
            "SubRegister2": ["Village4", "Village5"]
        },
        "District2": {
            "SubRegister3": ["Village6", "Village7"]
        }
    },
    "Zone2": {
        "District3": {
            "SubRegister4": ["Village8", "Village9"]
        }
    }
}
```

## 📈 Excel Cascading Dropdowns

### Current Implementation
- Basic dropdown for zones
- Named ranges for all hierarchical data
- Instructions and metadata included

### Advanced Implementation (Manual)
For full cascading functionality, you can:

1. Use INDIRECT formulas in Excel:
   ```excel
   # District dropdown (B2): =INDIRECT(A2)
   # Sub Register dropdown (C2): =INDIRECT(A2&"_"&B2)
   # Village dropdown (D2): =INDIRECT(A2&"_"&B2&"_"&C2)
   ```

2. Create dependent dropdown lists using Excel's Data Validation feature

## 🔒 Legal and Ethical Considerations

- ✅ Educational and research purposes
- ✅ Respects website terms of service
- ✅ Implements reasonable delays between requests
- ✅ Does not overload the server
- ✅ Follows robots.txt guidelines

## 🚀 Performance Tips

1. **Use headless mode** for faster execution
2. **Adjust delays** based on website responsiveness
3. **Enable retry mechanisms** for unstable connections
4. **Use virtual environments** to avoid dependency conflicts
5. **Monitor log files** for optimization opportunities

## 🔄 Version History

| Version | Features |
|---------|----------|
| **v1.0** | Basic scraping functionality |
| **v1.1** | Enhanced error handling and logging |
| **v1.2** | Configuration management system |
| **v1.3** | Interactive runner and setup validation |
| **v1.4** | Advanced Excel formatting and named ranges |

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues, questions, or contributions:

1. **Check the documentation** in this README
2. **Review log files** for detailed error information
3. **Run diagnostics** using `test_setup.py`
4. **Verify configuration** using `config.py`
5. **Test manually** on the target website

## 📝 License

This project is provided for educational and research purposes. Please ensure compliance with the target website's terms of service and applicable laws.

---

**Happy Scraping! 🎉**
