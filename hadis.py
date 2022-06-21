import requests
from  pprint import pprint as print

sura=1
oyat=1
tafsir='uzb-alauddinmansour'
tafsir_ru ='rus-abuadel'
tafsir_ar ='ara-quranbazzi'
url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
url_sura_ru = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir_ru}/{sura}.json"
url_sura_ar = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir_ar}/{sura}.json"
url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"
url_oyat_ru = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir_ru}/{sura}/{oyat}.json"
url_oyat_ar = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir_ar}/{sura}/{oyat}.json"


#sura
r_sura = requests.get(url_sura)
r_sura_ru = requests.get(url_sura_ru)
r_sura_ar = requests.get(url_sura_ar)

res_sura = r_sura.json()
res_sura_ru = r_sura_ru.json()
res_sura_ar = r_sura_ar.json()

print(res_sura)
print(res_sura_ru)
print(res_sura_ar)

#oyat
r_oyat = requests.get(url_oyat)
r_oyat_ru = requests.get(url_oyat_ru)
r_oyat_ar = requests.get(url_oyat_ar)

res_oyat = r_oyat.json()
res_oyat_ru = r_oyat_ru.json()
res_oyat_ar = r_oyat_ar.json()


print(res_oyat['text'])
print(res_oyat_ru['text'])
print(res_oyat_ar['text'])

