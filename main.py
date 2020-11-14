# coding: utf-8

import glob
import os

# 拡張子.pngのファイルを取得する
path = './dir/*.png'
i = 1

# pngファイルを取得する
before_file_list = glob.glob(path)
print('変更前')
print(before_file_list)

# ファイル名を一括で変更する
for file in before_file_list:
    os.rename(file, './dir/icon' + str(i) + '.png')
    i += 1

after_file_ist = glob.glob(path)
print('変更後')
print(after_file_ist)
