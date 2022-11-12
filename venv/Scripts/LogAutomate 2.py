import sys

orig = sys.stdout
with open("logoutput.txt", "wb") as f:
    sys.stdout = f
    try:
        code = compile("LogAutomate.py", f, "exec")
        with contextlib.redirect_stdout(o):
            print("This text will be added to the file")
    finally:
        sys.stdout = orig