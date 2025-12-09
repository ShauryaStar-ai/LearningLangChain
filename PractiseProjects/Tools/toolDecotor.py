from langchain_community.tools import tool

@tool
def square_number(number: int) -> int:
    """
    Returns the square of a given number.
    """
    return number * number

print(square_number(2))