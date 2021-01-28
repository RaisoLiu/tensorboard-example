from torch.utils.tensorboard import SummaryWriter
import numpy as np

writer = SummaryWriter()

for n_iter in range(8):
    A = np.random.rand(10);
    B = np.array(A)
    B.sort()
    writer.add_histogram('rand/before_sort', A, n_iter)
    writer.add_histogram('rand/after_sort', B, n_iter)
