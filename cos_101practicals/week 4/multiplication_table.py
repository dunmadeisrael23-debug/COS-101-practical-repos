#display a multiplication table from 1 to 12

number = int(input("enter a whole number: "))

print()
print(f"MULTIPLICATION TABLE FOR {number}")
print("==============================")

for multiplier in range (1,13):
    result = number * multiplier
    print(f"{number} * {multiplier} = {result}")
