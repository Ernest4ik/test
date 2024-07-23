FROM python:latest
WORKDIR /app
COPY ./memes_api /app/memes_api
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["uvicorn", "memes_api.main:app", "--host", "0.0.0.0", "--port", "80"]
