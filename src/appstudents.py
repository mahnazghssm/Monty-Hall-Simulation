import streamlit as st
import time
from monty_hall import simulate_game

st.image(
    "https://www.mikealche.com/wp-content/uploads/2021/11/The-Monty-Hall-Problem-Demystified-1536x864.png",
    width=600
)
st.title("Monty Hall Simulation")
num_games = st.number_input(
    "Enter the number of games to simulate",
    min_value=1, max_value=100000, value=100
    )
col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")
chart1 = col1.line_chart(x = None, y = None, height=400)
chart2 = col2.line_chart(x = None, y = None, height=400)

wins_no_switch = 0
wins_switch = 0

for i in range(num_games):
    num_wins_without_switching, num_wins_with_switching = simulate_game(1)
    wins_no_switch += num_wins_without_switching
    wins_switch += num_wins_with_switching
    chart1.add_rows([wins_no_switch / (i + 1) * 100])
    chart2.add_rows([wins_switch / (i + 1) * 100])

    time.sleep(0.01) 