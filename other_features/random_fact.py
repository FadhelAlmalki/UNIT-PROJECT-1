import random
from colorama import Fore
from utils.json_manager import load_json

def get_random_fact():
    '''Display a random Japanese fact'''
    
    facts = load_json('data/facts.json')

    random_fact = random.choice(facts)

    print(f"\n{Fore.MAGENTA}===+==( Random Fact )==+==={Fore.RESET}\n")
    print(f"{Fore.RED}Fact: {Fore.CYAN}{random_fact.get('fact', 'N/A')}{Fore.RESET}")