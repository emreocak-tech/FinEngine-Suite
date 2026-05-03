Link : https://finengine-suite-hb699kmjsdff6wxpvcrgvd.streamlit.app/

📈 Financial Calculator & Analysis Tool
This project is a comprehensive Streamlit application that combines core financial calculations, stock market analysis, real-time exchange rates, and AI-powered insights (Quant Trader simulation).

🚀 Features
The application is organized into four main modules:

1. Financial Calculations
Basic Interest: Calculate returns based on principal and rate.

Compound Interest: Analyze cumulative growth over a specific period.

Dividend Calculator: A simulation to check if your dividend income can cover a specific monthly target (e.g., minimum wage).

2. Valuation Tools (NPV & Stock Valuation)
Present Value (PV): Determine the current value of future money based on inflation/discount rates.

Investment Analysis: A "Profit for Me" tool to evaluate if a future value justifies the current investment cost.

Terminal Value: Calculate the perpetual growth value used in business valuations.

Intrinsic Stock Valuation: Estimate a stock's fair value per share using Free Cash Flow (FCF) projections and growth rates.

3. Stock Market Analysis
Live Data: Integration with yfinance to fetch data for tickers like AAPL, ASELS.IS, THYAO.IS, and GM.

Visualization: Interactive price charts for selected date ranges.

Comparison: Compare the performance of up to three different stocks on a single graph.

Financial Ratios: Track critical metrics including Sector, P/E Ratio, Forward P/E, and Beta.

4. AI & Utility Tools
5. Gemini AI Integration: Powered by Google Gemini (3-Flash), acting as a "Quant Trader" to explain concepts and answer financial queries.

Currency Exchange: Real-time USD/TRY parity tracking via Exchange Rate API.
6. 🛠️ Tech Stack
Python 3.11

Streamlit: For the web interface.

Google GenAI: For Gemini AI integration.

yfinance: For fetching historical and real-time market data.

Matplotlib: For data visualization and charting.

Requests: For handling API calls.

Dotenv: For secure API key management.

📂 Project Structure
ui.py: The main Streamlit interface and application logic.

calculations.py: Logic for interest and NPV-based calculations.

gemini.py: Integration for Google Gemini AI and Exchange Rate API.

stock_market.py: Classes for fetching stock data and generating visualizations.

⚠️ Disclaimer
The calculations and AI-generated responses provided by this app are for informational purposes only. This is not financial advice (YTD). Always consult with a professional advisor before making investment decisions.
Gemini AI Integration: Powered by Google Gemini (3-Flash), acting as a "Quant Trader" to explain concepts and answer financial queries.

Currency Exchange: Real-time USD/TRY parity tracking via Exchange Rate API.
