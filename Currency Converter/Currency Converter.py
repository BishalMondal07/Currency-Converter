with open('CurrentData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currency = parsed[0]
    rate = parsed[1].strip().split()[0]  # Extract the numeric part from the conversion rate
    currencyDict[currency] = float(rate)

amount = float(input("Enter the amount: \n"))
print("Enter the currency you want to convert this amount from? Available options:")
[print(item) for item in currencyDict.keys()]
from_currency = input("Please enter one of these values: ")

if from_currency not in currencyDict:
    print("Invalid currency.")
    exit()

print("Enter the currency you want to convert this amount to? Available options:")
[print(item) for item in currencyDict.keys()]
to_currency = input("Please enter one of these values: ")

if to_currency not in currencyDict:
    print("Invalid currency.")
    exit()

converted_amount = amount * (currencyDict[to_currency] / currencyDict[from_currency])
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency} (Updated on 30th January, 2023)")
