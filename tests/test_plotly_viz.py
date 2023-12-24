import pytest
import pandas as pd
from src.plotly_viz import create_fig  # Replace 'your_module' with the actual name of your Python file

class TestVisualization:
    @pytest.fixture
    def sample_data(self):
        """Fixture to create sample data for testing."""
        data = {
            'Month_Index': [1, 2, 3, 4, 5],
            'Emotion_Scale': [3, 4, 2, 5, 3],
            'Month': ['January', 'February', 'March', 'April', 'May'],
            'Emotion_Emoji': ['😁', '🙂', '😌', '😕', '😢'],
            'summary': ['Happy', 'Content', 'Calm', 'Anxious', 'Sad']
        }
        df = pd.DataFrame(data)
        return df

    def test_create_fig(self, sample_data):
        """Test the create_fig function."""
        emotions_list = ["Euphoria", "Contentment", "Equanimity", "Discomfort", "Distress"]
        emotion_scale = [5, 4, 3, 2, 1]

        fig = create_fig(sample_data, emotions_list, emotion_scale)

        # Assert that the figure is a Plotly graph object
        assert 'plotly.graph_objs._figure.Figure' in str(type(fig))

        # Additional assertions can be added here to check specific properties of the figure
