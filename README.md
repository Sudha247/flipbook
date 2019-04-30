# Flipbook

## Dependencies

Python 3

### Libraries
* PLY (Python-Lex-Yacc) - [GitHub page](https://github.com/dabeaz/ply)
* FPDF - [GitHub page](https://github.com/reingart/pyfpdf)

Image format supported - JPG

## Syntax

### Display an image over a range of pages

```
1 10 my_image.jpg
```
* 1 -> Initial page
* 2 -> Final page
* my_image.jpg -> Image file name/path

### Display an image over a range of pages and move the image
```
1 10 my_image.jpg move 100 150
```
* 1 -> Initial page
* 10 -> Final page 
* my_image.jpg -> Image file name/path
* 100 -> Movement of the image in the X axis over the given range of pages
* 150 -> Movement of the image in the X axis over the given range of pages

### Display an image over a range of pages and scale the image
```
1 5 my_image.jpg scale 2
```
* 1 -> Initial page
* 5 -> Final page
* my_image.jpg -> Image file name/path
* 2 -> Scaling factor

### Display an image over a range of pages and rotate the image
```
1 6 my_image.jpg rotate 90 
```
* 1 -> Initial page
* 6 -> Final page
* 90 -> Angle of rotation in degree

## Directions to execute

```
$ python3 finalf.py [input_file.txt] -o [output_file.pdf]
```

For example:

```
$ python3 finalf.py sample.txt -o sample.pdf
```

## Scope for improvemet

1. Support for multiple operations in the same loc.
2. Check for any blank pages.
