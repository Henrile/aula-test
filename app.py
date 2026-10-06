import streamlit as st


st.set_page_config(page_title="Calculadora", page_icon="🧮")
st.title("Calculadora básica")
st.write("Faça operações de adição, subtração, multiplicação e divisão.")

operacao = st.selectbox(
	"Operação",
	["Adição (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"]
)

col1, col2 = st.columns(2)
with col1:
	numero1 = st.number_input("Primeiro número", value=0.0)
with col2:
	numero2 = st.number_input("Segundo número", value=0.0)

if st.button("Calcular"):
	if operacao == "Adição (+)":
		resultado = numero1 + numero2
	elif operacao == "Subtração (-)":
		resultado = numero1 - numero2
	elif operacao == "Multiplicação (*)":
		resultado = numero1 * numero2
	elif operacao == "Divisão (/)":
		if numero2 == 0:
			st.error("Não é possível dividir por zero.")
			st.stop()
		resultado = numero1 / numero2

	st.success(f"Resultado: {resultado:g}")
