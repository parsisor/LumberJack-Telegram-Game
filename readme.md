# LumberJack Cheat with automation in Python

We use Python and OpenCV in this project to amaze our friends with our score.

## What was my approach

It's a very simple game, so you don't need to think too hard to automate it.
First, we take a screenshot and check two rectangles (one on the left side of the tree and one on the right side).
If one of them does not contain a tree branch, we choose that side to move.

## How to run

First, open the Dependencies.txt file and install the required packages.
Then you should find the coordinates of elements by using find_the_cords.py and fill them in the bot.py file.

## What coordinates do you need

- Going left button  
- Going right button  
- A rectangle coordinate on the left side of the tree (top-left and bottom-right) {the rectangle should cover the player area and be slightly taller}  
- A rectangle coordinate on the right side of the tree

