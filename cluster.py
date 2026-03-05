from dask.distributed import Client

def start_cluster():
    client = Client(n_workers=2, threads_per_worker=2)
    print("Dask Cluster Started Successfully")
    return client