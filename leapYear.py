leap = input("Do you want to input a year or check a range? (input/range): ").strip().lower()

if leap == 'input':

    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        
elif leap == 'range':
    print("Leap years from 2012 to 3040 are:")
    for year in range(2012, 3041):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)
else:
    print("Invalid option. Please select either 'input' or 'range'.")
