from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import langchain_anthropic
import os

#document loader set up
loader = Docx2txtLoader("The Foundation of Classical Mechanics.docx")
docs = loader.load()

#model 1 set up
my_api_key = os.getenv("OPEN_AI_API_KEY")  # the windows reteiver of the env variable
model1=ChatOpenAI(openai_api_key=my_api_key)
prompt1 = PromptTemplate(
    input_variables=["research"],  # list all placeholders used inside template
    template="Read the reserch and the provide me with 5 points of the research"
)

#model 2 set up
API_KEY = os.getenv("ANTHROPIC_API_KEY")
model = "claude-3-5-haiku-20241022"
model2 = langchain_anthropic.ChatAnthropic(model=model, api_key=API_KEY, temperature=0.7)
prompt2 = PromptTemplate(
    input_variables=["research"],  # list all placeholders used inside template
    template="Read the reserch and the provide me with 5 question multiple answer quiz of the research"
)
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {summary} and quiz -> {quiz}',
    input_variables=['summary', 'quiz']
)
output_parser = StrOutputParser()

parallel = RunnableParallel({
    "summary": prompt1 | model1 | output_parser,
    "quiz":  prompt2 | model2 | output_parser
})
merge_chain = prompt3 | model1 | output_parser

chain = parallel | merge_chain
text="""
In 1687, Sir Isaac Newton published his monumental work, Philosophiæ Naturalis Principia Mathematica, and in doing so, he laid the foundational framework for classical mechanics. Within its pages, he articulated three simple yet profound statements that describe the relationship between a body and the forces acting upon it, and its motion in response to those forces. These three laws of motion, which govern everything from a falling apple to the orbit of planets, remain a cornerstone of physics and engineering to this day.

The First Law, often called the law of inertia, states that an object at rest will remain at rest, and an object in motion will remain in motion at a constant velocity, unless acted upon by a net external force. This principle fundamentally challenges the Aristotelian view that motion requires a constant force. Instead, Newton posits that force is not the cause of motion itself, but the cause of a change in motion. Inertia is the property of matter that resists this change, a concept that is intuitively experienced when a car accelerates suddenly, pushing passengers back into their seats, or when a sliding hockey puck continues gliding across nearly frictionless ice.

The Second Law provides the quantitative punch to the First Law's qualitative statement. It defines that the acceleration of an object is directly proportional to the net force acting upon it and inversely proportional to its mass (F=ma). This elegant equation is the workhorse of classical mechanics. It establishes a clear, causal relationship: a net force is required to produce acceleration, and that same force applied to a more massive object will result in less acceleration. This law allows engineers to calculate the thrust needed for a rocket to escape Earth's gravity and enables us to understand why pushing a small car is easier than pushing a loaded truck.

The Third Law introduces the concept of force as an interaction between two bodies, famously stating that for every action, there is an equal and opposite reaction. When you push on a wall, the wall pushes back on you with equal force. When a rocket engine expels hot gases downward (the action), the gases exert an equal and upward force on the rocket (the reaction), propelling it forward. It is crucial to note that these paired forces act on different objects, which is why they do not cancel each other out. While the forces are equal, the resulting accelerations (as determined by the Second Law) can be vastly different if the masses of the objects are different; the Earth exerts a gravitational pull on you, and you exert an equal pull on the Earth, but you accelerate toward the Earth while the Earth's acceleration toward you is imperceptibly small.

In conclusion, Newton's three laws form an interlocking and powerful logical system. The First Law identifies the natural state of motion and the need for a force to alter it. The Second Law quantifies that alteration. The Third Law ensures that force is never a one-sided affair but a mutual interaction. Together, they created a unified theory that could explain and predict the behavior of objects on Earth and the heavens above with unprecedented accuracy, ushering in the Scientific Revolution and forever changing our understanding of the physical universe.
"""
result = chain.invoke({"research": text})

print(result)