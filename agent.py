from langchain.agents import create_agent

from tools import search_web, send_discord_message

SYSTEM_PROMPT = (
    "You are a helpful research assistant. When asked to look something up "
    "and share it, first use the search_web tool to gather information, "
    "then use the send_discord_message tool to post a clear, well-formatted "
    "summary to Discord."
)

agent = create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[search_web, send_discord_message],
    system_prompt=SYSTEM_PROMPT,
)


def run_agent(user_message: str) -> str:
    result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    content = result["messages"][-1].content

    if isinstance(content, list):
        return "".join(
            block.get("text", "") for block in content if isinstance(block, dict)
        )
    return content
