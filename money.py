import tkinter
import time as t

#tkinter 로 만든 UI 표시
app = tkinter.Tk()

#tkinter로 만든 UI 수정하기
app.geometry('860x720+530+180')
app.title('Earn Money!')
app.resizable(0,0)

#변수 설정
earned = 0
grade = 0
money = 0
tm = 0
file = open('Earnings.txt','w')
file.write('주의! / 프로그램으로 자동 작성되는 파일입니다. 건들지 말아주세요!\n\n게임을 껐다 키면 기록이 초기화 됩니다.\n\n')
file.close()

def earn():
    global money
    money = money + 2.5
    label1.config(text = str(money)+' LAK')

def upgrade():
    global grade

def quit():
    app.destroy()

def get_money():
    global earned
    global tm
    tm = t.localtime(t.time())
    stm = t.strftime('%Y-%m-%d %I:%M:%S %p', tm)
    earned = money * 0.068
    file = open('Earnings.txt','a')
    file.write(str(stm)+' / 현재 얻은 돈 : '+str(earned)+' 원\n')
    file.close()
    
    
label1 = tkinter.Label(app, text = '0 LAK', font = ('HY견고딕',36))
label2 = tkinter.Label(app, text = '현재 환율 : 1 LAK : 0.068 WON', font = ('맑은 고딕',24))
label3 = tkinter.Label(app, text = '게임을 끄면 현재 얻은돈이 모두 초기화 됩니다.', font = ('맑은 고딕',12))

b1 = tkinter.Button(app, text = '돈벌기', command = earn)
b2 = tkinter.Button(app, text = '업그레이드(준비중)', command = upgrade)
b3 = tkinter.Button(app, text = '기록하기', command = get_money)
b4 = tkinter.Button(app, text = '종료하기', command = quit)

label1.place(x = 410, y = 370, anchor = 'center')
label2.place(x = 410, y = 20, anchor = 'center')
label3.place(x = 410, y = 700, anchor = 'center')

b1.place(relx = '0.05', rely = '0.75')
b2.place(relx = '0.35', rely = '0.75')
b3.place(relx = '0.7', rely = '0.75')
b4.place(relx = '0.9', rely = '0.75')

app.mainloop()
