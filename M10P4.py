# Train ticket price based on miles from downtown Chicago using a function


def ticket_price(miles):
    if miles >= 30:
        price = 12.00
    elif miles >= 20:
        price = 10.00
    elif miles >= 10:
        price = 8.00
    else:
        price = 5.00
    return price


total_tickets = 0

response = input("Do you want to do this program? (Yes/No): ")

while response.lower() == "yes":
    last_name = input("Enter last name: ")
    miles = float(input("Enter miles from downtown Chicago: "))

    price = ticket_price(miles)
    total_tickets = total_tickets + price

    print("Last name:", last_name)
    print("Ticket price: $" + format(price, ",.2f"))

    response = input("Do you want to do this again? (Yes/No): ")

print("Sum of all ticket prices: $" + format(total_tickets, ",.2f"))
