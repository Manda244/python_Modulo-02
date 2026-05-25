#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/21 08:33:49 by marasolo            #+#    #+#            #
#   Updated: 2026/05/25 12:11:13 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError as e:
        raise ValueError(f"{e}")

    if temp > 40:
        raise ValueError(f"{temp}°C is too cold for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    input = ["25", "abc", "100", "-25"]

    print()
    for temp_str in input:
        print(f"Input data is {temp_str}")
        try:
            temp = input_temperature(str(temp_str))
            print(f"Temperature is now {temp}°C")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
