import random
import time

def create_frame(data, seq):
    checkSum = sum(ord(c) for c in data) % 256
    return {
        "seq":seq,
        "data":data,
        "checksum":checkSum
    }

def is_frame_valid(frame):
    cal_sum = sum(ord(c) for c in frame["data"]) % 256
    return cal_sum == frame["checksum"]

def transmit(frames):
    i = 0
    while i < len(frames):
        frame = frames[i]
        print(f"Sending frame {frame['seq']}")
        time.sleep(1)

        corrupted_frame = frame.copy()
        if random.random() < 0.2:
            corrupted_frame["data"] = corrupted_frame["data"] + "x"

        if is_frame_valid(corrupted_frame):
            print(f"Frame {frame['seq']} received successfully")
            i += 1
        else:
            print(f"Frame {frame['seq']} corrupted, retransmitting...")

def main():
    frames = [create_frame(f"data{i}", i) for i in range(5)]
    transmit(frames)

if __name__ == "__main__":
    main()
        
        