# Do Higher Salaries Predict Better MLB Player Performance in the Last 20 Years?

Vincent Bonamassa, Steven Lin, Aamina Mokhtar

---

## INTRODUCTION

MLB clubs spend billions on guaranteed deals expecting elite performance, yet aging curves, injuries, and role-specific volatility can break the link between pay and production. Taylor (2016) documented post-contract performance declines and aging effects for long-term deals, establishing WAR as a core evaluation metric but stopped at 2015 and did not compare WAR models. Turvey (2013) explained why teams embraced long contracts—front-loading competitive advantage while tolerating inefficiency later—but did not test whether value was realized. O'Neill (2014) found evidence of "contract-year bumps" in hitter performance, suggesting motivation spikes before payday yet leaving open whether production persists afterward.
Our project updates contract-performance analysis for the 2005–2025 window, compares hitter/pitcher dynamics, and quantifies surplus value using the commonly cited $8M-per-WAR benchmark. We only focused on players who have long term contracts. We did not calculate players currently under arbitration or making rookie salary.

---

## ABSTRACT

We evaluate whether guaranteed long-term contracts in Major League Baseball (MLB) translate into on-field production that justifies their cost. Using a curated sample of 28 prominent multi-year deals signed between 2005 and 2025, we pair Baseball-Reference/FanGraphs performance data with contract terms (Average Annual Value, AAV). After cleaning the dataset (removing blank rows, coercing numeric fields, and tagging hitters vs. pitchers), we examine the salary-to-performance relationship using WAR-based efficiency metrics, Pearson correlations, and visual analytics. Results show only a moderate overall correlation (r = 0.40), with hitters exhibiting a tighter salary-performance fit (r = 0.64) than pitchers (r = 0.25). Translating WAR into market value (1 WAR ≈ $8M) reveals that only about half of the sampled contracts generated positive surplus, highlighting the risk embedded in pitcher investments. These findings help teams contextualize how modern mega-deals age during the analytics era.

---

## FEATURE SELECTION

**Independent Variable:**  
Contract cost measured by Average Annual Value (inflation effects minimized by focusing on 2005–2025

**Dependent Variables:**  
Cumulative WAR during the contract window; hitter slash-line metrics (AVG/OBP/SLG/OPS, wRC+) and pitcher run-prevention proxies embedded in the dataset.

**Procedure:**  
After cleaning, we segmented hitters vs. pitchers, computed summary stats, and ran Pearson correlations between WAR and AAV. Salary efficiency and surplus metrics were derived to contextualize value. Visuals (scatter, box plot, timeline) were produced via poster_analysis.py.

---

## MODELS USED / FINDINGS

We were able to scrape our data from the internet. There is a program out there called pybaseball that we installed with pip and it automatically scrapes from a website called Fangraphs, which has descriptive data of all relevant statistics, including WAR which is our main focus to determine contract value.

| Corr(AAV, WAR) | Mean AAV (M)|MeanWAR|Mean/WAR | Mean Surplus ($M) |

| Overall | 0.40 | 19.4 | 9.0 | 3.6 | +52.5 |

| Hitters | 0.64 | 19.7 | 10.5 | 2.2 | +64.3 |

| Pitchers | 0.25 | 19.2 | 7.6 | 4.7 | +41.5 |

Top Surplus Deals: Max Scherzer (2015–18), Freddie Freeman (2022–25), Marcus Semien (2022–25).

Negative Surplus Deals: Pablo Sandoval (2015–18), Yasmany Tomas (2015–18), James Shields (2015–18), Jacob deGrom (2023–25 expected shortfall due to injuries).

Insight: Even when overall surplus is positive, the risk profile diverges sharply by position—pitcher variance and health setbacks erode value faster than hitter aging.

---

## CONCLUSIONS

Higher salaries do not guarantee proportionally higher WAR. The moderate correlation and numerous underperforming contracts suggest teams often overpay for projected, not realized, production.

Hitters with strong on-base skills maintain value deeper into contracts, supporting the strategy of investing in defensive/plate-discipline profiles.

Pitcher deals require built-in risk mitigation (opt-outs, staggered payments) given the low correlation and high dispersion in $/WAR.

---

## FUTURE DIRECTIONS

Expand the dataset to include shorter deals and arbitration outcomes to test whether team-controlled years subsidize long-term investments.

Compare Baseball Reference vs. FanGraphs WAR to quantify model sensitivity.

Incorporate injury days lost and aging-curve modeling (e.g., spline regression) to predict when surplus flips negative.

---

## REFERENCES

Taylor, Z. (2016). An Analysis of the Effects of Long-Term Contracts on Performance in Major League Baseball (Doctoral dissertation).

Turvey, J. (2013). "The future of baseball contracts: a look at the growing trend in long-term contracts." Baseball Research Journal, 42(2), 101+.

O'Neill, H. (2014). "Do Major League Baseball hitters come up big in their contract year?" SABR Research Journal.
