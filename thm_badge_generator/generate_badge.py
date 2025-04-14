import requests
from PIL import Image, ImageDraw, ImageFont

# Your public TryHackMe ID
user_public_id = "3970366"

# Fetch data from THM API
url = f"https://tryhackme.com/api/v2/badges/public-profile?userPublicId={user_public_id}"
response = requests.get(url)
data = response.json()

name = data["name"]
rank = data["rank"]
points = data["points"]

# Create image
img = Image.new("RGB", (600, 100), color=(30, 30, 30))
draw = ImageDraw.Draw(img)

# Load a font (fallback to default if none available)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = ImageFont.load_default()

text = f"TryHackMe | {name} | Rank: {rank} | Points: {points}"
draw.text((10, 35), text, font=font, fill=(255, 255, 255))

# Save badge
img.save("assets/thm_badge.png")
