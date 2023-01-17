import random

import pyrebase
from aiogram import Dispatcher,Bot,types,executor
bot=Bot(token='5842402640:AAHvVfCyD-Tg0cl5n5SgGWhZxqWGiR6_xJQ')
dp=Dispatcher(bot)
import datetime
from math import floor


firebaseConfig={
"apiKey": "AIzaSyD_ELfpFmQTgpGBwzG5oEsU-m0CbWd3ZHg",
  "authDomain": "mybase-341d1.firebaseapp.com",
  "projectId": "mybase-341d1",
  "storageBucket": "mybase-341d1.appspot.com",
  "messagingSenderId": "73297747191",
  "appId": "1:73297747191:web:2f4fcc8ad1b0f045f9c7f2",
  "measurementId": "G-LB3XJ1ZVKS",
    "databaseURL":"https://mybase-341d1-default-rtdb.firebaseio.com"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()



start_test=types.InlineKeyboardButton(text='Testni Boshlash✅',callback_data='tstart')
start_test_markup=types.InlineKeyboardMarkup().add(start_test)
this_user_access=''
this_user=''
len_u=len(db.child('Users').get().val().keys())+1
@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    global db
    global this_user
    global this_user_access
    global len_u
    len_u=len(db.child('Users').get().val().keys())+1
    is_equal=False
    for i in range(2,len_u):
        data=db.child('Users').child('u'+str(i)).child('id').get().val()
        if data==message.from_user.id:
            is_equal=True
            break
        else:
            is_equal=False
    if is_equal:
        this_user_access=db.child('Users').child('u' + str(i)).child('access').get().val()
        this_user = 'u'+str(i)
    if is_equal==False:
        db.child('Users').child('u' + str(len_u)).set({"name":message.from_user.first_name,'id':message.from_user.id,"access":"false",'num':len_u})
        this_user_access=db.child('Users').child('u' + str(len_u)).child('access').get().val()
        this_user='u'+str(len_u)
    await message.answer(
        "Assalomu alaykum ustoz agar siz Boshlang'ich sinf ustozi bo'lsangiz biz bilan bilimingizni oshirishingiz mumkin biz sizga professional testlarni taqdim etamiz, bot sizda ishlashligi  uchun  @admin_name ga murojaat eting!\n\n"
        f"Tartib Raqamingiz: {len_u-1}\n\n"
        f"Sizning ID: {message.from_user.id}\n\n"
        'Tel: 👇👇 \n'
        '+998 91 121 23 99',
        reply_markup=start_test_markup
    )

stest_math=types.InlineKeyboardButton(text='Matematika',callback_data='math_start')
stest_phy=types.InlineKeyboardButton(text='Fizika',callback_data='phy_start')
start_kb_mk=types.InlineKeyboardMarkup().add(stest_math,stest_phy)
@dp.callback_query_handler(text='tstart')
async def tstartfun(call:types.CallbackQuery):
    global len_u
    len_users= list(db.child('Users').get().val().keys())
    for i in range(2,len(len_users)+1):
        thisuser=db.child('Users').child('u'+str(i)).child('id').get().val()
        if thisuser==call.from_user.id:
            access = db.child('Users').child('u' + str(i)).child('access').get().val()
            break

    if access=='true':
        await call.message.edit_text(
            "Assalomu Alaykum\n"
            "🎉Botdan Foydalanayotganingizdan Xursandman🎊\n"
            "O'zingizga Kerakli Fanni Tanlashingiz Mumkun 👇\n"
            "🗒 Eslatma :\n\n"
            "Yo'nalishni Tanlaganingizdan So'ng ortga qayta olmaysiz❗"
            ,reply_markup=start_kb_mk
        )
    if access=='false':
        await call.message.answer(
            "Botdan foydalanish uchun @admin_name ga murojat qiling:\n\n"
            "Qo`ng`iroq qiling\n\n"
            "☎️+998901511177\n\n"
            "☎️ +998975951177\n\n"
            "👆 👆 👆 👆\n\n"
            "Admin Sizga Foydalanish Huhuqini Bergandan So'ng ' Testni Boshlash✅ ' Tugmasini Bosing"
        )

start_math_test_btn=types.InlineKeyboardButton(text='Start🟢',callback_data="rmathStart")
start_math_test_kb=types.InlineKeyboardMarkup().add(start_math_test_btn)

start_phy_test_btn=types.InlineKeyboardButton(text='Start🟢',callback_data="rphyStart")
start_phy_test_kb=types.InlineKeyboardMarkup().add(start_phy_test_btn)

@dp.callback_query_handler(text=['math_start','phy_start'])
async def startAccessedTest(call:types.CallbackQuery):

    if call.data=='math_start':
        len_users_frm = list(db.child('Users').get().val().keys())
        this_usr=''
        for i in range(2, len(len_users_frm) + 1):
            thisuser_frm = db.child('Users').child('u' + str(i)).child('id').get().val()
            if thisuser_frm == call.from_user.id:
                access = db.child('Users').child('u' + str(i)).child('access').get().val()
                this_usr='u'+str(i)
                break
        if access=='true':
            db.child('Users').child('u' + str(i)).update({'access':'false'})

        await call.message.edit_text(
            "Matematika Fanidan Testni Boshlash Uchun ' Start🟢'tugmasini bosing .\n"
            "❗️❗️Eslatib O'tamiz : \n\n"
            "❗️❗️Endi Ortga Qaytishni Iloji Yoq❗️❗️\n\n"
            "⏰ Sizga 40 daqiqa vaqt beriladi\n"
            "4️⃣0️⃣daqiqadan so'ng test avtomatik tarzda tugatiladi ❗\n\n"
            "Agar Test Yechish Mobaynida Chiqib Ketib Qolsangiz Test Avtomatik Tugatiladi ❗",
            reply_markup=start_math_test_kb
        )
    if call.data=='phy_start':
        len_users_frm = list(db.child('Users').get().val().keys())
        this_usr = ''
        for i in range(2, len(len_users_frm) + 1):
            thisuser_frm = db.child('Users').child('u' + str(i)).child('id').get().val()
            if thisuser_frm == call.from_user.id:
                access = db.child('Users').child('u' + str(i)).child('access').get().val()
                this_usr = 'u' + str(i)
                break
        if access == 'true':
            db.child('Users').child('u' + str(i)).update({'access': 'false'})

        await call.message.edit_text(
            "Fizika Fanidan Testni Boshlash Uchun ' Start🟢'tugmasini bosing .\n"
            "❗️❗️Eslatib O'tamiz : \n\n"
            "❗️❗️Endi Ortga Qaytishni Iloji Yoq❗️❗️\n\n"
            "⏰ Sizga 40 daqiqa vaqt beriladi\n"
            "4️⃣0️⃣daqiqadan so'ng test avtomatik tarzda tugatiladi ❗\n\n"
            "Agar Test Yechish Mobaynida Chiqib Ketib Qolsangiz Test Avtomatik Tugatiladi ❗",
            reply_markup=start_phy_test_kb
        )





ans_a=types.InlineKeyboardButton(text='A',callback_data='at')
ans_b=types.InlineKeyboardButton(text='B',callback_data='bt')
ans_c=types.InlineKeyboardButton(text='C',callback_data='ct')
ans_d=types.InlineKeyboardButton(text='D',callback_data='dt')
next_quest=types.InlineKeyboardButton(text='Keyingisi',callback_data='qnext')
rp_mk_kb_opt_true=types.InlineKeyboardMarkup(row_width=2).add(ans_a,ans_b,ans_c,ans_d,next_quest)

f_ans_a=types.InlineKeyboardButton(text='A',callback_data='atf')
f_ans_b=types.InlineKeyboardButton(text='B',callback_data='bf')
f_ans_c=types.InlineKeyboardButton(text='C',callback_data='cf')
f_ans_d=types.InlineKeyboardButton(text='D',callback_data='df')
f_next_quest=types.InlineKeyboardButton(text='Keyingi',callback_data='qnextf')
fiz_rp_mk_kb_opt_true=types.InlineKeyboardMarkup(row_width=2).add(f_ans_a,f_ans_b,f_ans_c,f_ans_d,f_next_quest)
t=0
randomed_quests=[]
qname=''
qa=''
qb=''
qc=''
qd=''
all=0
timer = []
ltime=0
rmtime=0
tm=0
timestart=False
@dp.callback_query_handler(text=['rphyStart','rmathStart'])
async def RealStarts(call:types.CallbackQuery):
    global timer
    global randomed_quests
    global t
    global ltime
    global qname
    global qa
    global qb
    global qc
    global qd
    global all
    global rmtime
    global tm
    global timestart
    if call.data=='rmathStart':
        randomed_quests=[]
        len_tests = len(list(db.child('tests').child('matematika').get().val().keys()))
        all=0
        for i in range(1,11):
            randomise=random.randint(2,len_tests)
            if randomise not in randomed_quests:
                randomed_quests.append(randomise)
                print('rs',randomise)

            else:
                randomm=random.randint(2,len_tests)
                if randomm not in randomed_quests:
                    randomed_quests.append(randomm)
                    print('rm',randomm)
                else:
                    if randomm+1<10:
                        randomed_quests.append(randomm+1)
                        print('rm', randomm+1)
                    else:
                        randomed_quests.append(randomm -1)
                        print('rm', randomm-1)

        timer = []
        timer.append(datetime.datetime.now().minute)
        print(timer)
        tm = timer[0] + 1
        ltime = tm - datetime.datetime.now().minute
        print(ltime)
        t=0
        qname=db.child('tests').child('matematika').child('t'+str(randomed_quests[t])).child('quest').child('name').get().val()
        qa=db.child('tests').child('matematika').child('t'+str(randomed_quests[t])).child('a').child('option').get().val()
        qb=db.child('tests').child('matematika').child('t'+str(randomed_quests[t])).child('b').child('option').get().val()
        qc=db.child('tests').child('matematika').child('t'+str(randomed_quests[t])).child('c').child('option').get().val()
        qd=db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('d').child('option').get().val()
        print(qname)


        await call.message.edit_text(
            f"Savol : {qname}\n\nA: {qa}\nB: {qb}\nC: {qc}\nD: {qd}\n\nQolgan Vaqtingiz: {ltime}minut\n\nJavobingizni Tanlang: \n"
            ,reply_markup=rp_mk_kb_opt_true
        )


        print('end')
    # ####################################### Fizika # #########################
    if call.data=='rphyStart':
        randomed_quests = []
        f_len_tests = len(list(db.child('tests').child('fizika').get().val().keys()))
        f_all = 0
        for i in range(1, 5):
            randomise = random.randint(1, f_len_tests)
            if randomise not in randomed_quests:
                randomed_quests.append(randomise)
                print('rs', randomise)

            else:
                randomm = random.randint(1, f_len_tests)
                if randomm not in randomed_quests:
                    randomed_quests.append(randomm)
                    print('rm', randomm)
                else:
                    if randomm + 1 < 5:
                        randomed_quests.append(randomm + 1)
                        print('rm', randomm + 1)
                    else:
                        randomed_quests.append(randomm - 1)
                        print('rm', randomm - 1)

        timer = []
        timer.append(datetime.datetime.now().minute)
        print(timer)
        tm = timer[0] + 1
        ltime = tm - datetime.datetime.now().minute
        print(ltime)
        f_t = 0
        qname = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('quest').child('name').get().val()
        qa = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('a').child('option').get().val()
        qb = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('b').child('option').get().val()
        qc = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('c').child('option').get().val()
        qd = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('d').child('option').get().val()
        print(qname)

        await call.message.edit_text(
            f"Savol : {qname}\n\nA: {qa}\nB: {qb}\nC: {qc}\nD: {qd}\n\nQolgan Vaqtingiz: {ltime}minut\n\nJavobingizni Tanlang: \n"
            , reply_markup=fiz_rp_mk_kb_opt_true
        )


asel=False
bsel=False
csel=False
dsel=False
@dp.callback_query_handler(text=['at', 'bt', 'ct', 'dt','qnext'])
async def checkTrueAns(call: types.CallbackQuery):
    global TrueAnswersCounter, all
    global rp_mk_kb_opt_true
    global randomed_quests
    global t
    global qname
    global qa
    global qb
    global qc
    global qd
    global ltime
    global db
    global selected_option
    global asel
    global bsel
    global csel
    global dsel
    global timer
    global tm
    global endedTime
    scd=''

    if call.data=='at':
        scd='a'
        asel = True
        bsel = False
        csel = False
        dsel = False
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa} ✅\n"
            f"B: {qb}\n"
            f"C: {qc}\n"
            f"D: {qd}\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=rp_mk_kb_opt_true
        )
    if call.data=='bt':
        scd='b'
        asel = False
        bsel = True
        csel = False
        dsel = False
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa}\n"
            f"B: {qb} ✅\n"
            f"C: {qc}\n"
            f"D: {qd}\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=rp_mk_kb_opt_true
        )
    if call.data=='ct':
        scd='c'
        asel = False
        bsel = False
        csel = True
        dsel = False
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa}\n"
            f"B: {qb}\n"
            f"C: {qc} ✅\n"
            f"D: {qd}\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=rp_mk_kb_opt_true
        )
    if call.data=='dt':
        scd='d'
        asel = False
        bsel = False
        csel = False
        dsel = True
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa}\n"
            f"B: {qb}\n"
            f"C: {qc}\n"
            f"D: {qd} ✅\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=rp_mk_kb_opt_true
        )
    print(asel,bsel,csel,dsel)
    if call.data=='qnext':
        ltime = tm - datetime.datetime.now().minute
        print(ltime)
        if asel==False and bsel==False and csel==False and dsel==False:
           try:
               await call.message.edit_text(
                f"Savol : {qname}\n\nA: {qa}\nB: {qb}\nC: {qc}\nD: {qd}\n\nQolgan Vaqtingiz: {ltime}minut\n\nJavobingizni Tanlang: \nAgar Variyantlardan birini tanlamasangiz keyingi savolga o'ta olmaysiz ❗️\n"
            ,reply_markup=rp_mk_kb_opt_true
            )
           except:
               pass
        else:
            try:
                print(ltime)
                if ltime==timer[0]:
                    await call.message.edit_text(
                        "Vaqt Tugadi"
                        f"Test Yakunlandi\n"
                        f"Jami Testlar: {len(randomed_quests)}"
                        f"To'gri Javob: {all}"
                        f"Xato Javob : {len(randomed_quests) - all}"
                    )
                else:
                    trueAnsA=db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('a').child('trust').get().val()
                    trueAnsB=db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('b').child('trust').get().val()
                    trueAnsC=db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('c').child('trust').get().val()
                    trueAnsD=db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('d').child('trust').get().val()
                    print('t' + str(randomed_quests[t]))
                    print(trueAnsA)
                    print(trueAnsB)
                    print(trueAnsC)
                    print(trueAnsD)
                    if asel:
                        if trueAnsA == 'true':
                            all += 1
                    if bsel:
                        if trueAnsB == 'true':
                            all += 1
                    if csel:
                        if trueAnsC == 'true':
                            all += 1
                    if dsel:
                        if trueAnsD == 'true':
                            all += 1
                    print(all)
                    t+=1

                    qname = db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('quest').child(
                        'name').get().val()
                    qa = db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('a').child(
                        'option').get().val()
                    qb = db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('b').child(
                        'option').get().val()
                    qc = db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('c').child(
                        'option').get().val()
                    qd = db.child('tests').child('matematika').child('t' + str(randomed_quests[t])).child('d').child(
                        'option').get().val()
                    await call.message.edit_text(
                        f"Savol : {qname}\n\nA: {qa}\nB: {qb}\nC: {qc}\nD: {qd}\n\nQolgan Vaqtingiz: {ltime}min\n\nJavobingizni Tanlang: \n"
                        , reply_markup=rp_mk_kb_opt_true
                    )
                    asel=False
                    bsel=False
                    csel=False
                    dsel=False

            except IndexError:
                await call.message.edit_text(
                    f"Test Yakunlandi\n"
                    f"Jami Testlar: {len(randomed_quests)}"
                    f"To'gri Javob: {all}"
                    f"Xato Javob : {len(randomed_quests)-all}"
                )
                all=0




