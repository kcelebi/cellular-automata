# Cellular-Automata 🔬
[![celebi-pkg](https://circleci.com/gh/kcelebi/cellular-automata.svg?style=svg)](https://circleci.com/gh/kcelebi/cellular-automata)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![](https://user-images.githubusercontent.com/35543500/111094823-74c67200-8512-11eb-912b-8e90c0995334.mp4)

This purpose of this project is to test different research ideas for cellular automata. This is in the form of hypotheses, demos, simulations, and unstructured trial/error. Some of these hypotheses are:

- How can we detect the self-producing cycles?
- How can we detect moving cycles? (mobiles)
- Can a Reinforcement Learning Agent interact with a CA environment to create a desired state?

## How to Use

You can utilize these functions and programs by cloning/forking this repository. Depending on future development, the structure of this project might change into a Python package available on PyPI. 

Clone/fork the repository to your local. Obtain the requirements:

    python -m pip install -r requirements.txt

Each stage of an automata simulation involves a `state`. You need to be able to initialize a state, update it, and view/analyze it. To initialize a state, either generate a random one or input it manually (as a 2d numpy or vanilla Python array):

    import src.automata as atm      # contains functions to affect states
    import src.analysis as ans      # contains functions to analyze states
    from src.rules import Rules     # contains the different rule-sets
    
    state = atm.get_random_state(shape = (5, 4)) # generates a 5 x 4 frame
    
    new_state = atm.update(state, rule = Rules.CONWAY) # updates using Conway's Game of Life rules

    ans.plot_state(new_state) # returns plt.imshow() of the provided state
    ans.display_state(new_state) # prints the state to CLI as ASCII

You can also play through multiple steps which are outputted as a 3D numpy array. Let's play through 15 steps:

    states = ans.play(state, steps = 15, rules = Rules.CONWAY)
    print(states.shape)     # outputs: (15, 5, 4)

Want to analyze this simulation?

    survival_stats = ans.get_survival_stats(states)
    
    plt.plot(survival_stats / (state.shape[0] * state.shape[1]))
    plt.title('Survival Rate')
    plt.xlabel('Time')
    plt.ylabel('Pct Alive')
    plt.show()

If you want to design your own rules, you can contribute to the `rules.py` module or write a custom function to pass through to `atm.update()` or `ans.play()`. The provided rule-set is to be applied to each cell in the grid and considers the value of eligible neighbors and itself. As a lambda, your function should be of the form:

    my_rule = lambda neighbors, curr_cell, state: ...   # your calculation

## Contributing

Please feel free to fork and submit a PR. For other queries, I can be reached at my email: kayacelebi17@gmail.com

## Release Notes

* Conway's Game of Life Interactive

    I am currently in the process of implementing an interactive demonstration where one can draw different pre-set patterns to a Game of Life simulation. The goal of this is to allow the user the ease of making new patterns, observing simulations of natural phenomena, or discovering new features.

    View the interactive cellular automata demonstration [here](https://kcelebi.github.io/cellular-automata/visualize/inter.html)

* Cellular Automata Dataset

    Conway's Game of Life is not the only set of rules for Cellular Automata. I want to bridge some of my focus to other rules, such as rule 30, and perhaps create a dataset for the purpose of analyzing the different patterns that appear. This project is still in the planning stages
