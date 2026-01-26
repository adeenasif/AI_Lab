# question 1: You are developing a simple AI-powered cybersecurity system to manage different types of security agents. All agents share common attributes like agent_id, name, and status, but each type has its own specialized role. 
# For example, FirewallAgent monitors network traffic,  MalwareDetectionAgent scans files for threats, and AutomationAgent performs routine AI-based tasks to optimize system security.  
# Your task is to create a base class SecurityAgent and derive classes for each agent type, implementing type-specific methods like monitor_traffic(), scan_files(), or run_automation(). 
# Create objects  for each agent type and call their methods to simulate how a cybersecurity system can automatically respond to threats using AI automation.

class SecurityAgent:
    def __init__(self, agent_id, name, status):
        self.agent_id = agent_id
        self.name = name
        self.status = status

class FireWallAgent(SecurityAgent):
    def monitor_traffic(self):
        print("Firewall Agent -> ID:", self.agent_id, ", Name: ", self.name, ", Status:", self.status, "is monitoring traffic.")

class MalwareDetection(SecurityAgent):
    def scan_files(self):
        print("Malware Detection Agent -> ID:", self.agent_id, ", Name: ", self.name, ", Status:", self.status, "is scanning files.")

class AutomationAgent(SecurityAgent):
    def run_automation(self):
        print("Automation Agent -> ID:", self.agent_id, ", Name: ", self.name, ", Status:", self.status, "is running automation.")

FA = FireWallAgent(7923, "Sameul", 'On Duty')
FA.monitor_traffic()
MDA = MalwareDetection(7719, "Jack", 'On Duty')
MDA.scan_files()
AA = AutomationAgent(7512, "Cygnus", 'On Duty')
AA.run_automation()
