# Cellular-Automata 🔬

This set of programs creates and simulates scenarios of Cellular Automata, particularly the Game of Life. 

* Conway's Game of Life Interactive

    I am currently in the process of implementing an interactive demonstration where one can draw different pre-set patterns to a Game of Life simulation. The goal of this is to allow the user the ease of making new patterns, observing simulations of natural phenomena, or discovering new features.

* Cellular Automata Dataset

    Conway's Game of Life is not the only set of rules for Cellular Automata. I want to bridge some of my focus to other rules, such as rule 30, and perhaps create a dataset for the purpose of analyzing the different patterns that appear. This project is still in the planning stage, but expect updates by December 2020. 

## automata.html

This program is a JavaScript file that runs the Game of Life scenario. It can be simply double-clicked to open in a browser.

## testfiles/automata_brute.py

This program generates various Game of Life scenarios and stores them into .txt files. It subsequently runs a Processing file that displays the simulation. It effectively does the same thing as automata_brute.html, however, in a different medium.

## automata_preset_maker.py

This file creates the scenarios in the ``scenarios`` folder that can then be run in the Processing file located in the ``automata`` folder.

### automata

This is a processing file that, more or less, does the same thing as ``automata.html``. It uses the scenarios located in the ``scenarios`` folder to simulate.

### testfiles
The remaining files in this folder serve as helper programs, mostly filled with functions and junk. Feel free to completely ignore them.
