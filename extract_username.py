import re

url  = input("enter url: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    username = matches.group(1)

print(f"username: {username}")
