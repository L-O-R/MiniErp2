#============================================================
#Step 1.1 => Emplyoees Class
#============================================================

class Employee:
    def __init__(self,emp_id:str, name:str, role:str, salary:float ):
        self.__emp_id = emp_id #private members(encalpsulation)
        self.__name = name
        self.__role = role
        self.__salary = salary
        self.__assigned_assets = [] # list to store the assigned assets

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def emp_name(self):
        return self.__name

    @emp_name.setter
    def emp_name(self,name):
        self.__name = name

    @property
    def emp_role(self):
        return self.__role

    @emp_role.setter
    def emp_role(self, role):
        self.__role = role

    @property
    def emp_salary(self):
        return self.__salary

    @emp_salary.setter
    def emp_salary(self, salary:float):
        self.__salary = salary

    @property
    def assigned_assets(self):
        return self.__assigned_assets

    def assign_assets(self, assets):
        self.__assigned_assets.append(assets)

    def get_details(self):

        if len(self.__assigned_assets) > 0:
            # assets_assigned = "|".join(assets)
            return f"ID: {self.__emp_id} | Name: {self.__name} | Role: {self.__role} | Salary: {self.__salary} | Assigned Assets: {self.__assigned_assets}"
        return f"ID: {self.__emp_id} | Name: {self.__name} | Role: {self.__role} | Salary: {self.__salary} | Assigned Assets: NO Assets Given"
    def __str__(self):
        return self.get_details()
    def __repr__(self):
        return self.get_details()


class Manager(Employee):
    def __init__(self, emp_id:str, name:str, role:str, salary:float , bonus:float = 1000):
        super().__init__(emp_id , name, role, salary)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus
    @bonus.setter
    def bonus(self, bonus:float):
        self.__bonus = bonus


    @property
    def total_payment(self):
        return self.__bonus + self.emp_salary

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Bonus: {self.bonus}"



# emp_dict = {
#     "Em001": {
#         name, role, salary, bonus
#     }
# }


