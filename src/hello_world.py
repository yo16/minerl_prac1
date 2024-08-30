# https://minerl.readthedocs.io/en/latest/tutorials/first_agent.html
# https://colab.research.google.com/drive/1rJ3lGy-bG7kJRe_wYBWg7fjSaD9oOMDw?usp=sharing#scrollTo=n3FGwWZ489mT

import gym
import minerl
from collections import OrderedDict
import time

def main():
    print("main")

    env = gym.make('MineRLBasaltFindCave-v0')
    obs = env.reset()

    # take actions through the environment until time runs out or the agent dies.
    done = False
    #while not done:
    #    # Take a random action
    #    action = env.action_space.sample()
    #    # In BASALT environments, sending ESC action will end the episode
    #    # Lets not do that
    #    action["ESC"] = 0
    #    obs, reward, done, _ = env.step(action)
    #    env.render()
    # Take a random action
    #action = env.action_space.sample()
    #print(action)
#    for _ in range(100):
#        print("---------")
#        time.sleep(0.2)
#
#        ac = env.action_space.noop()
#        ac["camera"] = [0, + 7]
# 
#        obs, reward, done, _ = env.step(ac)
#        env.render()
    
    action_step(env, {})
    #action_step(env, dict(inventory=[1]), sleep_time=1.0)
    #action_step(env, dict(camera=[0, +30]), sleep_time=1.0)
    #action_step(env, dict(camera=[-10, -30]), sleep_time=1.0)
    #action_step(env, dict(camera=[+10, 0]), sleep_time=1.0)
    #action_step(env, dict(inventory=[1]), sleep_time=1.0)  # Put inventory away? = Yes, if it is showing

    action_step_calibrate(env, 0, 0) 
    for x_off in [+0.62, +1.61, +3.22, +5.81, +10.0]:
        print(f"x_off={x_off}")
        action_step_calibrate(env, x_off,0) 
        action_step_calibrate(env, -x_off,0) 
    for y_off in [+0.62, +1.61, +3.22, +5.81, +10.0]:
        print(f"y_off={y_off}")
        action_step_calibrate(env, 0, y_off) 
        action_step_calibrate(env, 0, -y_off) 

    #ac["ESC"] = [1]
    #obs, reward, done, _ = env.step(ac)
    action_step(env, dict(ESC=[1]))
        

    # In BASALT environments, sending ESC action will end the episode
    # Lets not do that
    #action["ESC"] = 0
    #obs, reward, done, _ = env.step(action)
    #print(obs)
    #print(reward)
    #print(done)

    #env.render()

    return 1

def action_step(env, action, sleep_time=0.2):
    print("-----")
    time.sleep(sleep_time)
    ac = env.action_space.no_op()
    ac.update(action)
    obs, reward, done, info = env.step(ac)
    env.render()


def action_step_calibrate(env, x_off,y_off):
    time.sleep(1.0)
    ac = env.action_space.no_op()
    ac.update(dict(camera=[y_off, x_off]))
    obs, reward, done, info = env.step(ac)

    #im = obs["pov"][100:250, 200:400,:]
    #cv2_imshow(cv2.cvtColor(im, cv2.COLOR_RGB2BGR))
    env.render()

    time.sleep(1.0)
    ac = env.action_space.noop()
    ac.update(dict(camera=[-y_off, -x_off]))  # Move back
    obs, reward, done, info = env.step(ac)


if __name__=='__main__':
    main()
