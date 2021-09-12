from AgeCalculator import AgeCalculator

if __name__ == '__main__':
    ageCalculator = AgeCalculator()
    input_dateOfBirth = input('Enter the date of birth : ')
    ageCalculator.calculate_timedifference(input_dateOfBirth)
    print(ageCalculator.data)

