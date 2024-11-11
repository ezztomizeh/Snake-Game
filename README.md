This Python code implements a classic Snake game using the `pygame` library, providing an interactive and fun gaming experience. The code organizes the game into several key functions:

1. **Game Initialization and Display Setup**: 
   - The game initializes `pygame` and sets up a window of specific dimensions (600x400 pixels). 
   - Colors and fonts are predefined for use in rendering the game elements like the snake, food, score, and messages.

2. **Scoring and Messaging**:
   - The `display_score` function shows the player’s current score at the top of the screen.
   - The `display_message` function displays a game-over message when the snake collides with a boundary or itself, giving the player an option to quit or restart.

3. **Snake and Food Rendering**:
   - The `snake` function iterates over the snake's body segments, drawing each as a rectangle on the screen to represent the moving snake.
   - The food is drawn as a green rectangle at random positions, and the snake grows in length when it "eats" the food (i.e., when the snake’s head overlaps the food position).

4. **Game Logic and Main Loop**:
   - Inside the `game_loop` function, an event loop listens for player input (arrow keys) to control the snake’s direction.
   - The main game loop also manages snake movement, collision detection, food consumption, and screen updates.
   - **Boundary and Self-Collision Detection**: If the snake hits the screen boundary or itself, the game transitions to a "game over" state.
   - **Food Consumption and Growth**: Each time the snake eats food, its length increases, and a new food item appears in a random position.

5. **Game Over State**:
   - When the game ends, the player can press 'Q' to quit or 'C' to restart, controlled through a secondary event loop within `game_loop`.

6. **Clock and Frame Rate**:
   - The frame rate is controlled using `pygame.time.Clock()`, ensuring consistent movement speed, which can be adjusted by changing the `snake_speed` variable.

In summary, this code combines fundamental game development elements like rendering, input handling, and game state management to create a functional and enjoyable Snake game. The code is modular, making it easy to modify or expand with additional features, like varying difficulty levels, sound effects, or enhanced graphics.
