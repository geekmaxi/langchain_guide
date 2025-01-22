# from langchain_community.llms.openai import OpenAI
# from langchain_community.llms.ollama import Ollama
from langchain_ollama import OllamaLLM
from langchain_openai import OpenAI
from langchain_core.language_models import BaseLLM
from dotenv import dotenv_values
env_config = dotenv_values("../.env")

def get_model(model: str):
    if model == "openai":
        return OpenAI(
            api_key=env_config['OPENAI_API_KEY'],
            model='gpt-3.5-turbo',
            base_url=env_config['OPENAI_BASE_URL']
        )
    elif model == "llama":
        return OllamaLLM(model="llama2-chinese",base_url=env_config['OLLAMA_BASE_URL'])
    elif model == "deepseek":
        return OpenAI(
            model="deepseek-v3",
            base_url=env_config["DEEPSEEK_BASE_URL"],
            # base_url="https://api.deepseek.com/beta",
            api_key=env_config["DEEPSEEK_API_KEY"],
            )