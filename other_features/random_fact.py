import random
from colorama import Fore
from utils.json_manager import load_json

def get_random_fact():
    '''Display a random Japanese fact'''
    try:
        facts = load_json('data/facts.json')

    except FileNotFoundError:
        print(f"{Fore.RED}Error: JSON file not found.{Fore.RESET}")
        return
    except Exception as e:
        print(f"{Fore.RED}An error occurred while loading the JSON file: {e}{Fore.RESET}")
        return

    random_fact = random.choice(facts)

    print(f"\n{Fore.MAGENTA}===+==( Random Fact )==+==={Fore.RESET}\n")
    print(f"{Fore.RED}Fact: {Fore.CYAN}{random_fact.get('fact', 'N/A')}{Fore.RESET}")