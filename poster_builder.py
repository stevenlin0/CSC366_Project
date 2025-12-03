from __future__ import annotations

import textwrap

from pathlib import Path

from typing import Dict, List

import matplotlib.image as mpimg

import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

from poster_analysis import SummaryStats, compute_summary, load_and_clean

BASE_DIR = Path(__file__).parent

OUTPUT_PATH = BASE_DIR / "output" / "mlb_poster.png"

FIG_DIR = BASE_DIR / "output" / "figures"

def _wrap(text: str, width: int) -> str:

    return "\n".join(textwrap.wrap(text, width, break_long_words=False))

def _text_panel(

    fig: plt.Figure,

    position: List[float],

    title: str,

    lines: List[str],

    title_size: int = 18,

    body_size: int = 13,

) -> None:

    ax = fig.add_axes(position)

    ax.axis("off")

    ax.set_facecolor("white")

    rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, fill=True, edgecolor="#0b345d", linewidth=2, facecolor="white")

    ax.add_patch(rect)

    ax.text(0.02, 0.94, title, fontsize=title_size, fontweight="bold", color="#0b345d", va="top", transform=ax.transAxes)

    y = 0.85

    for line in lines:

        wrapped = _wrap(line, 55)

        ax.text(0.02, y, wrapped, fontsize=body_size, color="#111", va="top", transform=ax.transAxes)

        y -= 0.1

def _stats_table(fig: plt.Figure, position: List[float], stats: Dict[str, SummaryStats]) -> None:

    ax = fig.add_axes(position)

    ax.axis("off")

    ax.set_facecolor("white")

    rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, fill=True, edgecolor="#0b345d", linewidth=2, facecolor="white")

    ax.add_patch(rect)

    ax.text(0.02, 0.93, "Descriptive Statistics", fontsize=18, fontweight="bold", color="#0b345d", va="top")

    columns = ["Segment", "Corr", "Mean AAV", "Mean WAR", "Mean $/WAR", "Mean Δ ($M)"]

    rows = []

    for label in ["Overall", "Hitter", "Pitcher"]:

        stat = stats[label]

        rows.append(

            [

                label,

                f"{stat.corr:.2f}",

                f"{stat.mean_aav:.1f}",

                f"{stat.mean_war:.1f}",

                f"{stat.salary_per_war:.1f}",

                f"{stat.mean_value_delta:.1f}",

            ]

        )

    table = ax.table(cellText=rows, colLabels=columns, cellLoc="center", loc="center", colColours=["#edf2fb"] * len(columns))

    table.auto_set_font_size(False)

    table.set_fontsize(12)

    table.scale(1, 1.4)

def _image_panel(fig: plt.Figure, position: List[float], image_path: Path, caption: str) -> None:

    ax = fig.add_axes(position)

    ax.axis("off")

    rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, fill=True, edgecolor="#0b345d", linewidth=2, facecolor="white")

    ax.add_patch(rect)

    if image_path.exists():

        img = mpimg.imread(image_path)

        ax.imshow(img, extent=(0.02, 0.98, 0.2, 0.95))

    ax.text(0.02, 0.08, caption, fontsize=12, color="#111")

