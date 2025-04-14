from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from PIL import Image
import io
import base64
import litellm  # For calling gpt-4o-mini via LiteLLM

class ImageClassifierInput(BaseModel):
    image_path: str = Field(..., description="Local path to the image")
    instructions: str = Field(..., description="Instructions for classification (one-liner)")

def encode_image(image_path: str) -> str:
    with Image.open(image_path) as img:
        rgb_img = img.convert("RGB")
        buffer = io.BytesIO()
        rgb_img.save(buffer, format="JPEG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

class Base64ImageClassifierTool(BaseTool):
    name: str = "base64_image_classifier_tool"
    description: str = (
        "A tool that encodes a local image in base64 and calls gpt-4o-mini "
        "to classify the image based on provided instructions."
    )
    args_schema: Type[BaseModel] = ImageClassifierInput

    def _run(self, image_path: str, instructions: str) -> str:
        # 1. Encode the image
        base64_data = encode_image(image_path)
        data_url = f"data:image/jpeg;base64,{base64_data}"

        # 2. Construct the user message
        user_content = [
            {
                "type": "text",
                "text": instructions
            },
            {
                "type": "image_url",
                "image_url": {
                    # GPT-4o expects data URLs
                    "url": data_url
                }
            }
        ]

        # 3. Make the call to gpt-4o-mini via LiteLLM
        try:
            response = litellm.completion(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an image classification assistant. "
                                   "Follow user instructions strictly and output the classification result."
                    },
                    {
                        "role": "user",
                        "content": user_content
                    }
                ],
                temperature=0.0,  # Deterministic output
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error in classification: {str(e)}"