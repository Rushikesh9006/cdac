from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank % 2 == 0:  # 0,1,2,3,4,5--> 0,2,4 --> 1,3,5
    message = f"Hello from even process {rank}!"
    comm.send(message, dest=rank + 1, tag=rank)
    print(f"Process {rank} sending to {rank + 1} sent: {message}")

comm.Barrier() # synchronization 

if rank % 2 == 1:  # Odd-ranked processes    
    data = comm.recv(source=rank - 1, tag=MPI.ANY_TAG) 
    print(f"Process {rank} received: {data}")
