
from assets import Hardware, Software
from emploee_management import validate_name, validate_number


def generate_assets_id(asset_dict):
    """GENERATE ASSETS ID"""
    print()
    if not asset_dict:
        return "AS001"

    existing_ids = []
    for asset_id in asset_dict.keys():
        asset_id = int(asset_id.replace("AS", ""))
        existing_ids.append(asset_id)


    next_id = max(existing_ids) + 1

    return f"AS00{next_id}"

def validate_assets_type():
    """VALIDATE ASSETS TYPE"""
    print()
    while True:
        asset_type = input("Enter Asset type: ").strip().lower()
        if not asset_type or asset_type not in ["hardware", "software"]:
            print("Invalid Asset Type (Hardware or Software only)")
            continue
        return asset_type



def add_asset(asset_dict):
    """ADD ASSET"""
    print()
    print("=" * 50)
    print("          Add Assets")
    print("=" * 50)
    print()

    asset_id = generate_assets_id(asset_dict)
    asset_name = validate_name("Enter Asset name: ")
    asset_value = validate_number("Enter Asset value: ")
    asset_type = validate_assets_type()

    if asset_type == "hardware":
        condition = validate_name("Enter Hardware condition: ")
        asset = Hardware(asset_id, asset_name, "hardware",asset_value, condition)
    else:
        expiry_date = validate_name("Enter Hardware expiry date: ")
        asset = Software(asset_id, asset_name,"software", asset_value, expiry_date)

    print()
    print("Assets Added Successfully: ")
    print(asset)
    print()
    asset_dict[asset_id] = asset


def view_all_assets(assets_dict):
    """VIEW ALL EMPLOYEES"""
    print()
    print("=" * 50)
    print("           ALL Assets")
    print("=" * 50)
    print()

    if not assets_dict:
        print("No employees found in the system.")
    else:
        print(f"Total Employees: {len(assets_dict)}")
        print("-" * 50)
        for asset in assets_dict.values():
            print(asset)
            print("-" * 50)

    print()


def assign_asset_to_emp(asset_dict, employees_dict):
    print()
    print("=" * 50)
    print("       Asset Assignment")
    print("=" * 50)
    print()

    if not asset_dict:
        print("No Assets found in the system.")
        return

    if not employees_dict:
        print("No employees found in the system.")
        return

    assets_id = input("Enter Asset ID to be assigned : ")
    if assets_id not in asset_dict:
        print("Invalid Asset ID")
        return

    employees_id = input("Enter Employee ID to be assigned : ")
    if employees_id not in employees_dict:
        print("Invalid Employee ID")
        return

    asset = asset_dict[assets_id]
    employee = employees_dict[employees_id]

    employee.assign_assets(asset)

    employees_dict[employees_id] = employee

    print()
    print("Asset assigned to employee successfully: ")
    print(employee)
    print()

def calculate_assets_depreciation(asset_dict):
    print()
    print("=" * 50)
    print("       Calculate Depreciation")
    print("=" * 50)
    print()

    if not asset_dict:
        print("No Assets found in the system.")
        return

    asset_id = input("Enter Asset ID : ")
    if asset_id not in asset_dict:
        print("Invalid Asset ID")
        return

    asset = asset_dict[asset_id]

    years = validate_number("Enter Years: ")
    deprecated_value = asset.calculate_depreciation(years)
    print()
    print("Deprecated Assets calculated successfully: ")
    print(f"{deprecated_value},.2f")
    print()








