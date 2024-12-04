import streamlit as st

class View:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        st.markdown("## Modelo TSC - Teoria Social Cognitiva")
        
        # Entrada do usuário
        user_input = st.text_area("Digite sua questão aqui:", placeholder="Escreva sua questão...")
        
        #Botão para processar a entrada            
        if st.button("Analisar"):
            if user_input.strip():  # Verifica se há texto
                with st.spinner("Analisando sua questão..."):
                    try:
                        # Chama o método do controller para processar a entrada
                        resposta = self.controller.run(user_input)
                        
                        # Exibe o resultado
                        st.subheader("Resultado da Análise")
                        st.write(f"**Resposta:** {resposta}")
                    except Exception as e:
                        st.error(f"Ocorreu um erro: {e}")
            else:
                st.warning("Por favor, insira uma questão para análise.")



