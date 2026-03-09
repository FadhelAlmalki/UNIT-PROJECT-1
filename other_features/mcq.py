import random
from colorama import Fore
from utils.json_manager import load_json

def get_mcq():
    '''MCQ quiz: show a Hiragana/Katakana symbol and ask for the correct romaji'''
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

    all_romaji = list({char.get("romaji", "").strip().lower() for char in characters})
    wrong_romaji = [romaji for romaji in all_romaji if romaji != correct_romaji]

    wrong_choices = random.sample(wrong_romaji, 3)
    choices = wrong_choices + [correct_romaji]
    random.shuffle(choices)

    option_letters = ['a', 'b', 'c', 'd']
    options = dict(zip(option_letters, choices))

    print(f"\n{Fore.MAGENTA}===+==( Multiple Choice Quiz )==+==={Fore.RESET}\n")
    print(f"{Fore.CYAN}What is the correct romaji for this symbol?{Fore.RESET}")
    print(f"\n{Fore.YELLOW}{symbol}{Fore.RESET}\n")

    for letter, romaji in options.items():
        print(f"{Fore.GREEN}{letter}.{Fore.RESET} {Fore.CYAN}{romaji}{Fore.RESET}")

    user_answer = input(f"\n{Fore.YELLOW}Select an option (a-d): {Fore.RESET}").strip().lower()

    if user_answer not in options:
        raise ValueError(f"{Fore.RED}Invalid choice. Please select a valid option (a-d).{Fore.RESET}")

    if options[user_answer] == correct_romaji:
        print(f"\n{Fore.GREEN}Correct!{Fore.RESET}")
    else:
        print(f"\n{Fore.RED}Wrong!{Fore.RESET}")
        print(f"{Fore.CYAN}Correct answer: {correct_romaji}{Fore.RESET}")