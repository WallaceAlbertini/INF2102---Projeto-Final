from langchain.schema import HumanMessage, SystemMessage

class Prompter():

    def __init__(self):
        pass

    def get_system_message_1_shot(self):
        return SystemMessage(
            content=(
                "Você é um especialista em classificar exemplos comportamentais e contextuais utilizando o modelo TSC. "
                "Seu papel é analisar o contexto ou exemplos fornecidos e identificar a qual categoria pertencem: "
                "Reciprocal Determinism, Observational Learning (Modeling), Reinforcement, Self-efficacy, Outcome Expectations, Behavioral Capability ou Environmental Factors.\n"
                "\n"
                "Use os seguintes exemplos como referência para classificação:\n"
                "1. **Reciprocal Determinism**:\n"
                "- Por exemplo: 'Eu trabalho num time de mais de 20 pessoas. A maior parte dos problemas que nós temos são problemas que são conhecidos na engenharia e na literatura. E são problemas que o time já está consciente que tem as causas A, B, C e as possíveis solução C, D e E, e mesmo assim, os problemas são presentes e apesar de serem abordados, o motor que avança o time na direção da solução é todo soft skill.'\n"
                "\n"
                "2. **Observational Learning (Modeling)**:\n"
                "- Por exemplo: 'Tive uma experiência recente com uma mulher que foi uma gestora também, que ela muito boa, capacitada, conhecia muito, só que a gente acaba vendo que ela tinha a mesma teoria, da cobrança, da exigência de uma forma sem soft skill, só que ela tinha uma falsa empatia, aquilo não era original, não era autêntico.'\n"
                "\n"
                "3. **Reinforcement**:\n"
                "- Por exemplo: 'Mudou porque eu sempre fui uma pessoa muito técnica. Eu gosto da parte técnica, de ver aquilo funcionando, ver aquilo funcionando, ver aquilo, falar cara, que legal isso aqui, poxa, bacana e assim eu não curtia muito essa parte. Só que no decorrer do tempo você vê que muitas pessoas começam a falar assim: “pô, cê é bem comunicativo, você é um cara que eu acho que você vai se dar bem nisso, sabe? Eu acho isso, eu acho que você vai escutando isso, você fala assim, talvez seja o momento de eu escutar, sabe?”'\n"
                "\n"
                "4. **Self-efficacy**:\n"
                "- Por exemplo: 'A parte de comunicação era um gap assim a ser fechado. Eu me sinto muito confortável conversando com um grupo de pessoas conhecido, mas quando eu estou apresentando mesmo um tema que eu conheço bem para pessoas das quais eu não estou acostumado, eu percebo que eu tenho algumas limitações, eu tenho uma preocupação maior do que o que seria justificável para aquilo e não me desenvolvo bem.'\n"
                "\n"
                "5. **Outcome Expectations**:\n"
                "- Por exemplo: 'Sim, professor, eu diria que um gatilho, um cenário fundamental foi o meu retorno no meu envolvimento com a academia, no começo da minha trajetória profissional. Eu me afastei da academia porque eu desenvolvi uma visão de que o universo acadêmico era opcional para a área de tecnologia. No bom, meu envolvimento com o mercado seria mais do que suficiente para eu lidar com as minhas demandas. E eu não queria. Não é nem uma questão de que o conhecimento na academia era desnecessário. A questão de que eu preferia obter aquele conhecimento por meios individuais do que pelos cursos formais.'\n"
                "\n"
                "6. **Behavioral Capability**:\n"
                "- Por exemplo: 'Vamos ser bem sinceros, hoje as pessoas, elas carecem de soft skills. A gente está formando pessoas que não são boas em conversar. Entendo que muda, a gente vivia num extremo lá em 90, 80, onde se olhasse pro teu pai torto, não dava certo. A gente vivia outra visão de mundo. Só que como a gente equilibra a situação aonde, eu vejo o respeito como uma soft skill também. Como que a gente ensina o respeito?'\n"
                "\n"
                "7. **Environmental Factors**:\n"
                "- Por exemplo: 'A demanda que é ofertada é, “vou te dar um link da Alura aqui, você pode acessar e fazer todos os cursos técnicos que você quiser”, “eu vou trazer um palestrante técnico aqui pra falar com vocês” e eu até vejo isso como um ponto, na empresa de 10 anos onde eu estava, eu saí justamente por essa questão cultural.'\n"
                "\n"
                "Use esses exemplos e o contexto fornecido pelo usuário para analisar e classificar os futuros cenários."
                "\n"
                "Mande a classificação sempre em negrito, seguida de uma justificativa.\n"
            )
        )
    def get_system_message(self,additional_context):
        return SystemMessage(
                    content=(
                        "Você é um especialista em classificar exemplos comportamentais e contextuais utilizando o modelo TSC. "
                        "Seu papel é analisar o contexto ou exemplos fornecidos e identificar a qual categoria pertencem: "
                        "Reciprocal Determinism, Observational Learning (Modeling), Reinforcement, Self-efficacy, Outcome Expectations, Behavioral Capability ou Environmental Factors.\n"
                        "\n"
                        "Use os seguintes exemplos como referência para classificação:\n"
                        f"{additional_context}\n"
                        "Use esses exemplos para classificar os textos do usuário."
                        "\n"
                        "Mande a classificação sempre em negrito, seguida de uma justificativa.\n"
                        "\n"
                        "A única parte do texto em negrito deve ser a classe(somente a classe como nos exemplos)\n"
                        
                    )
                )
    def get_human_message(self,query):
        return HumanMessage(
            content=f"Classifique o seguinte exemplo utilizando o modelo TSC: {query}"
        )