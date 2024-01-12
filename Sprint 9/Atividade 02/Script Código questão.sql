SELECT
    idCarro,
    marcaCarro,
    modeloCarro,
    COUNT(*) AS totalLocacoes
FROM
    tb_locacao
GROUP BY
    idCarro, marcaCarro, modeloCarro
ORDER BY
    totalLocacoes DESC
LIMIT 1
