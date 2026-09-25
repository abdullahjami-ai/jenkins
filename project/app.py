"""
Week 18 - Day 1 : the tiny app we are going to put inside a Docker container.

It is a normal FastAPI app - nothing Docker-specific in here.
That is the whole point: Docker packages your app, it does not change it.
"""

import os
import platform
import socket

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Docker Demo API")


@app.get("/", response_class=HTMLResponse)
def home():
    """A small web page so you can SEE the result in your browser."""
    return f"""
    <html>
      <head><title>Hello from Docker</title></head>
      <body style="font-family: system-ui, sans-serif; background:#0f172a; color:#e2e8f0;
                   display:flex; align-items:center; justify-content:center; height:100vh; margin:0">
        <div style="text-align:center">
          <div style="font-size:72px">&#128051;</div>
          <h1 style="margin:8px 0">It works!</h1>
          <p style="color:#94a3b8">This page is being served from inside a container.</p>
          <table style="margin:24px auto; border-collapse:collapse; font-size:15px">
            <tr><td style="padding:6px 14px; color:#94a3b8; text-align:right">Hostname</td>
                <td style="padding:6px 14px; font-family:monospace; color:#38bdf8">{socket.gethostname()}</td></tr>
            <tr><td style="padding:6px 14px; color:#94a3b8; text-align:right">Python</td>
                <td style="padding:6px 14px; font-family:monospace; color:#38bdf8">{platform.python_version()}</td></tr>
            <tr><td style="padding:6px 14px; color:#94a3b8; text-align:right">OS inside</td>
                <td style="padding:6px 14px; font-family:monospace; color:#38bdf8">{platform.system()} {platform.release()}</td></tr>
            <tr><td style="padding:6px 14px; color:#94a3b8; text-align:right">Message</td>
                <td style="padding:6px 14px; font-family:monospace; color:#38bdf8">{os.getenv("GREETING", "set me with -e GREETING=...")}</td></tr>
          </table>
          <p style="color:#64748b; font-size:13px">Try also /health and /predict?value=21</p>
        </div>
      </body>
    </html>
    """


@app.get("/health")
def health():
    """Standard 'is my app alive?' endpoint. Every real service has one."""
    return {"status": "healthy"}


@app.get("/predict")
def predict(value: float = 0):
    """A fake 'model'. Later in the bootcamp this becomes a real one."""
    return {"input": value, "prediction": value * 2, "model": "times-two-v1"}
