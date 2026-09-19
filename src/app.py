import time

import streamlit as st

from monty_hall import simulate_game


st.set_page_config(
    page_title="Monty Hall Simulation",
    layout="centered",
)


# Display an image about the Monty Hall problem
st.image(
    "src/images/banner.png",
    width=600,
)

st.title("🎯 Monty Hall Simulation")


# Number of games to simulate
num_games: int = st.number_input(
    "Enter number of games to simulate:",
    min_value=1,
    max_value=100000,
    value=100,
)


# Create two charts
col1, col2 = st.columns(2)

col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")

chart1 = col1.line_chart({"Win %": []}, height=400)
chart2 = col2.line_chart({"Win %": []}, height=400)


wins_no_switch: int = 0
wins_switch: int = 0


# Run the simulation
for i in range(num_games):
    wins_switch_increment, wins_no_switch_increment = simulate_game(1)

    wins_no_switch += wins_no_switch_increment
    wins_switch += wins_switch_increment

    # Update the charts
    chart1.add_rows(
        {"Win %": [wins_no_switch / (i + 1)]}
    )
    chart2.add_rows(
        {"Win %": [wins_switch / (i + 1)]}
    )

    time.sleep(0.01)


# Display final results
st.success("✅ Simulation complete!")

st.metric(
    "Final Win % Without Switching",
    f"{wins_no_switch / num_games * 100:.2f}%",
)

st.metric(
    "Final Win % With Switching",
    f"{wins_switch / num_games * 100:.2f}%",
)
