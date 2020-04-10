stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

"""
Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

Example output for one block: I purchased General Electric stock for $4800

Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

Example output:

------ GE ------
100 shares at 48 dollars each on 01-jul-1998
200 shares at 56 dollars each on 10-sep-2001

Total value of stock in portfolio: $16000
"""

print("----- Personal Purchase History -----")
for purchase in purchases:
    abbreviation = purchase[0]
    name = stockDict[abbreviation]
    shares = purchase[1]
    date = purchase[2]
    price = purchase[-1]
    sentence = f"I purchased {name} stock for ${price}"
    print(sentence)

for abbreviation,company in stockDict.items():
  print(f"----- {company} -----")
  total = 0
  for purchase in purchases:
    if purchase[0] == abbreviation:
        shares = purchase[1]
        date = purchase[2]
        price = purchase[-1]
        total += price * shares
        sentence = f"{shares} shares at ${price} each on {date}"
        print(sentence)
  print(f"Total value of stock in portfolio: ${total}")