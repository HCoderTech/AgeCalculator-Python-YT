from datetime import date, datetime
from dateutil import relativedelta
import calendar


class AgeCalculator:
    def __init__(self):
        self.titlename = "Age Calculator"
        self.data = {}
        self.initialize_current_date()

    def initialize_current_date(self):
        self.data['Current_Date'] = {}
        self.data['Current_Date']['Date'] = date.today()
        self.data['Current_Date']['DateStr'] = str(self.data['Current_Date']['Date'].strftime("%d-%m-%Y"))
        self.data['Current_Date']['Day'] = calendar.day_name[self.data['Current_Date']['Date'].weekday()]

    def calculate_timedifference(self, dateOfBirth):
        self.data['Birth_Date'] = {}
        self.data['Birth_Date']['Date'] = datetime.strptime(dateOfBirth, '%d-%m-%Y').date()
        self.data['Birth_Date']['DateStr'] = dateOfBirth
        self.data['Birth_Date']['Day'] = calendar.day_name[self.data['Birth_Date']['Date'].weekday()]

        self.data['Difference'] = {}
        self.data['Difference']['DifferenceData'] = relativedelta.relativedelta(self.data['Current_Date']['Date'],
                                                              self.data['Birth_Date']['Date'])
        self.data['Difference']['Years'] = self.data['Difference']['DifferenceData'].years
        self.data['Difference']['Months'] = self.data['Difference']['DifferenceData'].months
        self.data['Difference']['Days'] = self.data['Difference']['DifferenceData'].days

    def calculate_futurebirthdate(self, year):
        future_birth_date = 'Next_Birth_Date_'+str(year)
        self.data[future_birth_date] = {}
        self.data[future_birth_date]['Date'] = self.data['Birth_Date']['Date'] + relativedelta.relativedelta(years=int(self.data['Difference']['Years'] + year))
        self.data[future_birth_date]['DateStr'] = str(self.data[future_birth_date]['Date'].strftime("%d-%m-%Y"))
        self.data[future_birth_date]['DifferenceData'] = relativedelta.relativedelta(
            self.data[future_birth_date]['Date'],
            self.data['Current_Date']['Date'])
        self.data[future_birth_date]['Rem_Years'] = self.data[future_birth_date]['DifferenceData'].years
        self.data[future_birth_date]['Rem_Months'] = self.data[future_birth_date]['DifferenceData'].months
        self.data[future_birth_date]['Rem_Days'] = self.data[future_birth_date]['DifferenceData'].days
        self.data[future_birth_date]['Day'] = calendar.day_name[self.data[future_birth_date]['Date'].weekday()]

    def calculate_futurebirthdates(self, years):
        for i in range(1,years):
            self.calculate_futurebirthdate(i)



