# F130 | Agentic Customer Insights | L3 Gold Standard | v1.0

A governed five-agent reference architecture for customer research, evidence intake, qualitative and quantitative synthesis, segmentation, insight generation, uncertainty management, privacy protection, representation review, and qualified human approval.

F130 is decision-support only. It can organize research evidence, synthesize interviews and feedback, analyze quantitative signals, identify themes, generate evidence-linked insights, and prepare decision-support packages. It cannot autonomously activate customer segments, contact customers, modify customer records, publish identifiable profiles, or make high-impact decisions about individuals.

## Customer-insights lifecycle

```text
Research Question and Evidence Intake
        -> Qualitative Synthesis
        -> Quantitative Analysis
        -> Triangulation and Insight Generation
        -> Privacy, Representation, Uncertainty, and Provenance Review
        -> Qualified Human Insights Approval
        -> Human-Controlled Downstream Use
```

The workflow fails closed when required reviews are missing or when material privacy, consent, sensitive-inference, representation, evidentiary, causal, reidentification, high-impact-use, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Evidence Agent | Registers sources, research context, provenance, limitations, and evidence quality | What evidence exists and how trustworthy and relevant is it? |
| Qualitative Agent | Synthesizes interviews, open text, observations, themes, contradictions, and quotations | What patterns and meanings appear in qualitative evidence? |
| Quantitative Agent | Analyzes metrics, survey responses, behavioral data, distributions, segments, and uncertainty | What measurable patterns are supported by the data? |
| Insight Agent | Triangulates evidence into findings, opportunities, hypotheses, and confidence-qualified insights | What can reasonably be concluded from the combined evidence? |
| Review Agent | Reviews privacy, consent, representation, uncertainty, causality, provenance, and approval state | Is the insight package appropriate for qualified human use? |

Agents support research and product judgment. They do not replace researchers, statisticians, privacy professionals, accessibility specialists, domain experts, legal counsel, ethics review, or accountable decision makers.

## Repository structure