####################### ##################       Fizika            ############################



f_asel=False
f_bsel=False
f_csel=False
f_dsel=False
@dp.callback_query_handler(text=['atf', 'btf', 'ctf', 'dtf','qnextf'])
async def checkTrueAns_fiz(call: types.CallbackQuery):
    global TrueAnswersCounter, all
    global rp_mk_kb_opt_true
    global randomed_quests
    global t
    global qname
    global qa
    global qb
    global qc
    global qd
    global ltime
    global db
    global selected_option
    global f_asel
    global f_bsel
    global f_csel
    global f_dsel
    global f_timer
    global f_tm
    global endedTime
    scd=''

    if call.data=='atf':
        scd='a'
        f_asel = True
        f_bsel = False
        f_csel = False
        f_dsel = False
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa} ✅\n"
            f"B: {qb}\n"
            f"C: {qc}\n"
            f"D: {qd}\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=fiz_rp_mk_kb_opt_true
        )
    if call.data=='btf':
        scd='b'
        f_asel = False
        f_bsel = True
        f_csel = False
        f_dsel = False
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa}\n"
            f"B: {qb} ✅\n"
            f"C: {qc}\n"
            f"D: {qd}\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=fiz_rp_mk_kb_opt_true
        )
    if call.data=='ctf':
        scd='c'
        f_asel = False
        f_bsel = False
        f_csel = True
        f_dsel = False
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa}\n"
            f"B: {qb}\n"
            f"C: {qc} ✅\n"
            f"D: {qd}\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=fiz_rp_mk_kb_opt_true
        )
    if call.data=='dtf':
        scd='d'
        f_asel = False
        f_bsel = False
        f_csel = False
        f_dsel = True
        await call.message.edit_text(
            f"Savol : {qname}\n\n"
            f"A: {qa}\n"
            f"B: {qb}\n"
            f"C: {qc}\n"
            f"D: {qd} ✅\n"
            f"Keyingisi Tugmasini Bosish orqali keyingi savolga o'tishingiz mumkun: \n"

            , reply_markup=fiz_rp_mk_kb_opt_true
        )
    print(f_asel,f_bsel,f_csel,f_dsel)
    if call.data=='qnextf':
        ltime = tm - datetime.datetime.now().minute
        print(ltime)
        if f_asel==False and f_bsel==False and f_csel==False and f_dsel==False:
           try:
               await call.message.edit_text(
                f"Savol : {qname}\n\nA: {qa}\nB: {qb}\nC: {qc}\nD: {qd}\n\nQolgan Vaqtingiz: {ltime}minut\n\nJavobingizni Tanlang: \nAgar Variyantlardan birini tanlamasangiz keyingi savolga o'ta olmaysiz ❗️\n"
            ,reply_markup=fiz_rp_mk_kb_opt_true
            )
           except:
               print("All False")
        else:
            try:
                print(ltime)
                if ltime==timer[0]:
                    await call.message.edit_text(
                        "Vaqt Tugadi"
                        f"Test Yakunlandi\n"
                        f"Jami Testlar: {len(randomed_quests)}"
                        f"To'gri Javob: {all}"
                        f"Xato Javob : {len(randomed_quests) - all}"
                    )
                else:
                    trueAnsA=db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('a').child('trust').get().val()
                    trueAnsB=db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('b').child('trust').get().val()
                    trueAnsC=db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('c').child('trust').get().val()
                    trueAnsD=db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('d').child('trust').get().val()
                    print('t' + str(randomed_quests[t]))
                    print(trueAnsA)
                    print(trueAnsB)
                    print(trueAnsC)
                    print(trueAnsD)
                    if f_asel:
                        if trueAnsA == 'true':
                            all += 1
                    if f_bsel:
                        if trueAnsB == 'true':
                            all += 1
                    if f_csel:
                        if trueAnsC == 'true':
                            all += 1
                    if f_dsel:
                        if trueAnsD == 'true':
                            all += 1
                    print(all)
                    t+=1

                    qname = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('quest').child(
                        'name').get().val()
                    qa = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('a').child(
                        'option').get().val()
                    qb = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('b').child(
                        'option').get().val()
                    qc = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('c').child(
                        'option').get().val()
                    qd = db.child('tests').child('fizika').child('t' + str(randomed_quests[t])).child('d').child(
                        'option').get().val()
                    await call.message.edit_text(
                        f"Savol : {qname}\n\nA: {qa}\nB: {qb}\nC: {qc}\nD: {qd}\n\nQolgan Vaqtingiz: {ltime}min\n\nJavobingizni Tanlang: \n"
                        , reply_markup=fiz_rp_mk_kb_opt_true
                    )
                    asel=False
                    bsel=False
                    csel=False
                    dsel=False

            except IndexError:
                await call.message.edit_text(
                    f"Test Yakunlandi\n"
                    f"Jami Testlar: {len(randomed_quests)}"
                    f"To'gri Javob: {all}"
                    f"Xato Javob : {len(randomed_quests)-all}"
                )




















