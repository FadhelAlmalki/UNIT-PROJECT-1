from utils.json_manager import load_json
from characters.character import Character

class Kana(Character):
    '''Class for Kana characters (Hiragana and Katakana)'''

    def __init__(self, symbol, romaji, strokes, example):
        super().__init__(symbol, strokes, example)
        self.romaji = romaji
    
    @classmethod
    def search_kana_by_romaji(cls, romaji: str, json_path: str):
        '''Search for a Kana by Romaji and return a Kana object'''
        if not isinstance(romaji, str):
            raise ValueError("Romaji must be a string.")
        
        target = romaji.strip().lower()
        kana_data = load_json(json_path)

        if not isinstance(kana_data, dict):
            raise ValueError("Invalid JSON format: Expected a dictionary of Kana characters.")

        for item in kana_data.values():
            if str(item.get("romaji", "")).strip().lower() == target:
                return cls(
                    symbol=item.get("symbol", ""),
                    romaji=item.get("romaji", ""),
                    strokes=item.get("strokes", 0),
                    example=item.get("example", "")
                )