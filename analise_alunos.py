import altair as alt
import pandas as pd
import streamlit as st

# Configurações da página
st.set_page_config(page_title="Analise de Alunos", layout="wide")
st.title("Analise de Desempenho dos Alunos")

# Carregar os dados dos alunos
df = pd.read_excel("alunos_notas.xlsx")
alunos = df.set_index("Aluno").T.to_dict(orient="list")

# Processar os dados para análise
df = pd.DataFrame(alunos).T
df.columns = ["nota1", "nota2", "nota3", "nota4",]
df["media"] = df.mean(axis=1).round(2)
df["desvio_padrao"] = df[["nota1", "nota2", "nota3", "nota4"]].std(axis=1).round(2)
df["amplitude"] = (
    df[["nota1", "nota2", "nota3", "nota4"]].max(axis=1)
    - df[["nota1", "nota2", "nota3", "nota4"]].min(axis=1)
).round(2)
df["evolucao_nota1_para_nota4"] = (df["nota4"] - df["nota1"]).round(2)

# Exibir a tabela de notas
st.subheader("Tabela de Notas")
st.dataframe(df, use_container_width=True, height=280)

# Configurar o corte de aprovação
corte_aprovacao = st.slider("Corte de aprovacao (média)", 0.0, 10.0, 7.0, 0.5)

# Calcular métricas de aprovação
aprovados = int((df["media"] >= corte_aprovacao).sum())
reprovados = int((df["media"] < corte_aprovacao).sum())
taxa_aprovacao = round((aprovados / len(df)) * 100, 2)

# Exibir métricas de aprovação
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Alunos", len(df))
col2.metric("Aprovados", aprovados)
col3.metric("Reprovados", reprovados)
col4.metric("Taxa de Aprovação", f"{taxa_aprovacao:.0f}%")

# Preparar dados para visualizações
media_df = (
    df["media"]
    .sort_values(ascending=False)
    .rename_axis("aluno")
    .reset_index(name="media")
)

# Calcular o ângulo para o gráfico de rosca
media_df["angulo"] = media_df["media"] / media_df["media"].sum() * 2 * 3.141592653589793

# Preparar dados para gráfico de barras de consistência
consistencia_df = (
    df[["desvio_padrao", "amplitude"]]
    .sort_values(by="desvio_padrao")
    .reset_index()
    .rename(columns={"index": "aluno"})
    .melt(id_vars="aluno", var_name="metrica", value_name="valor")
)

# Preparar dados para gráfico de barras de evolução
evolucao_df = (
    df["evolucao_nota1_para_nota4"]
    .sort_values(ascending=False)
    .rename_axis("aluno")
    .reset_index(name="evolucao")
)

# Classificar evolução como positiva ou negativa
evolucao_df["status"] = evolucao_df["evolucao"].apply(lambda x: "Positiva" if x >= 0 else "Negativa")

# Preparar dados para gráfico de barras de situação
situacao_df = (
    df["media"]
    .sort_values(ascending=False)
    .rename_axis("aluno")
    .reset_index(name="media")
)

# Classificar situação como aprovado ou reprovado
situacao_df["situacao"] = situacao_df["media"].apply(
    lambda x: "Aprovado" if x >= corte_aprovacao else "Reprovado"
)

# Visualizações
st.subheader("Dashboard")
col_a, col_b = st.columns(2)
col_c, col_d = st.columns(2)

# Gráfico de rosca para média dos alunos
with col_a:
    donut = alt.Chart(media_df).mark_arc(innerRadius=60).encode(
        theta=alt.Theta("media:Q"),
        color=alt.Color("aluno:N", legend=alt.Legend(title="Alunos")),
        tooltip=["aluno:N", alt.Tooltip("media:Q", format=".2f")],
    ).properties(title="Média de Cada Aluno (Máximo 10)", height=320)
    st.altair_chart(donut, use_container_width=True)

# Gráfico de barras para consistência (desvio padrão e amplitude)
with col_b:
    consistencia = alt.Chart(consistencia_df).mark_bar().encode(
        x=alt.X("aluno:N", sort=None, title="Aluno"),
        y=alt.Y("valor:Q", title="Valor"),
        color=alt.Color("metrica:N", title="Metrica"),
        xOffset="metrica:N",
        tooltip=["aluno:N", "metrica:N", alt.Tooltip("valor:Q", format=".2f")],
    ).properties(title="Consistência por Aluno", height=320)
    st.altair_chart(consistencia, use_container_width=True)

# Gráfico de barras para evolução (nota1 para nota4)
with col_c:
    evolucao = alt.Chart(evolucao_df).mark_bar().encode(
        x=alt.X("aluno:N", sort=None, title="Aluno"),
        y=alt.Y("evolucao:Q", title="Variação"),
        color=alt.Color(
            "status:N",
            scale=alt.Scale(domain=["Positiva", "Negativa"], range=["#2ca02c", "#d62728"]),
            legend=alt.Legend(title="Evolução"),
        ),
        tooltip=["aluno:N", alt.Tooltip("evolucao:Q", format=".2f"), "status:N"],
    ).properties(title="Evolução: Nota1 -> Nota4", height=320)
    linha_zero = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(color="black").encode(y="y:Q")
    st.altair_chart(evolucao + linha_zero, use_container_width=True)

# Gráfico de barras para situação (aprovado ou reprovado)
with col_d:
    situacao = alt.Chart(situacao_df).mark_bar().encode(
        x=alt.X("aluno:N", sort=None, title="Aluno"),
        y=alt.Y("media:Q", title="Média", scale=alt.Scale(domain=[0, 10])),
        color=alt.Color(
            "situacao:N",
            scale=alt.Scale(domain=["Aprovado", "Reprovado"], range=["#2ca02c", "#d62728"]),
            legend=alt.Legend(title="Situação"),
        ),
        tooltip=["aluno:N", alt.Tooltip("media:Q", format=".2f"), "situacao:N"],
    ).properties(title=f"Situação por Aluno (Corte: média >= {corte_aprovacao})", height=320)
    st.altair_chart(situacao, use_container_width=True)


