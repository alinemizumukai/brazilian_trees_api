INSERT INTO login VALUES(1,'xyz@gmail.com','123456');

INSERT INTO tb_ecological_class VALUES( 1, "pioneira" );
INSERT INTO tb_ecological_class VALUES( 2, "secundaria" );
INSERT INTO tb_ecological_class VALUES( 3, "climax" );

INSERT INTO tb_botanical_family VALUES( 1, "Arecaceae" );
INSERT INTO tb_botanical_family VALUES( 2, "Fabaceae" );
INSERT INTO tb_botanical_family VALUES( 3, "Lecythidaceae" );
INSERT INTO tb_botanical_family VALUES( 4, "Meliaceae" );
INSERT INTO tb_botanical_family VALUES( 5, "Bignoniaceae" );

INSERT INTO tb_trees VALUES( 1, "Mouritia flexuosa", "Buriti", 25, 3, 1 );

INSERT INTO tb_trees VALUES( 2, "Hymenaea courbaril", "Jatobá", 45, 3 , 2 );

INSERT INTO tb_trees VALUES( 3, "Schizolobium amazonicum", "Paricá", 40, 1, 2 );

INSERT INTO tb_trees VALUES( 4, "Stryphnodendron pulcherrimum", "Baginha", 15, 1, 2 );

INSERT INTO tb_trees VALUES( 5, "Bertholletia excelsa", "Castanha da Amazônia", 30, 3 , 3);

INSERT INTO tb_trees VALUES( 6, "Cedrela fissilis", "Cedro Vermelho", 40, 2, 4 );

SELECT t.scientific_name, t.popular_name, height_max ,e.ecological_class, f.botanical_family
FROM tb_trees t
LEFT JOIN tb_ecological_class e ON e.id = t.ecological_class
LEFT JOIN tb_botanical_family f ON f.id = t.botanical_family;