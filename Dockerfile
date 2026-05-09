FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set environment variables to handle headless Chrome better
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures Playwright doesn't try to use a display it doesn't have
ENV QT_QPA_PLATFORM=offscreen 

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-install the browser binaries if they aren't in your image
RUN playwright install chromium

COPY . .

ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port ${PORT}"]