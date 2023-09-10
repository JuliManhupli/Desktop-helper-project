import requests


api_url = 'http://numbersapi.com/'
nomber = "43"

response = requests.get(api_url + nomber)   # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)