import logging

from langchain_core.tools import tool


logger = logging.getLogger("StarAI")


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example:
    25 * 4
    100 / 5
    (20 + 5) * 3
    """

    try:
        # Restricted evaluation for assessment purposes.
        # A production system should use a safer math parser.
        result = eval(expression)

        logger.info("Calculator executed: %s", expression)

        return str(result)

    except Exception as e:
        logger.error("Calculator error: %s", e)

        return "Invalid mathematical expression."