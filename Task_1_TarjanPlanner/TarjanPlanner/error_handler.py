class TarjanError(Exception):
    """Custom exception class for TarjanPlanner."""
    pass

class InvalidInputError(TarjanError):
    """Raised when user input is invalid."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)
