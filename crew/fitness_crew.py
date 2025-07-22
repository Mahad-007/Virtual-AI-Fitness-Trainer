from crewai import Crew
from crew.agents import trainer, nutritionist, motivator

fitness_crew = Crew(
    agents=[trainer, nutritionist, motivator],
    verbose=True
)
