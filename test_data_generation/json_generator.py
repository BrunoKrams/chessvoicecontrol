import enum
import json
import os
from dataclasses import fields

from . import mask


class JsonGenerator:
    INDENT = 4

    def generate(self, move):
        return {
            "move": self._to_json(move),
            "mask": self._to_json(mask.type_masks[move.type])
        }

    def _to_json(self, obj):
        return json.dumps(self._to_dict(obj), indent=self.INDENT)

    def _to_dict(self, obj) -> dict[str, object]:
        result: dict[str, object] = {}
        for f in fields(obj):
            value = getattr(obj, f.name)
            if value is None:
                continue
            if isinstance(value, enum.Enum):
                result[f.name] = value.name
            else:
                result[f.name] = value
        return result
