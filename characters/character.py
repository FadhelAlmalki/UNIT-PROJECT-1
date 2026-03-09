from colorama import Fore
from utils.json_manager import load_json

class Character:
    '''Base class for all Japanese characters'''
    
    def __init__(self, symbol, strokes, example):
        self.symbol = symbol
        self.strokes = strokes
        self.example = example # dict: word, word_meaning, sentence, translation
    
    @classmethod
    def display_characters_chart(cls, json_path: str):
        '''Display a chart of characters'''
        try:    
            characters = load_json(json_path)
        except FileNotFoundError:
            print(f"{Fore.RED}Error: JSON file not found at '{json_path}'.{Fore.RESET}")
            return
        except Exception as e:
            print(f"{Fore.RED}An error occurred while loading the JSON file: {e}{Fore.RESET}")
            return
        
        print()
        count = 0
        for key, value in characters.items():
            print(f"{Fore.RED}{key}: {Fore.CYAN}{value['symbol']:<2} {Fore.RESET}", end="      ")
            count += 1
            if count % 5 == 0:
                print()
                
        print()