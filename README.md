# Load Balancing Algorithms

<p align="left">
  <a href="#introduction">Introduction</a> •
  <a href="#how-to-use">How to Use</a> •
  <a href="#credits">Credits</a>
</p>

## [Introduction](#introduction)

This repository contains various load balancing algorithms implemented in Python. The algorithms are implemented in the `src` directory. The `src/main.py` file contains a starting point to the applicaiton.

The following algorithms are implemented:

- [x] Round Robin
- [ ] Least Connections
- [ ] Random
- [ ] IP Hash
- [ ] URL Hash

## [How to Use](#how-to-use)

My plan for this repositry is to create a simple CLI that will allow users to select the algorithm they want to use and then run the load balancing algorithm.

But for now, you can run the following command from the root of the app to run the application:

```bash
make run
```

In order to change the algorithm and some other factores, you should look at the file: `src/main.py`.

## [Credits](#credits)

I was inspired by the blog written by [Sam Who](https://samwho.dev/load-balancing/) and the subsequent YouTube video made by [Theo]().

