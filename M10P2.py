# Paint needed for the walls (and bonus: ceiling) of a room using functions


def wall_square_footage(length, width, height):
    return 2 * length * height + 2 * width * height


def ceiling_area(length, width):
    return length * width


response = input("Do you want to do this program? (Yes/No): ")

while response.lower() == "yes":
    length = float(input("Enter length of the room: "))
    width = float(input("Enter width of the room: "))
    height = float(input("Enter height of the room: "))

    wall_sq_ft = wall_square_footage(length, width, height)
    wall_gallons = wall_sq_ft / 50

    ceiling_sq_ft = ceiling_area(length, width)
    ceiling_gallons = ceiling_sq_ft / 50

    print("Wall square footage:", format(wall_sq_ft, ",.2f"))
    print("Gallons of wall paint needed:", format(wall_gallons, ".2f"))
    print("Ceiling square footage:", format(ceiling_sq_ft, ",.2f"))
    print("Gallons of ceiling paint needed:", format(ceiling_gallons, ".2f"))

    response = input("Do you want to do this again? (Yes/No): ")
