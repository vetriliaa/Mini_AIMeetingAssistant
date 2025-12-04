import anthropic
import json
import re
from typing import Dict, Any

class MeetingAnalyzer:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def analyze_transcript(self, transcript: str) -> Dict[str, Any]:
        # Send transcript to Claude
        
        prompt = f"""Analyze this meeting transcript and extract:
1. Action items (who needs to do what)
2. Key decisions made
3. Overall sentiment (1-10 scale)
4. Main topics discussed

Return ONLY a JSON object with this structure (no other text before or after):
{{
  "action_items": [
    {{"task": "...", "owner": "...", "deadline": "..."}}
  ],
  "key_decisions": ["decision 1", "decision 2"],
  "sentiment_score": 7,
  "topics": ["topic 1", "topic 2"]
}}

Transcript:
{transcript}

"""
        
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        response_text = response.content[0].text
        
        try:
            # Direct parsing
            result = json.loads(response_text)
        except json.JSONDecodeError:
            # Extract JSON from response
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
            else:
                # Returns empty by default
                result = {
                    "action_items": [],
                    "key_decisions": [],
                    "sentiment_score": 5,
                    "topics": []
                }
        
        return result