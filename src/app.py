import streamlit as st
from src.monty_hall import simulate_game  # Importing the function to simulate the Monty Hall game
import time  # Used for adding a delay in chart updates for visual effect

# Setting the title and an image for the simulation app
st.title(":car: Monty Hall Simulation :goat:")
st.image("https://res.cloudinary.com/practicaldev/image/fetch/s--HUHJXhRr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/dppd3jokklf3jbhb1sk0.png", width=600)

# Input box to enter the number of games to simulate with min, max, and default values
num_games = st.number_input("Enter number of games to simulate",
                            min_value=1, max_value=100000,
                            value=100
)

# Creating two columns for side-by-side charts
col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")

# Initializing empty charts for each column
chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

# Variables to keep track of wins
wins_no_switch = 0
wins_switch = 0

# Main loop to run the number of simulations specified by the user
for i in range(num_games):
    # Simulate one game at a time, the function returns the wins for no switching and switching cases
    number_of_wins_without_switching, number_of_wins_with_switching = simulate_game(1)
    
    # Increment win counts
    wins_no_switch += number_of_wins_without_switching
    wins_switch += number_of_wins_with_switching

    # Update the charts with the win percentage so far
    # The win percentage is wins / total games so far
    chart1.add_rows([wins_no_switch / (i + 1)])  # For no switching
    chart2.add_rows([wins_switch / (i + 1)])     # For switching

    # Adding a small delay to slow down the simulation so users can visually see the chart update
    # The delay is more noticeable for a smaller number of games
    time.sleep(0.01)