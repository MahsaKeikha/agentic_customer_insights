from AGENTS import evidence_agent, insight_agent, qualitative_agent, quantitative_agent, review_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "evidence": evidence_agent.run(case),
        "qualitative": qualitative_agent.run(case),
        "quantitative": quantitative_agent.run(case),
        "insight": insight_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
