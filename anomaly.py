def detect_anomaly(row):
    if row["response_time_ms"] > 2000:
        return "HIGH_LATENCY"
    elif row["status_code"] >= 500:
        return "SERVER_ERROR"
    elif row["log_level"] == "ERROR":
        return "APPLICATION_ERROR"
    else:
        return "NORMAL"