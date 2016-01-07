PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS score;
DROP TABLE IF EXISTS terminal;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS user;

CREATE TABLE game(
	name text primary key);

CREATE TABLE user(
	username text primary key);

CREATE TABLE terminal(
	id integer primary key autoincrement,
	used boolean,
	game text,
	foreign key(game) references game(name));

CREATE TABLE score (
	score integer,
	game text,
	user text,
	foreign key(user) references user(username),
	foreign key(game) references game(name));


INSERT INTO game VALUES ("Memory");
INSERT INTO game VALUES ("TicTacToe");
INSERT INTO game VALUES ("ConnectFour");
INSERT INTO game VALUES ("Dance");
INSERT INTO game VALUES ("HopScotch");
INSERT INTO game VALUES ("RunAfterTheLight");

INSERT INTO user VALUES ("Yasmine");
INSERT INTO user VALUES ("Alexandre");
INSERT INTO user VALUES ("Francois");

INSERT INTO score VALUES ("20", "TicTacToe", "Yasmine");
INSERT INTO score VALUES ("100", "TicTacToe", "Alexandre");
INSERT INTO score VALUES ("100", "TicTacToe", "Francois");

INSERT INTO terminal VALUES ("1", '0', NULL);
INSERT INTO terminal VALUES ("2", '0', NULL);

COMMIT;
