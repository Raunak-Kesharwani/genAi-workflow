import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

def run_backend():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "backend.main:app",
            "--reload"
        ],
        cwd=ROOT
    )

def run_frontend():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "frontend/app.py"
        ],
        cwd=ROOT
    )

if __name__ == "__main__":
    print("🚀 Starting AI Project Lab...")
    backend = run_backend()
    frontend = run_frontend()

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        backend.terminate()
        frontend.terminate()
