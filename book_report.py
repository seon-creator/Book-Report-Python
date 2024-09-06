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
            create()
        elif choice == 2:
            # 2. 독후감 삭제
            file_name = input("삭제할 파일명을 작성해주세요:")
            delete_file(file_name)
        # elif choice == 3:
        #     # 3. 독후감 보기


        # elif choice == 4:
        #     # 4. 독후감 수정
        #     folder_path = './Data'
        #     txt_files = read.read_files(folder_path)
            
        #     if txt_files:

        elif choice == 0:
            # 0. 프로그램 종료
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    # 프로그램 실행
    main()