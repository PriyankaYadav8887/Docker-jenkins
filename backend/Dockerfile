#  STAGE 1: builder 
# Heavy image — installs ALL dependencies
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
# Install packages into an isolated folder
RUN pip install --no-cache-dir --target=/build/packages -r requirements.txt
#  STAGE 2: final 
# Clean slim image — NO pip, NO build tools
FROM python:3.12-slim AS final
# Security: run as non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser/app
# Copy ONLY the installed packages from builder
COPY --from=builder /build/packages /usr/local/lib/python3.12/site-packages/
COPY app.py .
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=15s --timeout=5s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/health')"

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]