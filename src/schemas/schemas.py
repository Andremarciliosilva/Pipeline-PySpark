from pyspark.sql.types import *

clientes_schema = StructType([
    StructField("cliente_id", IntegerType(), True),
    StructField("cpf", StringType(), True),
    StructField("data_cadastro", TimestampType(), True),
    StructField("data_nascimento", DateType(), True),
    StructField("nome", StringType(), True),
    StructField("renda_mensal", DecimalType(10,2), True),
    StructField("score_credito", IntegerType(), True),
    StructField("sexo", StringType(), True),
])

contas_schema = StructType([
    StructField("agencia", StringType(), True),
    StructField("cliente_id", StringType(), True),
    StructField("conta_id", StringType(), True),
    StructField("data_abertura", TimestampType(), True),
    StructField("saldo_atual", DoubleType(), True),
    StructField("tipo_conta", StringType(), True), 
])

transacao_schema = StructType([
    StructField("canal", StringType(), True),
    StructField("conta_id", StringType(), True),
    StructField("data_transacao", TimestampType(), True),
    StructField("status", StringType(), True),
    StructField("tipo_transacao", StringType(), True),
    StructField("transacao_id", StringType(), False),
    StructField("valor", DoubleType(), True)
    ])

enderecos_schema = StructType([
    StructField("cep", StringType(), True),
    StructField("cidade", StringType(), True),
    StructField("cliente_id", StringType(), True),
    StructField("endereco_id", IntegerType(), True),
    StructField("estado", StringType(), True),
    StructField("logradouro", StringType(), True)
])

cartoes_schema = StructType([
    StructField("cartao_id", StringType(), True),
    StructField("cliente_id", StringType(), True),
    StructField("limite_disponivel", DoubleType(), True),
    StructField("limite_total", DoubleType(), True),
    StructField("tipo_cartao", StringType(), True)
])

contratos_schema = StructType([
    StructField("cliente_id", StringType(), True),
    StructField("contrato_id", IntegerType(), True),
    StructField("data_inicio", TimestampType(), True),
    StructField("prazo_meses", IntegerType(), True),
    StructField("status", StringType(), True),
    StructField("taxa_juros", DoubleType(), True),
    StructField("tipo_credito", StringType(), True),
    StructField("valor_total", DoubleType(), True),
    
    
    
    
])