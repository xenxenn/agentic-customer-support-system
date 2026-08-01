import logging

from graph import graph


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("StarAI")


config = {
    "configurable": {
        "thread_id": "user-1"
    }
}


print("=== StarAI - Agentic Customer Support ===")
print("Type 'exit' to quit.\n")


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        logger.info("Application stopped by user")
        break

    logger.info("User query: %s", user_input)

    try:
        response = graph.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            },
            config=config
        )

        last_message = response["messages"][-1]

        content = last_message.content

        if isinstance(content, list):
            content = " ".join(
                item.get("text", "")
                for item in content
                if isinstance(item, dict)
            )

        logger.info("Response generated successfully")

        print(f"\nStarAI: {content}\n")

    except Exception as e:
        logger.error("Agent execution failed: %s", e)

        print(
            "\nStarAI: Sorry, I encountered an error. "
            "Please try again.\n"
        )