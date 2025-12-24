#============================================================
#Step 1.2 => Assets Class
#============================================================

class Assets:
    def __init__(self, assets_id:str, asset_name:str, asset_type:str, asset_value: float):
        self.__assets_id = assets_id
        self.__asset_name = asset_name
        self.__asset_type = asset_type
        self.__asset_value = asset_value

    @property
    def get_id(self):
        return self.__assets_id

    @property
    def get_name(self):
        return self.__asset_name

    @property
    def get_type(self):
        return self.__asset_type

    @property
    def get_value(self):
        return self.__asset_value

    def calculate_depreciation(self, years):
        """calculate depreciation for given years (10% per year)"""
        return self.get_value * (0.9 ** years)


    def get_details(self):
        return f"ID: {self.__assets_id} | Name: {self.__asset_name} | Type: {self.__asset_type} | Value: {self.get_value}"

    def __str__(self):
        return self.get_details()

    def __add__(self, other):
        return self.__asset_value + other.__value


class Hardware(Assets):
    def __init__(self,assets_id:str, asset_name:str, asset_type:str, asset_value: float, physical_condition:str =  "good"):
        super().__init__(assets_id, asset_name, asset_type, asset_value)
        self.__physical_condition = physical_condition

    @property
    def physical_condition(self):
        return self.__physical_condition

    def get_details(self):
        base_details = super().get_details()
        return base_details + f" | Physical condition: {self.physical_condition}"



class Software(Assets):
    def __init__(self,assets_id:str, asset_name:str, asset_type:str, asset_value: float, date:str):
        super().__init__(assets_id, asset_name, asset_type, asset_value)
        self.__date = date

    @property
    def date(self):
        return self.__date

    def get_details(self):
        base_details = super().get_details()
        return base_details + f" | Expiry Date: {self.date}"
