from mpi4py import MPI

comm = MPI.COMM_WORLD # communicator
rank = comm.Get_rank()
if rank==0:
	print(f'Hello world...first Process')
elif rank == 1:
	print(f'Hello world...second Process')
else:
	print(f'Hello world...from others')