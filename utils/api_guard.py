import os


def is_api_available():
    """
    Check whether API key exists.
    """
    return bool(os.getenv("GOOGLE_API_KEY"))


def safe_llm_call(callable_fn, fallback_fn):
    """
    Executes LLM call safely.
    Falls back if API fails.
    """
    try:
        if not is_api_available():
            raise RuntimeError("API key not found")

        return callable_fn()

    except Exception as e:
        return fallback_fn(str(e))
