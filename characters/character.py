class Character:
    '''Base class for all Japanese characters'''
    
    def __init__(self, symbol, strokes, example):
        self.symbol = symbol
        self.strokes = strokes
        self.example = example # dict: word, word_meaning, sentence, translation

    def display_characters_chart(self):
        pass