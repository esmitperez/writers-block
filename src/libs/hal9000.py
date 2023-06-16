from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

from pydantic import BaseModel, Field
from typing import List



model_name = 'gpt-3.5-turbo'
temperature = 0.0


class CorrectexText(BaseModel):
    input: str = Field(description="The text to be corrected")
    output: str = Field(description="The corrected text")


def correct_text(openai_api_key:str, style_rules: list, text_to_correct: str):
    llm = OpenAI(openai_api_key=openai_api_key, model_name=model_name, temperature=temperature)

    rules_section = ""

    # iterate over style_rules and append them to the template
    for rule in style_rules:
        rules_section += f"""
        {rule['text']}
        """

    template = """
    You are an expert style editor, and you always apply the following rule:
    {rules_section}

    Correct the following text:
    {text_to_correct}
    """

    prompt_template = PromptTemplate(input_variables=["text_to_correct", "rules_section"], template=template)
    correction_chain = LLMChain(llm=llm, prompt=prompt_template)

    return correction_chain.predict(text_to_correct=text_to_correct, rules_section=rules_section, verbose=True)
