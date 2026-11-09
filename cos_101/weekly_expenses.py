#student weekly expense calculator
#input
student_name = input("Enter Students name: ")
daily_transport_cost = float(input("Enter daily transport cost (naira): "))
daily_feeding_cost = float(input("Enter daily feeding cost (naira): "))
number_of_days_on_campus = int(input("enter number of days on campus: "))
other_weekly_expenses = float(input("Enter other weekly expenses (naira): "))

#process
transporttotal = daily_transport_cost*number_of_days_on_campus
feedingtotal = daily_feeding_cost*number_of_days_on_campus
weeklytotal = transporttotal+feedingtotal+other_weekly_expenses

#output
print(f"Student name: {student_name}")
print(f"Transport total: naira{transporttotal:,.2f}")
print(f"Feeding total: naira{feedingtotal:,.2f}")
print(f"Other expenses: naira{other_weekly_expenses:,.2f}")
print(f"Weekly total: naira{weeklytotal:,.2f}")
