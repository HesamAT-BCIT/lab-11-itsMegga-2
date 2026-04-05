import logging
import json
from datetime import datetime


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        if hasattr(record, "method"):
            log_entry["method"] = record.method
        if hasattr(record, "path"):
            log_entry["path"] = record.path
        if hasattr(record, "status"):
            log_entry["status"] = record.status
        if hasattr(record, "uid"):
            log_entry["uid"] = record.uid

        return json.dumps(log_entry)

# Configure logging
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())

root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(handler)