from colorama import Fore
from characters.hiragana import Hiragana

def get_hiragana_menu():
    
    while True:
        print(f"\n{Fore.MAGENTA}===+==( Hiragana Practice Menu )==+==={Fore.RESET}")
        print(f"\n{Fore.GREEN}a. Display Hiragana Chart{Fore.RESET}")
        print(f"{Fore.GREEN}b. Search Hiragana Character by Romaji{Fore.RESET}")
        print(f"{Fore.GREEN}c. Back to Main Menu{Fore.RESET}")
        
        choice = input(f"\n{Fore.YELLOW}Select an option (a-c): {Fore.RESET}").lower()

        if choice == 'a':
            Hiragana.display_characters_chart("data/hiragana.json")
        elif choice == 'b':
            romaji: str = input(f"{Fore.YELLOW}Enter the Romaji reading: {Fore.RESET}").lower()
            result = Hiragana.search_kana_by_romaji(romaji, "data/hiragana.json")

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
                raise ValueError(f"{Fore.RED}No matching Hiragana character found for Romaji '{romaji}'.{Fore.RESET}")
        elif choice == 'c':
            break
        else:
            raise ValueError(f"{Fore.RED}Invalid choice. Please select a valid option (a-c).{Fore.RESET}")

#get_hiragana_menu()