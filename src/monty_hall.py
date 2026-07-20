import random

def monty_hall_game(switch_doors: bool) -> bool:
    """
    This function simulates one round of the Monty Hall game.
    It randomly shuffles the doors, lets the player pick one, and then simulates Monty revealing a goat behind one of the remaining doors.
    Depending on the value of switch_doors, the player either switches their choice to the other door or stays with their initial choice.
    The function returns True if the player wins (i.e., chooses the car) and False otherwise.

    :param switch_doors: A boolean flag indicating whether the player should switch doors 
    after Monty reveals a goat (True for switching, False for staying).

    :return: True if the player's final choice is the car, False otherwise.
    """
    doors = ["car", "goat", "goat"]  # List of doors, where one has a car and two have goats
    random.shuffle(doors)  # Randomly shuffles the list

    initial_choice = random.choice(range(3))  # Player's initial random choice of door (0, 1, or 2)

    # List of doors Monty can reveal (a door with a goat that's not the initial choice)
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != "car"]
    door_revealed = random.choice(doors_revealed)  # Monty reveals one of the doors with a goat

    # If the player switches, they pick the remaining door. Otherwise, they stick with the initial choice.
    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"  # Return True if the final choice has the car


def simulate_game(num_of_game: int) -> tuple[int, int]:
    """
    Simulates a specified number of Monty Hall games and returns the number of wins
    when the player switches doors and when the player does not switch.

    :param num_of_game: The number of Monty Hall game simulations to run.

    :return: A tuple containing two integers: the number of wins without switching 
    and the number of wins with switching.
    """
    # Sum the number of wins without switching by running the game `num_of_game` times
    number_of_wins_without_switching: int = sum([monty_hall_game(False) for _ in range(num_of_game)])
    
    # Sum the number of wins with switching by running the game `num_of_game` times
    number_of_wins_with_switching: int = sum([monty_hall_game(True) for _ in range(num_of_game)])

    return number_of_wins_without_switching, number_of_wins_with_switching


if __name__ == "__main__":
    num_game = 1000  # Number of games to simulate
    wins_without_switching, wins_with_switching = simulate_game(num_game)

    print(f"Winning percentage without switching doors: {wins_without_switching / num_game * 100}%")
    print(f"Winning percentage with switching doors: {wins_with_switching / num_game * 100}%")