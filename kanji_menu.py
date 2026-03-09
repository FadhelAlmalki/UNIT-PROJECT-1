from colorama import Fore
from characters.kanji import Kanji

def get_kanji_menu():

    while True:
        print(f"\n{Fore.MAGENTA}===+==( Kanji Practice Menu )==+==={Fore.RESET}")
        print(f"\n{Fore.GREEN}a. Display Kanji Chart{Fore.RESET}")
        print(f"{Fore.GREEN}b. Search Kanji Character Details by Number{Fore.RESET}")
        print(f"{Fore.GREEN}c. Back to Main Menu{Fore.RESET}")

        choice = input(f"\n{Fore.YELLOW}Select an option (a-c): {Fore.RESET}").lower()

        if choice == 'a':
            Kanji.display_characters_chart("data/kanji.json")
        elif choice == 'b':
            number: str = input(f"{Fore.YELLOW}Enter the Kanji number: {Fore.RESET}").lower()
            result = Kanji.search_kanji_by_number(number, "data/kanji.json")

            if result:
                print(f"\n{Fore.RED}---+- Character Information -+---{Fore.RESET}\n")
                print(f"{Fore.RED}Character: {result.symbol}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Onyomi: {result.onyomi}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Kunyomi: {result.kunyomi}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Meaning in English: {result.meaning}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Strokes: {result.strokes}{Fore.CYAN}{Fore.RESET}")
                print(f"\n{Fore.RED}---+- Example: -+---{Fore.RESET}\n")
                print(f"{Fore.RED}Word: {result.example['word']}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Meaning in English: {result.example['word_meaning']}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Sentence: {result.example['sentence']}{Fore.CYAN}{Fore.RESET}")
                print(f"{Fore.RED}Meaning in English: {result.example['translation']}{Fore.CYAN}{Fore.RESET}")

            else:
                raise ValueError(f"{Fore.RED}No matching Kanji character found for number '{number}'.{Fore.RESET}")
        elif choice == 'c':
            break
        else:
            raise ValueError(f"{Fore.RED}Invalid choice. Please select a valid option (a-c).{Fore.RESET}")

#get_kanji_menu()