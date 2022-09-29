import re

email  = input("enter your email id: ").strip()

If re.search(r"^\w+@(\w|\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
