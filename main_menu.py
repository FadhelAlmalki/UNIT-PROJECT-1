from colorama import Fore
from hiragana_menu import get_hiragana_menu
from katakana_menu import get_katakana_menu
from kanji_menu import get_kanji_menu
from other_features.random_word import get_random_word
from other_features.mcq import get_mcq
from other_features.fill_in_the_blank_quiz import get_fill_in_the_blank_quiz
from other_features.random_fact import get_random_fact
from other_features.guide import get_guide

#print("🇯🇵 "*50)

def main_menu():
    while True:
        print(f"\n{Fore.MAGENTA}===+==( Main Menu )==+==={Fore.RESET}")
        print(f"\n{Fore.GREEN}1. Practice Hiragana{Fore.RESET}")
        print(f"{Fore.GREEN}2. Practice Katakana{Fore.RESET}")
        print(f"{Fore.GREEN}3. Practice Kanji{Fore.RESET}")
        print(f"{Fore.GREEN}4. Random Word{Fore.RESET}")
        print(f"{Fore.GREEN}5. Multiple Choice Quiz (correct romaji/meaning Quiz){Fore.RESET}")
        print(f"{Fore.GREEN}6. Fill-in-the-Blank Quiz (Hiragana & Katakana Romaji Quiz){Fore.RESET}")
        print(f"{Fore.GREEN}7. Random Fact / Cultural Insight{Fore.RESET}")
        print(f"{Fore.GREEN}8. Help{Fore.RESET}")
        print(f"{Fore.GREEN}9. Exit{Fore.RESET}")

        choice = input(f"\n{Fore.YELLOW}Select an option (1-9): {Fore.RESET}")

        if choice == '1':
            get_hiragana_menu()
        elif choice == '2':
            get_katakana_menu()
        elif choice == '3':
            get_kanji_menu()
        elif choice == '4':
            get_random_word()
        elif choice == '5':
            get_mcq()
        elif choice == '6':
            get_fill_in_the_blank_quiz()
        elif choice == '7':
            get_random_fact()
        elif choice == '8':
            get_guide()
        elif choice == '9':
            print(f"\n{Fore.RED}Exiting the program. Goodbye!{Fore.RESET}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option (1-9).{Fore.RESET}")

if __name__ == "__main__":
    main_menu()