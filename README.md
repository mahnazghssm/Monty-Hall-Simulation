# 🎯 Monty Hall Simulation 🚗🐐

This project simulates the famous **Monty Hall Problem**, implemented in Python using **Streamlit** for dynamic visualizations. The simulation demonstrates how **switching doors increases your chance of winning** the car in a game show setup.

---

## 🧠 What is the Monty Hall Problem?

The Monty Hall Problem is a probability puzzle based on a game show scenario:

1. There are **3 doors**: behind one is a **car**, behind the others are **goats**.
2. You pick one door.
3. The host (Monty Hall), who knows what’s behind the doors, opens **one of the remaining doors**, revealing a **goat**.
4. You’re now given a choice: **stay** with your original door, or **switch** to the other unopened door.

🎯 The correct strategy is to **switch**, which gives you a **2/3 chance** of winning, compared to a **1/3 chance** if you stay.

---

## 🚀 Features

- Simulate up to **100,000 games**
- Real-time visualization of:
  - 🟥 Win % without switching
  - 🟩 Win % with switching
- Clean, interactive UI with **Streamlit**
- Fast simulation with animated chart updates

---

## ⚙️ Installation & Setup

To run this project locally:

1. **Clone the repository**
```bash
git clone https://github.com/mahnazghassemi/monty-hall-simulation.git
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
│   └── monty_hall.py        # Core simulation logic
├── app.py                   # Streamlit dashboard
├── README.md
├── requirements.txt
```
Simulate a Game 
Run the Streamlit app:
```
streamlit run app.py
```
🧪 How to Use
	1.	Choose the number of games to simulate.
	2.	Watch the win percentage charts update:
	•	🔴 No Switch: wins when sticking with the first choice
	•	🟢 Switch: wins when switching doors after the goat is revealed
	3.	Observe that switching wins ~66%, while not switching wins ~33% — just like theory predicts!

📊 Example Output

If you simulate 10,000 games:
	•	Switching wins ~66%
	•	Staying wins ~33%

These results align with the mathematical solution to the Monty Hall problem.


