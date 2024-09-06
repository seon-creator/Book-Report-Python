# book_report.py
from file_create import create
from file_delete import delete_file
from read import read
from update import update
import os

def main_menu():
    # 메인 메뉴 표시 및 선택
    print("=== 독후감 관리 프로그램 ===")
    print("1. 독후감 작성")
    print("2. 독후감 삭제")
    print("3. 독후감 보기")
    print("4. 독후감 수정")
    print("0. 프로그램 종료")
    
    try:
        choice = int(input("원하는 작업을 선택하세요: "))
        return choice
    except ValueError:
        print("유효한 숫자를 입력하세요.")
        return -1

def main():
    while True:
        choice = main_menu()

        if choice == 1:
            # 1. 독후감 생성
            
        elif choice == 2:
            # 2. 독후감 삭제

        elif choice == 3:
            # 3. 독후감 보기
            folder_path = './Data'
    
            # 텍스트 파일 목록 표시
            txt_files = read_files(folder_path)
    
            # 텍스트 파일이 있는 경우에만 계속 진행
            if txt_files:
                # 사용자로부터 파일명 입력받기
                file_name = input("내용을 보고 싶은 파일명을 입력하세요: ")
        
                if file_name in txt_files:
                    display_files(folder_path, file_name)
                else:
                    print("목록에 없는 파일입니다. 정확한 파일명을 입력하세요.")

        elif choice == 4:
            # 4. 독후감 수정
            folder_path = './Data'
            txt_files = read.read_files(folder_path)
            
            if txt_files:
                for idx, file_name in enumerate(txt_files, 1):
                    print(f"{idx}. {fine_name}")
                try:
                    update_choice = int(input("수정할 파일 번호를 선택하세요: ")) - 1
                    if 0 <= update_choice < len(txt_files):
                        update(folder_path, txt_files[update_choice])  # 파일 인자 전달
                    else:
                        print("잘못된 선택입니다.")
                except ValueError:
                    print("유효한 숫자를 입력하세요.")
            else:
                print("수정할 파일이 없습니다. ")
        elif choice == 0:
            # 0. 프로그램 종료
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    # 프로그램 실행
    main()