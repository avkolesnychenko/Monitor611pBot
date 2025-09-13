
import telebot
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime, timedelta

TOKEN = "7197275852:AAHj6uZ64idQ3GA3q5FLStsw5o3Y6q_nIJA"
CHAT_ID = -4825230345

bot = telebot.TeleBot(TOKEN)
scheduler = BackgroundScheduler()

schedule = {
    0: {
        "odd": [
            {"time": "08:00", "subject": "Основи програмування, лекція", "teacher": "Євгенія Віталіївна Соколова"},
            {"time": "09:50", "subject": "Основи програмування, лаб. практикум", "teacher": "Євгенія Віталіївна Соколова / Оксана Вадимівна Лучшева"},
            {"time": "11:55", "subject": "Іноземна мова, практика", "teacher": "Ірина Анатоліївна Томаз / Олена Леонідівна Новицька"},
            {"time": "13:45", "subject": "Основи права, лекція", "teacher": "Артем Євгенович Голубов"},
        ],
        "even": [
            {"time": "08:00", "subject": "Основи програмування, лекція", "teacher": "Євгенія Віталіївна Соколова"},
            {"time": "09:50", "subject": "Основи програмування, лаб. практикум", "teacher": "Євгенія Віталіївна Соколова / Оксана Вадимівна Лучшева"},
            {"time": "11:55", "subject": "Вища математика, лекція", "teacher": "Ніна Валеріївна Савченко"},
            {"time": "13:45", "subject": "Основи права, лекція", "teacher": "Артем Євгенович Голубов"},
        ]
    },
    1: {
        "odd": [
            {"time": "09:50", "subject": "Комп'ютерна дискретна математика, лекція", "teacher": "Андрій Григорович Чухрай"},
            {"time": "11:55", "subject": "Українська мова за професійним спрямуванням, лекція", "teacher": "Олена Володимирівна Коновченко"},
            {"time": "11:55", "subject": "Основи права, практика", "teacher": "Артем Євгенович Голубов"},
            {"time": "13:45", "subject": "Фізичне виховання, практика", "teacher": "Дивіться в менторі"},
        ],
        "even": [
            {"time": "09:50", "subject": "Комп'ютерна дискретна математика, лекція", "teacher": "Андрій Григорович Чухрай"},
            {"time": "11:55", "subject": "Українська мова за професійним спрямуванням, лекція", "teacher": "Олена Володимирівна Коновченко"},
            {"time": "11:55", "subject": "Основи права, практика", "teacher": "Артем Євгенович Голубов"},
            {"time": "13:45", "subject": "Фізичне виховання, практика", "teacher": "Дивіться в менторі"},
        ]
    },
    2: {
        "odd": [
            {"time": "08:00", "subject": "Іноземна мова, практика", "teacher": "Ірина Анатоліївна Томаз / Олена Леонідівна Новицька"},
            {"time": "09:50", "subject": "Комп'ютерна дискретна математика, практика", "teacher": "Тетяна Григорівна Дегтярьова"},
            {"time": "11:55", "subject": "Основи програмування, лекція", "teacher": "Євгенія Віталіївна Соколова"},
            {"time": "11:55", "subject": "Українська мова за професійним спрямуванням, практика", "teacher": "Інна Юріївна Вялих"},
        ],
        "even": [
            {"time": "08:00", "subject": "Іноземна мова, практика", "teacher": "Ірина Анатоліївна Томаз / Олена Леонідівна Новицька"},
            {"time": "09:50", "subject": "Комп'ютерна дискретна математика, практика", "teacher": "Тетяна Григорівна Дегтярьова"},
            {"time": "11:55", "subject": "Основи програмування, лекція", "teacher": "Євгенія Віталіївна Соколова"},
            {"time": "11:55", "subject": "Українська мова за професійним спрямуванням, практика", "teacher": "Інна Юріївна Вялих"},
        ]
    },
    3: {
        "odd": [
            {"time": "08:00", "subject": "Основи програмування, практика", "teacher": "Оксана Вадимівна Лучшева"},
            {"time": "09:50", "subject": "Основи програмної інженерії, лекція", "teacher": "Ігор Борисович Туркін"},
            {"time": "11:55", "subject": "Основи програмної інженерії, практика", "teacher": "Людмила Василівна Мандрікова"},
            {"time": "13:45", "subject": "Фізичне виховання, практика", "teacher": "Дивіться в менторі"},
        ],
        "even": [{"time": "08:00", "subject": "Основи програмування, практика", "teacher": "Оксана Вадимівна Лучшева"},
            {"time": "09:50", "subject": "Основи програмної інженерії, лекція", "teacher": "Ігор Борисович Туркін"},
            {"time": "11:55", "subject": "Основи програмної інженерії, практика", "teacher": "Людмила Василівна Мандрікова"},
            {"time": "13:45", "subject": "Фізичне виховання, практика", "teacher": "Дивіться в менторі"},
        ]
    },
    5: {
        "odd": [
            {"time": "08:00", "subject": "Вища математика, лекція", "teacher": "Ніна Валеріївна Савченко"},
            {"time": "09:50", "subject": "Вища математика, практика", "teacher": "Наталія Володимирівна Драшпуль"},
        ],
        "even": [
            {"time": "08:00", "subject": "Вища математика, лекція", "teacher": "Ніна Валеріївна Савченко"},
            {"time": "09:50", "subject": "Вища математика, практика", "teacher": "Наталія Володимирівна Драшпуль"},
        ]
    }
}

def get_week_type():
    week_num = date.today().isocalendar()[1]
    return "odd" if week_num % 2 == 0 else "even"

keyboard = types.InlineKeyboardMarkup(row_width=1)
btn = types.InlineKeyboardButton("Mentor", url="https://mentor.khai.edu/")
keyboard.add(btn)

def send_message(subject, teacher, time):
    msg = f"📚 <em>{time}</em> <b>{subject}</b>\n"
    if teacher:
        msg += f"👩‍🏫 Викладач: <b>{teacher}</b>\n"
    msg += "\n⏰ Пара почнеться через 5 хвилин !"

    bot.send_message(CHAT_ID, msg, parse_mode="HTML", reply_markup=keyboard)


def schedule_lessons():
    scheduler.remove_all_jobs()  # очищаем старые задачи
    week_type = get_week_type()
    today = date.today().weekday()

    for day, lessons in schedule.items():
        for lesson in lessons.get(week_type, []):
            hour, minute = map(int, lesson["time"].split(":"))
            lesson_time = datetime(year=1, month=1, day=1, hour=hour, minute=minute)  # дата фиктивная
            notify_time = lesson_time - timedelta(minutes=5)
            scheduler.add_job(
                send_message,
                "cron",
                day_of_week=day,
                hour=notify_time.hour,
                minute=notify_time.minute,
                args=[lesson["subject"], lesson["teacher"], lesson["time"]]
            )

schedule_lessons()
scheduler.start()

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, f"✅ Бот запущен! Ваш chat_id: {message.chat.id}")



bot.polling(non_stop=True)