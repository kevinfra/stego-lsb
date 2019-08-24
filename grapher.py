import json
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":

    name = input("enter json name: ")

    data = None
    with open(f"{name}","r") as f:
        data = json.loads(f.read())
    print(data)


    graphdata_ranges = [k for (k,v) in data.items()]
    graphdata_ssims = [v['ssim'] for (k, v) in data.items()]
    graphdata_ps2nr = [v['ps2nr'] for (k, v) in data.items()]
    graphdata_mse = [v['mse'] for (k, v) in data.items()]
    graphdata_running_times = [v['elapsed'] for (k, v) in data.items()]
    #print(graphdata)

    plt.subplot(221)
    ssims = plt.plot(graphdata_ranges, graphdata_ssims, label='SSIMs')
    plt.xlabel("LSBs used")
    plt.ylabel("SSIM")
    plt.title("SSIM")
    plt.legend()

    plt.subplot(222)
    ps2nr = plt.plot(graphdata_ranges, graphdata_ps2nr, label='PS2NRs')
    plt.xlabel("LSBs used")
    plt.ylabel("PSNR")
    plt.title("PSNR")
    plt.legend()

    plt.subplot(223)
    mse = plt.plot(graphdata_ranges, graphdata_mse, label='MSEs')
    plt.xlabel("LSBs used")
    plt.ylabel("MSE")
    plt.title("MSE")
    plt.legend()

    plt.subplot(224)
    mse = plt.plot(graphdata_ranges, graphdata_running_times, label='Running Time (s)')
    plt.xlabel("LSBs used")
    plt.ylabel("Running Time (s)")
    plt.title("Running Time (s)")
    plt.legend()

    plt.tight_layout()
    plt.show()