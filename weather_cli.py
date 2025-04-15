import webbrowser


DEFAULT_CITY = "Belgrade"

while True:
    city_name = input("Enter city (press enter for Belgrade): ").lower().strip()

    if city_name == "":
        city_name = DEFAULT_CITY

