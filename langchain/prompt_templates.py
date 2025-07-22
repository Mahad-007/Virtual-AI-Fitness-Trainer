from langchain.prompts import PromptTemplate

fitness_template = PromptTemplate(
    input_variables=["goal", "duration"],
    template="Generate a workout plan for a user who wants to {goal} in {duration}."
)
