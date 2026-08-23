"""Held-out governance scenarios for F130."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"privacy_consent_gap": True}, False),
    (base() | {"sensitive_inference": True}, False),
    (base() | {"representation_bias": True}, False),
    (base() | {"unsupported_insight": True}, False),
    (base() | {"causal_overclaim": True}, False),
    (base() | {"reidentification_risk": True}, False),
    (base() | {"high_impact_use_risk": True}, False),
    (base() | {"evidence_provenance_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F130 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
