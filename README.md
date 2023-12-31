# solapi
<div>
<h2>문자 기본 전송양식</h2>
기본적인 문자 전송 양식입니다. main()으로 선언하고 할당할 필요는 없습니다. <br>
한번에 10,000까지 동시에 전송이 가능합니다. <br>

<pre><code>
  data = {
            'messages': [
                {
                    'to': data[i],
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
