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
    tracker1 TEXT,
    tracker2 TEXT,
    tracker3 TEXT,
    frame TEXT not NULL,
    pose TEXT not NULL,
    uid INTEGER not NULL
);