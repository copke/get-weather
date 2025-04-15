import webbrowser


DEFAULT_CITY = "Belgrade"

def is_valid_city_name(city):
    words = city.split()
    return all(word.isalpha() for word in words)

while True:
    city_name = input("Enter city (press enter for Belgrade): ").lower().strip()

    if city_name == "":
        city_name = DEFAULT_CITY

    if is_valid_city_name(city_name):
        city_name = city_name.replace("", "+")
        link = "https://www.google.com/search?q=weather+" + city_name
        webbrowser.open(link)
        break
    else:
        print("Invalid input. Enter city name without numbers and special simbols.")
        continue