# mallick_cascades

This repository contains minified versions of all OpenCV Haar and LBP cascades. Minification has been achieved by removing unnecessary white spaces and unnecessary precision. 

| Cascade Name	| File size	    | Minified file size|
|---------------|:-------------:|:-----------------:|
| haarcascade_eye.xml	| 336K	| 180K
| haarcascade_frontalface_default.xml	| 912K	| 488K
| haarcascade_frontalface_alt_tree.xml	| 2.6M | 1.4M
| lbpcascade_frontalface.xml	| 52K	| 36K

The original cascades are also shared for reference. The minified cascades are named with a prefix **mallick_**

## Tester

I have added a tester script (tester.py) that loads a haar cascade and its minified version and displays the results on the same frame of the your webcam. The blue box denotes output of the haar cascade and the red box denotes the output of the minified cascade. The blue box is deliberately made 4 pixels smaller in width and height for display purposes. Here is the usage

```
python tester.py haarcascades/haarcascade_frontalface.xml
```

## Visit us
For other OpenCV, Computer Vision and Machine Leanring goodies, please visit us at 

http://www.learnopencv.com

