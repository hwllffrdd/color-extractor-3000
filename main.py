from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import numpy as np
from PIL import Image
from collections import Counter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'
Bootstrap5(app)


def extract_common_colors(image_path, num_colors=3):
    """
    Extracts the most common colors from an image.

    Parameters:
    image_path (str): The path to the image file.
    num_colors (int): The number of most common colors to return.

    Returns:
    list of str: A list containing the hexadecimal color codes of the most common colors.
    """
    image = Image.open('image.jpg')
    img_array = np.array(image)

    dtype = [('R', np.uint8), ('G', np.uint8), ('B', np.uint8)]

    structured_array = np.zeros((img_array.shape[0], img_array.shape[1]), dtype=dtype)

    structured_array['R'] = img_array[:,:,0]
    structured_array['G'] = img_array[:,:,1]
    structured_array['B'] = img_array[:,:,2]

    flattened_tuples = [tuple(row) for row in structured_array.reshape(-1)]

    counter = Counter(flattened_tuples)
    most_common_colors = counter.most_common(num_colors)

    hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in (color[0] for color in most_common_colors)]

    return hex_colors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        num_colors = int(request.form.get('num_colors', 3))
        if file and file.filename != '':
            image = Image.open(file.stream)
            colors = extract_common_colors(image, num_colors)
            return render_template('results.html', colors=colors)
        else:
            return redirect(request.url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