###################             ADMIN PANEL         ###################
a_req=types.InlineKeyboardButton(text='Ruxsat Soraganlar 🟢',callback_data='reqs')
make_test=types.InlineKeyboardButton(text="Test Tuzish 🛠",callback_data='maketest')
exit_a_panel=types.InlineKeyboardButton(text='Admin Paneldan Chiqish 🔙',callback_data='epanel')
admin_markup=types.InlineKeyboardMarkup(row_width=1).add(a_req,make_test,exit_a_panel)
quest=''
opta=''
optb=''
optc=''
optd=''
tests_len=0
ftests_len_phy=0
fq=''
fa=''
fb=''
fc=''
fd=''
@dp.message_handler()
async def Apanel(message:types.Message):
    global admin_markup
    global quest
    global opta
    global optb
    global optc
    global optd
    global close
    global tests_len
    global ftests_len_phy
    global fq
    global fa
    global fb
    global fc
    global fd
    text=message.text
    if message.text=='Admin123':
        await message.answer(
            "Well Come To Admin Panel",
            reply_markup=admin_markup

        )
    if text[:2]=='fs':
        if text[2:]!='':
            fq=text[2:]
            await message.answer(
                'A variyatni qoshishishingiz kereak ❗️\n'
                " ' fa ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                "Menga tesni savolini ' fs ' sozidan song yozib jonating \n\n"
                "❌ Agar savolingiz fs so'zidan so'ng yozilmagan bolsa qabul qilinmaydi❗️❗️"
            )
    if text[:2] == 'fa':
        if text[2:] != '':
            fa = text[2:]
            await message.answer(
                'B variyatni qoshishishingiz kereak ❗️\n'
                " ' fb ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                'A variyatni qoshishishingiz kereak ❗️\n'
                " ' fa ' sozidan so'ng variyantni javobini yuboring"
            )

    if text[:2] == 'fb':
        if text[2:] != '':
            fb = text[2:]
            await message.answer(
                'C variyatni qoshishishingiz kereak ❗️\n'
                " ' fc ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                'B variyatni qoshishishingiz kereak ❗️\n'
                " ' fb ' sozidan so'ng variyantni javobini yuboring"
            )
    if text[:2] == 'fc':
        if text[2:] != '':
            fc = text[2:]
            await message.answer(
                'D variyatni qoshishishingiz kereak ❗️\n'
                " ' fd ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                'C variyatni qoshishishingiz kereak ❗️\n'
                " ' fc ' sozidan so'ng variyantni javobini yuboring"
            )
    if text[:2] == 'fd':
        if text[2:] != '':
            fd = text[2:]

            fta = types.InlineKeyboardButton(text='A✅', callback_data='fatrue')
            ftb = types.InlineKeyboardButton(text='B✅', callback_data='fbtrue')
            ftc = types.InlineKeyboardButton(text='C✅', callback_data='fctrue')
            ftd = types.InlineKeyboardButton(text='D✅', callback_data='fdtrue')
            ftru_option_rp_kb_phy = types.InlineKeyboardMarkup().add(fta, ftb, ftc, ftd)
            ftests_len_phy = len(list(db.child('tests').child('fizika').get().val().keys())) + 1
            db.child('tests').child('fizika').child('t' + str(ftests_len_phy)).child('a').set({'option': fa, 'trust': 'false'})
            db.child('tests').child('fizika').child('t' + str(ftests_len_phy)).child('b').set({'option': fb, 'trust': 'false'})
            db.child('tests').child('fizika').child('t' + str(ftests_len_phy)).child('c').set({'option': fc, 'trust': 'false'})
            db.child('tests').child('fizika').child('t' + str(ftests_len_phy)).child('d').set({'option': fd, 'trust': 'false'})
            db.child('tests').child('fizika').child('t' + str(ftests_len_phy)).child('quest').set({'name': fq})
            await message.answer(
                f"Savol: {fq}\n"
                f"A: {fa}\n"
                f"B: {fb}\n"
                f"C: {fc}\n"
                f"D: {fd}\n\n"
                f"Succesfully Added to base\n\n"
                f"To'g'ri variyantni tanlang : "
                , reply_markup=ftru_option_rp_kb_phy
            )

        else:
            await message.answer(
                'D variyatni qoshishishingiz kereak ❗️\n'
                " ' fd ' sozidan so'ng variyantni javobini yuboring"
            )




    # Math
    if text[:2] == 'ms':
        if text[2:]!='':
            quest=text[2:]
            await message.answer(
                'A variyatni qoshishishingiz kereak ❗️\n'
                " ' ma ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                "Menga tesni savolini ' ms ' sozidan song yozib jonating \n\n"
                "❌ Agar savolingiz ms so'zidan so'ng yozilmagan bolsa qabul qilinmaydi❗️❗️"
            )
    if text[:2]=='ma':
        if text[2:]!='':
            opta=text[2:]
            await message.answer(
                'B variyatni qoshishishingiz kereak ❗️\n'
                " ' mb ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                'A variyatni qoshishishingiz kereak ❗️\n'
                " ' ma ' sozidan so'ng variyantni javobini yuboring"
            )

    if text[:2]=='mb':
        if text[2:]!='':
            optb=text[2:]
            await message.answer(
                'C variyatni qoshishishingiz kereak ❗️\n'
                " ' mc ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                'B variyatni qoshishishingiz kereak ❗️\n'
                " ' mb ' sozidan so'ng variyantni javobini yuboring"
            )
    if text[:2]=='mc':
        if text[2:]!='':
            optc=text[2:]
            await message.answer(
                'D variyatni qoshishishingiz kereak ❗️\n'
                " ' md ' sozidan so'ng variyantni javobini yuboring"
            )
        else:
            await message.answer(
                'C variyatni qoshishishingiz kereak ❗️\n'
                " ' mc ' sozidan so'ng variyantni javobini yuboring"
            )
    if text[:2]=='md':
        if text[2:]!='':
            optd=text[2:]

            ta=types.InlineKeyboardButton(text='A✅',callback_data='matrue')
            tb=types.InlineKeyboardButton(text='B✅',callback_data='mbtrue')
            tc=types.InlineKeyboardButton(text='C✅',callback_data='mctrue')
            td=types.InlineKeyboardButton(text='D✅',callback_data='mdtrue')
            tru_option_rp_kb=types.InlineKeyboardMarkup().add(ta,tb,tc,td)
            tests_len = len(list(db.child('tests').child('matematika').get().val().keys()))+1
            db.child('tests').child('matematika').child('t'+str(tests_len)).child('a').set({'option':opta,'trust':'false'})
            db.child('tests').child('matematika').child('t'+str(tests_len)).child('b').set({'option':optb,'trust':'false'})
            db.child('tests').child('matematika').child('t'+str(tests_len)).child('c').set({'option':optc,'trust':'false'})
            db.child('tests').child('matematika').child('t'+str(tests_len)).child('d').set({'option':optd,'trust':'false'})
            db.child('tests').child('matematika').child('t'+str(tests_len)).child('quest').set({'name':quest})
            await message.answer(
                f"Savol: {quest}\n"
                f"A: {opta}\n"
                f"B: {optb}\n"
                f"C: {optc}\n"
                f"D: {optd}\n\n"
                f"Succesfully Added to base\n\n"
                f"To'g'ri variyantni tanlang : "
            ,reply_markup=tru_option_rp_kb
            )

        else:
            await message.answer(
                'D variyatni qoshishishingiz kereak ❗️\n'
                " ' md ' sozidan so'ng variyantni javobini yuboring"
            )






