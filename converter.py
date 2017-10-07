#currency converter like google
import math

rates = {
    "usd" : 1,
    "inr" : 65.44,
    "cad" : 1.25,
    "eur" : 0.85,
    "gbp" : 0.77,
    "yen" : 112.63
}

#Logic

#print("200 INR to CAD = %.3f" % ((200 / rates["inr"]) * rates["cad"]))
#print("3 INR to USD = %.3f" % (3 / rates["inr"]))

userQuery = {
    'currencyValue' : '',
    'fromCurrency' : '',
    'toCurrency' : ''
}

userInput = input("Enter the query : ").lower()
splittedInput = userInput.split(" ")

#Put the data into the list
userQuery['currencyValue'] = float(splittedInput[0])
userQuery['fromCurrency'] = str(splittedInput[1])
userQuery['toCurrency'] = str(splittedInput[3])

if userQuery['toCurrency'] == 'usd':
    result = userQuery['currencyValue'] / rates['inr']
    print("%.3f" % result)
else:
    result = (userQuery['currencyValue'] / rates[userQuery['fromCurrency']]) * rates[userQuery['toCurrency']]
    print("%.3f" % result)
