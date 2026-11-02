# Assessed value of a home by county using a function


def assessed_value(county, market_value):
    county = county.lower()

    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70

    return market_value * percent


total_market = 0
total_assessed = 0

response = input("Do you want to do this program? (Yes/No): ")

while response.lower() == "yes":
    county = input("Enter county: ")
    market_value = float(input("Enter market value of the home: "))

    assessed = assessed_value(county, market_value)

    total_market = total_market + market_value
    total_assessed = total_assessed + assessed

    print("Assessed value: $" + format(assessed, ",.2f"))

    response = input("Do you want to do this again? (Yes/No): ")

print("Sum of all market values: $" + format(total_market, ",.2f"))
print("Sum of all assessed values: $" + format(total_assessed, ",.2f"))
