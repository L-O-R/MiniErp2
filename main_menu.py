# ============================================
# PHASE 3: MAIN MENU
# ============================================
from assets import Hardware
from assets_management import add_asset, view_all_assets, assign_asset_to_emp, calculate_assets_depreciation, \
    delete_assets
from company_financial import calculate_total_salary_expenditure, calculate_total_assets_value, \
    generate_company_overview
from emploee_management import add_employee, update_employee, delete_employee, view_all_employees
from emplyoee import Employee, Manager
from input_validations import get_user_choice


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
        choice = get_user_choice(["1","2","3","4", "5"], "(1-5)")

        match choice:
            case 1:
                add_employee(employees_dict)
            case 2:
                view_all_employees(employees_dict)
            case 3:
                update_employee(employees_dict)
            case 4:
                delete_employee(employees_dict)
            case 5:
                input("Press Enter to Go back to Main Menu...")
                break

def manage_assets_menu(assets_dict:dict, employees_dict:dict):
    """
    Sub Menu => Employee Management
    :param employees_dict:
    :return:
    """
    while True:
        print()
        print("=" * 50)
        print("        Assets Management")
        print("=" * 50)
        print()
        print("=" * 50)
        print("1. Add Assets")
        print("2. View all Assets")
        print("3. Assign Assets")
        print("4. Calculate Depreciation")
        print("5. Delete Assets ")
        print("6. Back to Main Menu")
        print("=" * 50)
        print()
        choice = get_user_choice(["1","2","3","4", "5", "6"], "(1-5)")

        match choice:
            case 1:
                add_asset(assets_dict)
            case 2:
                view_all_assets(assets_dict)
            case 3:
                assign_asset_to_emp(assets_dict, employees_dict)
            case 4:
                calculate_assets_depreciation(assets_dict)
            case 5:
                delete_assets(assets_dict)
            case 6:
                input("Press Enter to Go back to Main Menu...")
                break


def company_financial_menu(assets_dict:dict, employees_dict:dict):
    while True:
        print()
        print("=" * 50)
        print("        Company Financials")
        print("=" * 50)
        print()
        print("1. Total Salary Expenditures")
        print("2. Total Assets Value")
        print("3. Company Overview")
        print("4. Back to Main Menu")
        print("=" * 50)
        print()

        choice = get_user_choice(["1", "2", "3", "4"], "(1-4)")
        match choice:
            case 1:
                calculate_total_salary_expenditure(employees_dict)
            case 2:
                calculate_total_assets_value(assets_dict)
            case 3:
                generate_company_overview(assets_dict, employees_dict)
            case 4:
                break

def save_employee_data(employee_dict, filename = "employee.txt"):
    with open(filename, 'w') as f:
        for employee in employee_dict.values():
            if isinstance(employee, Manager):
                line = f'{employee.emp_id}|{employee.emp_name}|{employee.emp_role}|{employee.emp_salary}|{employee.bonus}\n'
            else:
                line = f'{employee.emp_id}|{employee.emp_name}|{employee.emp_role}|{employee.emp_salary}\n'

            f.write(line)

def save_assets_data(assets_dict, filename = "assets.txt"):
    with open(filename, 'w') as f:
        for asset in assets_dict.values():
            if isinstance(asset, Hardware):
                line = f"{asset.get_id}|{asset.get_name}|{asset.get_type}|{asset.get_value}|{asset.physical_condition}\n"
            else:
                line = f"{asset.get_id}|{asset.get_name}|{asset.get_type}|{asset.get_value}|{asset.date}\n"
            f.write(line)



def main_menu_loop(user:tuple, employees_dict:dict, assets_dict:dict):
    while True:
        display_main_menu(user)
        choice = get_user_choice(["1","2","3","4"], "(1-4)")

        match choice:
            case 1:
                print("Loading Employees Menu...")
                manage_employee_menu(employees_dict)
            case 2:
                print("Loading Assets Menu...")
                manage_assets_menu(assets_dict, employees_dict)
            case 3:
                company_financial_menu(assets_dict, employees_dict)
            case 4:
                print("Saving the data")
                c = input("Do you really want to exit? (y/n): ")
                if c.lower() == "y":
                    print()
                    print("Thank you for using the application!")
                    save_assets_data(assets_dict)
                    save_employee_data(employees_dict)
                    print("=" * 50)
                    break
                else:
                    print("Exit cancelled, going back to Main Menu")

    return None


