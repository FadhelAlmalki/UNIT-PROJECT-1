import random
from colorama import Fore
from utils.json_manager import load_json

def get_fill_in_the_blank_quiz():
    '''Show a random Hiragana/Katakana symbol and ask for its romaji'''

    hiragana_data = load_json("data/hiragana.json")
    katakana_data = load_json("data/katakana.json")

    characters = list(hiragana_data.values()) + list(katakana_data.values())

    question = random.choice(characters)

    symbol = question.get("symbol", "")
    correct_romaji = question.get("romaji", "").strip().lower()

    print(f"\n{Fore.MAGENTA}===+==( Fill in the Blank Quiz )==+==={Fore.RESET}\n")

    print(f"{Fore.CYAN}Write the romaji for this character:{Fore.RESET}")
    print(f"\n{Fore.YELLOW}{symbol}{Fore.RESET}\n")

    user_answer = input(f"{Fore.GREEN}Your answer: {Fore.RESET}").strip().lower()

    if user_answer == correct_romaji:
        print(f"\n{Fore.GREEN}Correct!{Fore.RESET}")
    else:
        print(f"\n{Fore.RED}Wrong!{Fore.RESET}")
        print(f"{Fore.CYAN}Correct answer: {correct_romaji}{Fore.RESET}")
