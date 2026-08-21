from dataclasses import dataclass, field

@dataclass
class InsightState:
    evidence: list = field(default_factory=list)
    qualitative: list = field(default_factory=list)
    quantitative: list = field(default_factory=list)
    human_approval: bool = False
