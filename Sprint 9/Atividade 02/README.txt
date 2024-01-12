Passo a passo para transformar as tabelas conforme a modelagem dimensional proposta:

1º Tendo em vista que a tabela fato é aquela que contém dados quantitativos ou métricas do negócios, foi elaborada a Tabela Fato (FatoLocacao)

2º Já as tabelas dimensão contém informações descritivas e contextuais relacionadas aos dados, portanto as demais Tabelas trabalhadas são de Dimensão: Cliente (DimCliente), Carro (DimCarro), Combustível (DimCombustivel) e Vendedor (DimVendedor).

3º Pergunta que poderá ser respondida através da modelagem dimensional feita:

Qual carro foi mais frequentemente locado?

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

Responta:

idCarro|marcaCarro|modeloCarro|totalLocacoes|
-------+----------+-----------+-------------+
      5|Nissan    |Frontier   |            5|