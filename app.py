import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Load environment variables
load_dotenv()

# Initialize Groq model (or replace with OpenAI if preferred)
model = Groq(id="llama3-70b-8192")

# Agent 1: Startup Idea Generator
startup_idea_agent = Agent(
    name="StartupIdeaAgent",
    model=model,
    tools=[DuckDuckGo()],
    instructions=["Generate startup ideas based on current market trends."],
    show_tool_calls=True,
    markdown=True,
)

# Agent 2: Content Creator Idea Generator
content_creator_agent = Agent(
    name="ContentCreatorAgent",
    model=model,
    instructions=["Suggest content ideas such as blog posts, YouTube videos, or social media topics."],
    markdown=True,
)

# Function to select which agent to use based on user query
def idea_generator_ai(user_prompt):
    if "startup" in user_prompt.lower():
        response = startup_idea_agent.run(user_prompt)
    else:
        response = content_creator_agent.run(user_prompt)
    return response.content

if __name__ == "__main__":
    print("Welcome to Idea Generator AI!")
    print("Type your idea request below. Type 'exit' to quit.")
    while True:
        user_input = input("\n💬 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Stay creative!")
            break
        response = idea_generator_ai(user_input)
        print("\n🤖 Idea Generator AI:\n" + response)
