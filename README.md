# Background Remover API

This is a FastAPI-based web service that removes the background from uploaded images using the `rembg` library.

## Features
- Removes background from images
- Accepts image uploads via API
- Returns processed images in PNG format with transparent background

## Installation

### Prerequisites
- Python 3.8+
- `pip` installed

### Setup
```bash
# Clone the repository
git clone https://github.com/kashif2885/backgroundremover.git
cd backgroundremover

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Running the API
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)

## API Usage

### Endpoint: Remove Background
- **URL:** `/remove-background/`
- **Method:** `POST`
- **Request:** Upload an image file.
- **Response:** Returns a PNG image with the background removed.

#### Example Request Using `curl`
```bash
curl -X 'POST' \
  'http://localhost:8000/remove-background/' \
  -H 'accept: image/png' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@path_to_your_image.jpg'
```

#### Example Request Using Python
```python
import requests

url = "http://localhost:8000/remove-background/"
files = {"image": open("path_to_your_image.jpg", "rb")}
response = requests.post(url, files=files)

if response.status_code == 200:
    with open("output.png", "wb") as f:
        f.write(response.content)
    print("Background removed successfully!")
else:
    print("Error:", response.json())
```

## Running with Docker

### Build the Docker Image
```bash
docker build -t background-remover .
```

### Run the Container
```bash
docker run -p 8000:8000 background-remover
```

## Contributing
Feel free to submit issues or create pull requests to improve the project.

## License
This project is licensed under the MIT License.

