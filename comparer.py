import datetime
import os
from stego import hide, decode, formulas
import json

if __name__ == "__main__":
    img = input("Image to benchmark: ")
    text = input("Text to hide: ")

    results = {}
    print("Beginning benchmark...")
    for i in range(2,9):

        print(f"-- {i} bytes --")

        before_size = os.path.getsize(img)
        now = datetime.datetime.now()
        hide.hide(img, text, i)
        after = datetime.datetime.now() - now
        after_size = os.path.getsize(img.replace(".bmp","-stego.bmp"))
        comparison = formulas.compare(img, img.replace(".bmp","-stego.bmp"))

        results[i] = {
            "before_size": before_size,
            "after_size": after_size,
            "elapsed": after.total_seconds(),
            "mse": comparison[0],
            "ps2nr": comparison[1],
            "ssim": comparison[2]
        }
        print(f"Took {after.total_seconds()} seconds..")
    out = json.dumps(results)
    with open("benchmark.json", 'w') as f:
        f.write(out)