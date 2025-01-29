from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.post("/remove-background/")
async def remove_background(image: UploadFile = File(...)):
    """
    API endpoint to remove background from an uploaded image.
    :param image: The uploaded image file.
    :return: The image with the background removed.
    """
    try:
        # Ensure the uploaded file is an image
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

        # Read image content
        image_data = await image.read()

        # Process the image to remove the background
        input_image = Image.open(BytesIO(image_data))
        output_image_data = remove(image_data)

        # Convert the output data to an image format
        output_image = Image.open(BytesIO(output_image_data)).convert("RGBA")

        # Save the output to a BytesIO object
        output_buffer = BytesIO()
        output_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)

        # Return the image as a StreamingResponse
        return StreamingResponse(output_buffer, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
