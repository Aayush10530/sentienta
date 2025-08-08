import hashlib
import json
from typing import Any, Dict

class DummyModel:
    def __init__(self, version: str = "v1"):
        self.version = version

    def _hash_input(self, payload: Any) -> int:
        s = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        h = hashlib.sha256(s.encode("utf-8")).hexdigest()
        return int(h[-8:], 16)

    def predict(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        base = self._hash_input(payload)
        probability = ((base % 10000) / 10000.0)
        klass = "positive" if (base % 2 == 0) else "negative"
        return {
            "model_version": self.version,
            "input_summary": {"keys": list(payload.keys())},
            "prediction": {"class": klass, "score": round(probability, 4)}
        }