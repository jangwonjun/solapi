import json
from src.lib import message, storage
import pandas
from env import SEND
from tqdm import tqdm

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
             
if __name__ == '__main__':
    #print(clean_number())
    #final_send_target = clean_number()
    send = clean_number()
    print(send)
    res = storage.upload_image('images.jpeg')
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
    
    
    for i in range((len(send))):
        data = {
            'messages': [
                {
                    'to': send[i],
                    'from': SEND.SENDNUMBER,
                    'subject': '즐거운 한가위',
                    'imageId': 'ST01FZ230928234046348JkjlWTXZx7V',
                    'text': '안녕하세요 :) 어느새 신선한 바람이 부는 추석입니다. 맑은 하늘을 마주하고 더없이 좋은 날씨를 함께하는 것에 감사한 하루입니다. 올해도 대박 나시고 하시는 일마다 모두 이루시기를 기도합니다. 즐겁고 다복한 한가위 되세요! 장원준 올림'
                }
            ]
        }
        res = message.send_many(data)
        print(f"{send[i]}에게 성공적으로 전송했습니다")
        print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
        
        
    
