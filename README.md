# OpenBB Platform MVP

<div align="center">
  <h3>Investment research for everyone, anywhere - Simplified MVP</h3>
  <p>A minimal viable product version of the OpenBB Platform focusing on core stock data retrieval</p>
</div>

## 🎯 What is this?

This is a simplified MVP version of the [OpenBB Platform](https://github.com/OpenBB-finance/OpenBB) that demonstrates the core functionality:

- **Fetch historical stock prices** for any ticker symbol
- **No authentication required** - uses Yahoo Finance free data
- **Simple Python API** - just like the original OpenBB
- **REST API included** - access data via HTTP endpoints
- **Lightweight** - minimal dependencies, easy to understand

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/gitmvp-com/openbb-platform-mvp.git
cd openbb-platform-mvp

# Install dependencies
pip install -r requirements.txt
```

### Python Usage

```python
from openbb_mvp import obb

# Get historical price data
output = obb.equity.price.historical("AAPL")
df = output.to_dataframe()
print(df.tail())
```

### REST API

Start the API server:

```bash
python run_api.py
```

The API will be available at `http://localhost:8000`

Access the interactive docs at: `http://localhost:8000/docs`

#### Example API Request:

```bash
curl "http://localhost:8000/equity/price/historical?symbol=AAPL"
```

## 📚 Features

### Python Interface

```python
from openbb_mvp import obb
import pandas as pd

# Get stock data
result = obb.equity.price.historical(
    symbol="AAPL",
    start_date="2024-01-01",
    end_date="2024-12-31"
)

# Convert to DataFrame
df = result.to_dataframe()

# Access data
print(f"Latest close: ${df['close'].iloc[-1]:.2f}")
print(f"Period high: ${df['high'].max():.2f}")
print(f"Period low: ${df['low'].min():.2f}")
```

### REST API Endpoints

- `GET /equity/price/historical` - Get historical price data
  - Parameters:
    - `symbol` (required): Stock ticker symbol
    - `start_date` (optional): Start date (YYYY-MM-DD)
    - `end_date` (optional): End date (YYYY-MM-DD)

## 🏗️ Project Structure

```
openbb-platform-mvp/
├── openbb_mvp/              # Main package
│   ├── __init__.py          # Package initialization & obb interface
│   ├── core.py              # Core data fetching logic
│   └── models.py            # Data models
├── api/
│   └── main.py              # FastAPI application
├── run_api.py               # API server entry point
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🔧 Technology Stack

This MVP uses the same core technologies as OpenBB Platform:

- **Python 3.9+** - Programming language
- **yfinance** - Yahoo Finance data source (no API key required)
- **pandas** - Data manipulation
- **FastAPI** - REST API framework
- **uvicorn** - ASGI server
- **pydantic** - Data validation

## 📈 Example Output

```
            date    open    high     low   close      volume
0     2024-01-02  184.22  185.88  183.89  185.64  82488200.0
1     2024-01-03  184.25  185.99  183.43  184.25  58414800.0
2     2024-01-04  182.15  183.09  180.88  181.91  81622700.0
3     2024-01-05  181.99  182.76  180.17  181.18  98532700.0
4     2024-01-08  181.30  182.40  180.13  181.96  64843200.0
```

## 🎓 Learn More

This is a simplified educational version. For production use with multiple data sources, advanced features, and professional support, check out:

- **OpenBB Platform**: https://github.com/OpenBB-finance/OpenBB
- **Documentation**: https://docs.openbb.co
- **Website**: https://openbb.co

## 📝 Differences from Full OpenBB Platform

This MVP focuses on simplicity:

✅ **Included:**
- Historical stock price data
- Python interface
- REST API
- DataFrame output

❌ **Not included:**
- Multiple data providers (only Yahoo Finance)
- Authentication/API keys
- Options, crypto, forex, economy data
- Charting capabilities
- Advanced analytics
- Data persistence
- CLI interface

## 🤝 Contributing

This is an educational MVP. For contributions to the full platform, visit:
https://github.com/OpenBB-finance/OpenBB

## 📄 License

This MVP follows the same AGPL-3.0 license as OpenBB Platform.

## ⚠️ Disclaimer

This is a minimal viable product for educational purposes. The data is provided by Yahoo Finance and should not be used for actual trading decisions. For professional use, please use the official OpenBB Platform.
