# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.


def real_estate_ad(**kwargs):
    print("🏠 Real Estate Advertisement 🏠")
    print("Details:")
    for key, value in kwargs.items():
        print(f" - {key.capitalize()}: {value}")

# Example usage:
real_estate_ad(
    location="123 Maple Street",
    price="$350,000",
    bedrooms=3,
    bathrooms=2,
    sqft=1500,
    pet_friendly=True,
    parking="Garage"
)
