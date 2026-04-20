import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações do projeto Sentinel GRC
registros = 1000
departamentos = ['RH', 'Financeiro', 'TI', 'Vendas', 'Operacoes']
niveis = ['Estagiario', 'Analista', 'Gerente', 'Diretor']
arquivos = ['relatorio_mensal.xlsx', 'folha_pagamento.pdf', 'codigo_fonte.git', 'lista_clientes.csv', 'planejamento_estrategico.pptx']
paises = ['Brasil', 'Brasil', 'Brasil', 'Brasil', 'EUA', 'China', 'Russia']

data_lista = []

for i in range(registros):
    data_evento = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    
    acesso = {
        'ID_Funcionario': f'FUNC{random.randint(100, 999)}',
        'Departamento': random.choice(departamentos),
        'Nivel_Acesso': random.choice(niveis),
        'Data_Hora': data_evento.strftime('%Y-%m-%d %H:%M:%S'),
        'Arquivo_Acessado': random.choice(arquivos),
        'IP_Origem': f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}',
        'Pais': random.choice(paises)
    }
    data_lista.append(acesso)

df = pd.DataFrame(data_lista)
df.to_csv('acessos_auditoria.csv', index=False)

print("✅ Base de dados 'acessos_auditoria.csv' gerada com sucesso!")
