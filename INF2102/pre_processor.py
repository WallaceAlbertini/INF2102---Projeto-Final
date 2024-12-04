from sentence_transformers import SentenceTransformer


class PreProcessor():
    def __init__(self,embedding_model):
        self.model = SentenceTransformer(embedding_model)
    
    def preprocess(self,df):
        df['Embeddings'] = self.model.encode(df['Quote'].tolist()).tolist()
        return df
    
    def encode_single(self,quote):
        return self.model.encode(quote)
    

