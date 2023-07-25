import clear
from art import logo

print(logo)
check = True
bid = {}
prices = []

while check:
    name = str(input("What's your name"))
    bid[name] = int(input("What's your bid?: $"))
    anyone = str(input("Are there any other bidders? Type 'yes' or 'no'"))
    if anyone == 'yes':
        clear
    else:
        check = False

highest_bid = 0
winner = ""
# bidding_record = {"Angela": 123, "James": 321}
for bidder in bid:
    bid_amount = bid[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")
