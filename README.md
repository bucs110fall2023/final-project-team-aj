[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803286&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# PING PADDLES
## CS110 Final Project  First Semester, 2023

## Team Members

Aaron Damsky and Joseph Kesler

***

## Project Description

Our program is a game that replicates the classic arcade game, Pong, where two players play against each other hitting a ball back and forth with paddles. The goal is to try and get the ball past the other teams paddle.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Home Screen(s)
2. Game Screen (including score)
3. Paddles
4. Ball
5. Obstacles
6. Game Over Screen

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

Test Case 1: Paddle Movement

Test Description: Verify that the paddles move left and right as expected.

Test Steps:
Run the program.
Press Space Bar to open the game.
Push the right arrow key.
Verify the bottom paddle moves to the right.
Push the left arrow key.
Verify the bottom paddle moves to the left.
Push the "d" key.
Verify the top paddle moves to the right.
Push the "a" key.
Verify the top paddle moves to the left.

Expected Outcome: The paddles should move left and right in response to the keyboard key inputs.


Test Case 2: Ball Movement

Test Description: Verify that the ball initially moves correctly on the screen.

Test Steps:
Run the program.
Press Space Bar to open the game.
Press Space Bar to begin the game.
Do not touch the right arrow key, the left arrow key, the "d" key, or the "a" key.
Verify that the ball moves on the screen up and down.

Expected Outcome: When the space bar is initially pressed, the ball should move up and down as it bounces between the stationary paddles. 


Test Case 3: Paddle Collisions

Test Description: Verify that the ball bounces off of the paddles as expected.

Test Steps:
Run the program.
Press Space Bar to open the game.
Press Space Bar to begin the game.
Move the first paddle so that the ball bounces off the side of the paddle.
Verify that the ball bounces off of the paddle at an angle depending on where the ball hits the paddle.
Move the other paddle so that the ball bounces off the side of this paddle.
Verify that the ball bounces off of the paddle at an angle depending on where the ball hits this paddle. 

Expected Outcome: When the ball bounces off of each paddle, it should bounce off at an angle depending on where the ball hits the paddle. The closer to the edge of the paddle, the greater the angle the ball bounces off. 


Test Case 4: Wall Collisions

Test Description: Verify that the ball bounces off of the walls as expected. 

Test Steps:
Run the program.
Press Space Bar to open the game.
Press Space Bar to begin the game.
Let the ball bounce off of the side of the first paddle.
Let the ball move across the screen.
Verify that the ball bounces off of both side walls.

Expected Outcome: When the ball hits one of the side walls, it should bounce off the wall at the same angle in the opposite direction.


Test Case 5: Obstacle Collisions

Test Description: Verify that the ball bounces off of the triangles appropriately.

Test Steps:
Run the program.
Press Space Bar to open the game.
Press the "1" key.
Verify that the ball bounces off of the bottom triangle.
Exit the program.
Rerun the program.
Press Space Bar to begin.
Press the "2" key.
Verify that the ball bounces off of the top triangle.

Expected Outcome: The ball should bounce off of the triangles throughout the duration of the game depending on where and at what angle the ball hits the triangle.


Test Case 6: Score

Test Description: Ensure all of the appropriate changes occur when a goal is scored.

Test Steps:
Run the program.
Press Space Bar to open the game.
Press Space Bar to begin the game.
Allow the ball to pass one of the paddles.
Verify that opposite player's score increases by one.
Verify that the ball resets to the middle of the screen, like it was at the beginning of the game.
Press Space Bar to resume the game.
Allow the ball to pass the other paddle.
Verify that the opposite player's score increases by one.
Verify that the ball resets to the middle of the screen, like it was at the beginning of the game.

Expected Outcome: When the ball passes a paddle, the opposite player's score increases by one, and the ball resets to the middle of the screen, like it was at the beginning of the game.


Test Case 7: Game Over

Test Description: Confirm that the screen changes to the end screen when one of the players reaches 7 goals.

Test Steps:
Run the program.
Press Space Bar to open the game.
Press Space Bar to begin the game.
Play until one of the players reaches 7 points.
Verify that the end screen pops up stating which player won the game as well as the final score.

Expected Outcome: When one of the players reaches 7 points, the end screen pops up stating which player won the game as well as the final score.
