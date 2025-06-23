def count_char(input_str, char):
    """
    Count how many times a character appears in a string
    Args:
        input_str: The input string to search in
        char: The character to count (must be a single character)
    Returns:
        Number of occurrences of the character, or -1 if invalid input
    """
    if input_str is None or char is None:
        return -1
        
    if not isinstance(input_str, str):
        return -1
        
    if not isinstance(char, str) or len(char) != 1:
        return -1
    
    count = 0
    for c in input_str:
        if c == char:
            count += 1
    return count

def find_lowest(numbers):
    """
    Find the lowest integer in a list without using min()
    Args:
        numbers: List of integers
    Returns:
        The lowest integer in the list, or None if invalid input
    """
    if numbers is None:
        return None
        
    if not isinstance(numbers, list):
        return None
        
    if not numbers:
        return None
    
    # Validate that all elements are numbers
    if not all(isinstance(x, (int, float)) for x in numbers):
        return None
    
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest

def find_substring(str1, str2, find_all=False):
    """
    Find if str2 is contained in str1 and return its starting index(es)
    Args:
        str1: The string to search in
        str2: The string to search for
        find_all: Optional boolean to return all matches (default: False)
    Returns:
        If find_all=False: First index where str2 is found, or -1 if not found or invalid input
        If find_all=True: List of all indexes where str2 is found, or empty list if not found or invalid input
    """
    if str1 is None or str2 is None:
        return [] if find_all else -1
        
    if not isinstance(str1, str) or not isinstance(str2, str):
        return [] if find_all else -1
    
    if not str2:
        return [0] if find_all else 0
    
    len1 = len(str1)
    len2 = len(str2)
    
    if find_all:
        matches = []
        for i in range(len1 - len2 + 1):
            match = True
            for j in range(len2):
                if str1[i + j] != str2[j]:
                    match = False
                    break
            if match:
                matches.append(i)
        return matches
    else:
        for i in range(len1 - len2 + 1):
            match = True
            for j in range(len2):
                if str1[i + j] != str2[j]:
                    match = False
                    break
            if match:
                return i
        return -1

def main():
    print("Hello, Welcome to Python task!")

    # Test cases for count_char
    count_char_tests = [
        # Positive tests
        {"input": "hello", "char": "l", "expected": 2, "description": "Valid input - character exists"},
        # Negative tests
        {"input": "hello", "char": "x", "expected": 0, "description": "Valid input - character doesn't exist"},
        # Invalid inputs
        {"input": None, "char": "a", "expected": -1, "description": "Invalid - null string"},
        {"input": "hello", "char": "ab", "expected": -1, "description": "Invalid - multiple characters"}
    ]

    print("\nTesting count_char function:")
    print("-" * 50)
    for test in count_char_tests:
        result = count_char(test["input"], test["char"])
        status = "PASS" if result == test["expected"] else "FAIL"
        print(f"{status}: {test['description']}")
        print(f"Input: '{test['input']}', Char: '{test['char']}'")
        print(f"Expected: {test['expected']}, Got: {result}\n")

    # Test cases for find_lowest
    lowest_number_tests = [
        # Positive tests
        {"input": [1, 0, -3, 100], "expected": -3, "description": "Valid input - mixed numbers"},
        # Negative tests
        {"input": [], "expected": None, "description": "Edge case - empty list"},
        # Invalid inputs
        {"input": None, "expected": None, "description": "Invalid - null input"},
        {"input": [1, "2", 3], "expected": None, "description": "Invalid - mixed types"}
    ]

    print("\nTesting find_lowest function:")
    print("-" * 50)
    for test in lowest_number_tests:
        result = find_lowest(test["input"])
        status = "PASS" if result == test["expected"] else "FAIL"
        print(f"{status}: {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}, Got: {result}\n")

    # Test cases for find_substring
    substring_tests = [
        # Positive tests
        {"str1": "hello world", "str2": "world", "find_all": False, 
         "expected": 6, "description": "Valid input - single match"},
        {"str1": "hello hello hello", "str2": "hello", "find_all": True, 
         "expected": [0, 6, 12], "description": "Valid input - multiple matches"},
        # Negative tests
        {"str1": "hello world", "str2": "xyz", "find_all": False, 
         "expected": -1, "description": "Valid input - no matches"},
        # Invalid inputs
        {"str1": None, "str2": "test", "find_all": False,
         "expected": -1, "description": "Invalid - null input"}
    ]

    print("\nTesting find_substring function:")
    print("-" * 50)
    for test in substring_tests:
        result = find_substring(test["str1"], test["str2"], test.get("find_all", False))
        status = "PASS" if result == test["expected"] else "FAIL"
        print(f"{status}: {test['description']}")
        print(f"String 1: '{test['str1']}'")
        print(f"String 2: '{test['str2']}'")
        print(f"Find All: {test.get('find_all', False)}")
        print(f"Expected: {test['expected']}, Got: {result}\n")

if __name__ == "__main__":
    main()
