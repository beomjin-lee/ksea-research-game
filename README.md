# KSEA - Game AIs

## Authors
Beom Jin Lee < beomjin.lee@berkeley.edu >, Gabi Choi < gabichoi96@gmail.com >, Brian Yoo < brianyoo@berkeley.edu >, Wonwoo Choi < wonwoo9762@berkeley.edu >, Sabin Kim < kbk6881@berkeley.edu >, Paul Lim < keonwoolim@berkeley.edu >, Hae Young Jang < h_jang@berkeley.edu >

## Introduction
This project is Made by KSEA Project Research and SW Team 2018 at UC Berkeley.

We have built games for Tic-Tac-Toe and Tetris, both of which can be found in their respective directories. In addition, we built AIs for the games, one utilizing classic Mini/Expecti-Max algorithm and the other using genetic algorithm.

## Dependencies
The following packages should be installed prior to running the files:

1. Numpy
2. PyGame
3. Copy

Please note that we have used Python 2 (> 2.7) and Python 3 (> 3.6), and will not guarantee that the files will run for versions of Python other than them. If you choose to use Python 2, please add:

`from __future__ import division`

prior to running the files.

## Running Files
First, clone into the git repository:

`git clone git@github.com:beomjin-lee/ksea-research-game.git`

*Note: If this does not work, try `git clone https://github.com/beomjin-lee/ksea-research-game.git`*

Then, change directories into the cloned by using `cd`, and for tetris, `cd tetris` then run either:

1. `python tetris_player.py` for playing tetris
2. `python tetris_ai.py` for tetris AI

The project is still ongoing, and we may incur some significant changes to the programs. If so, please feel free to, instead of attempting to resolve merge conflicts, either re-clone or run:

`git fetch --all`

Followed by:

`git reset --hard origin/master`
