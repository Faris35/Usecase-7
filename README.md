# Player Performance Prediction App

This Streamlit app predicts the performance score of a player based on input features such as appearances, assists, injury days, and more. The prediction model is hosted via a FastAPI service deployed on Render.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Integration](#api-integration)

## Overview

The Player Performance Prediction App uses machine learning to analyze player statistics and predict their performance score. It takes user input through the app's sidebar, which includes data like the number of appearances, assists, days injured, and highest market value. The app then sends this data to an API endpoint and displays the predicted performance score.

## Features

- Input fields for:
  - Appearances
  - Assists
  - Days Injured
  - Games Missed
  - Awards (e.g., MVP Count)
  - Highest Value (€)
- Sends the data to an API (FastAPI) for prediction
- Displays the predicted performance score
- Handles missing or invalid responses from the API gracefully

## Installation

To run this app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Faris35/Usecase-7.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and go to `http://localhost:8501` to view the app.

## Usage

1. **Launch the App**: Once the app is running, open the app in your web browser.
2. **Enter Input**: On the sidebar, enter the player's data for the following parameters:
   - **Appearances**: Number of games the player has participated in.
   - **Assists**: Number of assists made by the player.
   - **Days Injured**: The number of days the player has been injured.
   - **Games Missed**: Number of games the player missed due to injury or other reasons.
   - **Awards (e.g., MVP Count)**: Number of awards the player has won.
   - **Highest Value (€)**: The highest market value of the player.

3. **Predict**: Click the "Predict Performance" button to get the player's predicted performance score based on the entered data.

4. **View Result**: The predicted performance score will be displayed at the center of the page.

## API Integration

The app integrates with a FastAPI service for predictions. The FastAPI service is hosted on Render. When the user clicks the "Predict Performance" button, the app sends a POST request with the following JSON payload:

```json
{
  "appearance": 0,
  "assists": 0,
  "days_injured": 0,
  "games_injured": 0,
  "award": 0,
  "highest_value": 0
}
```

### Key Highlights:
- **API Integration**: It explains how the Streamlit app integrates with the FastAPI service and the payload format expected by the API.
- **Installation & Usage**: Instructions on how to set up and run the app locally.
- **Error Handling**: It emphasizes how to ensure the correct number of features are sent to avoid errors from the API.
