import os

folder_path = os.path.join(os.getcwd(), 'sorted')
files = [(len(open(os.path.join(folder_path, file), 'r', encoding='utf-8').readlines()), file) \
         for file in os.listdir(folder_path)]
sorted_files = sorted(files)
res = ""

for num_lines, file in sorted_files:
    with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
        res += f'{file}\n{num_lines}\n{f.read()}'

with open(os.path.join(os.getcwd(), 'output.txt'), 'w', encoding='utf-8') as f:
    f.write(res)