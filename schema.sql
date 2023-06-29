DROP TABLE IF EXISTS players;

CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timeCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    rank TEXT NOT NULL,
    rankDiv int not NULL,
    level INTEGER not NULL,
    platform TEXT not NULL,
    legend TEXT not NULL,
    badge1 TEXT DEFAULT Null,
    badge2 TEXT DEFAULT Null,
    badge3 TEXT DEFAULT Null,
    tracker_name1 TEXT DEFAULT Null,
    tracker_name2 TEXT DEFAULT Null,
    tracker_name3 TEXT DEFAULT Null,
    tracker_value1 INTEGER DEFAULT Null,
    tracker_value2 INTEGER DEFAULT Null,
    tracker_value3 INTEGER DEFAULT Null,
    frame TEXT not NULL,
    pose TEXT not NULL,
    uid INTEGER not NULL
);