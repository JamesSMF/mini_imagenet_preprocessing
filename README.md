# Mini ImageNet Preprocessing

**Abstract:** With the growing needs for few shot learning, Mini Imagenet has gained its position in FSL area. However, I found at least 3 versions of Mini Imagenet Dataset (in different file formats and directory structures), and there are also tons of different pre-processing programs for this dataset, which requires your (tremendous) extra effort to rearrange the dataset in the right way. Well, I did all that for you. This is a complete pre-processing program for Mini Imagenet, leading you from downloading the raw data to getting the complete pre-processed dataset.



**keywords:** Mini ImageNet, Data Preprocessing, Few Shot Learning



## TL;DR

No, read it, seriously. Everything is important.



## Baseline Program

I borrowed the baseline pre-processing program from [here](https://github.com/ElementAI/TADAM/tree/master/datasets), and made some subtle changes. Credits to Boris Oreshkin et. al..



## Downloading the raw dataset

Link to Mini_Imagenet Dataset tar.gz file: [google drive](https://drive.google.com/file/d/16V_ZlkW4SsnNDtnGmaBRq2OoPmUOc5mY/view)

Our next step is downloading the raw dataset from google drive. After unpacking this file, you will get 3 `pkl` files, which stand for a series of pickled files. They can be opened via python `pickle` module.

Move/save the 3 `pkl` files to the mini_imagenet directory



## Build the directory structure

Before you run the program, prepare the directory structures like this:

```bash
.
|
 ---- datasets
|        |
|         ---- create_dataset_miniImagenet.py
|         ---- test.csv
|         ---- train.csv
|         ---- val.csv
|
 ---- mini_imagenet
|        |
|         ---- mini-imagenet-cache-train.pkl
|         ---- mini-imagenet-cache-test.pkl
|         ---- mini-imagenet-cache-val.pkl
|         ---- unpack.py
|
 ---- temp
```



Besides saving the three `pkl` files to `mini_imagenet` directory, create a new empty directory `temp`. This directory will be used to save unpacked images from the three `pkl` files. Of course you can put it anywhere you like, and you can modify the paths in `unpack.py` to fit your environment.



## Run the program
Before you run the program, check if all the packages/modules in `requirements.txt` files have been installed properly. If not, you may install with `pip install package`.

1.  Open the `unpack.py` file and make changes to paths to fit your devices.
2.  Run `python3 unpack.py` in python3 environment
3.  Go to `temp` folder and run `zip images.zip ./*`
4.  Run `mv images.zip ../datasets`
5.  You can remove the `temp` directory now to save storage space
6.  Go to `datasets` folder and run the python program `python3 create_dataset_miniImagenet.py --data-dir /path/to/current/dir/ --output-dir /path/to/save/the/final/preprocessed/files/`
7.  It might take some time, like... forever
8.  Done
