"""
Page 3: Play history.
"""
from models import VocabularyManager

TITLE = "ประวัติการเล่น 10 เกมล่าสุด"

def build(query=None):
    """Build context dict for page 3."""
    if query is None:
        query = {}

    sample_data = []

    manager = VocabularyManager(sample_data)

    return {
        "history": []
    }