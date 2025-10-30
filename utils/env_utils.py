import os
from dotenv import load_dotenv, set_key
from typing import Tuple

load_dotenv("./.env")

def get_env_var(key: str) -> str:
    '''Gets an env variable value'''
    value = os.getenv(key, None)
    if not value:
        raise Exception(f"Failed to load env variable: {key}")
    return value

def set_env_var(key: str, value: str) -> None:
    '''Sets an env variable value'''
    set_key(str("./.env"), key, value)

def get_last_count() -> int:
    '''Gets the last Kev Count'''
    return int(get_env_var("LAST_KEV_COUNT"))

def update_last_count(new_count: int) -> None:
    '''Updates the last Kev Count'''
    set_env_var("LAST_KEV_COUNT", str(new_count))

def load_prompts() -> Tuple[str, str]:
    '''Loads system prompts'''
    return (get_env_var("CONTEXT_CONTROLLER_AGENT_SYSTEM_PROMPT"), get_env_var("REPORTER_AGENT_SYSTEM_PROMPT"))