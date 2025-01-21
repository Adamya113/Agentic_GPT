import re
import requests
import streamlit as st
from PIL import Image
from IPython.display import display
from markdownify import markdownify
from requests.exceptions import RequestException
from smolagents import (
    Tool,
    tool
)

@tool
def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.
    Args:
        url: The URL of the webpage to visit.
    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

@tool
def image_diplay_tool(image_path : str) -> object:
    """
    This is a tool that returns the image object and displays it
    Args:
        image_path: The images's path for displaying.
    """
    try:
        # Open the .webp image using Pillow
        img = Image.open(image_path)
        # Display the image
        # display(img)
        st.image(image_path)
    except Exception as e:
        print(f"Error displaying image: {e}")
    return img

image_generation_tool = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt and return its path. Make sure to improve the prompt. Another tool MUST be called for displaying image"
)
