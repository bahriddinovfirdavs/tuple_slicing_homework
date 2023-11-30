def main(tuple1,n,k):
    """
    A tuple of several elements is given. Return the value from n index to k index.
    Args:
        tuple1(tuple): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        tuple: return answer.
    """
    return tuple1[n:k]
tuple1=['a', 'b', 'c', 'd', 'e', 'f']
n = 2
k = 5 
print(main(tuple1,n,k))