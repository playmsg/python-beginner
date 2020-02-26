'''
应用名称 百度语音合成（TTS）随便实现版
AppID 1000000
API key XXX
Secret Key XXX
spd	String	语速，取值0-9，默认为5中语速
pit	String	音调，取值0-9，默认为5中语调
vol	String	音量，取值0-15，默认为5中音量
per	String	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成度丫丫，默认为普通女
'''
from aip import AipSpeech
#试了好多MP3播放库，就这个比较简单还好用，在win10和ubuntu下测试都通过了
from playsound import playsound
#记得下面这3个参数的值换成自己在百度云（不是百度网盘！！！）申请到的，不要把XXX换成XOXOXO，那没用
APP_ID = '1000000'
API_KEY = 'XXX'
SECRET_KEY = 'XXX'
#这个显然是要朗读的文字
myText = '白洁是个年轻漂亮的女子'
readOpt = {
    'vol' :8,
    #根据我的经验来说，默认的这个0女生听着还正常一点，那个什么情感合成语音十分制杖
    'per' :0,

}
AIread = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
readRes = AIread.synthesis(myText,'zh',1,readOpt)
#判断如果取回来的是二进制的什么数据流，就写进文件，如果反回来是个字符dict那就是出错了，我也不想处理
if not isinstance(readRes, dict):
    with open('mytext.mp3', 'wb') as f:
        f.write(readRes)
    playsound(r'mytext.mp3')