from user import User
from database import create_table, get_all_users
from auth import register, login_user
from home import home_page
from search import search_students
print("\n🤝 Let's build, learn, and grow together.")
print("Welcome to Student Connect!")

create_table() # creates the table for users 

users = get_all_users()






print("=====Student Connect=====")
print("1. Register")
print("2. Login")

option = input("Choose an option: ")

if option == "1":
    register()

elif option == "2":
    logged_in_user = login_user()

else:
    print("Invalid Option")
    exit()

users = get_all_users()




search = input("Search A User By Project Description Or Agenda Or Skills: ")

found = False



print("\n========== TERMS & CONDITIONS ==========")
print("1. Be respectful to all users.")
print("2. No spam or advertisements.")
print("3. No fake profiles or impersonation.")
print("4. Do not share personal information unless you trust the other person.")
print("5. Do not send money or valuable items to anyone you meet through Student Connect.")
print("6. Student Connect only helps students connect. We are not responsible for any agreements between users.")



while True:

    agree = input("Do you accept our TERMS AND CONDITION? (y/n): ").lower()

    if agree == "y":
        print("Thanking you for accepting our Terms and Conditions")
        break #exit loop

    elif agree == "n":
        print("You cannot use Student Connect without accepting our TERMS AND CONDITIONS. ")
        

    else:
        print("Please enter only 'y' or 'n': ")

add_users = get_all_users() #get all users from the database




if logged_in_user:
    home_page(logged_in_user)