from google.cloud import vision
import io
def detect_text(path):
    """Detects text in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    texts = image.detect_text()
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

       
path='/home/athul/EY/snap.jpg'
detect_text(path)