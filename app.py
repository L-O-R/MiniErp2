# ============================================
# NEXGEN CORPORATE ECOSYSTEM (NCE)
# PHASE 1: THE STARTUP (The Loading Phase)
# ============================================

"""
PHASE 1 LOADING DATA:
-------------------
Before the user sees ANYTHING on screen, the program needs to "wake up."

What happens here:
1. Check if data files exist (employees.txt, assets.txt)
2. If files exist → Read them and convert text back into Python Objects
3. If files don't exist → Start with empty dictionaries
4. Prepare the system for user interaction

Think of this like a computer booting up - it needs to load everything
into memory (RAM) before you can use it.
"""
from main_menu import main_menu_loop

"""
PHASE 2 EXPLANATION:
-------------------
After the system boots up, the user sees a LOGIN SCREEN.

What happens here:
1. User is prompted for Username and Password
2. System verifies credentials against stored data
3. User has MAXIMUM 3 attempts
4. After 3 failed attempts → System locks and closes
5. On success → Move to Main Menu (Phase 3)

This is SECURITY - prevents unauthorized access to the system.
"""

"""
PHASE 3 Main Menu:
-------------------
After successful login, user sees the MAIN MENU.

What happens here:
1. Display 4 main options
2. User selects an option (1-4)
3. System executes the chosen action
4. After action completes → Return to Main Menu (LOOP)
5. Only "Save & Exit" breaks the loop

This is the CENTRAL HUB - all navigation starts here.
"""

from reading_writing import read_data_from_employee, read_data_from_assets, read_data_from_login_cred


# =================================================================
# phase 1.4
# =================================================================
def start_up_phase():
    """
    Phase1 :Boot system and load all data into memory
    :return: assets_dict, employee_dict
    """
    print("=" * 50)
    print("NEXGEN CORPORATE ECOSYSTEM")
    print("Booting System Up")
    print("=" * 50)
    print()

    print("Loading Employees Data.....")
    employee_dict = read_data_from_employee()

    print("Loading Assets Data.....")
    assets_dict = read_data_from_assets()

    return employee_dict, assets_dict

def login_phase():
    user_cred = read_data_from_login_cred()
    print("=" * 50)
    print("  Login Required ! ")
    print("=" * 50)
    print()

    max_attempts = 3
    attempt_count = 1
    role = input("Please enter your role: ").strip()
    while attempt_count <= max_attempts:
        print(f"Login attempt #{attempt_count} out of {max_attempts}")
        # input str data type return the values
        # need to handle the error
        if role in user_cred[role]:
            username = input("Username: ").strip()
            if username == user_cred[role][0]:
                password = input("Password: ").strip()
                if password == user_cred[role][1]:
                    return username, role
                else:
                    print("Invalid Credentials")
                    attempt_count += 1
            else:
                print("Invalid Username! Try Again")
                attempt_count += 1
    return None

if __name__ == "__main__":
    employee_dict, assets_dict = start_up_phase()
    login = login_phase()
    if login is None:
        print("=" * 50)
        print("Security Lockdown")
        print("Max Attempt reached , Application Shutting down...")
        print("=" * 50)
    else:
        print()
        print("=" * 50)
        print("All System Operational")
        print("=" * 50)
        print()
        print("Employee Management Active")
        print("Assets Management Active")
        # print("Company financial Active")
        # print("Data save and Exit")
        print()

        exit_requested = main_menu_loop(login, employee_dict, assets_dict)

