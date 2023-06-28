import re

def validate_credit_card(card_number):
    # Check if the card number starts with 4, 5, or 6 and has exactly 16 digits
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$', card_number):
        # Remove hyphens from the card number
        card_number = card_number.replace('-', '')
        # Check if there are no repeating consecutive digits (4 or more times)
        if not re.search(r'(\d)\1{3,}', card_number):
            return 'Valid'
    return 'Invalid'

# Read the number of credit card numbers
N = int(input())

# Iterate over each credit card number
for _ in range(N):
    card_number = input()
    result = validate_credit_card(card_number)
    print(result)
