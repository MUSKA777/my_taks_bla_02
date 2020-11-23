import requests as req
import json
"""
KU = KOMULATIVNÍ POČET UZDRAVENÝCH = Přehled vyléčených dle hlášení krajských hygienických stanic
KZ = KUMULATIVNÍ POČET ZEMŘELÝCH = Přehled úmrtí dle hlášení krajských hygienických stanic
KN = KUMULATIVNÍ POČET NAKAŽENÝCH = Přehled osob s prokázanou nákazou dle hlášení krajských hygienických stanic (v2)
A = AKTUÁLNÍ HODNOTY = Přehled epidemiologické situace dle hlášení krajských hygienických stanic podle okresu
AU = AKTUÁLNÍ POČET NOVĚ UZDRAVENÝCH
AZ = AKTUÁLNÍ POČET NOVĚ ZEMŘELÝCH
AN = AKTUÁLNÍ POČET NOVĚ NAKAŽENÝCH
"""
# <class 'requests.models.Response'>
KU_01 = req.get("https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/vyleceni.json")
KZ_01 = req.get("https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/umrti.json")
KN_01 = req.get("https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/osoby.json")
A_01 = req.get("https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/kraj-okres-nakazeni-vyleceni-umrti.json")

# <class 'dict'>
KU_02 = KU_01.json()
KZ_02 = KZ_01.json()
KN_02 = KN_01.json()
A_02 = A_01.json()


# hodnoty bez hlavicky [{}]
KU = KU_02.pop('data')
KZ = KZ_02.pop('data')
KN = KN_02.pop('data')
A = A_02.pop('data')


"""
KU = dict_keys(['datum', 'vek', 'pohlavi', 'kraj_nuts_kod', 'okres_lau_kod'])
KZ = dict_keys(['datum', 'vek', 'pohlavi', 'kraj_nuts_kod', 'okres_lau_kod'])
KN = dict_keys(['datum', 'vek', 'pohlavi', 'kraj_nuts_kod', 'okres_lau_kod', 'nakaza_v_zahranici', 'nakaza_zeme_csu_kod'])
"""





