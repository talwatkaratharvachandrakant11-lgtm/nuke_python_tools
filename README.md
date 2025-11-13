# Nuke Python Scripting Assignment

## Overview
This repository contains Python scripts for automating common tasks in Foundry Nuke through custom menu items and tools.

## Tools Implemented

### 1. Custom Write Node
- **Location:** Nodes → Custom → Custom Write Node
- **Function:** Creates a Write node with a pre-defined output path based on shot metadata
- **Path Format:** `/path/to/project/sequences/{sequence}/{shot}/{version}/render/{shot}.####.exr`

### 2. Split EXR
- **Location:** Utilities → Split EXR
- **Function:** Splits a multi-channel EXR into individual Shuffle nodes for each layer
- **Requirements:** Select a Read node with EXR file first

### 3. Cleanup Script
- **Location:** Utilities → Cleanup Script
- **Function:** 
  - Removes unnecessary nodes (NoOp, Viewer, Backdrop)
  - Deletes nodes with errors
  - Disables unused branches
  - Optimizes node graph performance

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/nuke-python-assignment.git