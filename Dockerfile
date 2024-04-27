FROM python:3.11-slim
WORKDIR /app
COPY . /app
# COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 5000
CMD ["/app/start.sh"]
