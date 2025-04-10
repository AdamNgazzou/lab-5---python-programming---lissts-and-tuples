from pickle import dump, load

def dumping():
    n = int(input("How many cities do you want to enter? "))
    villes = []
    
    for i in range(n):  # Changed to loop 'n' times based on user input
        nom_ville = input(f"Enter the name of city {i + 1}: ")
        latitude = float(input(f"Enter the latitude of {nom_ville}: "))
        longitude = float(input(f"Enter the longitude of {nom_ville}: "))
        villes.append((nom_ville, (latitude, longitude)))
    
    # Save the list of cities to a binary file
    with open('cities.dat', 'ab') as file:
        dump(villes, file)
    
    print("Cities have been saved to 'cities.dat'.")


def loading():
    villes_loaded = []
    with open("cities.dat", "rb") as file:
        while True:
            try:
                city = load(file)
                villes_loaded.append(city)
            except EOFError:  # End of file reached
                break
    
    print("Loaded cities:")
    for ville in villes_loaded:
        print(ville)
    return villes_loaded

def search():
    villes = loading()
    search_city = input("Enter the name of the city you want to search for: ")
    
    found = False
    for ville in villes:
        if search_city in ville[0]:  # Case-insensitive search
            print(f"City found: {search_city}")
            found = True
            break
    
    if not found:
        print(f"City '{search_city}' not found.")
# Call the dumping function to test it
def play():
    instruction = int(input("Do you want to enter cities? (1): \n do you want to load cities? (2): \n do you want to search for a city?(3) \n do you want to exit? (4): "))
    if(instruction == 1):
        dumping()
        play()
    elif(instruction == 2):
        loading()
        play()
    elif(instruction == 3):
        search()
        play()

play()