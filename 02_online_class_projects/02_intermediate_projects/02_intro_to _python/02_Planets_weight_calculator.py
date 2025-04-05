
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def planets_gravity():
    """a Program to calculate the weight of earthlings on different Planets asking use for Planet and weight on Earth"""
    try:
        planet = input("Enter the planet: ").strip().lower()
        if planet not in ["mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"]:
            raise ValueError("Invalid planet name")



        earth_weight = float(input("Enter your weight on Earth (kg): "))

        # Assign the correct gravity constant based on the planet name
        if planet == "mercury":
            gravity_constant = MERCURY_GRAVITY
        elif planet == "venus":
            gravity_constant = VENUS_GRAVITY
        elif planet == "mars":
            gravity_constant = MARS_GRAVITY
        elif planet == "jupiter":
            gravity_constant = JUPITER_GRAVITY
        elif planet == "saturn":
            gravity_constant = SATURN_GRAVITY
        elif planet == "uranus":
            gravity_constant = URANUS_GRAVITY
        else:
            gravity_constant = NEPTUNE_GRAVITY  # Default to Neptune if no match

        # Calculate the weight on the selected planet
        planetary_weight = earth_weight * gravity_constant
        rounded_planetary_weight = round(planetary_weight, 2)
        # Print the result
        print(f"Your weight on {planet.capitalize()}: {rounded_planetary_weight} kg")
    #  With e  in the value error: You can print detailed information about the specific error.   
    except ValueError as e:
        print(f"Error: {e}. Please enter the correct information.")


if __name__ == "__main__":
    planets_gravity()
    
# second way more acessible bcz of having planets in a list inside the function and checking by one if statemnt
# MERCURY_GRAVITY = 0.376
# VENUS_GRAVITY = 0.889
# MARS_GRAVITY = 0.378
# JUPITER_GRAVITY = 2.36
# SATURN_GRAVITY = 1.081
# URANUS_GRAVITY = 0.815
# NEPTUNE_GRAVITY = 1.14
# EARTH_GRAVITY = 1.0

# def planets_gravity():
#     """A program to calculate the weight of Earthlings on different planets by asking for the planet and weight on Earth"""
#     # Define a dictionary of planets and their gravity constants
#     planet_gravity_data = {
#         "mercury": MERCURY_GRAVITY,
#         "venus": VENUS_GRAVITY,
#         "mars": MARS_GRAVITY,
#         "jupiter": JUPITER_GRAVITY,
#         "saturn": SATURN_GRAVITY,
#         "uranus": URANUS_GRAVITY,
#         "neptune": NEPTUNE_GRAVITY
#     }

#     try:
#         # Ask for the planet and convert it to lowercase to handle case sensitivity
#         planet = input("Enter the planet: ").strip().lower()

#         # Check if the planet entered is valid, if not, raise an error
#         if planet not in planet_gravity_data:
#             raise ValueError("Invalid planet name.")

#         # Get the gravity constant for the selected planet
#         gravity_constant = planet_gravity_data[planet]

#         # Ask for the user's weight on Earth and ensure it's a valid number
#         earth_weight = float(input("Enter your weight on Earth (kg): "))

#         # Calculate the weight on the selected planet
#         planetary_weight = earth_weight * gravity_constant
#         rounded_planetary_weight = round(planetary_weight, 2)

#         # Print the result
#         print(f"Your weight on {planet.capitalize()}: {rounded_planetary_weight} kg")

#     except ValueError as e:
#         print(f"Error: {e}. Please enter the correct information.")

# if __name__ == "__main__":
#     planets_gravity()