def build_poster() -> None:

    df = load_and_clean()

    stats = compute_summary(df)

    fig = plt.figure(figsize=(28, 16), dpi=200)

    fig.patch.set_facecolor("#eef2fb")

    banner = fig.add_axes([0.02, 0.9, 0.96, 0.08])

    banner.axis("off")

    banner.set_facecolor("#0b345d")

    banner.text(

        0.01,

        0.55,

        "Do Higher Salaries Predict Better MLB Player Performance (2005–2025)?",

        fontsize=28,

        fontweight="bold",

        color="white",

        va="center",

    )

    banner.text(

        0.01,

        0.12,

        "Students A & B | Data: Baseball-Reference, FanGraphs, Spotrac-style contracts",

        fontsize=16,

        color="white",

    )

    _text_panel(

        fig,

        [0.02, 0.72, 0.29, 0.15],

        "Abstract",

        [

            "Analysis of 28 veteran long-term contracts indicates only a moderate salary-to-WAR correlation "

            "(r = 0.40). Hitters show tighter alignment (r = 0.64) than pitchers (r = 0.25). Valuing WAR at "

            "$8M reveals that around half the deals generate positive surplus.",

        ],

    )

    _text_panel(

        fig,

        [0.02, 0.52, 0.29, 0.18],

        "Literature Snapshot",

        [

            "Taylor (2016) documented post-contract declines before the analytics boom, emphasizing WAR.",

            "Turvey (2013) described the economic drivers behind mega-deals and late-year overpayment.",

            "O'Neill (2014) found contract-year performance bumps, leaving post-signing outcomes unresolved.",

            "Gap: modern comparison of hitter vs pitcher long-term value.",

        ],

    )

    _text_panel(

        fig,

        [0.02, 0.32, 0.29, 0.18],

        "Data Cleaning & Features",

        [

            "Merged Baseball-Reference/FanGraphs stats with contract data (`all_mlb_data.csv`).",

            "Removed blank rows, coerced numeric fields, parsed contract start/end years, inferred player type.",

            "Derived Salary per WAR (for WAR>0), Market Value = WAR×$8M, Surplus = Market Value − AAV.",

        ],

    )

    _text_panel(

        fig,

        [0.02, 0.12, 0.29, 0.18],

        "Methods & Variables",

        [

            "Independent variable: Average Annual Value (million USD).",

            "Dependent metrics: cumulative WAR, OPS+/wRC+ for hitters, ERA-like run prevention for pitchers.",

            "Statistical tools: Pearson correlations, descriptive stats, and the visuals generated in `poster_analysis.py`.",

        ],

    )

    _text_panel(

        fig,

        [0.34, 0.63, 0.29, 0.24],

        "Exploratory Insights",

        [

            "Salary vs WAR scatter indicates diminishing returns above ~$30M AAV for pitchers.",

            "Pitcher salary-per-WAR variance is much wider, signaling injury and volatility risk.",

            "Timeline shows rapid AAV growth post-2015 without proportional WAR increases.",

        ],

    )

    _stats_table(fig, [0.34, 0.35, 0.29, 0.24], stats)

    _text_panel(

        fig,

        [0.34, 0.12, 0.29, 0.2],

        "Key Findings",

        [

            "Top Surplus: Max Scherzer (+$178M), Freddie Freeman (+$152M), Marcus Semien (+$113M).",

            "Negative Surplus: Pablo Sandoval (−$29M), Yasmany Tomas (−$15M), James Shields (−$11M), Jacob deGrom (−$10M).",

            "Only ~54% of sampled contracts produced positive surplus at the $8M per WAR benchmark.",

        ],

    )

    _image_panel(

        fig,

        [0.66, 0.58, 0.32, 0.32],

        FIG_DIR / "salary_vs_war.png",

        "Figure 1. Salary vs WAR with regression line; hitters (blue) track closer than pitchers (orange).",

    )

    _image_panel(

        fig,

        [0.66, 0.2, 0.32, 0.32],

        FIG_DIR / "contract_trend.png",

        "Figure 2. Contract AAV escalation since 2005; WAR remains clustered, implying scarcity premiums.",

    )

    _text_panel(

        fig,

        [0.66, 0.12, 0.32, 0.12],

        "Conclusions & Future Work",

        [

            "Higher salaries only moderately predict WAR; hitters retain value longer than pitchers.",

            "Pitcher deals should incorporate opt-outs or escalators to hedge injuries.",

            "Next steps: add arbitration deals, compare WAR models, integrate injury/aging regressions.",

            "References: Taylor (2016); Turvey (2013); O'Neill (2014).",

        ],

    )

    _text_panel(

        fig,

        [0.66, 0.05, 0.32, 0.06],

        "Visual Storytelling",

        ["See also Figure 3 (salary efficiency) highlighting pitcher variance in $ per WAR."],

        title_size=16,

        body_size=12,

    )

    fig.savefig(OUTPUT_PATH, dpi=200, bbox_inches="tight")

    plt.close(fig)

if __name__ == "__main__":

    build_poster()
