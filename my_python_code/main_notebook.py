# AUTOGENERATED! DO NOT EDIT! File to edit: 01_main.ipynb (unless otherwise specified).

__all__ = []

# Cell
# Setup in notebook flag.  Useful when you export code and have some situations where you dont want certain part of code run like visulaizations..
import sys,os
try: from nbdev.imports import IN_NOTEBOOK
except: IN_NOTEBOOK=False

if IN_NOTEBOOK :
    print("In Notebooke mode")
else :
    print("Running in batch mode")
    os.chdir("../my_python_code")

# Cell
import my_python_code.library_notebook as funcs


# Cell
print(f"IN_NOTEBOOK = {IN_NOTEBOOK}")