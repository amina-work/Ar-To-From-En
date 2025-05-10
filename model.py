
##### Libraries #####
import torch
import torch.nn as nn
import math


#First Part to build: Input embedding
#the input embedding takes the inputs and convert it to embedding
#Embedding is an input word tranformmed into a 512 sized vector
class  InputEmbeddings(nn.Module):

    #constructor: size of model, how many words there are in the vocabulary
    def __init__(self, d_model: int, vocab_size:int):
        super().__init__()
        self.d_model = d_model
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(vocab_size, d_model)

    def forward(self, x):
        return self.embedding(x) * math.sqrt(self.d_model)
    
#Second part: positional encoding
#is giving the model info about the position of each word
#this is done by adding a second vector (same size) that includes some special values that tells the model the info

class PositionalEncoding(nn.Module):

    #seq_len is the length of the sentence
    def __init__(self, d_model: int, seq_len:int, dropout:float) -> None:
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len
        self.dropout = nn.Dropout(dropout)

        #create a matrix of shape (seq_len, d_model)
        #PE(pos,2i) = sin(pos/100002i/dmodel)
        pe = torch.zeros(seq_len, d_model)
        #create a vector of shape (seq_len, 1)
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 1).float() * (-math.log(10000.0) / d_model))
        #apply the sin and cos to even position
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        pe = pe.unsqueeze(0) #(1, seq_len,  d_model)

        self.register_buffer('pe', pe) #save the tensor

    def forward(self, x):
        x = x + (self.pe[:, :x.shape[1], :]).requires_grad_(False) #makes particular tensor not learn
        return self.dropout(x)
        

