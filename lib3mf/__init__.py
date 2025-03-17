import os
import sys
import platform

# Ensure that your Lib3MF.py wraps around the shared library correctly
from .Lib3MF import *  # Import necessary classes/functions from your Lib3MF.py

# Your existing logic to use the library
def get_wrapper():
    try:
        # No need to modify lib_path here; just use it directly in your wrapper
        return Wrapper(get_library_path_for_wrapper())
    except ELib3MFException as e:
        print("Failed to initialize the Lib3MF wrapper: ", e, file=sys.stderr)
        raise
