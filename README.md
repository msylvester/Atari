For anyone that is using the new Gymnasium fork in 2023 I have set up Breakout locally on my mac using the following steps:

Create a requirements.txt file with the following dependencies:

 gymnasium[atari, all]

 swig

 Box2D

 box2d-kengz

 pygame

 ale_py

 autorom
Create a python virtual env and install the dependencies by running:

 python3 -m venv .venv

 source .venv/bin/activate

 pip install -r requirements.txt
Run the following to accept the license

 AutoROM --accept-license
If you encounter any timeout issues during this step check out this github issue for some tips.

Run the following python code to launch the environment

 import gymnasium as gym
 import ale_py

 from gymnasium.utils import play

 print('gym:', gym.__version__)

 print('ale_py:', ale_py.__version__)

 env = gym.make("ALE/Breakout-v5", render_mode="rgb_array")

 play.play(env, zoom=3)
press space to start the game and s and d to control it.

Enjoy...!
