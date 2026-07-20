import streamlit as st
from monty_hall import simulate_game  # Import your simulation logic
import time


# ----------------------- Streamlit UI Setup -----------------------

st.set_page_config(page_title="Monty Hall Simulation", layout="centered")

# Display an explanatory image about the Monty Hall problem
st.image(
    "https://www.mikealche.com/wp-content/uploads/2021/11/The-Monty-Hall-Problem-Demystified-1536x864.png",
    width=600
)

# Title of the dashboard
st.title("🎯 Monty Hall Simulation")


# ----------------------- User Input -----------------------

# Number of games to simulate
num_games: int = st.number_input(
    "Enter number of games to simulate:",
    min_value=1,
    max_value=100000,
    value=100
)


# ----------------------- Charts Setup -----------------------

# Two side-by-side charts: one for each strategy
col1, col2 = st.columns(2)

col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")

# Initialize empty line charts
chart1 = col1.line_chart({"Win %": []}, height=400)
chart2 = col2.line_chart({"Win %": []}, height=400)


# ----------------------- Simulation Loop -----------------------

wins_no_switch: int = 0
wins_switch: int = 0

# Run the simulation one game at a time for visual feedback
for i in range(num_games):
    # Simulate a single game
    wins_switch_increment, wins_no_switch_increment = simulate_game(1)

    # Accumulate total wins
    wins_no_switch += wins_no_switch_increment
    wins_switch += wins_switch_increment

    # Update line charts with cumulative win percentages
    chart1.add_rows({"Win %": [wins_no_switch / (i + 1)]})
    chart2.add_rows({"Win %": [wins_switch / (i + 1)]})

    # Slight delay for animation
    time.sleep(0.01)


# ----------------------- Final Summary -----------------------

# Display final metrics below charts
st.success("✅ Simulation complete!")
st.metric("Final Win % Without Switching", f"{wins_no_switch / num_games * 100:.2f}%")
st.metric("Final Win % With Switching", f"{wins_switch / num_games * 100:.2f}%")