# physics
@dp.callback_query_handler(text=["fatrue",'fbtrue','fctrue','fdtrue'])
async def true_option_math(call:types.CallbackQuery):
    global make_test_fiz
    global ftests_len_phy
    if call.data=='fatrue':
        all_tests_phy = list(db.child("tests").child('fizika').get().val().keys())
        db.child('tests').child('fizika').child('t'+str(ftests_len_phy)).child('a').update({'trust':'true'})
        await call.message.edit_text(
            f"A variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nFizika: \nJami Testlar : {len(all_tests_phy)}",reply_markup=make_test_fiz

        )
    if call.data=='fbtrue':
        all_tests_phy = list(db.child("tests").child('fizika').get().val().keys())

        db.child('tests').child('fizika').child('t'+str(ftests_len_phy)).child('b').update({'trust':'true'})
        await call.message.edit_text(
            f"B variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nFizika: \nJami Testlar : {len(all_tests_phy)}", reply_markup=make_test_fiz

        )

    if call.data=='fctrue':
        all_tests_phy = list(db.child("tests").child('fizika').get().val().keys())

        db.child('tests').child('fizika').child('t'+str(ftests_len_phy)).child('c').update({'trust':'true'})
        await call.message.edit_text(
            f"C variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nFizika: \nJami Testlar : {len(all_tests_phy)}", reply_markup=make_test_fiz

        )

    if call.data=='fdtrue':
        all_tests_phy = list(db.child("tests").child('fizika').get().val().keys())

        db.child('tests').child('fizika').child('t'+str(ftests_len_phy)).child('d').update({'trust':'true'})
        await call.message.edit_text(
            f"D variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nFizika: \nJami Testlar : {len(all_tests_phy)}", reply_markup=make_test_fiz

        )






