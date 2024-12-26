import streamlit as st
import pandas as pd
from src.plotly_viz import create_fig
from src.download_viz import get_table_download_link
from src.emotion_analyzer import EmotionAnalyzer
from config.config import (emotion_index_map, emotion_emoji_map, emotions_list, emotion_scale,
                           month_list, month_index, instruction_prompt, context)

def initialize_session_state():
    """Initialize session state attributes."""
    default_values = {'disabled': False, 'placeholder': "Valid Openai API", 'visibility': "visible"}
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

def setup_page_layout():
    """Set up the page layout and style."""
    # max_width_str = f"max-width: 1030px;"
    # st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""", unsafe_allow_html=True)
    style_str = "<style>.reportview-container .main .block-container{max-width: 1030px;}</style>"
    st.markdown(style_str, unsafe_allow_html=True)
    st.image('images/year_in_a_wrap.jpg', use_container_width=True)

def display_intro():
    """Display the introduction section of the app."""
    st.subheader('How has your year been?')
    st.markdown(
        """<p>This has been a year filled with rollercoasters. Some good and some sad emotions.</p>
           <p>This web app helps to represent each month's highlights into five broad emotion category sentiments and creates a simple summary visualization.</p>
           <p>The emotions are: <strong>Euphoria, Contentment, Equanimity, Discomfort</strong>, and <strong>Distress</strong>.</p>""",
        unsafe_allow_html=True
    )
    if st.toggle('Turn on the toggle for more info about the emotion categories'):
        st.info(context)
    st.markdown("""### Wanna give the app a try? Go ahead and tick the start checkbox below
         """,unsafe_allow_html=True)

def get_user_input():
    """Collect user input for each month."""
    st.markdown("### Let's Begin")
    formatted_text = """
            Take a moment to write briefly a summary of each month.

            It could be a positive event that summarizes your month like 'In January, I got a new job offer that made my whole month'
            or a negative event like 'In March, I spent my time living on the streets because I was homeless'.

            The goal is to write out an event that was memorable (good or bad) and that overshadowed all other events that month.

            You also do not need to fill up all the month if you don't remember. You can leave the default message "Don't remember".
            """
#             # Display the formatted text in Streamlit
    st.write(formatted_text)
    data_input = []
    col1, col2 = st.columns(2)
    with col1:
        col1.subheader('First Half of the Year')
        for month in month_list[:6]:
            input_text = col1.text_area(month, "Don't remember")
            data_input.append(input_text)

    with col2:
        col2.subheader('Second Half of the Year')
        for month in month_list[6:]:
            input_text = col2.text_area(month, "Don't remember")
            data_input.append(input_text)

    return data_input

def create_and_display_chart(data):
    """Create and display the chart based on user data."""
    emotion_analyzer = EmotionAnalyzer(instruction_prompt, context, emotions_list, st.session_state['openai_api_key'])
    responses = emotion_analyzer.run_emotion_sent(data)
    processed_responses = emotion_analyzer.process_responses(responses)
    final_df = pd.DataFrame(zip(month_list, processed_responses, month_index, data),
                            columns=['Month', 'Emotion', 'Month_Index', 'summary'])
    final_df['Emotion_Scale'] = final_df['Emotion'].map(emotion_index_map)
    final_df['Emotion_Emoji'] = final_df['Emotion'].map(emotion_emoji_map)
    fig = create_fig(final_df, emotions_list, emotion_scale)
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    return fig

def viz_page():
    """Main function to run the visualization page."""
    setup_page_layout()
    display_intro()
    if st.checkbox('Start'):
        with st.container():
            data = get_user_input()
            st.session_state['openai_api_key'] = st.text_input("ADD YOUR OPENAI API FOR IT TO WORK",
                                                               label_visibility=st.session_state.visibility,
                                                               disabled=st.session_state.disabled,
                                                               placeholder=st.session_state.placeholder)
            if st.checkbox('Submit'):
                with st.expander('See Chart'):
                    fig = create_and_display_chart(data)
                    if st.button('Export Visualization image'):
                        st.text('Ready to Download')
                        st.markdown(get_table_download_link(fig), unsafe_allow_html=True)

if __name__ == "__main__":
    initialize_session_state()
    st.set_page_config(page_title="Your year in a wrap", page_icon="🎉", layout='wide', initial_sidebar_state='expanded')
    st.title("Your Year In A Wrap")
    viz_page()
