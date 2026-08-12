# Atlas Coding Standards

## General Principle

Code should prioritize readability, reproducibility and maintainability over cleverness.

---

## Python

Follow modern Python conventions and use clear descriptive names.

Example:

momentum_20d

is preferred over:

m20

unless the abbreviation is formally defined.

---

## Notebooks

Notebooks are primarily for:

- Exploration
- Visualization
- Research experiments
- Prototyping

Reusable production logic should eventually be moved into the atlas package.

---

## Functions

Functions should:

- Do one logical job
- Have descriptive names
- Avoid hidden side effects
- Document important assumptions

---

## Data

Raw data should never be modified directly.

Preferred flow:

Raw
 |
Validation
 |
Transformation
 |
Processed
 |
Features

---

## Reproducibility

Experiments should record:

- Dataset version
- Code version
- Model version
- Parameters
- Random seed where applicable

---

## Secrets

API keys and credentials must never be committed to GitHub.

Use environment variables or secret-management mechanisms.

---

## Comments

Comments should explain why something is done, not merely repeat what the code does.
