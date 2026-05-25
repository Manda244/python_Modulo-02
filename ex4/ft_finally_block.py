#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/25 19:55:23 by marasolo            #+#    #+#            #
#   Updated: 2026/05/25 22:50:18 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class PlantError(Exception):
    pass


def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    validation_plant = ["Tomato", "Lettuce", "Carrots"]
    invalid_plant = ["Tomato", "lettuce", "Carrots"]

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in validation_plant:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print()
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        for plant in invalid_plant:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
