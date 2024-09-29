# Define a custom exception
class CustomException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self):
        return f"[Error {self.code}]: {self.message}"

# Example usage
try:
    raise CustomException("Something went wrong!", 404)
except CustomException as e:
    print(e)

