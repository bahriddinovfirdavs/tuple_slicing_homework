def main(tuple1,n):
    """
    A tuple of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        tuple1(tuple): parameter
        n(int): parameter
    Returns:
        tuple: return answer.
    """
    return tuple1[:n-1:-1]