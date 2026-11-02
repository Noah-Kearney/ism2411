# Exercise 1

def calculate_tax(price, rate):
    return price *rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# Exercise 2

def apply_discount(price, rate):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out only manually first, then refractor a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discounts: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200,'gold', 0.07):.2f}")

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 6

x = 100 # apple # Global

def double_it():
    global x
    # x = 999 # another apple (not the same as above)
    return x * 2

print(x)
print(double_it())
print(x)

# Exercise 5

# Error 1 - The code says total = sale instead of total += sale, so it is replacing the total with the most recent sale instead of adding up all the sales in the list
# Error 2 - The code doesn't have a comma after the for loop, so python doesn't know that the code below belongs to the loop
# Error 3 - The code says i <= len(sales) which allows python to reach an index outside of the list. The code needs to be i < len(sales) so it can stay in the proper indexes