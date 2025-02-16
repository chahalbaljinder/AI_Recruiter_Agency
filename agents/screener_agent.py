from typing import Dict, Any
from .base_agent import BaseAgent

class ScreenerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Screener",
            instructions="""Screen candidates based on:
            -Qualifications Alignment
            -Experience Relevance 
            -Skill match percentage
            -Cultural fit Indicators
            -Red flags or concerns
            Provide comprehensive screening reports.""",
        )

    async def run(self, messages:list) ->Dict[str,Any]:
        """Screen the candidate"""
        print("Screener: Conducting initial screening")

        workflow_context = eval(messages[-1]["content"])
        screening_results = self._query_ollama(str(workflow_context))

        return {
            "Screening_report": screening_results,
            "Screening_timestamp": "2025-02-16",
            "Screening_score": 85, 
        }