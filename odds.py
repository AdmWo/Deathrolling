import random
import matplotlib.pyplot as plt

def deathroll_simulation(num_simulations, max_roll):
    if max_roll < 1:
        raise ValueError("max_roll must be greater than or equal to 1")

    win_probabilities_player1 = [0] * max_roll
    win_probabilities_player2 = [0] * max_roll

    for _ in range(num_simulations):
        starting_roll = random.randint(1, max_roll)
        current_player = 1
        roll = starting_roll

        while roll != 1:
            current_player = 3 - current_player  # Switch players (1 <-> 2)
            roll = random.randint(1, max_roll)

        if current_player == 1:
            win_probabilities_player1[starting_roll - 1] += 1
        else:
            win_probabilities_player2[starting_roll - 1] += 1

    total_simulations = num_simulations
    win_probabilities_player1 = [wins / total_simulations for wins in win_probabilities_player1]
    win_probabilities_player2 = [wins / total_simulations for wins in win_probabilities_player2]

    return win_probabilities_player1, win_probabilities_player2

num_simulations = 1000  # Adjust the number of simulations as needed
max_roll = 100  # Adjust the maximum roll value as needed

try:
    win_probabilities_player1, win_probabilities_player2 = deathroll_simulation(num_simulations, max_roll)

    # Create a line chart
    rolls = list(range(1, max_roll + 1))

    plt.plot(rolls, win_probabilities_player1, label='Player 1', color='blue')
    plt.plot(rolls, win_probabilities_player2, label='Player 2', color='green')
    plt.xlabel('Starting Roll Number')
    plt.ylabel('Win Probability')
    plt.title('Deathrolling Win Probability by Starting Roll Number')
    plt.legend()
    plt.grid(True)
    plt.show()
except ValueError as e:
    print(e)
