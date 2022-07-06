# JSON
import json
import urllib.request
count = 0

url = "http://py4e-data.dr-chuck.net/comments_1543946.json"
opened = urllib.request.urlopen(url)
data = opened.read()

info = json.loads(data)
for item in info["comments"]:
    number = int(item["count"])
    count = count + number
print(count)
