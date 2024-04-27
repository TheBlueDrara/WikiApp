# FROM python:3.11-slim
# WORKDIR /app
# COPY . /app
# RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 5000
# CMD ["python", "ShibariWiki.py"]


FROM python:3.11-slim
WORKDIR /app
COPY . /app
COPY start.sh /app/start.sh
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /app/start.sh
EXPOSE 5000
CMD ["/app/start.sh"]