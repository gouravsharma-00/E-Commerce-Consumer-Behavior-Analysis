import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./ECommerce_consumer behaviour.csv")
# Streamlit App
st.title("E-commerce Sales Analysis Dashboard")

# Show the dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Handle missing values
df['days_since_prior_order'] = df['days_since_prior_order'].fillna(0).astype(int)

# Analysis: Number of Purchases by Day
st.subheader("Number of Purchases by Day")
fig1, ax1 = plt.subplots(figsize=(6, 6))
df.groupby('order_dow')['user_id'].agg(['count']).sort_values(by='count', ascending=False).plot(
    kind='pie', autopct='%1.2f%%', subplots=True, title='Number of Purchases by Day', ax=ax1
)
st.pyplot(fig1)

# Analysis: Orders by Time of Day
st.subheader("Orders by Time of Day")
def order_time(hour):
    if hour in [6, 7, 8, 9, 10, 11, 12]:
        return 'Morning'
    elif hour in [13, 14, 15, 16, 17]:
        return 'Afternoon'
    elif hour in [18, 19, 20, 21, 22]:
        return 'Evening'
    else:
        return 'Night'

df['order_time_list'] = df['order_hour_of_day'].apply(order_time)

fig2, ax2 = plt.subplots(figsize=(6, 6))
df.groupby('order_time_list')['user_id'].agg(['count']).sort_values(by='count', ascending=False).plot(
    kind='bar', title='Orders by Time of Day', ax=ax2
)
st.pyplot(fig2)

# Analysis: Orders by Day and Time
st.subheader("Orders by Day and Time")
pivot_data = df.pivot_table(index='order_dow', columns='order_time_list', values='user_id', aggfunc='count')
fig3, ax3 = plt.subplots(figsize=(8, 6))
pivot_data.plot(kind='bar', ax=ax3, title="Orders by Day and Time of Day")
st.pyplot(fig3)

# Analysis: Number of Orders per User
st.subheader("Number of Orders per User")
def order_number_group(x):
    if x <= 20:
        return '1-20 orders'
    elif x <= 40:
        return '21-40 orders'
    elif x <= 60:
        return '41-60 orders'
    elif x <= 80:
        return '61-80 orders'
    else:
        return '81-100 orders'

df['order_number_group'] = df['order_number'].apply(order_number_group)
fig4, ax4 = plt.subplots(figsize=(6, 6))
df.groupby('order_number_group')['user_id'].agg(['count']).sort_values(by='count', ascending=False).plot(
    kind='pie', autopct='%1.3f%%', subplots=True, title='Number of Orders per User', ax=ax4
)
st.pyplot(fig4)

# Analysis: Days Since Prior Order
st.subheader("Days Since Prior Order")
fig5, ax5 = plt.subplots(figsize=(8, 6))
df.groupby('days_since_prior_order')['user_id'].agg('count').sort_values(ascending=False).plot(
    kind='bar', title='Days Since Prior Order', ax=ax5
)
st.pyplot(fig5)

# Analysis: Top 15 Products
st.subheader("Top 15 Products")
fig6, ax6 = plt.subplots(figsize=(6, 6))
df.groupby('product_name')['user_id'].agg(['count']).sort_values(by='count', ascending=False).head(15).plot(
    kind='pie', autopct='%1.2f%%', subplots=True, title='Top 15 Products', ax=ax6
)
st.pyplot(fig6)

# Hypotheses Section
st.subheader("Hypotheses")
st.markdown("""
1. Most purchases are made during specific days of the week and times of the day.
2. Users tend to order more frequently during the morning and evening hours.
3. The majority of users make less than 20 orders, indicating occasional buyers dominate.
4. Certain products have consistent popularity, accounting for a significant portion of sales.
5. Short intervals between orders might indicate loyalty or frequent shopping habits.
""")

st.subheader("Dataset After view")
st.write(df.head())