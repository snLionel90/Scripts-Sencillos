import speedtest
from tabulate import tabulate

class Network ( object):
    def __init__(self):
        self.parser = speedtest.Speedtest()

    def data(self):
        down = str(f"{round(self.parser.download() / 1_000_000 ,2)} Mbps")
        upld = str(f"{round(self.parser.upload() / 1_000_000 ,2)} Mbps")
        return [["Interfaz", "Download Speed", "Upload Speed"],
        ["Adapter ", down,upld]]

    def __repr__(self):
        speed = self.data()
        return tabulate(speed, headers="firtrow", tablefmt="fancy_grid")

if __name__ == "__main__":
    __author__="sn.lionel90"
    print(__author__)
    print(Network())







