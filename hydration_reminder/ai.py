# For now, I'm commenting out all related to Google GenAI, as I need to work on the error message
# [ERROR] Runtime.ImportModuleError: Unable to import module 'main': No module named 'pydantic_core._pydantic_core'


# from google.genai import Client


def generate_text() -> str:
    """
    Generate a short, funny sentence reminding someone to drink water
    """
    # client = Client(api_key=GOOGLE_API_KEY)
    # response = client.models.generate_content(
    #    model="gemini-2.5-flash",
    #    contents="Write a short, funny sentence (15 words or fewer) reminding someone to drink water. It should be playful, clever, and inspired by the Kraken myth or oceanic themes. No emojis.",
    # )

    return "Please, drink some water :)"  # Placeholder response for now
