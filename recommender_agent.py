from typing import Dict, Any
from .base_agent import BaseAgent

class RecommenderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
        name = "Recommender",
        instructions = """Generate final Recommendations considering:
        1.Extraction Profile
        2. Skills analysis
        3. Job matches
        4. Screening results
        Provide clear next steps and specific recommendations.""",
        )

    async def run(self, messages: list) -> Dict[str, Any]:
        """Generate final recommendations"""
        print("Recommender: Generating final recommendation")

        workflow_context = eval(messages[-1]["content"])
        recommendation = self._query_ollama(str(workflow_context))

        return {
            "final-recommendation":recommendation,
            "recommendation_timestamp":"2025-02-17",
            "confidence_level": "high",        
            }