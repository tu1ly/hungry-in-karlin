# Hungry in Karlín

Are you hungry in Karlín? Congratulations, that is a great first world problem to have! And this project is there exactly for you.

## Installation

```shell
$ python3 -m venv venv
$ . ./venv/bin/activate
(venv)$ pip install -r requirements.txt
```

### Supported operating systems

- OSX (`open` utility is a dependency)

## Solved Scenarios

### Analysis paralysis

> Analysis paralysis or paralysis by analysis is an anti-pattern, the state of over-analyzing (or over-thinking) a situation so that a decision or action is never taken, in effect paralyzing the outcome.
>
> -- [Wikipedia](https://en.wikipedia.org/wiki/Analysis_paralysis)

Just run the `decide.py` script:

```shell
(venv)$ python decide.py
```

The script selects a place where to eat for you. It uses very complicated algorithm, artificial intelligence and various heuristics to guess what is the best option for you at the moment.

## Planned Scenarios and Features

- Filter places which are not currently open.
- Select the closest place (lazy scenario).
- Automatically order an [ordr.cz](https://ordr.cz/) if available (super-lazy scenario).
- List lunch offers of restaurants and provide them in both Czech and English.
