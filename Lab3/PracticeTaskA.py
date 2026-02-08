# Practice Task Part A
import random

# A. Modify the code so that the initial state of the environment ('Dirty' or 'Clean') is randomly set when the program starts. The state should be chosen at the beginning of the program and should vary each time it runs.

class Environment:
    def __init__(self):
        self.percept = random.choice(['Dirty', 'Clean'])  # initial state of the environment ('Dirty' or 'Clean') is randomly set 
    
    def getPercept(self):  
        return self.percept

class Agent:            # Simple Reflex AI Agent
    def __init__(self):
        pass
    
    def act(self, percept):       
        if (percept == 'Dirty'):    # If percept is Dirty, Clean it
            return "Clean"
        else:
            return "Room Already Clean"
        
def run_agent(agent, environment, steps):         
    for step in range(steps):
        percept = environment.getPercept()              
        action = agent.act(percept)                     
        print(f"Step: {step + 1} Percept: {percept}, Action: {action}")  
            
agent = Agent()
environment = Environment()
run_agent(agent, environment, 5)
