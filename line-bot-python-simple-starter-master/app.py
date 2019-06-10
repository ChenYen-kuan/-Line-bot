# 運行以下程式需安裝模組: line-bot-sdk, flask

# 引入flask模組
from flask import Flask, request, abort
# 引入linebot相關模組
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

# MessageEvent: 收到訊息的處理器
# TextMessage: 接收使用者文字訊息的處理器
# StickerMessage: 接收使用者貼圖訊息的處理器
# TextSendMessage: 回傳文字訊息的處理器
# StickerSendMessage: 回傳貼圖訊息的處理器
# 如需增加其他處理器請參閱以下網址的 Message objects 章節
# https://github.com/line/line-bot-sdk-python
from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn
)

# 定義應用程式是一個Flask類別產生的實例
app = Flask(__name__)

# LINE的Webhook為了辨識開發者身份所需的資料
# 相關訊息進入網址(https://developers.line.me/console/)
CHANNEL_ACCESS_TOKEN = 'DWPmhGNF0zaf75ONaQuF9QCzkdnK10KrIrRJpAp01QO3V5uTqGCoaDNMVIfx63f/5ltaA5T94xDE3UAX3q59z0ArgISROg21Zs1b4LfHuYmp015UxBDZBpcw03dGba6Qb9t5ahXPT0Kpoi6tCwbnrAdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '6a6e2383e592ff49b79df4b2f0916fdc'

# ================== 以下為 X-LINE-SIGNATURE 驗證程序 ==================

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/", methods=['POST'])
def callback():
    # 當LINE發送訊息給機器人時，從header取得 X-Line-Signature
    # X-Line-Signature 用於驗證頻道是否合法
    signature = request.headers['X-Line-Signature']
    print('[REQUEST]')
    print(request)
    print('[SIGNATURE]')
    print(signature)

    # 將取得到的body內容轉換為文字處理
    body = request.get_data(as_text=True)
    print("[BODY]")
    print(body)

    # 一但驗證合法後，將body內容傳至handler
    try:
        print('[X-LINE-SIGNATURE驗證成功]')
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
# ================== 以上為 X-LINE-SIGNATURE 驗證程序 ==================


