# Monty Hall Simulation

## Description

This project is a Python simulation of the Monty Hall problem.

It compares two strategies:

- Staying with the first choice
- Switching to the other unopened door

The project also includes a Streamlit dashboard to run the simulation and see the results in charts.

## The Monty Hall Problem

The Monty Hall problem is a probability problem with three doors.

Behind one door there is a car, and behind the other two doors there are goats.

The contestant first chooses one door. The host then opens one of the other doors and shows a goat. The contestant can then either stay with the first choice or switch to the other unopened door.

This project uses simulation to compare these two choices.

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── .gitignore
└── src
    ├── monty_hall.py
    ├── app.py
    └── images
        └── banner.png
```

- `monty_hall.py`: Contains the simulation logic
- `app.py`: Streamlit dashboard
- `banner.png`: Image used in the dashboard
- `requirements.txt`: Required packages
- `.gitignore`: Files and folders ignored by Git

## Technologies

- Python
- Streamlit
- Pandas

## Requirements

- Python 3.7 or higher
- Streamlit
- Pandas

## Installation

Clone the repository:

```bash
git clone https://github.com/mahnazghssm/Monty-Hall-Simulation.git
```

Go to the project folder:

```bash
cd Monty-Hall-Simulation
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Run the Python Script

```bash
python src/monty_hall.py
```

This runs the simulation in the terminal and prints the winning percentages for both strategies.

### Run the Streamlit Dashboard

```bash
streamlit run src/app.py
```

The dashboard lets you choose the number of games and shows two charts for the results.

## Results

With a large number of simulations, the results usually get closer to the theoretical probabilities:

- Staying: about 33%
- Switching: about 67%

The exact results can be different each time because the simulation uses random choices.

## What I Practiced

- Python functions
- Loops and conditional statements
- Randomization
- Basic probability and simulation
- Pandas
- Data visualization
- Streamlit

## Author

Mahnaz Ghassemi

GitHub: mahnazghssm