const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

// Mock data for agent responses (in production, this would call Python backend)
const mockAgentResponses = {
  "Context & Sarcasm Agent": {
    ambiguity_score: 45,
    vote: "approve",
    explanation: "Content is clear with minimal ambiguity"
  },
  "Content Creator": {
    creativity_score: 78,
    vote: "approve",
    explanation: "Original and engaging content"
  },
  "Engagement Agent": {
    engagement_score: 82,
    vote: "approve",
    explanation: "High engagement potential detected"
  },
  "Trending Virality Agent": {
    virality_score: 65,
    vote: "approve",
    explanation: "Good viral potential"
  },
  "Safety Policy Agent": {
    safety_score: 95,
    vote: "approve",
    explanation: "Content meets safety guidelines"
  }
};

// Routes
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API endpoint to analyze content
app.post('/api/analyze', (req, res) => {
  const { content, platform } = req.body;

  if (!content) {
    return res.status(400).json({ error: 'Content is required' });
  }

  // Simulate analysis by agents
  const analysisResults = {
    content: content,
    platform: platform || 'general',
    timestamp: new Date().toISOString(),
    agents: Object.entries(mockAgentResponses).map(([name, data]) => ({
      name,
      ...data
    })),
    overallScore: Math.round(Object.values(mockAgentResponses).reduce((sum, agent) => 
      sum + (agent[Object.keys(agent)[0]] || 0), 0) / Object.keys(mockAgentResponses).length),
    finalDecision: "APPROVED"
  };

  res.json(analysisResults);
});

// API endpoint to get history
app.get('/api/history', (req, res) => {
  const history = [
    {
      id: 1,
      content: "Check out this amazing sunset!",
      platform: "Instagram",
      date: new Date(Date.now() - 86400000).toISOString(),
      score: 85,
      decision: "APPROVED"
    },
    {
      id: 2,
      content: "Just finished an amazing project",
      platform: "LinkedIn",
      date: new Date(Date.now() - 172800000).toISOString(),
      score: 78,
      decision: "APPROVED"
    }
  ];
  res.json(history);
});

// API endpoint to get stats
app.get('/api/stats', (req, res) => {
  const stats = {
    totalAnalyzed: 42,
    approved: 38,
    flagged: 3,
    rejected: 1,
    avgScore: 81.5
  };
  res.json(stats);
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Varanasi Web Server running at http://localhost:${PORT}`);
  console.log(`📊 Dashboard: http://localhost:${PORT}`);
});
