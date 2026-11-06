#!/bin/bash
# install-tools.sh — Fallback CLI Fluency Environment Setup
# Runs on Replit / Gitpod / any Ubuntu-based environment
# Usage: curl -fsSL https://raw.githubusercontent.com/ivycollegiate-development/ap-cybersecurity/main/install-tools.sh | bash

set -e

echo "=== AP Cybersecurity CLI Fluency Environment Setup ==="
echo "Detecting platform..."

# Platform detection
if command -v nix-env &> /dev/null && [ -n "$REPL_SLUG" ]; then
    PLATFORM="replit"
    echo "Platform: Replit (Nix)"
elif [ -n "$GITPOD_WORKSPACE_ID" ]; then
    PLATFORM="gitpod"
    echo "Platform: Gitpod (Ubuntu)"
elif [ -n "$CODESPACES" ]; then
    PLATFORM="codespaces"
    echo "Platform: GitHub Codespaces (Ubuntu) — should use devcontainer instead"
else
    PLATFORM="ubuntu"
    echo "Platform: Generic Ubuntu/Linux"
fi

# Install function for apt-based systems
install_apt() {
    echo "Updating package list..."
    sudo apt-get update -qq
    
    echo "Installing core tools..."
    sudo apt-get install -y -qq \
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
        coreutils
    
    echo "Installing Python tools..."
    pip3 install --no-cache-dir --quiet trufflehog gitleaks
    
    echo "Installing crictl..."
    VERSION="v1.28.0"
    wget -q https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
    sudo tar -xzf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
    rm crictl-$VERSION-linux-amd64.tar.gz
}

# Install function for Nix-based systems (Replit)
install_nix() {
    echo "Installing via Nix..."
    nix-env -iA \
        nixpkgs.nmap \
        nixpkgs.tcpdump \
        nixpkgs.wireshark-cli \
        nixpkgs.jq \
        nixpkgs.openssl \
        nixpkgs.gnupg \
        nixpkgs.docker \
        nixpkgs.git \
        nixpkgs.python3 \
        nixpkgs.pip \
        nixpkgs.lsof \
        nixpkgs.procps \
        nixpkgs.findutils \
        nixpkgs.gnugrep \
        nixpkgs.gawk \
        nixpkgs.gnused \
        nixpkgs.coreutils
    
    echo "Installing Python tools..."
    pip install --no-cache-dir --quiet trufflehog gitleaks
    
    echo "Installing crictl..."
    VERSION="v1.28.0"
    wget -q https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
    tar -xzf crictl-$VERSION-linux-amd64.tar.gz -C ~/.local/bin
    rm crictl-$VERSION-linux-amd64.tar.gz
    export PATH="$HOME/.local/bin:$PATH"
}

# Run platform-specific installation
case $PLATFORM in
    "replit")
        install_nix
        ;;
    "gitpod"|"codespaces"|"ubuntu")
        install_apt
        ;;
esac

# Verify installation
echo ""
echo "=== Verification ==="
echo "nmap:      $(nmap --version | head -1)"
echo "tcpdump:   $(tcpdump --version | head -1)"
echo "tshark:    $(tshark -v | head -1)"
echo "jq:        $(jq --version)"
echo "openssl:   $(openssl version)"
echo "gpg:       $(gpg --version | head -1)"
echo "docker:    $(docker --version)"
echo "crictl:    $(crictl version 2>/dev/null | head -1 || echo 'not found')"
echo "trufflehog: $(trufflehog --version 2>/dev/null || echo 'not found')"
echo "gitleaks:   $(gitleaks version 2>/dev/null || echo 'not found')"
echo "git:       $(git --version)"

# Check Docker daemon (for Codespaces/Gitpod)
if [ "$PLATFORM" != "replit" ]; then
    echo ""
    echo "=== Docker Daemon Check ==="
    if sudo systemctl is-active --quiet docker 2>/dev/null || sudo service docker status 2>/dev/null | grep -q running; then
        echo "Docker daemon: RUNNING"
    else
        echo "Docker daemon: NOT RUNNING — attempting to start..."
        sudo systemctl start docker 2>/dev/null || sudo service docker start 2>/dev/null || echo "Could not start Docker daemon"
    fi
fi

# Create test files for grader
echo ""
echo "=== Creating Test Artifacts ==="

# Create investigation directory with test files
mkdir -p /investigation
echo "normal log content" > /investigation/app.log
echo "ERROR: Something failed" >> /investigation/app.log
echo "CRITICAL: System down" >> /investigation/app.log
dd if=/dev/urandom of=/investigation/binary.dat bs=1M count=2 2>/dev/null
echo "hidden content" > /investigation/.hidden_file

# Create auth.json for log analysis task
cat > /investigation/auth.json << 'EOF'
{"timestamp": "2027-04-28T10:00:00Z", "message": "Failed password for root from 192.168.1.100", "source_ip": "192.168.1.100"}
{"timestamp": "2027-04-28T10:00:01Z", "message": "Failed password for root from 192.168.1.100", "source_ip": "192.168.1.100"}
{"timestamp": "2027-04-28T10:00:02Z", "message": "Failed password for admin from 10.0.0.50", "source_ip": "10.0.0.50"}
{"timestamp": "2027-04-28T10:00:03Z", "message": "Accepted password for admin from 10.0.0.50", "source_ip": "10.0.0.50"}
{"timestamp": "2027-04-28T10:00:04Z", "message": "Failed password for root from 192.168.1.100", "source_ip": "192.168.1.100"}
EOF

# Create traffic.pcap placeholder (students will use provided one)
touch /investigation/traffic.pcap

echo "Test artifacts created in /investigation/"

echo ""
echo "=== Setup Complete ==="
echo "Run the grader with: STUDENT_ID=your_id python3 CLI-Check-Grader.py"