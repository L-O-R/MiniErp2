from assets import Hardware
from emplyoee import Manager


def calculate_total_salary_expenditure(emplyoees_dict):
    print()
    if not emplyoees_dict:
        print("No employees found")
        return

    print()
    print("   Total Salary Expenditure")
    print('=' * 50)

    total_expenditure = 0
    staff_count = 0
    manager_count = 0

    print("Employees BreakDown: ")
    print("-" * 50)
    for employee in emplyoees_dict.values():
        if isinstance(employee, Manager):
            manager_count += 1
            pay = employee.total_payment
            print(employee)
        else:
            staff_count += 1
            pay = employee.emp_salary
            print(employee)
        total_expenditure  += pay
        print('-' * 50)

    print()
    print(f"Total Employees = {len(emplyoees_dict)}")
    print(f"Total Staff = {staff_count}")
    print(f"Total Manager = {manager_count}")
    print()
    print(f" Total Monthly Expenditure = {total_expenditure}")
    print(f" Total Yearly Expenditure = {total_expenditure * 12}")
    print()


def calculate_total_assets_value (assets_dict):
    print()
    if not assets_dict:
        print("No assets found")
        return
    print()
    print("   Total Assets Value")
    print('=' * 50)

    total_assets_value = 0
    hardware_count = 0
    hardware_expenditure = 0
    software_count = 0
    software_expenditure = 0

    for asset in assets_dict.values():
        if isinstance(asset, Hardware):
            hardware_count += 1
            value = asset.get_value
            hardware_expenditure += value
        else:
            software_count += 1
            value = asset.get_value
            software_expenditure += value
        total_assets_value += value
    print('-' * 50)
    print(f' Total Assets {len(assets_dict)}')
    print(f'Total Hardware = {hardware_count}')
    print(f'Total Hardware Expenditure = {hardware_expenditure}')
    print(f'Total Software {software_count}')
    print(f' Total Software Expenditure = {software_expenditure}')
    print()
    print(f" Total Assets Value = {total_assets_value}")
    print()


def generate_company_overview(assets_dict, employee_dict):
    print()
    print("   Company Overview")
    print()

    total_salary_expenditure = 0
    total_assets_value = 0

    for employee in employee_dict.values():
        if isinstance(employee, Manager):
            total_salary_expenditure += employee.total_payment
        else:
            total_salary_expenditure += employee.emp_salary

    for asset in assets_dict.values():
        total_assets_value += asset.get_value


    print()
    print('-' * 50)
    print(f" Total Employees = {len(employee_dict)}")
    print(f" Total Salary Expenditure = {total_salary_expenditure:.2f}")
    print()
    print(f"Total Assets {len(assets_dict)}")
    print(f" Total Assets Value = {total_assets_value:.2f}")
    print()



