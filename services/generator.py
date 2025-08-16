import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI   # ✅ new import
from langchain.prompts import PromptTemplate

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),   # ✅ param is `api_key` now
    model="gpt-3.5-turbo",                 # ✅ param is `model` instead of model_name
    temperature=0.2
)

# Prompt template
prompt_template = """
You are a helpful assistant. Use the following documents to answer the question.
Documents:
{context}

Question: {question}

Answer:
"""
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)

def generate_answer(question: str, docs: list) -> str:
    context = "\n\n".join(docs)
    formatted_prompt = prompt.format(context=context, question=question)

    # ✅ Call with messages (ChatOpenAI expects a list of messages)
    response = llm.invoke([{"role": "user", "content": formatted_prompt}])

    return response.content
# services/generator.py - Generate answers using LLM and retrieved documents
# This file contains the logic to generate answers based on retrieved documents and user questions