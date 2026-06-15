from __future__ import annotations

import os
from typing import Any

# Ensure LANGFUSE_HOST is configured if LANGFUSE_BASE_URL is used in environment variables
if "LANGFUSE_BASE_URL" in os.environ and not os.environ.get("LANGFUSE_HOST"):
    os.environ["LANGFUSE_HOST"] = os.environ["LANGFUSE_BASE_URL"]

try:
    from langfuse import observe, get_client
    
    class LangfuseContextWrapper:
        def update_current_trace(self, **kwargs: Any) -> None:
            try:
                get_client().update_current_trace(**kwargs)
            except Exception:
                pass
                
        def update_current_observation(self, **kwargs: Any) -> None:
            try:
                client = get_client()
                if "usage_details" in kwargs:
                    client.update_current_generation(**kwargs)
                else:
                    client.update_current_span(**kwargs)
            except Exception:
                pass

        def score(self, **kwargs: Any) -> None:
            try:
                client = get_client()
                current_otel_span = client._get_current_otel_span()
                if current_otel_span is not None:
                    from langfuse._client.span import LangfuseSpan
                    span = LangfuseSpan(otel_span=current_otel_span, langfuse_client=client)
                    span.score(**kwargs)
            except Exception:
                pass

        def score_trace(self, **kwargs: Any) -> None:
            try:
                client = get_client()
                current_otel_span = client._get_current_otel_span()
                if current_otel_span is not None:
                    from langfuse._client.span import LangfuseSpan
                    span = LangfuseSpan(otel_span=current_otel_span, langfuse_client=client)
                    span.score_trace(**kwargs)
            except Exception:
                pass
                
    langfuse_context = LangfuseContextWrapper()
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

        def score(self, **kwargs: Any) -> None:
            return None

        def score_trace(self, **kwargs: Any) -> None:
            return None

    langfuse_context = _DummyContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))

