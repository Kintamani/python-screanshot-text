# Python Screanshot Text
Implements a live screenshot with an image file format and then changes it to a text format using OCR (optical character recognition).

## Requierments
* Python = 3.11.3
* PyQt5 = 5.15.9
* Pillow = 9.5.0
* pytesseract = 0.3.10
* pyperclip3 = 0.4.1
* numpy = 1.24.3
* opencv = 4.7.0.72
* [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/Downloads.html) = 3.02 

## Tested (Windows 11 - 64 bit)
![Alt text](/gif/test.gif "Testing Videos")

## Structur Project
```python
kintamani-screanshot-text/
├── app/
│   ├── __init__.py
│   ├── ocr.py
│   ├── gui.py
│   ├── designer/
│   └── img/
├── main.py
└── requirements.txt
```

* The `app` folder contains modules for OCR, GUI, and the img folder for storing images to be processed.
    * The `img` directory is only for screan images <b>(dont remove `capture.png` inside this directory)</b>.
    * The `designer` directory is only for uploading sample images.
* The `main.py` file serves as the main file to run the program.
* The `requirements.txt` file contains a list of required dependencies.
    * `opencv`: OpenCV library for image processing.
    * `pytesseract`: Python wrapper library for Tesseract OCR engine.
    * `pyperclip3` : Python library that allows you to copy and paste text to the clipboard in a cross-platform manner.
    * `Pillow`: Python library for image manipulation such as resize, crop, and convert.
    * `numpy`: Package for performing mathematical operations on arrays and matrices
    * `PyQt5` :  Package user interface (GUI) applications


## Usage
* Install Requirements :
    ```bash 
    pip install --no-cache-dir -r requirements.txt
    ```

* Download and Install [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/Installation.html#windows)

* Run Project :

    ```bash 
    py main.py
    ```

