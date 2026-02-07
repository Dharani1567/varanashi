import subprocess


def call_llm(prompt: str) -> str:
    """
    Calls Ollama locally.
    Requires: ollama installed + model pulled.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        return result.stdout.strip()

    except Exception as e:
        raise RuntimeError(f"Ollama error: {e}")
