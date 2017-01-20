from name_function import get_formatted_name

print("Enter 'q' at any time to quit. ")

while True:
    city = input("\nPlease give me a City name: ")
    if city == 'q':
        break
    country = input("\nPlease give me a Country name: ")
    if country == 'q':
        break

    formmatted_name = get_formatted_name(city ,country)
    print("\t Neatly formatted name: " + formmatted_name + '.')
