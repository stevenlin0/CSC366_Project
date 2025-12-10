# MLB Long-Term Contracts Research Project

## Research Question

We are researching the question of Major League Baseball contracts and how well they result. We use a bunch of commonly used statistics to determine whether long term contracts are generally a good idea or a bad idea. We did not look at rookie contracts or players that were in arbitration because there is no standardized AAV for arbitration and for rookies, they make the league minimum.

Of course, we are not the first ones to look at this topic.

## Resources

### [1] Taylor, Z. (2016). An Analysis of the Effects of Long-Term Contracts on Performance in Major League Baseball (Doctoral dissertation).

Taylor's dissertation focuses specifically on how MLB players perform after signing long-term contracts, which makes it highly relevant to our topic. Her work pulls together multiple years of contract and performance data, looking at how guaranteed money and contract length relate to player motivation and output. She examines patterns such as whether players tend to decline once they obtain financial security or whether certain types of players remain productive across longer time spans. The study uses WAR (Wins Above Replacement), batting performance measures, and pitching metrics to evaluate the trends.

One of the most notable parts of Taylor's analysis is her focus on player aging curves. She observes that many players experience decline as they move into the later years of their careers, which often overlaps with the later years of long-term contracts. This finding aligns with common expectations in baseball economics but also shows how performance changes can vary depending on the player's role or position. While the study identifies drop-offs, Taylor also points out exceptions: certain elite players outperform expectations even deep into long-term deals, suggesting that the relationship is more nuanced than just "contracts cause declines."

Although Taylor's work is valuable, it also has limitations that matter for our project. Her study ends at 2015, meaning it predates the analytics boom that transformed how teams measure performance. She also uses WAR but does not compare different WAR systems like Baseball-Reference vs. Fangraphs, which is something we plan to explore. Her dissertation provides a strong foundation, but there is still room to update and expand the research using modern data and metrics.

### [2] Turvey, J. (2013). The future of baseball contracts: a look at the growing trend in long-term contracts. The Baseball Research Journal, 42(2), 101+.

Turvey's article provides important context about how MLB long-term contracts evolved over time. Instead of focusing solely on performance, he looks at economic and structural trends within the sport. He explains why teams increasingly began offering longer contracts, how average annual value (AAV) expanded over the years, and what financial risks and benefits teams consider when negotiating these deals. His analysis helps explain the environment that created the types of contracts we are studying.

Turvey also highlights how free agency and team budgeting strategies changed in the early 2010s. For example, teams became more willing to "overpay" in later years of a contract as long as they could get high performance during the early seasons. This is important for our research because it suggests that long-term deals are not only about matching salary to performance, but they are also about timing and strategic roster building. Teams often knowingly accept inefficiency at the back end of a contract in exchange for stability or competitive edge at the front.

However, Turvey's paper remains mostly descriptive. He does not attempt to evaluate whether the players actually lived up to the projected value of their contracts. He does not use metrics like WAR, OPS+, ERA+, or salary-per-WAR ratios. His work gives a big-picture view of how long-term contracts became common, but it stops short of quantifying how well these contracts perform in practice. That gap is where our project steps in.

### [3] O'Neill, H. (2014). "Do Major League Baseball hitters come up big in their contract year?" SABR Research Journal.

O'Neill's study looks at player behavior right before a contract is signed, that being the "contract year." He analyzes whether hitters tend to increase their performance when they know they are about to enter free agency or negotiate a new deal. Using adjusted OPS metrics (OPS100), he finds that many hitters do show a modest increase in productivity during their contract year. This suggests that money can be a motivating factor and that players respond to financial incentives when they are on the verge of payday.

Another important contribution from O'Neill is how he controls for other factors that could affect contract-year performance. He accounts for playing time, aging, and retirement decisions, and he uses fixed-effects regression to isolate the contract-year effect. This strengthens the credibility of his results, making the paper a reliable source for understanding incentive-related performance patterns. His findings show that players can elevate their performance when their next contract is on the line.

Despite the strengths of this paper, it only examines performance before a contract is signed. It does not explore whether players maintain, exceed, or fall below expectations after signing a long-term deal. In fact, the contract-year bump that O'Neill documents could be interpreted as temporary, a burst of effort that may or may not carry over into the first or later years of a long commitment. This question remains open, and it supports the need for our project's focus on performance during long-term contracts rather than leading up to them.

## Existing Findings and Metrics We Can Build On

There are several findings from earlier research that give us a helpful starting point for our project. Taylor's study on long-term MLB contracts shows how performance can change over the years and highlights the importance of using metrics like WAR to evaluate value. Turvey's work explains how long-term contracts became more common and why teams started committing larger amounts of money to players. These two sources give us background on both the performance side and the economic side of MLB contracts, which makes it easier for us to understand the environment we're working with.

We also have reliable datasets available through Baseball-Reference and FanGraphs, which provide season-by-season statistics, salaries, and advanced metrics such as WAR, OPS+, and ERA+. These databases are widely used by analysts, journalists, and researchers, so they give us trustworthy numbers to build our analysis on. Since our project covers the last 20 years, these sources are particularly useful because they offer consistent, modern data that fits the metrics teams rely on today.

Altogether, the previous research and the data we have access to give us a solid foundation to build on. They point us toward which statistics matter most, how contracts are usually evaluated, and what trends have already been observed. This helps guide our project and makes sure we are focusing on questions that are relevant to understanding player value under long-term MLB contracts.

## Gaps/Open Questions Our Project Addresses

Even though previous studies give us a good foundation, there are still a few areas that haven't been explored in much detail and that our project is able to expand on. Most of the existing research focuses on older contract periods or broader economic trends, but there is less work that looks closely at the performance of players under long-term contracts in the modern analytics era. Because the game has changed a lot in the last 20 years, especially with how teams evaluate players, there is room to update these findings using more recent data and advanced metrics.

Another open question involves how consistent a player's value is throughout the entire length of a long-term contract. Past studies talk about contract-year motivation or early performance, but they don't really break down how performance changes from the first year to the last year of a deal. This makes it harder to tell whether teams are getting steady value or if most of the value comes early on. Our project also adds something new by comparing different versions of WAR from Baseball Reference and FanGraphs, since each uses its own method. Seeing how these two systems line up or differ gives us a clearer picture of how performance and salary relate.

Overall, the gaps that exist are not major problems but rather opportunities for us to bring the research up to date and look at contract performance in a way that fits how MLB operates today. Our dataset lets us answer these questions, and the metrics we're using help us get a more detailed understanding of contract value than what appears in most earlier studies.

