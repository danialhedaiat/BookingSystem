FROM python:3.12-slim
LABEL author="dan hedaiat"

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV MONGO_HOST=mongodb://admin:1234@mongo/
ENV REDIS_HOST=redis://redis:6379

EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]