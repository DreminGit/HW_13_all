import requests

response = requests.get("https://api.github.com")

print(response)
print(response.status_code)
#print(response.content)
print(response.text)