def decimal_2_roman(n: int) -> str:

    roman_numerals = {
        "1": "I",
        "5": "V",
        "10": "X",
        "50": "L",
        "100": "C",
        "500": "D",
        "1000": "M"
    }

    overline_char = "\u0305"

    if type(n) is not int:
        raise ValueError("Input number should be an integer number.")

    if not 1 <= n <= 1000000:
        raise ValueError(f"The input number {n} should be between 1-1000000")

    result = []
    digits = n

    # We'll keep track of the power of ten in order to perform a lookup in the roman numerals map
    #  This power of 10 will be multiplied by 10 each time we process a digit, that way we'll now if we are processing
    #  units, tens, hundreds or thousands
    power_of_ten = 1

    # For numbers bigger than 3999 the characters are reused but an overline is drawn above it,
    #  to indicate that it multiplies the numeral by 1000. We'll increase this number each time we reach 4000 or a
    #  multiple of it
    number_of_overlines_1000 = 0

    while digits > 0:
        # This will allow us to overwrite the unit symbol when we are dealing with 1000, 2000 or 3000
        should_use_M_instead_of_I = False

        # Get the right-most digit
        current_digit = digits % 10

        # Delete the right-most digit
        digits = digits // 10

        # Check if we need to add overlines over the character and how many.
        if power_of_ten == 1000:
            number_of_overlines_1000 += 1
            # Reset the lookup so that we can reuse characters, we'll add the overlines later
            power_of_ten = 1

            # If we need to deal with units, use M this time instead of I
            should_use_M_instead_of_I = True

        if current_digit != 0:
            roman_num = []

            # We toy around with the idea that there are numbers for the units and multiples of 5 in a power of ten
            #  we then address the rules that deal with all 9 different digits
            if current_digit == 4:
                first_part = roman_numerals[str(power_of_ten)]
                second_part = roman_numerals[str(5 * power_of_ten)]
                roman_num.append(first_part)
                roman_num.append(second_part)

            elif current_digit == 9:
                first_part = roman_numerals[str(power_of_ten)]
                second_part = roman_numerals[str(10 * power_of_ten)]
                roman_num.append(first_part)
                roman_num.append(second_part)

            # Covers 1, 2, 3
            elif current_digit < 5:
                unit_numeral = roman_numerals["1000"] if should_use_M_instead_of_I else roman_numerals[str(power_of_ten)]
                counter = current_digit

                while counter > 0:

                    roman_num.append(unit_numeral)
                    counter -= 1

            # Covers 6, 7, 8
            elif current_digit > 5:
                roman_num.append(roman_numerals[str(5 * power_of_ten)])
                counter = current_digit

                while (counter - 5) > 0:
                    roman_num.append(roman_numerals[str(power_of_ten)])
                    counter -= 1

            # The digit is equal to 5
            else:
                roman_num.append(roman_numerals[str(power_of_ten * 5)])

            if number_of_overlines_1000 > 0:
                overlines_to_add = number_of_overlines_1000

                # This condition will allow us to use M, MM, MMM for 1000, 2000 and 3000 before reusing numerals with
                #  an overline
                if should_use_M_instead_of_I and 1 <= current_digit <= 3:
                    overlines_to_add -= 1

                overlines = [overline_char for n_overlines in range(overlines_to_add)]
                overlines = "".join(overlines)

                # Add the required number of overlines for each of the character that need to be multiplied by 1000
                for idx in range(len(roman_num)):
                    roman_num[idx] = overlines + roman_num[idx]

            result.append("".join(roman_num))

        # We'll process a new digit to the left, so we need to keep track if we are dealing with units, tens, hundreds
        #  or thousands
        power_of_ten *= 10

    # Given that we parsed the digits from right-left, we need to reverse the result to get the correct order
    result.reverse()

    return "".join(result)
