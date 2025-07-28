import os
from dotenv import load_dotenv
load_dotenv()

# Unset the OpenAI API key to force CrewAI to use the local model
try:
    del os.environ['OPENAI_API_KEY']
except KeyError:
    print("OpenAI API key not found in environment. Proceeding with local model.")

from crew import ProductCrew


def run():
    # Replace with your inputs, it can be a json, a csv file or a text file.
    inputs = {
        'product_topic': 'AI-powered noise-cancelling headphones',
        'product_description': 'A new line of headphones that uses AI to adapt noise cancellation to the user\'s environment in real-time. It also features a unique transparency mode that intelligently filters in important sounds.'
    }
    ProductCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
