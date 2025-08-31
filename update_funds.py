import json
import random # Using random to simulate data changes

# In a real-world script, you would use libraries like
# requests and BeautifulSoup to scrape websites for this data.
def get_latest_uti_nifty_50_data():
    # --- WEB SCRAPING LOGIC WOULD GO HERE ---
    # For this example, we'll just simulate a change.
    new_cagr = round(14.8 + random.uniform(-0.5, 0.5), 2)
    return {
        "name": "UTI Nifty 50 Index Fund",
        "fiveYearReturnCAGR": new_cagr,
        "expenseRatio": 0.20,
        "deepLinkUri": "groww.in/mutual-funds/uti-nifty-50-index-fund-direct-growth"
    }

# 1. Read the existing JSON file
with open('fund_data.json', 'r') as f:
    data = json.load(f)

# 2. Update the data with new values from our scraper function
# (Here we only update one fund for the example)
data['funds']['nifty50'][0] = get_latest_uti_nifty_50_data()

# 3. Write the updated data back to the file
with open('fund_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("fund_data.json has been updated successfully.")
