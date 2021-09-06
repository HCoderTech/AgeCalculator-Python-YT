from datetime import date


class AgeCalculator:
    def __init__(self):
        self.titlename= "Age Calculator"
        self.data={}
        self.initialize_current_date()

    def initialize_current_date(self):
        self.data['Current_Date'] ={}
        self.data['Current_Date']['Date']   = date.today()
        self.data['Current_Date']['DateStr'] = str( self.data['Current_Date']['Date'].strftime("%d-%m-%Y"))