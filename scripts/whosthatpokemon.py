import random
import requests
from PIL import Image
from list import pokedict
import io

# 721
UPPERLIMIT = 151
LOWERLIMIT = 1


rand_num = random.randint(LOWERLIMIT, UPPERLIMIT)
rand_pokemon = pokedict[str(rand_num)]

def get_sprite(poke_num):
    """
    Returns the sprite image content for a given Pokemon number using the PokeAPI.

    Args:
        poke_num (int): The number of the Pokemon to get the sprite for.

    Returns:
        bytes: The content of the sprite image as bytes.

    Raises:
        Exception: If the API call fails with a non-200 status code.
    """
    API_call = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_num}.png"
    value = requests.get(API_call)
    if value.status_code != 200:
        raise Exception(f"API call failed with status code {value.status_code}")
    return value.content

def create_siloutte(sprite, colour):
    """
    Creates a silhouette of the given sprite with the specified color.

    Args:
        sprite (bytes): The sprite image data.
        colour (tuple): The RGBA color tuple to use for the silhouette.

    Returns:
        Image: The silhouette image.
    """
    silloutte = Image.open(io.BytesIO(sprite)).convert('RGBA')
    pixels = silloutte.getdata()
    new_pixels = []
    for pixel in pixels:
        if pixel[3] != 0:
            new_pixels.append(colour)
        else:
            new_pixels.append(pixel)
    silloutte.putdata(new_pixels)
    return silloutte
    
def save_image(image, name):
    with open(name, 'w'):
        image.save(name)

original = get_sprite(rand_num)
siloutte = create_siloutte(original, (255, 255, 255, 255))
save_image(siloutte, 'siloutte.png')

answer = input(f"Who's that Pokemon? \n")

if answer == rand_pokemon.lower():
    print('you win!')
else:
    print('you lose!')
    print(f"the correct answer was {rand_pokemon}")

image = Image.open(io.BytesIO(original))
image.save('siloutte.png')
