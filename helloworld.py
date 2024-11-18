from mpi4py import MPI


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    totalProcess = comm.Get_size()
    print(f"Hello from process {rank} from {totalProcess} process")
