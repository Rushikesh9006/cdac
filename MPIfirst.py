from mpi4py import MPI
import numpy as np

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    start = MPI.Wtime()
    arr = np.ones(1000)
    end = MPI.Wtime()
    
    numProc = comm.Get_size()
    rank = comm.Get_rank()
    if rank == 0:
        print(f'Time taken: {end-start}')
        #print(f'{rank} --> arr: {arr}')
    #else:
        #print(f'{rank} --> arr: {arr}')