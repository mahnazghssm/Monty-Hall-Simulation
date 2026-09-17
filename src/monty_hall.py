import random


def monty_hall_game(switch_doors: bool) -> bool:
    """
    Simulates one round of the Monty Hall game.

    :param switch_doors: Whether the player switches doors.
    :return: True if the player wins, otherwise False.
    """
    doors = ["car", "goat", "goat"]
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    doors_revealed = [
        i
        for i in range(3)
        if i != initial_choice and doors[i] != "car"
    ]
    door_revealed = random.choice(doors_revealed)

    if switch_doors:
        final_choice = [
            i
            for i in range(3)
            if i != initial_choice and i != door_revealed
        ][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"


def simulate_game(num_of_game: int) -> tuple[int, int]:
    """
    Simulates a specified number of Monty Hall games.

    :param num_of_game: Number of games to simulate.
    :return: Number of wins without switching and with switching.
    """
    number_of_wins_without_switching: int = sum(
        [monty_hall_game(False) for _ in range(num_of_game)]
    )

    number_of_wins_with_switching: int = sum(
        [monty_hall_game(True) for _ in range(num_of_game)]
    )

    return (
        number_of_wins_without_switching,
        number_of_wins_with_switching,
    )


if __name__ == "__main__":
    num_game = 1000

    wins_without_switching, wins_with_switching = simulate_game(num_game)

    print(
        f"Winning percentage without switching doors: "
        f"{wins_without_switching / num_game * 100}%"
    )
    print(
        f"Winning percentage with switching doors: "
        f"{wins_with_switching / num_game * 100}%"
    )
