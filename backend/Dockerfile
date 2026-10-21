FROM python:3.12-slim-bookworm

# Copy standalone uv binaries directly from Astral's official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Configure uv behavior:
# 1. Force using the container's system Python (avoids broken shebang paths)
# 2. Enable bytecode compilation
# 3. Copy files instead of hardlinking
ENV UV_PYTHON_PREFERENCE=only-system
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Place the virtual environment path at the beginning of PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency specifications first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install exact production dependencies
RUN uv sync --frozen --no-dev --no-install-project

# Copy application source code (now safe because .dockerignore blocks .venv)
COPY . .

EXPOSE 8000

# Execute uvicorn via python module directly
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]