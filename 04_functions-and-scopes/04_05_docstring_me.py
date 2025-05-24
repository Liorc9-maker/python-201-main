# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km: float) ->float:
    """Converts a distance from kilometers to miles.

    Args:
        km (float): The distance in kilometers.

    Returns:
        float: The equivalent distance in miles.
    """
    miles = km * 0.621371
    return miles

km_input = float(input("Please type in the distance in km to convert into miles: "))
print(km_to_miles(km_input))
print(km_to_miles.__doc__)
