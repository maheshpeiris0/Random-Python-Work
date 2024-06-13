class CustomError(Exception):
    pass

class ResourceError(CustomError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Resource:
    def __enter__(self):
        print("Resource allocated")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"An error occurred: {exc_value}")
        print("Resource released")

def process_resource():
    try:
        with Resource() as resource:
            print("Processing resource")
            raise ValueError("A processing error")
    except ValueError as e:
        raise ResourceError("Failed to process resource") from e

try:
    process_resource()
except ResourceError as e:
    print(f"Caught custom exception: {e}")
