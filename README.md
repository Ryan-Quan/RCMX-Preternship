# RCM-X Preternship Project
#### Preternship Software Engineers: Jack Flaherty, Blake Kusky, Ryan Quan, Jack Schlehr
#### Preternship Project Manager: Kevan O'Brien
#### Preternship Mentor: Nathaniel Pawelczyk
Capstone project for CSE 20312 (Data Structures)
 
## Program
Developed algorithmic trading strategies based on technical indicators and backtesting framework for equities trading:
  * Strategy 1 (VWAP Cross): Long position when the VWAP rises above the price and short position when the VWAP falls below the price​
  * Strategy 2 (VWAP Mean Reversion): Long position when the price moves a certain percentage (1%) away from the VWAP​
  * Strategy 3 (Exponential Moving Averages): Long when the fast moving average rises above the slow moving and short the other way​
  * Strategy 4 (VWAP-TWAP Cross): Similar to the first strategy, but incorporates the TWAP into strategy​
  
## Resources Used:
  * Alpha-Vantage API (https://www.alphavantage.co/)
  * Jupyter Notebook (https://jupyter.org/)
  * Pandas/NumPy (https://pandas.pydata.org/)
  * mplfinance module (https://github.com/matplotlib/mplfinance)
