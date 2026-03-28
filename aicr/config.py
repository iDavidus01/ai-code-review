import os
import yaml
from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    api_key: str
    model: str
    ignore_paths: List[str]

def load_config() -> Config:
    api_key = os.environ.get("GEMINI_API_KEY", "")
    model = "gemini-2.5-flash"
    ignore_paths = []

    if os.path.exists(".aireview.yml"):
        with open(".aireview.yml", "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            if data:
                model = data.get("model", model)
                ignore_paths = data.get("ignore_paths", ignore_paths)

    return Config(api_key=api_key, model=model, ignore_paths=ignore_paths)
