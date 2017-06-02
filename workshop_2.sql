CREATE TABLE Users(
	id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(127) UNIQUE,
    username VARCHAR(255),
    hashed_password VARCHAR(60),
    PRIMARY KEY(id)
)
