# TradeSync – Post-Trade Reconciliation System

## Features
- Simulates trade ingestion via CSV
- Stores data in PostgreSQL
- Validates trades for mismatches
- Generates audit logs
- Automated reconciliation via shell script

## How to Use
1. Create database and run `db_setup.sql`
2. Update DB credentials in `config.py`
3. Add trade data to `trades.csv`
4. Run CLI:
    ```bash
    python3 main.py
    ```

## Dependencies
- Python 3
- PostgreSQL
- psycopg2

## Automation
You can simulate scheduled runs with:
```bash
./schedule_reconciliation.sh
