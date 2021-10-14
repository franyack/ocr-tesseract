# OCR Project with Tesseract

This project uses Tesseract software and Python language to resolve OCR problems.

Starting from an image (or a folder with images), the target is to convert visual information (e.g. words, numbers inside 
the image) into text information (e.g. csv file with relevant information).

All the scripts are based on <b>Adrian Rosebrock</b> and his website [pyimagesearch](https://www.pyimagesearch.com/). So, thanks Adrian!

## Index:

- [About project](#about-project)
- [Environment setup](#environment-setup)
- [References](#references)

## About project

![technology Python](https://img.shields.io/badge/technology-python-red.svg)

## Environment setup

- Install Tesseract technology on your machine, you can find how to do this [here](https://www.pyimagesearch.com/2021/08/16/installing-tesseract-pytesseract-and-python-ocr-packages-on-your-system/)

- Configure your development environment. It is highly recommended to use pyenv, so you can manage your python projects easily. More information [here](https://github.com/pyenv/pyenv-virtualenv)

- Once you have your environment ready, you must install requirements. To do this, in the root of this project, execute:

    ```
    pip install -r requirements.txt
    ```

- That's all! Yoy could run any python script. For example:

    ```
    python scripts/ocr_folder_process.py --folder folder_path_where_you_have_your_images_to_process --blacklist "|/\[](){}" 
    ```

## References

- [Your First OCR Project with Tesseract and Python](https://www.pyimagesearch.com/2021/08/23/your-first-ocr-project-with-tesseract-and-python/)
- [Detecting and OCR’ing Digits with Tesseract and Python](https://www.pyimagesearch.com/2021/08/30/detecting-and-ocring-digits-with-tesseract-and-python/)
- [Whitelisting and Blacklisting Characters with Tesseract and Python](https://www.pyimagesearch.com/2021/09/06/whitelisting-and-blacklisting-characters-with-tesseract-and-python/)


