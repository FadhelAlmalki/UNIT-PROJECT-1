from utils.json_manager import load_json
from characters.character import Character

class Kanji(Character):
    '''Class for Kanji characters'''

    def __init__(self, symbol, onyomi, kunyomi, meaning, strokes, example):
        super().__init__(symbol, strokes, example)
        self.onyomi = onyomi
        self.kunyomi = kunyomi
        self.meaning = meaning

    @classmethod
    def search_kanji_by_number(cls, number: str, json_path: str):
        '''Search for a Kanji by number and return a Kanji object'''
        if not isinstance(number, str):
            raise ValueError("Number must be a string.")
        
        target = number.strip()
        kanji_data = load_json(json_path)

        if not isinstance(kanji_data, dict):
            raise ValueError("Invalid JSON format: Expected a dictionary of Kanji characters.")

        for key, item in kanji_data.items():
            if key.strip() == target:
                return cls(
                    symbol=item.get("symbol", ""),
                    onyomi=item.get("onyomi", ""),
                    kunyomi=item.get("kunyomi", ""),
                    meaning=item.get("meaning", ""),
                    strokes=item.get("strokes", 0),
                    example=item.get("example", "")
                )