# Math
@dp.callback_query_handler(text=["matrue",'mbtrue','mctrue','mdtrue'])
async def true_option_math(call:types.CallbackQuery):
    global make_test_math
    global tests_len
    if call.data=='matrue':
        all_tests_math = list(db.child("tests").child('matematika').get().val().keys())

        db.child('tests').child('matematika').child('t'+str(tests_len)).child('a').update({'trust':'true'})
        await call.message.edit_text(
            f"A variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nMatematika: \nJami Testlar : {len(all_tests_math)}",reply_markup=make_test_math

        )
    if call.data=='mbtrue':
        all_tests_math = list(db.child("tests").child('matematika').get().val().keys())

        db.child('tests').child('matematika').child('t'+str(tests_len)).child('b').update({'trust':'true'})
        await call.message.edit_text(
            f"B variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nMatematika: \nJami Testlar : {len(all_tests_math)}", reply_markup=make_test_math

        )

    if call.data=='mctrue':
        all_tests_math = list(db.child("tests").child('matematika').get().val().keys())

        db.child('tests').child('matematika').child('t'+str(tests_len)).child('c').update({'trust':'true'})
        await call.message.edit_text(
            f"C variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nMatematika: \nJami Testlar : {len(all_tests_math)}", reply_markup=make_test_math

        )

    if call.data=='mdtrue':
        all_tests_math = list(db.child("tests").child('matematika').get().val().keys())

        db.child('tests').child('matematika').child('t'+str(tests_len)).child('d').update({'trust':'true'})
        await call.message.edit_text(
            f"D variyant To'g'ri ✅\n Test Bazaga Qo'shildi ! \nMatematika: \nJami Testlar : {len(all_tests_math)}", reply_markup=make_test_math

        )




