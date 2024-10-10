from fastapi import HTTPException

RESOURCE_NOT_FOUND = HTTPException(status_code=404, detail="resource not found")
