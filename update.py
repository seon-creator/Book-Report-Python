import chardet
import fileinput
import os

def update(folder_path, file_name):
    filename = os.path.join(folder_path, file_name)
    with open(filename, 'rb') as f:
        raw_data = b''.join([f.readline() for _ in range(20)])
        encoding=chardet.detect(raw_data)['encoding']
        
    with open(filename, 'r', encoding=encoding) as f:
        lines = f.readlines()
        
    if len(lines) >= 5:
        content_to_edit = ''.join(lines[4:]).strip()  # 5번째 줄부터 가져옴 (인덱스 4부터 시작)
    else:
        content_to_edit = ''
    
    print(f"현재 독후감 내용: {content_to_edit}")
    
    updateContent = input(f"수정할 독후감 내용을 입력하세요 (현재 내용 유지하려면 엔터를 누르세요): ")
    
    if updateContent == '':
        updateContent = content_to_edit

    with open(filename, 'w', encoding=encoding) as f:
        f.writelines(lines[:4])  # 처음 4줄은 그대로 유지
        
        # 수정된 내용으로 5번째 줄부터 작성
        f.write(updateContent + '\n')