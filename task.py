from crewai import Task
from tools import tool
from agents import project_manager_researcher, project_manager_writer

# Research task
research_task = Task(
  description=(
    """Conduct a comprehensive analysis of {project_topic}, leveraging all available resources and tools to uncover critical insights."
    "Your focus should be on identifying and evaluating potential risks, uncovering emerging opportunities, and proposing actionable strategies."
    "The final report must include a structured overview that clearly outlines:
    - Key findings from your research.
    - Data-driven insights and their implications.
    - Strategic recommendations to address challenges and leverage opportunities."
    "Include references or citations for any data sources used to support your conclusions."""
  ),
  expected_output=(
    """A thoroughly detailed 3-paragraph report that includes:
    - A concise summary of findings.
    - A detailed analysis of risks and opportunities.
    - Practical and strategic recommendations for {project_topic}."""
  ),
  tools=[tool],
  agent=project_manager_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    """Prepare a professional and engaging project update document for {project_topic}."
    "Your goal is to provide stakeholders with a clear understanding of:
    - Current project progress and milestones achieved.
    - Key challenges encountered and solutions implemented.
    - Upcoming priorities and how they align with the overall project timeline."
    "Ensure the update maintains a solution-oriented tone, highlights collaboration efforts, and includes any necessary visuals or data representations to enhance clarity."""
  ),
  expected_output=(
    """A 4-paragraph project update document formatted as markdown, including:
    - An opening summary paragraph.
    - Two detailed paragraphs on progress, challenges, charts and solutions.
    - A forward-looking paragraph on next steps and stakeholder alignment."""
  ),
  tools=[tool],
  agent=project_manager_writer,
  async_execution=False,
  output_file='project-update.md'  # Example of output customization
)

