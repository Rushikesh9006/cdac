from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = np.array([10, 20, 30, 40])  
    data = np.array_split(data, size)  
else:
    data = None

# Scatter the data to all processes
data = comm.scatter(data, root=0)

print(f"Process {rank} received: {data}")

