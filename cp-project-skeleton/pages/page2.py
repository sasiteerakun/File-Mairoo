"""
Page 2: Recall and test.
"""
from models import VocabularyManager

TITLE = "แบบทดสอบคำศัพท์"

def build(query=None):
    """Build context dict for page 2."""
    if query is None:
        query = {}

    sample_data = [
        {"word": "security", "length": 8, "difficulty": "easy", "category": "Daily Life", "hint_th": "ความปลอดภัย", "times_used": 0, "is_picked": "no"},
        {"word": "routine", "length": 7, "difficulty": "easy", "category": "Daily Life", "hint_th": "กิจวัตร", "times_used": 0, "is_picked": "no"},
        {"word": "appointment", "length": 11, "difficulty": "easy", "category": "Daily Life", "hint_th": "นัดหมาย", "times_used": 0, "is_picked": "no"},
        {"word": "convenient", "length": 10, "difficulty": "easy", "category": "Daily Life", "hint_th": "สะดวก", "times_used": 0, "is_picked": "no"},
        {"word": "schedule", "length": 8, "difficulty": "easy", "category": "Daily Life", "hint_th": "ตารางเวลา / กำหนดการ", "times_used": 0, "is_picked": "no"},
        {"word": "frequently", "length": 10, "difficulty": "easy", "category": "Daily Life", "hint_th": "บ่อยครั้ง", "times_used": 0, "is_picked": "no"},
        {"word": "occasionally", "length": 11, "difficulty": "easy", "category": "Daily Life", "hint_th": "เป็นครั้งคราว", "times_used": 0, "is_picked": "no"},
        {"word": "prepare", "length": 7, "difficulty": "easy", "category": "Daily Life", "hint_th": "เตรียม", "times_used": 0, "is_picked": "no"},
        {"word": "organize", "length": 8, "difficulty": "easy", "category": "Daily Life", "hint_th": "จัดระเบียบ", "times_used": 0, "is_picked": "no"},
        {"word": "manage", "length": 6, "difficulty": "easy", "category": "Daily Life", "hint_th": "จัดการ", "times_used": 0, "is_picked": "no"},
        {"word": "avoid", "length": 5, "difficulty": "medium", "category": "Daily Life", "hint_th": "หลีกเลี่ยง", "times_used": 0, "is_picked": "no"},
        {"word": "maintain", "length": 8, "difficulty": "medium", "category": "Daily Life", "hint_th": "รักษา / คงไว้", "times_used": 0, "is_picked": "no"},
        {"word": "require", "length": 7, "difficulty": "medium", "category": "Daily Life", "hint_th": "ต้องการ / จำเป็นต้อง", "times_used": 0, "is_picked": "no"},
        {"word": "prefer", "length": 6, "difficulty": "medium", "category": "Daily Life", "hint_th": "ชอบมากกว่า", "times_used": 0, "is_picked": "no"},
        {"word": "available", "length": 9, "difficulty": "medium", "category": "Daily Life", "hint_th": "มีอยู่ / พร้อมใช้งาน", "times_used": 0, "is_picked": "no"},
        {"word": "responsible", "length": 11, "difficulty": "medium", "category": "Daily Life", "hint_th": "รับผิดชอบ", "times_used": 0, "is_picked": "no"},
        {"word": "necessary", "length": 9, "difficulty": "medium", "category": "Daily Life", "hint_th": "จำเป็น", "times_used": 0, "is_picked": "no"},
        {"word": "immediately", "length": 11, "difficulty": "medium", "category": "Daily Life", "hint_th": "ทันที", "times_used": 0, "is_picked": "no"},
        {"word": "ordinary", "length": 8, "difficulty": "medium", "category": "Daily Life", "hint_th": "ธรรมดา / ทั่วไป", "times_used": 0, "is_picked": "no"},
        {"word": "improve", "length": 7, "difficulty": "medium", "category": "Daily Life", "hint_th": "ปรับปรุง / พัฒนา", "times_used": 0, "is_picked": "no"}
    ]

    manager = VocabularyManager(sample_data)

    return {
        "description": "เลือกระดับความยาก",
        "levels": [
            {"name": "ง่าย", "value": "easy", "words": 10, "time": 300},
            {"name": "ปานกลาง", "value": "medium", "words": 20, "time": 600},
            {"name": "ยาก", "value": "hard", "words": 30, "time": 600}
        ]
    }