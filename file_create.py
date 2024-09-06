def create():
    import os
    from datetime import datetime

    # 책 정보 및 독후감 내용 입력받기
    book_title = input("책 제목을 입력하세요: ")
    author = input("저자를 입력하세요: ")
    reviewer = input("작성자를 입력하세요: ")
    review_content = input("독후감 내용을 입력하세요: ")

    # 현재 날짜 가져오기
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 파일 내용 구성
    content = f"{book_title}\n{author}\n{reviewer}\n{current_date}\n{review_content}"

    # 디렉토리 확인 및 생성
    file_dir = 'data'
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    # 파일 경로 설정
    file_name = f"{book_title}-{reviewer}.txt"
    file_path = os.path.join(file_dir, file_name)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"독후감이 {file_path}에 저장되었습니다.")