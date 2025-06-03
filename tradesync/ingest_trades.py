from config import get_connection
from fetch_real_trade import fetch_real_trade

def ingest_trades():
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA", "JPM", "DIS"] 

    conn = get_connection()
    cur = conn.cursor()

    for symbol in symbols:
        try:
            real_trade = fetch_real_trade(symbol)

            cur.execute("""
                INSERT INTO trades (symbol, quantity, price)
                VALUES (%s, %s, %s) RETURNING id;
            """, (real_trade['symbol'], real_trade['quantity'], real_trade['price']))
            trade_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO settlements (trade_id, status, error_flag)
                VALUES (%s, %s, %s);
            """, (trade_id, 'PENDING', False))

            cur.execute("""
                INSERT INTO audit_logs (action)
                VALUES (%s);
            """, (f"Trade {trade_id} ingested for {real_trade['symbol']}",))

            conn.commit()
            print(f"Trade {trade_id} ingested successfully for {symbol}.")

        except Exception as e:
            print(f"[!] Error ingesting trade for {symbol}: {e}")
            conn.rollback()

    cur.close()
    conn.close()

if __name__ == "__main__":
    ingest_trades()
