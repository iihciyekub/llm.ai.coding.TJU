import pandas as pd
import re

def clean_sheet_name(name):
    """将sheet名称转换为有效的变量名"""
    # 将空格和特殊字符替换为下划线
    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', str(name))
    # 确保变量名不以数字开头
    if clean_name[0].isdigit():
        clean_name = 'sheet_' + clean_name
    return clean_name

# 读取第一个Excel文件 - firm return_total.xlsx
print("\n读取 firm return_total.xlsx:")
firm_return = pd.read_excel('firm return_total.xlsx', sheet_name=None)

# 创建一个字典来存储所有数据框
dfs = {}

# 处理第一个Excel文件的sheet
for sheet_name, df in firm_return.items():
    clean_name = f"firm_return_{clean_sheet_name(sheet_name)}"
    dfs[clean_name] = df
    print(f'成功读取sheet: {sheet_name}')
    print(f'保存为变量: {clean_name}')
    print(f'数据形状: {df.shape}')
    print(f'列名: {df.columns.tolist()}\n')

# 读取第二个Excel文件 - JP earthquake.xlsx
print("\n读取 JP earthquake.xlsx:")
jp_earthquake = pd.read_excel('JP earthquake.xlsx', sheet_name=None)

# 处理第二个Excel文件的sheet
for sheet_name, df in jp_earthquake.items():
    clean_name = f"jp_earthquake_{clean_sheet_name(sheet_name)}"
    dfs[clean_name] = df
    print(f'成功读取sheet: {sheet_name}')
    print(f'保存为变量: {clean_name}')
    print(f'数据形状: {df.shape}')
    print(f'列名: {df.columns.tolist()}\n')

# 将数据框存储到全局命名空间
globals().update(dfs)

print("所有数据已成功加载到以下变量中：")
for var_name in dfs.keys():
    print(f"- {var_name}")
