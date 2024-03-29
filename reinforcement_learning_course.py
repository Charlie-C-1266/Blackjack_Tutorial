import os
import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

env= gym.make("CartPole-v1", render_mode = "human")

episodes = 5

for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        (n_state, reward, done, info, _) = env.step(action)
        score += reward

    print(f"Episode: {episode}, Score: {score}")
env.close()







# if __name__ == "__main__":
#     print("Hello world!")