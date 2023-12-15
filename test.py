from gendiff import giff_with_formatter


file_path1 = 'file1.json'
file_path2 = 'file2.json'

diff = generate_diff(file_path1, file_path2)
print(diff)