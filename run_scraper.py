#!/usr/bin/env python3
"""
Simple runner script for TN Registration Scraper
Provides menu options and handles common tasks
"""

import os
import sys
import subprocess
import argparse

def check_requirements():
    """Check if requirements are installed"""
    try:
        import selenium
        import openpyxl
        import webdriver_manager
        return True
    except ImportError as e:
        print(f"Missing requirement: {e}")
        return False

def install_requirements():
    """Install requirements from requirements.txt"""
    try:
        print("Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")
        return False

def run_test():
    """Run the setup test"""
    try:
        print("Running setup test...")
        result = subprocess.run([sys.executable, "test_setup.py"], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Failed to run test: {e}")
        return False

def run_basic_scraper():
    """Run the basic scraper"""
    try:
        print("Running basic scraper...")
        subprocess.run([sys.executable, "tnreginet_scraper.py"])
    except Exception as e:
        print(f"Failed to run basic scraper: {e}")

def run_enhanced_scraper():
    """Run the enhanced scraper"""
    try:
        print("Running enhanced scraper...")
        subprocess.run([sys.executable, "tnreginet_scraper_enhanced.py"])
    except Exception as e:
        print(f"Failed to run enhanced scraper: {e}")

def show_config():
    """Show current configuration"""
    try:
        print("Current Configuration:")
        subprocess.run([sys.executable, "config.py"])
    except Exception as e:
        print(f"Failed to show config: {e}")

def show_menu():
    """Show interactive menu"""
    print("\n" + "="*50)
    print("TN Registration Department Scraper")
    print("="*50)
    print("1. Install Requirements")
    print("2. Run Setup Test")
    print("3. Show Configuration")
    print("4. Run Basic Scraper")
    print("5. Run Enhanced Scraper (Recommended)")
    print("6. Exit")
    print("="*50)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="TN Registration Scraper Runner")
    parser.add_argument("--install", action="store_true", help="Install requirements")
    parser.add_argument("--test", action="store_true", help="Run setup test")
    parser.add_argument("--config", action="store_true", help="Show configuration")
    parser.add_argument("--basic", action="store_true", help="Run basic scraper")
    parser.add_argument("--enhanced", action="store_true", help="Run enhanced scraper")
    parser.add_argument("--menu", action="store_true", help="Show interactive menu")
    
    args = parser.parse_args()
    
    # Handle command line arguments
    if args.install:
        install_requirements()
        return
    elif args.test:
        run_test()
        return
    elif args.config:
        show_config()
        return
    elif args.basic:
        if check_requirements():
            run_basic_scraper()
        else:
            print("Please install requirements first: python run_scraper.py --install")
        return
    elif args.enhanced:
        if check_requirements():
            run_enhanced_scraper()
        else:
            print("Please install requirements first: python run_scraper.py --install")
        return
    elif args.menu or len(sys.argv) == 1:
        # Interactive menu
        while True:
            show_menu()
            try:
                choice = input("\nEnter your choice (1-6): ").strip()
                
                if choice == "1":
                    install_requirements()
                elif choice == "2":
                    run_test()
                elif choice == "3":
                    show_config()
                elif choice == "4":
                    if check_requirements():
                        run_basic_scraper()
                    else:
                        print("Please install requirements first (Option 1)")
                elif choice == "5":
                    if check_requirements():
                        run_enhanced_scraper()
                    else:
                        print("Please install requirements first (Option 1)")
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter 1-6.")
                    
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                input("\nPress Enter to continue...")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
