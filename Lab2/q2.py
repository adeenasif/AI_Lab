# question 2: You are building an AI-based threat intelligence system that tracks different types of cybersecurity threats. All threats share common attributes like threat_id, name, and severity. 
# Derived classes include PhishingThreat (monitors emails), RansomwareThreat (monitors file systems), and BotnetThreat (monitors network traffic).
# Each class has specific methods such as analyze_email(), scan_files(),  or detect_traffic(). Your task is to create the base and derived classes, instantiate objects, and call their methods to simulate an automated threat response system.

class Threat:
    def __init__(self, threat_id, name, severity):
        self.threat_id = threat_id
        self.name = name
        self.severity = severity

class PhishingThreat(Threat):
    def analyze_email(self):
        print("Phishing Threat -> ID:", self.threat_id, ", Name: ", self.name, ", Status:", self.severity, "is monitoring emails.")

class RansomwareThreat(Threat):
    def scan_files(self):
        print("Ransomware Threat -> ID:", self.threat_id, ", Name: ", self.name, ", Status:", self.severity, "is scanning files.")

class BotnetThreat(Threat):
    def detect_traffic(self):
        print("Botnet Threat -> ID:", self.threat_id, ", Name: ", self.name, ", Status:", self.severity, "is monitoring network traffic")

PT = PhishingThreat(7923, "Sameul", 'On Duty')
PT.analyze_email()
RT = RansomwareThreat(7719, "Jack", 'On Duty')
RT.scan_files()
BT = BotnetThreat(7512, "Cygnus", 'On Duty')
BT.detect_traffic()
