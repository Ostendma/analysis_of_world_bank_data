def square(n, power):
    """Calculates power for number upto n

    Args:
        n (_type_): _description_
        power (_type_): _description_

    Returns:
        _type_: _description_
    """
    return [i **power for i in range(n)]

print(square(10,4))