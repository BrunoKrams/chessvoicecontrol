import enum
import json
import os
from dataclasses import fields

import mask
import transformer
from model.moves.move import Move


def to_dict(obj) -> dict[str, object]:
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

class JsonGenerator:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def generate(self, move):
        with open(os.path.join(self.base_dir, "move.json"), "w", encoding="utf-8") as f:
            json.dump(to_dict(move), f, indent=4)
        with open(os.path.join(self.base_dir, "mask.json"), "w", encoding="utf-8") as f:
            json.dump(to_dict(mask.type_masks[move.type]), f, indent=4)
