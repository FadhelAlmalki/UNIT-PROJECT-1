from colorama import Fore
from characters.katakana import Katakana

def get_katakana_menu():

    while True:
        print(f"\n{Fore.MAGENTA}===+==( Katakana Practice Menu )==+==={Fore.RESET}")
        print(f"\n{Fore.GREEN}a. Display Katakana Chart{Fore.RESET}")
        print(f"{Fore.GREEN}b. Search Katakana Character by Romaji{Fore.RESET}")
        print(f"{Fore.GREEN}c. Back to Main Menu{Fore.RESET}")

        choice = input(f"\n{Fore.YELLOW}Select an option (a-c): {Fore.RESET}").lower()

        if choice == 'a':
            Katakana.display_characters_chart('data/katakana.json')
        elif choice == 'b':
            romaji: str = input(f"{Fore.YELLOW}Enter the Romaji reading: {Fore.RESET}").lower()
            result = Katakana.search_kana_by_romaji(romaji, "data/katakana.json")

            if result:
                print(f"\n{Fore.RED}---+- Character Information -+---{Fore.RESET}\n")
                print(f"{Fore.RED}Character: {result.symbol}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Romaji: {result.romaji}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Strokes: {result.strokes}{Fore.CYAN}{Fore.RESET}")
                print(f"\n{Fore.RED}---+- Example: -+---{Fore.RESET}\n")
                print(f"{Fore.RED}Word: {result.example['word']}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Meaning in English: {result.example['word_meaning']}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Sentence: {result.example['sentence']}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Meaning in English: {result.example['translation']}{Fore.CYAN}{Fore.RESET}")

            else:
                print(f"{Fore.RED}No matching Katakana character found for Romaji '{romaji}'.{Fore.RESET}")
        elif choice == 'c':
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option (a-c).{Fore.RESET}")

#get_katakana_menu()