from colorama import Fore
from characters.kanji import Kanji

def get_kanji_menu():
    kanji = Kanji(None, None, None, None, None, None)

    while True:
        print()
        print(f"\n{Fore.MAGENTA}=== Kanji Practice Menu ==={Fore.RESET}")
        print(f"{Fore.GREEN}a. Display Kanji Chart{Fore.RESET}")
        print(f"{Fore.GREEN}b. Search Kanji Details by Number{Fore.RESET}")
        print(f"{Fore.GREEN}c. Back to Main Menu{Fore.RESET}")

        choice = input(f"{Fore.YELLOW}Select an option (a-c): {Fore.RESET}").lower()
        print()

        if choice == 'a':
            kanji.display_characters_chart("data/kanji.json")
        elif choice == 'b':
            kanji.search_kanji_by_number()
        elif choice == 'c':
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option (a-c).{Fore.RESET}")
        print()

#get_kanji_menu()