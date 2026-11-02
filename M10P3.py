# Out the door price of a car using a function


def out_the_door_price(msrp, make, model, electric):
    if electric.upper() == "Y":
        percent_off = 0.30
    elif make.lower() == "honda" and model.lower() == "accord":
        percent_off = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        percent_off = 0.15
    else:
        percent_off = 0.05

    discount = msrp * percent_off
    new_msrp = msrp - discount
    total = new_msrp + new_msrp * 0.07
    return total


total_msrp = 0
total_sales = 0

response = input("Do you want to do this program? (Yes/No): ")

while response.lower() == "yes":
    make = input("Enter make: ")
    model = input("Enter model: ")
    electric = input("Is it an electric vehicle? (Y or N): ")
    msrp = float(input("Enter MSRP: "))

    total = out_the_door_price(msrp, make, model, electric)

    total_msrp = total_msrp + msrp
    total_sales = total_sales + total

    print("Out the door price: $" + format(total, ",.2f"))

    response = input("Do you want to do this again? (Yes/No): ")

print("Sum of all MSRPs: $" + format(total_msrp, ",.2f"))
print("Sum of all sales prices: $" + format(total_sales, ",.2f"))
