from datetime import date, datetime
from dateutil import relativedelta


class AgeCalculator:
    def __init__(self):
        self.titlename = "Age Calculator"
        self.data = {}
        self.initialize_current_date()

    def initialize_current_date(self):
        self.data['Current_Date'] = {}
        self.data['Current_Date']['Date'] = date.today()
        self.data['Current_Date']['DateStr'] = str(self.data['Current_Date']['Date'].strftime("%d-%m-%Y"))

    def calculate_timedifference(self, dateOfBirth):
        self.data['Birth_Date'] = {}
        self.data['Birth_Date']['Date'] = datetime.strptime(dateOfBirth, '%d-%m-%Y').date()
        self.data['Birth_Date']['DateStr'] = dateOfBirth
        self.data['Difference'] = {}
        self.data['Difference']['DifferenceData'] = relativedelta.relativedelta(self.data['Current_Date']['Date'],
                                                              self.data['Birth_Date']['Date'])
        self.data['Difference']['Years'] = self.data['Difference']['DifferenceData'].years
        self.data['Difference']['Months'] = self.data['Difference']['DifferenceData'].months
        self.data['Difference']['Days'] = self.data['Difference']['DifferenceData'].days

