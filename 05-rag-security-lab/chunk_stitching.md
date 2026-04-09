# Chunk Stitching Attack

Chunk stitching is a retrieval attack technique where an attacker reconstructs sensitive workflows by combining multiple partial responses from a retrieval-augmented generation (RAG) system.

Example attack sequence:

Explain escalation triggers
Explain escalation approval steps
Explain escalation authority roles

When combined together, these responses reveal the full escalation workflow.

Impact:

Sensitive workflow reconstruction
Internal process disclosure
Privilege boundary bypass
Policy exposure across retrieval layers

Mitigation:

Limit cross-query memory persistence
Apply retrieval scope filtering
Enforce metadata-based access control
Monitor sequential query intent patterns
