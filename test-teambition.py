# example for post url
# import requests
# postdata =
# {
# 'client_id': "xxxxxxxxxxx" ,
# 'client_secret': "xxxxxx",
# 'code':"xxxxxxxx"
# }
# r = requests.post("https://account.teambition.com/oauth2/access_token",data=postdata)
# print(r.text)

# "access_token"  :
#  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfdXNlcklkIjoiNTc1OTA0ODE0ZjFjMTY4ZTYwM2JjZTQyIiwiYXVkIjoib2F1dGgyIiwiYXV0aFVwZGF0ZWQiOjE1MDYzOTU1MjE3NzMsImNsaWVudEtleSI6ImRkMDg4MTEwLTI5OTgtMTFlOC1iODk3LTYxMzAwYTZjZDAxMCIsImV4cCI6MTU1MjgwNTY3OCwiaWF0IjoxNTIxMjY5Njc4LCJpc3MiOiJhY2NvdW50cyJ9.XmtneSwELPMWkmzgDHJGA6EvQdj6eOcGDuj-zyQs6Pk",
#
# "refresh_token" :
#     "TLkKSIY_)v2l(Gj&PH+p!2IEm0az3*Y1"

# import requests
#
# postdata =
# {
# 'client_id': "dd088110-2998-11e8-b897-61300a6cd010" ,
# 'client_secret': "4c3f76c6-706e-49a8-97cc-6f01d227f843",
# 'code':"73ci2zlt9Of89hleVGyaLhbB"
# }
# r = requests.post("https://account.teambition.com/oauth2/access_token",data=postdata)
# print(r.text)

#code: 73ci2zlt9Of89hleVGyaLhbB
# client_id: dd088110-2998-11e8-b897-61300a6cd010
# client_secret:  4c3f76c6-706e-49a8-97cc-6f01d227f843

import requests
import json

base_url = "https://api.teambition.com/api"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfdXNlcklkIjoiNTc1OTA0ODE0ZjFjMTY4ZTYwM2JjZTQyIiwiYXVkIjoib2F1dGgyIiwiYXV0aFVwZGF0ZWQiOjE1MDYzOTU1MjE3NzMsImNsaWVudEtleSI6ImRkMDg4MTEwLTI5OTgtMTFlOC1iODk3LTYxMzAwYTZjZDAxMCIsImV4cCI6MTU1MjgwNTY3OCwiaWF0IjoxNTIxMjY5Njc4LCJpc3MiOiJhY2NvdW50cyJ9.XmtneSwELPMWkmzgDHJGA6EvQdj6eOcGDuj-zyQs6Pk"
r = requests.get(base_url + "/tasks/me?access_token=" + access_token)


print(type(r))
print(type(r.text))
d = json.loads(r.text)

# print("\n d: ")
# print(type(d))
# print(len(d))

print("\n d[0]")
print(type(d[0]))
print(len(d[0]))

print("\n d[0].keys()")
print(type(d[0].keys()))
print(d[0].keys() )


print("\n d[0].values()")
print(type(d[0].values()))
print(d[0].values())
