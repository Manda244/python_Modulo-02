#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/19 06:51:29 by marasolo            #+#    #+#            #
#   Updated: 2026/05/21 08:32:33 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    input = [25, "abc"]

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
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
