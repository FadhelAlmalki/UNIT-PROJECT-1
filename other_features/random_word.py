import random
from colorama import Fore
from utils.json_manager import load_json

def get_random_word():
    '''Display a random Japanese word'''
    
    words = load_json('data/words.json')

    random_word = random.choice(words)

    print(f"\n{Fore.MAGENTA}===+==( Random Word )==+==={Fore.RESET}\n")
    print(f"{Fore.RED}Word: {Fore.CYAN}{random_word.get('word', 'N/A')}{Fore.RESET}")
    print(f"{Fore.RED}Reading: {Fore.CYAN}{random_word.get('reading', 'N/A')}{Fore.RESET}")
    print(f"{Fore.RED}Romaji: {Fore.CYAN}{random_word.get('romaji', 'N/A')}{Fore.RESET}")
    print(f"{Fore.RED}Meaning: {Fore.CYAN}{random_word.get('meaning', 'N/A')}{Fore.RESET}")
    print(f"{Fore.RED}Example: {Fore.CYAN}{random_word.get('example', 'N/A')}{Fore.RESET}")

