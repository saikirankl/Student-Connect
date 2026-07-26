from user import User
print("Hello, Welcome to Student Connect")
print("Before we start, lets get some information")

from database import create_table, add_user, get_all_users

create_table() # creates the table for users 


users = get_all_users() #get all users from the database

choice = "y"

while choice == "y":
    print("\n======Student Connect======")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    stream = input("Enter your stream: ")
    projectdescription = input("Enter your project description: ")
    agenda = input("what is your agenda: ")
    skills = input("Enter your skills: ")


    print("\nCurrent Stage Of Your Project 🚀")
    print("1. 🌱 New Starter")
    print("2. 💡 I have an idea")
    print("3. 🤝 Looking for a team")
    print("4. 🏗️ Already Building Projects")
    print("5. 🚀 Ready to Launch")
    print("6. ✍️ Not mentioned above")

    current_stage = input("Select your current stage (1-6): ")

    if current_stage == "1":
        current_stage = "🌱 New Starter"

    elif current_stage == "2":
        current_stage = "💡 I have an idea"

    elif current_stage == "3":
        current_stage = "🤝 Looking for a team"

    elif current_stage == "4":
        current_stage = "🏗️ Already Building Projects"

    elif current_stage == "5":
        current_stage = "🚀 Ready to Launch"

    elif current_stage == "6":
        current_stage = input("Please specify your stage: ")

    new_user = User(
                    user_name,
                    password,
                    name,
                    age,
                    stream,
                    projectdescription,
                    agenda,
                    skills,
                    current_stage
                     )

    users.append(new_user)   #temorary
    add_user(new_user) #permanent

    
    


    choice = input("Add another user? (y/n) : ").lower()
    
    while choice != "y" and choice != "n":
        choice = input("Please enter a valid choice (y/n): ").lower()

    if choice == "y":
        print("Ok, Let's add another user")

    elif choice == "n":    
        print("Ok, lets finish it")

users = get_all_users() #get all users from the database


for user in users:
    print("--------------------")
    print(f"{user.name}'s information")
    print("--------------------")
    print("Name:", user.name)
    print("Age:", user.age)
    print("Stream:", user.stream)
    print("Project Description:", user.projectdescription)
    print("Agenda:", user.agenda)
    print("Skills:", user.skills)
    print("--------------------")



search = input("Search A User By Project Description Or Agenda Or Skills: ")

found = False


for user in users:
    if search.lower() in user.projectdescription.lower() or search.lower() in user.agenda.lower() or search.lower() in user.skills.lower():
         print("--------------------")
         print(f"{user.name}'s information")
         print(f"{user.age} Age")
         print(f"{user.stream} Stream")
         print(f"{user.projectdescription} ProjectDescription")
         print(f"{user.agenda} Agenda")
         print(f"{user.skills} Skills")
         print("--------------------")
         found = True

if not found:
    print("No user found with the given search criteria.") 


add_users = get_all_users() #get all users from the database
