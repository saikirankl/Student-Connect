from user import User
from database import update_user


def edit_profile(logged_in_user):

    while True:

        print("\n======Edit Profile======")

        print("1. Name")
        print("2. Age")
        print("3. Stream")
        print("4. Agenda")
        print("5. Skills")
        print("6. Current Stage")
        print("7. Back")

        choice = input("Choose: ")

        if choice == "1":

            logged_in_user.name = input("New Name: ")
            update_user(logged_in_user)
            print("Profile Updated Successfully ✅")
            break

        elif choice == "2":
            
            logged_in_user.age = int(input("Age: "))
            update_user(logged_in_user)
            print("Profile Updated Successfully ✅")
            break

        elif choice == "3":
            logged_in_user.stream = input("Stream: ")
            update_user(logged_in_user)
            print("Profile Updated Successfully ✅")
            break

        elif choice == "4":
            logged_in_user.agenda = input("Agenda: ")
            update_user(logged_in_user)
            print("Profile Updated Successfully ✅")
            break


        elif choice == "5":
            logged_in_user.skills = input("Skills: ")
            update_user(logged_in_user)
            print("Profile Updated Successfully ✅")
            break


        elif choice == "6":
            logged_in_user.current_stage = input("Current Stage: ")
            update_user(logged_in_user)
            print("Profile Updated Successfully ✅")
            break


        elif choice == "7":
            break

        else:
            print("Invalid Choice")