"""OpenBB Platform MVP - Simplified version for educational purposes."""

from openbb_mvp.core import OBBInterface

__version__ = "0.1.0"

# Create the main obb instance - similar to OpenBB Platform
obb = OBBInterface()

__all__ = ["obb"]
