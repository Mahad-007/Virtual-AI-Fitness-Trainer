import streamlit as st
from dotenv import load_dotenv
import os

from crew.fitness_crew import fitness_crew
from tools.calorie_tool import calculate_calories
from tools.search_tool import search_fitness

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

load_dotenv()

# — LLM & Memory Setup —
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# — Streamlit UI —
st.title("🏋️‍♂️ Virtual AI Fitness Trainer")
st.sidebar.header("User Info")
goal = st.sidebar.selectbox("Goal", ["Lose Fat", "Build Muscle", "Stay Fit"])
duration = st.sidebar.slider("Duration (weeks)", 1, 16, 4)

# Workout plan generator
if st.button("Generate Workout Plan"):
    prompt_w = PromptTemplate.from_template(
        "Create a workout plan to {goal} in {duration} weeks."
    )
    chain_w = LLMChain(llm=llm, prompt=prompt_w)
    response = chain_w.run(goal=goal, duration=duration)
    st.success("Workout Plan")
    st.write(response)

st.divider()
st.subheader("🧮 Calorie Estimator")
with st.form("calorie_form"):
    weight = st.number_input("Weight (kg)", min_value=30.0)
    height = st.number_input("Height (cm)", min_value=100.0)
    age = st.number_input("Age", min_value=10)
    gender = st.selectbox("Gender", ["Male", "Female"])
    activity = st.selectbox("Activity Level", ["Low", "Medium", "High"])
    if st.form_submit_button("Calculate"):
        result = calculate_calories.invoke({
            "weight": weight,
            "height": height,
            "age": age,
            "gender": gender,
            "activity_level": activity
        })
        st.info(result)

st.divider()
st.subheader("🌐 Ask Fitness Questions")
query = st.text_input("Ask something like 'Best protein sources?'")

# Use DuckDuckGo as a tool + LLM summarizer
search_prompt = PromptTemplate(
    input_variables=["query", "search_results"],
    template=(
        "You are a friendly fitness expert.\n"
        "User asked: {query}\n\n"
        "Here are web search snippets:\n{search_results}\n\n"
        "Please summarize clearly, informatively, and cite briefly."
    )
)
search_chain = LLMChain(llm=llm, prompt=search_prompt)

if st.button("Search"):
    raw = search_fitness.invoke({"query": query})
    answer = search_chain.run(query=query, search_results=raw)
    st.write(answer)
