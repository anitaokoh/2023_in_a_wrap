

# Emotion mappings and lists
emotion_index_map = {"Euphoria": 5, "Contentment": 4, "Equanimity": 3, "Discomfort": 2, "Distress": 1}
emotion_emoji_map = {"Euphoria": '😁', "Contentment": '😌', "Equanimity": '🙂', "Discomfort": '😕', "Distress": '😢'}
emotions_list = list(emotion_index_map.keys())
emotion_scale = list(emotion_index_map.values())
month_list = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
month_index = list(range(1, 13))

# Instruction prompt
instruction_prompt = (
    'Use the following description in the context and the following emotion categories (Euphoria, Contentment, Equanimity, Discomfort, Distress) to categorize the sentiment emotion of the text.\n'
    'Do not use any other information you might have learned to categorize the emotion in the text.\n'
    'Only base your answer on the information retrieved and the 5 emotion categories.\n'
    'Format of Response: If the emotion is Euphoria, just return "Euphoria". Do not explain and no prefix.\n'
    "If text is 'Dont Remember', just return 'Equanimity'\n"
)

# Context description
context = """For the top tier of extremely positive emotions, 'Euphoria' captures feelings of extreme joy, bliss, and ecstasy. This term encompasses the highest peaks of positive human emotion, where experiences are intensely pleasurable and overwhelmingly positive.

For the moderately positive emotions, 'Contentment' is a suitable term as it covers feelings of happiness, satisfaction, and pleasure that are less intense but still distinctly positive. It's the emotion of being pleased with your situation and generally feeling good about life.

For the neutral middle, 'Equanimity' is an apt description. It signifies a state of calmness, balance, and emotional stability. In this state, a person experiences neither strong positive nor negative emotions but rather a sense of peaceful detachment or indifference.

For the moderately negative emotions, 'Discomfort' is a fitting term as it includes feelings like mild sadness, frustration, and worry. These are emotions that cause some degree of unease or dissatisfaction but are not overwhelmingly intense.

For the most intense negative emotions, 'Distress' captures deep feelings of despair, rage, severe grief, and intense fear. These are powerful emotions that significantly impact a person's well-being and are often experienced in response to serious adversities or trauma."""
