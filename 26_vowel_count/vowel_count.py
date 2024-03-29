def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_count = {}
    vowels = ['a','e','i','o','u']
    for letter in phrase:
        letter = letter.lower()
        if letter in vowels:
            vowel_count[letter] = vowel_count.get(letter, 0) + 1
    return vowel_count