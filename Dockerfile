FROM python:3.12-alpine
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install flask requests

CMD ["flask", "run", "--host=0.0.0.0"]
