# KTP

This script is designed to run at windows env.

```shell
# set env variable
$ source ~/.bashrc

# create new conda env
$ conda create -n qpython python=3.11

# activate conda env
$ source activate qpython

# install required packages
$ pip install -r requirements.txt

# execute test
$ pytest -vv
```