# Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

dollarAmount = 8.69

piggyBank = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}

# # Your magic Python code here
# That should produce the following output.


def cashToCoins(amount):
  remaining = dollarAmount
  for coin in piggyBank:
    if coin == "quarters":
      value = 0.25
    elif coin == "dimes":
      value = 0.10
    elif coin == "nickels":
      value = 0.05
    elif coin == "pennies":
      value = 0.01
    piggyBank[coin] = remaining // value
    amnt = piggyBank[coin] * value
    # Had to add a rounding because of strange floating digits
    remaining = round(remaining - amnt, 2)
     
cashToCoins(dollarAmount)
print(piggyBank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }