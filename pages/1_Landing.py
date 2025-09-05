import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Page setup
# ------------------------------
st.set_page_config(page_title="Corporate Bonds in India", layout="wide")
st.title("💹 Why Invest in Corporate Bonds?")
st.markdown("""
Corporate bonds are debt instruments issued by companies to raise funds.  
They offer **stable returns** with lower volatility than equities and can be an excellent way to **diversify your portfolio**.  

In India, investors often compare corporate bonds with traditional options like:
- **Fixed Deposits (FDs)** – Safe but low returns.  
- **Equities (Stocks)** – High growth but volatile.  
- **Gold** – Hedge against inflation but fluctuates.  
- **Government Bonds** – Safe but lower yields.  

Let's see how **corporate bonds have performed compared to these asset classes** over the past 5 years.
""")

# ------------------------------
# Dummy performance data (annualized returns over 5 years)
# Replace with real dataset if available
# ------------------------------
data = {
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Corporate Bonds": [7.2, 7.5, 7.8, 8.0, 7.6],
    "Nifty 50 (Equities)": [12.0, 24.0, -3.0, 18.0, 15.0],
    "Gold": [26.0, -4.0, 12.0, 6.0, 8.0],
    "Fixed Deposits": [6.5, 5.8, 5.5, 6.0, 6.2],
    "Govt Bonds": [6.8, 6.9, 7.1, 7.0, 7.2],
}
df = pd.DataFrame(data)

# ------------------------------
# Plot
# ------------------------------
fig, ax = plt.subplots(figsize=(10, 5))
for column in df.columns[1:]:
    ax.plot(df["Year"], df[column], marker="o", label=column)

ax.set_title("Performance of Corporate Bonds vs Other Investments in India")
ax.set_xlabel("Year")
ax.set_ylabel("Annual Returns (%)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# ------------------------------
# Convincing Section
# ------------------------------
st.markdown("""
### 📌 Why Corporate Bonds?
- ✅ **Stability**: Less volatile compared to equities.  
- ✅ **Better Returns than FD/Govt Bonds**: Often 1–2% higher than traditional safe investments.  
- ✅ **Diversification**: Helps balance risk when combined with equities and gold.  
- ✅ **Accessibility**: With platforms supporting **fractional ownership**, bonds are now open to retail investors.  

👉 **Takeaway:**  
Corporate bonds may not beat equities in bull markets, but they **reduce portfolio risk** and ensure **steady income**, making them an essential part of a diversified investment strategy in India.
""")
