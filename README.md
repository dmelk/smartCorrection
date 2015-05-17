# smartCorrection
Smart words correction project (only for english now)

It correct words based on predefined dictionary and distance between unknown word from source and known word in dictionary.
How it will search words?
First of all it looks on first and last letters and len of the word, then unknown word will be normalized and compared to found normalized words in dictionary.
Result will be array of all words with minimal distance.

Supports different distance metrics. For now it uses QWERTY metric (where distance between letters is based on the qwerty keyboard).

# Example
For example such text:
```
Aocicndrg to the rtsleus of the rcasereh of one Eisgnlh uestivriny,
it deos not mtater in wcihh oedrr the lrteets are odrreed in a wrod.
It is olny iaprnomtt taht the fsrit and the lsat lrtetes be in tiehr pealcs.
All oehtr lreetts can be odreerd in an aitrrraby oredr, and one can slitl
raed the txet wutioht any plmobers. It semes to be due to the fcat taht we
do not raed ecah lteter stplraaeey, but raed ecah wrod as a wolhe.
```
will be transformed to (delta = 0):
```
according to the [results, rustles] of the research of one english university,
it does not matter in which order the letters are ordered in a word.
it is only important that the first and the last letters be in their places.
all other letters can be ordered in an arbitrary order, and one can still
read the text without any problems. it seems to be due to the fact that we
do not read each letter separately, but read each word as a whole.
```

If we have typo mistakes, then set delta to the 0.3. For example:
```
Tihs os tyopgraphic nistake
```
will be transformed to 
```
this [is, ow, ox] typographic mistake
```
