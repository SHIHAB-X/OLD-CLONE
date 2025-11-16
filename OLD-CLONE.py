#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OLD CLONE TOOL - ENTRY POINT
Run: python OLD-CLONE.py
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Import the main module
    import old
    
    # Check if main function exists
    if hasattr(old, 'main'):
        old.main()
    elif hasattr(old, '_0xmain'):
        old._0xapproval_screen()
    elif hasattr(old, '_0xapproval_screen'):
        old._0xapproval_screen()
    else:
        print("\033[1;91m[!] Error: main() function not found in old.py")
        sys.exit(1)
        
except ImportError as e:
    print("\033[1;91m[!] Error: old.py file not found!")
    print(f"\033[1;93m[*] Details: {e}")
    print("\033[1;96m[*] Make sure old.py exists in the same directory")
    sys.exit(1)
    
except Exception as e:
    print(f"\033[1;91m[!] Unexpected Error: {e}")
    sys.exit(1)
