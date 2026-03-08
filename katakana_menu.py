from colorama import Fore
from characters.katakana import Katakana

def get_katakana_menu():
    katakana = Katakana(None, None, None, None)

    while True:
        print(f"\n{Fore.MAGENTA}=== Katakana Practice Menu ==={Fore.RESET}")
        print(f"{Fore.GREEN}a. Display Katakana Chart{Fore.RESET}")
        print(f"{Fore.GREEN}b. Search Katakana Character by Romaji{Fore.RESET}")
        print(f"{Fore.GREEN}c. Back to Main Menu{Fore.RESET}")

        choice = input(f"{Fore.YELLOW}Select an option (a-c): {Fore.RESET}").lower()

        if choice == 'a':
            katakana.display_characters_chart('data/katakana.json')
        elif choice == 'b':
            katakana.search_kana_by_romaji()
        elif choice == 'c':
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option (a-c).{Fore.RESET}")

#get_katakana_menu()