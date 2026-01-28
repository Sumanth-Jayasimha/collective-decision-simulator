cat > experiments/baseline.py << 'EOF'
from src.agents import DecisionAgent

agent = DecisionAgent(agent_id=1, threshold=0.6)

observations = [0.55, 0.62, 0.58, 0.65]

for obs in observations:
    agent.observe(obs)
    agent.update_belief()
    print(f"Belief: {agent.belief:.3f}, Decision: {agent.decide()}")

print("Baseline experiment running")
EOF
