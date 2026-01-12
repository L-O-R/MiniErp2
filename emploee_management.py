from emplyoee import Manager, Employee
from input_validations import get_user_choice


def validate_name(text):
    name = input(text).strip()
    while True:
        if len(name) == 0:
            print("Employee name cannot be empty.")
            name = input(text).strip()
        else:
            break
    return name

def validate_employee_role():

    while True:
        role = input("Enter employee role: ").strip().lower()
        if role == "":
            print("Employee role cannot be empty.")
        elif role not in ["manager", "staff", "admin"]:
            print("Employee role can only be Manager, Staff or Admin.")
        else:
            return role


def validate_number (text):
    while True:
        number = input(text).strip()
        if number.isdigit():
            return float(number)
        else:
            print("Add Valid Salary/Bonus")

def generate_employee_id(emp_dict):
    if not emp_dict:
        return "E001"
    emp_id_list = []
    for keys in emp_dict.keys():
        num = int(keys.replace('E', ""))
        emp_id_list.append(num)

    next_num = max(emp_id_list) + 1
    return f"E00{next_num}"







def add_employee(emp_dict):
    print("")
    print("=" * 50)
    print("                 Add new employee")
    print("=" * 50)
    print()
    emp_id = generate_employee_id(emp_dict)
    name = validate_name("Enter employee name: ")
    role = validate_employee_role()
    salary = validate_number("Enter Employee Salary: ")
    if role == "manager":
        bonus = validate_number("Enter the Manager Bonus(Default : 1000)")
        employee = Manager(emp_id,name, role, salary,bonus)
    else:
        employee = Employee(emp_id,name,role,salary)
    print("Employee Add Successfully")
    print()
    emp_dict[emp_id] = employee
    return emp_dict


def view_all_employees(employees):
    """VIEW ALL EMPLOYEES"""
    print()
    print("=" * 50)
    print("           ALL EMPLOYEES")
    print("=" * 50)
    print()

    if not employees:
        print("No employees found in the system.")
    else:
        print(f"Total Employees: {len(employees)}")
        print("-" * 50)
        for employee in employees.values():
            print(employee)
            print("-" * 50)

    print()


def delete_employee(employees):
    """DELETE EMPLOYEE"""
    print()
    print("=" * 50)
    print("           DELETE EMPLOYEE")
    print("=" * 50)
    print()

    if not employees:
        print("No employees found in the system.")
        print()
        return

    emp_id = input("Enter Employee ID to delete: ").strip()

    if emp_id not in employees:
        print(f"Employee with ID '{emp_id}' not found!")
        print()
        return

    employee = employees[emp_id]

    print()
    print("Employee to be deleted:")
    print(employee)
    print()

    confirm = input("Are you sure you want to delete this employee? (yes/no): ").strip().lower()

    if confirm == 'yes' or confirm == 'y':
        del employees[emp_id]
        print()
        print(f"Employee {emp_id} deleted successfully!")
    else:
        print()
        print("Deletion cancelled.")

    print()





def update_employee(employees):
    """UPDATE EMPLOYEES"""
    print()
    print("=" * 50)
    print("           UPDATE EMPLOYEES")
    print("=" * 50)
    print()

    if not employees:
        print("No employees found in the system.")
        print()
        return

    emp_id = input("Enter Employee ID to update: ").strip()

    if emp_id not in employees:
        print(f"Employee with ID '{emp_id}' not found!")
        print()
        return

    employee = employees[emp_id]
    print()
    print("Employee to be updated:")
    print(employee)
    print()

    print("What would you like to update?")
    print("1. Name")
    print("2. Salary")

    if isinstance(employee, Manager):
        print("3. Bonus")
        choice = get_user_choice(["1", "2", "3"], "(1-3)")
    else:
        choice = get_user_choice(["1", "2"], "(1-2)")

    match choice:
        case 1:
            new_name = validate_name("Enter employee name: ")
            employee.emp_name = new_name
            print(f"New employee name: {new_name} (Updated Successfully)")
        case 2:
            new_salary = validate_number("Enter New Salary: ")
            employee.emp_salary = new_salary
            print(f"New employee salary: {new_salary} (Updated Successfully)")
        case 3:
            new_bonus = validate_number("Enter New Bonus(Default : 1000): ")
            employee.bonus = new_bonus
            print(f"New employee bonus: {new_bonus} (Updated Successfully)")

    employees[emp_id] = employee

    print()
    print("-" * 50)
    print("Updated Details: ")
    print(employee)
    print()






