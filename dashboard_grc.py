import plotly.express as px
import pandas as pd

# Dados que seu robô encontrou
data = {
    'Tipo de Risco': ['Acessos Internacionais', 'Horários Críticos', 'Violação de Privilégio'],
    'Total de Alertas': [451, 361, 101],
    'Nivel_Gravidade': ['Alto', 'Médio', 'Crítico']
}

df_radar = pd.DataFrame(data)

# Criando o gráfico
fig = px.bar(df_radar, 
             x='Tipo de Risco', 
             y='Total de Alertas',
             color='Nivel_Gravidade',
             color_discrete_map={'Alto': 'orange', 'Médio': 'yellow', 'Crítico': 'red'},
             title='Análise de Riscos e Compliance - Sentinel GRC',
             text_auto=True)

# Ajustando o visual para ficar "dark" e profissional
fig.update_layout(template='plotly_dark')

# Salvando a imagem
fig.write_image("dashboard_grc.png")
print("📊 Gráfico 'dashboard_grc.png' gerado com sucesso!")
