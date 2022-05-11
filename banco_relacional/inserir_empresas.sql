-- INSERT INTO empresas
--     (nome, cnpj)
-- VALUES
--     ('Bradesco', 111111111111111),
--     ('Vale', 000000000000000),
--     ('Cielo', 222222222222222);

INSERT INTO empresas_unidades
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);

-- ALTER TABLE empresas MODIFY cnpj VARCHAR(20);
SELECT * FROM empresas;
SELECT * FROM empresas_unidades;
SELECT * FROM cidades;
desc empresas;
