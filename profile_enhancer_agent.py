from typing import Dict, Any
from swarm import Agent

# Profile Enhancer agent: Enhances the candidate's profile
def profile_enhancer_agent_fucntion(extracted_info: Dict[str, Any])->Dict[str, Any]:
    enhanced_profile = extracted_info.copy()
    total_experience_years= sum(item["years"] for item in extracted_info["experinece"])
    enhanced_profile["summary"] = (
        f"{extracted_info["name"]} has {total_experience_years} year of experience"
    )

    return enhanced_profile

profile_enhancer_agent = Agent(
    name = "Profile Enhancer Agent",
    model = "llama3.2:1b",
    instructions = "Enhance the candidate's profile based on the extracted information",
    functions = [profile_enhancer_agent_fucntion],
)