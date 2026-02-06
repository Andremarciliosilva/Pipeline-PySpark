import data

num_registros = 1000

data.save_df_to_csv(data.generate_client_data(num_registros), "data/raw/clientes")

data.save_df_to_csv(data.generate_address_data(num_registros), "data/raw/enderecos")

data.save_df_to_csv(data.generate_account_data(num_registros), "data/raw/contas")

data.save_df_to_csv(data.generate_card_data(num_registros), "data/raw/cartoes")

data.save_df_to_csv(data.generate_transaction_data(num_registros), "data/raw/transacoes")

data.save_df_to_csv(data.generate_credit_contract_data(num_registros), "data/raw/contratos_credito")

data.rename_csvs("data/raw", "data/raw")

# data.save_clients_to_csv(data.generate_address_data(num_registros), "data/raw/enderecos.csv")
# data.rename_spark_csv("data/raw", "data/raw/enderecos.csv")