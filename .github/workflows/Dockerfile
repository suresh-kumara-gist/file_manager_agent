# FROM python:alpine

# RUN pip install requests && mkdir -p /app/code

# WORKDIR /app

# COPY docker-resources /docker-resources

# RUN cp /docker-resources/*.py /app/

# ENTRYPOINT [ "python3" ]

# Stage 1: Flutter SDK
FROM ubuntu:22.04 AS flutter
ENV FLUTTER_VERSION=3.16.9
RUN apt-get update && apt-get install -y \
    curl unzip git xz-utils clang cmake ninja-build \
    && rm -rf /var/lib/apt/lists/*
RUN curl -O https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_${FLUTTER_VERSION}-stable.tar.xz \
    && tar xf flutter_linux_${FLUTTER_VERSION}-stable.tar.xz -C /usr/local \
    && export PATH="$PATH:/usr/local/flutter/bin" \
    && flutter precache
RUN flutter config --enable-windows-desktop --enable-macos-desktop --enable-linux-desktop

# Stage 2: Python + Gemini
FROM python:3.10-slim
WORKDIR /app
COPY --from=flutter /usr/local/flutter /usr/local/flutter
ENV PATH="${PATH}:/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin"
RUN apt-get update && apt-get install -y \
    git openssh-client \
    && pip install google-generativeai python-dotenv \
    && flutter doctor -v
COPY . .
CMD ["python", "agentic_ai.py"]