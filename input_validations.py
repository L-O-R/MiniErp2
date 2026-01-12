def get_user_choice(value:list, ab:str):
    print()
    choice = input(f"Select your choice {ab}: ").strip()
    while choice not in value:
        print(f"Please enter a number between {ab} only")
        choice = input(f"Select your choice {ab}: ")
    return int(choice)