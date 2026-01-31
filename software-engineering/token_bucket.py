import time
import threading

class TokenBucket:
    def __init__(self, capacity , refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.lock = threading.Lock()
        self.last_refill = time.time()


    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        added_tokens = int(elapsed * self.refill_rate) # cannot be float - production issues
        self.tokens = min(self.capacity, self.tokens + added_tokens)
        self.last_refill = now

    def allow_request(self, tokens_needed = 1):
        with self.lock:
            self._refill()
            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            return False

# example usage
if __name__ == "__main__":
    capacity = 10
    refill_rate = 2 # 2 tokens/sec
    bucket = TokenBucket(capacity=10, refill_rate=2)  # 2 tokens/sec
    for i in range(20):
        if bucket.allow_request():
            print(f"[{time.strftime('%X')}] Request {i} allowed")
        else:
            print("X==Warning==X")
            print(f"[{time.strftime('%X')}] Request {i} denied")
        time.sleep(0.2)
