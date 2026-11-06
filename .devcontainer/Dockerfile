# Dockerfile for AP Cybersecurity CLI Fluency Check Codespace
# Build: docker build -t ap-cyber-cli-fluency .devcontainer
# Used by: .devcontainer/devcontainer.json

FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Prevent interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Install security tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap \
    tcpdump \
    tshark \
    wireshark-common \
    jq \
    openssl \
    gnupg2 \
    docker.io \
    containerd \
    git \
    python3-pip \
    curl \
    wget \
    iproute2 \
    lsof \
    procps \
    findutils \
    grep \
    awk \
    sed \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Install Python security tools
RUN pip3 install --no-cache-dir \
    trufflehog \
    gitleaks

# Install crictl (Kubernetes container runtime CLI)
ARG CRICTL_VERSION="v1.28.0"
RUN wget -q https://github.com/kubernetes-sigs/cri-tools/releases/download/${CRICTL_VERSION}/crictl-${CRICTL_VERSION}-linux-amd64.tar.gz && \
    tar -xzf crictl-${CRICTL_VERSION}-linux-amd64.tar.gz -C /usr/local/bin && \
    rm crictl-${CRICTL_VERSION}-linux-amd64.tar.gz

# Create test artifacts directory structure
RUN mkdir -p /investigation && \
    echo "normal log content" > /investigation/app.log && \
    echo "ERROR: Something failed" >> /investigation/app.log && \
    echo "CRITICAL: System down" >> /investigation/app.log && \
    dd if=/dev/urandom of=/investigation/binary.dat bs=1M count=2 2>/dev/null && \
    echo "hidden content" > /investigation/.hidden_file && \
    printf '{"timestamp": "2027-04-28T10:00:00Z", "message": "Failed password for root from 192.168.1.100", "source_ip": "192.168.1.100"}\n{"timestamp": "2027-04-28T10:00:01Z", "message": "Failed password for root from 192.168.1.100", "source_ip": "192.168.1.100"}\n{"timestamp": "2027-04-28T10:00:02Z", "message": "Failed password for admin from 10.0.0.50", "source_ip": "10.0.0.50"}\n{"timestamp": "2027-04-28T10:00:03Z", "message": "Accepted password for admin from 10.0.0.50", "source_ip": "10.0.0.50"}\n{"timestamp": "2027-04-28T10:00:04Z", "message": "Failed password for root from 192.168.1.100", "source_ip": "192.168.1.100"}\n' > /investigation/auth.json

# Create placeholder for traffic.pcap (real one provided at runtime)
RUN touch /investigation/traffic.pcap

# Set up non-root user (codespace user already exists in base image)
USER codespace

# Add local bin to PATH
ENV PATH="/home/codespace/.local/bin:${PATH}"

# Verify tools are available
RUN nmap --version | head -1 && \
    tcpdump --version | head -1 && \
    tshark -v | head -1 && \
    jq --version && \
    openssl version && \
    gpg --version | head -1 && \
    docker --version && \
    crictl version && \
    trufflehog --version && \
    gitleaks version && \
    git --version

# Default command
CMD ["sleep", "infinity"]