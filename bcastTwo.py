from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = None
if rank == 0:
    data = [10,20,30,40]  
data = comm.bcast(data, root=0)
print(f"Process {rank} received: {data}")