close = types.InlineKeyboardButton(text="◀️ Back", callback_data='bc')

math=types.InlineKeyboardButton(text='Matematika',callback_data='math_selected')
fiz = types.InlineKeyboardButton(text='Fizika', callback_data='fiz_selected')
close_admin_panel=types.InlineKeyboardButton(text='Back',callback_data='back_aPanel')
cat_rp_markup=types.InlineKeyboardMarkup(row_width=2).add(math,fiz,close_admin_panel)
a_len=0
@dp.callback_query_handler(text=['reqs','maketest','epanel','back_aPanel'])
async def adminPanelFuncs(call:types.CallbackQuery):
    global req_array
    global close
    global cat_rp_markup
    len_reqs = len(db.child('Users').get().val().keys())
    if call.data=='reqs':
        users = ''
        rp_markup=types.InlineKeyboardMarkup(row_width=3)
        a_len=0;
        for i in range(2,len_reqs+1):
            name=db.child("Users").child('u'+str(i)).child('name').get().val()
            id=db.child("Users").child('u'+str(i)).child('id').get().val()
            num=db.child('Users').child('u'+str(i)).child('num').get().val()
            users+=f'{num}. Name: {name} id: {id}\n\n'
            rp_markup.add(types.InlineKeyboardButton(text=str(num),callback_data=f'u{num}'))
            a_len+=1
        rp_markup.add(close)
        await call.message.edit_text(
            "Rexsat Soraganlar:\n\n"
            f"Jami: {a_len} ta\n\n"
           f"{users}",
            reply_markup=rp_markup
        )
    if call.data=='maketest':
        await call.message.edit_text(
            "Qaysi fan uchun test tuzmoqchisiz ? : ",
            reply_markup=cat_rp_markup
        )
    if call.data=="epanel":
        await call.message.edit_text(
            "Assalomu alaykum ustoz agar siz Boshlang'ich sinf ustozi bo'lsangiz biz bilan bilimingizni oshirishingiz mumkin biz sizga professional testlarni taqdim etamiz, bot sizda ishlashligi  uchun  @admin_name ga murojaat eting!\n\n"
            f"Sizning ID: {call.message.from_user.id}\n\n"
            'Tel: 👇👇 \n'
            '+998 91 121 23 99',
            reply_markup=start_test_markup
        )
    if call.data=='back_aPanel':
        await call.message.edit_text(
            "You Returned Admin Menu: ",
            reply_markup=admin_markup

        )


