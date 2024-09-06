import os

def read_files(folder_path):
    # 지정된 폴더 내 파일 목록 가져오기
    try:
        files = os.listdir(folder_path)
        
        # .txt 파일만 필터링
        txt_files = [file for file in files if file.endswith('.txt')]
        
        if not txt_files:
            print("폴더에 텍스트 파일이 없습니다.")
            return txt_files
        
        # 보기 좋게 파일 목록 출력
        print("=== 저장된 독후감 목록 ===")
        for idx, file in enumerate(txt_files, 1):
            print("{}. {}".format(idx, file))
            
        return txt_files
        
    except FileNotFoundError:
        print("'{}' 폴더가 존재하지 않습니다.".format(folder_path))
        return []

def display_files(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    
    # 파일 내용 출력
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\n=== {}의 내용 ===".format(file_name))
            print(content)
    except FileNotFoundError:
        print("'{}' 파일을 찾을 수 없습니다.".format(file_name))
    except Exception as e:
        print("파일을 여는 중 오류 발생:", e)
