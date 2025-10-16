#!/usr/bin/env python
"""Run the OpenBB MVP API server."""

import uvicorn

if __name__ == "__main__":
    print("🚀 Starting OpenBB MVP API Server...")
    print("📊 API will be available at: http://localhost:8000")
    print("📖 Interactive docs at: http://localhost:8000/docs")
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
