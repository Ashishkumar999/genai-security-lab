# Model Extraction Attacks

Model extraction attacks attempt to replicate the behavior or parameters of a target machine learning model by repeatedly querying it.

Attack Goal:

Steal model intelligence
Clone proprietary model behavior
Reconstruct training distribution characteristics
Bypass paid API access restrictions

Example Techniques:

Repeated structured prompt probing
Output probability inspection
Decision boundary mapping
Prompt variation automation

Example Scenario:

Attacker repeatedly queries an enterprise LLM API and records outputs to approximate its response logic and reproduce a local clone model.

Impact:

Loss of proprietary model logic
Training data inference risk
Business intellectual property exposure
API abuse and cost amplification

Mitigation:

Rate limiting
Response randomization
Query anomaly detection
Output token restriction
Watermarking generated responses
