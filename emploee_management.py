from emplyoee import Manager, Employee


def validate_name():
    name = input("Enter employee name: ").strip()
    while True:
        if len(name) == 0:
            print("Employee name cannot be empty.")
            name = input("Enter employee name: ").strip()
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
    return f"E{next_num}"







def add_employee(emp_dict):
    print("")
    print("=" * 50)
    print("                 Add new employee")
    print("=" * 50)
    print()
    emp_id = generate_employee_id(emp_dict)
    name = validate_name()
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

def view_employee():
    pass
def delete_employee():
    pass
def update_employee():
    pass



