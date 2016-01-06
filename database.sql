PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;

CREATE TABLE terminal(
	id integer auto increment primary key,
	used boolean,
	game text,
	foreign key(game) references game(name));

CREATE TABLE game(
	name text primary key);

CREATE TABLE users(
	username text primary key);

CREATE TABLE score (
	score integer,
	game text,
	user text,
	foreign key(user) references users(username),
	foreign key(game) references game(game));

COMMIT;
