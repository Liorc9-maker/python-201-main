import requests

min_len = 4
max_len = 6
URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}"

response = requests.get(URL)
print(response.text)
