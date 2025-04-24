FROM python:3.12-slim

# environment
#ENV DATABASE_URL "sqlite:///./app.db"

# install dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
	&& rm -rf /var/lib/apt/lists/*

# pip
RUN python3 -m pip install --upgrade pip

# app folder
WORKDIR /app

# install app
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# expose ports
EXPOSE 8000

# entrypoint
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]