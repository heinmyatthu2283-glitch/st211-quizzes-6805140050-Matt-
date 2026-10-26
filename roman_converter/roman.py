def convert(number: str) -> int:
    """Converts a Roman numeral string into an integer with strict validation."""
    if not number:
        raise ValueError("Input string cannot be empty")

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    number = number.upper()
    
    # 1. Rule: V, L, D can NEVER be repeated (e.g., VV, LL, DD are invalid)
    non_repeatable = ['V', 'L', 'D']
    for char in non_repeatable:
        if char * 2 in number:
            raise ValueError(f"Symbol '{char}' cannot be repeated: {number}")
            
    # 2. Rule: I, X, C, M cannot appear more than 3 times consecutively (e.g., IIII is invalid)
    repeatable = ['I', 'X', 'C', 'M']
    for char in repeatable:
        if char * 4 in number:
            raise ValueError(f"Symbol '{char}' cannot repeat 4 times in a row: {number}")

    total = 0
    prev_value = 0
    
    for char in reversed(number):
        if char not in roman_map:
            raise ValueError(f"Invalid symbol: {char}")
            
        val = roman_map[char]
        
        # Rule: V, L, D can never be subtracted (e.g., VX is invalid)
        if val < prev_value:
            if char in non_repeatable:
                raise ValueError(f"Invalid subtractive symbol: {char}")
            total -= val
        else:
            total += val
        prev_value = val
        
    return total