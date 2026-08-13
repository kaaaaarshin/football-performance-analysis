# ⚽ Football Performance Analysis

An end-to-end football analytics platform for player profiling, role discovery, player similarity, and player recommendation using StatsBomb event data.

The project combines data ingestion, feature engineering, unsupervised clustering, supervised role classification, similarity analysis, a FastAPI backend, and an interactive React dashboard.

---

## 🚀 Features

- ⚽ Player performance profiling
- 🔎 Player search
- 📊 Player statistics dashboard
- 🧩 K-Means player clustering
- 🏷️ Player role / archetype discovery
- 🤖 SVM-based role classification
- 🔗 Player similarity using cosine similarity
- 👥 Similar-player recommendations
- ⚖️ Player comparison
- 📈 Interactive visualizations
- ⚡ FastAPI REST API
- ⚛️ React + Vite frontend

---

## 🧠 Machine Learning Pipeline

The system processes StatsBomb football event data into player-level performance profiles.

```text
StatsBomb Open Data
        │
        ▼
Data Ingestion
        │
        ▼
Season / Match Dataset
        │
        ▼
Player Profile Construction
        │
        ▼
Feature Engineering
        │
        ▼
Standardization
        │
        ▼
K-Means Clustering
        │
        ▼
5 Player Clusters
        │
        ▼
Role Mapping
        │
        ├── Defender
        ├── Midfielder
        ├── Attacker
        ├── Goalkeeper
        └── Utility
        │
        ├────────────────────┐
        ▼                    ▼
SVM Role Classifier    Similarity Engine
                           │
                           ▼
                    Player Recommendations
                           │
                           ▼
                     FastAPI Backend
                           │
                           ▼
                     React Dashboard