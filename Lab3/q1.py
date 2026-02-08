# Task 1
# A company’s security system consists of nine critical components (A through I). Each component can be either safe or vulnerable due to security flaws. A security agent is
# responsible for scanning the entire system, identifying vulnerabilities, and patching them to prevent attacks.
# You are tasked with simulating a cybersecurity exercise using the given environment and agent. Complete the following steps:

# Initial System Check: The system environment is initialized with random vulnerabilities. Display the initial state of the system, showing which components are safe and which are vulnerable.
import random

class Environment:
    def __init__(self):   # initialize all components with random safe or vulnerable states
        self.components = {
            'A': random.choice(['Safe', 'Vulnerable']),
            'B': random.choice(['Safe', 'Vulnerable']),
            'C': random.choice(['Safe', 'Vulnerable']),
            'D': random.choice(['Safe', 'Vulnerable']),
            'E': random.choice(['Safe', 'Vulnerable']),
            'F': random.choice(['Safe', 'Vulnerable']),
            'G': random.choice(['Safe', 'Vulnerable']),
            'H': random.choice(['Safe', 'Vulnerable']),
            'I': random.choice(['Safe', 'Vulnerable'])
        }

    def displayInitalState(self):   # display the initial state of each component    
        for comp, status in self.components.items():
            print(f"Component: {comp} | Status: {status}")
    
    def get_percept(self, component):  # return the current state of a component as a percept
        return self.components[component]
            
    def patch(self, component):  # patch the vulnerable component and mark it as safe
        self.components[component] = 'Safe'
        
class SimpleReflexAgent:
    def __init__(self):
        self.to_patch = []
    
    # System Scan: The security agent scans each component. If a component is vulnerable, the agent logs a warning and adds it to a list for patching. If it is secure, a success message is logged.

    def act(self, percept, component, environment): # take action based on the percept of the component
        if percept == 'Vulnerable':
            environment.patch(component)
            return f"WARNING: Component {component} was vulnerable → patched."
        else:
            return f"SUCCESS: Component {component} is already safe."

    # Patching Vulnerabilities: After the scan, the agent patches all vulnerable components, marking them as safe. Display messages indicating which components have been patched.

    def patch_vulnerabilities(self, environment):  # patch all components stored in the vulnerable list
        print("\nPatching Vulnerabilities...")
        for comp in self.to_patch:
            environment.patch(comp)
            print(f"Component {comp} patched successfully")
    
# Final System Check: Display the system’s final state, confirming that all vulnerabilities have been patched.

def run_agent(agent, environment):
    print("Initial System State:")
    for comp, state in environment.components.items():
        print(f"Component {comp}: {state}")

    print("\nSystem Scan & Actions:")
    for component in environment.components:
        percept = environment.get_percept(component)
        action = agent.act(percept, component, environment)
        print(action)

    print("\nFinal System State:")
    for comp, state in environment.components.items():
        print(f"Component {comp}: {state}")


agent = SimpleReflexAgent()
environment = Environment()

run_agent(agent, environment)
