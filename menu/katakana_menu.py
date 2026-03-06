from characters.katakana import display_katakana_chart, search_katakana_by_romaji

def get_katakana_menu():
    while True:
        print("\n=== Katakana Practice Menu ===")
        print("a. Display Katakana Chart")
        print("b. Search Katakana Character by Romaji")
        print("c. Back to Main Menu")

        choice = input("Select an option (a-c): ").lower()

        if choice == 'a':
            display_katakana_chart()
        elif choice == 'b':
            search_katakana_by_romaji()
        elif choice == 'c':
            break
        else:
            print("Invalid choice. Please select a valid option (a-c).")