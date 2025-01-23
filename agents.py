from crewai import Agent, LLM  # Ensure this library is installed and properly configured
from dotenv import load_dotenv
import os
import logging
from tools import tool  # Ensure this import matches your tools configuration

# Load environment variables from a .env file
load_dotenv()

# Retrieve the Gemini API key from the environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure this is set in your .env file

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in your environment. Please check your .env file.")

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Initialize the LLM with the Gemini model
llm = LLM(
    model="gemini/gemini-1.5-pro-latest",
    temperature=0.7,
    api_key=GEMINI_API_KEY
)

# Create the Project Manager Researcher Agent
project_manager_researcher = Agent(
    role="Project Manager Assistant - Researcher",
    goal="Discover emerging trends, evaluate risks, and propose innovative solutions to optimize {project_topic} outcomes",
    verbose=True,  # Enable verbosity for the agent
    memory=True,
    backstory=(
        "With a sharp analytical mind and a knack for uncovering patterns, you excel at delivering actionable insights. "
        "Your mission is to empower the project team by providing data-driven recommendations and strategic foresight."
    ),
    tools=[tool],  # Ensure `tool` is properly defined
    llm=llm,
    allow_delegation=True
)

# Create the Project Manager Writer Agent
project_manager_writer = Agent(
    role="Project Manager Assistant - Communicator",
    goal="Craft engaging and precise updates, reports, and communication materials to align stakeholders and drive project success in {project_topic}",
    verbose=True,  # Enable verbosity for the agent
    memory=True,
    backstory=(
        "A storyteller with a strategic mindset, you transform complex project details into clear and impactful narratives. "
        "Your work ensures seamless communication and fosters collaboration among all stakeholders."
    ),
    tools=[tool],  # Ensure `tool` is properly defined
    llm=llm,
    allow_delegation=False
)
