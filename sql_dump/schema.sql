-- Arvore
--	* Nome Cientifico
-- 	* Nomes Populares
-- 	* Altura Máxima
--	* Classe Ecologica
--	* Familia Botanica

CREATE TABLE tb_ecological_class(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	ecological_class TEXT
);

CREATE TABLE tb_botanical_family(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	botanical_family TEXT
);

CREATE TABLE tb_trees(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	scientific_name TEXT,
	height_max REAL,
	ecological_class INTEGER,
	botanical_family INTEGER,
    FOREIGN KEY (ecological_class) REFERENCES tb_ecological_class(id),
	FOREIGN KEY (botanical_family) REFERENCES tb_botanical_family(id)
);

CREATE TABLE tb_popular_names(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	popular_name TEXT,
	tree INTEGER,
	FOREIGN KEY (tree) REFERENCES trees(id)
);
