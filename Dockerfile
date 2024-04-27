FROM python:3.11-slim

WORKDIR /app

# Copying requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app

# Copy start.sh and make it executable
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Expose port if needed
EXPOSE 5000

# Run the start.sh script
CMD ["/bin/bash", "/app/start.sh"]
