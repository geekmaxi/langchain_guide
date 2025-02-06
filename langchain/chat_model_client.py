# from langchain_community.chat_models import ChatOpenAI, ChatOllama

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os

from dotenv import dotenv_values
env_config = dotenv_values("../.env")

from langchain.globals import set_debug

# 开启全局 verbose
# set_debug(True)

def get_deepseek():
    llm = ChatOpenAI(
        api_key=env_config['DEEPSEEK_API_KEY'],
        base_url=env_config['DEEPSEEK_BASE_URL'],
        model='deepseek-chat',
        temperature=0, # 设置成0最稳定；structured generation中稳定最重要
        max_tokens=2000,
        # model_kwargs = {
        #     'frequency_penalty':0,
        #     'presence_penalty':0,
        #     'top_p':1.0,
        # }
    )

    
    return llm

def get_openai():
    llm = ChatOpenAI(
        api_key=env_config['OPENAI_API_KEY'],
        model='gpt-3.5-turbo',
        temperature=0, # 设置成0最稳定；structured generation中稳定最重要
        max_tokens=2000,
        model_kwargs = {
            'frequency_penalty':0,
            'presence_penalty':0,
            'top_p':1.0,
        }
    )
    return llm

def get_llama():
    llm = ChatOllama(
        model='llama2-chinese',
        # base_url='http://localhost:11434',
        base_url=env_config['OLLAMA_BASE_URL'],
        temperature=0, # 设置成0最稳定；structured generation中稳定最重要
        max_tokens=2000,
        model_kwargs={
            'frequency_penalty':0,
            'presence_penalty':0,
            'top_p':1.0,
        }
        # frequency_penalty=0,
        # presence_penalty=0,
        # top_p=1.0
    )
    return llm

def get_model(model: str):
    if model == 'openai':
        return get_openai()
    elif model == 'deepseek':
        return get_deepseek()
    elif model == 'llama':
        return get_llama()