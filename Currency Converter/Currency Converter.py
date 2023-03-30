with open('CurrentData.txt') as f :
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter the name of the amount: \n"))
print("Enter the currency you want to convert this amount to ? Available options")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values : ")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency} (Updated on 30th January, 2023)")