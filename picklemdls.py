#models.py
class threshmdl:
    def __init__ (self, threshold):
        self.threshold = threshold

    def determine(self, input_data):
        #assume input data is 1xn
        accept = 0
        for i in range(len(input_data)):
            if input_data[i] >= self.threshold:
                accept = 1
                break
        return accept

class n_strikes:
    def __init__ (self, threshold, n):
        self.threshold = threshold
        self.n = n

    def determine(self, input_data):
        #assume input data is 1xn
        accept = 0
        for i in range(len(input_data)):
            if input_data[i] >= self.threshold:
                accept += 1
        if accept >= self.n:
            return 1
        return 0