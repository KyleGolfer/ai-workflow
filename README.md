Here is the **complete README.md** with **Option B** (generic placeholder approach). Copy this entire block:

```markdown
# AI Workflow Stack

A containerized AI stack with n8n workflow automation, Open WebUI chat interface, LiteLLM proxy, Ollama LLM backend, and SearXNG search - all secured behind a dedicated Tailscale network with Caddy reverse proxy.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Tailscale Network (<TAILSCALE_IP>)                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Caddy Reverse Proxy                             │   │
│  │  :4000 → LiteLLM (172.21.0.3)                   │   │
│  │  :8080 → Open WebUI (172.21.0.5)                 │   │
│  │  :5678 → n8n (172.21.0.2)                        │   │
│  │  :8081 → SearXNG (172.21.0.13)                   │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│  ┌─────────────┐  ┌──────┴──────┐  ┌──────────────┐   │
│  │  LiteLLM    │  │ Open WebUI  │  │     n8n      │   │
│  │  :4000      │  │   :8080     │  │   :5678      │   │
│  └──────┬──────┘  └─────────────┘  └──────┬───────┘   │
│         │                                   │           │
│  ┌──────┴──────┐  ┌──────────────┐  ┌────┴──────┐   │
│  │   Ollama    │  │ SearXNG      │  │  Sandbox  │   │
│  │  :11434     │  │   :8080      │  │   Stack   │   │
│  └─────────────┘  └──────────────┘  └───────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Docker & Docker Compose installed
- Tailscale account and auth key
- At least 16GB RAM (64GB+ recommended for larger models)

### 1. Clone and Configure

```bash
git clone https://github.com/KyleGolfer/ai-workflow.git
cd ai-workflow

# Copy environment template
cp .env.example .env

# Edit with your values
nano .env
```

### 2. Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `TAILSCALE_AUTH_KEY` | Tailscale auth key | `tskey-auth-...` |
| `LITELLM_DB_PASSWORD` | PostgreSQL password | `secure-password` |
| `LITELLM_MASTER_KEY` | LiteLLM API key | `sk-...` |
| `VENICE_API_KEY` | Venice.ai API key | `venice-...` |
| `N8N_USER` / `N8N_PASSWORD` | n8n credentials | `admin` / `password` |
| `N8N_ENCRYPTION_KEY` | n8n encryption | `random-string` |

### 3. Start the Stack

```bash
docker-compose up -d
```

### 4. Get Your Tailscale IP

```bash
docker exec tailscale-ai tailscale ip -4
# Returns: 100.x.x.x (your unique IP)
```

### 5. Access Services

All services available at `http://<TAILSCALE_IP>:<PORT>`:

| Service | Port | Purpose |
|---------|------|---------|
| **Open WebUI** | 8080 | Chat interface with models |
| **LiteLLM** | 4000 | API key management & model routing |
| **n8n** | 5678 | Workflow automation |
| **SearXNG** | 8081 | Private search engine |

**Example**: If your Tailscale IP is `100.70.205.60`:
- Open WebUI: http://100.70.205.60:8080
- LiteLLM: http://100.70.205.60:4000

## Services Overview

### Open WebUI
- Web-based chat interface
- Supports multiple model providers via LiteLLM
- Document upload and RAG capabilities
- User management and permissions

### LiteLLM
- Unified API for multiple LLM providers
- Cost tracking and rate limiting
- API key management
- Supports Venice.ai, OpenAI, Anthropic, etc.

### n8n
- Workflow automation
- AI agent capabilities with sandboxed code execution
- Integration with 400+ services
- Visual workflow builder

### Ollama
- Local LLM inference
- Runs models like Llama, Mistral, etc.
- GPU acceleration support
- Model management via CLI

### SearXNG
- Privacy-focused metasearch engine
- No tracking or profiling
- Customizable search sources

## Maintenance

### Update Images

```bash
docker-compose pull
docker-compose up -d
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f open-webui
```

### Backup Data

```bash
# Backup volumes
docker run --rm -v ai-workflow_open-webui-data:/data -v $(pwd):/backup alpine tar czf /backup/open-webui-backup.tar.gz -C /data .
```

## Network Configuration

- **Tailscale IP**: Unique per deployment (get with `docker exec tailscale-ai tailscale ip -4`)
- **Docker Network**: `172.21.0.0/16`
- **Caddy** proxies all traffic through Tailscale container
- No ports exposed directly to host - all traffic routed through Tailscale

## Troubleshooting

### Services not accessible
```bash
# Check Tailscale status
docker exec tailscale-ai tailscale status

# Verify Caddy is listening
docker exec tailscale-ai netstat -tlnp | grep caddy

# Get your Tailscale IP
docker exec tailscale-ai tailscale ip -4
```

### Reset Tailscale
```bash
docker-compose down
sudo rm -rf /mnt/appdata/tailscale-ai
docker-compose up -d
```

## Security Notes

- All services protected by Tailscale network (no public exposure)
- `.env` file contains secrets - never commit to Git
- Sandbox environment isolates untrusted code execution
- Internal Docker network prevents direct container access

## License

MIT - See LICENSE file
```

---

## Step 2: Commit the README

**Complete this step before moving on:**

```bash
cd /mnt/appdata/ai-workflow

# Create the README file
nano README.md
# (Paste the content above, then Ctrl+X, Y, Enter)

# Stage and commit
git add README.md
git commit -m "Add comprehensive README with setup instructions

- Documented architecture with Caddy + Tailscale networking
- Step-by-step setup instructions
- Generic Tailscale IP placeholder for portability
- Service descriptions and troubleshooting guide"

# Push to GitHub
git push origin main
```

**Confirm completion** before we move to Step 1 (tidying other stacks).
