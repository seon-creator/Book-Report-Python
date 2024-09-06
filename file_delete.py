import os

def delete_file(filename):
    # 파일 경로 설정
    file_dir = 'data'
    file_path = os.path.join(file_dir, f"{filename}.txt")
    
    # 파일 존재 여부 확인 후 삭제
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"독후감 파일 '{filename}'가 삭제되었습니다.")
    else:
        print(f"독후감 파일 '{file_path}'이 존재하지 않습니다.")