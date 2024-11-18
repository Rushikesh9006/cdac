from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"Process {rank} is working...")
time.sleep(rank)  # Simulated workload varies by rank
print(f"Process {rank} has completed work.")

#comm.Barrier()# Synchronization point
print(f"Process {rank} has reached the barrier.")

# Continue with more work after the barrier
print(f"Process {rank} is proceeding after the barrier.")
