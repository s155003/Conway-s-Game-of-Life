# Conway's Game of Life (Terminal Version)

This is a Python implementation of **Conway’s Game of Life**, a zero-player game where cells on a grid evolve over time based on simple rules. The simulation runs directly in the terminal and animates generations using ASCII characters.

## 📌 Features
- Terminal-based grid animation using ASCII blocks (`█`)
- Starts with a predefined "blinker" pattern
- Automatically evolves for 20 generations
- Clean, modular code for easy modification

## 🚀 How It Works
Each cell in a 2D grid is either **alive** (`1`) or **dead** (`0`). The simulation applies the following rules at each step:
1. A live cell with 2 or 3 neighbors survives.
2. A dead cell with exactly 3 neighbors becomes alive.
3. All other cells die or remain dead.

These rules are applied simultaneously to every cell to generate the next frame of the animation.
