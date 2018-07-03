import requests
import json

base_url = "https://api.teambition.com/api"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfdXNlcklkIjoiNTc1OTA0ODE0ZjFjMTY4ZTYwM2JjZTQyIiwiYXVkIjoib2F1dGgyIiwiYXV0aFVwZGF0ZWQiOjE1MDYzOTU1MjE3NzMsImNsaWVudEtleSI6ImRkMDg4MTEwLTI5OTgtMTFlOC1iODk3LTYxMzAwYTZjZDAxMCIsImV4cCI6MTU1MjgwNTY3OCwiaWF0IjoxNTIxMjY5Njc4LCJpc3MiOiJhY2NvdW50cyJ9.XmtneSwELPMWkmzgDHJGA6EvQdj6eOcGDuj-zyQs6Pk"
project_id = "590722992a70b4442c3cccd8"
r = requests.get(base_url + "/projects/590722992a70b4442c3cccd8/callink&access_token=" + access_token)
# project_id + "/tasks/?access_token=" + access_token)


print(type(r))
print(type(r.text))
print(r.text)
# d = json.loads(r.text)
