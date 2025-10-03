#!/bin/bash

# Build script for Render deployment
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Loading portfolio data..."
python load_portfolio_data.py || echo "Portfolio data loading skipped"

echo "Build completed successfully!"
