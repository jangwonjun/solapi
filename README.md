# solapi
<div><h2>전송 파일 구성법</h2>
전송 파일을 구성하는것이 기존의 Reference에서 찾아보기 매우 귀찮게 되어있습니다. <br>
간단하게 말하자면, 그냥 Solapi에 있는 Reference 그대로 구성하면 문자 전송이 가능합니다. <br>
<pre>
└── lib
    ├── __init__.py
    ├── auth.py
    ├── config.ini
    ├── config.py
    ├── message.py
    └── storage.py
</pre>
다음과 파일을 구성해두면, 문자 전송이 가능합니다. <br>
그다음, 가장 중요한 세팅이 gitignore을 설정해두긴 했지만, config.ini 파일을 구성해야합니다. <br>
config.ini는 간단하게 생각하자면, Flask에서 env.py를 설정하는거와 같다고 생각하시면 됩니다. <br>
즉 한마디로 정리하자면, Enum Class를 설정하는 파일이라고 생각하시면 편할것 같습니다. <br>
어려운게 아니니까 딱히 겁 먹으실 필요는 없고요! 바로 살펴보죠! <br>
<pre><code>
 [AUTH]
# 계정의 API Key와 API Secret을 입력해주세요
api_key ="API KEY"
api_secret = = "SECRET KEY"

[SERVER]
domain = api.solapi.com
protocol = https
prefix = 
</code></pre>
다음과 같이 config.ini를 구성하시면 문자 전송을 위한 기본적인 세팅이 끝이 납니다. 
</div>

<div>
<h2>문자 기본 전송양식</h2>
기본적인 문자 전송 양식입니다. main()으로 선언하고 할당할 필요는 없습니다. <br>
한번에 10,000까지 동시에 전송이 가능합니다. <br>

<pre><code>
  data = {
            'messages': [
                {
                    'to': send[i],
                    'from': SEND.SENDNUMBER,
                    'subject': '즐거운 새해',
                    'imageId': '이미지ID를 입력하세요. 단, 이미지는 res로 따로 업로드 해야합니다.',
                    'text': '원하는 메시지를 보내보세요!'
                }
            ]
        }
        
  res = message.send_many(data)
  print(f"{send[i]}에게 성공적으로 전송했습니다")
  print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))

  
</code></pre>
</div>

<div><h2>이미지 업로드 방식</h2>
이미지를 업로드하는것은 상당한 민감한 조건이 붙습니다. <br>
우선 jpg의 이미지만 전송이 가능합니다. <br>
또한 200kb 미만의 사진만 전송이 가능하다는점을 유념하여 전송하시길 바랍니다. <br>
  
<pre><code>
res = storage.upload_image('image.jpg')
print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
</code></pre>

다음과 같은 방법으로 문자에 사진을 추가하여 전송할 수 있습니다. <br>
사진을 추가하여 전송하면, 문자 길이와 상관없이 자동으로 mms로 전환됩니다. <br>
즉 전송 요금이 올라간다는것 입니다. <br>
</div>

<div><h2>데이터 정제 방식</h2>
데이터를 정제할때 다음과 같은 방식으로 접근하면 처리가 매우 쉽습니다. <br>
<pre><code>
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
</code></pre>
다음과 같은 코드를 유념하시여, 문자전송을 시도해보시길 바랍니다! <br>
</div>

