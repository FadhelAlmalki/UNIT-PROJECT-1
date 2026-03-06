from menu.hiragana_menu import get_hiragana_menu
from menu.katakana_menu import get_katakana_menu
from menu.kanji_menu import get_kanji_menu
from random_word import get_random_word
from mcq import get_mcq
from fill_in_the_blank_quiz import get_fill_in_the_blank_quiz
from random_fact import get_random_fact
from guide import get_guide

#print("🇯🇵 "*50)

core_functions = '''
1. Practice Hiragana
2. Practice Katakana
3. Practice Kanji
4. Random Word
5. Multiple Choice Quiz (correct romaji/meaning Quiz)
6. Fill-in-the-Blank Quiz (Hiragana & Katakana Romaji Quiz)
7. Random Fact / Cultural Insight
8. Help
9. Exit
'''
#print(core_functions)

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Practice Hiragana")
        print("2. Practice Katakana")
        print("3. Practice Kanji")
        print("4. Random Word")
        print("5. Multiple Choice Quiz (correct romaji/meaning Quiz)")
        print("6. Fill-in-the-Blank Quiz (Hiragana & Katakana Romaji Quiz)")
        print("7. Random Fact / Cultural Insight")
        print("8. Help")
        print("9. Exit")

        choice = input("Select an option (1-9): ")

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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-9).")
