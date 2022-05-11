-- select e.nome, c.nome, e.regiao from estados e, cidades c
-- where e.id = c.estado_id
-- select * from prefeitos;
select * from cidades c inner join prefeitos p on c.id = p.cidade_id;
select * from cidades c left join prefeitos p on c.id = p.cidade_id;
select * from cidades c right join prefeitos p on c.id = p.cidade_id;

-- MYSQL NÃO SUPORTA O FULL JOIN. 
-- FAZENDO UM UNION DO LEFT JOIN E RIGHT JOIN EQUIVALE AO FULL JOIN
select * from cidades c left join prefeitos p on c.id = p.cidade_id
union
select * from cidades c right join prefeitos p on c.id = p.cidade_id;