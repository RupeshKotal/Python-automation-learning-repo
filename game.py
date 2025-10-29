import hashlib
import hmac
import matplotlib.pyplot as plt
import numpy as np

def generate_grid(server_seed, client_seed, nonce, rows=5, cols=5, mines=3):
    """
    Generate a grid for the Stake Mines game based on server seed, client seed, and nonce.

    Parameters:
    - server_seed: The server seed provided by the game.
    - client_seed: The client seed provided by the game.
    - nonce: The nonce value provided by the game, incremented with each game round.
    - rows: Number of rows in the grid (default is 5).
    - cols: Number of columns in the grid (default is 5).
    - mines: Number of mines to place in the grid (default is 3).

    Returns:
    - A grid with mines and gems.
    """
    # Combine seeds and nonce with additional factors
    seed_combination = f"{server_seed}-{client_seed}-{nonce}-{rows}-{cols}-{mines}"
    # Generate hash
    hash_result = hmac.new(bytes(server_seed, 'utf-8'), bytes(seed_combination, 'utf-8'), hashlib.sha256).hexdigest()
    # Convert hash to a list of integers
    hash_integers = [int(hash_result[i:i+8], 16) for i in range(0, len(hash_result), 8)]

    # Ensure deterministic shuffling based on seeds
    random.seed(hash_integers[0])
    random.shuffle(hash_integers)

    # Map integers to grid positions without collisions
    grid = [['gem' for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()

    while len(mine_positions) < mines:
        pos = hash_integers.pop(0) % (rows * cols)
        mine_positions.add(pos)

    for pos in mine_positions:
        row = pos // cols
        col = pos % cols
        grid[row][col] = 'mine'

    return grid

def print_grid(grid):
    """
    Print the grid in a readable format.
    """
    for row in grid:
        print(' '.join(row))

def visualize_grid(grid):
    """
    Visualize the grid using matplotlib.
    """
    fig, ax = plt.subplots()
    cmap = plt.cm.colors.ListedColormap(['lightblue', 'red'])
    bounds = [0, 1, 2]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    # Create a matrix for visualization
    matrix = np.array([[0 if cell == 'gem' else 1 for cell in row] for row in grid])

    cax = ax.imshow(matrix, cmap=cmap, norm=norm)

    # Add grid lines
    ax.grid(which="minor", color="w", linestyle='-', linewidth=2)
    ax.set_xticks(np.arange(-0.5, len(grid[0]), 1))
    ax.set_yticks(np.arange(-0.5, len(grid), 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Add color bar
    fig.colorbar(cax, ticks=[0, 1], boundaries=bounds, fraction=0.046, pad=0.04)

    plt.show()

# Example usage with provided seeds
server_seed = "ae053a23c42b00c562d418b81ad5397697d438f7ddcf9293fa9bca1ded3be44f"
client_seed = "62755a6a24e1cf17"
nonce = 1  # Replace with the actual nonce value from the game

# Generate the grid
grid = generate_grid(server_seed, client_seed, nonce)

# Print the grid
print_grid(grid)

# Visualize the grid
visualize_grid(grid)
