#!/usr/bin/env python
"""Example usage of OpenBB MVP."""

from openbb_mvp import obb
import pandas as pd


def main():
    print("OpenBB Platform MVP - Example Usage\n")
    print("=" * 50)
    
    # Example 1: Get Apple stock data
    print("\n📈 Example 1: Getting AAPL historical data...\n")
    
    result = obb.equity.price.historical("AAPL")
    df = result.to_dataframe()
    
    print(f"Retrieved {len(df)} records for AAPL")
    print("\nLast 5 days:")
    print(df.tail())
    
    # Example 2: Calculate some basic statistics
    print("\n" + "=" * 50)
    print("\n📊 Example 2: Basic Statistics for AAPL\n")
    
    print(f"Period: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
    print(f"Latest Close: ${df['close'].iloc[-1]:.2f}")
    print(f"Period High: ${df['high'].max():.2f}")
    print(f"Period Low: ${df['low'].min():.2f}")
    print(f"Average Volume: {df['volume'].mean():,.0f}")
    
    # Example 3: Multiple stocks comparison
    print("\n" + "=" * 50)
    print("\n📊 Example 3: Comparing Multiple Stocks\n")
    
    symbols = ["AAPL", "MSFT", "GOOGL"]
    
    for symbol in symbols:
        result = obb.equity.price.historical(
            symbol=symbol,
            start_date="2024-01-01"
        )
        df = result.to_dataframe()
        latest_price = df['close'].iloc[-1]
        change = ((df['close'].iloc[-1] - df['close'].iloc[0]) / df['close'].iloc[0]) * 100
        
        print(f"{symbol:6s} - Latest: ${latest_price:8.2f} | YTD Change: {change:+.2f}%")
    
    print("\n" + "=" * 50)
    print("\n✅ Examples completed successfully!\n")


if __name__ == "__main__":
    main()
