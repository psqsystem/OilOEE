# Architecture Overview

Four-layer pipeline:

1. Raw work-order layer: free text, action taken, downtime, equipment id, shift, date.
2. Metadata layer: equipment hierarchy, shift calendar, operational context.
3. OEE label layer: mapping of each event to Availability, Performance, Quality.
4. Validation layer: supervisor approval or correction, stored with audit trail.

A knowledge graph links equipment, failure modes, work orders, and RCA records.
It provides engineering grounding for LLM-based labeling assistants.

Data flow:
raw -> preprocess -> LLM label proposal -> supervisor validation -> training set -> model -> OEE attribution