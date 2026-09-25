# ---------------------------------------------------------------
#  Week 18 - Day 1 : our first Dockerfile
#  A Dockerfile is a RECIPE. `docker build` bakes it into an IMAGE.
#  Every line below becomes one LAYER of that image.
# ---------------------------------------------------------------

# 1. Start from an official image that already has Python inside.
FROM python:3.12-slim

# 2. Every command after this runs inside /app in the container.
WORKDIR /app

# 3. Copy ONLY requirements first. Why? Layer caching:
#    if your code changes but requirements don't, Docker reuses
#    the cached pip layer and the rebuild takes ~1 second.
COPY requirements.txt .

# 4. Install the dependencies inside the image.
#    --no-cache-dir keeps the image small.
RUN pip install -r requirements.txt

# 5. Now copy the application code (this is what changes most often).
COPY app.py .

# 6. Documentation: this app listens on port 8000.
EXPOSE 8000

# 7. The command that runs when the container starts.
#    --host 0.0.0.0 is REQUIRED: 127.0.0.1 inside a container
#    would only be reachable from inside the container itself.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
