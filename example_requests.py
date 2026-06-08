# Fazer chamadas com requests: GET, POST, sessões, cookies, headers customizados

# Praticar: consumir uma API pública (ex: JSONPlaceholder ou ViaCEP)

# import requests
# import json

# r = requests.get("https://jsonplaceholder.typicode.com/posts")

# print(r.status_code)
# print(r.text)

# json_text = r.text

# data_list = json.loads(json_text)

# for item in data_list:
#     print(item)
#     if item["id"] == 10:
# break

# r = requests.get("https://viacep.com.br/ws/95012301/json")

# print(r.status_code)
# print(r.text)
# print(f"o bairro é {r.json()['bairro']}")
