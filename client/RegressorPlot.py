
import streamlit as st
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
def regressor(aggregated_df):
    fig = px.line(aggregated_df, x='dates', y='price', title=f'Expenses for Selected Period')

    # Add regression line for next month
    if len(aggregated_df) > 1:
        # Extract features and target variable
        X = aggregated_df['dates'].apply(lambda x: x.toordinal()).values.reshape(-1, 1)
        y = aggregated_df['price'].values

        # Fit polynomial regression model
        degree = 5  # Degree of polynomial (linear regression)
        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(X, y)

        # Generate dates for next month
        next_month_dates = pd.date_range(aggregated_df['dates'].iloc[-1], periods=30, freq='D')[1:]

        # Predict prices for next month
        next_month_dates_ordinal = next_month_dates.to_series().apply(lambda x: x.toordinal()).values.reshape(-1, 1)
    
        next_month_prices = model.predict(next_month_dates_ordinal)

        # Add prediction line to the plot
        fig.add_scatter(x=aggregated_df['dates'], y=aggregated_df['price'], mode='lines', name='Original', line=dict(color='blue'))
        fig.add_scatter(x=next_month_dates, y=next_month_prices, mode='lines', name='Prediction', line=dict(color='green'))
    
# Display plot
    st.plotly_chart(fig, use_container_width=True)