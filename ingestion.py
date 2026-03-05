import dask.dataframe as dd

def load_logs(file_path):
    df = dd.read_json(file_path, lines=True)
    print("Logs Loaded Successfully")
    return df