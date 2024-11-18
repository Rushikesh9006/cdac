from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()

if rank == 0:
    data = ['Hello',1234, 'Any text Message you want to send']
    print(f'First process sending .. {data}')
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print(f'Recieved data from first process: {data}')