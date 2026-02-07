"""
Threshold definitions - platform-specific rules and safety thresholds.
"""

PLATFORM_RULES = {
    "twitter": {
        "max_length": 280,
        "max_hashtags": 5,
        "max_mentions": 3,
    },
    "instagram": {
        "max_length": 2200,
        "max_hashtags": 30,
        "supports_links": False,
    },
    "linkedin": {
        "max_length": 3000,
        "max_hashtags": 5,
        "professional_tone": True,
    },
}

SAFETY_THRESHOLDS = {
    "max_risk_score": 0.3,
    "min_engagement_score": 0.4,
    "language_check": True,
    "hate_speech_threshold": 0.1,
    "misinformation_threshold": 0.2,
}

POSTING_THRESHOLDS = {
    "daily_limit": 10,
    "hourly_limit": 2,
    "min_interval_minutes": 15,
}
