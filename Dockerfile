FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN chmod +x /app/start.sh
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 5000
CMD ["/app/start.sh"]
#change this part so the the starting command will run the python app file, in the app file add enviroment vriable with the credentials and URI for the data base connection.