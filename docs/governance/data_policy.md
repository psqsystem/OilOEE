# Data Governance Policy

Principles:

- Purpose limitation: monitoring data is not auto-reused for training.
- Data minimization: only fields required for OEE mapping are retained.
- Anonymization before model input: operator, location, and shift notes removed or aggregated.
- Role-based access: individual-level outputs restricted.
- Audit trail: every label acceptance or rejection is logged.
- Worker consultation: collective dialogue and independent data expertise recognized.
- Model role: LLM is a labeling assistant, not a technical authority.

Retention:

- Raw reports: per site policy, minimum required for OEE auditing.
- Validated labels: retained for model reproducibility.
- Rejected labels: retained as negative samples for retraining.
