from fastapi import UploadFile, HTTPException
from typing import List

# Allowed image MIME types
ALLOWED_IMAGE_TYPES = [
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/webp"
]

async def validate_image_upload(
    file: UploadFile,
    allowed_types: List[str] = ALLOWED_IMAGE_TYPES,
    max_size_mb: int = 5  # Optional: max size in MB
) -> None:
    # Check content type
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}"
        )

    # Check size (optional)
    file.file.seek(0, 2)  # move to end of file
    file_size = file.file.tell()
    file.file.seek(0)     # reset pointer

    max_bytes = max_size_mb * 1024 * 1024
    if file_size > max_bytes:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds {max_size_mb}MB limit."
        )
