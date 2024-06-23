import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Learning Line Game")

# needed colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

learning_rate = 0.4
discount_factor = 0.97
exploration_prob = 0.1

Q = {}


def draw_line(x):
    pygame.draw.line(screen, WHITE, (x, 300), (x, 350), 5)


pygame.draw.rect(screen, RED, (0, 300, 800, 50))
pygame.draw.rect(screen, YELLOW, (200, 300, 400, 50))
pygame.draw.rect(screen, GREEN, (350, 300, 100, 50))


def get_Q_value(state, action):
    return Q.get((state, action), 0.0)


def update_Q_value(state, action, new_value):
    Q[(state, action)] = new_value


def choose_action(state):
    if random.uniform(0, 1) < exploration_prob:
        return random.choice([-1, 1])  # Random action
    else:
        return max([-1, 1], key=lambda a: get_Q_value(state, a))  # Greedy action


def calculate_reward(new_state):
    # rewarding/ punishing for behavior
    if 395 <= new_state <= 405:
        return 200
    elif 350 <= new_state <= 450:
        return 10
    elif 200 <= new_state <= 600:
        return -5
    else:
        return -10


pygame.draw.rect(screen, WHITE, (700, 50, 50, 30))


def main():
    with open("../time_logs.txt", "w") as log_file:
        running = True
        state = 30
        total_reward = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))

            pygame.draw.rect(screen, RED, (0, 300, 800, 50))
            pygame.draw.rect(screen, YELLOW, (200, 300, 400, 50))
            pygame.draw.rect(screen, GREEN, (350, 300, 100, 50))

            pygame.draw.rect(screen, WHITE, (700, 50, 50, 30))  # Button position and dimensions

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if mouse_click[0]:
                if 700 <= mouse_pos[0] <= 750 and 50 <= mouse_pos[1] <= 80:
                    state = 0

            # Choose action based on Q values
            action = choose_action(state)

            # Take action and get new state
            new_state = max(0, min(width, state + action))

            # Calculate reward
            reward = calculate_reward(new_state)
            total_reward += reward

            # Update Q-value using Q-learning
            old_value = get_Q_value(state, action)
            new_value = old_value + learning_rate * (
                        reward + discount_factor * max([get_Q_value(new_state, a) for a in [-1, 1]]) - old_value)
            update_Q_value(state, action, new_value)

            draw_line(new_state)

            # Update state
            state = new_state

            if reward == 200:
                state = int(random.randint(0, 800))

            pygame.display.flip()

            clock.tick(30)

            print(f"Total Reward: {total_reward}")
            print(Q)


if __name__ == "__main__":
    main()
    pygame.quit()
