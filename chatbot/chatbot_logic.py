import json
import os
import re

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "college_data.json")

def load_data():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)

def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def get_reply(message):
    data = load_data()
    msg = normalize(message)

    # greeting
    if any(w in msg for w in ["hi", "hello", "namaste"]):
        return data["general"]["greeting"]

    # admission
    if "admission" in msg or "apply" in msg:
        return data["admission"]["process"]

    # documents
    if "document" in msg:
        return data["admission"]["documents"]

    # fee
    if "fee" in msg:
        return "Please check Fee Structure 2025 or specify program name."

    # syllabus
    if "syllabus" in msg:
        return "Entrance syllabus is available in downloads section."

    # scholarship
    if "scholarship" in msg:
        return data["scholarship"]["info"]

    # notices
    if "notice" in msg:
        return "\n".join(data["notices"][:3])

    # contact
    if "contact" in msg:
        return f"Phone: {data['general']['phone']} Email: {data['general']['email']}"
    if "Entrance" in msg:
        return data["general"]["entrance_info"]
    

    return "Please ask about admission, fee, syllabus, scholarship, notices or contact."