# Social Media Multi-Agent System

A sophisticated multi-agent system for content creation, optimization, and posting across social media platforms with built-in safety checks and engagement optimization.

## Project Structure

```
social-media-multi-agent/
├── app.py                      # Streamlit entry point
├── agents/                      # Individual agent modules
│   ├── content_creator.py      # Content generation
│   ├── platform_adapter.py     # Platform-specific adaptation
│   ├── trend_agent.py          # Trend analysis and incorporation
│   ├── engagement_agent.py     # Engagement optimization
│   ├── safety_policy_agent.py  # Policy compliance checks
│   ├── context_sarcasm_agent.py # Context and sarcasm detection
│   └── decision_agent.py       # Final posting decisions
├── crew/                        # CrewAI orchestration
│   └── crew_setup.py           # Agent workflow configuration
├── memory/                      # Learning and history
│   └── refused_posts.json      # Log of refused posts
├── utils/                       # Utility modules
│   ├── scoring.py              # Engagement and risk scoring
│   ├── thresholds.py           # Platform rules and thresholds
│   └── helpers.py              # Common helper functions
├── workflows/                   # External workflow definitions
│   └── n8n_flow.json          # Optional n8n integration
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Agents

### Content Creator Agent
Generates engaging social media content based on topics and user preferences.

### Platform Adapter Agent
Adapts content to be optimized for specific social media platforms (Twitter, Instagram, LinkedIn, etc.).

### Trend Agent
Identifies current trending topics and incorporates them into content.

### Engagement Agent
Scores and optimizes content for maximum user engagement.

### Safety Policy Agent
Ensures all content complies with platform safety guidelines and policies.

### Context Sarcasm Agent
Detects and properly handles sarcasm, irony, and contextual nuances in content.

### Decision Agent
Makes final decisions about whether and when to post content.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## Features

- Multi-agent orchestration using CrewAI
- Content optimization for engagement
- Platform-specific adaptation
- Safety and policy compliance checking
- Trend analysis and incorporation
- Learning from refused posts
- Configurable thresholds and rules

## Configuration

Edit `utils/thresholds.py` to customize:
- Platform-specific rules
- Safety thresholds
- Posting limits

## Memory and Learning

The system maintains a log of refused posts in `memory/refused_posts.json` to learn from policy violations and improve content generation.

## License

Specify your license here
