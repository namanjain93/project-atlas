# Atlas Experiment Protocol

## Purpose

Every material research experiment must follow a consistent process.

---

## Experiment Lifecycle

Research Question
        |
        v
Literature Review
        |
        v
Hypothesis
        |
        v
Data Definition
        |
        v
Feature Definition
        |
        v
Statistical Test
        |
        v
Model / Backtest
        |
        v
Out-of-Sample Validation
        |
        v
Robustness Testing
        |
        v
Conclusion

---

## Experiment ID

Every experiment receives a unique identifier.

Format:

EXP-XXXX

Example:

EXP-0001

---

## Required Experiment Components

Each experiment should document:

- Objective
- Hypothesis
- Economic rationale
- Dataset
- Universe
- Time period
- Features
- Target
- Model
- Benchmarks
- Results
- Robustness
- Limitations
- Decision

---

## Experiment Rules

1. Hypotheses should be documented before testing whenever practical.
2. Changes after seeing results must be explicitly documented.
3. Validation data must not be used to optimize the model.
4. Multiple testing must be considered where applicable.
5. Statistical significance must not be confused with economic significance.
6. Transaction costs and liquidity must be considered for trading conclusions.
7. Negative results must be retained.

---

## Experiment Status

Experiments may have one of four statuses:

- PROPOSED
- RUNNING
- COMPLETED
- ARCHIVED

---

## Research Decision

Every completed experiment must conclude with one of:

- ACCEPT
- REJECT
- INCONCLUSIVE
- EXTEND

The reason must be documented.
