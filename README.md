Learning Line Game
Overview
This project demonstrates a simple Q-learning algorithm where an AI agent, represented as a line, learns to navigate towards a designated green area in the middle of the screen. Initially, the agent takes random actions, but over time, it learns to make precise decisions to reach the green area more efficiently.

How It Works
Initialization:

The display is set up with a line controlled by the AI.
The screen is divided into three colored areas: red, yellow, and green.
Color Zones:

Red Area: Represents negative points.
Yellow Area: Represents moderate negative points.
Green Area: Represents positive points.
Exact Middle of the Green Area: Represents a high positive reward.
Rewards and Penalties:

The AI receives rewards or penalties based on its position:
Red Area: -10 points
Yellow Area: -5 points
Green Area: 10 point
Exact Middle (395 <= x <= 405): +200 points
The goal of the AI is to maximize its total reward by learning to move towards the green area, specifically the exact middle.
Learning Process:

Exploration vs. Exploitation: Initially, the AI takes random actions to explore the environment. Over time, it uses its learned Q-values to make more informed decisions.
Q-learning Algorithm:
The AI updates its Q-values based on the reward received and the expected future rewards.
This helps the AI to learn which actions lead to the highest rewards.
Reinforcement: Each time the AI reaches the exact middle, it is teleported to a random position to continue learning.
Performance Improvement:

At first, it may take the AI a few seconds to reach the middle as it explores and learns the environment.
After a few minutes of training, the AI learns to reach the middle in about 10 seconds or less, making precise decisions based on the learned Q-values.
Execution
To run the game, execute the script. The AI will start navigating the screen, learning to reach the green area efficiently over time.
Observe the AI's improvement as it learns from its actions and the rewards received.
