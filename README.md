# Cellular-Automata

This set of programs creates and simulates scenarios of Cellular Automata, particularly the Game of Life. 

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
