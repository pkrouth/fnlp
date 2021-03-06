# fnlp

This repo contains scripts to train NLP models using the text data.

## Dependencies

* [pytorch](http://pytorch.org/)
* numpy
* nltk.tokenize

## Train new GloVe vectors

`glove.py` contains a GloVe model written in `pytorch`. `dataset.py` contains a Dataset class - it is written in a way so that `torch.utils.data.DataLoader` utility class of `pytorch` can be used for training.

```bash
$ python3 glove.py --input wiki_data.txt --batch_size 512
```

## Check the word Vectors

Trained word vectors are available on the [releases](https://github.com/hardikp/fnlp/releases) page.

Let's check if the closest words make sense.

```bash
$ python3 test_word_vectors.py --word IRA
roth, iras, sep, 401, contribute

$ python3 test_word_vectors.py --word option
call, options, put, exercise, underlying

$ python3 test_word_vectors.py --word stock
shares, share, market, stocks, price
```

## Notes
This CPU-only implementation is not yet optimized. For training on CPU, it might be best to download the Glove software from [here](https://nlp.stanford.edu/projects/glove/).

## Credits
* [GloVe Paper](https://nlp.stanford.edu/pubs/glove.pdf)
* [TorchGlove](https://github.com/2014mchidamb/TorchGlove) repo

## License
MIT
