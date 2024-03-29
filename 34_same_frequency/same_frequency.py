def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    def freq(num): 
        count = {}
        for val in str(num):
            count[val] = count.get(val, 0) + 1
        return count

    return True if freq(num1) == freq(num2) else False
    