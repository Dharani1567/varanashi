// Tab Navigation
document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const tabName = e.target.dataset.tab;
        switchTab(tabName);
    });
});

function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active state from all nav buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(`${tabName}-tab`).classList.add('active');
    
    // Add active state to clicked button
    event.target.classList.add('active');
    
    // Load data for specific tabs
    if (tabName === 'history') {
        loadHistory();
    } else if (tabName === 'stats') {
        loadStats();
    }
}

// Form Submission
document.getElementById('analyzeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const content = document.getElementById('content').value;
    const platform = document.getElementById('platform').value;
    
    if (!content.trim()) {
        alert('Please enter content to analyze');
        return;
    }
    
    // Show loading, hide results
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('results').classList.add('hidden');
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content, platform })
        });
        
        if (!response.ok) throw new Error('Analysis failed');
        
        const data = await response.json();
        displayResults(data);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Error analyzing content. Please try again.');
    } finally {
        document.getElementById('loading').classList.add('hidden');
    }
});

function displayResults(data) {
    // Display overall score
    document.getElementById('overallScore').textContent = data.overallScore;
    document.getElementById('finalDecision').textContent = data.finalDecision;
    
    // Update decision color
    const decisionEl = document.getElementById('finalDecision');
    decisionEl.className = 'score-decision';
    if (data.finalDecision === 'APPROVED') {
        decisionEl.style.color = '#10b981';
    } else if (data.finalDecision === 'FLAGGED') {
        decisionEl.style.color = '#f59e0b';
    } else {
        decisionEl.style.color = '#ef4444';
    }
    
    // Display agent results
    const agentsContainer = document.getElementById('agentsContainer');
    agentsContainer.innerHTML = '';
    
    data.agents.forEach(agent => {
        const scoreKey = Object.keys(agent).find(key => 
            key.includes('score') || key.includes('Score')
        ) || 'score';
        
        const card = document.createElement('div');
        card.className = 'agent-card';
        
        const scoreValue = agent[scoreKey] || 0;
        const voteClass = agent.vote.toLowerCase();
        
        card.innerHTML = `
            <div class="agent-name">${agent.name}</div>
            <div class="agent-score">
                <span class="agent-score-value">${scoreValue}</span>
                <span class="agent-score-unit">/100</span>
            </div>
            <span class="agent-vote ${voteClass}">${agent.vote.toUpperCase()}</span>
            <p class="agent-explanation">${agent.explanation}</p>
        `;
        
        agentsContainer.appendChild(card);
    });
    
    // Show results
    document.getElementById('results').classList.remove('hidden');
}

function resetForm() {
    document.getElementById('analyzeForm').reset();
    document.getElementById('results').classList.add('hidden');
}

function saveResult() {
    alert('Result saved to history!');
    // In a real app, this would save to the backend
}

// Load History
async function loadHistory() {
    try {
        const response = await fetch('/api/history');
        if (!response.ok) throw new Error('Failed to load history');
        
        const data = await response.json();
        displayHistory(data);
        
    } catch (error) {
        console.error('Error loading history:', error);
    }
}

function displayHistory(items) {
    const container = document.getElementById('historyContainer');
    
    if (items.length === 0) {
        container.innerHTML = '<p style="color: var(--text-secondary); text-align: center; padding: 40px;">No analysis history yet</p>';
        return;
    }
    
    container.innerHTML = items.map(item => `
        <div class="history-item">
            <div class="history-header">
                <span class="history-platform">${item.platform}</span>
                <span class="history-date">${new Date(item.date).toLocaleDateString()}</span>
            </div>
            <div class="history-content">
                "${item.content.substring(0, 100)}${item.content.length > 100 ? '...' : ''}"
            </div>
            <div class="history-footer">
                <span class="history-score">Score: ${item.score}/100</span>
                <span class="history-decision ${item.decision.toLowerCase()}">${item.decision}</span>
            </div>
        </div>
    `).join('');
}

// Load Stats
async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        if (!response.ok) throw new Error('Failed to load stats');
        
        const data = await response.json();
        displayStats(data);
        
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

function displayStats(stats) {
    document.getElementById('statTotal').textContent = stats.totalAnalyzed;
    document.getElementById('statApproved').textContent = stats.approved;
    document.getElementById('statFlagged').textContent = stats.flagged;
    document.getElementById('statRejected').textContent = stats.rejected;
    document.getElementById('statAvgScore').textContent = stats.avgScore.toFixed(1);
}

// Load stats on page load
window.addEventListener('load', () => {
    loadStats();
});
