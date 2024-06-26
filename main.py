import numpy as np
from PIL import Image
from collections import Counter

image = Image.open('image.jpg')
img_array = np.array(image)

dtype = [('R', np.uint8), ('G', np.uint8), ('B', np.uint8)]

structured_array = np.zeros((img_array.shape[0], img_array.shape[1]), dtype=dtype)

structured_array['R'] = img_array[:,:,0]
structured_array['G'] = img_array[:,:,1]
structured_array['B'] = img_array[:,:,2]

flattened_tuples = [tuple(row) for row in structured_array.reshape(-1)]

counter = Counter(flattened_tuples)

first_value = counter.most_common(3)[0][0]
second_value = counter.most_common(3)[1][0]
third_value = counter.most_common(3)[2][0]

r1, g1, b1 = first_value
r2, g2, b2 = second_value
r3, g3, b3 = third_value

hex_color_first = f"#{r1:02x}{g1:02x}{b1:02x}"
hex_color_second = f"#{r2:02x}{g2:02x}{b2:02x}"
hex_color_third = f"#{r3:02x}{g3:02x}{b3:02x}"

print(hex_color_first)
print(hex_color_second)
print(hex_color_third)


