from characters.character import Character

class Kanji(Character):
    '''Class for Kanji characters'''

    def __init__(self, symbol, onyomi, kunyomi, meaning, strokes, example):
        super().__init__(symbol, strokes, example)
        self.onyomi = onyomi
        self.kunyomi = kunyomi
        self.meaning = meaning

    @classmethod
    def search_kanji_by_number(cls, number):
        pass

