Passo a passo realizado para realizar a normalização da tabela tb_locacao.

1º Identificar Dependências Funcionais:
Análise da tabela e identificação das dependências funcionais entre as colunas.
Exemplos de dependências funcionais identificadas: idCliente determinando nomeCliente, cidadeCliente, etc.
Remover Redundâncias:

2º Verificar a existência de colunas que podem ser derivadas de outras. 

3º Para dados categóricos como marcaCarro, modeloCarro, tipoCombustivel, por exemplo, foram criadas tabelas de referência separadas e usadas chaves estrangeiras na tabela principal.
Assim a tabela foi dividida em Partes Menores cada uma representando uma entidade específica (ex: locacao, cliente, carro, vendedor e combustivel).

4º Garantir Integridade Referencial:
Ao criar chaves estrangeiras, foi certificado de que a integridade referencial fosse mantida, pois não é possível ter uma referência para um valor que não existe na tabela de origem.

5º Atualizar Relacionamentos:
Para garanta que os relacionamentos entre as tabelas estivessem corretos, com chaves estrangeiras sendo usadas adequadamente.