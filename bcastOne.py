from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = None
if rank == 0:
    data = f'Message to be sent from process {rank}'  
data = comm.bcast(data, root=0)
print(f"Process {rank} received: {data}")
