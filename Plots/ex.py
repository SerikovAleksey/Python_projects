p = []
# try:
#     with open('m.txt') as f:
#         for line in f:
#             line = line.replace('\n', '')
#             line = line.replace(',', '.')
#             p.append([x for x in line])
# finally:
#     f.close()

with open ('m.txt', 'r') as f:
  old_data = f.read()

new_data = old_data.replace(' ', ', ')

with open ('m.txt', 'w') as f:
  f.write(new_data)

