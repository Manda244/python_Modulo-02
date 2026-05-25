#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/25 17:23:12 by marasolo            #+#    #+#            #
#   Updated: 2026/05/25 20:26:24 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def checke_plant(Plant_name, is_wilting) -> None:
    if is_wilting:
        raise PlantError(f"The {Plant_name} plant is wilting!")


def checke_water(tank_level, minimum) -> None:
    if tank_level < minimum:
        raise WaterError("Not enough water in the tank!")


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        checke_plant("tomato", is_wilting=True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        checke_water(tank_level=2, minimum=10)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_garden_error_catch_all() -> None:
    print("Testing catching all garden errors...")

    garden_action = [
        lambda: checke_plant("Tomato", is_wilting=True),
        lambda: checke_water(tank_level=2, minimum=10)
    ]

    for action in garden_action:
        try:
            action()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print()
    test_plant_error()

    print()
    test_water_error()

    print()
    test_garden_error_catch_all()

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
