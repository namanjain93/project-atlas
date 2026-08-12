# Atlas Decision Log

This document records material decisions affecting the architecture, research methodology or project scope.

---

## ADR-0001 — Repository Platform

Decision: GitHub

Reason: Strong ecosystem, version control, collaboration and integration with research tooling.

Date: 2026-08-13

---

## ADR-0002 — Initial Research Environment

Decision: Google Colab

Reason: Reduces local setup complexity and allows rapid experimentation while the project is in its research phase.

Trade-off: Not intended to be the final production execution environment.

Date: 2026-08-13

---

## ADR-0003 — Initial Data Policy

Decision: Publicly available data

Reason: Minimize cost during the research discovery phase.

Future consideration: Commercial datasets may be evaluated if data quality becomes a material research constraint.

Date: 2026-08-13

---

## ADR-0004 — Historical Research Period

Decision: 2015–2025

Validation: 2026

Reason: Provides a decade of historical research while preserving a genuinely unseen validation period.

Date: 2026-08-13

---

## ADR-0005 — Initial Research Universe

Decision: NIFTY 50, with explicit consideration of historical membership and survivorship bias.

Reason: High liquidity, data availability and relevance to Indian large-cap equities.

Date: 2026-08-13

---

## ADR-0006 — Initial Trading Horizon

Decision: 20 trading days as the primary swing-trading horizon.

Reason: Relevant to the project's eventual swing-trading objective while remaining long enough to reduce excessive microstructure noise.

Note: Alpha will also investigate multiple horizons.

Date: 2026-08-13
