# Connect Four AI 

## Overview

Connect Four AI is an Artificial Intelligence project that implements the classic Connect Four game with an intelligent computer opponent. The AI uses the Minimax algorithm with Alpha-Beta Pruning to analyze possible future game states and select the optimal move.

This project demonstrates fundamental AI concepts such as adversarial search, game trees, heuristic evaluation, decision-making, and search optimization techniques.

## Features

* Interactive Connect Four game built using Python and Pygame
* Human vs AI gameplay
* AI opponent powered by Minimax Algorithm
* Alpha-Beta Pruning for efficient search
* Real-time game board visualization
* Automatic win detection
* Heuristic evaluation of board positions
* Strategic AI decision-making

## Artificial Intelligence Concepts Demonstrated

### Minimax Algorithm

The AI evaluates all possible future moves and chooses the move that maximizes its chances of winning while minimizing the opponent's chances.

### Alpha-Beta Pruning

An optimization technique that reduces the number of nodes explored in the game tree, making the AI faster without affecting the quality of decisions.

### Adversarial Search

The game represents a competitive environment where the AI and human player have opposing objectives.

### Heuristic Evaluation Function

The AI assigns scores to board states and uses these scores to determine the most favorable positions.

## Technologies Used

* Python 3.x
* Pygame
* NumPy

## Project Structure

```text
ConnectFourAI/
│
├── main.py
├── connect_four.py
├── minimax.py
├── assets/
│
├── README.md
└── report.docx
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd ConnectFourAI
```

### Install Dependencies

```bash
pip install pygame numpy
```

## Running the Project

```bash
python main.py
```

## How to Play

1. Launch the game.
2. The human player plays first.
3. Click on a column to drop your piece.
4. The AI will automatically calculate and perform its move.
5. The first player to connect four pieces horizontally, vertically, or diagonally wins.
6. The game displays the winner once a winning condition is achieved.

## Game Rules

* The board consists of 6 rows and 7 columns.
* Players take turns dropping pieces into columns.
* Pieces occupy the lowest available position in a column.
* Four consecutive pieces of the same player form a winning connection.
* Winning connections can be horizontal, vertical, or diagonal.

## Applications

This project can be used for:

* Artificial Intelligence coursework
* Academic demonstrations
* Understanding game-playing strategies
* Learning Minimax and Alpha-Beta Pruning
* Educational AI experiments

## Future Enhancements

* Multiple difficulty levels
* Improved evaluation heuristics
* Player vs Player mode
* Score tracking system
* Sound effects and animations
* Online multiplayer support
* Advanced AI strategies

## Learning Outcomes

Through this project, the following AI concepts are demonstrated:

* Game Tree Search
* Adversarial Search
* Decision Making
* Minimax Algorithm
* Alpha-Beta Pruning
* Heuristic Evaluation Functions
* Intelligent Agent Design

## Conclusion

This project successfully demonstrates how Artificial Intelligence can be applied to game-playing environments. By implementing Minimax with Alpha-Beta Pruning, the AI is capable of making intelligent decisions and providing a challenging opponent for the player. The project serves as a practical example of search-based AI techniques and strategic decision-making.
