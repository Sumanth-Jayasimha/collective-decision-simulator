cat > src/agents.py << 'EOF'
class DecisionAgent:
    def __init__(self, agent_id, threshold):
        self.agent_id = agent_id
        self.threshold = threshold
        self.belief = 0.5  # neutral initial belief
        self.observations = []

    def observe(self, value):
        """
        Receive a noisy observation
        """
        self.observations.append(value)

    def update_belief(self):
        """
        Update belief as the mean of observations
        """
        if len(self.observations) == 0:
            return

        self.belief = sum(self.observations) / len(self.observations)

    def decide(self):
        """
        Make a binary decision based on threshold
        """
        return self.belief >= self.threshold
EOF
