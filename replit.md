# Nehéz Balogij - Animal Species Tracker

## Overview
This is a simple Python CLI (Command Line Interface) application written in Hungarian that collects information about animal species. The program prompts the user to enter 3 different animal species with their names and weights, then displays the collected data.

## Project Details
- **Language**: Python 3.11
- **Type**: Command-line application
- **Original Source**: GitHub import
- **Last Updated**: November 25, 2025

## Recent Changes
- **2025-11-25**: Initial Replit setup
  - Installed Python 3.11 module
  - Fixed code bugs (incorrect instance creation and variable assignment)
  - Added proper .gitignore for Python projects
  - Set up workflow to run the CLI application
  - Converted Windows line endings to Unix format

## Project Structure
```
.
├── nehez_balogij.py    # Main Python script
├── .gitignore          # Python-specific gitignore
└── replit.md           # This documentation file
```

## How It Works
1. The program defines an `Allatfaj` (Animal Species) class with properties for name (`fajnev`) and weight (`tomeg`)
2. It prompts the user 3 times to enter:
   - Animal species name (text input)
   - Animal species weight (numeric input)
3. After collecting all data, it displays all entered animal species with their weights

## Running the Application
The application is configured to run automatically via the "Run Python CLI App" workflow. Simply click the Run button in Replit to start the program.

The program will:
1. Ask for an animal species name ("Add meg egy állatfaj nevét:")
2. Ask for the animal's weight ("Add meg az állatfaj tömegét:")
3. Repeat steps 1-2 two more times
4. Display all three animals with their information

## Code Fixes Applied
The original code had several bugs that were fixed during import:
- Changed from trying to assign attributes to the class itself to properly creating class instances
- Fixed the second prompt to ask for weight instead of name again
- Added proper type conversion for numeric weight input
- Improved output formatting to show animal data clearly
