
#import thư viện

import re
import pandas as pd
import numpy as pd

#task1

file_dict = {
	"class1": "class1.txt",
	"class2": "class2.txt",
	"class3": "class3.txt",
	"class4": "class4.txt",
	"class5": "class5.txt",
	"class6": "class6.txt",
	"class7": "class7.txt",
	"class8": "class8.txt"
}

while True:
	filename = input("Nhập tên file: ")
	if filename in file_dict:
		break
	print(f"Không tìm thấy file: {filename}")

try:
	file_op = open(file_dict[filename], "r")
except FileNotFoundError:
	print(f"Lỗi: không tìm thấy file {file_dict[filename]}")
print(f"Đã mở file: {file_dict[filename]}")

#task2

with open(file_dict[filename], "r") as file_op:
	lines = file_op.readlines()

#2.1 Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp.
	
num_lines = len(lines)
print( "Tổng số dòng dữ liệu được lưu trữ trong tệp:", num_lines)

#2.3 Báo cáo tổng số dòng dữ liệu không hợp lệ trong tệp.

invalid_lines = 0
valid_lines = 0

#task3
# 3 khai báo và xữ lý đáp án

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
key=answer_key.split(",")
ketqua={}
diem={}
skip_sumit=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
wrong_sumit=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in lines:
	
	lines_part=line.split(",")
	valid = re.match(r'^N\d{8},.*', line)
	
	if len(lines_part)!=26 or not valid:
		
		misstask = "Dữ liệu lỗi không đủ 26 giá trị và lỗi id 'N'"
		
		if len(lines_part)!=26:
			misstask = "Dữ liệu lỗi không đủ 26 giá trị"
		
		elif not valid:
			misstask = "Dữ liệu lỗi id 'N'"

		print(misstask + ":\n", line)
		invalid_lines += 1
	
	else:
		valid_lines += 1
		
		scores = 0
		sumit = []
		for k, l in zip(key, lines_part[1:]):
			l=l.strip()
			scores = 4 if k==l else 0  if not l else -1 
			sumit.append(scores)
			ketqua[line]=sumit
			diem[line]=sum(sumit)


print("Tổng số dòng dữ liệu hợp lệ trong tệp:", valid_lines)
print("Tổng số dòng dữ liệu không hợp lệ trong tệp:", invalid_lines)

#3.1. Đếm số lượng học sinh đạt điểm cao (>80)

count_hightscores=0
for x in diem.values():
    if x > 80:
        count_hightscores += 1

avg_scores = sum(diem.values())/len(diem)
max_scores = max(diem.values())
min_scores = min(diem.values())
range_scores = max_scores - min_scores

sort_scores = list(diem.values())
sort_scores.sort()
mid=len(sort_scores)//2
res_scores=(sort_scores[mid]+sort_scores[~mid])/2

for k in ketqua.values():
    for l in range(len(k)):
        if k[l] == 0:
            skip_sumit[l]+=1
        elif k[l] == -1:
            wrong_sumit[l]+=1

max_skip=[]

max_wrong=[]

for s in range(len(skip_sumit)):
	if skip_sumit[s]==max(skip_sumit):
		number_skip=s+1
		max_skip.append(number_skip)

max_skip_sumit=max(skip_sumit)
rate_max_skip_sumit=max_skip_sumit/len(ketqua)

for w in range(len(wrong_sumit)):
	if wrong_sumit[w]==max(wrong_sumit):
		number_wrong=w+1
		max_wrong.append((w+1))
max_wrong_sumit=max(wrong_sumit)
rate_max_wrong_sumit=max_wrong_sumit/len(ketqua)

print("Số lượng học sinh đạt điểm cao (>80):", count_hightscores)
print("Điểm trung bình:", avg_scores)
print("Điểm cao nhất:", max_scores)
print("Điểm thấp nhất:", min_scores)
print("Miền giá trị của điểm:", range_scores)
print("Giá trị trung vị điểm:", res_scores)
print(f"Các câu hỏi bị học sinh bỏ qua nhiều nhất: {max_skip} - {max_skip_sumit} - {rate_max_skip_sumit:.2f} ")
print(f"Các câu hỏi bị học sinh sai qua nhiều nhất: {max_wrong} - {max(wrong_sumit)} - {rate_max_wrong_sumit:.2f} ")

# task 4

write_file= filename +"_grades.txt"

with open(write_file, 'w') as writefile:
    for d in diem:
        id=d.split(",")[0]    
        id_diem=diem[d]
        text= f"{id}, {id_diem}\n"
        writefile.write(text)

