Passo a passo:

1º Tabelas normalizadas (filmes, artistas e avaliacoes) em formato csv na Trusted zone do bucket no S3.

2º Código no AWS glue para enviar os arquivos em formato csv da Trusted zone para a Refined zone em formato parquet.

3º Job04 rodou com sucesso e os arquivos foram salvos na Refined zone.

4º Criação dos crawlers.

5º Crawlers rodaram com sucesso.

6º Criação banco de dados no Athena.

7º Arquivos do Refined zone abertos no Athena.