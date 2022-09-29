import re

email  = input("enter your email id: ").strip()

matches = re.search(r"^\w+@+(\w|\.)?\.com$", email, re.IGNORECASE)
if matches:
    print("Valid")
else:
    print("Invalid")    