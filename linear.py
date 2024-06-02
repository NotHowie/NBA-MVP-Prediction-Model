import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df = pd.read_excel("updated_dataset.xlsx")
df = pd.get_dummies(df, columns=['Position', 'Seed'])
df['Year'] = df['Year'].astype(str)


features = df.drop(columns=['Player', 'Year', 'MVP_Won', 'Consecutive MVP', 'Total MVP', 'Team', 'WS/48', 'Share'])
target = df['Share']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

feature_importance = pd.DataFrame({
    'Feature': features.columns,
    'Importance': linear_model.coef_
})


feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

print("Feature Importance:\n", feature_importance)


df['Predicted Share'] = linear_model.predict(features)
predicted_mvp = df.loc[df.groupby('Year')['Predicted Share'].idxmax()]
actual_mvp = df[df['MVP_Won'] == 1]
comparison_df = actual_mvp[['Year', 'Player', 'Share']].merge(
    predicted_mvp[['Year', 'Player', 'Predicted Share']],
    on='Year', suffixes=('_Actual', '_Predicted')
)


mse = mean_squared_error(y_test, linear_model.predict(X_test))
print(f"Mean Squared Error of the Linear Regression model: {mse:.2f}")

print(comparison_df)
