from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Each process has its own data
data = np.array((rank + 1) * 10)  

# Gather data at root process
gathered_data = comm.gather(data, root=0)

if rank == 0:
    print(f"Process {rank} gathered data: {gathered_data} with data {data}")
else:
    print(f'Other process data {data}')


