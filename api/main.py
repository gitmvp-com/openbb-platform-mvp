"""FastAPI application for OpenBB MVP."""

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from datetime import datetime, timedelta
import sys
import os

# Add parent directory to path to import openbb_mvp
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openbb_mvp import obb

app = FastAPI(
    title="OpenBB Platform MVP API",
    description="Simplified REST API for accessing stock market data",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "OpenBB Platform MVP API",
        "version": "0.1.0",
        "docs": "/docs",
        "endpoints": {
            "historical_price": "/equity/price/historical"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/equity/price/historical")
async def get_historical_price(
    symbol: str = Query(..., description="Stock ticker symbol (e.g., AAPL, MSFT)"),
    start_date: Optional[str] = Query(
        None,
        description="Start date in YYYY-MM-DD format",
        regex=r"^\d{4}-\d{2}-\d{2}$"
    ),
    end_date: Optional[str] = Query(
        None,
        description="End date in YYYY-MM-DD format",
        regex=r"^\d{4}-\d{2}-\d{2}$"
    ),
):
    """Get historical price data for a stock symbol.
    
    Parameters
    ----------
    symbol : str
        Stock ticker symbol (e.g., 'AAPL', 'MSFT', 'GOOGL')
    start_date : str, optional
        Start date in YYYY-MM-DD format. Defaults to 1 year ago.
    end_date : str, optional
        End date in YYYY-MM-DD format. Defaults to today.
        
    Returns
    -------
    dict
        JSON response with historical price data and metadata.
        
    Examples
    --------
    GET /equity/price/historical?symbol=AAPL
    GET /equity/price/historical?symbol=AAPL&start_date=2024-01-01&end_date=2024-12-31
    """
    try:
        # Get data using OpenBB MVP interface
        result = obb.equity.price.historical(
            symbol=symbol.upper(),
            start_date=start_date,
            end_date=end_date
        )
        
        # Convert to dictionary for JSON response
        response_data = result.to_dict()
        
        return JSONResponse(
            content={
                "success": True,
                "data": response_data["data"],
                "metadata": {
                    "symbol": symbol.upper(),
                    "start_date": start_date or (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d"),
                    "end_date": end_date or datetime.now().strftime("%Y-%m-%d"),
                    "records": len(response_data["data"])
                }
            },
            status_code=200
        )
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
