name = "Ademola"
print(name.upper())

# in built string functions
# .upper - returns string all in uppercase
# .lower - returns string all in lowercase
# .find - returns the index of the first occurrence of the item you're looking for.
# .replace - replaces all occurrence of old substring with new in string

print(name.replace("Ademola", "Bamidele"))

# Choosing lunch

main = {"BLT": 2.30, "Chicken and Bacon": 2.10, "Egg-cress": 1.20,  "Ham and Cheese": 1.00}
snack = {"Crisps": 0.80, "Pancakes": 1.00, "Sausage Roll": 1.20, "Sweets": 1.90}
drink = {"Fanta": 1.00, "Coke": 1.00, "Dr Pepper": 0.90, "Lemonade": 1.20, "Water": 0.70}


main1 = str(input("Select a main"))
snack1 = str(input("Select a snack"))
drink1 = str(input("Select a drink"))


totalcost = main[main1] + snack[snack1] + drink[drink1]
print('This has a cost of ' + str(totalcost) + ' pounds')





