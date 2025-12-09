from langchain_community.tools import StructuredTool
from pydantic import BaseModel, Field

class SquareInput(BaseModel):
    a: int = Field(..., description="The number to square")
def square(a: int) -> int:
    return a * a

sqauretool = StructuredTool.from_function(func = square, name="square", description="A tool that squares a number",args_schema=SquareInput)
print(sqauretool.invoke({"a": 2}))
