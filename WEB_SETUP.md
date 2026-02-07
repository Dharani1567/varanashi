# Varanasi - Web Interface

A modern web interface for the Varanasi Content Analysis Platform built with Node.js, Express, HTML, CSS, and JavaScript.

## Features

- 🔍 **Content Analysis** - Submit content for analysis by multiple AI agents
- 📊 **Real-time Scoring** - Get instant scores from context, engagement, virality, safety agents
- 📈 **Statistics Dashboard** - Track analysis history and platform statistics
- 🎨 **Modern UI** - Dark-themed, responsive interface
- ⚡ **Fast API** - RESTful API built with Express.js

## Project Structure

```
Varanasi/
├── server.js              # Node.js Express server
├── package.json           # Dependencies
├── .env                   # Environment variables
├── public/
│   ├── index.html        # Main HTML page
│   ├── style.css         # Styling (dark theme)
│   └── script.js         # Frontend logic
├── agents/               # Python agents (unchanged)
├── crew/                 # CrewAI setup
├── utils/                # Utilities
├── memory/               # Memory management
└── workflows/            # N8N workflows
```

## Installation

1. **Install Node.js dependencies:**

```bash
npm install
```

2. **Configure environment variables:**

Edit `.env` file and add your API keys:

```env
PORT=3000
NODE_ENV=development
GROK_API_KEY=your_key_here
```

## Running the Server

### Development Mode (with auto-reload)

```bash
npm run dev
```

### Production Mode

```bash
npm start
```

The server will start on `http://localhost:3000`

## API Endpoints

### POST /api/analyze
Analyze content with all agents

**Request:**
```json
{
  "content": "Your content here",
  "platform": "twitter|instagram|linkedin|tiktok|general"
}
```

**Response:**
```json
{
  "content": "...",
  "platform": "twitter",
  "timestamp": "2026-02-07T...",
  "agents": [
    {
      "name": "Agent Name",
      "score": 85,
      "vote": "approve",
      "explanation": "..."
    }
  ],
  "overallScore": 82,
  "finalDecision": "APPROVED"
}
```

### GET /api/history
Get analysis history

### GET /api/stats
Get platform statistics

## Interface Sections

### 1. Analyze Tab
- Submit content for analysis
- Select target platform
- View real-time results with agent scores
- Save results to history

### 2. History Tab
- View all past analyses
- See scores and decisions
- Filter by platform

### 3. Stats Tab
- Total content analyzed
- Approval rate
- Average scores
- Performance metrics

## Customization

### Modify Agent Mock Responses
Edit `server.js` line 15-30 to adjust agent response templates:

```javascript
const mockAgentResponses = {
  "Your Agent Name": {
    score: 75,
    vote: "approve",
    explanation: "Custom explanation"
  }
};
```

### Update Styling
All CSS is in `public/style.css`. Key theme variables:

```css
--primary-color: #6366f1
--secondary-color: #8b5cf6
--success-color: #10b981
--danger-color: #ef4444
```

### Integrate Python Backend
Currently using mock data. To connect real Python agents:

1. Add Python Flask API alongside Node.js server
2. Update fetch calls in `public/script.js`
3. Or use child_process to call Python directly

## Technologies Used

- **Backend:** Node.js, Express.js
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Styling:** Dark theme with gradient accents
- **API:** RESTful design

## Future Enhancements

- [ ] WebSocket for real-time updates
- [ ] Database integration (MongoDB/PostgreSQL)
- [ ] User authentication
- [ ] Batch processing
- [ ] Export results (PDF/CSV)
- [ ] Integration with Python CrewAI agents
- [ ] Real-time agent streaming

## License

MIT
