CREATE TABLE trades (
    trade_id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    quantity INTEGER,
    price DECIMAL(10, 2),
    trade_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE settlements (
    trade_id INTEGER REFERENCES trades(trade_id),
    status VARCHAR(20),
    error_flag BOOLEAN DEFAULT FALSE
);

CREATE TABLE audit_logs (
    log_id SERIAL PRIMARY KEY,
    action TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
