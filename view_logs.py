from config import get_connection

def view_audit_logs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, action, log_time FROM audit_logs ORDER BY log_time DESC LIMIT 20;")
    logs = cur.fetchall()

    print("\n📜 Last 20 Audit Logs:")
    for log in logs:
        print(f"[{log[2]}] (ID {log[0]}) - {log[1]}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    view_audit_logs()
