# Monty Hall Simulaion 🎉🚗🐐
This project is a simulation of the famous Monty Hall Problem, implemented using Python and the Streamlit library for visualizing results. The problem demonstrates how switching doors improves the probability of winning the car in a game show. You can simulate thousands of games to see how the probabilities evolve.

## The Monty Hall Problem
The Monty Hall Problem is a brain teaser based on a TV game show. The problem goes as follows:

1.	There are 3 doors, one of which hides a car while the other two hide goats.
2.	You pick one door (hoping to win the car).
3.	The host, Monty Hall, who knows what’s behind the doors, opens one of the other two doors to reveal a goat.
4.	You are then given a choice: stick with your original choice or switch to the other unopened door.

The key question is: Should you switch or not to maximize your chances of winning the car?

The answer is: Yes, you should switch!. Switching gives you a 2/3 chance of winning, while staying with your initial choice only gives you a 1/3 chance.

## features 
•	Simulate up to 100,000 games of the Monty Hall problem.
•	Real-time visualization of the win percentages for both strategies: switching vs. not switching.
•	Dynamic and interactive chart updates as the simulation progresses.
•	A clean and simple UI powered by Streamlit.

## installation

To run this project locally, follow these steps:

1.	Clone the repository:

```
git clone https://github.com/your-username/monty-hall-simulation.git
cd monty-hall-simulation
```

2.	Set up a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3.	Install dependencies:
Make sure you have Streamlit installed by running:
```
pip install -r requirements.txt
```
4.	Install Streamlit:
```
pip install -r requirements.txt
```
5.	Create the required file structure:
The simulation code assumes you have a file src/monty_hall.py that contains the simulate_game() function. Make sure your project structure looks like this:
```
monty-hall-simulation/
├── src/
│   └── monty_hall.py
├── app.py
├── README.md
├── requirements.txt
```
Simulate a Game
1.	Run the Streamlit app:
```
streamlit run app.py
```
2.	Using the app:
•	You will see two options for simulating the Monty Hall problem: Win Percentage Without Switching and Win Percentage With Switching.
•	Input the number of games you’d like to simulate (between 1 and 100,000).
•	Watch as the charts dynamically update to reflect the winning percentages as more games are simulated.
3.	Understanding the Results:
•	The No Switch Win Percentage shows the likelihood of winning if you stick with your first choice.
•	The Switch Win Percentage shows the likelihood of winning if you switch doors after the host reveals a goat.

## Example Simulation
If you simulate 10,000 games, you’ll observe that switching doors tends to win about 66% of the time, while not switching wins about 33% of the time. These results align with the theoretical probabilities of the Monty Hall Problem.
