# Atlas Research Charter

**Version:** 1.0  
**Status:** Active  
**Project:** Atlas Research Labs

---

## 1. Mission

Atlas is a quantitative research and investment intelligence platform focused on the Indian equity market.

Its objective is to systematically investigate how fundamental, technical, sentiment, behavioural and macroeconomic information affects Indian equity returns, and to determine whether these insights can be converted into a robust, explainable and reproducible investment process.

---

## 2. Research Philosophy

Atlas follows five principles:

1. Evidence over intuition.
2. Research before optimization.
3. Out-of-sample validation before conclusions.
4. Reproducibility of every material result.
5. Risk-adjusted performance rather than raw returns.

The project is designed to falsify hypotheses rather than prove preconceived beliefs.

---

## 3. Research Question

The primary research question is:

> How does information become stock prices in the Indian equity market, and how does the predictive importance of fundamentals, technicals, sentiment and macroeconomic variables change across investment horizons and market regimes?

A central sub-question is:

> Has the relative importance of fundamental information changed between 2015 and 2025 as market participation, information availability and trading technology have evolved?

---

## 4. Research Period

### Historical Research Period

2015–2025

This period will be used for:

- Literature-informed hypothesis testing
- Exploratory analysis
- Model development
- Feature evaluation
- Statistical testing
- Historical backtesting

### Out-of-Sample Validation

2026

The methodology and model specification should be frozen before final 2026 validation.

No model modification should be made merely to improve performance on the validation period.

---

## 5. Initial Market Universe

The initial research universe will be NIFTY 50 constituents, with appropriate treatment of historical index membership and survivorship bias.

The universe may later expand to:

- NIFTY 100
- NIFTY 500
- Other liquid Indian equities

Any expansion must be documented as a separate research decision.

---

## 6. Information Categories

Atlas will initially investigate four primary information categories.

### Fundamentals

Examples:

- Revenue growth
- Earnings growth
- EPS
- ROE
- ROCE
- Operating margins
- Free cash flow
- Debt
- Valuation
- Book value

### Technicals

Examples:

- Momentum
- RSI
- Moving averages
- Relative strength
- Volume
- Volatility
- ATR
- Trend measures

### Sentiment / Behaviour

Examples:

- India VIX
- FII/DII flows
- Options positioning
- News sentiment
- Retail participation proxies
- Search interest where reliable

### Macroeconomics

Examples:

- Interest rates
- Inflation
- USD/INR
- Crude oil
- Bond yields
- Economic growth

---

## 7. Primary Research Horizons

Initial analysis will examine:

- 5 trading days
- 20 trading days
- 60 trading days
- 120 trading days
- 250 trading days

The 20-trading-day horizon will receive particular attention because it is relevant to the project's swing-trading objective.

---

## 8. Primary Target

The initial predictive target will be:

> Whether a stock outperforms its appropriate benchmark over the specified forward horizon.

The project will not initially attempt to predict an exact future stock price.

---

## 9. Benchmarking

Models and strategies must be evaluated against appropriate simple benchmarks, including where applicable:

- NIFTY buy-and-hold
- Equal-weight portfolio
- Simple momentum strategy
- Simple value strategy
- Simple quality strategy
- Moving-average strategy

Complexity must demonstrate incremental value over simpler alternatives.

---

## 10. Validation Principles

Atlas must actively guard against:

- Look-ahead bias
- Survivorship bias
- Data leakage
- Data snooping
- Overfitting
- Selection bias
- Incorrect corporate-action treatment
- Unrealistic transaction assumptions

Where relevant, we will use:

- Time-series cross-validation
- Walk-forward validation
- Out-of-sample testing
- Rolling-window analysis
- Regime analysis

---

## 11. Research Governance

A result cannot become part of the production strategy merely because it improves historical backtest performance.

A proposed feature or strategy must demonstrate:

1. Economic or behavioural rationale.
2. Relevant literature or clearly documented research hypothesis.
3. Statistical evidence.
4. Out-of-sample robustness.
5. Economic significance.
6. Practical feasibility.

---

## 12. Change Control

Changes to the core research question, target variable, validation methodology or training/validation periods must be documented.

Changes made after observing results must be explicitly identified.

No research conclusion may be retroactively changed solely to improve apparent performance.

---

## 13. Status

This charter represents Atlas Research Charter v1.0.

Changes will be versioned and recorded in the project decision log.
