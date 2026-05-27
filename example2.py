import time

while True:
    words = ["hello","world","beagle","sturgeon","motorcycle"]

    for i in words:
        print(i, end="",flush=True)
        time.sleep(2)
        counter = len(i)
        while counter>0:
            print(" \b\b",end="",flush=True)
            counter-=1
            time.sleep(1)
        print(" "*len(i) + "\b"*len(i), end="")