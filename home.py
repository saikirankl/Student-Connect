from search import search_students
from profile import profile_page
from edit_profile import edit_profile

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
        print("6. 🖋️  Edit Profile")

        choice = input("Choice: ")

        if choice == "1":
            search = search_students()

        elif choice == "2":
            print("Create a team page coming soon...")
            break

        elif choice == "3":
            print("Search page coming soon...")
            break

        elif choice == "4":
            profile = profile_page(logged_in_user)
            break

        elif choice == "5":
            print("Logout page coming soon...")

        elif choice == "6":
            edit_profile(logged_in_user)

        else:
            print("Invalid choice.")