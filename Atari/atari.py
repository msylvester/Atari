import gymnasium as gym
import ale_py

from gymnasium.utils import play

print('gym:', gym.__version__)

print('ale_py:', ale_py.__version__)

# env = gym.make("ALE/Breakout-v5", render_mode="rgb_array")
env = gym.make("ALE/Krull-v5", render_mode="rgb_array")

play.play(env, zoom=3)