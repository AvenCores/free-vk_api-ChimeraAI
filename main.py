import sys
import time
import vk_api
import openai
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from botapiconfig import vk_api_key, chimeraAI_api_key, openai_api_server

session = vk_api.VkApi(token=vk_api_key)
vk_upload = vk_api.VkUpload(session)
vk = session.get_api()
openai.api_key = chimeraAI_api_key
openai.api_base = openai_api_server

start_time = time.time()

keyboard = VkKeyboard(one_time=False, inline=False)
keyboard.add_button('F.A.Q', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Тех. поддержка', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Статус бота', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('ChimeraAI', color=VkKeyboardColor.POSITIVE)


def sendmessage(userid, message):
    session.method("messages.send",
                   {"user_id": userid, "message": message, "keyboard": keyboard.get_keyboard(), "random_id": 0})


def mainloader():
    for event in VkLongPoll(session).listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                text = event.text.lower()
                userid = event.user_id
                if text in ["начать", "привет", "hello", "start", "ку", "re"]:
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    firstmessage = """👋 Добро пожаловать в сообщество по тематике ChatGPT! 🎉 Мы рады видеть вас здесь. 🤗 Наша цель - предоставить жителям стран СНГ простой доступ к информации из ChatGPT.

    ⚠️ Внимание! ⚠️
    Пожалуйста, будьте осторожны при отправке сообщений в этом сообществе. Особенностью этого сообщества является то, что создатель сообщества может просматривать все сообщения, отправленные в нем. Пожалуйста, будьте внимательны и выскажитесь только теми словами и мыслями, которые вы готовы делиться публично. Спасибо за понимание.

    Как задать вопрос ChatGPT 3.5? ❓
    Легко! Просто напиши что хочешь спросить у нейросети и дожидайся ответа 😉

    Как задать вопрос ChatGPT 4.0? ❓
    Легко! Просто напиши /gpt4 "ТЕКСТ" и дожидайся ответа 😉

    Как получить картинку от DALLE-2? ❓
    Легко! Просто напиши /dalle2 ВАШ-ЗАПРОС 😉"""
                    vk.messages.edit(peer_id=event.user_id, message=firstmessage, message_id=(event.message_id + 1))
                    break

                if text == "f.a.q":
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    faq = """——— ⬇️ Ответы на вопросы по поводу данного бота ⬇️ ———
    ———
    Как задать вопрос в ChatGPT?

    Для того чтобы задать вопрос в ChatGPT, просто напишите свой вопрос в поле ввода и нажмите "Отправить" или "Enter". Затем дождитесь ответа от ChatGPT. Если ответ не пришел, можно обратиться в "Тех. поддержка" для получения помощи и объяснений.
    ———
    Какая модель используется в Боте?

    Для обучения данного бота используется модель gpt-3.5-turbo-16k и в тестовом режиме gpt-4. Эта модель обеспечивает более быстрый и точный ответ на вопросы пользователей.
    ———
    Умеет ли бот запоминать сообщения?

    Увы, на данный момент бот не умеет запоминать сообщения.
    ———

    ——— ⬇️ Определения названий технологий OpenAI⬇️ ———
    ———
    ChatGPT - это чат-бот с искусственным интеллектом, разработанный компанией OpenAI и способный работать в диалоговом режиме, поддерживающий запросы на естественных языках. ChatGPT — большая языковая модель, для тренировки которой использовались методы обучения с учителем и обучения с подкреплением.
    ———
    DALL-E 2 — это новый алгоритм нейронной сети, который создает картинку из предоставленной вами короткой фразы или предложения.
    ———
    Whisper - это модель распознавания речи общего назначения. Она обучена на большом наборе данных разнообразных аудиозаписей и является многозадачной моделью, которая может выполнять многоязычное распознавание речи, перевод речи и идентификацию языка.
    ———"""
                    vk.messages.edit(peer_id=event.user_id, message=faq, message_id=(event.message_id + 1))
                    break

                if text == "тех. поддержка":
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    texsupport = "Если у вас возникли какие-либо вопросы или проблемы c ботом, я всегда готов помочь вам в решении технических вопросов. Вы можете связаться со мной по следующим каналам коммуникации:\n\n💬 Я в VK: https://vk.com/avencores\n💬 Я в Telegram: https://t.me/avencores"
                    vk.messages.edit(peer_id=event.user_id, message=texsupport, message_id=(event.message_id + 1))
                    break

                if text == "статус бота":
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    pyver = sys.version.split()[0]
                    current_time = time.time()
                    uptime = int(current_time - start_time)
                    uptime_str = f"{uptime // (24 * 3600)} день(-ней), {uptime // 3600 % 24} час(-ов), {uptime // 60 % 60} минут(-а), {uptime % 60} секунд(-а)"
                    status = datetime.now().strftime(f"""Бот работает в штатном режиме. 🤖

    Время на сервере: %H:%M:%S ⏰
    Дата на сервере: %d.%m.%y 📅

    Платформа на сервере: {sys.platform} 💻
    Версия Python на сервере: {pyver} 🐍
    Аптайм бота: {uptime_str} ⌛""")
                    vk.messages.edit(peer_id=event.user_id, message=status, message_id=(event.message_id + 1))
                    break

                if text == "chimeraai":
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    botapimessage = "Данный бот использует бесплатное api ChimeraAI: \n\nhttps://chimeragpt.adventblocks.cc/ru/intel"
                    vk.messages.edit(peer_id=event.user_id, message=botapimessage, message_id=(event.message_id + 1))
                    break

                if text[:7] == "/dalle2":
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    try:
                        dalletext = event.text[7:]
                        response = openai.Image.create(
                            prompt=dalletext,
                            n=10,
                            size="1024x1024"
                        )
                        output = response['data'][0]['url']
                        vk.messages.edit(peer_id=event.user_id, message=output, message_id=(event.message_id + 1))

                    except Exception as e:
                        errormessage = f"❌ Ошибка API: {e}"
                        vk.messages.edit(peer_id=event.user_id, message=errormessage, message_id=(event.message_id + 1))
                    break

                if text[:5] == "/gpt4":
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    try:
                        response = openai.ChatCompletion.create(
                            model='gpt-4',
                            messages=[
                                {'role': 'user', 'content': text[5:]},
                            ],
                            allow_fallback=True
                        )
                        output = response["choices"][0]["message"]["content"]
                        vk.messages.edit(peer_id=event.user_id, message=output, message_id=(event.message_id + 1))

                    except Exception as e:
                        errormessage = f"❌ Ошибка API: {e}"
                        vk.messages.edit(peer_id=event.user_id, message=errormessage, message_id=(event.message_id + 1))
                    break

                else:
                    load = "🔎 Идет загрузка, подождите..."
                    sendmessage(userid, load)
                    try:
                        response = openai.ChatCompletion.create(
                            model='gpt-3.5-turbo-16k',
                            messages=[
                                {'role': 'user', 'content': text},
                            ],
                            allow_fallback=True
                        )
                        output = response["choices"][0]["message"]["content"]
                        vk.messages.edit(peer_id=event.user_id, message=output, message_id=(event.message_id + 1))

                    except Exception as e:
                        errormessage = f"❌ Ошибка API: {e}"
                        vk.messages.edit(peer_id=event.user_id, message=errormessage, message_id=(event.message_id + 1))


while True:
    try:
        mainloader()
    except Exception:
        pass