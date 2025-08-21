# OpenDex

# 📊 DataDex – A Modern Data-Driven Pokédex

DataDex is a production-style data engineering project that ingests Pokémon data from the PokeAPI
, transforms it into dimensional/fact models, and exposes it through a queryable warehouse, APIs, and dashboards.

🔧 Tech Stack

Python + Pandas → API ingestion & JSON normalization

Apache Airflow → Orchestrated ETL pipelines

Apache Spark → Transformations, exploding nested JSON, building dims/facts

AWS S3 → Raw + staging data lake

Postgres/Redshift → Data warehouse with analytical schemas

FastAPI → Query API (search, compare, type effectiveness)

Streamlit/Metabase → Interactive Pokédex dashboards

Docker + GitHub Actions → Reproducible deployments & CI/CD

Grafana + CloudWatch → Pipeline health, data freshness, and observability

🚀 Features

Scheduled ingestion of Pokémon, moves, abilities, and type matchups

Dimensional & fact tables for analytical queries (e.g., fastest Pokémon by gen)

REST API with filters, comparisons, and type effectiveness calculator

Streamlit UI with search, compare, and type-matrix explorer

Monitoring dashboards with freshness alerts and ingestion lag metrics

🎯 Why This Project

This project simulates a real-world data platform: API ingestion, scalable transformations, data warehousing, pipeline orchestration, monitoring, and a public-facing UI.
It demonstrates end-to-end data engineering skills on a dataset that’s fun, familiar, and instantly engaging.
