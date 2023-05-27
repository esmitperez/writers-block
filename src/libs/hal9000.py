from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List



model_name = 'text-davinci-003'
temperature = 0.0
model = OpenAI(model_name=model_name, temperature=temperature)


class CorrectexText(BaseModel):
    input: str = Field(description="The text to be corrected")
    output: str = Field(description="The corrected text")


def correct_text(text_to_correct: str):
    # Set up a parser + inject instructions into the prompt template.
    parser = PydanticOutputParser(pydantic_object=CorrectexText)

    prompt = PromptTemplate(
        template="Correct the text.\n{format_instructions}\n{input_text}\n",
        input_variables=["input_text"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    _input = prompt.format_prompt(input_text=text_to_correct)
    return model(_input.to_string())

def correct_text2(text: str):
    # Set up a parser + inject instructions into the prompt template.
    parser = PydanticOutputParser(pydantic_object=CorrectexText)

    prompt = PromptTemplate(
        template="Correct the text.\n{format_instructions}\n{input_text}\n",
        input_variables=["input_text"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    # And a query intented to prompt a language model to populate the data structure.
    text_to_correct = "Thsi is not speled corectly."
    _input = prompt.format_prompt(input_text=text_to_correct)

    output = model(_input.to_string())

    parser.parse(output)