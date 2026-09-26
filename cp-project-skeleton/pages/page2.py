"""
Page 2: Recall and test.
"""
import json
from pages.page1 import build as build_page1

TITLE = "แบบทดสอบคำศัพท์"

def build(query=None):
    """Build context dict for page 2."""
    if query is None:
        query = {}

    page1_data = build_page1()

    words = []

    for category in page1_data["categories"]:
        for item in category["words"]:
            parts = item.split(" = ", 1)

            word = parts[0]
            hint_and_pos = parts[1]

            hint_parts = hint_and_pos.rsplit(" (", 1)

            hint_th = hint_parts[0]
            part_of_speech = hint_parts[1].rstrip(")") if len(hint_parts) > 1 else ""

            words.append({
                "word": word,
                "hint_th": hint_th,
                "part_of_speech": part_of_speech
            })

    return {
        "description": "เลือกระดับความยาก",
        "levels": [
            {"name": "ง่าย", "value": "easy", "words": 10, "time": 300},
            {"name": "ปานกลาง", "value": "medium", "words": 20, "time": 600},
            {"name": "ยาก", "value": "hard", "words": 30, "time": 600}
        ],
        "words_json": json.dumps(words, ensure_ascii=False)
    }