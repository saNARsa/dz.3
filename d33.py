def send_email(message, recipient, sender="university.help@gmail.com"):
    if '@' in recipient:
        pass
    else:
        print("Невозможно отправить письмо с адреса", sender , 'на адрес' , recipient)
        return


    if recipient[-4 : ] == '.com' or recipient[-4 : ] == '.ner' or recipient[-3 : ] == '.ru':
        pass
    else:
        print("Невозможно отправить письмо с адреса", sender , 'на адрес' , recipient)
        return



    if sender[-4 :] == '.com' or sender[-4 : ] == '.ner' or sender[-3 : ] == '.ru':
        pass
    else:
        print("Невозможно отправить письмо с адреса", sender , 'на адрес' , recipient)
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender , "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса" , sender , "на адрес" ,recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
