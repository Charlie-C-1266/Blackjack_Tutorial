# Configure.
from ray.rllib.algorithms.ppo import PPOConfig
import gymnasium

env = gymnasium.make("CartPole-v1", render_mode = "human")

config = PPOConfig().environment(env="CartPole-v1").training(train_batch_size=4000)

# Build.
algo = config.build()

# Train.
print(algo.train())