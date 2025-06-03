import csv
from config import get_connection

def ingest_trades(csv_file='trades.csv'):
    conn = get_connection()
    cur = conn.cursor()

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO trades (symbol, quantity, price)
                VALUES (%s, %s, %s) RETURNING id;
            """, (row['symbol'], row['quantity'], row['price']))
            trade_id = cur.fetchone()[0]
            cur.execute("INSERT INTO settlements (trade_id, status) VALUES (%s, %s);", (trade_id, 'PENDING'))
            cur.execute("INSERT INTO audit_logs (action) VALUES (%s);", (f"Trade {trade_id} ingested",))

    conn.commit()
    print("Trades ingested successfully.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    ingest_trades()