@dp.callback_query_handler(text=['bc'])
async def edit(call:types.CallbackQuery):
    global a_len
    global admin_markup
    if call.data=='bc':
        await call.message.edit_text(
            "Well Come To Admin Panel",
            reply_markup=admin_markup
        )


make_test_math=types.InlineKeyboardMarkup()
make_test_fiz = types.InlineKeyboardMarkup()
@dp.callback_query_handler(text=['math_selected','fiz_selected'])
async def subselect(call:types.CallbackQuery):
    global close
    global make_test_math
    global make_test_fiz
    if call.data=='math_selected':
        make_test_math=types.InlineKeyboardMarkup()
        new_test_math=types.InlineKeyboardButton(text='Yangi Test Qoshish➕',callback_data='maketestmath')
        make_test_math.add(new_test_math,close)
        all_tests_math=list(db.child("tests").child('matematika').get().val().keys())
        await call.message.edit_text(
            f"Matematika:\n\n"
            f"Jami Testlar : {len(all_tests_math)}",
            reply_markup=make_test_math
        )
    if call.data == 'fiz_selected':
        make_test_fiz=types.InlineKeyboardMarkup()
        new_test_fiz= types.InlineKeyboardButton(text='Yangi Test Qoshish➕', callback_data='maketestfiz')
        make_test_fiz.add(new_test_fiz,close)
        all_tests_fiz= list(db.child("tests").child('fizika').get().val().keys())
        await call.message.edit_text(
            f"Fizika:\n\n"
            f"Jami Testlar : {len(all_tests_fiz)}",
            reply_markup=make_test_fiz
        )




