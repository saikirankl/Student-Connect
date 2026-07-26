def home_page(logged_in_user):

    while True:
        print("\n=================")
        print(f"👋 Welcome, {logged_in_user.name}")
        print("=================")

        print("1. 🔎 Search Students")
        print("2. 👥 Create Team")
        print("3. 💬 Messages")
        print("4. 👤 Profile")
        print("5. 🚪 Logout")

        choice = input("Choice: ")

        if choice == "1":
            search = search_students

        elif choice == "2":
            print("Create a team page coming soon...")
            break

        elif choice == "3":
            print("Search page coming soon...")
            break

        elif choice == "4":
            print("Profile page coming soon...")
            break

        else:
            print("Invalid choice.")