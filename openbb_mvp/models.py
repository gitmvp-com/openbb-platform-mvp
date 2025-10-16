"""Data models for OpenBB MVP."""

from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel, Field
import pandas as pd


class HistoricalData(BaseModel):
    """Historical price data model."""
    
    date: datetime = Field(description="Date of the data point")
    open: float = Field(description="Opening price")
    high: float = Field(description="Highest price")
    low: float = Field(description="Lowest price")
    close: float = Field(description="Closing price")
    volume: Optional[float] = Field(default=None, description="Trading volume")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d")
        }


class OBBResult:
    """Result object that mimics OpenBB Platform output."""
    
    def __init__(self, data: List[HistoricalData], metadata: Dict[str, Any] = None):
        self.data = data
        self.metadata = metadata or {}
    
    def to_dataframe(self) -> pd.DataFrame:
        """Convert result to pandas DataFrame.
        
        Returns
        -------
        pd.DataFrame
            DataFrame with historical price data.
        """
        if not self.data:
            return pd.DataFrame()
        
        # Convert Pydantic models to dict and create DataFrame
        data_dicts = [item.model_dump() for item in self.data]
        return pd.DataFrame(data_dicts)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary.
        
        Returns
        -------
        dict
            Dictionary with data and metadata.
        """
        return {
            "data": [item.model_dump() for item in self.data],
            "metadata": self.metadata
        }
    
    def __repr__(self) -> str:
        return f"OBBResult(data={len(self.data)} records, metadata={self.metadata})"
