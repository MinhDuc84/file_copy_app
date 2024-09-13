# config.py - Manages configuration settings

class AppConfig:
    def __init__(self, source_directory, destination_directory, interval):
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.interval = interval

    @staticmethod
    def load():
        # In a real scenario, this might load from a file or environment variables
        return AppConfig("/path/to/source", "/path/to/destination", 60)  # Example path and interval

    def save(self):
        # Save config to a file or database if needed
        pass
