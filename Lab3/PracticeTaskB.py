# Practice Task Part B
import random

# B. Modify the code to make the environment’s state change randomly after each step. The state should switch between 'Dirty' and 'Clean' after each iteration of
# the loop or after the agent performs an action. This will simulate a dynamic environment where the state is unpredictable throughout the agent’s execution.

class Environment:
    def __init__(self):
        self.percept = random.choice(['Dirty', 'Clean'])     # initial state of the environment ('Dirty' or 'Clean') is randomly set 
    
    def getPercept(self):                                 
        return self.percept
    
    def changeStateAfterEachtep(self):
        self.percept = random.choice(['Dirty', 'Clean'])     # state should switch between 'Dirty' and 'Clean' after each iteration
        return

class Agent:     # Simple Reflex AI Agent
    def __init__(self):
        pass
    
    def act(self, percept):         # Determine action based on the initial percept. (the percept argument)
        if (percept == 'Dirty'):    # If percept = Dirty, Clean the room
            return "Clean"
        else:
            return "Room Already Clean"

def run_agent(agent, environment, steps):         # The agent reacts to the initial stimuli
    for step in range(steps):
        percept = environment.getPercept()              # Get the perception from Environment
        action = agent.act(percept)                     # What action to be done based upon the perception
        print(f"Step: {step + 1} Percept: {percept}, Action: {action}")  # Action 
        environment.changeStateAfterEachtep()
            

# MAIN SECTIONS
agent = Agent()
environment = Environment()
run_agent(agent, environment, 5)
