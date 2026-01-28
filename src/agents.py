cat > src/agents.py << 'EOF'
class DecisionAgent:
  def __inti__ (self,threshold, agent_id):
    self.agent_id = agent_id
    self.threshold = threshold
    self.belif = 0.5 #neutral
    self.observations = []

  def observe(self, value):
  #receives a noisy observations
  self.observations.append(value)


  def update_belief(self):
  """
  updates belief as the average of the all the observations
  """
    if len(self.observations) == 0:
      return

    self.belief = sum(self.observations)/len(self.observations)


  def decide(self)
  #makes decision based on observation
  if self.belief >= self.threshold
  #else return 0
EOF


