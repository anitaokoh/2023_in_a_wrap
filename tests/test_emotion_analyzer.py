# test_emotion_analyzer.py

from src.emotion_analyzer import EmotionAnalyzer
import pytest
from config.config import (emotions_list, instruction_prompt, context)
from dotenv import load_dotenv
import os

load_dotenv()

mock_api_key = os.getenv('MOCK_API_KEY')  # Mock API key for testing

@pytest.fixture
def emotion_analyzer():
    """
    Fixture for creating an instance of EmotionAnalyzer.

    This fixture initializes an EmotionAnalyzer with predefined instruction prompt,
    context, emotions list, and a mock API key for testing purposes.

    Returns:
        EmotionAnalyzer: An instance of EmotionAnalyzer for use in tests.
    """
    return EmotionAnalyzer(instruction_prompt, context, emotions_list, mock_api_key)

class TestEmotionAnalyzer:
    """
    Test suite for the EmotionAnalyzer class.

    This class contains a series of pytest test cases for testing the functionality
    of the EmotionAnalyzer class.
    """

    def test_extract_emotion_word(self, emotion_analyzer):
        """
        Test the extract_emotion_word method of EmotionAnalyzer.
        """
        mock_response = "The day was filled with Euphoria"
        expected_emotion = "Euphoria"
        assert emotion_analyzer.extract_emotion_word(mock_response) == expected_emotion

    def test_process_responses(self, emotion_analyzer):
        """
        Test the process_responses method of EmotionAnalyzer.

        Verifies that the method correctly processes a list of responses and extracts
        the emotion words.
        """
        mock_responses = ["The day was filled with Euphoria", "It was a day of Distress"]
        expected_processed = ["Euphoria", "Distress"]
        assert emotion_analyzer.process_responses(mock_responses) == expected_processed

    # Additional tests can be added here