```text
AGENTS/
├── evidence_agent.py
├── qualitative_agent.py
├── quantitative_agent.py
├── insight_agent.py
└── review_agent.py

SKILLS/
├── evidence_discipline.py
├── qualitative_reasoning.py
├── quantitative_reasoning.py
├── insight_reasoning.py
└── review_reasoning.py

TOOLS/
├── evidence_register.py
├── theme_table.py
├── metric_registry.py
├── insight_register.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Research framing

Customer-insight work should begin with an explicit research question, decision context, population, timeframe, known constraints, and intended use. A vague request to "understand customers" can encourage selective interpretation and should be decomposed into answerable questions.

Research questions can address needs, behaviors, motivations, barriers, adoption, satisfaction, retention, workflows, accessibility, product experience, decision criteria, or unmet needs.

## Evidence discipline

The executable policy requires `evidence_reviewed` and `evidence_provenance_reviewed`.

Evidence should preserve source type, collection method, population, sample, dates, geography, product version, question wording, researcher, transformations, limitations, and permitted use where relevant.

F130 distinguishes observation from interpretation and interpretation from recommendation.

## Evidence register

`TOOLS/evidence_register.py` provides a deterministic surface for evidence tracking. A production implementation can preserve fields such as:

```text
evidence_id
source_type
source_owner
collection_method
population
sample_size
collection_window
consent_basis
permitted_use
provenance
limitations
quality_state
review_state
```

## Source types

Potential evidence can include interviews, surveys, support tickets, usability studies, product analytics, CRM data, sales notes, reviews, observational studies, field research, experiments, community discussions, market research, and operational records.

Different sources answer different questions. High volume does not automatically mean high evidentiary quality.

## Qualitative research

The policy requires `qualitative_reviewed`.

Qualitative synthesis can identify motivations, mental models, unmet needs, workflows, language, frustrations, workarounds, contradictions, and context that aggregate metrics may miss.

The system should not convert a memorable quote into a population-level fact.

## Interview analysis

Interview synthesis should preserve participant context, question wording, interviewer influence, sample selection, contradictions, and uncertainty. Themes should remain traceable to underlying evidence.

## Coding and themes

`TOOLS/theme_table.py` can organize codes, themes, supporting evidence, contradictory evidence, frequency, segment context, confidence, and researcher notes.

Theme frequency is not automatically equivalent to importance, prevalence, or causal impact.

## Quotations

Customer quotations should be accurate and traceable. F130 must not fabricate quotes, merge statements from different participants into a synthetic quote presented as real, or expose identifying details without appropriate permission.

## Open-text analysis

Large volumes of survey comments, reviews, support messages, or other open text can be clustered and summarized. Automated categorization can miss sarcasm, multilingual nuance, domain terminology, rare but severe issues, or context.

Human review remains important for consequential conclusions.

## Quantitative research

The policy requires `quantitative_reviewed`.

Quantitative analysis can include counts, rates, distributions, trends, cohorts, survey scales, funnel metrics, behavioral events, retention, conversion, satisfaction, or other defined measures.

Metric definitions, denominators, filters, missingness, and observation windows should be explicit.

## Metric registry

`TOOLS/metric_registry.py` can preserve metric name, definition, numerator, denominator, source, owner, timeframe, segmentation, caveats, and version.

A metric name alone is insufficient evidence when teams use different definitions.

## Surveys

Survey analysis should preserve recruitment method, sample frame, response rate, question wording, scale design, order effects, nonresponse, weighting, and collection dates.

Leading questions and poorly defined scales can produce precise-looking but weak evidence.

## Sampling

Samples should be evaluated against the intended population. Convenience samples, highly engaged customers, support users, recent churners, or research-panel participants can differ materially from the broader customer base.

`representation_bias` blocks release when material sample or representation bias remains unresolved.

## Representation

The policy requires `representation_fairness_reviewed`.

Insight packages should identify which groups are represented, underrepresented, missing, or aggregated beyond useful interpretation. Lack of evidence about a group should not be silently interpreted as absence of need.

## Segmentation

Segments can be based on legitimate behavioral, lifecycle, product, organizational, contextual, or research variables when appropriate to the question.

Segmentation should not become unsupported psychological profiling or sensitive-trait inference.

## Sensitive inference

`sensitive_inference` blocks release when the system would infer or expose inappropriate sensitive characteristics without a legitimate, reviewed basis.

Potentially sensitive domains can include health, disability, financial hardship, race or ethnicity, religion, sexual orientation, political beliefs, precise location, family circumstances, or other protected or intimate information.

F130 should minimize rather than expand sensitive inference.

## Privacy and consent

The policy requires `privacy_consent_reviewed`.

`privacy_consent_gap` blocks release when data collection, analysis, linkage, retention, disclosure, or downstream use exceeds reviewed permission or legitimate purpose.

Customer research should respect notice, consent where required, contractual restrictions, withdrawal, deletion, retention, and purpose limitation.

## Data minimization

Collect and retain only what is necessary for the research purpose. Customer-insight work should not accumulate identifiable data merely because storage is available.

## De-identification

Removing names alone may not make data anonymous. Rare combinations of geography, role, age, behavior, dates, quotations, or product events can enable reidentification.

`reidentification_risk` blocks release when disclosure risk remains material.

## Small cells

Small segments can expose individuals or create unstable conclusions. Production implementations should use appropriate suppression, aggregation, access controls, and statistical disclosure practices.

## Data linkage

Linking interviews, product analytics, CRM records, support history, or external datasets can improve context while increasing privacy and reidentification risk. Linkage should have a legitimate purpose and reviewed authorization.

## Qualitative and quantitative triangulation

Triangulation asks whether different forms of evidence converge, diverge, or answer different parts of the research question.

A quantitative pattern can indicate where something occurs while qualitative evidence can help explain how participants experience it. Neither automatically proves causation.

## Insight generation

The policy requires `insight_reviewed`.

An insight should connect evidence to a meaningful interpretation that can inform a decision. It should preserve scope, confidence, limitations, contradictory evidence, and affected population.

`unsupported_insight` blocks release when a conclusion exceeds the available evidence.

## Insight register

`TOOLS/insight_register.py` can organize:

```text
insight_id
research_question
finding
interpretation
supporting_evidence
contradictory_evidence
population_scope
confidence
limitations
implication
owner
review_state
```

## Findings versus insights

A finding describes an observed pattern. An insight interprets why that pattern matters in context. A recommendation proposes an action.

F130 should preserve these distinctions so recommendations are not presented as direct observations.

## Causal boundaries

`causal_overclaim` blocks release when observational association is represented as causation.

For example, customers who use a feature more often may retain longer because the feature helps retention, because more committed customers choose the feature, or because both are driven by another factor.

Causal claims require appropriate experimental or quasi-experimental evidence.

## Correlation

Correlations can generate hypotheses but should preserve confounding, selection effects, reverse causality, measurement error, and multiple-comparison risks.

## Confidence and uncertainty

Confidence should reflect evidence quality, consistency, sample relevance, measurement quality, recency, and methodological limitations rather than rhetorical certainty.

F130 should explicitly surface when evidence is mixed or insufficient.

## Contradictory evidence

Contradictions are informative. The system should preserve disconfirming interviews, segments, metrics, or studies rather than deleting them to create a cleaner story.

## Negative evidence

Absence of observed complaints does not prove absence of a problem. Customers may churn silently, adapt with workarounds, lack access to feedback channels, or not recognize an issue as reportable.

## Jobs to be done

JTBD-style synthesis can organize customer situations, motivations, desired progress, barriers, alternatives, and outcomes. These constructs should be grounded in evidence rather than assigned as personality labels.

## Personas

Personas can be useful communication devices when they summarize real evidence. They become risky when fictional detail is mistaken for customer fact.

F130 should clearly distinguish research-backed attributes from illustrative narrative elements.

## Journey maps

Journey analysis can map stages, goals, touchpoints, emotions, friction, workarounds, and evidence. Journey maps should identify which elements are observed, inferred, or hypothesized.

## Customer needs

Needs can be functional, emotional, social, accessibility-related, operational, or contextual. A stated feature request should not automatically be treated as the underlying need.

## Accessibility research

Customer research should include accessibility needs where relevant and avoid assuming that the majority experience represents users with disabilities.

Research methods themselves should be accessible to participants.

## Inclusion

Recruitment and analysis should consider whether language, technology access, geography, disability, schedule, compensation, or research format systematically exclude relevant participants.

## Vulnerable customers

Research involving children, patients, people in crisis, financially vulnerable customers, or other vulnerable populations requires heightened consent, privacy, safeguarding, and ethical review.

## Incentives

Participant incentives should compensate appropriately without creating coercive pressure. Incentive design should consider population and study context.

## Researcher bias

Confirmation bias, leading questions, selective coding, survivorship bias, availability bias, and expectation effects can influence research. F130 should preserve evidence that challenges the initial hypothesis.

## AI-assisted coding

AI can accelerate coding and summarization but may introduce category drift, flatten nuance, misclassify rare themes, or amplify researcher assumptions. Automated coding should be auditable against source material.

## Sentiment analysis

Sentiment can support large-scale triage but is not a complete representation of customer experience. Sarcasm, cultural variation, mixed emotions, technical language, and multilingual content can reduce accuracy.

## Behavioral analytics

Behavioral events show what was recorded, not necessarily customer intent. Event instrumentation, bots, shared accounts, missing events, product changes, and identity stitching can affect interpretation.

## Funnel analysis

Funnels should preserve entry criteria, denominator, order, time window, repeated events, cross-device behavior, and eligibility. Drop-off indicates where behavior changes, not automatically why.

## Cohort analysis

Cohorts can reveal differences by acquisition period, product version, lifecycle stage, geography, customer type, or other legitimate dimensions. Cohort differences should not be automatically attributed to the cohort label itself.

## Retention and churn insights

Retention research should distinguish voluntary churn, involuntary churn, contract timing, product usage, customer maturity, pricing, support, market conditions, and survivorship.

Churn-risk patterns should not automatically trigger individual-level treatment without separate governance.

## Support data

Support tickets provide rich problem evidence but overrepresent customers who contact support. Ticket volume can also change because of channel design, self-service, routing, outages, or policy changes.

## Sales data

Sales notes can reveal objections and buyer context while reflecting seller incentives, qualification practices, and incomplete recording. They should be triangulated with other sources.

## Reviews and social data

Public reviews and online discussions can provide useful context but are self-selected and vulnerable to manipulation, brigading, duplicates, fake reviews, and platform-specific populations.

## Longitudinal research

Customer needs and behaviors change over time. Longitudinal analysis should preserve product versions, market conditions, customer tenure, research method changes, and cohort composition.

## Recency

Old evidence may no longer represent the current product or market. F130 should preserve collection dates and flag stale evidence when product, pricing, policy, or customer composition has changed materially.

## Market and customer distinction

Customer evidence describes observed or researched customers. It should not automatically be generalized to an entire addressable market, noncustomers, competitors' customers, or future populations.

## Competitive comparisons

Customer perceptions of competitors can inform hypotheses but should not be presented as verified competitor facts without separate evidence.

## Opportunity identification

F130 can identify evidence-backed opportunity areas, unmet needs, friction points, and research gaps. Opportunity size and priority require additional business, technical, strategic, and economic judgment.

## Prioritization

Frequency, severity, strategic relevance, affected population, confidence, accessibility impact, revenue, retention, implementation cost, and risk can all matter. No single customer metric should automatically determine roadmap priority.

## High-impact downstream use

`high_impact_use_risk` blocks release when insights would be used to make consequential decisions about individuals in areas such as employment, credit, insurance, housing, healthcare, education, legal access, or essential services without specialized qualified review.

Customer-insight tooling is not an authority for such decisions.

## Profiling boundaries

F130 should not construct hidden dossiers, infer intimate traits, rank personal worth, or recommend discriminatory treatment. Research synthesis should remain tied to legitimate research and product questions.

## Individual versus aggregate inference

Population-level patterns should not automatically be applied to a specific person. A segment average does not determine an individual's preferences, intent, risk, or behavior.

## Fairness

Fairness review should consider sampling, measurement, segmentation, accessibility, exclusion, downstream use, and whether findings could systematically disadvantage groups that are already underrepresented in the evidence.

## Localization

Research conducted in one language or market may not transfer directly to another. Translation should preserve meaning, idiom, scale interpretation, cultural context, and research intent.

## Multilingual research

Automated translation and sentiment tools can lose nuance. Important multilingual findings should be reviewed by people with appropriate language and cultural competence where feasible.

## Research operations

A mature research program should track study ownership, recruitment, participant contact, consent, incentive state, data access, retention, findings, and repository status without exposing unnecessary personal data.

## Research repositories

Research repositories can reduce duplicated studies and preserve organizational learning. Access controls, consent, retention, provenance, searchability, and stale-evidence handling should be designed explicitly.

## Duplicate evidence

The same customer statement may appear in interview notes, a research summary, a ticket, and a presentation. F130 should avoid counting duplicated evidence as independent support.

## Data quality

Quantitative data should be checked for missingness, duplicates, instrumentation changes, impossible values, outliers, identity errors, schema changes, and denominator drift before strong conclusions are drawn.

## Missing data

Missingness can be systematic. Customers who do not answer a survey, complete onboarding, enable telemetry, or contact support may differ from those who do.

## Outliers

Outliers can be errors, rare valid cases, fraud, accessibility edge cases, enterprise customers, or early indicators. They should be investigated rather than automatically removed.

## Statistical uncertainty

Point estimates should be accompanied by appropriate uncertainty when material. Small samples and repeated slicing can create unstable patterns.

## Multiple comparisons

Searching many metrics and segments increases the chance of finding apparently interesting patterns by chance. Exploratory findings should be labeled accordingly and validated where appropriate.

## Weighting

Survey or panel weighting can improve alignment with a target population but introduces modeling assumptions. Weight construction and limitations should be documented.

## Nonresponse bias

High response counts do not eliminate nonresponse bias. People who respond can differ systematically from those who do not.

## Survivorship bias

Research based only on active customers can miss people who failed onboarding, churned, were excluded, or never adopted the product.

## Selection bias

Recruitment channels can systematically favor particular customer types. Findings should preserve the recruitment mechanism and target population.

## Recall bias

Participants may misremember past behavior or motivations. Self-report and behavioral data can be compared where appropriate without assuming either is perfectly accurate.

## Social desirability bias

Participants may provide answers they believe are expected or acceptable. Research design and interpretation should account for this possibility.

## Observer effects

Research settings can change participant behavior. Moderated tests and interviews should distinguish observed behavior in study conditions from naturalistic product use.

## Synthetic data

Synthetic examples can support method testing but must never be represented as real customer evidence. Synthetic records should be clearly labeled and excluded from empirical prevalence claims.

## Fabricated evidence

F130 must never invent participants, interviews, survey responses, quotes, metrics, cohorts, themes, statistical results, or customer stories to fill evidence gaps.

## Data access

Customer data should follow least-privilege access. Research convenience does not justify broad access to identifiable records.

## Security

Research datasets can contain commercially sensitive and personal information. Production systems should use appropriate access control, encryption, logging, retention, and incident procedures.

## Deletion and withdrawal

Where applicable, participant withdrawal or deletion requests should propagate to research systems according to governing policy and law.

## Change control

Product changes, metric definitions, survey wording, recruitment methods, segmentation logic, coding frameworks, and research populations can alter conclusions. Material changes should be versioned.

## Versioning

Insight packages should preserve the evidence set, analysis method, date, product context, reviewer, confidence, and supersession state so teams know whether a finding remains current.

## Memory and state

The `memory/` layer can preserve structured research state. It should distinguish source evidence, derived themes, metrics, interpretations, recommendations, private data, review decisions, and downstream outcomes.

Sensitive information should be minimized and segregated where appropriate.

## Observability

The `observability/` layer supports traceability across evidence, qualitative synthesis, quantitative analysis, insights, privacy, representation, provenance, and governance state.

Useful telemetry includes source count, evidence age, sample context, theme support, contradictory evidence, metric definitions, privacy state, representation gaps, confidence, approval state, and protected-action attempts.

## Required reviews

The executable policy requires all eight conditions:

```text
evidence_reviewed
qualitative_reviewed
quantitative_reviewed
insight_reviewed
privacy_consent_reviewed
representation_fairness_reviewed
evidence_provenance_reviewed
qualified_insights_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- privacy, consent, or permitted-use review is incomplete
- unsupported or inappropriate sensitive inference is detected
- material sample or representation bias remains unresolved
- an insight exceeds available evidence
- association is represented as causation without adequate evidence
- reidentification or disclosure risk remains unresolved
- high-impact downstream use requires specialized human review
- evidence provenance is incomplete
- any required review is missing
- qualified customer-insights approval is missing

