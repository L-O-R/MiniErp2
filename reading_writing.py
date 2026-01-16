#============================================================
#Step 1.3 => Read and write from the files
#============================================================
import os
from assets import Hardware, Software
from emplyoee import Employee, Manager


def read_data_from_employee():
    employee_dict ={}

    if not os.path.exists("employee.txt"):
        print("employee.txt file not found. Starting with empty Data")
        return employee_dict

    with open("employee.txt","r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                emp_id = parts[0]
                emp_name = parts[1]
                emp_role = parts[2]
                emp_salary = float(parts[3])
                if emp_role == "manager":
                    emp_bonus = float(parts[4])
                    employee_dict[emp_id] = Manager(emp_id, emp_name, emp_role, emp_salary, emp_bonus)
                else:
                    employee_dict[emp_id] = Employee(emp_id, emp_name, emp_role, emp_salary)
    return employee_dict


def read_data_from_assets():
    assets_dict ={}
    if not os.path.exists("assets.txt"):
        print("assets.txt file not found. Starting with empty Data")
        return assets_dict

    with open("assets.txt","r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                asset_id = parts[0]
                asset_name = parts[1]
                asset_type = parts[2]
                asset_value = float(parts[3])

                if asset_type == "Hardware":
                    assets_condition = parts[4]
                    assets_dict[asset_id] = Hardware(asset_id, asset_name, asset_type, asset_value, assets_condition)
                else:
                    assets_date = parts[4]
                    assets_dict[asset_id] = Software(asset_id, asset_name, asset_type, asset_value, assets_date)
    return assets_dict


def read_data_from_login_cred():
    users_credentials_dict ={}
    if not os.path.exists("login_cred.txt"):
        print("login_cred.txt file not found. Login with admin access only")
        username = "admin"
        password = "1234"
        users_credentials_dict["admin"] = (username, password)
        return users_credentials_dict

    with open("login_cred.txt","r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                user_role = parts[0].strip()
                username = parts[1].strip()
                password = parts[2].strip()
                users_credentials_dict[user_role] = (username, password)

    return users_credentials_dict



