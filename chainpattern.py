class SupportHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handler_request(self, issue):
        if self.successor:
            return self.successor.handler_request(issue)
        else:
            return "No one available to handle the issue"


class AgentHandler(SupportHandler):
    def handler_request(self, issue):
        if issue["severity"].lower() == "low":
            return f"Agent handling request: {issue['description']}"
        else:
            return super().handler_request(issue)


class TeamLeadHandler(SupportHandler):
    def handler_request(self, issue):
        if issue["severity"].lower() == "medium":
            return f"Team Lead handled issue: {issue['description']}"
        else:
            return super().handler_request(issue)


class ManagerHandler(SupportHandler):
    def handler_request(self, issue):
        if issue["severity"].lower() == "high":
            return f"Manager handled issue: {issue['description']}"
        else:
            return super().handler_request(issue)


# Setting up the chain
manager = ManagerHandler()
team_lead = TeamLeadHandler(successor=manager)
agent = AgentHandler(successor=team_lead)

# Issues
issues = [
    {"description": "password reset request", "severity": "low"},
    {"description": "system not responding", "severity": "medium"},
    {"description": "Data breach detected", "severity": "high"},
]

for issue in issues:
    print(agent.handler_request(issue))
