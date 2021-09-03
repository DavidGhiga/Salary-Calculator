# Salary Per Hour Converter
# This code converts how much money you make per hour into money made per day, per week, per month and per year!
# DM me on Discord if you have any questions! David™#4383.

print("Welcome To The Salary per Hour Converter!")
salaryperhour = input("How Much Money Do You Make per Hour?")
salaryday = int(salaryperhour) * 8.8
salaryweek = int(salaryperhour) * 44
salarymonth = int(salaryday) * 20.5
salaryyear = int(salaryday) * 220

choice = input("Do you want to find out how much you make per day, per week, per month or per year?")
if choice == "per day":
    print("You make " + str(salaryday) + " dollars per day!")
elif choice == "per week":
    print("You make " + str(salaryweek) + " dollars per week!")
elif choice == "per month":
    print("You make " + str(salarymonth) + " dollars per month!")
elif choice == "per year":
    print("You make " + str(salaryyear) + " dollars per year!")
else:
    print("Please enter a valid choice(e.g. per day; per year)")
