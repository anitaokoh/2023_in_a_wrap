import pytest
import plotly.express as px
from src.download_viz import get_table_download_link  # Replace 'your_module' with the actual name of your Python file

class TestDownloadLink:
    @pytest.fixture
    def sample_figure(self):
        """Fixture to create a sample Plotly figure for testing."""
        df = px.data.iris()  # Sample dataset from Plotly Express
        fig = px.scatter(df, x='sepal_width', y='sepal_length')
        return fig

    def test_get_table_download_link(self, sample_figure):
        """Test the get_table_download_link function."""
        download_link = get_table_download_link(sample_figure)

        # Check if the download link is a string
        assert isinstance(download_link, str)

        # Check if the download link contains the expected structure
        assert 'href="data:file/image;base64,' in download_link
        assert 'download="My 2022 in a wrap.png"' in download_link
