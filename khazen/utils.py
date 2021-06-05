import os
import uuid

from django.core.files import File
from django.utils import timezone


def gen_filename(instance: File, filename: str) -> str:
    """
    Generate random filename for FileField.

    This is important because the same filename being uploaded
    more than once a day causes collisions on the storage backend.

    - Note: If the filename starts with ":" it will use given file name and not random name.
            e.g, ":original_profile-2342.jpg" -> "original_profile-2342.jpg"
    """

    if filename.startswith(":"):
        filename = filename[1:]
    else:
        parts = filename.split(".")
        filename = "{0}{1}".format(uuid.uuid4().hex, f".{parts[-1]}" if len(parts) > 1 else "")

    # Create folder structure Year/Month/Day/random-filename.ext
    return os.path.join(timezone.now().strftime("%Y/%m/%d"), filename)
