Change = 100 - int(input('Input an amount spent in cents\n'))
print(Change)

Quarters,UnsortedChange = divmod(Change,25)
print(str(Quarters) + ' quarters')

Dimes,UnsortedChange = divmod(UnsortedChange,10)
print(str(Dimes) + ' dimes')

Nickels,UnsortedChange = divmod(UnsortedChange,5)
print(str(Nickels) + ' nickels')

print(str(UnsortedChange) + ' pennies')
