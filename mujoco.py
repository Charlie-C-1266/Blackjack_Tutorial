import gymnasium as gym

env = gym.make("Hopper-v4", render_mode = "human")

env.render()