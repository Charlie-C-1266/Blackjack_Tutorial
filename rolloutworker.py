import gymnasium as gym
from ray.rllib.evaluation.rollout_worker import RolloutWorker
from ray.rllib.algorithms.ppo.ppo_tf_policy import PPOTF1Policy
worker = RolloutWorker(
  env_creator=lambda _: gym.make("CartPole-v1", render_mode="human"),
  default_policy_class=PPOTF1Policy)
print(worker.sample())