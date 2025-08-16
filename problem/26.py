def search_countries_by_letter(country_data):
    result = []
    while True:
        letter = input("Please input 1 letter: ")
        if len(letter) != 1 :
            print("Please try again")
        else:
            break
    for code, country in country_data.items():
        for i , char in enumerate(country):
            if i == 0 and letter.lower() == char.lower():
                result.append(country)
                break
            else:
                break
    result.sort()
    return(result)


country_data = {
"+1": "United States",
"+44": "United Kingdom",
"+91": "India",
"+81": "Japan",
"+49": "Germany",
"+86": "China"
}

print(search_countries_by_letter(country_data))

