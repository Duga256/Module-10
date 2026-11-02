# Next month's sales forecast using a function


def compute_forecast(month, sales):
    month = month[:3].lower()

    if month in ("jan", "feb", "mar"):
        forecast_percent = 0.10
    elif month in ("apr", "may", "jun"):
        forecast_percent = 0.15
    elif month in ("jul", "aug", "sep"):
        forecast_percent = 0.20
    else:
        forecast_percent = 0.25

    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales


response = input("Do you want to do this program? (Yes/No): ")

while response.lower() == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month (Jan - Dec): ")
    sales = float(input("Enter sales: "))

    next_sales = compute_forecast(month, sales)

    print("Last name:", last_name)
    print("Next month's sales forecast: $" + format(next_sales, ",.2f"))

    response = input("Do you want to do this again? (Yes/No): ")
