from colorama import Fore

from characters.hiragana import Hiragana

def get_hiragana_menu():
    hiragana = Hiragana(None, None, None, None)

    while True:
        print()
        print(f"{Fore.MAGENTA}=== Hiragana Practice Menu ==={Fore.RESET}")
        print(f"{Fore.GREEN}a. Display Hiragana Chart{Fore.RESET}")
        print(f"{Fore.GREEN}b. Search Hiragana Character by Romaji{Fore.RESET}")
        print(f"{Fore.GREEN}c. Back to Main Menu{Fore.RESET}")

        choice = input(f"{Fore.YELLOW}Select an option (a-c): {Fore.RESET}").lower()
        print()

        if choice == 'a':
            hiragana.display_characters_chart("data/hiragana.json")
        elif choice == 'b':
            hiragana.search_kana_by_romaji()
        elif choice == 'c':
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option (a-c).{Fore.RESET}")
        print()

#get_hiragana_menu()