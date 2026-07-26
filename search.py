from database import get_all_users


def search_students():


        users = get_all_users()
        
        search = input("Search A User By Project Description Or Agenda Or Skills: ")

        found = False

        for user in users:
            if search.lower() in user.projectdescription.lower() or search.lower() in user.agenda.lower() or search.lower() in user.skills.lower():
                print("--------------------")
                print("👤 "f"{user.name}'s information")
                print("🔢 "f"{user.age} Age")
                print("🎓 "f"{user.stream} Stream")
                print("📝 "f"{user.projectdescription} ProjectDescription")
                print("🎯 "f"{user.agenda} Agenda")
                print("💻 "f"{user.skills} Skills")
                print(f"{user.current_stage} Current Stage")
                print("--------------------")
                found = True

        if not found:
            print("No user found with the given search criteria.")