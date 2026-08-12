# Atlas Data Dictionary

## Purpose

This document defines the initial datasets required by Atlas.

Definitions will become more detailed as actual datasets are acquired.

---

## Market Data

| Variable | Definition | Frequency | Initial Source |
|---|---|---|---|
| Open | Daily opening price | Daily | Public market data |
| High | Daily high price | Daily | Public market data |
| Low | Daily low price | Daily | Public market data |
| Close | Daily closing price | Daily | Public market data |
| Adjusted Close | Corporate-action-adjusted closing price where available | Daily | Public market data |
| Volume | Daily traded volume | Daily | Public market data |

---

## Fundamental Data

| Variable | Definition | Frequency |
|---|---|---|
| Revenue | Reported revenue | Quarterly/Annual |
| Net Income | Reported net income | Quarterly/Annual |
| EPS | Earnings per share | Quarterly/Annual |
| ROE | Return on equity | Quarterly/Annual |
| ROCE | Return on capital employed | Quarterly/Annual |
| Operating Margin | Operating profit relative to revenue | Quarterly/Annual |
| Free Cash Flow | Cash available after operating and capital expenditure | Quarterly/Annual |
| Debt | Relevant debt measure | Quarterly/Annual |
| Book Value | Accounting book value | Quarterly/Annual |
| PE | Price-to-earnings ratio | Point-in-time |
| PB | Price-to-book ratio | Point-in-time |

---

## Technical Features

These will generally be derived from market data.

Examples:

- 5-day momentum
- 20-day momentum
- 60-day momentum
- RSI
- Moving-average distance
- Moving-average crossover
- Volatility
- ATR
- Volume ratio
- Relative strength

---

## Macro Data

Initial candidates:

- RBI policy rate
- CPI inflation
- USD/INR
- Brent crude
- India 10-year government bond yield
- GDP growth
- India VIX

---

## Market Participation

Initial candidates:

- FII net flows
- DII net flows
- Institutional ownership
- Promoter ownership
- Changes in institutional ownership

---

## Data Quality Requirements

Every dataset should document:

1. Source
2. Collection date
3. Frequency
4. Units
5. Missing-value treatment
6. Corporate-action treatment
7. Revision policy
8. Point-in-time availability
9. Known limitations

---

## Point-in-Time Principle

A variable may only be used in a historical prediction if the information would actually have been available to an investor at that point in time.

This is a critical requirement for avoiding look-ahead bias.
