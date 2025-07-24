print("Welcome to the tip calculator!")

bill = float(input("What is the total bill? : "))

tip = float(input("Enter the percentage of tip you would like to give : "))

people = int(input("How many people to split the bill? : "))

costPerPerson = (bill + bill*tip*0.01) / people

print(f"Each person should pay: ${costPerPerson}")