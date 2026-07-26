from user import User

def profile_page(logged_in_user):
    print(f"{logged_in_user.name}")
    print(f"{logged_in_user.age}")
    print(f"{logged_in_user.stream}")
    print(f"{logged_in_user.agenda}")
    print(f"{logged_in_user.skills}")
    print(f"{logged_in_user.current_stage}"
    )