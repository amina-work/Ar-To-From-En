
Original Paper: https://arxiv.org/pdf/1706.03762

An exercise to unserstanding LLMs and Tranformers better

By creating a pre-trained language translation modele,

The Transformer: " is a model that relies entirely on an attention mechanism to draw global dependencies between
input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs"

Tranfomers were first introduced with the goal of reducing sequential computation.

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.


# The model's structure is as follows:

An encoder maps an input sequence of symbol representations (x1,...,xn) to a sequence of continuous representations z = (z1,...,zn).
Given z, the decoder then generates an output sequence (y1,...,ym) of symbols one element at a time.
At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.

The decoder has 6 identical layers, and each layer have two sub-layers: The first is a multi-head self-attention mechanism, and the second is a simple, position wise fully connected feed-forward network

The decoder has 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack.


## Tools Used:

PyTorch
