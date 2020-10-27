# coding: utf-8

import glob
import os

# 拡張子.txtのファイルを取得する
path = './dir/*.txt'
i = 1

# txtファイルを取得する
beforeFileList = glob.glob(path)
print('変更前')
print(beforeFileList)

# ファイル名を一括で変更する(留意点：事前にバックアップを取っておくこと)
for file in beforeFileList:
    os.rename(file, './dir/sample' + str(i) + '.txt')
    i += 1

AfterFileList = glob.glob(path)
print('変更後')
print(AfterFileList)
