from langchain_community.tools import tool

@tool
def square_number(number: int) -> int:
    """
    Returns the square of a given number.
    """
    return number * number

@tool
def substract_number(Bignumber: int,Smallnumber: int) -> int:
    """
    Returns the square of a given number.
    """
    return Bignumber - Smallnumber

class ToolKit:
    def _getTools(self, tools):
        return [square_number,substract_number]
