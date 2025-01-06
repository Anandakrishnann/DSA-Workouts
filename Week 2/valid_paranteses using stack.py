def is_valid_parentheses(s):
    """
    Check if the given string of parentheses is valid.
    A string is valid if:
    1. Every opening bracket has a corresponding closing bracket.
    2. The brackets are properly nested.
    """
    stack = []  # Stack to keep track of opening brackets.
    mapping = {')': '(', '}': '{', ']': '['}  # Map closing to opening brackets.

    for char in s:
        if char in mapping:  # If the character is a closing bracket
            # Get the top element of the stack if it's not empty; else use a dummy "#".
            top_element = stack.pop() if stack else "#"
            
            # Check if the top element matches the corresponding opening bracket.
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack.
            stack.append(char)

    # The stack should be empty if all brackets are balanced.
    return not stack


# Example Usage
s = "({[]})"  # Balanced and properly nested
print(is_valid_parentheses(s))  # Output: True

s = "({[})"  # Improper nesting
print(is_valid_parentheses(s))  # Output: False
