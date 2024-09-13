# services.py - Contains the business logic for file copying

import os
import shutil
from datetime import datetime, timedelta

class FileCopyService:
    def __init__(self, config):
        self.config = config

    def copy_files(self):
        """Copy files modified within the last 45 days."""
        last_45_days = datetime.now() - timedelta(days=45)
        for root, dirs, files in os.walk(self.config.source_directory):
            for file in files:
                src_file = os.path.join(root, file)
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(src_file))
                if file_mod_time > last_45_days:
                    self.copy_file(src_file, root, file)

    def copy_file(self, src_file, root, file):
        """Perform the actual file copy if conditions are met."""
        rel_path = os.path.relpath(src_file, self.config.source_directory)
        dest_file = os.path.join(self.config.destination_directory, rel_path)
        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
        shutil.copy2(src_file, dest_file)  # Uses copy2 to preserve metadata
        print(f"Copied: {src_file} -> {dest_file}")  # Log the copy operation
