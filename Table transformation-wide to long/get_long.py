# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# 文件地址，例：C:\\Users\\xxx\\Desktop\\BI data\\宏观数据\\filename.xlsx
url = input('请输入文件路径(如文件在此目录下输入文件名即可)：')
# 目标表名称，例： Data
sheet = input('目标sheet：')

raw = pd.read_excel(io=url, sheet_name=sheet)
print('-'*15)
print(sheet,'表中列的数量：', len(raw.columns))
print(sheet,'表中的所有列名为：', raw.columns)
print('-'*15)

keep_cols = input('请输入保持不变的列名(多个用空格间隔)：')
tlong_cols = input('请输入要转换的列名(多个用空格间隔)：')
tlong_varname = input('请输入转换后的变量列名：')
tlong_valname = input('请输入转换后的数值列名：')

dt = raw.melt(id_vars=keep_cols.split(),
	value_vars=tlong_cols.split(),
	var_name=tlong_varname,
	value_name=tlong_valname).sort_values(by=keep_cols.split()[0])

print('-'*15)
print('转换后的行列数量：',dt.shape)
print('-'*15)

tlong_url = input('输出的文件名称：')
dt.to_csv(tlong_url+'.csv',index=False,encoding='gbk')