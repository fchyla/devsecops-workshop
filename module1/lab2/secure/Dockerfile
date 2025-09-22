FROM ubuntu:22.04@sha256:specific_digest
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3=3.10.* && \
    rm -rf /var/lib/apt/lists/*
COPY --chown=appuser:appgroup app.py /app/
USER appuser
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1
CMD ["python3", "/app/app.py"]

