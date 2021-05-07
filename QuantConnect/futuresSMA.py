from datetime import timedelta
import decimal as d
import numpy as np


class futures(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 3, 1)
        self.SetEndDate(2017, 9, 21)
        self.SetCash(100000)
        self.IsUpTrend = False
        self.IsDownTrend = False

        # Adds SPY
        self.symbol = "SPY"
        equity = self.AddEquity(self.symbol, Resolution.Daily)
        
        #25 day moving average
        self.fastSMA = self.SMA(equity.Symbol, 25, Resolution.Daily)
        #50 day moving average 
        self.slowSMA = self.SMA(equity.Symbol, 50, Resolution.Daily)

        # Adds the future that will be traded and
        # set our expiry filter for this futures chain
        future = self.AddFuture(Futures.Indices.SP500EMini)
        future.SetFilter(timedelta(0), timedelta(182))


    def OnData(self, slice):
        if not self.slowSMA.IsReady: return
    
        if not self.Portfolio.Invested and self.fastSMA > self.slowSMA:
            for chain in slice.FuturesChains:
                contracts = None
                # find the front contract expiring no earlier than in 90 days
                contracts = filter(lambda x: x.Expiry > self.Time + timedelta(90), chain.Value)
                # if there is any contract, trade the front contract
                #if len(contracts) == 0: continue
                contract = sorted(contracts, key = lambda x: x.Expiry, reverse=True)[0]
                self.MarketOrder(contract.Symbol , 1)
        else:
            self.Liquidate()

    def OnOrderEvent(self, orderEvent):
        self.Log(str(orderEvent))
