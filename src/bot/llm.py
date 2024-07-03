import os
from dotenv import load_dotenv, find_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

# from openai import AsyncOpenAI
import asyncio

env_path = "LLM-Hackathon/src/.env"

# Load environment variables from the specified .env file
load_dotenv(dotenv_path=env_path)

# Set the OpenAI API key
openai_api_key = os.getenv("HUGGINGFACE_API_TOKEN")
