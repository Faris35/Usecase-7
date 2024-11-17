import streamlit as st
import requests

# Set the FastAPI endpoint
API_URL = "https://usecase-7-wgvt.onrender.com/predict"

# Streamlit app customization
st.set_page_config(
    page_title="Player Performance Predictor",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App title and description
st.markdown(
    """
    <style>
    .main-title {
        font-size: 36px;
        color: #3D85C6;
        font-weight: bold;
        text-align: center;
    }
    .sub-title {
        font-size: 18px;
        color: #444;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    <div class="main-title">Player Performance Predictor</div>
    <div class="sub-title">Analyze player data and predict performance outcomes</div>
    """,
    unsafe_allow_html=True,
)

# Sidebar input
st.sidebar.title("⚙️ Configure Inputs")
st.sidebar.markdown(
    "Enter player data below. Adjust values to predict performance metrics dynamically."
)

# Input fields for user data
appearance = st.sidebar.slider("Appearances", 0, 100, 10)
assists = st.sidebar.slider("Assists", 0.0, 50.0, 0.0)
days_injured = st.sidebar.slider("Days Injured", 0, 365, 10)
games_injured = st.sidebar.slider("Games Missed", 0, 50, 2)
award = st.sidebar.slider("Awards (e.g., MVP Count)", 0, 10, 0)
highest_value = st.sidebar.number_input(
    "Highest Value (€)", min_value=0, value=100000, step=10000, format="%d"
)

# Display selected input summary
with st.expander("📋 Input Summary", expanded=True):
    st.write(
        f"""
        - **Appearances**: {appearance}
        - **Assists**: {assists}
        - **Days Injured**: {days_injured}
        - **Games Missed**: {games_injured}
        - **Awards**: {award}
        - **Highest Value (€)**: {highest_value}
        """
    )

# Create a payload for the API request
payload = {
    "appearance": appearance,
    "assists": assists,
    "days_injured": days_injured,
    "games_injured": games_injured,
    "award": award,
    "highest_value": highest_value,
}

# Predict button and result display
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🔍 Predict Performance"):
        with st.spinner("Fetching prediction..."):
            try:
                # Make a POST request to the FastAPI endpoint
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()  # Raise error for bad responses

                # Check if the response contains the 'pred' key
                prediction = response.json()
                if 'pred' in prediction:
                    # Display the prediction
                    st.success(f"Predicted Performance Score: {prediction['pred']}")
                else:
                    st.error("Prediction key ('pred') not found in the response.")
                    
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
