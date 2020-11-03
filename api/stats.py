from . import api
from multiprocessing import Process
import pickle

import psutil
import time

interface = ""
up = [0, 0]
down = [0, 0]

class processClass:
    def __init__(self):
        p = Process(target=self.run, args=())
        p.daemon = True
        p.start()

    def run(self):
        if list(psutil.net_io_counters(pernic=True).keys())[0] == "lo":
            interface = list(psutil.net_io_counters(pernic=True).keys())[1]
        else:
            interface = list(psutil.net_io_counters(pernic=True).keys())[0]

        while True:
            stats = psutil.net_io_counters(pernic=True)[interface]
            up[1] = up[0]
            up[0] = stats.bytes_sent
            down[1] = down[0]
            down[0] = stats.bytes_recv
            with open('stats.pickle', 'wb') as f:
                pickle.dump([interface, up, down], f, protocol=pickle.HIGHEST_PROTOCOL)
            time.sleep(1)

    def get_stats(self):
        print(interface)
        return up

stats_class = processClass()

@api.route("/stats")
def stats():
    with open('stats.pickle', 'rb') as f:
        stats = pickle.load(f)
        global interface, up, down
        interface = stats[0]
        up = stats[1]
        down = stats[2]
    
    print(stats)
    return "Yay, stats!"