# ========== 文字訊息傳入時的處理器 ==========
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 當有文字訊息傳入時
    # event.message.text : 使用者輸入的訊息內容
    print('[使用者傳入文字訊息]')
    print(str(event))
    #問答表
    faq = {
        "BTS": TextSendMessage(text="出道日期\
\nK:2013/06/13\
\nJ:2014/06/04\
\n\
\n粉絲名公佈日期\
\n2013/07/09\
\n\
\n首張單曲\
\n2013年2 COOL 4 SKOOL-NoMoreDream\
\n\
\n正規專輯\
\n	2014 DARK & WILD-Danger\
\n	2016 WINGS-BloodSweat&Tears\
\n	2018 Love Yourself 轉 ‘Teat’-FakeLove(告示牌專輯榜冠軍)\
\n迷你專輯\
\n	2013 O! R U L 8, 2? -N.O\
\n	2014 Skool Luv Affair-Boy in Luv\
\n	2015 花樣年華 pt.1 – I Need U\
\n	2015 花樣年華 pt.2 -Run\
\n	2017  Love Yourself 承 ‘Her’- DNA\
\n	2019年《MAP OF THE SOUL : PERSONA》\
\n特別專輯\
\n	2014 Skool Luv Affair Special Addition \
\n	2016 花樣年華 Young Forever -Fire\
\n	2017 You Never Walk Alone- SpringDay\
\n	2018 Love Yourself 結 ‘Answer’-IDOL(告示牌專輯榜冠軍)\
\nLY系列\
\n•Love Yourself起Wonder/JK-Euphoria\
\n•Love Yourself承Her/JM-Serendipity\
\nDNA 2017/9/18\
\n•Love Yourself轉Tear/V-Singularity\
\nFakeLove 2018/5/18\
\n•Love Yourself結Answer/JIN-Epiphany\
\nIDOL 2018/8/24\
\n歷年來台時間\
\n2015/03/08\
\n2016/06/09\
\n2017/10/21、22\
\n2018/12/8 、9\
\n\
\n年齡順序\
\nJIN-SUGA-JHOPE-RM-JIMIN-V-JUNGKOOK\
\n應援口號順序\
\n金南俊-金碩珍-閔玧其-鄭號錫-朴智旻-金泰亨-田柾國-BTS\
\nMV破億順序\
\nDOPE\
\nFIRE\
\n血汗淚\
\n男子漢\
\nSaveMe\
\nNotToday\
\nSpringDay\
\nDNA\
\nDanger\
\nI NEED U\
\n荷爾蒙戰爭\
\nMicDrop\
\nFakeLove\
\nIDOL\
\n共14支\
\n破一億\
\nDanger\
\nI NEEDU\
\n荷爾蒙戰爭\
\n破兩億\
\n男子漢\
\nSaveMe\
\nNotToday\
\nSpringDay\
\nIDOL\
\n破三億\
\nDOPE\
\n血汗淚\
\nMicDrop\
\nFakeLove\
\n破四億\
\nFIRE\
\n破五億\
\nDNA\
"),
        "seventeen":TextSendMessage(text=".\n出道日期：\
\n	K:2015/05/26\
\n	J:2018/05/30\
\n粉絲名公佈日期：\
\n	2016/02/14\
\n\
\n韓語：\
\n正規專輯\
\n2016 Love & Letter\
\n2016 Love & Letter（改版專輯）\
\n2017 TEEN, AGE\
\n迷你專輯\
\n2015 17 CARAT\
\n2015 BOYS BE\
\n2016 Going Seventeen\
\n2017 Al1\
\n2018 YOU MAKE MY DAY\
\n2019 YOU MADE MY DAWN\
\n特別專輯\
\n2018 DIRECTOR'S CUT\
\n精選輯\
\n2016 17 Hits\
\n日語：\
\n迷你專輯\
\n2018 We Make You\
\n單曲\
\n2019 Happy Ending\
\n年齡（排序）：\
\n	S.coups 1995/08/08\
\n淨漢 1995/10/04\
\nJoshua 1995/12/30\
\nJun 1996/06/10\
\nHoshi 1996/06/15\
\n	圓佑 1996/07/17\
\n	Woozi 1996/11/22\
\n	DK 1997/02/18\
\n	珉奎 1997/04/06\
\n	The8 1997/11/07\
\n	勝寬 1998/01/16\
\n	Vernon 1998/02/18\
\n	Dino 1999/02/11\
\n\
\n歷年來臺：\
\n	2017/10/01\
\n	2018/10/06\
\n小分隊(第一個為隊長)：\
\n	Hip-pop: S.coups 圓佑 珉奎 Vernon\
\n	Vocal: WOOZI淨漢 Joshua DK 勝寛\
\n	Performance：Hoshi Jun The8 Dino\
\nMV破億：\
\n	2018/10/23 Don't Wanna Cry 破億\
\n	2+0+1+8+1+0+2+3=17\
"),
        "TWICE": TextSendMessage(text="\n出道日期：	\
\n	K：2015/10/20\
\n	J：2017/06/28\
\n粉絲名公佈日期：\
\n	2015/11/04\
\n韓語：\
\n	正規專輯\
\n2017/10/30 Twicetagram\
\n改版專輯\
\n2017/12/11 Merry&Happy \
\n迷你專輯\
\n2015/10/20 THE STORY BEGINS\
\n2016/04/25 PAGE TWO\
\n2016/10/24 TWICEcoaster: LANE 1\
\n2017/05/15 SIGNAL\
\n2018/04/09 What is Love?\
\n2018/11/05 YES or YES\
\n2019/04/22 FANCY YOU\
\n特別專輯\
\n2017/02/20 TWICEcoaster: LANE 2\
\n2018/07/09 Summer Nights\
\n2018/12/12 The year of Yes\
\n日語\
\n正規專輯\
\n2018/09/12 BDZ \
\n改版專輯\
\n2018/12/26 BDZ -Repackage-\
\n精選專輯\
\n2017/06/28 #TWICE\
\n2019/03/06 #TWICE2\
\n單曲\
\n2017/10/18 One More Time\
\n2018/02/07 Candy Pop\
\n2018/05/16 Wake Me Up\
\n2019/07/17 HAPPY HAPPY\
\n2019/07/24 Breakthrough\
\n\
\nOST\
\n2018/06/15 I WANT YOU BACK\
\n\
\n成員年齡（排序）：\
\n	娜璉(林娜璉) 1995/09/22\
\n	定延(俞定延) 1996/11/11\
\n	Momo(平井桃) 1996/11/09\
\n	Sana(湊崎紗夏) 1996/12/29\
\n	志效(朴志效) 1997/02/01\
\n	Mina(名井南) 1997/03/24\
\n	多賢(金多賢) 1998/05/28\
\n	彩瑛(孫彩瑛) 1999/04/23\
\n	子瑜(周子瑜)1999/06/14\
\n\
\n歷年來臺\
\n	QQ尚未\
\n\
\n應援口號順序\
\n林娜璉-俞定延-Momo醬- Sana醬-朴志效- Mina醬-金多賢-孫彩瑛-周子瑜 one in a million 世界上獨一無二的 Twice\
\n\
\nMV破億順序\
\nlike ooh ahh \
\n一億2016 11.11 兩億2017 11.02\
\ncheer up\
\n一億 2016 11.17 兩億 2017 08.09 三億2018 11.04\
\nTT \
\n一億2017 01.02 兩億2017 05.26 三億2017/12/22 四億2018 09.17\
\nknock knock \
\n一億2017 05.20 兩億2018 08.05\
\nSignal\
\n一億2017.08.30 兩億2019 02.07\
\nLikey\
\n一億2017.12.03 兩億2018.03.08 三億2018.09.16\
\nheart shaker\
\n一億2018.01.22 兩億2018.07.11\
\nWhat is love \
\n一億2018.05.15 兩億2018.10.11\
\nDance The Night Away \
\n一億2018.09.06\
\nYes or Yes \
\n一億2018 12.14\
"),
        "SJ": TextSendMessage(text="\n出道日期：\
\n	韓國 2005年11月6日\
\n日本 2011年6月8日\
\n\
\n粉絲名公佈日期：\
\n	ELF（Ever Lasting Friends）2006年06月02日\
\n粉絲名由隊長利特命名：意思為永遠的朋友\
\n\
\n應援色：寶藍色\
\n\
\n生日(順序)：\
\n利特 1983/07/01\
\n希澈 1983/07/10\
\n藝聲 1984/08/24\
\n強仁 1985/01/17\
\n神童 1985/09/28\
\n晟敏 1986/01/01\
\n銀赫 1986/04/04\
\n始源 1986/04/07\
\n東海 1986/10/15\
\n厲旭 1987/06/21\
\n圭賢 1988/02/03\
\n\
\n離隊成員\
\n韓庚 1984/02/09\
\n起範 1987/08/21\
\n\
\nSJ-M成員\
\n周覓 1986/04/19\
\n亨利 1989/10/11\
\n\
\n小分隊：\
\nK.R.Y：圭賢、厲旭、藝聲\
\n出道日期 2006年11月5日\
\nSJ-T：利特 、希澈、 強仁、神童、 晟敏、銀赫\
\n出道日期 2007年2月23日\
\nSJ-Happy：利特、藝聲、 強仁、神童、 晟敏、銀赫\
\n出道日期 2008年6月5日\
\nSJ-M：晟敏、銀赫、始源、東海、厲旭、圭賢、周覓、Henry\
\n出道日期 2008年4月8日\
\nSJ-D&E：東海、銀赫\
\n出道日期 2011年12月16日\
\n\
\n正規專輯：\
\n韓語正規專輯\
\n2005：Super Junior05\
\n2007：Don't Don\
\n2009：Sorry, Sorry\
\n2010：Bonamana / No Other\
\n2011：Mr. Simple / A-CHA\
\n2012：Sexy, Free & Single / SPY\
\n2014：Mamacita / This Is Love\
\n2017：Play\
\n特別專輯\
\n2015：Devil / Magic\
\n\
\n特別迷你專輯\
\n2018：One More Time\
\n單曲\
\n2006：U\
\n\
\n出道10周年特別紀念專輯\
\n2015：Devil / Magic\
\n日語正規專輯\
\n2013：Hero\
\n歷年來臺：\
\n2007-06-16、2007-11-22、2008-01-05、2009-06-27、2010-02-20、2011-03-11、2011-11-26、2012-02-02、2012-06-09、2013-08-10、2014-11-29、2015-03-21、2016-2-13、2018-3-31、2018-08-11、\
\n2019-01-26、2019-03-28\
\nMV破億順序：\
\n	Mr.Simple\
\n	Bonamana\
\n	Sorry, Sorry\
"),
        "EXO": TextSendMessage(text="\n出道期：\
\n	K：2012/04/08\
\n	J：2015/11/04\
\n粉絲名公佈期：\
\n	2014/08/05\
\n韓語：\
\n	正規專輯\
\n2013: XOXO (Kiss&Hug)\
\n2015: EXODUS\
\n2016: EX'ACT\
\n2017: The War\
\n2018: DON'T MESS UP MY TEMPO\
\n迷你專輯\
\n2012: MAMA\
\n2014: Overdose\
\n冬季特別專輯\
\n2013: Miracles In December\
\n2015: Sing For You\
\n2016: For Life\
\n2017: Universe\
\n日語：\
\n	單曲：\
\n2015 Love Me Right ~romantic universe~\
\n2016 coming over\
\n專輯：\
\n2018 COUNTDOWN\
\n成員年齡：\
\n	Xiumin 1990/3/26\
\n	Suho 1991/5/22\
\n	Lay 1991/10/7\
\n	Baekhyun 1992/5/6\
\n	Chen 1992/9/21\
\n	Chanyeol 1992/11/27\
\n	D.O. 1993/1/12\
\n	Kai 1994/1/14\
\n	Sehun 1994/4/12\
\n\
\n歷年來臺：\
\n	2014/07/11 2015/06/12 2016/11/26 2018/02/10 2019/05/18（CHEN） 2019/03/30\
\n小分隊：\
\n	EXO-K\
\n	EXO-M\
\n	EXO-CBX\
"),
        "GOT7":TextSendMessage(text="\n出道期：\
\n	K：2014/01/16\
\n	J：2014/10/22\
\n粉絲名公佈期：\
\n	2014/05/09\
\n韓語：\
\n	正規專輯\
\nIdentify 2014/11/18\
\nFLIGHT LOG : TURBULENCE 2016/9/27\
\nPresent: YOU 2018/9/17\
\n改版專輯\
\nMAD Winter Edition 2015/11/23\
\n7 for 7 Present Edition 2017/12/7\
\n<Present : YOU> &ME Edition 2018/12/3\
\n迷你專輯\
\nGot it? 2014/1/20\
\nGOT♡ 2014/6/23\
\nJust right 2015/7/13\
\nMAD 2015/9/29\
\nFLIGHT LOG : DEPARTURE 2016/3/21\
\nFLIGHT LOG : ARRIVAL 2017/3/13\
\n7 for 7 2017/10/10\
\nEyes On You 2018/3/12\
\nSPINNING TOP : BETWEEN SECURITY & INSECURITY 2019/5/20\
\n日語：\
\n	正規專輯\
\n翻天↑覆地  2016/2/3\
\n迷你專輯\
\nHey Yah 2016/11/16\
\nTURN UP 2017/11/15\
\nI WON'T LET YOU GO 2019/1/30\
\n單曲\
\nAROUND THE WORLD 2014/10/22\
\nLOVE TRAIN 2015/6/10\
\nLAUGH LAUGH LAUGH 2015/9/23\
\nMY SWAGGER 2017/5/24\
\nTHE New Era  2018/6/20\
\n年齡排序：\
\nMark 1993/09/04\
\nJB 1994/01/06\
\nJackson 1994/03/28\
\n珍榮1994/09/22\
\nYoungJae 1996/09/17\
\nBamBam 1997/05/02\
\nYuGyeom 1997/11/17\
\n歷年來臺：\
\n	2015/01/20、2017/01/16、2018/06/16、2019/04/14(Jus2)\
"),

    "組長": TextSendMessage(text="Kevin\t林彥宇"),
    "組員": TextSendMessage(text="Ken\t陳彥寬\nMark\t梁健彬"),
    }
    

    # # 準備要回傳的文字訊息
    if event.message.text in faq:
        reply = faq[event.message.text]
    else:
        reply = TextSendMessage(text="啥玩意兒阿？？"),StickerSendMessage(package_id='2', sticker_id='149')

    # 回傳訊息
    line_bot_api.reply_message(
        event.reply_token,
        reply)


# ========== 貼圖訊息傳入時的處理器 ==========
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    # 當有貼圖訊息傳入時
    print('[使用者傳入貼圖訊息]')
    print(str(event))

    # 準備要回傳的貼圖訊息
    # HINT: 機器人可用的貼圖 https://devdocs.line.me/files/sticker_list.pdf
    reply = StickerSendMessage(package_id='2', sticker_id='149')

    # 回傳訊息
    line_bot_api.reply_message(
        event.reply_token,
        reply)


import os
if __name__ == "__main__":
    print('[伺服器開始運行]')
    # 取得遠端環境使用的連接端口，若是在本機端測試則預設開啟於port5500
    port = int(os.environ.get('PORT', 5500))
    # 使app開始在此連接端口上運行
    print('[Flask運行於連接端口:{}]'.format(port))
    # 本機測試使用127.0.0.1, debug=True
    # Heroku部署使用 0.0.0.0
    app.run(host='127.0.0.1', port=port, debug=True)
