import streamlit as st

class View:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        st.markdown("## Classificador TSC - Teoria Social Cognitiva")
        
        # Entrada do usuário
        user_input = st.text_area("Digite o trecho a ser classificado:", placeholder="Escreva seu trecho textual...")
        
        #Botão para processar a entrada            
        if st.button("Classificar"):
            if user_input.strip():  # Verifica se há texto
                with st.spinner("Claficando trecho fornecido..."):
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



