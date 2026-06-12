# Pathfinding Visualizer

Interactive pathfinding visualizer built with Python and Pygame, featuring real-time animation of BFS, DFS, Dijkstra, and A* algorithms on a dynamic grid.

## 🚀 Features
- Interactive 20x20 grid-based interface
- Start node and end node placement
- Left-click wall creation
- Click-and-drag wall placement
- Right-click cell clearing
- Random maze generation
- Algorithm selection dropdown
- Adjustable animation speed slider
- Real-time statistics panel
  - Visited nodes count
  - Path length count
- Visualized pathfinding algorithms:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Dijkstra’s Algorithm
  - A* Search
- Real-time step-by-step animation
- Automatic path reconstruction
- Color-coded visualization:
  - Start node (Green)
  - End node (Red)
  - Visited nodes (Blue)
  - Final path (Yellow)
  - Walls (Dark Gray)
- Reset functionality

## 🧠 Purpose
This project is built to strengthen understanding of graph algorithms and visualization techniques through an interactive and graphical approach.

It focuses on:
- Algorithm intuition
- Real-time rendering
- Event-driven programming with Pygame

## 🛠 Technologies Used
- Python
- Pygame

## 📦 How To Run
Clone the repository:
```bash
git clone https://github.com/AbhinavSilwal1/pathfinding-visualizer.git
cd pathfinding-visualizer
```

Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the project:
```bash
python3 main.py
```