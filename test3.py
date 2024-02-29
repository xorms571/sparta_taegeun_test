name = input("이름이 뭔가요? ")
username = input("아이디는 뭔가요? ")
password = input("비밀번호는 뭔가요? ")
member = {"name": name, "username": username, 'password': password}
title = input('게시물 제목을 입력해주세요.')
content = input('게시물 내용을 입력해주세요.')
Post = {"title": title, "content": content, 'author': username}
print(f'제목 : {title}, 내용 : {content} 작성자 : {username}')