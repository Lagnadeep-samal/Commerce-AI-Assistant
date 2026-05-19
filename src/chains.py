from langchain_core.prompts import (
    ChatPromptTemplate
)

from src.prompts import SYSTEM_PROMPT


prompt_template = ChatPromptTemplate.from_template(
    """
    {system_prompt}

    Context:
    {context}

    Question:
    {question}
    """
)


def build_prompt(context, question):

    return prompt_template.format(
        system_prompt=SYSTEM_PROMPT,
        context=context,
        question=question
    )