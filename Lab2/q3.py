# question 3: You are designing an AI system to automatically respond to cybersecurity threats. There are different types of response agents: AlertAgent, BlockAgent, and RecoverAgent. 
# All agents have a method execute_response(), but each performs a different action—AlertAgent sends notifications, BlockAgent blocks malicious activities, and RecoverAgent restores affected systems. 
# Your task is to create a base class ResponseAgent with a generic execute_response() method, override it in each derived class, and then demonstrate polymorphism by calling execute_response() on a list of mixed agent objects.

class ResponseAgent:  # base class
    def execute_response(self):  # method that is overriden in child classes
        print("Base Class: Response Agent.")

class AlertAgent(ResponseAgent):  # child class
    def execute_response(self):   # overriding method of base class
        print("Alert Agent: Sending Notifications.")

class BlockAgent(ResponseAgent):  # child class
    def execute_response(self):   # overriding method of base class
        print("Block Agent: Blocking Malacious Activities.")

class RecoverAgent(ResponseAgent):  # child class
    def execute_response(self):     # overriding method of base class
        print("Recover Agent: Restoring affected systems.")


RA = ResponseAgent()
RA.execute_response()

AA = AlertAgent()
AA.execute_response()

BA = BlockAgent()
BA.execute_response()

RecA = RecoverAgent()
RecA.execute_response()
