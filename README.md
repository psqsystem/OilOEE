# OilOEE

AI-Driven Work-Order Analytics for OEE Optimization in Industrial Environments

## Overview

OilOEE is an open research and engineering project that collects, structures, and analyzes individual work-order reports from industrial environments in order to train and evaluate artificial intelligence models. The core idea is to synchronize human-written shift notes, maintenance logs, and failure reports with OEE (Overall Equipment Effectiveness) indicators, transforming scattered operational text into a measurable and auditable data asset for machine learning.

The project targets three industrial domains:

- Oil and gas production and processing facilities
- Aviation maintenance, repair, and overhaul (MRO)
- Transportation and logistics systems

## Objective

The primary objective is to build a reproducible pipeline in which:

1. Work-order reports are captured in a structured and privacy-aware format.
2. Each report is mapped to one or more OEE components (Availability, Performance, Quality).
3. Supervisor validation is performed as a technical label-verification step, not merely an administrative signature.
4. Validated data becomes training input for models that classify failure modes, estimate reliability, and identify root causes of OEE loss.

## Scope

In scope:

- Data schema design for work-order reports aligned with OEE calculation.
- Human-in-the-loop labeling workflow with supervisor approval and audit trail.
- Natural language processing of short, unstructured, domain-specific maintenance text.
- Knowledge graph construction linking equipment, failure events, and work orders.
- Site-specific model calibration, because OEE behavior differs significantly across plants.

Out of scope:

- Real-time control of industrial equipment.
- Autonomous maintenance decision-making without human approval.
- Personal performance evaluation of individual workers.

## Key Concepts

OEE is defined as the product of three components:

- Availability: ratio of actual operating time to planned production time.
- Performance: ratio of actual output to theoretical maximum output.
- Quality: ratio of good units to total units produced.

Each work-order report must be linked to at least one of these components to produce a meaningful learning target. Without this mapping, a model learns only the text of failures, not the cause of OEE loss.

## Architecture

The proposed architecture has four layers:

1. Raw work-order layer: free-text description, action taken, downtime duration, equipment identifier, shift, and date.
2. Metadata layer: equipment hierarchy, shift calendar, and operational context.
3. OEE label layer: mapping of each event to Availability, Performance, or Quality impact.
4. Validation layer: supervisor approval or correction of each label, stored with an audit trail.

A knowledge graph sits alongside these layers and connects equipment, failure modes, work orders, and root-cause analyses. It functions as a digital twin of the plant and provides engineering grounding for AI agents.

## Data Governance and Privacy

Privacy and governance are architectural requirements, not add-ons.

- Purpose limitation: data collected for daily monitoring is not automatically reused for model training.
- Data minimization: only fields required for OEE mapping are retained.
- Anonymization before model input: operator names, exact locations, and shift notes are removed or aggregated.
- Role-based access: individual-level outputs are restricted under occupational-health governance.
- Audit trail: every label acceptance or rejection is recorded.
- Worker consultation: collective dialogue and independent data expertise are recognized as necessary governance mechanisms.

## Human-in-the-Loop Validation

Large language models are used as labeling assistants, not as technical authorities. A qualified supervisor must confirm the AI-generated summary and take prioritization decisions under organizational rules. The AI does not issue diagnoses, work instructions, or technical approvals.

Workflow:

1. Technician or operator submits the raw report.
2. LLM proposes a failure-mode label and an OEE component mapping.
3. Supervisor accepts or corrects the label.
4. Accepted records enter the training set; rejected records are kept as negative or re-training samples.

## Industry Use Cases

### Oil and Gas

OEE in oil and gas facilities is strongly affected by unplanned shutdowns and internal slowdowns. Site-specific calibration is required because plants with stable performance are harder to model than plants with volatile performance. An LLM-based AI agent combined with a knowledge graph has been shown to identify work-order delays and unresolved root-cause analyses as key drivers of OEE loss.

### Aviation MRO

Aviation maintenance records and pilot logs contain safety ground truth that sensors cannot capture. The main challenge is data fragmentation across paper records, ERP systems, and manual processes. Integration with part traceability and certification records is essential when applying this project's pipeline to aviation.

### Transportation and Logistics

In logistics, OEE is typically combined with MTBF, MTTR, and failure-rate indicators. Predictive maintenance based on AI applied to maintenance reports has demonstrated measurable reductions in failure rate and improvements in OEE in piggyback transport systems.

## Repository Structure

data/         Schemas, sample anonymized records, and labeling guidelines
docs/         Architecture notes, governance policy, and design decisions
src/          Data ingestion, NLP pipeline, OEE mapping, and model training code
notebooks/    Exploratory analysis and calibration experiments
tests/        Unit and integration tests
.github/      CI workflows and issue templates

## Roadmap

Phase 1 - Limited pilot: one site, one equipment family, 100 percent supervisor validation of proposed labels.

Phase 2 - OEE integration and governance: connect validated labels to OEE calculation at equipment and shift level, implement anonymization and role-based access, build initial knowledge graph.

Phase 3 - Model training and deployment: train failure-mode classification and OEE-loss attribution models, deploy as human-in-the-loop assistants, monitor drift.

Phase 4 - Cross-site and cross-industry expansion: site-specific calibration, aviation certification layer, transport MTBF and MTTR integration.

## Getting Started

Clone the repository and review the documentation folder before contributing data or code.

git clone https://github.com/psqsystem/OilOEE.git
cd OilOEE

## Contributing

Contributions are welcome in the form of schema proposals, anonymized sample data, labeling guidelines, and model evaluation results. All contributions must respect the governance rules described above.

## License

To be defined. Until a license is added, all rights are reserved by the project owner.

## Contact

Maintainer: psqsystem
Repository: https://github.com/psqsystem/OilOEE