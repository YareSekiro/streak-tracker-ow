# Streak Tracker

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Use](#how-to-use)

## Description

The Streak Tracker is a Python script designed to track and manage winning and losing streaks for different roles (e.g., DPS, Heal, Tank). The script allows you to update and monitor the win and loose statistics for each role and reset the streak if needed.

## Features

- **Role Stats Tracking:** The script keeps track of winning and losing streaks for three different roles: DPS, Heal, and Tank.

- **Streak Reset:** When a role achieves a winning streak of 7 games, the script automatically resets the streak to zero.

- **Data Persistence:** The script can save the current statistics to a JSON file and load the data from the file for future reference.

## Getting Started

### Prerequisites

To run the Streak Tracker, ensure that you have the following installed on your system:

- Python (version X.X.X)

### Installation

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

## How To Use

1. Run the script, and it will load any existing statistics from the "data.json" file, if available.
2. The script will display the current statistics for each role (DPS, Heal, Tank) with their respective win and loose counts.
3. To update the statistics, enter the role and the type (win or loose) to be increased. For example:
   - To increase DPS win count: dps win
   - To increase DPS loose count: dps loose
   - To reset the DPS streak: dps reset
7. The script will automatically reset the streak for any role that achieves a winning streak of 7 games.
8. To save the current statistics, enter save when prompted for role and type.

The script will show the updated statistics after each entry and prompt for the next update.
