# 테스트 케이스 받기
num  = int(input())

# 각 메세지 판단 함수
def solution(msg):
    # 메세지 문자 딕셔너리
    msg_char_list = {}
    # 3번 째 나온 단어
    is_third = 0
    # 성공 여부
    flag = True
    
    for char in msg:
        # 만약 is_third 가 0이 아니면
        if is_third:
            # is_third 다음이 is_third와 같을 때
            if char == is_third:
                is_third = 0
                msg_char_list[char] = 0
                continue
            # 아니면 FAKE
            else:
                print("FAKE")
                return
        # 딕셔너리에 문자가 없을 때
        if char not in msg_char_list.keys():
            msg_char_list.update({char:1})
        # 있으면서 3번째 일때
        elif msg_char_list[char]==2:
            msg_char_list[char] = 0
            is_third = char
        else:
            msg_char_list[char]+=1
    # 만약 3번 반복된 후에 한번더 반복했거나 모두 정상일때      
    if flag and is_third == 0:
        print("OK")
    # 만약 3번 반복후에 바로 문자열이 끝날 때
    else: 
        print("FAKE")
            
msg_list = []
for _ in range(num):
    msg_list.append(input())
for msg in msg_list:
    solution(msg)