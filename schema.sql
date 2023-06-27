DROP TABLE IF EXISTS players;

CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timeCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    rank TEXT NOT NULL,
    level INTEGER not NULL,
    platform TEXT not NULL,
    legend TEXT not NULL,
    badge1 TEXT,
    badge2 TEXT,
    badge3 TEXT,
    tracker_name1 TEXT,
    tracker_name2 TEXT,
    tracker_name3 TEXT,
    tracker_value1 INTEGER,
    tracker_value2 INTEGER,
    tracker_value3 INTEGER,
    frame TEXT not NULL,
    pose TEXT not NULL,
    uid INTEGER not NULL
);