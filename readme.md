# FlappyBirdAI

FlappyBirdAI is a python implementation using pygame from tutorials of [The Coding Train](https://www.youtube.com/c/TheCodingTrain) implementing [NEAT algorithm using p5.js](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6Yd3975YwxrR0x40XGJ_KGO) 

<p align='center'>
    <img src="./Resources/flappy_bird_ai.gif">
</p>

# Setup

If you want to give it a try you can clone the project 

```
      git clone git@github.com:indiVar0508/FappyBirdAI.git
```

Install the requirements into your Python virtual environment, make sure you are in `FlappyBirdAI` directory

```
    python3 -m venv venv # create virtual environment
    source venv/bin/activate # activate virtual environment in terminal
    pip install -r requirements.txt
```

# How to Play

If you want to run the game once your virtual environment is setup, you can simply run main.py file to intialize the prompt to start the game.

```
            python main.py
```

The prompt will give options to either play yourself where you can press `S` to play yourself, use `Space bar` as a signal to let bird jump in screen. if you want to see how ai Evolves using NeuroEvolution algorithm press `A` to let AI play the game and you can watch AI play the game.
