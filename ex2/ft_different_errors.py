#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/25 11:50:13 by marasolo            #+#    #+#            #
#   Updated: 2026/05/25 17:18:38 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        _ = "garden" + 42  # type: ignore[operator]
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for nb in range(5):
        print(f"Testing operation {nb}...")
        try:
            garden_operations(nb)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ValueError: {e}")
        except FileNotFoundError as e:
            print(f"Caught ValueError: {e}")
        except TypeError as e:
            print(f"Caught ValueError: {e}")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
