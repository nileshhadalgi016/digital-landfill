# Run Your Own Private AI Over the Internet

Access a locally running LLM from anywhere using Ollama + Ngrok. No cloud. No API costs. Fully private.

Works on **macOS**, **Linux**, and **Windows** — accessible from **Android** and **iPhone**.

---

## Prerequisites

- A computer running macOS, Linux, or Windows
- Free accounts on [Ngrok](https://ngrok.com) and [Ollama](https://ollama.com)
- Android or iPhone

---

## Step 1 — Install Ollama

Ollama lets you run open-source LLMs locally on your machine.

### macOS
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Or download the desktop app from [https://ollama.com/download](https://ollama.com/download)

### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Supports Ubuntu, Debian, Fedora, Arch, and most major distros.

### Windows
Download the `.exe` installer from [https://ollama.com/download](https://ollama.com/download) and run it.
Ollama installs as a system tray app and starts automatically.

---

### Verify installation (all platforms):
```bash
ollama --version
```

### Pull a model:
```bash
ollama pull llama3.1:latest
```

> Other good models: `mistral`, `phi3`, `gemma2`, `qwen2`

### Test it works locally:
```bash
ollama run llama3.1
```

Type a message and confirm you get a response. Press `Ctrl+D` or type `/bye` to exit.

### Check the local API is running:
```bash
curl http://localhost:11434/api/tags
```

You should see a JSON list of your downloaded models. This confirms Ollama's API server is live on port `11434`.

---

## Step 2 — Install and Configure Ngrok

Ngrok creates a secure public tunnel to your local machine.

### macOS
```bash
brew install ngrok
```

### Linux
```bash
# Debian/Ubuntu
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok

# Or download binary directly
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin
```

### Windows
Download the `.zip` from [https://ngrok.com/download](https://ngrok.com/download), extract it, and add the folder to your PATH.  
Or install via **Chocolatey**:
```powershell
choco install ngrok
```

---

### Add your auth token (all platforms):

Go to [https://ngrok.com](https://ngrok.com) → Sign up → Dashboard → copy your **Authtoken**, then run:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

### Verify config:

**macOS / Linux:**
```bash
cat ~/.config/ngrok/ngrok.yml
```

**Windows:**
```powershell
type %USERPROFILE%\AppData\Local/ngrok/ngrok.yml
```

---

## Step 3 — Expose Ollama to the Internet

### macOS / Linux

Make sure Ollama is running:
```bash
ollama serve
```

> If you already ran `ollama run` earlier, the server is likely already active. Verify with `curl http://localhost:11434`.

Open a **new terminal tab** and run:
```bash
ngrok http http://localhost:11434
```

### Windows

Ollama starts automatically as a background service after installation. Open **Command Prompt** or **PowerShell** and run:
```powershell
ngrok http http://localhost:11434
```

---

You'll see output like:
```
Forwarding    https://abc123.ngrok-free.app -> http://localhost:11434
```

**Copy that `https://` URL.** This is your public endpoint. Keep it private — anyone with this URL can reach your local Ollama.

---

## Step 4 — Connect from Your Phone

### Android — API Tester

1. Download **API Tester** from the Play Store
2. Create a new request:
   - Method: `POST`
   - URL: `https://YOUR-NGROK-URL/api/generate`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON):
     ```json
     {
       "model": "llama3.1",
       "prompt": "Hello, who are you?",
       "stream": false
     }
     ```
3. Hit **Send** — you'll get a response from your machine's AI

### Android — Enchanted (alternative)

1. Download **Enchanted** from the Play Store
2. Open Settings → paste your Ngrok URL as the server
3. Start chatting with a clean UI

### iPhone — Mollama

1. Download **Mollama** from the App Store
2. Open the app → Go to **Settings**
3. Paste your Ngrok URL as the **Ollama Server URL**
4. Go back to the chat screen — it will list your available models
5. Select `llama3.1` and start chatting

### iPhone — Enchanted (alternative)

1. Download **Enchanted** from the App Store
2. Open Settings → set the Ollama host to your Ngrok URL
3. Select a model and chat

---

## Step 5 — Test the API Directly (Optional)

Works from any terminal on macOS, Linux, or Windows (Git Bash / WSL / PowerShell with curl):

```bash
curl -X POST https://YOUR-NGROK-URL/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.1",
    "prompt": "What is the capital of France?",
    "stream": false
  }'
```

Or use the OpenAI-compatible chat endpoint:

```bash
curl -X POST https://YOUR-NGROK-URL/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.1",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `curl localhost:11434` fails | Run `ollama serve` in terminal |
| Ngrok shows "tunnel not found" | Restart `ngrok http http://localhost:11434` |
| Phone gets a timeout | Check Ngrok is still running on your machine |
| Model not found error | Run `ollama pull llama3.1:latest` |
| Ngrok URL expired | Free Ngrok URLs reset every session — copy the new one |
| Windows Firewall blocking | Allow Ngrok through Windows Defender Firewall |
| Linux port permission denied | Run `sudo ufw allow 11434` if using UFW firewall |

---

## Keep It Running in the Background (Optional)

### macOS / Linux
```bash
# Keep Ollama serving in background
nohup ollama serve > /tmp/ollama.log 2>&1 &

# Keep Ngrok running in background
nohup ngrok http http://localhost:11434 > /tmp/ngrok.log 2>&1 &
```

Check the Ngrok URL:
```bash
cat /tmp/ngrok.log
```

### Windows (PowerShell)
```powershell
# Ollama runs as a service automatically on Windows

# Run Ngrok in background and log output
Start-Process -NoNewWindow ngrok -ArgumentList "http http://localhost:11434" -RedirectStandardOutput "$env:TEMP\ngrok.log"
```

Check the Ngrok URL:
```powershell
type $env:TEMP\ngrok.log
```

---

## Notes

- The **free Ngrok plan** gives you one tunnel with a random URL that resets each session. For a fixed URL, upgrade to a paid plan.
- This setup is for **personal use**. Don't expose this publicly without adding authentication.
- Your data never leaves your machine — the AI runs 100% locally.
- Works on cellular data (4G/5G), not just Wi-Fi.
