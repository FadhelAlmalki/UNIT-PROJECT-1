from characters.hiragana import display_hiragana_chart, search_hiragana_by_romaji

def get_hiragana_menu():
    while True:
        print("\n=== Hiragana Practice Menu ===")
        print("a. Display Hiragana Chart")
        print("b. Search Hiragana Character by Romaji")
        print("c. Back to Main Menu")

        choice = input("Select an option (a-c): ").lower()

        if choice == 'a':
            display_hiragana_chart()
        elif choice == 'b':
            search_hiragana_by_romaji()
        elif choice == 'c':
            break
        else:
            print("Invalid choice. Please select a valid option (a-c).")

