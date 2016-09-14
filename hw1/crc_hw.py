def parse_array(x):
    """ Turns a string of 0s and 1s into a binary array.

    :param x: String to parse
    :type x: str

    :return: A binary array
    :rtype: list
    """

    return [c.strip() == '1' for c in x]

def fmt_array(x):
    """ Formats a binary array as a human-readable 0/1 string

    :param x: Boolean Array to format
    :type x: list

    :return: a nicely formatted string
    :rtype: str
    """

    return ''.join(['1' if a else '0' for a in x])

def xor(x, y):
    """ Computes the XOR of two binary arrays.

    :param x: First boolean array
    :type x: list

    :param y: Second boolean array
    :type y: list

    :return: A boolean array of results
    :rtype: list
    """

    return [a ^ b for (a, b) in zip(x, y)]


def crc_check(message, divisor, quiet = True):
    """ Performs a nice CRC check.

    :param message: Message (including appeneded checksum) to check.
    :type message: str

    :param divisor: Divisor to use.
    :type divisor: str

    :param quiet: A boolean indicating if we should not print anything. Defaults to True.
    :type quiet: bool

    :return: a boolean indicating if the CRC was successfull.
    :rtype: bool
    """

    # Make nice lists
    M = parse_array(message)
    G = parse_array(divisor)

    # the length of the divisor
    l = len(G)

    # Print the beginning
    if not quiet:
        print('G = %s' % (fmt_array(G)))
        print('M = %s' % (fmt_array(M)))

    # setup state
    space = ' '*4
    line = '-'*l
    pull = l # next index to pull
    remainder = M[:l] # the current remainder

    # print the initial remainder
    if not quiet:
        print('%s%s' % (space, fmt_array(remainder)))

    # keep doing this forever
    while True:

        # print thing to compute
        if not quiet:
            print('%s%s' % (space, fmt_array(G)))
            print('%s%s' % (space, line))

        # remainder = remainder / G
        remainder = xor(remainder, G)

        # We have a 1 in the first division, so do it again.
        if remainder[0]:

            # print the thing to compute again
            if not quiet:
                print('%s%s\n%s%s' % (space, fmt_array(remainder), space, fmt_array(G)))
                print('%s%s' % (space, line))

            # to get the new remainder
            remainder = xor(remainder, G)

        # If we have nothing more to pull down
        if len(M) <= pull:
            break

        # pull down the next number
        remainder.append(M[pull])
        pull = pull + 1

        # Print the remainder again.
        if not quiet:
            print('%s%s' % (space, fmt_array(remainder)))

        # add a space, remove trailing zero
        space += ' '
        remainder.pop(0)

    if not quiet:
        print('%s%s' % (space, fmt_array(remainder)))

    # Check if we have all zeros
    return all([(not a) for a in remainder])


check = crc_check('1101011001011010', '10101', quiet = False)
print(check)