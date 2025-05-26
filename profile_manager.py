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


def update_user_profile(username, preference ):
    profiles=load_profiles()
    if username not in profiles:
        profiles[username] = {
            "all_preference":{},
            "end_preference": preference
        }
    preferences=profiles[username] ["all_preference"]
    preferences[preference]=preferences.get(preference,0)+1
    profiles[username]["end_preference"]=preference

def get_user_profile(username):
    profiles=load_profiles()
    return profiles.get(username, None)