The system exposes uncertainty and blockers rather than manufacturing confidence.

## Protected actions

The safety policy permanently protects:

```text
publish_customer_profile
activate_segment
contact_customer
change_customer_record
make_high_impact_decision
external_distribution
```

These actions remain outside autonomous authority even after all review conditions are satisfied.

## Human authority boundaries

F130 must not autonomously publish identifiable customer profiles, activate marketing or product segments, contact customers, change customer records, make consequential decisions about individuals, disclose private research data, or externally distribute research findings.

Qualified humans retain control over participant recruitment, consent, data access, research interpretation, sensitive segmentation, publication, customer contact, and consequential downstream decisions.

## Explicit failure states

```text
EVIDENCE REVIEW REQUIRED
QUALITATIVE REVIEW REQUIRED
QUANTITATIVE REVIEW REQUIRED
INSIGHT REVIEW REQUIRED
PRIVACY OR CONSENT GAP
SENSITIVE INFERENCE BLOCKED
REPRESENTATION BIAS UNRESOLVED
INSIGHT UNSUPPORTED
CAUSAL OVERCLAIM
REIDENTIFICATION RISK
HIGH IMPACT USE ESCALATION REQUIRED
EVIDENCE PROVENANCE GAP
QUALIFIED INSIGHTS APPROVAL REQUIRED
CUSTOMER PROFILE PUBLICATION PROHIBITED
SEGMENT ACTIVATION PROHIBITED
CUSTOMER CONTACT PROHIBITED
CUSTOMER RECORD CHANGE PROHIBITED
HIGH IMPACT DECISION PROHIBITED
EXTERNAL DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Define the research question, decision context, target population, and intended use.
2. Register evidence sources, provenance, collection methods, consent, and limitations.
3. Review sample coverage, recruitment, representation, and missing populations.
4. Synthesize qualitative evidence while preserving contradictions and source traceability.
5. Analyze quantitative evidence with explicit metrics, denominators, filters, and uncertainty.
6. Triangulate qualitative and quantitative findings.
7. Generate insights that distinguish observations, interpretations, hypotheses, and recommendations.
8. Review privacy, consent, sensitive inference, reidentification, fairness, and downstream-use risk.
9. Preserve evidence provenance, uncertainty, contradictory evidence, and research gaps.
10. Apply fail-closed governance.
11. Require qualified human customer-insights approval.
12. Keep segment activation, customer contact, customer-record changes, identifiable profile publication, high-impact decisions, and external distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test evidence traceability, qualitative fidelity, quantitative reasoning, triangulation, uncertainty, representation awareness, privacy behavior, and governance.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, privacy gaps, sensitive inference, representation bias, unsupported insights, causal overclaim, reidentification risk, high-impact downstream use, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Reproducible insight generation requires preserving research questions, source evidence, sample definitions, collection windows, survey wording, coding frameworks, metric definitions, transformations, segmentation, analysis methods, contradictions, confidence, and review state.

## Extension points

Organization-specific implementations can add governed integrations for research repositories, survey systems, analytics platforms, data warehouses, CRM, support systems, interview repositories, experimentation systems, transcription services, and product analytics.

Any integration capable of contacting customers, changing customer records, activating audiences, or making consequential decisions should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include interview synthesis, survey analysis, voice-of-customer programs, usability-research synthesis, customer journey research, churn research, onboarding analysis, support-theme analysis, accessibility research, segmentation research, product discovery, market-learning synthesis, and research repository support.

F130 is not an autonomous customer profiler, marketing activation engine, surveillance system, high-impact decision maker, or substitute for qualified research, statistical, privacy, legal, accessibility, or domain judgment.

## Design principles

1. Evidence before narrative convenience.
2. Preserve source provenance, sample context, contradictions, and uncertainty.
3. Separate observation, interpretation, hypothesis, and recommendation.
4. Protect privacy, consent, vulnerable participants, and sensitive information.
5. Reject unsupported sensitive inference and hidden profiling.
6. Review representation before generalizing from a sample.
7. Never convert correlation into causation without adequate design.
8. Keep individual-level and high-impact decisions outside autonomous authority.
9. Fail closed when material evidence or review is incomplete.

## Scope statement

F130 demonstrates a governed multi-agent architecture for customer-insight decision support. It combines specialized evidence, qualitative, quantitative, insight, and review agents with deterministic evidence, theme, metric, insight, and review tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over customer contact, profiling, activation, and consequential downstream use.

Author: Mahsa Keikha
