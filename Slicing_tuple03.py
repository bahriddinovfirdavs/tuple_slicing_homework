def main(tuple1):
    """
    A tuple of several elements is given. Return this tuple by adding the reverse.
    Args:
        tuple1(tuple): parameter
    Returns:
        tuple: return answer.
    """
    return tuple1+tuple1[::-1]