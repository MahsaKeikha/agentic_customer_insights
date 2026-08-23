"""Fail-closed governance for F130 Agentic Customer Insights."""

PROTECTED_ACTIONS = {
    "publish_customer_profile",
    "activate_segment",
    "contact_customer",
    "change_customer_record",
    "make_high_impact_decision",
    "external_distribution",
}

REQUIRED_REVIEWS = (
    "evidence_reviewed",
    "qualitative_reviewed",
    "quantitative_reviewed",
    "insight_reviewed",
    "privacy_consent_reviewed",
    "representation_fairness_reviewed",
    "evidence_provenance_reviewed",
    "qualified_insights_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding customer action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required customer-insights review", "missing": missing}
    checks = {
        "privacy_consent_gap": "privacy, consent, or permitted-use gap unresolved",
        "sensitive_inference": "unsupported or inappropriate sensitive inference detected",
        "representation_bias": "sample or representation bias materially unresolved",
        "unsupported_insight": "insight exceeds available evidence",
        "causal_overclaim": "association is being represented as causation",
        "reidentification_risk": "reidentification or disclosure risk unresolved",
        "high_impact_use_risk": "high-impact downstream use requires specialized human review",
        "evidence_provenance_gap": "evidence provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "customer-insights governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "customer-insights support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
