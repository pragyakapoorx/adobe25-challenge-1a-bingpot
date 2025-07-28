# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy scripts
COPY challenge-1a.py get_text.py ./

# Install dependencies
RUN pip install --no-cache-dir pymupdf

# Create a mount point for data
VOLUME ["/data"]

# Default command (can be overridden)
CMD ["python", "challenge-1a.py"] 