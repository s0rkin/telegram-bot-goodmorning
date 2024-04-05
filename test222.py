import requests

response = requests.get("https://api.elphen.site/api?mode=default_my_poolkey")
if response.status_code == 200:
    FreeAI_Pool_Token=response.json()

print(FreeAI_Pool_Token)