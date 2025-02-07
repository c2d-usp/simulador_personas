from functools import lru_cache

from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import ChatOpenAI

from source.chat_graph.models import ModelName
from source.constantes import TEMPERATURE, FREQUENCY_PENALTY, PRESENCE_PENALTY


@lru_cache(maxsize=4)
def get_llm(model_name: ModelName) -> ChatOpenAI | GoogleGenerativeAI:
    """
    Loads a language model.
    :param model_name: Enum with the name of the model to load.
    :return: A ChatOpenAI or GoogleGenerativeAI object configured with the chosen model.
    :raises ValueError: If the model cannot be loaded.
    """
    if model_name in [ModelName.GPT4_MINI, ModelName.GPT4]:
        return get_openai_llm(model_name)
    elif model_name in [ModelName.GEMINI_THINKING_EXP]:
        return get_google_model(model_name)
    else:
        raise ValueError(f"Model {model_name} not found.")

@lru_cache(maxsize=4)
def get_openai_llm(model_name: ModelName) -> ChatOpenAI:
    """
    Loads an OpenAI language model.
    :param model_name: Enum with the name of the model to load.
    :return: A ChatOpenAI object configured with the chosen model.
    :raises ValueError: If the model cannot be loaded.
    """
    openai_model: str = model_name.value
    try:
        model = ChatOpenAI(model=openai_model,
                           temperature=TEMPERATURE,
                           presence_penalty=PRESENCE_PENALTY,
                           frequency_penalty=FREQUENCY_PENALTY)
        return model
    except Exception as e:
        raise ValueError(f"Error loading the model {model_name}: {e}")

@lru_cache(maxsize=4)
def get_google_model(model_name: ModelName) -> GoogleGenerativeAI:
    """
    Loads a Google language model.
    :param model_name: Enum with the name of the model to load.
    :return: A GoogleGenerativeAI object configured with the chosen model.
    :raises ValueError: If the model cannot be loaded.
    """
    google_model: str = model_name.value
    try:
        model = GoogleGenerativeAI(model=google_model)
        return model
    except Exception as e:
        raise ValueError(f"Error loading the model {model_name}: {e}")