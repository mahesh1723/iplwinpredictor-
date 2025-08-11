 IPL Win Prediction (2008–2019)
📌 Project Overview
This project predicts the probability of winning for a team in an IPL match (2008–2019) in percentage based on match situation such as batting team, bowling team, runs left, balls left, wickets remaining, and required run rate.

The prediction helps fans, analysts, and commentators understand which team has the upper hand in real-time match scenarios.

🎯 Objective
To build a machine learning model and a Streamlit web application that:

Takes live match data as input.

Predicts the winning probability for both teams.

Outputs a clear percentage score for decision-making.

📂 Dataset
Source: IPL ball-by-ball dataset (2008–2019).

Key Features Used:

batting_team

bowling_team

city (venue)

runs_left

balls_left

wickets

total_runs_x (target)

crr (Current Run Rate)

rrr (Required Run Rate)

🔍 Approach
Data Preprocessing

Removed unnecessary columns.

Handled missing values.

Converted categorical variables using One-Hot Encoding.

Created match context features (runs_left, balls_left, crr, rrr).

Train-Test Split


Model Training

Logistic Regression (Baseline)


Model Evaluation

Accuracy Score


Developed an interactive Streamlit web application to:

Take user input for current match situation.

Predict live winning probabilities for both teams.

Display results in a visually appealing format.

🛠 Tech Stack
Language: Python

Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit

Deployment: Streamlit

📊 Sample Prediction
Match: Kolkata Knight Riders 🆚 Delhi Daredevils (2018, Match 13)
Predicted Score:

KKR Win Probability: 68%

Delhi Win Probability: 32%
