from user import User
from database import add_user, login

def register():
    choice = "y"

    while choice == "y":

        print("\n======Register =====")

        user_name = input("User Name: ")
        password = input("Password: ")
        name = input("Name: ")
        age = int(input("Enter your age 🔢 : "))
        stream = input("Enter your stream 📚 : ")
        projectdescription = input("Enter your project description ✍️  : ")
        agenda = input("what is your agenda 🚀 : ")
        skills = input("Enter your skills 🥷 : ")


        print("\nCurrent Stage Of Your Project 🚀")
        print("1. 🌱 New Starter")
        print("2. 💡 I have an idea")
        print("3. 🤝 Looking for a team")
        print("4. 🏗️ Already Building Projects")
        print("5. 🚀 Ready to Launch")
        print("6. ✍️  Not mentioned above")

        current_stage = input("Select your current stage (1-6): ")

        if current_stage == "1":
            current_stage = "🌱 New Starter"

        elif current_stage == "2":
            current_stage = "💡 I have an idea"

        elif current_stage == "3":
            current_stage = "🤝 Looking for a team"

        elif current_stage == "4":
            current_stage = "🛠️ Already Building Projects"

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

        
        add_user(new_user) #permanent

        print("Registration Successful!")

        choice = input("Add another user? (y/n) : ").lower()



def login_user():
    

    while True:

        user_name = input("Username: ")
        password = input("Password: ")

        logged_in_user = login(user_name, password)

        if logged_in_user:
            print(f"Welcome {logged_in_user.name} 🎉")
            return logged_in_user
    
        else:
            print("Invalid username or password")