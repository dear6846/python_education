
import requests

app_id = "b4d57fd5"
app_key = "0f676a46ae61ac6e50972ce3dd815ab8"
language = "en-gb"

def getDefinitions(word_id):
     url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id().lower()
     r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
     res = r.json()
     if 'error' in res.keys():
         return False

     output = {}
     senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
     definitions = []
     for senses in senses:
        definitions.append(f"-->{senses['definitions'][0]}")
     output["definitions"] = '\n'.join(definitions)

     if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get['audioFile']:
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

     return output
if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinitions('car'))
    print(getDefinitions('bad'))
