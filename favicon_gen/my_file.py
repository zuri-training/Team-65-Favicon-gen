# Set your Cloudinary credentials
# ==============================
import json
import cloudinary.api
import cloudinary.uploader
import cloudinary
from dotenv import read_dotenv
read_dotenv()

# Import the Cloudinary libraries
# ==============================

# Import to format the JSON responses
# ==============================

# Set configuration parameter: return "https" URLs by setting secure=True
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ",
      config.cloud_name, config.api_key, "\n")


def uploadImage():

    # Upload the image and get its URL
    # ==============================

    # Upload the image.
    # Set the asset's public ID and allow overwriting the asset with new versions
    cloudinary.uploader.upload("https://cloudinary-devs.github.io/cld-docs-assets/assets/images/butterfly.jpeg",
                               public_id="quickstart_butterfly", unique_filename=False, overwrite=True)

    # Build the URL for the image and save it in the variable 'srcURL's
    srcURL = cloudinary.CloudinaryImage("quickstart_butterfly").build_url()

    # Log the image URL to the console.
    # Copy this URL in a browser tab to generate the image on the fly.
    print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")


# uploadImage()
