import google.generativeai as genai
from .config import Config

def initialize_gemini(config: Config) -> None:
    genai.configure(api_key=config.api_key)

def get_code_review(diff: str, config: Config, system_prompt: str) -> str:
    model = genai.GenerativeModel(
        model_name=config.model,
        system_instruction=system_prompt
    )
    response = model.generate_content(diff)
    return response.text
