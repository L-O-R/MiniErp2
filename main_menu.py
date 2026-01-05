# ============================================
# PHASE 3: MAIN MENU
# ============================================
from emploee_management import add_employee, update_employee, delete_employee, view_employee


def display_main_menu(user:tuple):
    print()
    print("=" * 50)
    print(f"                 Welcome {user[0]}!")
    print("=" * 50)
    print()
    print("=" * 50)
    print("1. Manage Employees")
    print("2. Manage Assets")
    print("3. Company Financials")
    print("4. Save & Exit")
    print("=" * 50)

def get_user_choice(value:list):
    print()
    choice = input("Select your choice (1-4): ").strip()
    while choice not in value:
        print("Please enter a number between 1 and 4 only")
        choice = input("Select your choice (1-4): ")
    return int(choice)

def manage_employee_menu(employees_dict:dict):
    """
    Sub Menu => Employee Management
    :param employees_dict:
    :return:
    """
    while True:
        print()
        print("=" * 50)
        print("        Employee Management")
        print("=" * 50)
        print()
        print("=" * 50)
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Back to Main Menu")
        print("=" * 50)
        print()
        choice = get_user_choice(["1","2","3","4", "5"])

        match choice:
            case 1:
                add_employee(employees_dict)
            case 2:
                view_employee()
            case 3:
                update_employee()
            case 4:
                delete_employee()
            case 5:
                break



def main_menu_loop(user:tuple, employees_dict:dict):
    while True:
        display_main_menu(user)
        choice = get_user_choice(["1","2","3","4"])

        match choice:
            case 1:
                print("Loading Employees Data...")
                manage_employee_menu(employees_dict)
            case 2:
                print("Loading Assets Data...")
            case 3:
                print("Loading Company Financial Data...")
            case 4:
                print("Saving the data")
                c = input("Do you really want to exit? (y/n): ")
                if c.lower() == "y":
                    print()
                    print("Thank you for using the application!")
                    print("=" * 50)
                    break
                else:
                    print("Exit cancelled, going back to Main Menu")

    return None



main_menu_loop(("john", ""), {})