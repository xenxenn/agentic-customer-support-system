import logging

from langchain_core.tools import tool
from pypdf import PdfReader


logger = logging.getLogger("StarAI")


@tool
def search_knowledge_base(query: str) -> str:
    """
    Search information from PointStar customer support knowledge base PDF.
    Use this tool when users ask about PointStar services, billing,
    refund policy, technical support, or service issues.
    """

    logger.info("Knowledge base search triggered: %s", query)

    try:
        pdf_path = "data/PointStar_FAQ.pdf"

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return f"""
Use only the following knowledge base information to answer the question.

Knowledge Base:
{text}

Question:
{query}

If the answer is not available in the knowledge base,
state that the information is unavailable and recommend contacting support.
"""

    except Exception as e:
        logger.error("Knowledge base error: %s", e)

        return (
            "The knowledge base is currently unavailable. "
            "Please contact customer support for further assistance."
        )