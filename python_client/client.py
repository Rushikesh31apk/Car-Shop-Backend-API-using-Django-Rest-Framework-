import requests

endpoints="http://127.0.0.1:8000/car/carlist/"
getresponce=requests.get(endpoints)
print(getresponce.json())
print(getresponce.status_code)