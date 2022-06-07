INSERT INTO login VALUES(1,'xyz@gmail.com','123456');

INSERT INTO tb_ecological_class VALUES( 1, "pioneira" );
INSERT INTO tb_ecological_class VALUES( 2, "secundaria" );
INSERT INTO tb_ecological_class VALUES( 3, "climax" );

INSERT INTO tb_botanical_family VALUES( 1, "Arecaceae" );
INSERT INTO tb_botanical_family VALUES( 2, "Fabaceae" );
INSERT INTO tb_botanical_family VALUES( 3, "Lecythidaceae" );
INSERT INTO tb_botanical_family VALUES( 4, "Meliaceae" );
INSERT INTO tb_botanical_family VALUES( 5, "Bignoniaceae" );

INSERT INTO tb_trees VALUES( 1, "Euterpe precatoria", 20, 3, 1 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Açai da Mata", 1 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Açai Solteiro", 1 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Açai do Para", 1 );

INSERT INTO tb_trees VALUES( 2, "Handroanthus heptaphyllus", 20, 2 , 5 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Ipe Roxo", 2 );

INSERT INTO tb_trees VALUES( 3, "Schizolobium amazonicum", 40, 1, 2 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Paricá", 3 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Pinho Cuiabano", 3 );

INSERT INTO tb_trees VALUES( 4, "Stryphnodendron pulcherrimum", 15, 1, 2 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Baginha", 4 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Falso Barbatimão", 4 );

INSERT INTO tb_trees VALUES( 5, "Bertholletia excelsa", 30, 3 , 3);
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Castanha da Amazônia", 5 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Castanheira do Brasil", 5 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Castanha do Para", 5 );

INSERT INTO tb_trees VALUES( 6, "Cedrela fissilis", 40, 2, 4 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Cedro Vermelho", 6 );
INSERT INTO tb_popular_names ( popular_name, tree ) VALUES( "Cedro Roxo", 6 );


SELECT scientific_name, height_max ,e.ecological_class, f.botanical_family,
( SELECT popular_name FROM tb_popular_names WHERE tree = t.id)
FROM tb_trees t
LEFT JOIN tb_ecological_class e ON e.id = t.ecological_class
LEFT JOIN tb_botanical_family f ON e.id = f.botanical_family;