"""Core functionality for OpenBB MVP."""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional
from openbb_mvp.models import HistoricalData, OBBResult


class PriceInterface:
    """Price data interface."""
    
    def historical(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> OBBResult:
        """Get historical price data for a symbol.
        
        Parameters
        ----------
        symbol : str
            Stock ticker symbol (e.g., 'AAPL', 'MSFT')
        start_date : str, optional
            Start date in YYYY-MM-DD format. Defaults to 1 year ago.
        end_date : str, optional
            End date in YYYY-MM-DD format. Defaults to today.
            
        Returns
        -------
        OBBResult
            Result object containing the historical price data.
            
        Examples
        --------
        >>> from openbb_mvp import obb
        >>> result = obb.equity.price.historical("AAPL")
        >>> df = result.to_dataframe()
        >>> print(df.tail())
        """
        # Set default dates if not provided
        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")
        if start_date is None:
            start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
        
        # Fetch data from Yahoo Finance
        ticker = yf.Ticker(symbol)
        df = ticker.history(start=start_date, end=end_date)
        
        if df.empty:
            raise ValueError(f"No data found for symbol: {symbol}")
        
        # Reset index to get date as a column
        df = df.reset_index()
        
        # Rename columns to match OpenBB convention (lowercase)
        df.columns = [col.lower() for col in df.columns]
        
        # Select only the columns we need
        columns_to_keep = ['date', 'open', 'high', 'low', 'close', 'volume']
        df = df[[col for col in columns_to_keep if col in df.columns]]
        
        # Convert to list of HistoricalData objects
        data = [HistoricalData(**row) for row in df.to_dict('records')]
        
        return OBBResult(data=data, metadata={"symbol": symbol})


class EquityInterface:
    """Equity data interface."""
    
    def __init__(self):
        self.price = PriceInterface()


class OBBInterface:
    """Main OpenBB interface - simplified MVP version."""
    
    def __init__(self):
        self.equity = EquityInterface()
