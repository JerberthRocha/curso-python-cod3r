-- INSERT INTO cidades(nome, area, estado_id)
-- VALUES ('Niterói', 499, 19)

-- INSERT INTO cidades
--     (nome, area, estado_id)
-- VALUES 
--     ('Juazeiro do Norte', 
--     220.9, 
--     (SELECT id FROM estados WHERE sigla = 'CE')
-- )


Select * from cidades

-- update cidades
-- set nome = 'Godofredo Viana', area = 221
-- where id = 3