import streamlit as st
from crewai import Crew, Process
from task import research_task, write_task
from agents import project_manager_researcher, project_manager_writer

# Initialize the Crew
crew = Crew(
    agents=[project_manager_researcher, project_manager_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Streamlit Interface
st.title("Project Manager Assistant")
st.subheader("Kick off a task and get detailed insights and updates!")

# Input form
project_topic = st.text_input("Enter the Project Topic", "AI in project management")

# Start task execution when button is clicked
if st.button("Start Task Execution"):
    st.info("Executing tasks, please wait...")

    # Execute tasks with user input
    result = crew.kickoff(inputs={"project_topic": project_topic})
    
    # Display results
    st.success("Task execution completed!")
    st.subheader("Results:")
    st.write(result)

# Display footer
st.sidebar.title("About")
st.sidebar.info(
    "This app is designed to assist project managers by leveraging AI-driven tools "
    "for research and reporting tasks."
)

