
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

## Dataset Used:

from : https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks


## progress: 
stopped training model at : (after 3h)
Processing epoch 00:   2%|2         | 337/14297 [2:26:04<107:40:09, 27.77s/it, loss=6.842]
Processing epoch 00:   2%|2         | 338/14297 [2:26:18<108:31:52, 27.99s/it, loss=6.842]
Processing epoch 00:   2%|2         | 338/14297 [2:26:33<108:31:52, 27.99s/it, loss=7.074]
Processing epoch 00:   2%|2         | 339/14297 [2:26:47<109:59:01, 28.37s/it, loss=7.074]
Processing epoch 00:   2%|2         | 339/14297 [2:27:02<109:59:01, 28.37s/it, loss=6.729]
Processing epoch 00:   2%|2         | 340/14297 [2:27:16<110:25:34, 28.48s/it, loss=6.729]
Processing epoch 00:   2%|2         | 340/14297 [2:27:31<110:25:34, 28.48s/it, loss=7.003]
Processing epoch 00:   2%|2         | 341/14297 [2:27:46<112:11:18, 28.94s/it, loss=7.003]
Processing epoch 00:   2%|2         | 341/14297 [2:28:01<112:11:18, 28.94s/it, loss=6.370]
Processing epoch 00:   2%|2         | 342/14297 [2:28:13<110:52:47, 28.60s/it, loss=6.370]
Processing epoch 00:   2%|2         | 342/14297 [2:28:26<110:52:47, 28.60s/it, loss=6.488]
Processing epoch 00:   2%|2         | 343/14297 [2:28:37<104:58:46, 27.08s/it, loss=6.488]