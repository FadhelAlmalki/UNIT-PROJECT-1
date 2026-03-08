from characters.character import Character

class Kana(Character):
    '''Class for Kana characters (Hiragana and Katakana)'''

    def __init__(self, symbol, romaji, strokes, example):
        super().__init__(symbol, strokes, example)
        self.romaji = romaji
    
    def search_kana_by_romaji(self, romaji):
        pass