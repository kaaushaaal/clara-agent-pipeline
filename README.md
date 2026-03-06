# Clara AI – Agent Configuration Pipeline

This project implements an automated pipeline that converts onboarding conversations into structured **agent configuration specifications** for a voice receptionist system.

The pipeline extracts operational requirements from call transcripts and chat inputs, generates structured configuration artifacts, versions agent behavior, and stores results in a database. It also supports automation through **n8n orchestration**.

---

# System Overview

The pipeline processes onboarding data and produces:

* Structured **account memo**
* **Agent configuration specification**
* **Versioned updates (v1 → v2)**
* **Changelog showing differences**
* **Supabase storage for persistence**

Pipeline flow:

```
Dataset
  ↓
Memo Extraction (v1)
  ↓
Agent Spec Generation (v1)
  ↓
Onboarding Updates
  ↓
Memo Update (v2)
  ↓
Agent Spec Generation (v2)
  ↓
Changelog Generation
  ↓
Supabase Storage
```

The pipeline can be triggered manually or through **n8n orchestration**.

---

# Repository Structure

```
clara-agent-pipeline/

dataset/
  bens-electric/
    transcript.txt
    onboarding_transcript.txt
    chat.txt

scripts/
  generate_memo_v1.py
  generate_agent_v1.py
  update_memo_v2.py
  generate_agent_v2.py
  generate_changelog.py
  store_account_supabase.py

  run_pipeline.py
  run_all_accounts.py
  pipeline_server.py

outputs/
  accounts/
    bens-electric/
      v1/
        memo.json
        agent_spec.json
      v2/
        memo.json
        agent_spec.json

workflows/
  n8n_pipeline.json

logs/
  pipeline.log
```

---

# Setup Instructions

## 1. Clone the repository

```
git clone <repo-url>
cd clara-agent-pipeline
```

---

## 2. Create virtual environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

---

## 3. Install dependencies

```
pip install supabase flask
```

---

# Running the Pipeline

## Run a single account

```
python scripts/run_pipeline.py bens-electric
```

This executes the full pipeline for one dataset account.

---

## Run all accounts

```
python scripts/run_all_accounts.py
```

This automatically processes every account inside the `dataset/` directory.

---

# Supabase Integration

Results are stored in Supabase after each pipeline run.

The pipeline writes:

* memo_v1
* memo_v2
* agent_spec_v1
* agent_spec_v2

Each version is stored for comparison and auditing.

---

# n8n Orchestration

The system supports external orchestration using **n8n**.

## Start the pipeline server

```
python scripts/pipeline_server.py
```

Server runs at:

```
http://localhost:5000
```

---

## Import the n8n workflow

Open n8n:

```
http://localhost:5678
```

Import:

```
workflows/n8n_pipeline.json
```

The workflow triggers the pipeline via:

```
GET http://localhost:5000/run
```

This executes:

```
run_all_accounts.py
```

which processes the entire dataset automatically.

---

# Agent Specification Design

Each generated agent spec includes:

* call handling flow
* emergency detection
* service categorization
* call transfer protocol
* fallback logic
* business hours handling
* after-hours escalation

Example sections:

```
Business Hours Flow
After Hours Flow
Emergency Handling
Transfer Protocol
Fallback Protocol
```

These specifications are structured so they can be directly adapted for a voice AI platform.

---

# Versioning

Two versions of each account configuration are produced:

### v1

Generated from the **initial demo call transcript**.

### v2

Updated using **onboarding conversation updates**.

A changelog is generated to highlight configuration differences between versions.

---

# Logging

Pipeline execution logs are stored in:

```
logs/pipeline.log
```

Logs capture:

* account processing
* pipeline steps
* errors
* database writes

---

# Example Output

```
outputs/accounts/bens-electric/v1/memo.json
outputs/accounts/bens-electric/v1/agent_spec.json

outputs/accounts/bens-electric/v2/memo.json
outputs/accounts/bens-electric/v2/agent_spec.json
```

---

# Design Considerations

The pipeline was designed to support:

* reproducibility
* automation
* batch dataset processing
* versioned configuration management
* orchestration integration
* database persistence

These properties allow the system to scale across multiple onboarding accounts.

---

# Author

Kaushal
Final Year B.Tech Computer Science
