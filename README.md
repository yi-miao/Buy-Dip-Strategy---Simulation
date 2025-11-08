# Buy-Dip-Strategy---Simulation
A Python-based simulation that visualizes disciplined dip-buying strategies across multiple pullback scenarios. This project models geometric price drops and recoveries, calculates breakeven points, and annotates final portfolio values and returns — helping investors understand how strategic accumulation during dips can outperform passive holding.

## 🚀 Features

- Simulates price dips and recoveries using configurable angles and pullback percentages  
- Models fixed-share buying strategy from halfway down to bottom of dip  
- Calculates:
  - Average cost per share
  - Breakeven price
  - Final portfolio value
  - Return percentage
- Visualizes:
  - Price path geometry
  - Buy markers, breakeven, and final value
  - Annotated returns for each scenario

## 📊 Strategy Logic

- **Fixed shares per buy**: 1 share per buy across 10 buys  
- **Buy range**: halfway down to bottom of dip  
- **Final price**: assumed to recover to starting price  
- **Return**: based on difference between final price and average cost  

## 🧠 Why It Matters

This simulation shows how disciplined dip-buying can generate positive returns even when prices only recover to their original level — outperforming passive buy-and-hold strategies in volatile markets.

## 🛠️ Requirements

- Python 3.7+  
- `matplotlib`  
- `numpy`  

Install dependencies:
```bash
pip install matplotlib numpy

📌 Customization
You can tweak:
- pullback_percents: to simulate different dip depths
- num_buys: to adjust granularity
- drop_angle_deg and rise_angle_deg: to shape the price path
- Add overlays for volatility, partial recoveries, or historical data
