import random

total_frames = 8
window_size = 4
loss_prob = 0.3

class Receiver:
    def __init__(self):
        self.expected = 0
    
    def receive(self, frame):
        if frame == self.expected:
            print(f"Receiver: Got frame {frame}")
            self.expected += 1
            return True
        else:
            print(f"Receiver: Discarded frame {frame} (expected {self.expected})")
            return False
        
def simulate():
    sender_base = 0
    receiver = Receiver()
    while sender_base < total_frames:
        print(f"Sender Window: {list(range(sender_base, min(sender_base + window_size, total_frames)))}")
        for i in range(sender_base, min(sender_base + window_size, total_frames)):
            if random.random() < loss_prob:
                print(f"Sender: Frame {i} lost")
                break

            success = receiver.receive(i)
            if not success:
                break
            
        if receiver.expected > sender_base:
            sender_base = receiver.expected
        else:
            print("Timeout - Resending window")

simulate()
            
    
