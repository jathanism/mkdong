mkdong
======

A Python module for printing dongs.  
_This module borrows heavily from https://github.com/jathanism/mkdong.git_  


__installation:__  
```bash
$ git clone https://github.com/cfralick/mkdong.git  
$ cd mkdong  
$ python setup.py install  
```    

__usage:__
```bash
$ python -m mkdong 5       
```

```python
>>> import mkdong     
>>> mkdong.dong(5)    
'( )/( )=====D'    
```

__help:__
```bash
$ python -m mkdong -h
usage: mkdong [-h] [-w] [-c] [-v] l

Prints a dong.

positional arguments:
  l              the desired dong length

optional arguments:
  -h, --help     show this help message and exit
  -w, --wide     make a wide, thick dong
  -c, --climax   makes the dong climax
  -v, --version  print version and exit

mkdong 0.0.1
```
