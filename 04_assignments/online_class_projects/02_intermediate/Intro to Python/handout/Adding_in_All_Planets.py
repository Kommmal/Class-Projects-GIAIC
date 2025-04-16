def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").capitalize()

    if planet == "Mercury":
        equivalent = earth_weight * 0.376
        print("The equivalent weight on Mercury:", round(equivalent, 2))
    elif planet == "Venus":
        equivalent = earth_weight * 0.889
        print("The equivalent weight on Venus:", round(equivalent, 2))
    elif planet == "Mars":
        equivalent = earth_weight * 0.378
        print("The equivalent weight on Mars:", round(equivalent, 2))
    elif planet == "Jupiter":
        equivalent = earth_weight * 2.36
        print("The equivalent weight on Jupiter:", round(equivalent, 2))
    elif planet == "Saturn":
        equivalent = earth_weight * 1.081
        print("The equivalent weight on Saturn:", round(equivalent, 2))
    elif planet == "Uranus":
        equivalent = earth_weight * 0.815
        print("The equivalent weight on Uranus:", round(equivalent, 2))
    elif planet == "Neptune":
        equivalent = earth_weight * 1.14
        print("The equivalent weight on Neptune:", round(equivalent, 2))
    else:
        print("Invalid planet name.")

if __name__ == "__main__":
    main()
