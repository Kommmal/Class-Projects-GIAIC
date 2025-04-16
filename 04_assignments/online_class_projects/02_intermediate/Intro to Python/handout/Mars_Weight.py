def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * 0.378
    print("The equivalent on Mars:", round(mars_weight, 2))

if __name__ == "__main__":
    main()
