# otus_web_01
Homework task for OTUS "Python for Web" course


# Otus Web 01 Word Counter

This simple library counts words (verbs by default) in different folders and shows simple stats.

## Getting Started

### Prerequisites

- Python 3.6+
- Virtualenv
- Pip


### Installing

Make a new virtualenv (you may as well not if you know what you're doing)

```
$ virtualenv -p python3 otus_web_04
```

Clone this repo

```
$ git clone https://github.com/xelnod/otus_web_01.git
```


Install requirements

```
$ pip install -r requirements.txt
```

Add an nltk perception tagger:

```
$ python
>>> import nltk; nltk.download('averaged_perceptron_tagger')
```

## How to use

```
$ cd words_counter
$ python words_counter.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
