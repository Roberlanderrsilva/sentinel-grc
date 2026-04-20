import pandas as pd

# 1. Carregar os dados
df = pd.read_csv('acessos_auditoria.csv')

# 2. Converter a coluna Data_Hora para o formato de data real
df['Data_Hora'] = pd.to_datetime(df['Data_Hora'])

# 3. Regras de GRC (Onde o filho chora e a mãe não vê!)

# Regra A: Quem está acessando de fora do Brasil?
risco_pais = df[df['Pais'] != 'Brasil']

# Regra B: Quem está trabalhando de madrugada? (entre 22h e 06h)
risco_horario = df[(df['Data_Hora'].dt.hour >= 22) | (df['Data_Hora'].dt.hour <= 6)]

# Regra C: Estagiários tentando abrir arquivos sensíveis
arquivos_criticos = ['folha_pagamento.pdf', 'codigo_fonte.git']
risco_privilegio = df[(df['Nivel_Acesso'] == 'Estagiario') & (df['Arquivo_Acessado'].isin(arquivos_criticos))]

# 4. Exibir o resultado na tela
print("\n" + "="*45)
print("🛡️  SISTEMA SENTINEL GRC - RELATÓRIO FINAL  🛡️")
print("="*45)
print(f"🚩 ALERTA: {len(risco_pais)} acessos internacionais suspeitos.")
print(f"🚩 ALERTA: {len(risco_horario)} acessos em horários críticos.")
print(f"🚩 ALERTA: {len(risco_privilegio)} violações de privilégio (Estagiários).")
print("="*45)

# 5. Salvar a lista de "suspeitos" para o RH/Segurança investigar
alertas_totais = pd.concat([risco_pais, risco_horario, risco_privilegio]).drop_duplicates()
alertas_totais.to_csv('alertas_criticos.csv', index=False)
print("✅ Lista de investigação salva em: 'alertas_criticos.csv'")
