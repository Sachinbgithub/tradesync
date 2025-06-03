# TradeSync – Post-Trade Reconciliation System

## Features
- Simulates trade ingestion from CSV files and real-time market data via Alpha Vantage API
- Stores trades, settlement statuses, error flags, and audit logs in PostgreSQL
- Validates trades for mismatches and flags errors in settlements
- Generates detailed audit logs with trade information for traceability
- Provides a CLI interface to ingest trades, reconcile them, and view audit logs
- Automated reconciliation simulated via shell scripts and cron jobs

## How to Use
1. Create PostgreSQL database and run the schema setup script `db_setup.sql`
2. Update database credentials in `config.py`
3. (Optional) Configure Alpha Vantage API key in `fetch_real_trade.py` to ingest live trade data
4. Add trade data to `trades.csv` or use live API ingestion
5. Run the CLI tool:
    ```bash
    python3 main.py
    ```

## Dependencies
- Python 3.x
- PostgreSQL
- Python packages: `psycopg2-binary`, `requests`

## Automation
To simulate scheduled reconciliation runs, use the shell script:
```bash
./schedule_reconciliation.sh
