"""
Models for the Vocabulary Memory Training Game.
"""

class Item:
    """
    Class representing a vocabulary item in the game.
    Matches data.json schema: word, length, difficulty, category, hint_th, times_used, is_picked
    """

    def __init__(self, data: dict):
        self.word = data.get("word", "")
        self.length = int(data.get("length", len(self.word)))
        self.difficulty = data.get("difficulty", "easy")
        self.category = data.get("category", "noun")
        self.hint_th = data.get("hint_th", "")
        self.times_used = int(data.get("times_used", 0))
        self.is_picked = data.get("is_picked", "no")

    def to_dict(self) -> dict:
        """Convert Item instance back to a dictionary format."""
        return {
            "word": self.word,
            "length": self.length,
            "difficulty": self.difficulty,
            "category": self.category,
            "hint_th": self.hint_th,
            "times_used": self.times_used,
            "is_picked": self.is_picked
        }

    def mark_as_picked(self):
        """Mark the item as picked and increment times_used."""
        self.is_picked = "yes"
        self.times_used += 1

    def reset_picked(self):
        """Reset is_picked status."""
        self.is_picked = "no"

    def is_easy(self) -> bool:
        """Check if difficulty is easy."""
        if self.difficulty == "easy":
            return True
        else:
            return False


class VocabularyManager:
    """
    Manager class to handle operations over multiple Item instances.
    Provides filtering, search, and loop operations required by project criteria.
    """

    def __init__(self, items_data: list):
        self.items = []
        for data in items_data:
            if isinstance(data, dict):
                self.items.append(Item(data))

    def filter_by_difficulty(self, target_difficulty: str) -> list:
        """Filter words by difficulty using a loop and if/else structure."""
        filtered = []
        for item in self.items:
            if item.difficulty == target_difficulty:
                filtered.append(item.to_dict())
            else:
                continue
        return filtered

    def filter_by_category(self, target_category: str) -> list:
        """Filter words by category using a loop and if/else structure."""
        filtered = []
        for item in self.items:
            if item.category == target_category:
                filtered.append(item.to_dict())
            else:
                continue
        return filtered

    def get_unpicked_items(self) -> list:
        """Get items where is_picked is 'no'."""
        unpicked = []
        for item in self.items:
            if item.is_picked == "no":
                unpicked.append(item)
            else:
                pass
        return unpicked

    def reset_all_picked(self):
        """Reset is_picked status for all items using a loop."""
        for item in self.items:
            item.reset_picked()