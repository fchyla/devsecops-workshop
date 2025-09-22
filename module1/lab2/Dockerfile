FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl wget sudo
COPY app.py /app/
EXPOSE 8080
CMD ["python3", "/app/app.py"]

