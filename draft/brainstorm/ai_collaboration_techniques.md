# Brainstorm: Advanced AI Collaboration Techniques
**Date**: 2026-07-18  
**Goal**: Go beyond simple prompting. Document methods that demonstrate "AI as engineering copilot".

## Promising Approaches

### 1. Multi-Agent Role Play (in single session)
Prompt the model to role-play as:
- Chief Engineer (conservative)
- Propulsion lead (optimistic)
- Structures skeptic
- Cost accountant
Then force them to debate a decision.

### 2. "Red Team" + "Blue Team"
- Blue: Propose best version of current design
- Red: Attack it with worst-case assumptions and historical failure modes

### 3. Generative Design Mutation
Use LLM to generate new design vectors or architecture descriptions, then feed those into an evolutionary algorithm.

### 4. Explainable Decision Extraction
After analysis, ask AI:
"Given these results, write a one-paragraph justification suitable for a technical review that a skeptical professor would accept."

### 5. Prompt Chaining for Uncertainty
Chain:
1. "List all assumptions in this calculation"
2. "For each assumption, assign uncertainty range and distribution"
3. "Now run a qualitative Monte Carlo in text form"

### 6. Historical Failure Injection
"List 5 historical reusable vehicle failures or near-misses related to [topic]. How would you redesign to avoid them?"

## Logging Standard
Every AI session should record:
- Roles assigned
- Temperature / creativity setting (if controllable)
- Whether we accepted / rejected outputs
- How it changed the design

**Stretch Goal for Project**: Produce a short "AI Engineering Copilot Best Practices" appendix.
