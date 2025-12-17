print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
Phoenix Feather.............$14.99
Time Turner..................$84.99
Enchanted Sword.................$65.99
Potion of Luck..............$11.99
Crystal Ball...................$39.99
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    input('What is the item?')
    input('How much does the item cost?')
    input('How many items are you buying?')
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
subtotal = int('Dragon Egg')
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
tax = int(0.095)
total = subtotal * tax
round(total, 2)

# Print statements
print("--------------------------")
print(f'Dragon Egg x5 @ ${Dragon Egg} each')
print("--------------------------")
print(f'Subtotal: ${subtotal} ')
print(f'Tax: ${tax}')
print(f'Total: ${total}')

print("\nThank you for shopping at\nThe Peculiar Emporium!")
