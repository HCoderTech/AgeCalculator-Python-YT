import json

from AgeCalculator import AgeCalculator

if __name__ == '__main__':
    ageCalculator = AgeCalculator()
    input_dateOfBirth = input('Enter the date of birth : ')
    ageCalculator.calculate_timedifference(input_dateOfBirth)
    ageCalculator.calculate_futurebirthdates(5)
    print(json.dumps(ageCalculator.data,indent=4, sort_keys=True, default=str))

