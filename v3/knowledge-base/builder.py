import requests
from typing import List, Dict

# Йде перевірка ліцензії UMLS (3 бізнес дні)
UMLS_API_KEY = 'your_umls_api_key_here'
BASE_URL = 'https://uts-ws.nlm.nih.gov'
SERVICE = 'http://umlsks.nlm.nih.gov' 

# 1. Отримуємо TGT (Ticket Granting Ticket)
def get_tgt(api_key: str) -> str:
    response = requests.post(f'{BASE_URL}/cas/v1/api-key', data={'apikey': api_key})
    return response.headers['location']

# 2. Отримуємо ST (Service Ticket)
def get_st(tgt: str) -> str:
    response = requests.post(tgt, data={'service': SERVICE})
    return response.text

# 3. Шукаємо термін (хворобу або симптом)
def search_umls(term: str, st: str) -> List[Dict]:
    params = {
        'string': term,
        'ticket': st,
        'pageSize': 5,
        'searchType': 'exact'
    }
    response = requests.get(f'{BASE_URL}/rest/search/current', params=params)
    return response.json()['result']['results']

# Приклад виконання
if __name__ == '__main__':
    term = 'pneumonia'
    tgt = get_tgt(UMLS_API_KEY)
    st = get_st(tgt)
    results = search_umls(term, st)
    
    for r in results:
        print(f"{r['ui']}: {r['name']} ({r['rootSource']})")
