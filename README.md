# Conway's Game of Life using Pygame and Numpy

This project is an implementation of Conway's Game of Life using Pygame and Numpy libraries in Python. The Game of Life is a cellular automaton created by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state and does not require any further input.

## Installation

To run this project, you need to have Python 3 installed on your system. You also need to install the following dependencies:

- Pygame
- Numpy
- Scipy

You can install these dependencies using pip. Open your terminal or command prompt and run the following commands:

pip install pygame numpy scipy

## Usage

To run the project, open the terminal or command prompt in the project directory and run the following command:

python main.py

This will open a window showing the initial state of the grid. Press the "W" key to start the simulation. The cells will evolve according to the rules of Conway's Game of Life. You can stop the simulation by closing the window or pressing the "Q" key.

## Code Structure

The `main.py` file contains the main code for the project. It initializes the Pygame library and creates a window to display the grid. It also contains the game loop that updates the grid and redraws it on the screen.

The `update_grid` function updates the state of the grid according to the rules of Conway's Game of Life. It uses the Numpy and Scipy libraries to perform convolution and element-wise operations on the grid.

The `draw_grid` function draws the grid on the Pygame window. It uses the Pygame library to draw rectangles on the screen.
