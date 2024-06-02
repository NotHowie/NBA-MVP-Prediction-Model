Every April, as the NBA season comes to a close, a monumental debate ensues. Analysts, writers, and fans across the globe engage in heated discussions over which player deserves to be crowned the Most Valuable Player (MVP). This prestigious honor is awarded by a panel of sportswriters and broadcasters who rank their picks for the MVP from first to fifth. The player with the highest point total is bestowed with the award. However, the MVP voting process can sometimes be influenced by popular narratives rather than purely on-court performance.

In this project, I aimed to explore the statistical factors that determine the NBA MVP and create a linear regression model to predict who should have won each year.

Data Collection
The data was meticulously collected from basketball-reference.com, including all players who received MVP votes and their season averages. Additional columns for advanced statistics like true shooting percentage (TS%) and Value Over Replacement Player (VORP) were included to enhance the analysis. The dataset was expanded to include new players based on their top regular season averages in various categories, ensuring a robust model. Ultimately, the dataset included features such as year, player name, share of MVP votes, player statistics, and advanced metrics.

Exploratory Data Analysis (EDA)
In the EDA phase, I explored how different variables related to MVP vote shares. Key findings from the correlation mapping showed that VORP, Win Shares (WS), and WS/48 had the highest positive correlations with MVP vote share, while seed also played a significant role.

Model Creation
I chose a linear regression model to predict MVP vote shares due to its effectiveness in modeling relationships between player statistics and vote shares. The model allowed for the identification of key features influencing MVP voting. Categorical variables like player position and seed were encoded, and the dataset was split into training and testing sets. The Mean Squared Error (MSE) was used to evaluate model accuracy, with an MSE of 0.04 indicating good performance.

Findings
The analysis of feature importance revealed that Field Goal Percentage (FG%) was the most significant predictor of MVP voting share, followed by seed and three-point percentage. Defensive contributions, represented by steals, also played an important role. Interestingly, true shooting percentage (TS%) and free throw percentage had negative importance coefficients, suggesting that other metrics might be more influential in predicting MVP vote share.

Key Differences in Predictions
For seven out of the 20 years in the dataset, the model predicted a different MVP winner than the actual choice. Notable differences included the 2010-2011 and 2022-2023 seasons, which remain debated today. If the model were assigning the shares, LeBron James would have won 7 MVPs and Nikola Jokić 4. The model's preference for players like Jokić and James reflects their superior advanced statistics.

Conclusion
The discrepancies between my model's predictions and the actual MVP winners highlight the complexity and subjectivity of NBA MVP voting. While the model relies on statistical data, narratives, records, and biases also play a crucial role in the final decision. This analysis provides valuable insights into the statistical factors considered in MVP voting alongside these other elements.
