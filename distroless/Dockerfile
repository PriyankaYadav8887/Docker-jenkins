# ---------- STAGE 1 : Builder ----------

FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --target=/python-packages -r requirements.txt


# ---------- STAGE 2 : Distroless ----------

FROM gcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /python-packages /python-packages

COPY app.py .

ENV PYTHONPATH=/python-packages

EXPOSE 5000

CMD ["app.py"]