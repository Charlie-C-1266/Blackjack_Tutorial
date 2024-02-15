import gymnasium
import random


env = gymnasium.make("CarRacing-v2", render_mode = "human")

episodes = 10

for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0
    
    while not done:
        action = random.choice([0,1, 2])
        result= env.step(action)
        #print(result)
        obs, reward, done, _, _ = result
        
        #print(done) 
        #print(f"Returned item was: {result}")
        score += reward
        env.render()

        
    print(f"Episode: {episode}, Score: {score}")
    
env.close()
    
