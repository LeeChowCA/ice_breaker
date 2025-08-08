import os

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("This is the ice breaker module.")
    print(os.getenv('OPENAI_API_KEY'))  # Example usage of the environment variable