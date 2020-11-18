import smtplib
from colorama import Fore,Back,Style,init
init(convert=True)

print(Fore.LIGHTGREEN_EX+f"""
▒█░░░ ░▀░ █▀▄▀█ █▀▀ ░░ ▒█▀▀▄ ░▀░ █▀▀ ▀▀█▀▀ █▀▀█ ░▀░ █▀▀▄ █░░█ ▀▀█▀▀ ░▀░ █▀▀█ █▀▀▄ 
▒█░░░ ▀█▀ █░▀░█ █▀▀ ▀▀ ▒█░▒█ ▀█▀ ▀▀█ ░░█░░ █▄▄▀ ▀█▀ █▀▀▄ █░░█ ░░█░░ ▀█▀ █░░█ █░░█ 
▒█▄▄█ ▀▀▀ ▀░░░▀ ▀▀▀ ░░ ▒█▄▄▀ ▀▀▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀ ▀▀▀░ ░▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀"""+Style.RESET_ALL)
mail = input(Fore.LIGHTYELLOW_EX+f"\nС какой почты будет осуществлятся рассылка?\n1.Gmail\n2.Yandex\nВыбор(вводить цыфру): ")
if mail == "1":
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
elif mail == "2":
    smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
else:
    print(Fore.RED+f"Выбор не корректен :(\nПопробуйте еще раз!")
    exit(0)
smtpObj.starttls()
mal = input("Ваша почта: ")
pas = input("Пароль: ")
tem = input("тема,без темы - пустое поле: ")
text = input("Текст рассылки: ")
w = input("Имя файла БД: ")
wrd = open(w, 'r').readlines()
smtpObj.login(mal, pas)
print("Успешная авторизация")
for line in wrd:
    mail = line.strip()
    mail = mail.split(':')
    BODY = "\r\n".join((
        "From: %s" % mail,
        "To: %s" % mail,
        "Subject: %s" % tem ,
        "",
        text
    ))
    smtpObj.sendmail(mal, mail, BODY)
    print(Fore.LIGHTGREEN_EX+f"Собщение отправлено на - "+ mail)
print("Полетели лимоны")