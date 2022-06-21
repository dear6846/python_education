import requests

app_id = "b4d57fd5"
app_key = "0f676a46ae61ac6e50972ce3dd815ab8"
language = "en-gb"
word_id = "car"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

print(r)
