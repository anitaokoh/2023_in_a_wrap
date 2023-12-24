# emotion_analyzer.py

from langchain.llms import OpenAI

class EmotionAnalyzer:
    """
    A class to analyze emotions from text using a language model.

    Attributes:
        context (str): The context used for emotion analysis.
        emotions_list (list): A list of possible emotions.
        llm (OpenAI): An instance of the OpenAI language model.
    """

    def __init__(self,instruction_prompt, context, emotions_list, openai_api_key):
        """
        Initializes the EmotionAnalyzer with the given context, emotions list, and OpenAI API key.

        Args:
            context (str): The context used for emotion analysis.
            emotions_list (list): A list of possible emotions.
            openai_api_key (str): The API key for accessing OpenAI's language model.
        """
        self.instruction_prompt = instruction_prompt
        self.context = context
        self.emotions_list = emotions_list
        self.llm = OpenAI(openai_api_key=openai_api_key)

    def run_emotion_sent(self, user_texts):
        """
        Analyzes the emotions in the given texts.

        Args:
            user_texts (list): A list of texts to analyze.

        Returns:
            list: A list of responses from the language model.
        """
        responses = []
        for user_text in user_texts:
            prompt = (
                self.instruction_prompt +
                '{context}\n\n'.format(context=self.context) +
                'Here\'s the text:\n' + user_text
            )
            response = self.llm(prompt)
            responses.append(response)
        return responses

    def extract_emotion_word(self, response):
        """
        Extracts the emotion word from a given response.

        Args:
            response (str): A response from the language model.

        Returns:
            str: The extracted emotion word, or an empty string if not found.
        """
        words = response.lower().split()
        emotion_words = [emotion.lower() for emotion in self.emotions_list]
        for word in words:
            if word in emotion_words:
                return word.capitalize()
        return ""

    def process_responses(self, responses):
        """
        Processes a list of responses to extract emotion words.

        Args:
            responses (list): A list of responses from the language model.

        Returns:
            list: A list of extracted emotion words.
        """
        processed_responses = []
        for response in responses:
            emotion = self.extract_emotion_word(response)
            processed_responses.append(emotion)
        return processed_responses