@dp.callback_query_handler(text=['maketestmath','maketestfiz'])
async def mathorphy(call:types.CallbackQuery):
    if call.data=='maketestmath':
        await call.message.edit_text(
            "Menga tesni savolini ' ms ' sozidan song yozib jonating \n\n"
            "❌ Agar savolingiz ms so'zidan so'ng yozilmagan bolsa qabul qilinmaydi❗️❗️"
        )
    if call.data=='maketestfiz':
        await call.message.edit_text(
            "Menga tesni savolini ' fs ' sozidan song yozib jonating \n\n"
            "❌ Agar savolingiz fs so'zidan so'ng yozilmagan bolsa qabul qilinmaydi❗️❗️"
        )


trust=types.InlineKeyboardButton(text='Ruxsat Berish ✅',callback_data='trust')
stop_user=types.InlineKeyboardButton(text='Taqiqlash 🛑',callback_data='stop')
rmv=types.InlineKeyboardButton(text="O'chirib yuborish ❌",callback_data='rmv')
reply_edit_user=types.InlineKeyboardMarkup(row_width=2).add(trust,stop_user,rmv,close)

user=''
@dp.callback_query_handler()
async def handlers(call:types.CallbackQuery):
    global user
    global admin_markup
    if call.data[:1]=='u' and int(call.data[1:]) > 0 :
        name=db.child("Users").child(str(call.data)).child('name').get().val()
        id=db.child("Users").child(str(call.data)).child('id').get().val()
        num=db.child("Users").child(str(call.data)).child('num').get().val()
        acs=db.child("Users").child(str(call.data)).child('access').get().val()
        user=call.data
        await call.message.edit_text(
            f"{num}\n"
            f"Name: {name}\n\n"
            f"id : {id}\n\n"
            f"access : {acs}\n"
            ,reply_markup=reply_edit_user
        )

    if call.data=='trust':
        db.child("Users").child(user).update({'access':'true'})
        uname = db.child("Users").child(str(user)).child('name').get().val()
        uid = db.child("Users").child(str(user)).child('id').get().val()
        unum = db.child("Users").child(str(user)).child('num').get().val()
        uacs = db.child("Users").child(str(user)).child('access').get().val()
        await call.message.edit_text(
                    f"{unum}\n"
                    f"Name: {uname}\n\n"
                    f"id : {uid}\n\n"
                    f"access : {uacs}\n"
                    ,reply_markup=reply_edit_user
                )
    if call.data == 'stop':
        db.child("Users").child(user).update({'access': 'false'})
        suname = db.child("Users").child(str(user)).child('name').get().val()
        suid = db.child("Users").child(str(user)).child('id').get().val()
        sunum = db.child("Users").child(str(user)).child('num').get().val()
        suacs = db.child("Users").child(str(user)).child('access').get().val()
        await call.message.edit_text(
            f"{sunum}\n"
            f"Name: {suname}\n\n"
            f"id : {suid}\n\n"
            f"access : {suacs}\n"
            , reply_markup=reply_edit_user
        )
    if call.data=='rmv':
        db.child("Users").child(user).remove()
        await call.message.edit_text("Muvofiqatli O'cirib Tashlandi\n\nAsosiy Menu: ",reply_markup=admin_markup)






















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)