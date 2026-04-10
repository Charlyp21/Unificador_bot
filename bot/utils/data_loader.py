from pathlib import Path
import json


class DataFormatError(Exception):
    pass


def load_contacts(file_path: Path) -> dict[str, str]:
    if not file_path.exists():
        raise FileNotFoundError(f"Contacts file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if not isinstance(payload, dict):
        raise DataFormatError("Contacts JSON must be an object with name/url pairs.")

    clean_payload: dict[str, str] = {}
    for key, value in payload.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise DataFormatError("Contacts JSON entries must be strings.")
        clean_payload[key.strip()] = value.strip()

    return clean_payload

def load_community(file_path: Path) -> dict[str, str]:
    if not file_path.exists():
        raise FileNotFoundError(f"Community file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if not isinstance(payload, dict):
        raise DataFormatError("Community JSON must be an object with name/url pairs.")

    clean_payload: dict[str, str] = {}
    for key, value in payload.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise DataFormatError("Community JSON entries must be strings.")
        clean_payload[key.strip()] = value.strip()

    return clean_payload
