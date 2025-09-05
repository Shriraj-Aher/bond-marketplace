import streamlit as st
import pandas as pd
import math

# ------------------------------
# Load and clean data
# ------------------------------
file_path = "/Users/shrirajaher/SEBIhack/proto3/bond-marketplace/pages/data.csv"
df = pd.read_csv(file_path)

# Clean messy column names
df.columns = df.columns.str.strip().str.replace("\n", "", regex=True)

# Keep only useful columns
df = df[[
    "ISIN",
    "DESCRIPTOR",
    "WEIGHTED AVERAGE PRICE",
    "LAST TRADE PRICE",
    "WEIGHTED  AVERAGE YIELD (YTM) (%)",
    "LAST  TRADE YIELD  (Annualized) (%)",
    "VALUE  (₹ Crores)",
    "NO. OF TRADES"
]]

# Rename columns for readability
df = df.rename(columns={
    "DESCRIPTOR": "Company / Bond",
    "WEIGHTED AVERAGE PRICE": "Weighted Avg Price",
    "LAST TRADE PRICE": "Last Trade Price",
    "WEIGHTED  AVERAGE YIELD (YTM) (%)": "Yield (YTM) %",
    "LAST  TRADE YIELD  (Annualized) (%)": "Yield (Annualized) %",
    "VALUE  (₹ Crores)": "Trade Value (₹ Cr)",
    "NO. OF TRADES": "Number of Trades"
})

# ------------------------------
# Add Annual Report URL column (placeholder mapping)
# ------------------------------
report_urls = {
    "SUNDARAM FINANCE LIMITED": "https://www.sundaramfinance.in/annual-report.pdf",
    "TOYOTA FINANCIAL SERVICES INDIA LIMITED": "https://www.toyotafinancial.co.in/annual-report.pdf",
    "POWER FINANCE CORPORATION LIMITED": "https://www.pfcindia.com/annual-report.pdf",
    "GMR AIRPORTS LIMITED": "https://www.gmrgroup.in/annual-report.pdf",
    # 👉 Add more mappings here
}

df["Annual Report URL"] = df["Company / Bond"].apply(
    lambda x: next((url for company, url in report_urls.items() if company.lower() in str(x).lower()), "Not Available")
)

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="Corporate Bond Market", layout="wide")
st.title("📊 Corporate Bond Market Dashboard")
st.markdown("Browse OTC corporate bond trades and download issuer reports.")

# Pagination setup
rows_per_page = 10
total_pages = math.ceil(len(df) / rows_per_page)
page = st.number_input("Page", min_value=1, max_value=total_pages, step=1)

# Slice data for current page
start = (page - 1) * rows_per_page
end = start + rows_per_page
page_df = df.iloc[start:end].copy()

# Make URLs clickable in Streamlit dataframe
page_df["Annual Report URL"] = page_df["Annual Report URL"].apply(
    lambda x: f"[Download Report]({x})" if x != "Not Available" else "Not Available"
)

# Display table with Annual Report column
st.dataframe(page_df, use_container_width=True)
