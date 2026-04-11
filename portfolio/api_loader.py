import requests, json, os

schoolYear = '202526'
course = 12  

# criar pasta
os.makedirs("portfolio/data/api", exist_ok=True)

for language in ['PT']:

    url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'

    payload = {
        'language': language,
        'courseCode': course,
        'schoolYear': schoolYear
    }

    headers = {'content-type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    # guardar curso
    with open(f"portfolio/data/api/curso_{language}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # guardar UCs
    for uc in data['courseFlatPlan']:
        url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'

        payload_uc = {
            'language': language,
            'curricularIUnitReadableCode': uc['curricularIUnitReadableCode'],
        }

        response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
        data_uc = response_uc.json()

        codigo = uc['curricularIUnitReadableCode']

        with open(f"portfolio/data/api/{codigo}.json", "w", encoding="utf-8") as f:
            json.dump(data_uc, f, indent=4, ensure_ascii=False)

print("Dados LIG guardados!")