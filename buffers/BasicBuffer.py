import numpy as np
import random
from collections import deque
from buffers import Buffer


class BasicBuffer(Buffer):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.buffer = deque(maxlen=max_size)

    def push(self, state, action, reward, next_state, done):
        experience = (state, action, np.array([reward]), next_state, done)
        self.buffer.append(experience)

    def sample(self, batch_size):
        state_batch = []
        action_batch = []
        reward_batch = []
        next_state_batch = []
        done_batch = []

        batch = random.sample(self.buffer, batch_size)
        for experience in batch:
            state, action, reward, next_state, done = experience
            state_batch.append(state)
            action_batch.append(action)
            reward_batch.append(reward)
            next_state_batch.append(next_state)
            done_batch.append(done)

        return map(lambda x: np.asarray(x), (state_batch, action_batch, reward_batch, next_state_batch, done_batch))

    def __len__(self):
        return len(self.buffer)