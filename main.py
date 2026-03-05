from cluster import start_cluster
from ingestion import load_logs
from anomaly import detect_anomaly

def main():
    # Start Dask Cluster
    client = start_cluster()

    # Load Logs
    df = load_logs("../logs/sample_logs.json")

    # Apply anomaly detection
    df["anomaly"] = df.map_partitions(
        lambda partition: partition.apply(detect_anomaly, axis=1),
        meta=("anomaly", "object")
    )

    # Compute results
    result = df.compute()

    print("\nProcessed Logs:\n")
    print(result)

    # Save only anomalies
    anomalies = result[result["anomaly"] != "NORMAL"]
    anomalies.to_csv("anomalies_output.csv", index=False)

    print("\nAnomalies saved to anomalies_output.csv")

if __name__ == "__main__":
    main()