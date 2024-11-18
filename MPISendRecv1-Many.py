from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:   
    for i in range(1, size):
        message = f"Hello from process 0 to process {i}!"
        comm.send(message, dest=i, tag=i)
        print(f"Process {rank} sent: {message}")
else:    
    data = comm.recv(source=0, tag=rank)  # Receive from process 0
    print(f"Process {rank} received: {data}")
