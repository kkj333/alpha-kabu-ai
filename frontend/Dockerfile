FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy project definition
COPY pyproject.toml .

# Install dependencies
RUN uv sync --frozen --no-install-project || uv sync --no-install-project

# Copy the rest of the project
COPY . .

# Install the project itself
RUN uv sync --frozen || uv sync

CMD ["uv", "run", "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
