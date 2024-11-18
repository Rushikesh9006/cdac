from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = "Hello from process 0!"
    comm.send(data, dest=1, tag=101)  # Process 0 sends message to Process 1
    print(f"Process {rank} sent: {data}")
elif rank == 1:
    data = comm.recv(source=0, tag=101)  # Process 1 receives message from Process 0
    print(f"Process {rank} received: {data}")
