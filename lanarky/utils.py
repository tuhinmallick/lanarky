from typing import Any

import pydantic
from pydantic.fields import FieldInfo

PYDANTIC_V2 = pydantic.VERSION.startswith("2.")


def model_dump(model: pydantic.BaseModel, **kwargs) -> dict[str, Any]:
    """Dump a pydantic model to a dictionary.

    Args:
        model: A pydantic model.
    """
    return model.model_dump(**kwargs) if PYDANTIC_V2 else model.dict(**kwargs)


def model_dump_json(model: pydantic.BaseModel, **kwargs) -> str:
    """Dump a pydantic model to a JSON string.

    Args:
        model: A pydantic model.
    """
    return model.model_dump_json(**kwargs) if PYDANTIC_V2 else model.json(**kwargs)


def model_fields(model: pydantic.BaseModel) -> dict[str, FieldInfo]:
    """Get the fields of a pydantic model.

    Args:
        model: A pydantic model.
    """
    return model.model_fields if PYDANTIC_V2 else model.__fields__
