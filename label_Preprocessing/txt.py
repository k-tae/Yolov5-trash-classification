import os

def create_empty_txt_files(json_folder_path):
    # JSON 파일이 있는 폴더 내의 모든 파일에 대해 반복
    for filename in os.listdir(json_folder_path):
        # 파일 이름이 확장자를 포함하는지 확인
        if filename.endswith(".json"):
            # JSON 파일의 경로 및 이름 가져오기
            json_path = os.path.join(json_folder_path, filename)
            
            # 해당 JSON 파일과 동일한 이름의 텍스트 파일 경로 생성
            txt_path = os.path.splitext(json_path)[0] + ".txt"
            
            # 텍스트 파일 생성
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                pass  # 빈 파일이므로 아무 내용도 추가하지 않음
            
            print(f"빈 텍스트 파일 {txt_path}가 생성되었습니다.")

# JSON 파일이 있는 폴더 경로
json_folder_path = 'C:\\Users\\rnjsx\\OneDrive\\Desktop\\v\\label'

# 빈 텍스트 파일 생성
create_empty_txt_files(json_folder_path)
