# whileループをif条件を満たない場合は繰り返し、ifの条件が会う時のみその下の動作が作動する方法


import matplotlib.pyplot as plt
from PIL import Image
import time

i = 0
while i < 8:
    i = i + 1
    print("stay normal")
    img = Image.open('/Users/kam/Documents/Python/egg02.png')
    # img.append([plt.imshow(img)])
    img.show()

    time.sleep(2)

    if (i % 2)  == 1:
        continue

    print(i, "is even")