import re

#re.match() 예제 코드
#알파벳 소문자로 시작하는지 확인
pattern = r'^[a-z]'
text = 'example'

match = re.match(pattern, text)
if match:
    print('문자열은 알파벳 소문자로 시작합니다.')
else:
    print('문자열은 알파벳 소문자로 시작하지 않습니다.')

    
#re.search() 예제 코드
#주어진 패턴이 문자열에서 어디에든지 일치하는 경우 찾기
import re

pattern = r'apple'
text = 'I have an apple and a banana.'

match = re.search(pattern, text)
if match:
    print('일치하는 패턴을 찾았습니다!')
else:
    print('일치하는 패턴을 찾지 못했습니다.')
    
    
#re.findall() 예제 코드
#문자열에서 패턴과 일치하는 모든 부분을 찾아 리스트로 반환
import re

pattern = r'\d+'  # 숫자에 해당하는 패턴
text = '10 apples, 20 bananas, 30 oranges'

matches = re.findall(pattern, text)
print(matches
      
      
#re.finditer() 예제 코드
#문자열에서 패턴과 일치하는 모든 부분을 찾아 이터레이터로 반환
import re

pattern = r'\d+'  # 숫자에 해당하는 패턴
text = '10 apples, 20 bananas, 30 oranges'

matches = re.finditer(pattern, text)
for match in matches:
    print('일치하는 패턴:', match.group())

     
#reference(참조) : chat-GPT
