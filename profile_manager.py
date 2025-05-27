import json
import os
FILE_PATH = "coffee_profiles.json"

def load_profiles():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4, ensure_ascii=False)
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_profiles(data):
    with open(FILE_PATH,"w", encoding="utf-8") as f:
        json.dump(data,f,indent=4, ensure_ascii=False)

def update_user_profile(username, coffee, time=None):
    profiles = load_profiles()

    if username not in profiles:
        profiles[username] = {
            "total_choices": {},
            "last_choice": coffee,
            "history": []
        }

    tercih_sayilari = profiles[username]["total_choices"]
    tercih_sayilari[coffee] = tercih_sayilari.get(coffee, 0) + 1
    profiles[username]["last_choice"] = coffee

    if time is not None:
        profiles[username]["history"].append({
            "coffee": coffee,
            "time": time
        })

    save_profiles(profiles)


def get_user_profile(username):
    profiles=load_profiles()
    return profiles.get(username, None)
