# Projeto TSC - Teoria Social Cognitiva

Este projeto implementa um modelo de classificação utilizando a Teoria Social Cognitiva (TSC) para categorizar exemplos comportamentais e contextuais. O sistema foi desenvolvido utilizando técnicas de aprendizado de máquina, como embeddings de texto e a integração com a API da OpenAI.

## Pré-instalação

Antes de iniciar a instalação, é necessário ter algumas ferramentas e pacotes instalados em seu sistema.

### Requisitos de Sistema

- **Sistema Operacional**: Linux, macOS ou Windows
- **Python**: 3.12.4 (ou superior)
- **Conda**: Recomendado para gestão de ambientes e dependências

### Passo 1: Instalar o Conda

Caso não tenha o Conda instalado, faça o download e instale o [Anaconda](https://www.anaconda.com/products/distribution) ou o [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (uma versão mais leve do Anaconda).

### Passo 2: Criar o Ambiente Virtual

Com o Conda instalado, você pode criar um ambiente virtual para este projeto. Para isso, siga os passos abaixo:

1. **Clone o Repositório**:

   Clone este repositório em seu diretório local:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```
   
### Passo 3: Criar o Ambiente Conda
Utilize o arquivo environment.yml fornecido para criar o ambiente Conda:
```bash
conda env create -f environment.yml
```

### Passo 4: Ative o Ambiente

Após a criação do ambiente, ative-o com o seguinte comando:

```bash
conda activate para_testar
```

### Passo 5: Instalar Dependências Adicionais (se necessário)

Embora a maioria das dependências já estejam incluídas no arquivo environment.yml, caso queira instalar manualmente algum pacote adicional, use o seguinte comando:

```bash
pip install <PACOTE>
```
    
### Passo 6: Configurar a Chave da API OpenAI

Este projeto utiliza a API da OpenAI para interação com o modelo GPT. Para utilizá-la, é necessário configurar sua chave de API.

**Obtenha sua chave da OpenAI:**

Acesse https://platform.openai.com e crie uma conta ou faça login.
Navegue até a seção de API Keys e gere uma nova chave de API.

**Configuração:**

Em seu código, substitua a chave de API no arquivo controller.py:

```bash
openai_api_key = "SUA_CHAVE_DE_API_AQUI"
```

### Passo 7: Testar a Instalação

Para verificar se tudo está funcionando corretamente, execute o código de exemplo fornecido no repositório:
    
```bash
streamlit run app.py  
```

Isso deve iniciar o aplicativo Streamlit, onde você poderá interagir com o modelo e fazer as análises.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
