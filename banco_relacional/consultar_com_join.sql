-- select 
--     e.nome as Estado, 
--     c.nome as Cidade, 
--     e.regiao as Região 
-- from estados e, cidades c
-- where e.id = c.estado_id

SELECT
    c.nome AS Cidade,
    e.nome AS Estado,
    regiao AS Região
FROM estados e 
INNER JOIN cidades c ON e.id = c.estado_id