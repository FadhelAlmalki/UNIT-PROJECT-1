import random
from colorama import Fore
from utils.json_manager import load_json

def get_fill_in_the_blank_quiz():
    '''Show a random Hiragana/Katakana symbol and ask for its romaji'''
    try:
        hiragana_data = load_json("data/hiragana.json")
        katakana_data = load_json("data/katakana.json")

    except FileNotFoundError:
        print(f"{Fore.RED}Error: JSON file not found.{Fore.RESET}")
        return
    except Exception as e:
        print(f"{Fore.RED}An error occurred while loading the JSON files: {e}{Fore.RESET}")
        return

    characters = list(hiragana_data.values()) + list(katakana_data.values())

    question = random.choice(characters)
    symbol = question.get("symbol", "")
    correct_romaji = question.get("romaji", "").strip().lower()

    print(f"\n{Fore.MAGENTA}===+==( Fill in the Blank Quiz )==+==={Fore.RESET}\n")

    print(f"{Fore.CYAN}Write the romaji for this character:{Fore.RESET}")
    print(f"\n{Fore.YELLOW}{symbol}{Fore.RESET}\n")
    try:
        user_answer = input(f"{Fore.GREEN}Your answer: {Fore.RESET}").strip().lower()

    except Exception as e:
        print(f"{Fore.RED}An error occurred while reading your input: {e}{Fore.RESET}")
        return

    if user_answer == correct_romaji:
        print(f"\n{Fore.GREEN}Correct!{Fore.RESET}")
    else:
        print(f"\n{Fore.RED}Wrong!{Fore.RESET}")
        print(f"{Fore.CYAN}Correct answer: {correct_romaji}{Fore.RESET}")
