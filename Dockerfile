FROM python:3.9-slim-bookworm
WORKDIR /app
RUN pip install --progress-bar off flask
EXPOSE 5000
CMD ["flask", "--app", "app.py", "run", "--debug", "--host", "0.0.0.0"]
