import requests
import datetime
import pandas


API_NUTRI = "e6dfc67baaae81671021875e9f04d2f5"
APP_ID_NUTRI = "c63c3e42"

API_DOCS_GET = "https://api.sheety.co/59c0621c007ce2ee83f5bfe51df90b9d/workoutDay38/arkusz1"

API_DOCS_POST = "https://api.sheety.co/59c0621c007ce2ee83f5bfe51df90b9d/workoutDay38/arkusz1"


current_date = datetime.datetime.now()
nutri_params = {
    "query": input("What exercise did you do today?: "),
    "gender": "male",
    "weight_kg": "98",
    "height_cm": "185",
    "age": "26"
}

nutri_url = f"https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_headers = {
    "x-app-id": APP_ID_NUTRI,
    "x-app-key": API_NUTRI,
    "x-remote-user-id": "0"
}

resposne = requests.post(url=nutri_url, headers=nutri_headers, json=nutri_params )
# resposne.raise_for_status()
result = (resposne.json()["exercises"])
print(result)
date =current_date.strftime("%d/%m/%Y")
time = current_date.strftime("%X")
header = {
    "Content-Type": "application/json"
}



for exercise in result:
    doc_params = {
        # "detail": "POST",
        "arkusz1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }

    }
    new_data = pandas.DataFrame.from_dict(doc_params)
    print(new_data)
    # doc_response = requests.post(API_DOCS_POST, json=doc_params, headers=header)
    # # doc_response.raise_for_status()
    # print(doc_response.json())