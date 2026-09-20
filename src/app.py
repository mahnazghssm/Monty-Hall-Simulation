import time

import streamlit as st

from monty_hall import simulate_game

st.image("src/images/banner.png")

num_games = st.number_input(
    "Enter number of games to simulate",
    min_value=1,
)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")

chart1 = col1.empty()
chart2 = col2.empty()

wins_no_switch = 0
wins_switch = 0
history_no_switch = []
history_switch = []

for i in range(num_games):
    no_switch_win, switch_win = simulate_game(1)

    wins_no_switch += no_switch_win
    wins_switch += switch_win

    history_no_switch.append(wins_no_switch / (i + 1))
    history_switch.append(wins_switch / (i + 1))

    chart1.line_chart(history_no_switch, height=400)
    chart2.line_chart(history_switch, height=400)

    time.sleep(0.01)

st.metric("Final Win % Without Switching", f"{wins_no_switch / num_games * 100:.2f}%")
st.metric("Final Win % With Switching", f"{wins_switch / num_games * 100:.2f}%")
