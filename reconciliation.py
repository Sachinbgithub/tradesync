from config import get_connection

def reconcile_trades():
    conn = get_connection()
    cur = conn.cursor()

    # Fetch trade id, symbol, and quantity
    cur.execute("SELECT id, symbol, quantity FROM trades;")
    trades = cur.fetchall()

    for trade_id, symbol, quantity in trades:
        if quantity <= 0:  # Example of a simple mismatch rule
            cur.execute("""
                UPDATE settlements SET status=%s, error_flag=%s WHERE trade_id=%s;
            """, ("ERROR", True, trade_id))
            cur.execute("INSERT INTO audit_logs (action) VALUES (%s);", (f"Trade {trade_id} ({symbol}) flagged for error",))
            print(f"Trade {trade_id} ({symbol}) flagged for error")
        else:
            cur.execute("""
                UPDATE settlements SET status=%s WHERE trade_id=%s;
            """, ("SETTLED", trade_id))
            cur.execute("INSERT INTO audit_logs (action) VALUES (%s);", (f"Trade {trade_id} ({symbol}) reconciled",))
            print(f"Trade {trade_id} ({symbol}) reconciled")

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    reconcile_trades()
