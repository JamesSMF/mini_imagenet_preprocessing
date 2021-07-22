import pickle as pk
import pandas as pd
from PIL import Image as im
import os
from tqdm import tqdm

# path to the preprocessing program and csv files
preproc_path = '/home/liguangyao/Datasets/datasets/'

# path to save all the images
save_path = '/home/liguangyao/Datasets/temp'

for split in ['train', 'val', 'test']:
   with open('mini-imagenet-cache-'+ split + '.pkl', 'rb') as f:
      data = pk.load(f)

   csv_record = pd.read_csv(os.path.join(preproc_path, split+'.csv'))

   # data: [image_data class_dict]
   for cls, img in tqdm(data['class_dict'].items()):
      print('handling class', cls)

      for idx in img:
         arr = data['image_data'][idx]
         image = im.fromarray(arr)
         name = csv_record.at[idx, 'filename']
         image.save(os.path.join(save_path, name))
