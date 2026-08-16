from langchain.agents import create_agent

from tools import search_web, send_discord_message

SYSTEM_PROMPT = (
    "You are a helpful research assistant. When asked to look something up "
    "and share it, first use the search_web tool to gather information, "
    "then use the send_discord_message tool to post a clear, well-formatted "
    "summary to Discord."
)

agent = create_agent(
    model="google_genai:gemini-flash-latest",
    tools=[search_web, send_discord_message],
    system_prompt=SYSTEM_PROMPT,
)


def run_agent(user_message: str) -> str:
    result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    return result["messages"][-1].content
