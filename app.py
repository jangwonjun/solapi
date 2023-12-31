import json
from src.lib import message, storage
from env import SEND

def clean_number():
       with open('list.csv',encoding='utf-8') as f:
        file =f.read()
        phone_number = file.split(',')

        cleaned_data = []
        current_name = None

        for item in phone_number:
            if item.strip():  # 빈 문자열이 아닌 경우에만 처리
                if item.isdigit():
                    cleaned_data.append([current_name, item])
                else:
                    current_name = item.strip()

        real_result = []

        for i in range(len(cleaned_data)):
            real_result.append('010'+cleaned_data[i][1])
   
        return real_result
             
def set_sms_message():
    print("전송할 메세지를 입력합니다. SMS 타입에 한글 45자, 영자 90자 이상 입력되면 오류가 발생합니다.")
    
         

if __name__ == '__main__':
    send = clean_number()
    print(send)
    res = storage.upload_image('image.jpg')
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
    
    
    for i in range((len(send))):
        
        data = {
            'messages': [
                {
                    'to': data[i],
                    'from': SEND.SENDNUMBER,
                    'subject': '즐거운 새해',
                    'imageId': 'ST01FZ231231012815743E3YyJdSE3j5',
                    'text': '안녕하세요 :) \n다사다난했던 2023년이 마무리 되어 갑니다. 새해에는 소망하시는 일들 모두 이루어지시고 \n늘 행복한 일만 가득한 해가 되시길 기원합니다. 새해복 많이 받으세요!\n장원준 올림'
                }
            ]
        }
        
        res = message.send_many(data)
        #print(f"{send[i]}에게 성공적으로 전송했습니다")
        print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
        
    
        
    
