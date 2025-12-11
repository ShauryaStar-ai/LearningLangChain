from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class SusbtractInput(BaseModel):
    BigNumber: int = Field(description="The number to subtract from")
    SubtractBy: int = Field(description="The number to subtract")

class Subtract(BaseTool):
    name: str = "Subtract"
    description: str = "Subtract a number from another number"
    args_schema: Type[BaseModel] = SusbtractInput
    def _run(self, BigNumber: int, SubtractBy: int)->int:
        return BigNumber - SubtractBy
subtract = Subtract()

# Correct way to call it:
result = subtract.invoke({"BigNumber": 6, "SubtractBy": 2})
print(result)
