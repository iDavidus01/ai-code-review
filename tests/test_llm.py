import pytest
from aicr.config import Config
from aicr.llm import get_code_review

class MockResponse:
    def __init__(self, text):
        self.text = text

class MockModel:
    def __init__(self, model_name, system_instruction):
        pass
        
    def generate_content(self, diff):
        return MockResponse("LGTM!")

def test_get_code_review(monkeypatch):
    monkeypatch.setattr("google.generativeai.GenerativeModel", MockModel)
    config = Config(api_key="TEST_KEY", model="gemini-2.5-flash", ignore_paths=[])
    system_prompt = "Test prompt"
    review = get_code_review("fake diff", config, system_prompt)
    assert review == "LGTM!"
