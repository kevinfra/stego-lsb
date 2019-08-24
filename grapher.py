import json
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":

    print("the name of the benchmark json file must be something like benchmark-still-life1.json")
    benchmark_name = input("Benchmark json image type: ")

    name1 = "benchmark-" + benchmark_name + "1.json"
    name2 = "benchmark-" + benchmark_name + "2.json"
    name3 = "benchmark-" + benchmark_name + "3.json"
    name4 = "benchmark-" + benchmark_name + "4.json"
    name5 = "benchmark-" + benchmark_name + "5.json"
    name6 = "benchmark-" + benchmark_name + "6.json"

    data1 = None
    data2 = None
    data3 = None
    data4 = None
    data5 = None
    data6 = None
    with open(f"{name1}","r") as f:
        data1 = json.loads(f.read())
    with open(f"{name2}","r") as f:
        data2 = json.loads(f.read())
    with open(f"{name3}","r") as f:
        data3 = json.loads(f.read())
    with open(f"{name4}","r") as f:
        data4 = json.loads(f.read())
    with open(f"{name5}","r") as f:
        data5 = json.loads(f.read())
    with open(f"{name6}","r") as f:
        data6 = json.loads(f.read())

    graphdata_ranges1 = [k for (k,v) in data1.items()]
    graphdata_ssims1 = [v['ssim'] for (k, v) in data1.items()]
    graphdata_ps2nr1 = [v['ps2nr'] for (k, v) in data1.items()]
    graphdata_mse1 = [v['mse'] for (k, v) in data1.items()]
    graphdata_running_times1 = [v['elapsed'] for (k, v) in data1.items()]

    graphdata_ranges2 = [k for (k,v) in data2.items()]
    graphdata_ssims2 = [v['ssim'] for (k, v) in data2.items()]
    graphdata_ps2nr2 = [v['ps2nr'] for (k, v) in data2.items()]
    graphdata_mse2 = [v['mse'] for (k, v) in data2.items()]
    graphdata_running_times2 = [v['elapsed'] for (k, v) in data2.items()]

    graphdata_ranges3 = [k for (k,v) in data3.items()]
    graphdata_ssims3 = [v['ssim'] for (k, v) in data3.items()]
    graphdata_ps2nr3 = [v['ps2nr'] for (k, v) in data3.items()]
    graphdata_mse3 = [v['mse'] for (k, v) in data3.items()]
    graphdata_running_times3 = [v['elapsed'] for (k, v) in data3.items()]

    graphdata_ranges4 = [k for (k,v) in data4.items()]
    graphdata_ssims4 = [v['ssim'] for (k, v) in data4.items()]
    graphdata_ps2nr4 = [v['ps2nr'] for (k, v) in data4.items()]
    graphdata_mse4 = [v['mse'] for (k, v) in data4.items()]
    graphdata_running_times4 = [v['elapsed'] for (k, v) in data4.items()]

    graphdata_ranges5 = [k for (k,v) in data5.items()]
    graphdata_ssims5 = [v['ssim'] for (k, v) in data5.items()]
    graphdata_ps2nr5 = [v['ps2nr'] for (k, v) in data5.items()]
    graphdata_mse5 = [v['mse'] for (k, v) in data5.items()]
    graphdata_running_times5 = [v['elapsed'] for (k, v) in data5.items()]

    graphdata_ranges6 = [k for (k,v) in data6.items()]
    graphdata_ssims6 = [v['ssim'] for (k, v) in data6.items()]
    graphdata_ps2nr6 = [v['ps2nr'] for (k, v) in data6.items()]
    graphdata_mse6 = [v['mse'] for (k, v) in data6.items()]
    graphdata_running_times6 = [v['elapsed'] for (k, v) in data6.items()]

    plt.subplot(221)
    plt.plot(graphdata_ranges1, graphdata_ssims1, label=benchmark_name + ' 1')
    plt.plot(graphdata_ranges2, graphdata_ssims2, label=benchmark_name + ' 2')
    plt.plot(graphdata_ranges3, graphdata_ssims3, label=benchmark_name + ' 3')
    plt.plot(graphdata_ranges4, graphdata_ssims4, label=benchmark_name + ' 4')
    plt.plot(graphdata_ranges5, graphdata_ssims5, label=benchmark_name + ' 5')
    plt.plot(graphdata_ranges6, graphdata_ssims6, label=benchmark_name + ' 6')
    plt.xlabel("LSBs used")
    plt.ylabel("SSIM")
    plt.title("SSIM")
    plt.legend()

    plt.subplot(222)
    plt.plot(graphdata_ranges1, graphdata_ps2nr1, label=benchmark_name + ' 1')
    plt.plot(graphdata_ranges2, graphdata_ps2nr2, label=benchmark_name + ' 2')
    plt.plot(graphdata_ranges3, graphdata_ps2nr3, label=benchmark_name + ' 3')
    plt.plot(graphdata_ranges4, graphdata_ps2nr4, label=benchmark_name + ' 4')
    plt.plot(graphdata_ranges5, graphdata_ps2nr5, label=benchmark_name + ' 5')
    plt.plot(graphdata_ranges6, graphdata_ps2nr6, label=benchmark_name + ' 6')
    plt.xlabel("LSBs used")
    plt.ylabel("PSNR")
    plt.title("PSNR")
    plt.legend()

    plt.subplot(223)
    plt.plot(graphdata_ranges1, graphdata_mse1, label=benchmark_name + ' 1')
    plt.plot(graphdata_ranges2, graphdata_mse2, label=benchmark_name + ' 2')
    plt.plot(graphdata_ranges3, graphdata_mse3, label=benchmark_name + ' 3')
    plt.plot(graphdata_ranges4, graphdata_mse4, label=benchmark_name + ' 4')
    plt.plot(graphdata_ranges5, graphdata_mse5, label=benchmark_name + ' 5')
    plt.plot(graphdata_ranges6, graphdata_mse6, label=benchmark_name + ' 6')
    plt.xlabel("LSBs used")
    plt.ylabel("MSE")
    plt.title("MSE")
    plt.legend()

    plt.subplot(224)
    plt.plot(graphdata_ranges1, graphdata_running_times1, label=benchmark_name + ' 1')
    plt.plot(graphdata_ranges2, graphdata_running_times2, label=benchmark_name + ' 2')
    plt.plot(graphdata_ranges3, graphdata_running_times3, label=benchmark_name + ' 3')
    plt.plot(graphdata_ranges4, graphdata_running_times4, label=benchmark_name + ' 4')
    plt.plot(graphdata_ranges5, graphdata_running_times5, label=benchmark_name + ' 5')
    plt.plot(graphdata_ranges6, graphdata_running_times6, label=benchmark_name + ' 6')
    plt.xlabel("LSBs used")
    plt.ylabel("Running Time (s)")
    plt.title("Running Time (s)")
    plt.legend()

    plt.tight_layout()
    plt.show()