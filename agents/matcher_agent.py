from typing import Dict, Any
from .base_agent import BaseAgent

class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name = "Matcher",
            instructions="""Match the candidate profiles with job positions.
            Consider: Skill match, Experience level, location prefernces.
            Provide detailed reasoning and compatibility scores.
            Return matches in JSON format with the title, match_score and loaction fields."""
        )

        async def run(self, messages: list) -> Dict[str, Any]:
            """Match candidate with available positions"""
            print("Matcher: Finding suitable job matches")

            analysis_result = eval(messages[-1]["content"])
            
            #  create API for below
            sample_jobs = [
                {
                    "title": "Senior Software Engineer",
                    "requirements": "Python, cloud, 5+ years experience",
                    "location": "Remote",
                },
                {
                    "title": "Data Scientist",
                    "requirements": "Machine Learning, Python, SQL, 3+ years experience",
                    "location": "New York, NY",
                },
                {
                    "title": "DevOps Engineer",
                    "requirements": "AWS, Kubernetes, CI/CD, 4+ years experience",
                    "location": "Remote",
                },
                {
                    "title": "Frontend Developer",
                    "requirements": "React, JavaScript, HTML/CSS, 2+ years experience",
                    "location": "San Francisco, CA",
                },
                {
                    "title": "AI/ML Engineer",
                    "requirements": "Deep Learning, TensorFlow, Python, 3+ years experience",
                    "location": "Remote",
                },
                {
                    "title": "Backend Engineer",
                    "requirements": "Node.js, PostgreSQL, REST APIs, 4+ years experience",
                    "location": "Seattle, WA",
                }
            ]

            # Get matching results from ollama
            matching_response = self._query_ollama(
                f"""Analyze the following profile and provide job match in valid JSON format:
                Profile:{analysis_result['skills_analysis']}
                Available Jobs: {sample_jobs}
                
                Return ONLY a JSON object with the exact structure:
                {{
                    "matched_jobs":[
                        {{
                            "title": "job_title",
                            "match_score": "85%",
                            "location": "job_location"
                        }}
                        ],
                        "match_timeStamp":2025-02-16",
                        "number of matches": 5
                }}"""
            )
            
            # parse the response
            parsed_response = self._parse_json_safely(matching_response)

            # Fallback to sample data if parsing fails
            if "error" in parsed_response:
                return{
                    "matched_jobs": [
                            {
                            "title": "Senior Software Engineer",
                            "requirements": "Python, cloud, 5+ years experience",
                            "location": "Remote",
                        },
                        {
                            "title": "Data Scientist",
                            "requirements": "Machine Learning, Python, SQL, 3+ years experience",
                            "location": "New York, NY",
                        },
                        {
                            "title": "DevOps Engineer",
                            "requirements": "AWS, Kubernetes, CI/CD, 4+ years experience",
                            "location": "Remote",
                        }
                    ],
                    "match_timeStamp":"2025-02-16",
                    "number of matches": 5
                }
            return parsed_response
