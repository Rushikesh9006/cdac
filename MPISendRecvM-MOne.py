from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank % 2 == 0:  # Even-ranked processes
    # Send a message to all odd-ranked processes
    for dest in range(1, size, 2):  # Send to odd ranks only
        message = f"Hello from even process {rank}!"
        comm.send(message, dest=dest, tag=rank)
        print(f"Process {rank} sending to {dest} sent: {message}")

comm.Barrier() # synchronization 

if rank % 2 == 1:  # Odd-ranked processes
    # Receive messages from even-ranked processes
    for source in range(0,size,2):
        data = comm.recv(source=source, tag=MPI.ANY_TAG)  # Receive from any even process
        print(f"Process {rank} received: {data}")
