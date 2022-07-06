# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
# following links
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the link : ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
count = int(input("Enter count: "))
position = int(input("Enter position: ")) - 1


print(f"Retrieving: {url}")
while count > 0:
    next_url = tags[position].get("href", None)
    print(f"Retrieving: {next_url}")
    html = urllib.request.urlopen(next_url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    count -= 1
