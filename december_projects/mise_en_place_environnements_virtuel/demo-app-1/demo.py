import requests
r = requests.get(url="https://openclassrooms.com/fr/")
print(r.status_code)
