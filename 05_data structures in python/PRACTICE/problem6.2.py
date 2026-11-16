# Given a dictionary of products and their prices, find the product with the highest price.
products = {
    "Laptop": 65000,
    "Phone": 30000,
    "Tablet": 25000,
    "Monitor": 18000
}

# Find the product with the highest price
highest_product = max(products, key=products.get)

print("Highest priced product:", highest_product)
print("Price:", products[highest_product])

'''Normally, max() compares the items directly
 (which would compare "Laptop" vs "Phone" alphabetically). The key parameter
   gives max() a custom rule to score each item before comparing:
• It passes "Laptop" into products.get("Laptop") → gets 65000
• It passes "Phone" into products.get("Phone") → gets 30000
• It passes "Tablet" into products.get("Tablet") → gets 25000
• It passes "Monitor" into products.get("Monitor") → gets 18000

3. Returning the Original Key

max() compares those returned scores (65000, 30000, 25000, 18000), sees
 that 65000 is the highest, and gives you back the original item that produced 
 it: "Laptop".
(Note: We write products.get without parentheses because we are handing
the function itself to max() so max() can call it later for each item.)'''