define lizanka = Character("lizanka_var", color="#FFB300", dynamic=True)
define sofija = Character("sofija_var", color="#803E75", dynamic=True)
define famusov = Character("famusov_var", color="#FF6800", dynamic=True)
define molchalin = Character("molchalin_var", color="#A6BDD7", dynamic=True)
define sluga_1_6 = Character("sluga_1_6_var", color="#C10020", dynamic=True)
define chatskij = Character("chatskij_var", color="#CEA262", dynamic=True)
define sluga_2_3 = Character("sluga_2_3_var", color="#817066", dynamic=True)
define skalozub = Character("skalozub_var", color="#007D34", dynamic=True)
define glavnij_sluga = Character("glavnij_sluga_var", color="#F6768E", dynamic=True)
define natalja_dmitrievna = Character("natalja_dmitrievna_var", color="#00538A", dynamic=True)
define platon_mihajlovich = Character("platon_mihajlovich_var", color="#FF7A5C", dynamic=True)
define pervaja_knjazhna = Character("pervaja_knjazhna_var", color="#53377A", dynamic=True)
define vtoraja_knjazhna = Character("vtoraja_knjazhna_var", color="#FF8E00", dynamic=True)
define tretja_knjazhna = Character("tretja_knjazhna_var", color="#B32851", dynamic=True)
define chetviortaja_knjazhna = Character("chetviortaja_knjazhna_var", color="#F4C800", dynamic=True)
define pjataja_knjazhna = Character("pjataja_knjazhna_var", color="#7F180D", dynamic=True)
define shestaja_knjazhna = Character("shestaja_knjazhna_var", color="#93AA00", dynamic=True)
define knjaginja = Character("knjaginja_var", color="#593315", dynamic=True)
define knjaz = Character("knjaz_var", color="#F13A13", dynamic=True)
define grafinja_vnuchka = Character("grafinja_vnuchka_var", color="#232C16", dynamic=True)
define zagoretskij = Character("zagoretskij_var", color="#182D83", dynamic=True)
define hlestova = Character("hlestova_var", color="#1CAA15", dynamic=True)
define gd = Character("gd_var", color="#4AA750", dynamic=True)
define gn = Character("gn_var", color="#D2C20A", dynamic=True)
define grafinja_babushka = Character("grafinja_babushka_var", color="#E31244", dynamic=True)
define lakej_4_1 = Character("lakej_4_1_var", color="#09DF8F", dynamic=True)
define lakej_4_2a = Character("lakej_4_2a_var", color="#19AF6A", dynamic=True)
define lakej_4_2b = Character("lakej_4_2b_var", color="#0CDFDB", dynamic=True)
define lakej_chatskogo = Character("lakej_chatskogo_var", color="#152F85", dynamic=True)
define repetilov = Character("repetilov_var", color="#AAC2EC", dynamic=True)
define lakej_4_4 = Character("lakej_4_4_var", color="#A062B0", dynamic=True)

label start:
    play music "audio/music/2.mp3" fadeout 1.0 fadein 1.0

    scene poster with fade

    "Горе от ума"

    "Комедия в четырех действиях, в стихах"

    menu:
        "{color=#000}Действующие:{/color}":
            jump Characters
        "{color=#000}Действие первое{/color}":
            jump Act_1
        "{color=#000}Действие второе{/color}":
            jump Act_2
        "{color=#000}Действие третье{/color}":
            jump Act_3
        "{color=#000}Действие четвертое{/color}":
            jump Act_4

label Characters:
    play music "audio/music/10.mp3" fadeout 1.0 fadein 1.0

    scene 1 with fade

    "{b}Действующие:{/b}"

    show famusov at truecenter
    "Павел Афанасьевич Фамусов, управляющий в казенном месте."
    hide famusov

    show sofija at truecenter
    "Софья Павловна, его дочь."
    hide sofija

    show lizanka at truecenter
    "Лизанька, служанка."
    hide lizanka

    show molchalin at truecenter
    "Алексей Степанович Молчалин, секретарь Фамусова, живущий у него в доме."
    hide molchalin

    show chatskij at truecenter
    "Александр Андреевич Чацкий."
    hide chatskij

    show skalozub at truecenter
    "Полковник Скалозуб, Сергей Сергеевич."
    hide skalozub

    "Горичи."

    show natalja_dmitrievna at truecenter
    "Наталья Дмитриевна, молодая дама"
    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter
    "Платон Михайлович, муж ее"
    hide platon_mihajlovich

    "Князь Тугоуховский и Княгиня, жена его, с шестью дочерями."

    show knjaz at truecenter
    "Князь"
    hide knjaz

    show knjaginja at truecenter
    "Княгиня"
    hide knjaginja

    show pervaja_knjazhna at truecenter
    "1-я княжна"
    hide pervaja_knjazhna

    show vtoraja_knjazhna at truecenter
    "2-я княжна"
    hide vtoraja_knjazhna

    show tretja_knjazhna at truecenter
    "3-я княжна"
    hide tretja_knjazhna

    show chetviortaja_knjazhna at truecenter
    "4-я княжна"
    hide chetviortaja_knjazhna

    show pjataja_knjazhna at truecenter
    "5-я княжна"
    hide pjataja_knjazhna

    show shestaja_knjazhna at truecenter
    "6-я княжна"
    hide shestaja_knjazhna

    "Хрюмины."

    show grafinja_babushka at truecenter
    "Графиня бабушка"
    hide grafinja_babushka

    show grafinja_vnuchka at truecenter
    "Графиня внучка"
    hide grafinja_vnuchka

    show zagoretskij at truecenter
    "Антон Антонович Загорецкий."
    hide zagoretskij

    show hlestova at truecenter
    "Старуха Хлёстова, свояченица Фамусова."
    hide hlestova

    show gn at truecenter
    "г. N*."
    hide gn

    show gd at truecenter
    "г. D*."
    hide gd

    show repetilov at truecenter
    "Репетилов."
    hide repetilov

    "Петрушка и несколько говорящих слуг."

    show glavnij_sluga at truecenter
    "Главный слуга"
    hide glavnij_sluga

    show sluga_2_3 at truecenter
    "Слуга (Петрушка)"
    hide sluga_2_3

    show sluga_1_6 at truecenter
    "Слуга"
    hide sluga_1_6

    "Множество гостей всякого разбора и их лакеев при разъезде."

    show lakej_chatskogo at truecenter
    "Лакей Чацкого"
    hide lakej_chatskogo

    show lakej_4_1 at truecenter
    "Лакей"
    hide lakej_4_1

    show lakej_4_2a at truecenter
    "Лакей"
    hide lakej_4_2a

    show lakej_4_2b at truecenter
    "Лакей"
    hide lakej_4_2b

    show lakej_4_4 at truecenter
    "Лакей"
    hide lakej_4_4

    "Официанты Фамусова."

    "Действие в Москве, в доме Фамусова."

label Act_1:
    play music "audio/music/9.mp3" fadeout 1.0 fadein 1.0

    scene 3 with fade

    "{b}Действие первое{/b}"

    menu:
        "{color=#000}Явление 1{/color}":
            jump Act_1_Scene_1
        "{color=#000}Явление 2{/color}":
            jump Act_1_Scene_2
        "{color=#000}Явление 3{/color}":
            jump Act_1_Scene_3
        "{color=#000}Явление 4{/color}":
            jump Act_1_Scene_4
        "{color=#000}Явление 5{/color}":
            jump Act_1_Scene_5
        "{color=#000}Явление 6{/color}":
            jump Act_1_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_1_Scene_6_1

label Further_Act_1_Scene_6_1:
    menu:
        "{color=#000}Явление 7{/color}":
            jump Act_1_Scene_7
        "{color=#000}Явление 8{/color}":
            jump Act_1_Scene_8
        "{color=#000}Явление 9{/color}":
            jump Act_1_Scene_9
        "{color=#000}Явление 10{/color}":
            jump Act_1_Scene_10

label Act_1_Scene_1:
    "{b}Явление 1{/b}"

    play sound1 piano
    play sound2 flute
    play sound3 door_creak

    show sofija at left
    show lizanka at right

    "<{i}Гостиная, в ней большие часы, справа дверь в спальню Софии, откудова слышно
            фортопияно с флейтою, которые потом умолкают. Лизанька среди комнаты спит, свесившись с
            кресел. Утро, чуть день брезжится.{/i}>"

    hide sofija
    hide lizanka

    stop sound1
    stop sound2
    stop sound3

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лизанька"

    lizanka "<{i}(вдруг просыпается, встает с кресел, оглядывается){/i}>"

    lizanka "Светает!.. Ах! как скоро ночь минула!"

    lizanka "Вчера просилась спать — отказ."

    lizanka "«Ждем друга». — Нужен глаз да глаз,"

    lizanka "Не спи, покудова не скатишься со стула."

    lizanka "Теперь вот только что вздремнула,"

    lizanka "Уж день!.. сказать им..."

    play sound1 knocking

    hide lizanka

    show lizanka at left
    show sofija at right

    lizanka "<{i}(Стучится к Софии.){/i}>"

    hide sofija

    show lizanka at truecenter

    stop sound1

    lizanka "{space=400}Господа,"

    lizanka "Эй! Софья Павловна, беда."

    lizanka "Зашла беседа ваша за́ ночь."

    lizanka "Вы глухи? — Алексей Степаныч!"

    lizanka "Сударыня!... — И страх их не берет!"

    play sound1 footsteps
    play sound2 door_creak

    lizanka "<{i}(Отходит от дверей.){/i}>"

    stop sound1
    stop sound2

    lizanka "Ну, гость неприглашенный,"

    lizanka "Быть может, батюшка войдет!"

    lizanka "Прошу служить у барышни влюбленной!"

    play sound1 footsteps
    play sound2 door_creak

    lizanka "<{i}(Опять к дверям.){/i}>"

    stop sound1
    stop sound2

    lizanka "Да расходитесь. Утро. — Что-с?"

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}Голос Софии"

    sofija "Который час?"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лизанька"

    lizanka "{space=400}Все в доме поднялось."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(из своей комнаты){/i}>"

    sofija "Который час?"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лизанька"

    lizanka "{space=400}Седьмой, осьмой, девятый."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(оттуда же){/i}>"

    sofija "Неправда."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лизанька"

    play sound1 footsteps
    play sound2 door_creak

    lizanka "<{i}(прочь от дверей){/i}>"

    stop sound1
    stop sound2

    lizanka "{space=400}Ах! амур проклятый!"

    lizanka "И слышат, не хотят понять,"

    lizanka "Ну что бы ставни им отнять?"

    lizanka "Переведу часы, хоть знаю: будет гонка,"

    lizanka "Заставлю их играть."

    play sound1 clock

    lizanka "<{i}(Лезет на стул, передвигает стрелку, часы бьют и играют.){/i}>"

    stop sound1

    hide lizanka

label Act_1_Scene_2:
    "{b}Явление 2{/b}"

    show lizanka at left
    show famusov at right

    "<{i}Лиза и Фамусов.{/i}>"

    hide lizanka
    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=200}Ах! барин!"

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Барин, да."

    play sound1 clock

    famusov "<{i}(Останавливает часовую музыку.){/i}>"

    stop sound1

    famusov "Ведь экая шалунья ты девчонка."

    famusov "Не мог придумать я, что это за беда!"

    famusov "То флейта слышится, то будто фортопьяно;"

    famusov "Для Софьи слишком было б рано?.."

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Нет, сударь, я... лишь невзначай..."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Вот то-то невзначай, за вами примечай;"

    famusov "Так верно с умыслом."

    hide famusov

    show famusov at left
    show lizanka at right

    famusov "<{i}(Жмется к ней и заигрывает){/i}>"

    hide lizanka

    show famusov at truecenter

    famusov "{space=400}Ох! зелье, баловница."

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Вы баловник, к лицу ль вам эти лица!"

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Скромна, а ничего кроме"

    famusov "Проказ и ветру на уме."

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Пустите, ветренники сами,"

    lizanka "Опомнитесь, вы старики..."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Почти."

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Ну кто придет, куда мы с вами?"

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Кому сюда прийти?"

    famusov "Ведь Софья спит?"

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Сейчас започивала."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Сейчас! А ночь?"

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Ночь целую читала."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Вишь, прихоти какие завелись!"

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Все по-французски, вслух, читает запершись."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Скажи-ка, что глаза ей портить не годится,"

    famusov "И в чтеньи прок-та не велик:"

    famusov "Ей сна нет от французских книг,"

    famusov "А мне от русских больно спится."

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Что встанет, доложусь,"

    lizanka "Извольте же идти; разбудите, боюсь."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Чего будить? Сама часы заводишь,"

    famusov "На весь квартал симфонию гремишь."

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "<{i}(как можно громче){/i}>"

    lizanka "Да полноте-с!"

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    play sound1 female_gag

    hide famusov

    show famusov at left
    show lizanka at right

    famusov "<{i}(зажимает ей рот){/i}>"

    hide lizanka

    show famusov at truecenter

    stop sound1

    famusov "{space=400}Помилуй, как кричишь,"

    famusov "{space=400}С ума ты сходишь?"

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Боюсь, чтобы не вышло из того..."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Чего?"

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Пора, суда́рь, вам знать, вы не ребенок;"

    lizanka "У девушек сон утренний так тонок;"

    lizanka "Чуть дверью скрипнешь, чуть шепнешь:"

    lizanka "Всё слышат..."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Все ты лжешь."

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}Голос Софии"

    sofija "Эй, Лиза!"

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(торопливо){/i}>"

    famusov "{space=400}Тс!"

    play sound1 tiptoes

    famusov "<{i}(Крадется вон из комнаты на цыпочках.){/i}>"

    stop sound1

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "<{i}(одна){/i}>"

    lizanka "{space=400}Ушел!.. Ах! от господ подалей;"

    lizanka "У них беды себе на всякий час готовь,"

    lizanka "Минуй нас пуще всех печалей"

    lizanka "И барский гнев, и барская любовь."

    hide lizanka

label Act_1_Scene_3:
    "{b}Явление 3{/b}"

    show lizanka at left
    show sofija at truecenter
    show molchalin at right

    "<{i}Лиза, София со свечкою, за ней Молчалин.{/i}>"

    hide lizanka
    hide sofija
    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Что, Лиза, на тебя напало?"

    sofija "Шумишь..."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Конечно вам расстаться тяжело?"

    lizanka "До света запершись, и кажется все мало?"

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Ах, в самом деле рассвело!"

    play sound1 female_blow_candle

    sofija "<{i}(Тушит свечу.){/i}>"

    stop sound1

    sofija "И свет и грусть. Как быстры ночи!"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Тужите, знай, со стороны нет мочи,"

    lizanka "Сюда ваш батюшка зашел, я обмерла;"

    lizanka "Вертелась перед ним, не помню что врала;"

    lizanka "Ну что же стали вы? поклон, сударь, отвесьте."

    lizanka "Подите, сердце не на месте;"

    lizanka "Смотрите на часы, взгляните-ка в окно:"

    lizanka "Валит народ по улицам давно;"

    lizanka "А в доме стук, ходьба, метут и убирают."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Счастливые часов не наблюдают."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Не наблюдайте, ваша власть;"

    lizanka "А что в ответ за вас, конечно, мне попасть."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    hide sofija

    show sofija at left
    show molchalin at right

    sofija "<{i}(Молчалину){/i}>"

    hide molchalin

    show sofija at truecenter

    sofija "Идите; целый день еще потерпим скуку."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Бог с вами-с; прочь возьмите руку."

    play sound1 footsteps
    play sound2 punch
    play sound3 door_creak

    hide lizanka

    show lizanka at left
    show molchalin at truecenter
    show famusov at right

    lizanka "<{i}(Разводит их, Молчалин в дверях сталкивается с Фамусовым.){/i}>"

    hide molchalin
    hide famusov

    show lizanka at truecenter

    stop sound1
    stop sound2
    stop sound3

    hide lizanka

label Act_1_Scene_4:
    "{b}Явление 4{/b}"

    show lizanka at left
    show molchalin at truecenter
    show famusov at right

    "<{i}София, Лиза, Молчалин, Фамусов.{/i}>"

    hide sofija
    hide lizanka
    hide molchalin
    hide famusov

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Что за оказия! Молчалин, ты, брат?"

    hide famusov

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Я-с."

    hide molchalin

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Зачем же здесь? и в этот час?"

    famusov "И Софья!.. Здравствуй, Софья, что ты"

    famusov "Так рано поднялась! а? для какой заботы?"

    famusov "И как вас бог не в пору вместе свел?"

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Он только что теперь вошел."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Сейчас с прогулки."

    hide molchalin

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Друг, нельзя ли для прогулок"

    famusov "Подальше выбрать закоулок?"

    famusov "А ты, сударыня, чуть из постели прыг,"

    famusov "С мужчиной! с молодым! — Занятье для девицы!"

    famusov "Всю ночь читает небылицы,"

    famusov "И вот плоды от этих книг!"

    famusov "А все Кузнецкий мост, и вечные французы,"

    famusov "Оттуда моды к нам, и авторы, и музы:"

    famusov "Губители карманов и сердец!"

    famusov "Когда избавит нас творец"

    famusov "От шляпок их! чепцов! и шпилек! и булавок!"

    famusov "И книжных и бисквитных лавок!"

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Позвольте, батюшка, кружится голова;"

    sofija "Я от испуга дух перевожу едва;"

    sofija "Изволили вбежать вы так проворно,"

    sofija "Смешалась я."

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Благодарю покорно,"

    famusov "Я скоро к ним вбежал!"

    famusov "Я помешал! я испужал!"

    famusov "Я, Софья Павловна, расстроен сам, день целый"

    famusov "Нет отдыха, мечусь как словно угорелый."

    famusov "По должности, по службе хлопотня,"

    famusov "Тот пристает, другой, всем дело до меня!"

    famusov "Но ждал ли новых я хлопот? чтоб был обманут..."

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    play sound1 female_cry

    sofija "<{i}(сквозь слезы){/i}>"

    stop sound1

    sofija "Кем, батюшка?"

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Вот попрекать мне станут,"

    famusov "Что без толку всегда журю,"

    famusov "Не плачь, я дело говорю:"

    famusov "Уж об твоем ли не радели"

    famusov "Об воспитаньи! с колыбели!"

    famusov "Мать умерла: умел я принанять"

    famusov "В мадам Розье вторую мать."

    famusov "Старушку-золото в надзор к тебе приставил:"

    famusov "Умна была, нрав тихий, редких правил."

    famusov "Одно не к чести служит ей:"

    famusov "За лишних в год пятьсот рублей"

    famusov "Сманить себя другими допустила."

    famusov "Да не в мадаме сила."

    famusov "Не надобно иного образца,"

    famusov "Когда в глазах пример отца."

    famusov "Смотри ты на меня: не хвастаю сложеньем;"

    famusov "Однако бодр и свеж, и дожил до седин,"

    famusov "Свободен, вдов, себе я господин..."

    famusov "Монашеским известен поведеньем!.."

    hide famusov

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Осмелюсь я, суда́рь..."

    hide lizanka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Молчать!"

    famusov "Ужасный век! Не знаешь, что начать!"

    famusov "Все умудрились не по ле́там,"

    famusov "А пуще дочери, да сами добряки,"

    famusov "Дались нам эти языки!"

    famusov "Берем же побродяг, и в дом и по билетам,"

    famusov "Чтоб наших дочерей всему учить, всему —"

    famusov "И танцам! и пенью́! и нежностям! и вздохам!"

    famusov "Как будто в жены их готовим скоморохам."

    famusov "Ты, посетитель, что? ты здесь, сударь, к чему?"

    famusov "Безродного пригрел и ввел в мое семейство,"

    famusov "Дал чин асессора и взял в секретари;"

    famusov "В Москву переведен через мое содейство;"

    famusov "И будь не я, коптел бы ты в Твери."

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Я гнева вашего никак не растолкую."

    sofija "Он в доме здесь живет, великая напасть!"

    sofija "Шел в комнату, попал в другую."

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Попал или хотел попасть?"

    famusov "Да вместе вы зачем? Нельзя, чтобы случайно."

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Вот в чем, однако, случай весь:"

    sofija "Как давиче вы с Лизой были здесь,"

    sofija "Перепугал меня ваш голос чрезвычайно,"

    sofija "И бросилась сюда я со всех ног..."

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Пожалуй, на меня всю суматоху сложит."

    famusov "Не в пору голос мой наделал им тревог!"

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "По смутном сне безделица тревожит;"

    sofija "Сказать вам сон: поймете вы тогда."

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Что за история?"

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Вам рассказать?"

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Ну да."

    famusov "<{i}(Садится.){/i}>"

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Позвольте... видите ль... сначала"

    sofija "Цветистый луг; и я искала"

    sofija "{space=400}Траву"

    sofija "Какую-то, не вспомню наяву."

    sofija "Вдруг милый человек, один из тех, кого мы"

    sofija "Увидим — будто век знакомы,"

    sofija "Явился тут со мной; и вкрадчив, и умен,"

    sofija "Но робок... знаете, кто в бедности рожден..."

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Ах, матушка, не довершай удара!"

    famusov "Кто беден, тот тебе не пара!"

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Потом пропало все: луга и небеса. —"

    sofija "Мы в темной комнате. Для довершенья чуда"

    sofija "Раскрылся пол — и вы оттуда"

    sofija "Бледны, как смерть, и дыбом волоса!"

    sofija "Тут с громом распахнулись двери"

    sofija "Какие-то не люди и не звери"

    sofija "Нас врознь — и мучили сидевшего со мной."

    sofija "Он будто мне дороже всех сокровищ,"

    sofija "Хочу к нему — вы тащите с собой:"

    sofija "Нас провожают стон, рев, хохот, свист чудовищ!"

    sofija "Он вслед кричит!.. —"

    sofija "Проснулась. — Кто-то говорит:"

    sofija "Ваш голос был; что, думаю, так рано?"

    sofija "Бегу сюда — и вас обоих нахожу."

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Да, дурен сон; как погляжу,"

    famusov "Тут всё есть, коли нет обмана:"

    famusov "И черти и любовь, и страхи и цветы."

    famusov "Ну, сударь мой, а ты?"

    hide famusov

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Я слышал голос ваш."

    hide molchalin

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Забавно."

    famusov "Дался им голос мой, и как себе исправно"

    famusov "Всем слышится, и всех сзывает до зари!"

    famusov "На голос мой спешил, за чем же? — говори."

    hide famusov

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}С бумагами-с."

    hide molchalin

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Да! их недоставало."

    famusov "Помилуйте, что это вдруг припало"

    famusov "Усердье к письменным делам!"

    famusov "<{i}(Встает.){/i}>"

    famusov "Ну, Сонюшка, тебе покой я дам:"

    famusov "Бывают странны сны, а наяву страннее;"

    famusov "Искала ты себе травы,"

    famusov "На друга набрела скорее;"

    famusov "Повыкинь вздор из головы;"

    famusov "Где чудеса, там мало складу. —"

    famusov "Поди-ка, ляг, усни опять."

    hide famusov

    show famusov at left
    show molchalin at right

    famusov "<{i}(Молчалину){/i}>"

    hide molchalin

    show famusov at truecenter

    famusov "Идем бумаги разбирать."

    hide famusov

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Я только нес их для докладу,"

    molchalin "Что в ход нельзя пустить без справок, без иных,"

    molchalin "Противуречья есть, и многое не дельно."

    hide molchalin

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Боюсь, суда́рь, я одного смертельно,"

    famusov "Чтоб множество не накоплялось их;"

    famusov "Дай волю вам, оно бы и засело;"

    famusov "А у меня, что дело, что не дело,"

    famusov "{space=400}Обычай мой такой:"

    famusov "Подписано, так с плеч долой."

    play sound1 footsteps
    play sound2 door_creak

    hide famusov

    show famusov at left
    show molchalin at right

    famusov "<{i}(Уходит с Молчалиным, в дверях пропускает его вперед.){/i}>"

    hide molchalin

    show famusov at truecenter

    stop sound1
    stop sound2

    hide famusov

label Act_1_Scene_5:
    "{b}Явление 5{/b}"

    show sofija at left
    show lizanka at right

    "<{i}София, Лиза.{/i}>"

    hide sofija
    hide lizanka

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Ну вот у праздника! ну вот вам и потеха!"

    lizanka "Однако нет, теперь уж не до смеха;"

    lizanka "В глазах темно, и замерла душа;"

    lizanka "Грех не беда, молва не хороша."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Что мне молва? Кто хочет, так и судит,"

    sofija "Да батюшка задуматься принудит:"

    sofija "Брюзглив, неугомонен, скор,"

    sofija "Таков всегда, а с этих пор..."

    sofija "Ты можешь посудить..."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Сужу-с не по рассказам;"

    lizanka "Запрет он вас; — добро еще со мной;"

    lizanka "А то, помилуй бог, как разом"

    lizanka "Меня, Молчалина и всех с двора долой."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Подумаешь, как счастье своенравно!"

    sofija "Бывает хуже, с рук сойдет;"

    sofija "Когда ж печальное ничто на ум нейдет;"

    sofija "Забылись музыкой, и время шло так плавно;"

    sofija "Судьба нас будто берегла;"

    sofija "Ни беспокойства, ни сомненья..."

    sofija "А горе ждет из-за угла."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Вот то-то-с, моего вы глупого сужденья"

    lizanka "Не жалуете никогда:"

    lizanka "{space=400}Ан вот беда."

    lizanka "На что вам лучшего пророка?"

    lizanka "Твердила я: в любви не будет в этой прока"

    lizanka "Ни во́ веки веков."

    lizanka "Как все московские, ваш батюшка таков:"

    lizanka "Желал бы зятя он с звездами, да с чинами,"

    lizanka "А при звездах не все богаты, между нами;"

    lizanka "Ну, разумеется, к тому б"

    lizanka "И деньги, чтоб пожить, чтоб мог давать он ба́лы;"

    lizanka "Вот, например, полковник Скалозуб:"

    lizanka "И золотой мешок, и метит в генералы."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Куда как мил! и весело мне страх"

    sofija "Выслушивать о фрунте и рядах;"

    sofija "Он слова умного не выговорил сроду, —"

    sofija "Мне все равно, что за него, что в воду."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Да-с, так сказать, речист, а больно не хитер;"

    lizanka "Но будь военный, будь он статский,"

    lizanka "Кто так чувствителен, и весел, и остер,"

    lizanka "Как Александр Андреич Чацкий!"

    lizanka "Не для того, чтоб вас смутить;"

    lizanka "Давно прошло, не воротить."

    lizanka "А помнится..."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Что помнится? Он славно"

    sofija "Пересмеять умеет всех;"

    sofija "Болтает, шутит, мне забавно;"

    sofija "Делить со всяким можно смех."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "И только? будто бы? — Слезами обливался,"

    lizanka "Я помню, бедный он, как с вами расставался."

    lizanka "— Что, сударь, плачете? живите-ка смеясь. —"

    lizanka "А он в ответ: «Недаром, Лиза, плачу,"

    lizanka "Кому известно, что́ найду я воротясь?"

    lizanka "И сколько, может быть, утрачу!»"

    lizanka "Бедняжка будто знал, что года через три..."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Послушай, вольности ты лишней не бери."

    sofija "Я очень ветрено, быть может, поступила,"

    sofija "И знаю, и винюсь; но где же изменила?"

    sofija "Кому? чтоб укорять неверностью могли."

    sofija "Да, с Чацким, правда, мы воспитаны, росли;"

    sofija "Привычка вместе быть день каждый неразлучно"

    sofija "Связала детскою нас дружбой; но потом"

    sofija "Он съехал, уж у нас ему казалось скучно,"

    sofija "И редко посещал наш дом;"

    sofija "Потом опять прикинулся влюбленным,"

    sofija "Взыскательным и огорченным!!."

    sofija "Остер, умен, красноречив,"

    sofija "В друзьях особенно счастлив."

    sofija "Вот об себе задумал он высоко..."

    sofija "Охота странствовать напала на него,"

    sofija "Ах! если любит кто кого,"

    sofija "Зачем ума искать, и ездить так далёко?"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Где носится? в каких краях?"

    lizanka "Лечился, говорят, на кислых он водах,"

    lizanka "Не от болезни, чай, от скуки, — повольнее."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "И, верно, счастлив там, где люди посмешнее."

    sofija "Кого люблю я, не таков:"

    sofija "Молчалин за других себя забыть готов,"

    sofija "Враг дерзости, — всегда застенчиво, несмело"

    sofija "Ночь целую с кем можно так провесть!"

    sofija "Сидим, а на дворе давно уж побелело,"

    sofija "Как думаешь? чем заняты?"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Бог весть!"

    lizanka "Сударыня, мое ли это дело?"

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Возьмет он руку, к сердцу жмет,"

    sofija "Из глубины души вздохнет,"

    sofija "Ни слова вольного, и так вся ночь проходит,"

    sofija "Рука с рукой, и глаз с меня не сводит. —"

    sofija "Смеешься! можно ли! чем повод подала"

    sofija "Тебе я к хохоту такому!"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Мне-с ваша тетушка на ум теперь пришла,"

    lizanka "Как молодой француз сбежал у ней из дому."

    lizanka "Голубушка! хотела схоронить"

    lizanka "Свою досаду, не сумела:"

    lizanka "Забыла волосы чернить,"

    lizanka "И через три дни поседела."

    play sound1 female_laughter

    lizanka "<{i}(Продолжает хохотать.){/i}>"

    stop sound1

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(с огорчением){/i}>"

    sofija "Вот так же обо мне потом заговорят. —"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Простите, право, как бог свят,"

    lizanka "Хотела я, чтоб этот смех дурацкий"

    lizanka "Вас несколько развеселить помог."

    hide lizanka

label Act_1_Scene_6:
    "{b}Явление 6{/b}"

    show lizanka at left
    show sluga_2_3 at truecenter
    show chatskij at right

    "<{i}София, Лиза, слуга, за ним Чацкий.{/i}>"

    hide sofija
    hide lizanka
    hide sluga_2_3
    hide chatskij

    show sluga_1_6 at truecenter

    $ sluga_1_6_var = "{noalt}Слуга"

    sluga_1_6 "К вам Александр Андреич Чацкий."

    play sound1 footsteps

    sluga_1_6 "<{i}(Уходит.){/i}>"

    stop sound1

    hide sluga_1_6

label Act_1_Scene_7:
    "{b}Явление 7{/b}"

    show sofija at left
    show lizanka at truecenter
    show chatskij at right

    "<{i}София, Лиза, Чацкий.{/i}>"

    hide sofija
    hide lizanka
    hide chatskij

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Чуть свет — уж на ногах! и я у ваших ног."

    play sound1 kiss

    chatskij "<{i}(С жаром целует руку.){/i}>"

    stop sound1

    chatskij "Ну поцелуйте же, не ждали? говорите!"

    chatskij "Что ж, рады? Нет? В лицо мне посмотрите."

    chatskij "Удивлены? и только? вот прием!"

    chatskij "Как будто не прошло недели,"

    chatskij "Как будто бы вчера вдвоем"

    chatskij "Мы мочи нет друг другу надоели,"

    chatskij "Ни на́ волос любви! куда как хороши!"

    chatskij "И между тем, не вспомнюсь, без души,"

    chatskij "Я сорок пять часов, глаз мигом не прищуря,"

    chatskij "Верст больше седьмисот пронесся, — ветер, буря;"

    chatskij "И растерялся весь, и падал сколько раз —"

    chatskij "И вот за подвиги награда!"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Ах! Чацкий, я вам очень рада."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Вы рады? в добрый час."

    chatskij "Однако искренно кто ж радуется эдак?"

    chatskij "Мне кажется, так напоследок"

    chatskij "Людей и лошадей знобя,"

    chatskij "Я только тешил сам себя."

    hide chatskij

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Вот, сударь, если бы вы были за дверями,"

    lizanka "Ей-богу, нет пяти минут,"

    lizanka "Как поминали вас мы тут."

    lizanka "Сударыня, скажите сами."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Всегда, не только что теперь. —"

    sofija "Не можете мне сделать вы упрека."

    sofija "Кто промелькнет, отворит дверь,"

    sofija "Проездом, случаем, из чужи, из далека —"

    sofija "С вопросом я, хоть будь моряк:"

    sofija "Не повстречал ли где в почтовой вас карете?"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Положимте, что так."

    chatskij "Блажен, кто верует, тепло ему на свете! —"

    chatskij "Ах! Боже мой! ужли я здесь опять,"

    chatskij "В Москве! у вас! да как же вас узнать!"

    chatskij "Где время то? где возраст тот невинный,"

    chatskij "Когда, бывало, в вечер длинный"

    chatskij "Мы с вами явимся, исчезнем тут и там,"

    chatskij "Играем и шумим по стульям и столам."

    chatskij "А тут ваш батюшка с мадамой, за пикетом;"

    chatskij "Мы в темном уголке, и кажется, что в этом!"

    chatskij "Вы помните? вздрогнем, что скрипнет столик,"

    chatskij "{space=400}дверь..."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Ребячество!"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Да-с, а теперь,"

    chatskij "В седьмнадцать лет вы расцвели прелестно,"

    chatskij "Неподражаемо, и это вам известно,"

    chatskij "И потому скромны, не смотрите на свет."

    chatskij "Не влюблены ли вы? прошу мне дать ответ,"

    chatskij "Без думы, полноте смущаться."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Да хоть кого смутят"

    sofija "Вопросы быстрые и любопытный взгляд..."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Помилуйте, — не вам, чему же удивляться?"

    chatskij "Что нового покажет мне Москва?"

    chatskij "Вчера был бал, а завтра будет два."

    chatskij "Тот сватался — успел, а тот дал промах."

    chatskij "Все тот же толк, и те ж стихи в альбомах."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Гоненье на Москву. Что значит видеть свет!"

    sofija "Где ж лучше?"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Где нас нет."

    chatskij "Ну что ваш батюшка? все Английского клоба"

    chatskij "Старинный, верный член до гроба?"

    chatskij "Ваш дядюшка отпрыгал ли свой век?"

    chatskij "А этот, как его, он турок или грек?"

    chatskij "Тот черномазенький, на ножках журавлиных,"

    chatskij "Не знаю как его зовут,"

    chatskij "Куда ни сунься: тут, как тут."

    chatskij "В столовых и в гостиных?"

    chatskij "А трое из бульварных лиц,"

    chatskij "Которые с полвека молодятся?"

    chatskij "Родных мильон у них, и с помощью сестриц"

    chatskij "Со всей Европой породнятся."

    chatskij "А наше солнышко? наш клад?"

    chatskij "На лбу написано: Театр и Маскерад;"

    chatskij "Дом зеленью раскрашен в виде рощи,"

    chatskij "Сам толст, его артисты тощи."

    chatskij "На бале, помните, открыли мы вдвоем"

    chatskij "За ширмами, в одной из комнат посекретней,"

    chatskij "Был спрятан человек и щелкал соловьем,"

    chatskij "Певец зимой погоды летней."

    chatskij "А тот чахоточный, родня вам, книгам враг,"

    chatskij "В ученый комитет который поселился"

    chatskij "И с криком требовал присяг,"

    chatskij "Чтоб грамоте никто не знал и не учился?"

    chatskij "Опять увидеть их мне суждено судьбой!"

    chatskij "Жить с ними надоест, и в ком не сыщещь пятен?"

    chatskij "Когда ж пространствуешь, воротишься домой,"

    chatskij "И дым Отечества нам сладок и приятен!"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Вот вас бы с тетушкою свесть,"

    sofija "Чтоб всех знакомых перечесть."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "А тетушка? все девушкой, Минервой?"

    chatskij "Все фрейлиной Екатерины Первой?"

    chatskij "Воспитанниц и мосек полон дом?"

    chatskij "Ах! к воспитанью перейдем."

    chatskij "Что нынче, так же, как издревле,"

    chatskij "Хлопочут набирать учителей полки,"

    chatskij "Числом поболее, ценою подешевле?"

    chatskij "Не то, чтобы в науке далеки;"

    chatskij "В России, под великим штрафом,"

    chatskij "Нам каждого признать велят"

    chatskij "Историком и геогра́фом!"

    chatskij "Наш ментор, помните колпак его, халат,"

    chatskij "Перст указательный, все признаки ученья"

    chatskij "Как наши робкие тревожные умы,"

    chatskij "Как с ранних пор привыкли верить мы,"

    chatskij "Что нам без немцев нет спасенья! —"

    chatskij "А Гильоме, француз, подбитый ветерком?"

    chatskij "Он не женат еще?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}На ком?"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Хоть на какой-нибудь княгине"

    chatskij "Пульхерии Андревне, например?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Танцмейстер! можно ли!"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Что ж, он и кавалер."

    chatskij "От нас потребуют с именьем быть и в чине,"

    chatskij "А Гильоме!.. — Здесь нынче тон каков"

    chatskij "На съездах, на больших, по праздникам приходским"

    chatskij "Господствует еще смешенье языков:"

    chatskij "Французского с нижегородским? —"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Смесь языков?"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Да, двух, без этого нельзя ж."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Но мудрено из них один скроить, как ваш."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "По крайней мере не надутый."

    chatskij "Вот новости! — я пользуюсь минутой,"

    chatskij "Свиданьем с вами оживлен,"

    chatskij "И говорлив; а разве нет времен,"

    chatskij "Что я Молчалина глупее? Где он, кстати?"

    chatskij "Еще ли не сломил безмолвия печати?"

    chatskij "Бывало песенок где новеньких тетрадь"

    chatskij "Увидит, пристает: пожалуйте списать."

    chatskij "А впрочем, он дойдет до степеней известных,"

    chatskij "Ведь нынче любят бессловесных."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(в сторону){/i}>"

    sofija "Не человек, змея!"

    sofija "<{i}(Громко и принужденно){/i}>"

    sofija "{space=400}Хочу у вас спросить:"

    sofija "Случалось ли, чтоб вы смеясь? или в печали?"

    sofija "Ошибкою? добро о ком-нибудь сказали?"

    sofija "Хоть не теперь, а в детстве может быть."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Когда все мягко так? и нежно, и незрело?"

    chatskij "На что же так давно? вот доброе вам дело:"

    chatskij "Звонками только что гремя"

    chatskij "И день и ночь по снеговой пустыне,"

    chatskij "Спешу к вам, голову сломя."

    chatskij "И как вас нахожу? в каком-то строгом чине!"

    chatskij "Вот полчаса холодности терплю!"

    chatskij "Лицо святейшей богомолки!.."

    chatskij "И все-таки я вас без памяти люблю."

    chatskij "<{i}Минутное молчание.{/i}>"

    chatskij "Послушайте, ужли слова мои все колки?"

    chatskij "И клонятся к чьему-нибудь вреду?"

    chatskij "Но если так: ум с сердцем не в ладу."

    chatskij "Я в чудаках иному чуду"

    chatskij "Раз посмеюсь, потом забуду;"

    chatskij "{space=400}Велите ж мне в огонь: пойду как на обед."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Да, хорошо сгорите, если ж нет?"

    hide sofija

label Act_1_Scene_8:
    "{b}Явление 8{/b}"

    show lizanka at left
    show chatskij at truecenter
    show famusov at right

    "<{i}София, Лиза, Чацкий, Фамусов.{/i}>"

    hide sofija
    hide lizanka
    hide chatskij
    hide famusov

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Вот и другой."

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Ах, батюшка, сон в руку."

    play sound1 footsteps

    sofija "<{i}(Уходит.){/i}>"

    stop sound1

    hide sofija

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    hide famusov

    show famusov at left
    show sofija at right

    famusov "<{i}(ей вслед вполголоса){/i}>"

    hide sofija

    show famusov at truecenter

    famusov "Проклятый сон."

    hide famusov

label Act_1_Scene_9:
    "{b}Явление 9{/b}"

    play sound1 footsteps
    play sound2 door_creak

    show famusov at left
    show chatskij at truecenter
    show sofija at right

    "<{i}Фамусов, Чацкий (смотрит на дверь, в которую София вышла).{/i}>"

    hide famusov
    hide chatskij
    hide sofija

    stop sound1
    stop sound2

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Ну выкинул ты штуку!"

    famusov "Три года не писал двух слов!"

    famusov "И грянул вдруг как с облаков."

    famusov "<{i}Обнимаются.{/i}>"

    famusov "Здорово, друг, здорово, брат, здорово!"

    famusov "Рассказывай, чай у тебя готово"

    famusov "Собранье важное вестей?"

    famusov "Садись-ка, объяви скорей."

    famusov "<{i}Садятся.{/i}>"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(рассеянно){/i}>"

    chatskij "Как Софья Павловна у вас похорошела!"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Вам, людям молодым, другого нету дела,"

    famusov "Как замечать девичьи красоты:"

    famusov "Сказала что-то вскользь, а ты,"

    famusov "Я чай, надеждами занесся, заколдован."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Ах! нет, надеждами я мало избалован."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "«Сон в руку» — мне она изволила шепнуть,"

    famusov "Вот ты задумал..."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Я? — Ничуть."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "О ком ей снилось? что такое?"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я не отгадчик снов."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Не верь ей, все пустое."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я верю собственным глазам;"

    chatskij "Век не встречал, подписку дам,"

    chatskij "Что б было ей хоть несколько подобно!"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Он все свое. Да расскажи подробно,"

    famusov "Где был? Скитался столько лет!"

    famusov "Откудова теперь?"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Теперь мне до того ли!"

    chatskij "Хотел объехать, целый свет,"

    chatskij "И не объехал сотой доли."

    chatskij "<{i}(Встает поспешно.){/i}>"

    chatskij "Простите; я спешил скорее видеть вас,"

    chatskij "Не заезжал домой. Прощайте! Через час"

    chatskij "Явлюсь, подробности малейшей не забуду,"

    chatskij "Вам первым, вы потом рассказывайте всюду."

    play sound1 door_creak

    chatskij "<{i}(В дверях){/i}>"

    stop sound1

    chatskij "Как хороша!"

    play sound1 footsteps

    chatskij "<{i}(Уходит.){/i}>"

    stop sound1

    hide chatskij

label Act_1_Scene_10:
    "{b}Явление 10{/b}"

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(один){/i}>"

    famusov "{space=400}Который же из двух?"

    famusov "«Ах! батюшка, сон в руку!»"

    famusov "И говорит мне это вслух!"

    famusov "Ну, виноват! Какого ж дал я крюку!"

    famusov "Молчалин давиче в сомненье ввел меня."

    famusov "Теперь... да в полмя из огня:"

    famusov "Тот нищий, этот франт-приятель;"

    famusov "Отъявлен мотом, сорванцом;"

    famusov "Что за комиссия, Создатель,"

    famusov "Быть взрослой дочери отцом! —"

    play sound1 footsteps

    famusov "<{i}(Уходит.){/i}>"

    stop sound1

    hide famusov

label Act_2:
    play music "audio/music/12.mp3" fadeout 1.0 fadein 1.0

    scene 4 with fade

    "{b}Действие второе{/b}"

    menu:
        "{color=#000}Явление 1{/color}":
            jump Act_2_Scene_1
        "{color=#000}Явление 2{/color}":
            jump Act_2_Scene_2
        "{color=#000}Явление 3{/color}":
            jump Act_2_Scene_3
        "{color=#000}Явление 4{/color}":
            jump Act_2_Scene_4
        "{color=#000}Явление 5{/color}":
            jump Act_2_Scene_5
        "{color=#000}Явление 6{/color}":
            jump Act_2_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_2_Scene_6_1

label Further_Act_2_Scene_6_1:
    menu:
        "{color=#000}Явление 7{/color}":
            jump Act_2_Scene_7
        "{color=#000}Явление 8{/color}":
            jump Act_2_Scene_8
        "{color=#000}Явление 9{/color}":
            jump Act_2_Scene_9
        "{color=#000}Явление 10{/color}":
            jump Act_2_Scene_10
        "{color=#000}Явление 11{/color}":
            jump Act_2_Scene_11
        "{color=#000}Явление 12{/color}":
            jump Act_2_Scene_12
        "{color=#000}>{/color}":
            jump Further_Act_2_Scene_12_2

label Further_Act_2_Scene_12_2:
    menu:
        "{color=#000}Явление 13{/color}":
            jump Act_2_Scene_13

label Act_2_Scene_1:
    "{b}Явление 1{/b}"

    show famusov at left
    show sluga_2_3 at right

    "<{i}Фамусов, Слуга.{/i}>"

    hide famusov
    hide sluga_2_3

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Петрушка, вечно ты с обновкой,"

    famusov "С разодранным локтем. Достань-ка календарь:"

    famusov "Читай не так, как пономарь;"

    famusov "А с чувством, с толком, с расстановкой."

    famusov "Постой же. — На листе черкни на записном,"

    famusov "Противу будущей недели:"

    famusov "К Прасковье Федоровне в дом"

    famusov "Во вторник зван я на форели."

    famusov "Куда как чуден создан свет!"

    famusov "Пофилософствуй, ум вскружится;"

    famusov "То бережешься, то обед:"

    famusov "Ешь три часа, а в три дни не сварится!"

    famusov "Отметь-ка, в тот же день... Нет, нет."

    famusov "В четверг я зван на погребенье."

    famusov "Ох, род людской! пришло в забвенье,"

    famusov "Что всякий сам туда же должен лезть,"

    famusov "В тот ларчик, где ни стать, ни сесть."

    famusov "Но память по себе намерен кто оставить"

    famusov "Житьем похвальным, вот пример:"

    famusov "Покойник был почтенный камергер,"

    famusov "С ключом, и сыну ключ умел доставить;"

    famusov "Богат, и на богатой был женат;"

    famusov "Переженил детей, внучат;"

    famusov "Скончался; все о нем прискорбно поминают."

    famusov "Кузьма Петрович! Мир ему! —"

    famusov "Что за тузы в Москве живут и умирают! —"

    famusov "Пиши в четверг, одно уж к одному,"

    famusov "А может в пятницу, а может и в субботу,"

    famusov "Я должен у вдовы, у докторши, крестить."

    famusov "Она не родила, но по расчету"

    famusov "По моему: должна родить. —"

    hide famusov

label Act_2_Scene_2:
    "{b}Явление 2{/b}"

    show famusov at left
    show sluga_2_3 at truecenter
    show chatskij at right

    "<{i}Фамусов, Слуга, Чацкий.{/i}>"

    hide famusov
    hide sluga_2_3
    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "А! Александр Андреич, просим,"

    famusov "Садитесь-ко."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Вы заняты?"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    hide famusov

    show famusov at left
    show sluga_2_3 at right

    famusov "<{i}(Слуге){/i}>"

    hide sluga_2_3

    show famusov at truecenter

    famusov "{space=400}Поди."

    play sound1 footsteps

    hide famusov

    show famusov at left
    show sluga_2_3 at right

    famusov "<{i}Слуга уходит.{/i}>"

    hide sluga_2_3

    show famusov at truecenter

    stop sound1

    famusov "Да, разные дела на память в книгу вносим,"

    famusov "Забудется того гляди. —"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Вы что-то не весёлы стали;"

    chatskij "Скажите, отчего? Приезд не в пору мой?"

    chatskij "Уж Софье Павловне какой"

    chatskij "Не приключилось ли печали?"

    chatskij "У вас в лице, в движеньях суета."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Ах! батюшка, нашел загадку,"

    famusov "Не весел я!.. В мои лета"

    famusov "Не можно же пускаться мне вприсядку!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Никто не приглашает вас;"

    chatskij "Я только, что спросил два слова"

    chatskij "Об Софье Павловне, быть может, нездорова?"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Тьфу, господи прости! Пять тысяч раз"

    famusov "Твердит одно и то же!"

    famusov "То Софьи Павловны на свете нет пригоже,"

    famusov "То Софья Павловна больна, —"

    famusov "Скажи, тебе понравилась она?"

    famusov "Обрыскал свет; не хочешь ли жениться?"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "А вам на что?"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Меня не худо бы спроситься,"

    famusov "Ведь я ей несколько сродни;"

    famusov "По крайней мере искони"

    famusov "Отцом недаром называли."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Пусть я посватаюсь, вы что бы мне сказали?"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Сказал бы я, во-первых: не блажи,"

    famusov "Именьем, брат, не упрекай оплошно,"

    famusov "А, главное, поди-тка послужи."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Служить бы рад, прислуживаться тошно."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Вот то-то, все вы гордецы!"

    famusov "Спросили бы, как делали отцы?"

    famusov "Учились бы, на старших глядя:"

    famusov "Мы, например, или покойник дядя,"

    famusov "Максим Петрович: он не то на серебре,"

    famusov "На золоте едал; сто человек к услугам;"

    famusov "Весь в орденах; езжал-то вечно цугом;"

    famusov "Век при дворе, да при каком дворе!"

    famusov "{space=400}Тогда не то, что ныне,"

    famusov "При государыне служил Екатерине."

    famusov "А в те поры все важны! в сорок пуд..."

    famusov "Раскланяйся — тупеем не кивнут."

    famusov "Вельможа в случае — тем паче,"

    famusov "Не как другой, и пил и ел иначе."

    famusov "А дядя! что твой князь? что граф?"

    famusov "Сурьезный взгляд, надменный нрав."

    famusov "Когда же надо подслужиться,"

    famusov "И он сгибался вперегиб:"

    famusov "На куртаге ему случилось обступиться;"

    famusov "Упал, да так, что чуть затылка не пришиб;"

    famusov "Старик заохал, голос хрипкий;"

    famusov "Был высочайшею пожалован улыбкой;"

    famusov "Изволили смеяться; как же он?"

    famusov "Привстал, оправился, хотел отдать поклон,"

    famusov "Упал вдруго́рядь — уж нарочно, —"

    famusov "А хохот пуще, он и в третий так же точно."

    famusov "А? как по вашему? по нашему — смышлен."

    famusov "Упал он больно, встал здорово."

    famusov "Зато, бывало, в вист кто чаще приглашен?"

    famusov "Кто слышит при дворе приветливое слово?"

    famusov "Максим Петрович! Кто пред всеми знал почет?"

    famusov "Максим Петрович! Шутка!"

    famusov "В чины выводит кто и пенсии дает?"

    famusov "Максим Петрович! Да! Вы, нынешние, — ну-тка!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "И точно начал свет глупеть,"

    chatskij "Сказать вы можете вздохнувши;"

    chatskij "Как посравнить, да посмотреть"

    chatskij "Век нынешний и век минувший:"

    chatskij "Свежо предание, а верится с трудом;"

    chatskij "Как тот и славился, чья чаще гнулась шея;"

    chatskij "Как не в войне, а в мире брали лбом;"

    chatskij "Стучали об пол не жалея!"

    chatskij "Кому нужда: тем спесь, лежи они в пыли,"

    chatskij "А тем, кто выше, лесть как кружево плели."

    chatskij "Прямой был век покорности и страха,"

    chatskij "Всё под личиною усердия к царю."

    chatskij "Я не об дядюшке об вашем говорю;"

    chatskij "Его не возмутим мы праха:"

    chatskij "Но между тем кого охота заберет,"

    chatskij "Хоть в раболепстве самом пылком,"

    chatskij "Теперь, чтобы смешить народ,"

    chatskij "Отважно жертвовать затылком?"

    chatskij "А сверстничек, а старичок"

    chatskij "Иной, глядя на тот скачок,"

    chatskij "И разрушаясь в ветхой коже,"

    chatskij "Чай приговаривал: ах! если бы мне тоже!"

    chatskij "Хоть есть охотники поподличать везде,"

    chatskij "Да нынче смех страшит, и держит стыд в узде;"

    chatskij "Недаром жалуют их скупо государи."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Ах! Боже мой! он карбонари!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Нет, нынче свет уж не таков."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Опасный человек!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Вольнее всякий дышит"

    chatskij "И не торопится вписаться в полк шутов."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Что говорит! и говорит, как пишет!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "У покровителей зевать на потолок,"

    chatskij "Явиться помолчать, пошаркать, пообедать,"

    chatskij "Подставить стул, поднять платок."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Он вольность хочет проповедать!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Кто путешествует, в деревне кто живет..."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Да он властей не признает!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Кто служит делу, а не лицам..."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Строжайше б запретил я этим господам"

    famusov "На выстрел подъезжать к столицам."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я наконец вам отдых дам..."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Терпенья, мочи нет, досадно."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Ваш век бранил я беспощадно,"

    chatskij "Предоставляю вам во власть:"

    chatskij "{space=400}Откиньте часть,"

    chatskij "Хоть нашим временам в придачу;"

    chatskij "Уж так и быть, я не поплачу."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "И знать вас не хочу, разврата не терплю."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я досказал."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Добро заткнул я уши."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "На что ж? я их не оскорблю. —"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(скороговоркой){/i}>"

    famusov "Вот рыскают по свету, бьют баклуши,"

    famusov "Воротятся, от них порядка жди."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я перестал..."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Пожалуй, пощади."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Длить споры не мое желанье..."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Хоть душу отпусти на покаянье!"

    hide famusov

label Act_2_Scene_3:
    "{b}Явление 3{/b}"

    show sluga_2_3 at truecenter

    $ sluga_2_3_var = "{noalt}Слуга"

    play sound1 footsteps

    sluga_2_3 "<{i}(входит){/i}>"

    stop sound1

    sluga_2_3 "Полковник Скалозуб."

    hide sluga_2_3

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(ничего не видит и не слышит.){/i}>"

    famusov "{space=400}Тебя уж упекут."

    famusov "Под суд, как пить дадут."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Пожаловал к вам кто-то на́ дом."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Не слушаю, под суд!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}К вам человек с докладом."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Не слушаю, под суд! под суд!"

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Да обернитесь, вас зовут."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(оборачивается){/i}>"

    famusov "А? бунт? ну так и жду содома."

    hide famusov

    show sluga_2_3 at truecenter

    $ sluga_2_3_var = "{noalt}Слуга"

    sluga_2_3 "Полковник Скалозуб. Прикажете принять?"

    hide sluga_2_3

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(встает){/i}>"

    famusov "Ослы! сто раз вам повторять?"

    famusov "Принять его, позвать, просить, сказать, что дома,"

    famusov "Что очень рад. Пошел же, торопись."

    play sound1 footsteps

    hide famusov

    show famusov at left
    show sluga_2_3 at right

    famusov "<{i}Слуга уходит.{/i}>"

    hide sluga_2_3

    show famusov at truecenter

    stop sound1

    famusov "Пожало-ста, суда́рь, при нем остерегись:"

    famusov "Известный человек, солидный,"

    famusov "И знаков тьму отличья нахватал;"

    famusov "Не по летам и чин завидный,"

    famusov "Не нынче завтра генерал."

    famusov "Пожало-ста при нем веди себя скромненько."

    famusov "Эх! Александр Андреич, дурно, брат!"

    famusov "Ко мне он жалует частенько;"

    famusov "Я всякому, ты знаешь, рад;"

    famusov "В Москве прибавят вечно втрое;"

    famusov "Вот будто женится на Сонюшке. Пустое!"

    famusov "Он, может быть, и рад бы был душой,"

    famusov "Да надобности сам не вижу я большой"

    famusov "Дочь выдавать ни завтра, ни сегодня;"

    famusov "Ведь Софья молода. А впрочем, власть господня."

    famusov "Пожало-ста при нем не спорь ты вкривь и вкось,"

    famusov "И завиральные идеи эти брось."

    famusov "Однако нет его! какую бы причину..."

    famusov "А! знать ко мне пошел в другую половину."

    play sound1 footsteps

    famusov "<{i}(Поспешно уходит.){/i}>"

    stop sound1

    hide famusov

label Act_2_Scene_4:
    "{b}Явление 4{/b}"

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Как суетится! что за прыть!"

    chatskij "А Софья? — Нет ли впрямь тут жениха какого?"

    chatskij "С которых пор меня дичатся как чужого!"

    chatskij "Как здесь бы ей не быть!!"

    chatskij "Кто этот Скалозуб? отец им сильно бредит,"

    chatskij "А может быть, не только, что отец..."

    chatskij "Ах! тот скажи любви конец,"

    chatskij "Кто на три года вдаль уедет."

    hide chatskij

label Act_2_Scene_5:
    "{b}Явление 5{/b}"

    show chatskij at left
    show famusov at truecenter
    show skalozub at right

    "<{i}Чацкий, Фамусов, Скалозуб.{/i}>"

    hide chatskij
    hide famusov
    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Сергей Сергеич, к нам сюда-с."

    famusov "Прошу покорно, здесь теплее;"

    famusov "Прозябли вы, согреем вас;"

    famusov "Отдушничек отвернем поскорее."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "<{i}(густым басом){/i}>"

    skalozub "Зачем же лазить, например,"

    skalozub "Самим!... Мне совестно, как честный офицер."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Неужто для друзей не делать мне ни шагу,"

    famusov "Сергей Сергеич дорогой!"

    famusov "Кладите шляпу, сденьте шпагу;"

    famusov "Вот вам софа, раскиньтесь на покой."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Куда прикажете, лишь только бы усесться."

    hide skalozub

    show skalozub at left
    show chatskij at right

    skalozub "<{i}(Садятся все трое. Чацкий поодаль.){/i}>"

    hide chatskij

    show skalozub at truecenter

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Ах! батюшка, сказать, чтоб не забыть:"

    famusov "Позвольте нам своими счесться,"

    famusov "Хоть дальними, — наследства не делить;"

    famusov "Не знали вы, а я подавно,"

    famusov "Спасибо научил двоюродный ваш брат,"

    famusov "Как вам доводится Настасья Николавна?"

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Не знаю-с, виноват;"

    skalozub "Мы с нею вместе не служили."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Сергей Сергеич, это вы ли!"

    famusov "Нет! я перед родней, где встретится, ползком;"

    famusov "Сыщу ее на дне морском."

    famusov "При мне служащие чужие очень редки;"

    famusov "Все больше сестрины, свояченицы детки;"

    famusov "Один Молчалин мне не свой,"

    famusov "И то затем, что деловой."

    famusov "Как станешь представлять к крестишку ли,"

    famusov "{space=400}к местечку,"

    famusov "Ну как не порадеть родному человечку!.."

    famusov "Однако братец ваш мне друг и говорил,"

    famusov "Что вами выгод тьму по службе получил."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "В тринадцатом году мы отличались с братом"

    skalozub "В тридцатом егерском, а после в сорок пятом."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Да, счастье у кого есть эдакий сынок;"

    famusov "Имеет, кажется, в петличке орденок?"

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "За третье августа; засели мы в траншею:"

    skalozub "Ему дан с бантом, мне на шею."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Любезный человек, и посмотреть — так хват;"

    famusov "Прекрасный человек двоюродный ваш брат."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Но крепко набрался каких-то новых правил."

    skalozub "Чин следовал ему: он службу вдруг оставил,"

    skalozub "В деревне книги стал читать."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Вот молодость!.. читать!.. а после — хвать!.."

    famusov "Вы повели себя исправно,"

    famusov "Давно полковники, а служите недавно."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Довольно счастлив я в товарищах моих,"

    skalozub "Вакансии как раз открыты:"

    skalozub "То старших выключат иных,"

    skalozub "Другие, смотришь, перебиты."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Да, чем кого господь поищет, вознесет!"

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Бывает, моего счастливее везет,"

    skalozub "У нас в пятнадцатой дивизии, не дале,"

    skalozub "Об нашем хоть сказать бригадном генерале."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Помилуйте, а вам чего недостает?"

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Не жалуюсь, не обходили,"

    skalozub "Однако за полком два года поводили."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "В погонь ли за полком?"

    famusov "Зато, конечно, в чем другом"

    famusov "За вами далеко тянуться."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Нет-с, ста́рее меня по корпусу найдутся,"

    skalozub "Я с восемьсот девятого служу;"

    skalozub "Да, чтоб чины добыть, есть многие каналы;"

    skalozub "Об них как истинный философ я сужу;"

    skalozub "Мне только бы досталось в генералы."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "И славно судите, дай бог здоровье вам"

    famusov "И генеральский чин; а там"

    famusov "Зачем откладывать бы дальше,"

    famusov "Речь завести об генеральше?"

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Жениться? Я ничуть не прочь."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Что ж? у кого сестра, племянница есть, дочь;"

    famusov "В Москве ведь нет невестам перевода;"

    famusov "Чего? плодятся год от года;"

    famusov "А батюшка, признайтесь, что едва"

    famusov "Где сыщется столица, как Москва."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Дистанции огромного размера."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Вкус, батюшка, отменная манера;"

    famusov "На все свои законы есть:"

    famusov "Вот, например, у нас уж исстари ведется,"

    famusov "Что по отцу и сыну честь;"

    famusov "Будь плохинький, да если наберется"

    famusov "Душ тысячки две родовых —"

    famusov "{space=400}Тот и жених."

    famusov "Другой хоть прытче будь, надутый всяким"

    famusov "{space=400}чванством,"

    famusov "Пускай себе разумником слыви,"

    famusov "А в се́мью не включат. На нас не подиви."

    famusov "Ведь только здесь еще и дорожат дворянством."

    famusov "Да это ли одно? возьмите вы хлеб-соль:"

    famusov "Кто хочет к нам пожаловать, — изволь;"

    famusov "Дверь отперта для званных и незванных,"

    famusov "Особенно из иностранных;"

    famusov "Хоть честный человек, хоть нет,"

    famusov "Для нас равнехонько, про всех готов обед."

    famusov "Возьмите вы от головы до пяток,"

    famusov "На всех московских есть особый отпечаток."

    famusov "Извольте посмотреть на нашу молодежь,"

    famusov "На юношей — сынков и вну́чат,"

    famusov "Журим мы их, а если разберешь, —"

    famusov "В пятнадцать лет учителей научат!"

    famusov "А наши старички?? — Как их возьмет задор,"

    famusov "Засудят об делах, что слово — приговор, —"

    famusov "Ведь столбовые всё, в ус никого не дуют;"

    famusov "И об правительстве иной раз так толкуют,"

    famusov "Что если б кто подслушал их... беда!"

    famusov "Не то, чтоб новизны вводили, — никогда,"

    famusov "Спаси нас боже! Нет. А придерутся"

    famusov "К тому, к сему, а чаще ни к чему,"

    famusov "Поспорят, пошумят, и... разойдутся."

    famusov "Прямые канцлеры в отставке — по уму!"

    famusov "Я вам скажу, знать время не приспело,"

    famusov "Но что без них не обойдется дело. —"

    famusov "А дамы? — сунься кто, попробуй, овладей;"

    famusov "Судьи́ всему, везде, над ними нет судей;"

    famusov "За картами когда восстанут общим бунтом,"

    famusov "Дай бог терпение, ведь сам я был женат."

    famusov "Скомандовать велите перед фрунтом!"

    famusov "Присутствовать пошлите их в Сенат!"

    famusov "Ирина Власьевна! Лукерья Алексевна!"

    famusov "Татьяна Юрьевна! Пульхерия Андревна!"

    famusov "А дочек кто видал, всяк голову повесь,"

    famusov "Его величество король был прусский здесь;"

    famusov "Дивился не путем московским от девицам,"

    famusov "Их благонравью, а не лицам,"

    famusov "И точно, можно ли воспитаннее быть!"

    famusov "Умеют же себя принарядить"

    famusov "Тафтицей, бархатцем и дымкой,"

    famusov "Словечка в простоте не скажут, всё с ужимкой;"

    famusov "Французские романсы вам поют"

    famusov "И верхние выводят нотки,"

    famusov "К военным людям так и льнут,"

    famusov "А потому, что патриотки."

    famusov "Решительно скажу: едва"

    famusov "Другая сыщется столица как Москва."

    hide famusov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "По моему сужденью,"

    skalozub "Пожар способствовал ей много к украшенью."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Не поминайте нам, уж мало ли крехтят:"

    famusov "С тех пор дороги, тротуары,"

    famusov "Дома и все на новый лад."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Дома новы́, но предрассудки стары."

    chatskij "Порадуйтесь, не истребят"

    chatskij "Ни годы их, ни моды, ни пожары."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    hide famusov

    show famusov at left
    show chatskij at right

    famusov "<{i}(Чацкому){/i}>"

    hide chatskij

    show famusov at truecenter

    famusov "Эй, завяжи на память узелок;"

    famusov "Просил я помолчать, не велика услуга."

    hide famusov

    show famusov at left
    show skalozub at right

    famusov "<{i}(Скалозубу){/i}>"

    hide skalozub

    show famusov at truecenter

    famusov "Позвольте, батюшка. Вот-с — Чацкого, мне друга,"

    famusov "Андрея Ильича покойного сынок:"

    famusov "Не служит, то есть в том он пользы не находит,"

    famusov "Но захоти — так был бы деловой,"

    famusov "Жаль, очень жаль, он малый с головой;"

    famusov "И славно пишет, переводит."

    famusov "Нельзя не пожалеть, что с эдаким умом..."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Нельзя ли пожалеть об ком-нибудь другом?"

    chatskij "И похвалы мне ваши досаждают."

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Не я один, все также осуждают."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "А судьи кто? — За древностию лет"

    chatskij "К свободной жизни их вражда непримирима,"

    chatskij "Сужденья черпают из забытых газет"

    chatskij "Времен Очаковских и покоренья Крыма;"

    chatskij "Всегда готовые к журьбе,"

    chatskij "Поют всё песнь одну и ту же,"

    chatskij "Не замечая об себе:"

    chatskij "Что старее, то хуже."

    chatskij "Где? укажите нам, отечества отцы,"

    chatskij "Которых мы должны принять за образцы?"

    chatskij "Не эти ли, грабительством богаты?"

    chatskij "Защиту от суда в друзьях нашли, в родстве,"

    chatskij "Великолепные соорудя палаты,"

    chatskij "Где разливаются в пирах и мотовстве,"

    chatskij "И где не воскресят клиенты-иностранцы"

    chatskij "Прошедшего житья подлейшие черты."

    chatskij "Да и кому в Москве не зажимали рты"

    chatskij "Обеды, ужины и танцы?"

    chatskij "Не тот ли, вы к кому меня еще с пелен,"

    chatskij "Для замыслов каких-то непонятных,"

    chatskij "Дитёй возили на поклон?"

    chatskij "Тот Нестор негодяев знатных,"

    chatskij "Толпою окруженный слуг;"

    chatskij "Усердствуя, они в часы вина и драки"

    chatskij "И честь и жизнь его не раз спасали: вдруг"

    chatskij "На них он выменил борзые три собаки!!!"

    chatskij "Или вон тот еще, который для затей"

    chatskij "На крепостной балет согнал на многих фурах"

    chatskij "От матерей, отцов отторженных детей?!"

    chatskij "Сам погружен умом в Зефирах и в Амурах,"

    chatskij "Заставил всю Москву дивиться их красе!"

    chatskij "Но должников не согласил к отсрочке:"

    chatskij "Амуры и Зефиры все"

    chatskij "Распроданы по одиночке!!"

    chatskij "Вот те, которые дожили до седин!"

    chatskij "Вот уважать кого должны мы на безлюдьи!"

    chatskij "Вот наши строгие ценители и судьи!"

    chatskij "Теперь пускай из нас один,"

    chatskij "Из молодых людей, найдется — враг исканий,"

    chatskij "Не требуя ни мест, ни повышенья в чин,"

    chatskij "В науки он вперит ум, алчущий познаний;"

    chatskij "К искусствам творческим, высоким и прекрасным,"

    chatskij "Они тотчас: разбой! пожар!"

    chatskij "И прослывет у них мечтателем! опасным!! —"

    chatskij "Мундир! один мундир! Он в прежнем их быту"

    chatskij "Когда-то укрывал, расшитый и красивый,"

    chatskij "Их слабодушие, рассудка нищету;"

    chatskij "И нам за ними в путь счастливый!"

    chatskij "И в женах, дочерях — к мундиру та же страсть!"

    chatskij "Я сам к нему давно ль от нежности отрекся?!"

    chatskij "Теперь уж в это мне ребячество не впасть;"

    chatskij "Но кто б тогда за всеми не повлекся?"

    chatskij "Когда из гвардии, иные от двора"

    chatskij "Сюда на время приезжали, —"

    chatskij "Кричали женщины: ура!"

    chatskij "И в воздух чепчики бросали!"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(про себя){/i}>"

    famusov "Уж втянет он меня в беду."

    famusov "<{i}(Громко.){/i}>"

    famusov "Сергей Сергеич, я пойду,"

    famusov "И буду ждать вас в кабинете."

    play sound1 footsteps

    famusov "<{i}(Уходит.){/i}>"

    stop sound1

    hide famusov

label Act_2_Scene_6:
    "{b}Явление 6{/b}"

    show skalozub at left
    show chatskij at right

    "<{i}Скалозуб, Чацкий.{/i}>"

    hide skalozub
    hide chatskij

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Мне нравится, при этой смете"

    skalozub "Искусно как коснулись вы"

    skalozub "Предубеждения Москвы"

    skalozub "К любимцам, к гвардии, к гвардейским,"

    skalozub "{space=400}к гвардионцам;"

    skalozub "Их золоту, шитью дивятся будто солнцам!"

    skalozub "А в первой армии когда отстали? в чем?"

    skalozub "Все так прилажено, и тальи все так узки,"

    skalozub "И офицеров вам начтём,"

    skalozub "Что даже говорят, иные, по-французски."

    hide skalozub

label Act_2_Scene_7:
    "{b}Явление 7{/b}"

    show chatskij at left
    show sofija at truecenter
    show lizanka at right

    "<{i}Скалозуб, Чацкий, София, Лиза.{/i}>"

    hide skalozub
    hide chatskij
    hide sofija
    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    play sound1 running

    sofija "<{i}(бежит к окну){/i}>"

    stop sound1

    sofija "Ах! Боже мой! упал, убился!"

    sofija "<{i}(Теряет чувства.){/i}>"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Кто?"

    chatskij "Кто это?"

    hide chatskij

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "{space=400}С кем беда?"

    hide skalozub

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Она мертва со страху!"

    hide chatskij

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Да кто? откудова?"

    hide skalozub

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Ушибся обо что?"

    hide chatskij

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Уж не старик ли наш дал маху?"

    hide skalozub

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "<{i}(хлопочет около барышни){/i}>"

    lizanka "Кому назначено-с: не миновать судьбы,"

    lizanka "Молчалин на́ лошадь садился, ногу в стремя,"

    lizanka "А лошадь на дыбы."

    lizanka "Он об землю и прямо в темя."

    hide lizanka

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Поводья затянул, ну, жалкий же ездок."

    skalozub "Взглянуть, как треснулся он — грудью или в бок?"

    play sound1 footsteps

    skalozub "<{i}(Уходит.){/i}>"

    stop sound1

    hide skalozub

label Act_2_Scene_8:
    "{b}Явление 8{/b}"

    show skalozub at truecenter

    "<{i}Те же, без Скалозуба.{/i}>"

    hide skalozub

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Помочь ей чем? Скажи скорее."

    hide chatskij

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Там в комнате вода стоит."

    play sound1 running

    hide lizanka

    show lizanka at left
    show chatskij at truecenter
    show sofija at right

    lizanka "<{i}Чацкий бежит и приносит. Все следующее — вполголоса, — до того, как София
                очнется.{/i}>"

    hide chatskij
    hide sofija

    show lizanka at truecenter

    stop sound1

    lizanka "Стакан налейте."

    hide lizanka

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Уж налит."

    chatskij "Шнуровку отпусти вольнее,"

    chatskij "Виски ей уксусом потри,"

    chatskij "Опрыскивай водой. Смотри,"

    chatskij "Свободнее дыханье стало."

    chatskij "Повеять чем?"

    hide chatskij

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Вот опахало."

    hide lizanka

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Гляди в окно,"

    chatskij "Молчалин на ногах давно!"

    chatskij "Безделица ее тревожит."

    hide chatskij

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Да-с, барышнин несчастен нрав."

    lizanka "Со стороны смотреть не может,"

    lizanka "Как люди падают стремглав."

    hide lizanka

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Опрыскивай еще водою."

    chatskij "Вот так. Еще. Еще."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    play sound1 female_sigh

    sofija "<{i}(с глубоким вздохом){/i}>"

    stop sound1

    sofija "{space=400}Кто здесь со мною?"

    sofija "Я точно как во сне."

    sofija "<{i}(Торопко и громко){/i}>"

    sofija "Где он? что с ним? Скажите мне."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Пускай себе сломил бы шею,"

    chatskij "Вас чуть было не уморил."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Убийственны холодностью своею!"

    sofija "Смотреть на вас, вас слушать нету сил."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Прикажете мне за него терзаться?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Туда бежать, там быть, помочь ему стараться."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Чтоб оставались вы без помощи одне?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}На что вы мне?"

    sofija "Да, правда, не свои беды́ — для вас забавы,"

    sofija "Отец родной убейся — все равно."

    hide sofija

    show sofija at left
    show lizanka at right

    sofija "<{i}(Лизе.){/i}>"

    hide lizanka

    show sofija at truecenter

    sofija "Пойдем туда, бежим."

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    play sound1 footsteps

    hide lizanka

    show lizanka at left
    show sofija at right

    lizanka "<{i}(отводит ее в сторону){/i}>"

    hide sofija

    show lizanka at truecenter

    stop sound1

    lizanka "{space=400}Опомнитесь! куда вы?"

    lizanka "Он жив, здоров, смотрите здесь в окно."

    hide lizanka

    show sofija at truecenter

    "<{i}София в окошко высовывается.{/i}>"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Смятенье! обморок! поспешность! гнев! испуга!"

    chatskij "Так можно только ощущать,"

    chatskij "Когда лишаешься единственного друга."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Сюда идут. Руки не может он поднять."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Желал бы с ним убиться..."

    hide chatskij

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Для компаньи?"

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Нет, оставайтесь при желаньи."

    hide sofija

label Act_2_Scene_9:
    "{b}Явление 9{/b}"

    show chatskij at left
    show skalozub at truecenter
    show molchalin at right

    "<{i}София, Лиза, Чацкий, Скалозуб, Молчалин (с подвязанною рукою).{/i}>"

    hide sofija
    hide lizanka
    hide chatskij
    hide skalozub
    hide molchalin

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Воскрес и невредим, рука"

    skalozub "Ушиблена слегка,"

    skalozub "И впрочем все фальшивая тревога."

    hide skalozub

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Я вас перепугал, простите ради бога."

    hide molchalin

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Ну! я не знал, что будет из того"

    skalozub "Вам ирритация. Опро́метью вбежали. —"

    skalozub "Мы вздрогнули. — Вы в обморок упали,"

    skalozub "И что ж? — весь страх из ничего."

    hide skalozub

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    hide sofija

    show sofija at left
    show skalozub at right

    sofija "<{i}(не глядя ни на кого){/i}>"

    hide skalozub

    show sofija at truecenter

    sofija "Ах! очень вижу: из пустого,"

    sofija "А вся еще теперь дрожу."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(про себя){/i}>"

    chatskij "С Молчалиным ни слова!"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(по-прежнему){/i}>"

    sofija "Однако о себе скажу,"

    sofija "Что не труслива. Так, бывает,"

    sofija "Карета свалится, подымут: я опять"

    sofija "Готова сызнова скакать;"

    sofija "Но все малейшее в других меня пугает,"

    sofija "Хоть нет великого несчастья от того,"

    sofija "Хоть незнакомый мне, — до этого нет дела."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(про себя){/i}>"

    chatskij "Прощенья просит у него,"

    chatskij "Что раз о ком-то пожалела!"

    hide chatskij

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Позвольте расскажу вам весть:"

    skalozub "Княгиня Ласова какая-то здесь есть,"

    skalozub "Наездница, вдова, но нет примеров,"

    skalozub "Чтоб ездило с ней много кавалеров."

    skalozub "На днях расшиблась в пух, —"

    skalozub "Жоке́ не поддержал, считал он, видно, мух."

    skalozub "И без того она, как слышно, неуклюжа,"

    skalozub "Теперь ребра недостает,"

    skalozub "Так для поддержки ищет мужа."

    hide skalozub

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Ах! Александр Андреич, вот,"

    sofija "Яви́тесь, вы вполне великодушны:"

    sofija "К несчастью ближнего вы так неравнодушны."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Да-с, это я сейчас явил,"

    chatskij "Моим усерднейшим стараньем,"

    chatskij "И прысканьем, и оттираньем;"

    chatskij "Не знаю для кого, но вас я воскресил."

    play sound1 footsteps

    chatskij "<{i}(Берет шляпу и уходит.){/i}>"

    stop sound1

    hide chatskij

label Act_2_Scene_10:
    "{b}Явление 10{/b}"

    show chatskij at truecenter

    "<{i}Те же, кроме Чацкого.{/i}>"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Вы вечером к нам будете?"

    hide sofija

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "{space=400}Как рано?"

    hide skalozub

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Пораньше: съедутся домашние друзья,"

    sofija "Потанцевать под фортопияно,"

    sofija "Мы в трауре, так балу дать нельзя."

    hide sofija

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Явлюсь, но к батюшке зайти я обещался,"

    skalozub "Откланяюсь."

    hide skalozub

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Прощайте."

    hide sofija

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    hide skalozub

    show skalozub at left
    show molchalin at right

    skalozub "<{i}(жмет руку Молчалину){/i}>"

    hide molchalin

    show skalozub at truecenter

    skalozub "{space=400}Ваш слуга."

    play sound1 footsteps

    skalozub "<{i}(Уходит.){/i}>"

    stop sound1

    hide skalozub

label Act_2_Scene_11:
    "{b}Явление 11{/b}"

    show sofija at left
    show lizanka at truecenter
    show molchalin at right

    "<{i}София, Лиза, Молчалин.{/i}>"

    hide sofija
    hide lizanka
    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Молчалин! как во мне рассудок цел остался!"

    sofija "Ведь знаете, как жизнь мне ваша дорога!"

    sofija "Зачем же ей играть, и так неосторожно?"

    sofija "Скажите, что у вас с рукой?"

    sofija "Не дать ли капель вам? не нужен ли покой?"

    sofija "Пошлемте к доктору, пренебрегать не должно."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Платком перевязал, не больно мне с тех пор."

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Ударюсь об заклад, что вздор,"

    lizanka "И если б не к лицу, не нужно перевязки;"

    lizanka "А то не вздор, что вам не избежать огласки:"

    lizanka "На смех того гляди подымет Чацкий вас;"

    lizanka "И Скалозуб, как свой хохол закрутит,"

    lizanka "Расскажет обморок, прибавит сто прикрас;"

    lizanka "Шутить и он горазд, ведь нынче кто не шутит!"

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "А кем из них я дорожу?"

    sofija "Хочу люблю, хочу скажу."

    sofija "Молчалин! будто я себя не принуждала?"

    sofija "Вошли вы, слова не сказала,"

    sofija "При них не смела я дохнуть,"

    sofija "У вас спросить, на вас взглянуть."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Нет, Софья Павловна, вы слишком откровенны."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Откуда скрытность почерпнуть!"

    sofija "Готова я была в окошко, к вам прыгну́ть."

    sofija "Да что мне до кого? до них? до всей вселенны?"

    sofija "Смешно? — пусть шутят их; досадно? — пусть бранят."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Не повредила бы нам откровенность эта."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Неужто на дуэль вас вызвать захотят?"

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Ах! злые языки страшнее пистолета."

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Сидят они у батюшки теперь,"

    lizanka "Вот кабы вы порхнули в дверь"

    lizanka "С лицом веселым, беззаботно:"

    lizanka "Когда нам скажут, что хотим,"

    lizanka "Куда как верится охотно!"

    lizanka "И Александр Андреич, — с ним"

    lizanka "О прежних днях, о тех проказах"

    lizanka "Поразвернитесь-ка в рассказах:"

    lizanka "Улыбочка и пара слов,"

    lizanka "И кто влюблен — на все готов."

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Я вам советовать не смею."

    play sound1 kiss

    hide molchalin

    show molchalin at left
    show lizanka at right

    molchalin "<{i}(Целует ей руку.){/i}>"

    hide lizanka

    show molchalin at truecenter

    stop sound1

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Хотите вы?.. Пойду любезничать сквозь слез;"

    sofija "Боюсь, что выдержать притворства не сумею."

    sofija "Зачем сюда бог Чацкого принес!"

    play sound1 footsteps

    sofija "<{i}(Уходит.){/i}>"

    stop sound1

    hide sofija

label Act_2_Scene_12:
    "{b}Явление 12{/b}"

    show molchalin at left
    show lizanka at right

    "<{i}Молчалин, Лиза.{/i}>"

    hide molchalin
    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Веселое созданье ты! живое!"

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Прошу пустить, и без меня вас двое."

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Какое личико твое!"

    molchalin "Как я тебя люблю!"

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}А барышню?"

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Ее"

    molchalin "По должности, тебя..."

    hide molchalin

    show molchalin at left
    show lizanka at right

    molchalin "<{i}(Хочет ее обнять.){/i}>"

    hide lizanka

    show molchalin at truecenter

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}От скуки!"

    lizanka "Прошу подальше руки!"

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Есть у меня вещицы три:"

    molchalin "Есть туалет, прехитрая работа —"

    molchalin "Снаружи зеркальце, и зеркальце внутри,"

    molchalin "Кругом всё прорезь, позолота;"

    molchalin "Подушечка, из бисера узор;"

    molchalin "И перламутровый прибор:"

    molchalin "Игольничек и ножинки, как милы!"

    molchalin "Жемчужинки, растертые в белилы!"

    molchalin "Помада есть для губ, и для других причин,"

    molchalin "С духами сткляночки: резеда и жасмин."

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Вы знаете, что я не льщусь на интересы;"

    lizanka "Скажите лучше, почему"

    lizanka "Вы с барышней скромны, а с горнишной повесы?"

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Сегодня болен я, обвязки не сниму;"

    molchalin "Приди в обед, побудь со мною;"

    molchalin "Я правду всю тебе открою."

    play sound1 footsteps
    play sound2 door_creak

    molchalin "<{i}(Уходит в боковую дверь.){/i}>"

    stop sound1
    stop sound2

    hide molchalin

label Act_2_Scene_13:
    "{b}Явление 13{/b}"

    show sofija at left
    show lizanka at right

    "<{i}София, Лиза.{/i}>"

    hide sofija
    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Была у батюшки, там нету никого."

    sofija "Сегодня я больна, и не пойду обедать."

    sofija "Скажи Молчалину, и позови его,"

    sofija "Чтоб он пришел меня проведать."

    play sound1 footsteps

    sofija "<{i}(Уходит к себе.){/i}>"

    stop sound1

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Ну! люди в здешней стороне!"

    lizanka "Она к нему, а он ко мне,"

    lizanka "А я... одна лишь я любви до смерти трушу, —"

    lizanka "А как не полюбить буфетчика Петрушу!"

    hide lizanka

label Act_3:
    play music "audio/music/1.mp3" fadeout 1.0 fadein 1.0

    scene 5 with fade

    "{b}Действие третье{/b}"

    menu:
        "{color=#000}Явление 1{/color}":
            jump Act_3_Scene_1
        "{color=#000}Явление 2{/color}":
            jump Act_3_Scene_2
        "{color=#000}Явление 3{/color}":
            jump Act_3_Scene_3
        "{color=#000}Явление 4{/color}":
            jump Act_3_Scene_4
        "{color=#000}Явление 5{/color}":
            jump Act_3_Scene_5
        "{color=#000}Явление 6{/color}":
            jump Act_3_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_3_Scene_6_1

label Further_Act_3_Scene_6_1:
    menu:
        "{color=#000}Явление 7{/color}":
            jump Act_3_Scene_7
        "{color=#000}Явление 8{/color}":
            jump Act_3_Scene_8
        "{color=#000}Явление 9{/color}":
            jump Act_3_Scene_9
        "{color=#000}Явление 10{/color}":
            jump Act_3_Scene_10
        "{color=#000}Явление 11{/color}":
            jump Act_3_Scene_11
        "{color=#000}Явление 12{/color}":
            jump Act_3_Scene_12
        "{color=#000}>{/color}":
            jump Further_Act_3_Scene_12_2

label Further_Act_3_Scene_12_2:
    menu:
        "{color=#000}Явление 13{/color}":
            jump Act_3_Scene_13
        "{color=#000}Явление 14{/color}":
            jump Act_3_Scene_14
        "{color=#000}Явление 15{/color}":
            jump Act_3_Scene_15
        "{color=#000}Явление 16{/color}":
            jump Act_3_Scene_16
        "{color=#000}Явление 17{/color}":
            jump Act_3_Scene_17
        "{color=#000}Явление 18{/color}":
            jump Act_3_Scene_18
        "{color=#000}>{/color}":
            jump Further_Act_3_Scene_18_3

label Further_Act_3_Scene_18_3:
    menu:
        "{color=#000}Явление 19{/color}":
            jump Act_3_Scene_19
        "{color=#000}Явление 20{/color}":
            jump Act_3_Scene_20
        "{color=#000}Явление 21{/color}":
            jump Act_3_Scene_21
        "{color=#000}Явление 22{/color}":
            jump Act_3_Scene_22

label Act_3_Scene_1:
    "{b}Явление 1{/b}"

    show chatskij at left
    show sofija at right

    "<{i}Чацкий, потом София.{/i}>"

    hide chatskij
    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Дождусь ее, и вынужу признанье:"

    chatskij "Кто наконец ей мил? Молчалин! Скалозуб!"

    chatskij "Молчалин прежде был так глуп!.."

    chatskij "Жалчайшее созданье!"

    chatskij "Уж разве поумнел?.. А тот —"

    chatskij "Хрипун, удавленник, фагот,"

    chatskij "Созвездие манёвров и мазурки!"

    chatskij "Судьба любви — играть ей в жмурки,"

    chatskij "А мне..."

    play sound1 footsteps

    hide chatskij

    show chatskij at left
    show sofija at right

    chatskij "<{i}Входит София.{/i}>"

    hide sofija

    show chatskij at truecenter

    stop sound1

    chatskij "{space=400}Вы здесь? я очень рад,"

    chatskij "Я этого желал."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(про себя){/i}>"

    sofija "{space=400}И очень невпопад."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Конечно не меня искали?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Я не искала вас."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Дознаться мне нельзя ли,"

    chatskij "Хоть и некстати, ну́жды нет,"

    chatskij "Кого вы любите?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Ах! Боже мой! весь свет."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Кто более вам мил?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Есть многие, родные."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Все более меня?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Иные."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "И я чего хочу, когда все решено?"

    chatskij "Мне в петлю лезть, а ей смешно."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Хотите ли знать истины два слова?"

    sofija "Малейшая в ком странность чуть видна,"

    sofija "Веселость ваша не скромна,"

    sofija "У вас тотчас уж острота́ готова,"

    sofija "А сами вы..."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Я сам? не правда ли, смешон?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Да! грозный взгляд, и резкий тон,"

    sofija "И этих в вас особенностей бездна;"

    sofija "А над собой гроза куда не бесполезна."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я странен; а не странен кто ж?"

    chatskij "Тот, кто на всех глупцов похож;"

    chatskij "Молчалин например..."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Примеры мне не новы;"

    sofija "Заметно, что вы желчь на всех излить готовы;"

    sofija "А я, чтоб не мешать, отсюда уклонюсь."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    hide chatskij

    show chatskij at left
    show sofija at right

    chatskij "<{i}(держит ее){/i}>"

    hide sofija

    show chatskij at truecenter

    chatskij "Постойте же!"

    chatskij "<{i}(В сторону.){/i}>"

    chatskij "{space=400}Раз в жизни притворюсь."

    chatskij "<{i}(Громко.){/i}>"

    chatskij "Оставимте мы эти пренья."

    chatskij "Перед Молчалиным не прав я, виноват;"

    chatskij "Быть может, он не то, что три года назад:"

    chatskij "Есть на земле такие превращенья"

    chatskij "Правлений, климатов, и нравов, и умов;"

    chatskij "Есть люди важные, слыли за дураков:"

    chatskij "Иной по армии, иной плохим поэтом,"

    chatskij "Иной... Боюсь назвать, но признано всем светом,"

    chatskij "Особенно в последние года,"

    chatskij "Что стали умны хоть куда."

    chatskij "Пускай в Молчалине ум бойкий, гений смелый;"

    chatskij "Но есть ли в нем та страсть? то чувство?"

    chatskij "{space=400}пылкость та?"

    chatskij "Чтоб кроме вас ему мир целый"

    chatskij "Казался прах и суета?"

    chatskij "Чтоб сердца каждое биенье"

    chatskij "Любовью ускорялось к вам?"

    chatskij "Чтоб мыслям были всем и всем его делам"

    chatskij "Душою — вы, вам угожденье?.."

    chatskij "Сам это чувствую, сказать я не могу,"

    chatskij "Но что теперь во мне кипит, волнует, бесит,"

    chatskij "Не пожелал бы я и личному врагу,"

    chatskij "А он?.. смолчит и голову повесит."

    chatskij "Конечно смирен, все такие не резвы́;"

    chatskij "Бог знает, в нем какая тайна скрыта;"

    chatskij "Бог знает, за него что выдумали вы,"

    chatskij "Чем голова его ввек не была набита."

    chatskij "Быть может качеств ваших тьму,"

    chatskij "Любуясь им, вы придали ему;"

    chatskij "Не грешен он ни в чем, вы во сто раз грешнее."

    chatskij "Нет! нет! пускай умен, час от часу умнее;"

    chatskij "Но вас он стоит ли? вот вам один вопрос;"

    chatskij "Чтоб равнодушнее мне понести утрату,"

    chatskij "Как человеку вы, который с вами взрос,"

    chatskij "Как другу вашему, как брату"

    chatskij "Мне дайте убедиться в том;"

    chatskij "{space=400}Потом"

    chatskij "От сумасшествия могу я остеречься;"

    chatskij "Пущусь подалее простыть, охолодеть,"

    chatskij "Не думать о любви, но буду я уметь"

    chatskij "Теряться по́ свету, забыться и развлечься."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(про себя){/i}>"

    sofija "Вот нехотя с ума свела!"

    sofija "<{i}(Вслух.){/i}>"

    sofija "Что притворяться?"

    sofija "Молчалин давиче мог без руки остаться,"

    sofija "Я живо в нем участье приняла;"

    sofija "А вы, случась на эту пору,"

    sofija "Не позаботились расчесть,"

    sofija "Что можно доброй быть ко всем и без разбору;"

    sofija "Но, может, истина в догадках ваших есть,"

    sofija "И горячо его беру я под защиту:"

    sofija "Зачем же быть, скажу вам напрямик,"

    sofija "Так невоздержну на язык?"

    sofija "В презреньи к людям так нескрыту?"

    sofija "Что и смирнейшему пощады нет!.. чего?"

    sofija "Случись кому назвать его:"

    sofija "Град колкостей и шуток ваших грянет."

    sofija "Шутить! и век шутить! как вас на это станет! —"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Ах! Боже мой! неужли я из тех,"

    chatskij "Которым цель всей жизни — смех?"

    chatskij "Мне весело, когда смешных встречаю,"

    chatskij "А чаще с ними я скучаю."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Напрасно: это все относится к другим,"

    sofija "Молчалин вам наскучил бы едва ли,"

    sofija "Когда б сошлись короче с ним."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(с жаром){/i}>"

    chatskij "Зачем же вы его так коротко узнали?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Я не старалась, бог нас свел."

    sofija "Смотрите, дружбу всех он в доме приобрел:"

    sofija "При батюшке три года служит,"

    sofija "Тот часто бе́з толку сердит,"

    sofija "А он безмолвием его обезоружит,"

    sofija "От доброты души простит;"

    sofija "{space=400}И между прочим,"

    sofija "Веселостей искать бы мог;"

    sofija "Ничуть: от старичков не ступит за порог;"

    sofija "{space=400}Мы ре́звимся, хохочем;"

    sofija "Он с ними целый день засядет, рад не рад,"

    sofija "Играет..."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Целый день играет!"

    chatskij "Молчит, когда его бранят!"

    chatskij "<{i}(В сторону){/i}>"

    chatskij "Она его не уважает."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Конечно, нет в нем этого ума,"

    sofija "Что гений для иных, а для иных чума,"

    sofija "Который скор, блестящ и скоро опротивит,"

    sofija "Который свет ругает наповал,"

    sofija "Чтоб свет об нем хоть что-нибудь сказал;"

    sofija "Да эдакий ли ум семейство осчастливит?"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Сатира и мораль — смысл этого всего?"

    chatskij "<{i}(В сторону.){/i}>"

    chatskij "Она не ставит в грош его."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Чудеснейшего свойства"

    sofija "Он наконец: уступчив, скромен, тих,"

    sofija "В лице ни тени беспокойства"

    sofija "И на душе проступков никаких;"

    sofija "Чужих и вкривь и вкось не рубит, —"

    sofija "Вот я за что его люблю."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(в сторону){/i}>"

    chatskij "Шалит, она его не любит."

    chatskij "<{i}(Вслух.){/i}>"

    chatskij "Докончить я вам пособлю"

    chatskij "Молчалина изображенье."

    chatskij "Но Скалозуб? вот загляденье:"

    chatskij "За армию стоит горой,"

    chatskij "{space=400}И прямизною стана,"

    chatskij "Лицом и голосом герой..."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Не моего романа."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Не вашего? кто разгадает вас?"

    hide chatskij

label Act_3_Scene_2:
    "{b}Явление 2{/b}"

    show chatskij at left
    show sofija at truecenter
    show lizanka at right

    "<{i}Чацкий, София, Лиза.{/i}>"

    hide chatskij
    hide sofija
    hide lizanka

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "<{i}(шепотом){/i}>"

    lizanka "Сударыня, за мной сейчас"

    lizanka "К вам Алексей Степаныч будет."

    hide lizanka

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Простите, надобно идти мне поскорей."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Куда?"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "К прихмахеру."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Бог с ним."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Щипцы простудит."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Пускай себе..."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Нельзя, ждем на́ вечер гостей."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Бог с вами, остаюсь опять с моей загадкой."

    chatskij "Однако дайте мне зайти, хотя украдкой,"

    chatskij "К вам в комнату на несколько минут;"

    chatskij "Там стены, воздух — все приятно!"

    chatskij "Согреют, оживят, мне отдохнуть дадут"

    chatskij "Воспоминания об том, что невозвратно!"

    chatskij "Не засижусь, войду, всего минуты две,"

    chatskij "Потом подумайте, член Английского клуба,"

    chatskij "Я там дни целые пожертвую молве"

    chatskij "Про ум Молчалина, про душу Скалозуба."

    play sound1 footsteps

    hide chatskij

    show sofija at left
    show pervaja_knjazhna at truecenter
    show lizanka at right

    chatskij "<{i}София пожимает плечами, уходит к себе и запирается, за нею и Лиза.{/i}>"

    hide sofija
    hide pervaja_knjazhna
    hide lizanka

    show chatskij at truecenter

    stop sound1

    hide chatskij

label Act_3_Scene_3:
    "{b}Явление 3{/b}"

    show chatskij at left
    show molchalin at right

    "<{i}Чацкий, потом Молчалин.{/i}>"

    hide chatskij
    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Ах! Софья! Неужли Молчалин избран ей!"

    chatskij "А чем не муж? Ума в нем только мало;"

    chatskij "Но чтоб иметь детей,"

    chatskij "Кому ума недоставало?"

    chatskij "Услужлив, скромненький, в лице румянец есть."

    play sound1 footsteps

    hide chatskij

    show chatskij at left
    show molchalin at right

    chatskij "<{i}Входит Молчалин.{/i}>"

    hide molchalin

    show chatskij at truecenter

    stop sound1

    chatskij "Вот он, на цыпочках, и не богат словами;"

    chatskij "Какою ворожбой умел к ней в сердце влезть!"

    hide chatskij

    show chatskij at left
    show molchalin at right

    chatskij "<{i}(Обращается к нему.){/i}>"

    hide molchalin

    show chatskij at truecenter

    chatskij "Нам, Алексей Степаныч, с вами"

    chatskij "Не удалось сказать двух слов."

    chatskij "Ну, образ жизни ваш каков?"

    chatskij "Без горя нынче? без печали?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "По-прежнему-с."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}А прежде как живали?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "День за́ день, нынче как вчера."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "К перу от карт? и к картам от пера?"

    chatskij "И положённый час приливам и отливам?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "По мере я трудов и сил,"

    molchalin "С тех пор, как числюсь по Архивам,"

    molchalin "Три награжденья получил."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Взманили почести и знатность?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Нет-с, свой талант у всех..."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}У вас?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Два-с:"

    molchalin "Умеренность и аккуратность."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Чудеснейшие два! и стоят наших всех."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Вам не дались чины, по службе неуспех?"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Чины людьми даются;"

    chatskij "А люди могут обмануться."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Как удивлялись мы!"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Какое ж диво тут?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Жалели вас."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Напрасный труд."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Татьяна Юрьевна рассказывала что-то,"

    molchalin "Из Петербурга воротясь,"

    molchalin "С министрами про вашу связь,"

    molchalin "Потом разрыв..."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Ей почему забота?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Татьяне Юрьевне!"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Я с нею незнаком."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "С Татьяной Юрьевной!!"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}С ней век мы не встречались;"

    chatskij "Слыхал, что вздорная."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Да это, полно, та ли-с?"

    molchalin "Татьяна Юрьевна!!! Известная, — притом"

    molchalin "Чиновные и должностные"

    molchalin "Все ей друзья и все родные;"

    molchalin "К Татьяне Юрьевне хоть раз бы съездить вам."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "На что же?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Так: частенько там"

    molchalin "Мы покровительство находим, где не метим."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я езжу к женщинам, да только не за этим."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Как обходительна! добра! мила! проста!"

    molchalin "Балы дает нельзя богаче,"

    molchalin "От Рождества и до поста,"

    molchalin "И летом праздники на даче."

    molchalin "Ну, право, что́ бы вам в Москве у нас служить?"

    molchalin "И награжденья брать, и весело пожить?"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Когда в делах, я от веселий прячусь,"

    chatskij "Когда дурачиться: дурачусь;"

    chatskij "А смешивать два эти ремесла"

    chatskij "Есть тьма искусников, я не из их числа."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Простите, впрочем, тут не вижу преступленья;"

    molchalin "Вот сам Фома Фомич, знаком он вам?"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Ну что ж?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "При трех министрах был начальник отделенья;"

    molchalin "Переведен сюда..."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Хорош!"

    chatskij "Пустейший человек из самых бестолковых!"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Как можно! слог его здесь ставят в образец!"

    molchalin "Читали вы?"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Я глупостей не чтец,"

    chatskij "А пуще образцовых."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Нет, мне так довелось с приятностью прочесть,"

    molchalin "Не сочинитель я..."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}И по всему заметно."

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Не смею моего сужденья произнесть."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Зачем же так секретно?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "В мои лета не должно сметь"

    molchalin "Свое суждение иметь."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Помилуйте, мы с вами не ребяты;"

    chatskij "Зачем же мнения чужие только святы?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Ведь надобно ж зависеть от других."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Зачем же надобно?"

    hide chatskij

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}В чинах мы небольших."

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(почти громко){/i}>"

    chatskij "С такими чувствами, с такой душою"

    chatskij "Любим!.. Обманщица смеялась надо мною!"

    hide chatskij

label Act_3_Scene_4:
    "{b}Явление 4{/b}"

    play sound1 door_creak

    show sofija at left
    show sluga_2_3 at truecenter
    show glavnij_sluga at right

    "<{i}Вечер. Все двери настежь, кроме в спальню к Софии. В перспективе раскрывается ряд
            освещенных комнат. Слуги суетятся, один из них, главный, говорит:{/i}>"

    hide sofija
    hide sluga_2_3
    hide glavnij_sluga

    stop sound1

    show glavnij_sluga at truecenter

    $ glavnij_sluga_var = "{noalt}Главный слуга"

    glavnij_sluga "Эй! Филька, Фомка, ну, ловчей!"

    glavnij_sluga "Столы для карт, мел, щеток и свечей!"

    play sound1 knocking
    play sound2 door_creak

    hide glavnij_sluga

    show glavnij_sluga at left
    show sofija at right

    glavnij_sluga "<{i}(Стучится к Софии в дверь.){/i}>"

    hide sofija

    show glavnij_sluga at truecenter

    stop sound1
    stop sound2

    glavnij_sluga "Скажите барышне скорее, Лизавета:"

    glavnij_sluga "Наталья Дмитревна, и с мужем, и к крыльцу"

    glavnij_sluga "Еще подъехала карета."

    hide glavnij_sluga

    show chatskij at truecenter

    "<{i}Расходятся, остается один Чацкий.{/i}>"

    hide chatskij

label Act_3_Scene_5:
    "{b}Явление 5{/b}"

    show chatskij at left
    show natalja_dmitrievna at right

    "<{i}Чацкий, Наталья Дмитриевна, молодая дама.{/i}>"

    hide chatskij
    hide natalja_dmitrievna

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Не ошибаюсь ли!.. он точно, по лицу..."

    natalja_dmitrievna "Ах! Александр Андреич, вы ли?"

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "С сомненьем смотрите от ног до головы;"

    chatskij "Неужли так меня три года изменили?"

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Я полагала вас далёко от Москвы."

    natalja_dmitrievna "Давно ли?"

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Нынче лишь..."

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "{space=400}Надолго?"

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Как случится."

    chatskij "Однако кто, смотря на вас, не подивится!"

    chatskij "Полнее прежнего, похорошели страх."

    chatskij "Моложе вы, свежее стали;"

    chatskij "Огонь, румянец, смех, игра во всех чертах."

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Я замужем."

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Давно бы вы сказали!"

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Мой муж — прелестный муж, вот он сейчас войдет,"

    natalja_dmitrievna "Я познакомлю вас, хотите?"

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Прошу."

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "{space=400}И знаю наперед,"

    natalja_dmitrievna "Что вам понравится. Взгляните и судите!"

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Я верю, он вам муж."

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "{space=400}О нет-с, не потому;"

    natalja_dmitrievna "Сам по себе, по нраву, по уму."

    natalja_dmitrievna "Платон Михайлыч мой единственный, бесценный!"

    natalja_dmitrievna "Теперь в отставке, был военный;"

    natalja_dmitrievna "И утверждают все, кто только прежде знал,"

    natalja_dmitrievna "Что с храбростью его, с талантом,"

    natalja_dmitrievna "Когда бы службу продолжал,"

    natalja_dmitrievna "Конечно был бы он московским комендантом."

    hide natalja_dmitrievna

label Act_3_Scene_6:
    "{b}Явление 6{/b}"

    show chatskij at left
    show natalja_dmitrievna at truecenter
    show platon_mihajlovich at right

    "<{i}Чацкий, Наталья Дмитриевна, Платон Михайлович.{/i}>"

    hide chatskij
    hide natalja_dmitrievna
    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Вот мой Платон Михайлыч."

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Ба!"

    chatskij "Друг старый, мы давно знакомы, вот судьба!"

    hide chatskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "Здорово, Чацкий, брат!"

    hide platon_mihajlovich

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Платон любезный, славно."

    chatskij "Похвальный лист тебе: ведешь себя исправно."

    hide chatskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "Как видишь, брат:"

    platon_mihajlovich "Московский житель и женат."

    hide platon_mihajlovich

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Забыт шум лагерный, товарищи и братья?"

    chatskij "Спокоен и ленив?"

    hide chatskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "{space=400}Нет, есть-таки занятья:"

    platon_mihajlovich "На флейте я твержу дуэт"

    platon_mihajlovich "А-мольный..."

    hide platon_mihajlovich

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Что твердил назад тому пять лет?"

    chatskij "Ну, постоянный вкус! в мужьях всего дороже!"

    hide chatskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "Брат, женишься, тогда меня вспомянь!"

    platon_mihajlovich "От скуки будешь ты свистеть одно и то же."

    hide platon_mihajlovich

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "От скуки! как? уж ты ей платишь дань?"

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Платон Михайлыч мой к занятьям склонен разным,"

    natalja_dmitrievna "Которых нет теперь; к ученьям и смотрам,"

    natalja_dmitrievna "К манежу... иногда скучает по утрам."

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "А кто, любезный друг, велит тебе быть праздным?"

    chatskij "В полк, эскадрон дадут. Ты обер или штаб?"

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Платон Михайлыч мой здоровьем очень слаб."

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Здоровьем слаб! Давно ли?"

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Все рюматизм и головные боли."

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Движенья более. В деревню, в теплый край."

    chatskij "Будь чаще на коне. Деревня летом — рай."

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Платон Михайлыч город любит,"

    natalja_dmitrievna "Москву; за что в глуши он дни свои погубит!"

    hide natalja_dmitrievna

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Москву и город... Ты чудак!"

    chatskij "А помнишь прежнее?"

    hide chatskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "{space=400}Да, брат, теперь не так..."

    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Ах! мой дружочик!"

    natalja_dmitrievna "Здесь так свежо, что мочи нет,"

    natalja_dmitrievna "Ты распахнулся весь, и расстегнул жилет."

    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "Теперь, брат, я не тот..."

    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "{space=400}Послушайся разочек,"

    natalja_dmitrievna "Мой милый, застегнись скорей."

    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "<{i}(хладнокровно){/i}>"

    platon_mihajlovich "Сейчас."

    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Да отойди подальше от дверей,"

    natalja_dmitrievna "Сквозной там ветер дует сзади!"

    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "Теперь, брат, я не тот..."

    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "{space=400}Мой ангел, бога ради"

    natalja_dmitrievna "От двери дальше отойди."

    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "<{i}(глаза к небу){/i}>"

    platon_mihajlovich "Ах! матушка!"

    hide platon_mihajlovich

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Ну, бог тебя суди;"

    chatskij "Уж точно, стал не тот в короткое ты время;"

    chatskij "Не в прошлом ли году, в конце,"

    chatskij "В полку тебя я знал? лишь утро: ногу в стремя"

    chatskij "И носишься на борзом жеребце;"

    chatskij "Осенний ветер дуй, хоть спереди, хоть с тыла."

    hide chatskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    play sound1 male_sigh

    platon_mihajlovich "<{i}(со вздохом){/i}>"

    stop sound1

    platon_mihajlovich "Эх! братец! славное тогда житье-то было."

    hide platon_mihajlovich

label Act_3_Scene_7:
    "{b}Явление 7{/b}"

    show knjaz at left
    show knjaginja at truecenter
    show sofija at right

    "<{i}Те же, Князь Тугоуховский и Княгиня с шестью дочерьми.{/i}>"

    hide knjaz
    hide knjaginja
    hide sofija

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "<{i}(тоненьким голоском){/i}>"

    natalja_dmitrievna "Князь Петр Ильич, княгиня! боже мой!"

    natalja_dmitrievna "Княжна Зизи! Мими!"

    hide natalja_dmitrievna

    play sound1 kisses

    "<{i}Громкие лобызания, потом усаживаются и осматривают одна другую с головы до
            ног.{/i}>"

    stop sound1

    show pervaja_knjazhna at truecenter

    $ pervaja_knjazhna_var = "{noalt}1-я княжна"

    pervaja_knjazhna "{space=400}Какой фасон прекрасный!"

    hide pervaja_knjazhna

    show vtoraja_knjazhna at truecenter

    $ vtoraja_knjazhna_var = "{noalt}2-я княжна"

    vtoraja_knjazhna "Какие складочки!"

    hide vtoraja_knjazhna

    show pervaja_knjazhna at truecenter

    $ pervaja_knjazhna_var = "{noalt}1-я княжна"

    pervaja_knjazhna "{space=400}Обшито бахромой."

    hide pervaja_knjazhna

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Нет, если б видели, мой тюрлюрлю атласный!"

    hide natalja_dmitrievna

    show tretja_knjazhna at truecenter

    $ tretja_knjazhna_var = "{noalt}3-я княжна"

    tretja_knjazhna "Какой эшарп cousin мне подарил!"

    hide tretja_knjazhna

    show chetviortaja_knjazhna at truecenter

    $ chetviortaja_knjazhna_var = "{noalt}4-я княжна"

    chetviortaja_knjazhna "Ах! да, барежевый!"

    hide chetviortaja_knjazhna

    show pjataja_knjazhna at truecenter

    $ pjataja_knjazhna_var = "{noalt}5-я княжна"

    pjataja_knjazhna "{space=400}Ах прелесть!"

    hide pjataja_knjazhna

    show shestaja_knjazhna at truecenter

    $ shestaja_knjazhna_var = "{noalt}6-я княжна"

    shestaja_knjazhna "{space=400}Ах! как мил!"

    hide shestaja_knjazhna

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "Сс! — Кто это в углу, взошли мы, поклонился?"

    hide knjaginja

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Приезжий, Чацкий."

    hide natalja_dmitrievna

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "{space=400}От-став-ной?"

    hide knjaginja

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Да, путешествовал, недавно воротился."

    hide natalja_dmitrievna

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "И хо-ло-стой?"

    hide knjaginja

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Да, не женат."

    hide natalja_dmitrievna

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "{space=400}Князь, князь, сюда. Живее!"

    hide knjaginja

    show knjaz at truecenter

    $ knjaz_var = "{noalt}Князь"

    hide knjaz

    show knjaz at left
    show knjaginja at right

    knjaz "<{i}(к ней оборачивает слуховую трубку){/i}>"

    hide knjaginja

    show knjaz at truecenter

    knjaz "О-хм!"

    hide knjaz

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "К нам на́ вечер, в четверг, проси скорее"

    knjaginja "Натальи Дмитревны знакомого: вон он!"

    hide knjaginja

    show knjaz at truecenter

    $ knjaz_var = "{noalt}Князь"

    knjaz "И-хм!"

    play sound1 footsteps
    play sound2 male_cough

    hide knjaz

    show knjaz at left
    show chatskij at right

    knjaz "<{i}(Отправляется, вьется около Чацкого и покашливает){/i}>"

    hide chatskij

    show knjaz at truecenter

    stop sound1
    stop sound2

    hide knjaz

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "{space=400}Вот то-то, детки:"

    knjaginja "Им бал, а батюшка таскайся на поклон;"

    knjaginja "Танцовщики ужасно стали редки!.."

    knjaginja "Он камер-юнкер?"

    hide knjaginja

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "{space=400}Нет."

    hide natalja_dmitrievna

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "{space=400}Бо-гат?"

    hide knjaginja

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "О нет!"

    hide natalja_dmitrievna

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "<{i}(громко, что есть мочи){/i}>"

    knjaginja "{space=400}Князь, князь! Назад!"

    hide knjaginja

label Act_3_Scene_8:
    "{b}Явление 8{/b}"

    show grafinja_vnuchka at left
    show grafinja_babushka at right

    "<{i}Те же и Графини Хрюмины: бабушка и внучка.{/i}>"

    hide grafinja_vnuchka
    hide grafinja_babushka

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "Ax! grand' maman! Ну, кто так рано приезжает?"

    grafinja_vnuchka "Мы первые!"

    grafinja_vnuchka "<{i}(Пропадает в боковую комнату.){/i}>"

    hide grafinja_vnuchka

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "{space=400}Вот нас честит!"

    knjaginja "Вот первая, и нас за никого считает!"

    knjaginja "Зла, в девках целый век, уж бог ее простит."

    hide knjaginja

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    hide grafinja_vnuchka

    show grafinja_vnuchka at left
    show chatskij at right

    grafinja_vnuchka "<{i}(вернувшись, направляет на Чацкого двойной лорнет){/i}>"

    hide chatskij

    show grafinja_vnuchka at truecenter

    grafinja_vnuchka "Мсье Чацкий! вы в Москве! как были, всё такие?"

    hide grafinja_vnuchka

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "На что меняться мне?"

    hide chatskij

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Вернулись холостые?"

    hide grafinja_vnuchka

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "На ком жениться мне?"

    hide chatskij

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}В чужих краях на ком?"

    grafinja_vnuchka "О! наших тьма без дальних справок"

    grafinja_vnuchka "Там женятся, и нас дарят родством"

    grafinja_vnuchka "С искусницами модных лавок."

    hide grafinja_vnuchka

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Несчастные! должны ль упреки несть"

    chatskij "От подражательниц модисткам?"

    chatskij "За то, что смели предпочесть"

    chatskij "Оригиналы спискам?"

    hide chatskij

label Act_3_Scene_9:
    "{b}Явление 9{/b}"

    play sound1 footsteps

    show zagoretskij at left
    show sofija at right

    "<{i}Те же и множество других гостей. Между прочим Загорецкий. Мужчины являются,
            шаркают, отходят в сторону, кочуют из комнаты в комнату и проч. София от себя выходит,
            все к ней навстречу.{/i}>"

    hide zagoretskij
    hide sofija

    stop sound1

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "Eh! bon soir! vous voilà! Jamais trop diligente,"

    grafinja_vnuchka "Vous nous donnez toujours le plaisir de l'attente."

    hide grafinja_vnuchka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "На завтрашний спектакль имеете билет?"

    hide zagoretskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Нет."

    hide sofija

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Позвольте вам вручить, напрасно бы кто взялся"

    zagoretskij "Другой вам услужить, зато"

    zagoretskij "Куда я ни кидался!"

    zagoretskij "В контору — все взято,"

    zagoretskij "К директору — он мне приятель, —"

    zagoretskij "С зарей в шестом часу, и кстати ль!"

    zagoretskij "Уж с вечера никто достать не мог;"

    zagoretskij "К тому, к сему, всех сбил я с ног;"

    zagoretskij "И этот наконец похитил уже силой"

    zagoretskij "У одного, старик он хилый,"

    zagoretskij "Мне друг, известный домосед;"

    zagoretskij "Пусть дома просидит в покое."

    hide zagoretskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Благодарю вас за билет,"

    sofija "А за старанье вдвое."

    hide sofija

    play sound1 footsteps

    show zagoretskij at truecenter

    "<{i}Являются еще кое-какие, тем временем Загорецкий отходит к мужчинам.{/i}>"

    hide zagoretskij

    stop sound1

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Платон Михайлыч..."

    hide zagoretskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "{space=400}Прочь!"

    platon_mihajlovich "Поди ты к женщинам, лги им, и их морочь;"

    platon_mihajlovich "Я правду об тебе порасскажу такую,"

    platon_mihajlovich "Что хуже всякой лжи. Вот, брат,"

    hide platon_mihajlovich

    show platon_mihajlovich at left
    show chatskij at right

    platon_mihajlovich "<{i}(Чацкому){/i}>"

    hide chatskij

    show platon_mihajlovich at truecenter

    platon_mihajlovich "{space=400}рекомендую!"

    platon_mihajlovich "Как эдаких людей учтивее зовут,"

    platon_mihajlovich "Нежнее? — человек он светский,"

    platon_mihajlovich "Отъявленный мошенник, плут:"

    platon_mihajlovich "Антон Антоныч Загорецкий."

    platon_mihajlovich "При нем остерегись: переносить горазд,"

    platon_mihajlovich "И в карты не садись: продаст."

    hide platon_mihajlovich

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Оригинал! брюзглив, а без малейшей злобы."

    hide zagoretskij

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "И оскорбляться вам смешно бы,"

    chatskij "Окроме честности, есть множество отрад:"

    chatskij "Ругают здесь, а там благодарят."

    hide chatskij

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "Ох, нет, братец! у нас ругают"

    platon_mihajlovich "Везде, а всюду принимают."

    hide platon_mihajlovich

    show zagoretskij at truecenter

    "<{i}Загорецкий мешается в толпу.{/i}>"

    hide zagoretskij

label Act_3_Scene_10:
    "{b}Явление 10{/b}"

    show hlestova at truecenter

    "<{i}Те же и Хлёстова.{/i}>"

    hide hlestova

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Легко ли в шестьдесят пять лет"

    hlestova "Тащиться мне к тебе, племянница?.. мученье!"

    hlestova "Час битый ехала с Покровки, силы нет;"

    hlestova "Ночь — света преставленье!"

    hlestova "От скуки я взяла с собой"

    hlestova "Арапку-девку да собачку, —"

    hlestova "Вели их накормить, ужо, дружочик мой;"

    hlestova "От ужина сошли подачку."

    hlestova "Княгиня, здравствуйте!"

    hlestova "<{i}(Села.){/i}>"

    hlestova "{space=400}Ну, Софьюшка, мой друг,"

    hlestova "Какая у меня арапка для услуг,"

    hlestova "Курчавая! горбом лопатки!"

    hlestova "Сердитая! все кошачьи ухватки!"

    hlestova "Да как черна! да как страшна!"

    hlestova "Ведь создал же господь такое племя!"

    hlestova "Черт сущий; в девичей она;"

    hlestova "Позвать ли?"

    hide hlestova

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Нет-с; в другое время."

    hide sofija

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Представь: их, как зверей, выводят напоказ,"

    hlestova "Я слышала, там... город есть турецкий..."

    hlestova "А знаешь ли, кто мне припас?"

    hlestova "Антон Антоныч Загорецкий."

    hide hlestova

    show hlestova at left
    show zagoretskij at right

    hlestova "<{i}Загорецкий выставляется вперед.{/i}>"

    hide zagoretskij

    show hlestova at truecenter

    hlestova "Лгунишка он, картежник, вор."

    hide hlestova

    show hlestova at left
    show zagoretskij at right

    hlestova "<{i}Загорецкий исчезает.{/i}>"

    hide zagoretskij

    show hlestova at truecenter

    hlestova "Я от него было и двери на запор;"

    hlestova "Да мастер услужить: мне и сестре Прасковье"

    hlestova "Двоих ара́пченков на ярмонке достал;"

    hlestova "Купил, он говорит, чай в карты сплутовал;"

    hlestova "А мне подарочек, дай бог ему здоровье!"

    hide hlestova

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    play sound1 male_laughter

    hide chatskij

    show chatskij at left
    show platon_mihajlovich at right

    chatskij "<{i}(с хохотом Платону Михайловичу){/i}>"

    hide platon_mihajlovich

    show chatskij at truecenter

    stop sound1

    chatskij "Не поздоровится от эдаких похвал,"

    chatskij "И Загорецкий сам не выдержал, пропал."

    hide chatskij

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Кто этот весельчак? Из звания какого?"

    hide hlestova

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Вон этот? Чацкий."

    hide sofija

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "{space=400}Ну? а что нашел смешного?"

    hlestova "Чему он рад? Какой тут смех?"

    hlestova "Над старостью смеяться грех."

    hlestova "Я помню, ты дитёй с ним часто танцевала,"

    hlestova "Я за уши его дирала, только мало."

    hide hlestova

label Act_3_Scene_11:
    "{b}Явление 11{/b}"

    show famusov at truecenter

    "<{i}Те же и Фамусов.{/i}>"

    hide famusov

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "<{i}(громогласно){/i}>"

    famusov "Ждем князя Пётра Ильича,"

    famusov "А князь уж здесь! А я забился там, в портретной."

    famusov "Где Скалозуб Сергей Сергеич? а?"

    famusov "Нет; кажется, что нет. — Он человек заметный —"

    famusov "Сергей Сергеич Скалозуб."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Творец мой! оглушил, звончее всяких труб!"

    hide hlestova

label Act_3_Scene_12:
    "{b}Явление 12{/b}"

    show skalozub at left
    show molchalin at right

    "<{i}Те же и Скалозуб, потом Молчалин.{/i}>"

    hide skalozub
    hide molchalin

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Сергей Сергеич, запоздали;"

    famusov "А мы вас ждали, ждали, ждали."

    play sound1 footsteps

    hide famusov

    show famusov at left
    show hlestova at right

    famusov "<{i}(Подводит к Хлёстовой){/i}>"

    hide hlestova

    show famusov at truecenter

    stop sound1

    famusov "Моя невестушка, которой уж давно"

    famusov "Об вас говорено."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "<{i}(сидя){/i}>"

    hlestova "Вы прежде были здесь... в полку... в том..."

    hlestova "{space=400}в гренадерском?"

    hide hlestova

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "<{i}(басом){/i}>"

    skalozub "В его высочества, хотите вы сказать,"

    skalozub "Ново-землянском мушкетерском."

    hide skalozub

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Не мастерица я полки-то различать."

    hide hlestova

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "А форменные есть отлички:"

    skalozub "В мундирах выпушки, погончики, петлички."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Пойдемте, батюшка, там вас я насмешу,"

    famusov "Курьезный вист у нас. За нами, князь! прошу."

    play sound1 footsteps

    hide famusov

    show famusov at left
    show knjaz at right

    famusov "<{i}(Его и князя уводит с собою.){/i}>"

    hide knjaz

    show famusov at truecenter

    stop sound1

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hide hlestova

    show hlestova at left
    show sofija at right

    hlestova "<{i}(Софии){/i}>"

    hide sofija

    show hlestova at truecenter

    hlestova "Ух! я точнехонько избавилась от петли;"

    hlestova "Ведь полоумный твой отец;"

    hlestova "Дался ему трех сажень удалец, —"

    hlestova "Знакомит, не спросясь, приятно ли нам, нет ли!"

    hide hlestova

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    hide molchalin

    show molchalin at left
    show hlestova at right

    molchalin "<{i}(подает ей карту){/i}>"

    hide hlestova

    show molchalin at truecenter

    molchalin "Я вашу партию составил: мосьё Кок,"

    molchalin "Фома Фомич и я."

    hide molchalin

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "{space=400}Спасибо, мой дружок."

    hlestova "<{i}(Встает.){/i}>"

    hide hlestova

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Ваш шпиц — прелестный шпиц, не более наперстка,"

    molchalin "Я гладил все его; как шелковая шерстка!"

    hide molchalin

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Спасибо, мой родной!"

    hide hlestova

    play sound1 footsteps

    show hlestova at left
    show molchalin at right

    "<{i}Уходит, за ней Молчалин и многие другие.{/i}>"

    hide hlestova
    hide molchalin

    stop sound1

label Act_3_Scene_13:
    "{b}Явление 13{/b}"

    show chatskij at left
    show sofija at right

    "<{i}Чацкий, София и несколько посторонних, которые в продолжении расходятся.{/i}>"

    hide chatskij
    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Ну! тучу разогнал..."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Нельзя ль не продолжать?"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Чем вас я напугал?"

    chatskij "За то, что он смягчил разгневанную гостью,"

    chatskij "Хотел я похвалить."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}А кончили бы злостью."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Сказать вам, что я думал? Вот:"

    chatskij "Старушки все народ сердитый;"

    chatskij "Не худо, чтоб при них услужник знаменитый"

    chatskij "Тут был, как громовой отвод."

    chatskij "Тут был, как громовой отвод."

    chatskij "Молчалин! — Кто другой так мирно всё уладит!"

    chatskij "Там моську вовремя погладит,"

    chatskij "Тут в пору карточку вотрет,"

    chatskij "В нем Загорецкий не умрет!"

    chatskij "Вы давиче его мне исчисляли свойства,"

    chatskij "Но многие забыли? — Да?"

    play sound1 footsteps

    chatskij "<{i}(Уходит.){/i}>"

    stop sound1

    hide chatskij

label Act_3_Scene_14:
    "{b}Явление 14{/b}"

    show sofija at left
    show gd at right

    "<{i}София, потом г. N.{/i}>"

    hide sofija
    hide gd

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(про себя){/i}>"

    sofija "Ах! этот человек всегда"

    sofija "Причиной мне ужасного расстройства!"

    sofija "Унизить рад, кольнуть; завистлив, горд и зол!"

    hide sofija

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    play sound1 footsteps

    gn "<{i}(подходит){/i}>"

    stop sound1

    gn "{space=400}Вы в размышленье."

    hide gn

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Об Чацком."

    hide sofija

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "{space=400}Как его нашли по возвращеньи?"

    hide gn

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Он не в своем уме."

    hide sofija

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "{space=400}Ужли с ума сошел?"

    hide gn

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(помолчавши){/i}>"

    sofija "Не то, чтобы совсем..."

    hide sofija

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "{space=400}Однако есть приметы?"

    hide gn

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    hide sofija

    show sofija at left
    show gn at right

    sofija "<{i}(смотрит на него пристально){/i}>"

    hide gn

    show sofija at truecenter

    sofija "Мне кажется."

    hide sofija

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "{space=400}Как можно, в эти леты!"

    hide gn

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Как быть!"

    sofija "<{i}(В сторону.){/i}>"

    sofija "{space=400}Готов он верить!"

    sofija "А, Чацкий! Любите вы всех в шуты рядить,"

    sofija "Угодно ль на себе примерить?"

    play sound1 footsteps

    sofija "<{i}(Уходит.){/i}>"

    stop sound1

    hide sofija

label Act_3_Scene_15:
    "{b}Явление 15{/b}"

    show gd at truecenter

    "<{i}Г. N., потом г. D.{/i}>"

    hide gd

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "С ума сошел!.. Ей кажется... вот на!"

    gn "Недаром? Стало быть... с чего б взяла она!"

    gn "Ты слышал?"

    hide gn

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "{space=400}Что?"

    hide gd

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "{space=400}Об Чацком?"

    hide gn

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "{space=400}Что такое?"

    hide gd

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "С ума сошел!"

    hide gn

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "{space=400}Пустое."

    hide gd

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "Не я сказал, другие говорят."

    hide gn

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "А ты расславить это рад?"

    hide gd

    show gn at truecenter

    $ gn_var = "{noalt}Г. N."

    gn "Пойду, осведомлюсь; чай кто-нибудь да знает."

    play sound1 footsteps

    gn "<{i}(Уходит.){/i}>"

    stop sound1

    hide gn

label Act_3_Scene_16:
    "{b}Явление 16{/b}"

    show gd at left
    show zagoretskij at right

    "<{i}Г. D., потом Загорецкий.{/i}>"

    hide gd
    hide zagoretskij

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "Верь болтуну!"

    gd "Услышит вздор, и тотчас повторяет!"

    gd "Ты знаешь ли об Чацком?"

    hide gd

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "{space=400}Ну?"

    hide zagoretskij

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "С ума сошел!"

    hide gd

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "{space=400}А! знаю, помню, слышал."

    zagoretskij "Как мне не знать? примерный случай вышел;"

    zagoretskij "Его в безумные упрятал дядя-плут..."

    zagoretskij "Схватили, в желтый дом, и на́ цепь посадили."

    hide zagoretskij

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "Помилуй, он сейчас здесь в комнате был, тут."

    hide gd

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Так с цепи, стало быть, спустили."

    hide zagoretskij

    show gd at truecenter

    $ gd_var = "{noalt}Г. D."

    gd "Ну, милый друг, с тобой не надобно газет,"

    gd "Пойду-ка я, расправлю крылья,"

    gd "У всех повыспрошу; однако, чур! секрет."

    play sound1 footsteps

    gd "<{i}(Уходит.){/i}>"

    stop sound1

    hide gd

label Act_3_Scene_17:
    "{b}Явление 17{/b}"

    show zagoretskij at left
    show grafinja_vnuchka at right

    "<{i}Загорецкий, потом графиня внучка.{/i}>"

    hide zagoretskij
    hide grafinja_vnuchka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Который Чацкий тут? — Известная фамилья."

    zagoretskij "С каким-то Чацким я когда-то был знаком."

    zagoretskij "Вы слышали об нем?"

    hide zagoretskij

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Об ком?"

    hide grafinja_vnuchka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Об Чацком, он сейчас здесь в комнате был."

    hide zagoretskij

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Знаю."

    grafinja_vnuchka "Я говорила с ним."

    hide grafinja_vnuchka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "{space=400}Так я вас поздравляю:"

    zagoretskij "Он сумасшедший..."

    hide zagoretskij

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Что?"

    hide grafinja_vnuchka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "{space=400}Да, он сошел с ума."

    hide zagoretskij

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "Представьте, я заметила сама;"

    grafinja_vnuchka "И хоть пари держать, со мной в одно вы слово."

    hide grafinja_vnuchka

label Act_3_Scene_18:
    "{b}Явление 18{/b}"

    show grafinja_vnuchka at left
    show grafinja_babushka at right

    "<{i}Те же и Графиня бабушка.{/i}>"

    hide grafinja_vnuchka
    hide grafinja_babushka

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "Ah! grand'maman, вот чудеса! вот ново!"

    grafinja_vnuchka "Вы не слыхали здешних бед?"

    grafinja_vnuchka "Послушайте. Вот прелести! вот мило!.."

    hide grafinja_vnuchka

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "Мой труг, мне уши залошило;"

    grafinja_babushka "Скаши покромче..."

    hide grafinja_babushka

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Время нет!"

    hide grafinja_vnuchka

    show grafinja_vnuchka at left
    show zagoretskij at right

    grafinja_vnuchka "<{i}(Указывает на Загорецкого.){/i}>"

    hide zagoretskij

    show grafinja_vnuchka at truecenter

    grafinja_vnuchka "{space=400}Il vous dira toute I'histoire."

    grafinja_vnuchka "Пойду, спрошу..."

    play sound1 footsteps

    grafinja_vnuchka "<{i}(Уходит.){/i}>"

    stop sound1

    hide grafinja_vnuchka

label Act_3_Scene_19:
    "{b}Явление 19{/b}"

    show zagoretskij at left
    show grafinja_vnuchka at truecenter
    show grafinja_babushka at right

    "<{i}Загорецкий, графиня бабушка.{/i}>"

    hide zagoretskij
    hide grafinja_vnuchka
    hide grafinja_babushka

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "{space=400}Что? что? уж нет ли здесь пошара?"

    hide grafinja_babushka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Нет, Чацкий произвел всю эту кутерьму."

    hide zagoretskij

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "Как, Чацкого? Кто свел в тюрьму?"

    hide grafinja_babushka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "В горах изранен в лоб, сошел с ума от раны."

    hide zagoretskij

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "Что? К фармазанам в клоб? Пошел он в пусурманы?"

    hide grafinja_babushka

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Ее не вразумишь."

    play sound1 footsteps

    zagoretskij "<{i}(Уходит.){/i}>"

    stop sound1

    hide zagoretskij

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "{space=400}Антон Антоныч! Ах!"

    grafinja_babushka "И он пешит, все в страхе, впопыхах."

    hide grafinja_babushka

label Act_3_Scene_20:
    "{b}Явление 20{/b}"

    show grafinja_vnuchka at left
    show grafinja_babushka at truecenter
    show knjaz at right

    "<{i}Графиня бабушка и Князь Тугоуховский.{/i}>"

    hide grafinja_vnuchka
    hide grafinja_babushka
    hide knjaz

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "Князь, князь! Ох, этот князь, по палам, сам чуть"

    grafinja_babushka "{space=400}тышит!"

    grafinja_babushka "Князь, слышали?"

    hide grafinja_babushka

    show knjaz at truecenter

    $ knjaz_var = "{noalt}Князь"

    knjaz "{space=400}А-хм?"

    hide knjaz

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "{space=400}Он ничего не слышит!"

    grafinja_babushka "Хоть, мошет видели, здесь полицмейстер пыл?"

    hide grafinja_babushka

    show knjaz at truecenter

    $ knjaz_var = "{noalt}Князь"

    knjaz "Э-хм?"

    hide knjaz

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "В тюрьму-та, князь, кто Чацкого схватил?"

    hide grafinja_babushka

    show knjaz at truecenter

    $ knjaz_var = "{noalt}Князь"

    knjaz "И-хм?"

    hide knjaz

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "{space=400}Тесак ему, да ранец,"

    grafinja_babushka "В солтаты! Шутка ли! переменил закон!"

    hide grafinja_babushka

    show knjaz at truecenter

    $ knjaz_var = "{noalt}Князь"

    knjaz "У-хм?"

    hide knjaz

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "Да!.. в пусурманах он!"

    grafinja_babushka "Ах! окаянный волтерьянец!"

    grafinja_babushka "Что? а? Глух, мой отец; достаньте свой рошок."

    grafinja_babushka "Ох! глухота польшой порок."

    hide grafinja_babushka

label Act_3_Scene_21:
    "{b}Явление 21{/b}"

    show zagoretskij at left
    show skalozub at truecenter
    show famusov at right

    "<{i}Те же и Хлёстова, София, Молчалин, Платон Михайлович, Наталья Дмитриевна, Графиня
            внучка, Княгиня с дочерьми, Загорецкий, Скалозуб, потом Фамусов и многие другие.{/i}>"

    hide hlestova
    hide sofija
    hide molchalin
    hide platon_mihajlovich
    hide natalja_dmitrievna
    hide grafinja_vnuchka
    hide knjaginja
    hide zagoretskij
    hide skalozub
    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "С ума сошел! прошу покорно!"

    hlestova "Да невзначай! да как проворно!"

    hlestova "Ты, Софья, слышала?"

    hide hlestova

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "{space=400}Кто первый разгласил?"

    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Ах, друг мой, все!"

    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "{space=400}Ну, все, так верить поневоле,"

    platon_mihajlovich "А мне сомнительно."

    hide platon_mihajlovich

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    play sound1 footsteps

    famusov "<{i}(входя){/i}>"

    stop sound1

    famusov "{space=400}О чем? о Чацком, что ли?"

    famusov "Чего сомнительно? Я первый, я открыл!"

    famusov "Давно дивлюсь я, как никто его не свяжет!"

    famusov "Попробуй о властях, и невесть что наскажет!"

    famusov "Чуть низко поклонись, согнись-ка кто кольцом,"

    famusov "Хоть пред монаршиим лицом,"

    famusov "Так назовет он подлецом!.."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Туда же из смешливых;"

    hlestova "Сказала что-то я — он начал хохотать."

    hide hlestova

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Мне отсоветовал в Москве служить в Архивах."

    hide molchalin

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "Меня модисткою изволил величать!"

    hide grafinja_vnuchka

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "А мужу моему совет дал жить в деревне."

    hide natalja_dmitrievna

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Безумный по всему."

    hide zagoretskij

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Я видела из глаз."

    hide grafinja_vnuchka

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "По матери пошел, по Анне Алексевне;"

    famusov "Покойница с ума сходила восемь раз."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "На свете дивные бывают приключенья!"

    hlestova "В его лета с ума спрыгну́л!"

    hlestova "Чай, пил не по летам."

    hide hlestova

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "{space=400}О! верно..."

    hide knjaginja

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Без сомненья."

    hide grafinja_vnuchka

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Шампанское стаканами тянул."

    hide hlestova

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Бутылками-с, и пребольшими."

    hide natalja_dmitrievna

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "<{i}(с жаром){/i}>"

    zagoretskij "Нет-с, бочками сороковыми."

    hide zagoretskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Ну вот! великая беда,"

    famusov "Что выпьет лишнее мужчина!"

    famusov "Ученье — вот чума, ученость — вот причина,"

    famusov "Что нынче, пуще, чем когда,"

    famusov "Безумных развелось людей, и дел, и мнений."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "И впрямь с ума сойдешь от этих, от одних"

    hlestova "От пансионов, школ, лицеев, как бишь их;"

    hlestova "Да от ланкартачных взаимных обучений."

    hide hlestova

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "Нет, в Петербурге институт"

    knjaginja "Пе-да-го-гический, так, кажется, зовут:"

    knjaginja "Там упражняются в расколах и в безверьи,"

    knjaginja "Профессоры!! — У них учился наш родня,"

    knjaginja "И вышел! хоть сейчас в аптеку, в подмастерьи."

    knjaginja "От женщин бегает, и даже от меня!"

    knjaginja "Чинов не хочет знать! Он химик, он ботаник,"

    knjaginja "Князь Федор, мой племянник."

    hide knjaginja

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Я вас обрадую: всеобщая молва,"

    skalozub "Что есть проект насчет лицеев, школ, гимназий;"

    skalozub "Там будут лишь учить по нашему: раз, два;"

    skalozub "А книги сохранят так: для больших оказий."

    hide skalozub

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Сергей Сергеич, нет! Уж коли зло пресечь:"

    famusov "Забрать все книги бы, да сжечь."

    hide famusov

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Нет-с, книги книгам рознь. А если б, между нами,"

    zagoretskij "Был ценсором назначен я,"

    zagoretskij "На басни бы налег; ох! басни — смерть моя!"

    zagoretskij "Насмешки вечные над львами! над орлами!"

    zagoretskij "Кто что ни говори:"

    zagoretskij "Хотя животные, а все-таки цари."

    hide zagoretskij

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Отцы мои, уж кто в уме расстроен,"

    hlestova "Так все равно, от книг ли, от питья ль,"

    hlestova "А Чацкого мне жаль."

    hlestova "По-христиански так, он жалости достоин,"

    hlestova "Был острый человек, имел душ сотни три."

    hide hlestova

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Четыре."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "{space=400}Три, суда́рь."

    hide hlestova

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "{space=400}Четыреста."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "{space=400}Нет! триста."

    hide hlestova

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "В моем календаре..."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "{space=400}Всё врут календари."

    hide hlestova

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Как раз четыреста, ох! спорить голосиста!"

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Нет! триста! — уж чужих имений мне не знать!"

    hide hlestova

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Четыреста, прошу понять."

    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Нет! триста, триста, триста."

    hide hlestova

label Act_3_Scene_22:
    "{b}Явление 22{/b}"

    show chatskij at truecenter

    "<{i}Те же все и Чацкий.{/i}>"

    hide chatskij

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Вот он."

    hide natalja_dmitrievna

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "{space=400}Шш!"

    hide grafinja_vnuchka

    show zagoretskij at left
    show skalozub at truecenter
    show famusov at right

    $ zagoretskij_var = "{noalt}Все"

    zagoretskij "{space=400}Шш!"

    zagoretskij "<{i}(Пятятся от него в противную сторону.){/i}>"

    hide zagoretskij
    hide skalozub
    hide famusov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "{space=400}Ну как с безумных глаз"

    hlestova "Затеет драться он, потребует к разделке!"

    hide hlestova

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "О господи! помилуй грешных нас!"

    famusov "<{i}(Опасливо.){/i}>"

    famusov "Любезнейший! Ты не в своей тарелке."

    famusov "С дороги нужен сон. Дай пульс. Ты нездоров."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Да, мочи нет: мильон терзаний"

    chatskij "Груди от дружеских тисков,"

    chatskij "Ногам от шарканья, ушам от восклицаний,"

    chatskij "А пуще голове от всяких пустяков."

    play sound1 footsteps

    hide chatskij

    show chatskij at left
    show sofija at right

    chatskij "<{i}(Подходит к Софье.){/i}>"

    hide sofija

    show chatskij at truecenter

    stop sound1

    chatskij "Душа здесь у меня каким-то горем сжата,"

    chatskij "И в многолюдстве я потерян, сам не свой."

    chatskij "Нет! недоволен я Москвой."

    hide chatskij

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Москва, вишь, виновата."

    hide hlestova

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Подальше от него."

    hide famusov

    show famusov at left
    show sofija at right

    famusov "<{i}(Делает знак Софии.){/i}>"

    hide sofija

    show famusov at truecenter

    famusov "{space=400}Гм, Софья! — Не глядит!"

    hide famusov

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    hide sofija

    show sofija at left
    show chatskij at right

    sofija "<{i}(Чацкому){/i}>"

    hide chatskij

    show sofija at truecenter

    sofija "Скажите, что вас так гневит?"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "В той комнате незначущая встреча:"

    chatskij "Французик из Бордо, надсаживая грудь,"

    chatskij "Собрал вокруг себя род веча,"

    chatskij "И сказывал, как снаряжался в путь"

    chatskij "В Россию, к варварам, со страхом и слезами;"

    chatskij "Приехал — и нашел, что ласкам нет конца;"

    chatskij "Ни звука русского, ни русского лица"

    chatskij "Не встретил: будто бы в отечестве, с друзьями;"

    chatskij "Своя провинция. Посмотришь, вечерком"

    chatskij "Он чувствует себя здесь маленьким царьком;"

    chatskij "Такой же толк у дам, такие же наряды..."

    chatskij "Он рад, но мы не рады."

    chatskij "Умолк. И тут со всех сторон"

    chatskij "Тоска, и оханье, и стон:"

    chatskij "Ах! Франция! Нет в мире лучше края! —"

    chatskij "Решили две княжны, сестрицы, повторяя"

    chatskij "Урок, который им из детства натвержён."

    chatskij "Куда деваться от княжен!"

    chatskij "Я одаль воссылал желанья"

    chatskij "Смиренные, однако вслух,"

    chatskij "Чтоб истребил господь нечистый этот дух"

    chatskij "Пустого, рабского, слепого подражанья;"

    chatskij "Чтоб искру заронил он в ком-нибудь с душой,"

    chatskij "Кто мог бы словом и примером"

    chatskij "Нас удержать, как крепкою возжой,"

    chatskij "От жалкой тошноты по стороне чужой."

    chatskij "Пускай меня отъявят старовером,"

    chatskij "Но хуже для меня наш Север во сто крат"

    chatskij "С тех пор, как отдал все в обмен на новый лад, —"

    chatskij "И нравы, и язык, и старину святую,"

    chatskij "И величавую одежду на другую —"

    chatskij "По шутовскому образцу:"

    chatskij "Хвост сзади, спереди какой-то чудный выем,"

    chatskij "Рассудку вопреки, наперекор стихиям,"

    chatskij "Движенья связаны, и не краса лицу;"

    chatskij "Смешные, бритые, седые подбородки!"

    chatskij "Как платья, волосы, так и умы коротки!.."

    chatskij "Ах! если рождены мы всё перенимать,"

    chatskij "Хоть у китайцев бы нам несколько занять"

    chatskij "Премудрого у них незнанья иноземцев;"

    chatskij "Воскреснем ли когда от чужевластья мод?"

    chatskij "Чтоб умный, бодрый наш народ"

    chatskij "Хотя по языку нас не считал за немцев."

    chatskij "«Как европейское поставить в параллель"

    chatskij "С национальным — странно что-то!"

    chatskij "Ну как перевести мадам и мадмуазель?"

    chatskij "Ужли сударыня!!» — забормотал мне кто-то..."

    chatskij "Вообразите, тут у всех"

    chatskij "На мой же счет поднялся смех."

    chatskij "«Сударыня! Ха! ха! ха! ха! прекрасно!"

    chatskij "Сударыня! Ха! ха! ха! ха! ужасно!!» —"

    chatskij "Я, рассердясь и жизнь кляня,"

    chatskij "Готовил им ответ громовый;"

    chatskij "Но все оставили меня. —"

    chatskij "Вот случай вам со мною, он не новый;"

    chatskij "Москва и Петербург — во всей России то,"

    chatskij "Что человек из города Бордо"

    chatskij "Лишь рот открыл, имеет счастье"

    chatskij "Во всех княжен вселять участье;"

    chatskij "И в Петербурге и в Москве,"

    chatskij "Кто недруг выписных лиц, вычур, слов кудрявых,"

    chatskij "В чьей по несчастью голове"

    chatskij "Пять, шесть найдется мыслей здравых,"

    chatskij "И он осмелится их гласно объявлять, —"

    chatskij "{space=400}Глядь..."

    play sound1 footsteps

    chatskij "<{i}Оглядывается, все в вальсе кружатся с величайшим усердием. Старики разбрелись к
            карточным столам.{/i}>"

    stop sound1

    hide chatskij

label Act_4:
    play music "audio/music/7.mp3" fadeout 1.0 fadein 1.0

    scene 6 with fade

    "{b}Действие четвертое{/b}"

    menu:
        "{color=#000}Явление 1{/color}":
            jump Act_4_Scene_1
        "{color=#000}Явление 2{/color}":
            jump Act_4_Scene_2
        "{color=#000}Явление 3{/color}":
            jump Act_4_Scene_3
        "{color=#000}Явление 4{/color}":
            jump Act_4_Scene_4
        "{color=#000}Явление 5{/color}":
            jump Act_4_Scene_5
        "{color=#000}Явление 6{/color}":
            jump Act_4_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_4_Scene_6_1

label Further_Act_4_Scene_6_1:
    menu:
        "{color=#000}Явление 7{/color}":
            jump Act_4_Scene_7
        "{color=#000}Явление 8{/color}":
            jump Act_4_Scene_8
        "{color=#000}Явление 9{/color}":
            jump Act_4_Scene_9
        "{color=#000}Явление 10{/color}":
            jump Act_4_Scene_10
        "{color=#000}Явление 11{/color}":
            jump Act_4_Scene_11
        "{color=#000}Явление 12{/color}":
            jump Act_4_Scene_12
        "{color=#000}>{/color}":
            jump Further_Act_4_Scene_12_2

label Further_Act_4_Scene_12_2:
    menu:
        "{color=#000}Явление 13{/color}":
            jump Act_4_Scene_13
        "{color=#000}Явление 14{/color}":
            jump Act_4_Scene_14
        "{color=#000}Явление 15{/color}":
            jump Act_4_Scene_15

label Act_4_Scene_1:
    "{b}Явление 1{/b}"

    show grafinja_vnuchka at left
    show grafinja_babushka at truecenter
    show lakej_4_4 at right

    "<{i}Графиня бабушка, графиня внучка, впереди их Лакей.{/i}>"

    hide grafinja_vnuchka
    hide grafinja_babushka
    hide lakej_4_4

    show lakej_4_1 at truecenter

    $ lakej_4_1_var = "{noalt}Лакей"

    lakej_4_1 "Графини Хрюминой карета."

    hide lakej_4_1

    show grafinja_vnuchka at truecenter

    $ grafinja_vnuchka_var = "{noalt}Графиня внучка"

    grafinja_vnuchka "<{i}(покуда ее укутывают){/i}>"

    grafinja_vnuchka "Ну бал! Ну Фамусов! умел гостей назвать!"

    grafinja_vnuchka "Какие-то уроды с того света,"

    grafinja_vnuchka "И не с кем говорить, и не с кем танцовать."

    hide grafinja_vnuchka

    show grafinja_babushka at truecenter

    $ grafinja_babushka_var = "{noalt}Графиня бабушка"

    grafinja_babushka "Поетем, матушка, мне прафо не под силу,"

    grafinja_babushka "Когда-нибуть я с пала та в могилу."

    hide grafinja_babushka

    play sound1 horse_run

    "<{i}Обе уезжают.{/i}>"

    stop sound1

label Act_4_Scene_2:
    "{b}Явление 2{/b}"

    show platon_mihajlovich at left
    show natalja_dmitrievna at truecenter
    show lakej_4_4 at right

    "<{i}Платон Михайлович и Наталья Дмитриевна; один лакей около их хлопочет, другой у
            подъезда кричит:{/i}>"

    hide platon_mihajlovich
    hide natalja_dmitrievna
    hide lakej_4_4

    show lakej_4_2a at truecenter

    $ lakej_4_2a_var = "{noalt}Лакей"

    lakej_4_2a "Карета Горича."

    hide lakej_4_2a

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "{space=400}Мой ангел, жизнь моя,"

    natalja_dmitrievna "Бесценный, душечка, Попошь, что́ так уныло?"

    play sound1 kiss

    hide natalja_dmitrievna

    show natalja_dmitrievna at left
    show platon_mihajlovich at right

    natalja_dmitrievna "<{i}(целует мужа в лоб.){/i}>"

    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    stop sound1

    natalja_dmitrievna "Признайся, весело у Фамусовых было."

    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "Наташа-матушка, дремлю на ба́лах я,"

    platon_mihajlovich "До них смертельный неохотник,"

    platon_mihajlovich "А не противлюсь, твой работник,"

    platon_mihajlovich "Дежурю за полночь, подчас"

    platon_mihajlovich "Тебе в угодность, как ни грустно,"

    platon_mihajlovich "Пускаюсь по команде в пляс."

    hide platon_mihajlovich

    show natalja_dmitrievna at truecenter

    $ natalja_dmitrievna_var = "{noalt}Наталья Дмитриевна"

    natalja_dmitrievna "Ты притворяешься, и очень неискусно;"

    natalja_dmitrievna "Охота смертная прослыть за старика."

    play sound1 footsteps

    hide natalja_dmitrievna

    show natalja_dmitrievna at left
    show lakej_4_4 at right

    natalja_dmitrievna "<{i}(Уходит с лакеем.){/i}>"

    hide lakej_4_4

    show natalja_dmitrievna at truecenter

    stop sound1

    hide natalja_dmitrievna

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    platon_mihajlovich "<{i}(хладнокровно){/i}>"

    platon_mihajlovich "Бал вещь хорошая, неволя-то горька;"

    platon_mihajlovich "И кто жениться нас неволит!"

    platon_mihajlovich "Ведь сказано ж, иному на роду..."

    hide platon_mihajlovich

    show lakej_4_2b at truecenter

    $ lakej_4_2b_var = "{noalt}Лакей"

    lakej_4_2b "<{i}(с крыльца){/i}>"

    lakej_4_2b "В карете барыня-с, и гневаться изволит."

    hide lakej_4_2b

    show platon_mihajlovich at truecenter

    $ platon_mihajlovich_var = "{noalt}Платон Михайлович"

    play sound1 male_sigh

    platon_mihajlovich "<{i}(со вздохом){/i}>"

    stop sound1

    platon_mihajlovich "{space=400}Иду, иду."

    play sound1 horse_run

    platon_mihajlovich "<{i}(Уезжает.){/i}>"

    stop sound1

    hide platon_mihajlovich

label Act_4_Scene_3:
    "{b}Явление 3{/b}"

    show chatskij at left
    show lakej_4_4 at right

    "<{i}Чацкий и Лакей его впереди.{/i}>"

    hide chatskij
    hide lakej_4_4

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Кричи, чтобы скорее подавали."

    play sound1 footsteps

    hide chatskij

    show chatskij at left
    show lakej_4_4 at right

    chatskij "<{i}Лакей уходит.{/i}>"

    hide lakej_4_4

    show chatskij at truecenter

    stop sound1

    chatskij "Ну вот и день прошел, и с ним"

    chatskij "Все призраки, весь чад и дым"

    chatskij "Надежд, которые мне душу наполняли."

    chatskij "Чего я ждал? что думал здесь найти?"

    chatskij "Где прелесть эта встреч? участье в ком живое?"

    chatskij "Крик! радость! обнялись! Пустое."

    chatskij "В повозке так-то на пути,"

    chatskij "Необозримою равниной, сидя праздно,"

    chatskij "Все что-то видно впереди"

    chatskij "Светло, синё, разнообразно;"

    chatskij "И едешь час, и два, день целый; вот резво́"

    chatskij "Домчались к отдыху; ночлег: куда ни взглянешь,"

    chatskij "Все та же гладь, и степь, и пусто и мертво;"

    chatskij "Досадно, мочи нет, чем больше думать станешь."

    play sound1 footsteps

    hide chatskij

    show chatskij at left
    show lakej_4_4 at right

    chatskij "<{i}Лакей возвращается.{/i}>"

    hide lakej_4_4

    show chatskij at truecenter

    stop sound1

    chatskij "Готово?"

    hide chatskij

    show lakej_chatskogo at truecenter

    $ lakej_chatskogo_var = "{noalt}Лакей"

    lakej_chatskogo "{space=400}Кучера-с нигде, вишь, не найдут."

    hide lakej_chatskogo

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Пошел, ищи, не ночевать же тут."

    hide chatskij

    play sound1 footsteps

    show lakej_4_4 at truecenter

    "<{i}Лакей опять уходит.{/i}>"

    hide lakej_4_4

    stop sound1

label Act_4_Scene_4:
    "{b}Явление 4{/b}"

    play sound1 footsteps

    show chatskij at left
    show repetilov at right

    "<{i}Чацкий, Репетилов (вбегает с крыльца, при самом входе падает со всех ног и поспешно
            оправляется).{/i}>"

    hide chatskij
    hide repetilov

    stop sound1

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Тьфу! оплошал. — Ах, мой создатель!"

    repetilov "Дай протереть глаза; откудова? приятель!.."

    repetilov "Сердечный друг! Любезный друг! Mon cher!"

    repetilov "Вот фарсы мне как часто были петы,"

    repetilov "Что пустомеля я, что глуп, что суевер,"

    repetilov "Что у меня на всё предчувствия, приметы;"

    repetilov "Сейчас... растолковать прошу,"

    repetilov "Как будто знал, сюда спешу,"

    repetilov "Хвать, об порог задел ногою,"

    repetilov "И растянулся во весь рост."

    repetilov "Пожалуй смейся надо мною,"

    repetilov "Что Репетилов врет, что Репетилов прост,"

    repetilov "А у меня к тебе влеченье, род недуга,"

    repetilov "Любовь какая-то и страсть,"

    repetilov "Готов я душу прозакласть,"

    repetilov "Что в мире не найдешь себе такого друга,"

    repetilov "Такого верного, ей-ей;"

    repetilov "Пускай лишусь жены, детей,"

    repetilov "Оставлен буду целым светом,"

    repetilov "Пускай умру на месте этом,"

    repetilov "И разразит меня господь..."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Да полно вздор молоть."

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Не любишь ты меня, естественное дело:"

    repetilov "С другими я и так и сяк,"

    repetilov "С тобою говорю несмело,"

    repetilov "Я жалок, я смешон, я неуч, я дурак."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Вот странное уничиженье!"

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Ругай меня, я сам кляну свое рожденье,"

    repetilov "Когда подумаю, как время убивал!"

    repetilov "Скажи, который час?"

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Час ехать спать ложиться;"

    chatskij "Коли явился ты на бал,"

    chatskij "Так можешь воротиться."

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Что бал? братец, где мы всю ночь до бела дня,"

    repetilov "В приличьях скованы, не вырвемся из ига,"

    repetilov "Читал ли ты? есть книга..."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "А ты читал? задача для меня,"

    chatskij "Ты Репетилов ли?"

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Зови меня вандалом:"

    repetilov "Я это имя заслужил."

    repetilov "Людьми пустыми дорожил!"

    repetilov "Сам бредил целый век обедом или балом!"

    repetilov "Об детях забывал! обманывал жену!"

    repetilov "Играл! проигрывал! в опеку взят указом!"

    repetilov "Танцовщицу держал! и не одну:"

    repetilov "{space=400}Трех разом!"

    repetilov "Пил мертвую! не спал ночей по девяти!"

    repetilov "Всё отвергал: законы! совесть! веру!"

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Послушай! ври, да знай же меру;"

    chatskij "Есть от чего в отчаянье прийти."

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Поздравь меня, теперь с людьми я знаюсь"

    repetilov "С умнейшими!! — Всю ночь не рыщу напролет."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Вот нынче например?"

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Что? ночь одна не в счет!"

    repetilov "Зато спроси, где был?"

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}И сам я догадаюсь,"

    chatskij "Чай в клубе?"

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}В Английском. Чтоб исповедь начать:"

    repetilov "Из шумного я заседанья."

    repetilov "Пожалоста, молчи, я слово дал молчать."

    repetilov "У нас есть общество, и тайные собранья,"

    repetilov "По четвергам. Секретнейший союз..."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Ах! я, братец, боюсь."

    chatskij "Как? в клубе?"

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Именно."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Вот меры чрезвычайны,"

    chatskij "Чтоб вза́шеи прогнать и вас, и ваши тайны."

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Напрасно страх тебя берет,"

    repetilov "Вслух, громко говорим, никто не разберет."

    repetilov "Я сам, как схватятся о камерах, присяжных,"

    repetilov "О Бейроне, ну о матерьях важных,"

    repetilov "Частенько слушаю, не разжимая губ;"

    repetilov "Мне не под силу, брат, и чувствую, что глуп."

    repetilov "Ах, Alexandre! у нас тебя недоставало;"

    repetilov "Послушай, миленький, потешь меня хоть мало;"

    repetilov "Поедем-ка сейчас; мы, благо, на ходу;"

    repetilov "С какими я тебя сведу"

    repetilov "Людьми!!! Уж на меня нисколько не похожи."

    repetilov "Что за́ люди, mon cher! Сок умной молодежи!"

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Бог с ними и с тобой. Куда я поскачу?"

    chatskij "Зачем? в глухую ночь? Домой, я спать хочу."

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Э! брось! кто нынче спит? Ну, полно, без прелюдий,"

    repetilov "Решись, а мы!.. у нас... решительные люди,"

    repetilov "{space=400}Горячих дюжина голов!"

    repetilov "Кричим — подумаешь, что сотни голосов!.."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Да из чего беснуетесь вы столько?"

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Шумим, братец, шумим..."

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Шумите вы? и только?"

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Не место объяснять теперь и недосуг,"

    repetilov "Но государственное дело:"

    repetilov "Оно, вот видишь, не созрело,"

    repetilov "{space=400}Нельзя же вдруг."

    repetilov "Что за люди! mon cher! Без дальних я историй"

    repetilov "Скажу тебе: во-первых, князь Григорий!!"

    repetilov "Чудак единственный! нас со́ смеху морит!"

    repetilov "Век с англичанами, вся а́нглийская складка,"

    repetilov "И так же он сквозь зубы говорит,"

    repetilov "И так же коротко обстрижен для порядка."

    repetilov "Ты не знаком? о! познакомься с ним."

    repetilov "Другой — Воркулов Евдоким,"

    repetilov "Ты не слыхал, как он поет? о! диво!"

    repetilov "Послушай, милый, особливо"

    repetilov "Есть у него любимое одно:"

    repetilov "«А! нон лашьяр ми, но, но, но»."

    repetilov "Еще у нас два брата:"

    repetilov "Левон и Боринька, чудесные ребята!"

    repetilov "Об них не знаешь что сказать;"

    repetilov "Но если гения прикажете назвать:"

    repetilov "Удушьев Ипполит Маркелыч!!!"

    repetilov "Ты сочинения его"

    repetilov "Читал ли что-нибудь? хоть мелочь?"

    repetilov "Прочти, братец, да он не пишет ничего;"

    repetilov "Вот эдаких людей бы сечь-то,"

    repetilov "И приговаривать: писать, писать, писать;"

    repetilov "В журналах можешь ты однако отыскать"

    repetilov "Его отрывок, взгляд и нечто."

    repetilov "Об чем бишь нечто? — обо всем;"

    repetilov "Все знает, мы его на черный день пасем."

    repetilov "Но голова у нас, какой в России нету,"

    repetilov "Не надо называть, узнаешь по портрету:"

    repetilov "Ночной разбойник, дуэлист,"

    repetilov "В Камчатку сослан был, вернулся алеутом,"

    repetilov "И крепко на руку нечист;"

    repetilov "Да умный человек не может быть не плутом."

    repetilov "Когда ж об честности высокой говорит,"

    repetilov "Каким-то демоном внушаем:"

    repetilov "Глаза в крови, лицо горит,"

    repetilov "Сам плачет, и мы все рыдаем."

    repetilov "Вот люди, есть ли им подобные? Навряд..."

    repetilov "Ну, между ими я, конечно, зауряд,"

    repetilov "Немножко поотстал, ленив, подумать ужас!"

    repetilov "Однако ж я, когда, умишком понатужась,"

    repetilov "Засяду, часу не сижу,"

    repetilov "И как-то невзначай, вдруг каламбур рожу,"

    repetilov "Другие у меня мысль эту же подцепят,"

    repetilov "И вшестером, глядь, водевильчик слепят,"

    repetilov "Другие шестеро на музыку кладут,"

    repetilov "Другие хлопают, когда его дают."

    repetilov "Брат, смейся, а что любо, любо:"

    repetilov "Способностями бог меня не наградил,"

    repetilov "Дал сердце доброе, вот чем я людям мил,"

    repetilov "Совру — простят..."

    hide repetilov

    show lakej_4_4 at truecenter

    $ lakej_4_4_var = "{noalt}Лакей"

    lakej_4_4 "<{i}(у подъезда){/i}>"

    lakej_4_4 "{space=400}Карета Скалозуба."

    hide lakej_4_4

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Чья?"

    hide repetilov

label Act_4_Scene_5:
    "{b}Явление 5{/b}"

    show skalozub at truecenter

    "<{i}Те же и Скалозуб, спускается с лестницы.{/i}>"

    hide skalozub

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    hide repetilov

    show repetilov at left
    show skalozub at right

    repetilov "<{i}(к нему навстречу){/i}>"

    hide skalozub

    show repetilov at truecenter

    repetilov "Ах! Скалозуб, душа моя,"

    repetilov "Постой; куда же? сделай дружбу."

    hide repetilov

    show repetilov at left
    show skalozub at right

    repetilov "<{i}(Душит его в объятиях.){/i}>"

    hide skalozub

    show repetilov at truecenter

    hide repetilov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Куда деваться мне от них!"

    play sound1 footsteps

    chatskij "<{i}(Входит в швейцарскую.){/i}>"

    stop sound1

    hide chatskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    hide repetilov

    show repetilov at left
    show skalozub at right

    repetilov "<{i}(Скалозубу){/i}>"

    hide skalozub

    show repetilov at truecenter

    repetilov "Слух об тебе давно затих,"

    repetilov "Сказали, что ты в полк отправился на службу."

    repetilov "Знакомы вы?"

    hide repetilov

    show repetilov at left
    show chatskij at right

    repetilov "<{i}(Ищет Чацкого глазами.){/i}>"

    hide chatskij

    show repetilov at truecenter

    repetilov "{space=400}Упрямец! ускакал!"

    repetilov "Нет ну́жды, я тебя нечаянно сыскал,"

    repetilov "И просим-ка со мной, сейчас без отговорок:"

    repetilov "У князь-Григория теперь народу тьма,"

    repetilov "Увидишь человек нас сорок,"

    repetilov "Фу, сколько, братец, там ума!"

    repetilov "Всю ночь толкуют, не наскучат,"

    repetilov "Во-первых, напоят шампанским на убой,"

    repetilov "А во-вторых, таким вещам научат,"

    repetilov "Каких, конечно, нам не выдумать с тобой."

    hide repetilov

    show skalozub at truecenter

    $ skalozub_var = "{noalt}Скалозуб"

    skalozub "Избавь. Ученостью меня не обморочишь;"

    skalozub "Скликай других, а если хочешь,"

    skalozub "Я князь-Григорию и вам"

    skalozub "Фельдфебеля в Волтеры дам,"

    skalozub "Он в три шеренги вас построит,"

    skalozub "А пикнете, так мигом успокоит."

    hide skalozub

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Все служба на уме! Mon cher, гляди сюда:"

    repetilov "И я в чины бы лез, да неудачи встретил,"

    repetilov "Как, может быть, никто и никогда,"

    repetilov "По статской я служил, тогда"

    repetilov "Барон фон Клоц в министры метил,"

    repetilov "{space=400}А я —"

    repetilov "{space=400}К нему в зятья."

    repetilov "Шел напрямик без дальней думы,"

    repetilov "С его женой и с ним пускался в реверси,"

    repetilov "Ему и ей какие суммы"

    repetilov "Спустил, что боже упаси!"

    repetilov "Он на Фонтанке жил, я возле дом построил,"

    repetilov "С колоннами! огромный! сколько стоил!"

    repetilov "Женился наконец на дочери его,"

    repetilov "Приданого взял — шиш, по службе — ничего."

    repetilov "{space=400}Тесть немец, а что проку?"

    repetilov "Боялся, видишь, он упреку"

    repetilov "За слабость будто бы к родне!"

    repetilov "Боялся, прах его возьми, да легче ль мне?"

    repetilov "Секретари его все хамы, все продажны,"

    repetilov "Людишки, пишущая тварь,"

    repetilov "Все вышли в знать, все нынче важны,"

    repetilov "Гляди-ка в адрес-календарь."

    repetilov "Тьфу! служба и чины, кресты — души мытарства,"

    repetilov "Лахмотьев Алексей чудесно говорит,"

    repetilov "Что радикальные потребны тут лекарства,"

    repetilov "Желудок дольше не варит."

    play sound1 horse_run

    hide repetilov

    show repetilov at left
    show zagoretskij at truecenter
    show skalozub at right

    repetilov "<{i}(Останавливается, увидя, что Загорецкий заступил место Скалозуба, который
              покудова уехал.){/i}>"

    hide zagoretskij
    hide skalozub

    show repetilov at truecenter

    stop sound1

    hide repetilov

label Act_4_Scene_6:
    "{b}Явление 6{/b}"

    show repetilov at left
    show zagoretskij at right

    "<{i}Репетилов, Загорецкий.{/i}>"

    hide repetilov
    hide zagoretskij

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Извольте продолжать, вам искренно признаюсь,"

    zagoretskij "Такой же я, как вы: ужасный либерал!"

    zagoretskij "И от того, что прям и смело объясняюсь,"

    zagoretskij "Куда как много потерял!.."

    hide zagoretskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "<{i}(с досадой){/i}>"

    repetilov "Все врознь, не говоря ни слова;"

    repetilov "Чуть из виду один, гляди — уж нет другого."

    repetilov "Был Чацкий, вдруг исчез, потом и Скалозуб."

    hide repetilov

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Как думаете вы об Чацком?"

    hide zagoretskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Он не глуп,"

    repetilov "Сейчас столкнулись мы, тут всякие турусы,"

    repetilov "И дельный разговор зашел про водевиль."

    repetilov "Да! водевиль есть вещь, а прочее все гиль."

    repetilov "Мы с ним... у нас... одни и те же вкусы."

    hide repetilov

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "А вы заметили, что он"

    zagoretskij "В уме сурьезно поврежден?"

    hide zagoretskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Какая чепуха!"

    hide repetilov

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "{space=400}Об нем все этой веры."

    hide zagoretskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Вранье."

    hide repetilov

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "{space=400}Спросите всех."

    hide zagoretskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Химеры."

    hide repetilov

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "А кстати, вот князь Петр Ильич,"

    zagoretskij "Княгиня и с княжнами."

    hide zagoretskij

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Дичь."

    hide repetilov

label Act_4_Scene_7:
    "{b}Явление 7{/b}"

    show hlestova at left
    show molchalin at truecenter
    show lakej_4_4 at right

    "<{i}Репетилов, Загорецкий, Князь и Княгиня с шестью дочерями, немного погодя Хлёстова
            спускается с парадной лестницы, Молчалин ведет ее под руку. Лакеи в суетах.{/i}>"

    hide repetilov
    hide zagoretskij
    hide knjaz
    hide knjaginja
    hide sofija
    hide hlestova
    hide molchalin
    hide lakej_4_4

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "Княжны, пожалуйте, скажите ваше мненье,"

    zagoretskij "Безумный Чацкий или нет?"

    hide zagoretskij

    show pervaja_knjazhna at truecenter

    $ pervaja_knjazhna_var = "{noalt}1-я княжна"

    pervaja_knjazhna "Какое ж в этом есть сомненье?"

    hide pervaja_knjazhna

    show vtoraja_knjazhna at truecenter

    $ vtoraja_knjazhna_var = "{noalt}2-я княжна"

    vtoraja_knjazhna "Про это знает целый свет."

    hide vtoraja_knjazhna

    show tretja_knjazhna at truecenter

    $ tretja_knjazhna_var = "{noalt}3-я княжна"

    tretja_knjazhna "Дрянские, Хворовы, Варлянские, Скачковы."

    hide tretja_knjazhna

    show chetviortaja_knjazhna at truecenter

    $ chetviortaja_knjazhna_var = "{noalt}4-я княжна"

    chetviortaja_knjazhna "Ах! вести старые, кому они новы́?"

    hide chetviortaja_knjazhna

    show pjataja_knjazhna at truecenter

    $ pjataja_knjazhna_var = "{noalt}5-я княжна"

    pjataja_knjazhna "Кто сомневается?"

    hide pjataja_knjazhna

    show zagoretskij at truecenter

    $ zagoretskij_var = "{noalt}Загорецкий"

    zagoretskij "{space=400}Да вот не верит..."

    hide zagoretskij

    show shestaja_knjazhna at truecenter

    $ shestaja_knjazhna_var = "{noalt}6-я княжна"

    shestaja_knjazhna "{space=400}Вы!"

    hide shestaja_knjazhna

    show chetviortaja_knjazhna at left
    show pjataja_knjazhna at truecenter
    show shestaja_knjazhna at right

    $ chetviortaja_knjazhna_var = "{noalt}Все вместе"

    chetviortaja_knjazhna "Мсьё Репетилов! Вы! Мсье Репетилов, что вы!"

    chetviortaja_knjazhna "Да как вы! Можно ль против всех!"

    chetviortaja_knjazhna "Да почему вы? стыд и смех."

    hide chetviortaja_knjazhna
    hide pjataja_knjazhna
    hide shestaja_knjazhna

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "<{i}(затыкает себе уши){/i}>"

    repetilov "Простите, я не знал, что это слишком гласно."

    hide repetilov

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "Еще не гласно бы, с ним говорить опасно,"

    knjaginja "Давно бы запереть пора,"

    knjaginja "Послушать, так его мизинец"

    knjaginja "Умнее всех, и даже князь-Петра!"

    knjaginja "Я думаю, он просто якобинец,"

    knjaginja "Ваш Чацкий!!! Едемте. Князь, ты везти бы мог"

    knjaginja "Катишь или Зизи, мы сядем в шестиместной."

    hide knjaginja

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "<{i}(с лестницы){/i}>"

    hlestova "Княгиня, карточный должок."

    hide hlestova

    show knjaginja at truecenter

    $ knjaginja_var = "{noalt}Княгиня"

    knjaginja "За мною, матушка."

    hide knjaginja

    show knjaginja at left
    show repetilov at truecenter
    show hlestova at right

    $ knjaginja_var = "{noalt}Все"

    knjaginja "<{i}(друг к другу){/i}>"

    knjaginja "{space=400}Прощайте."

    hide knjaginja
    hide repetilov
    hide hlestova

    play sound1 horse_run

    show zagoretskij at truecenter

    "<{i}Княжеская фамилия уезжает и Загорецкий тоже.{/i}>"

    hide zagoretskij

    stop sound1

label Act_4_Scene_8:
    "{b}Явление 8{/b}"

    show repetilov at left
    show hlestova at truecenter
    show molchalin at right

    "<{i}Репетилов, Хлёстова, Молчалин.{/i}>"

    hide repetilov
    hide hlestova
    hide molchalin

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "{space=400}Царь небесный!"

    repetilov "Амфиса Ниловна! Ах! Чацкий! бедный! вот!"

    repetilov "Что́ наш высокий ум! и тысяча забот!"

    repetilov "Скажите, из чего на свете мы хлопочем!"

    hide repetilov

    show hlestova at truecenter

    $ hlestova_var = "{noalt}Хлёстова"

    hlestova "Так бог ему судил; а впрочем,"

    hlestova "Полечат, вылечат авось;"

    hlestova "А ты, мой батюшка, неисцелим, хоть брось."

    hlestova "Изволил вовремя явиться!"

    hlestova "Молчалин, вон чуланчик твой,"

    hlestova "Не нужны проводы, поди, господь с тобой."

    play sound1 footsteps

    hide hlestova

    show hlestova at left
    show molchalin at right

    hlestova "<{i}Молчалин уходит к себе в комнату.{/i}>"

    hide molchalin

    show hlestova at truecenter

    stop sound1

    hlestova "Прощайте, батюшка; пора перебеситься."

    play sound1 horse_run

    hlestova "<{i}(Уезжает.){/i}>"

    stop sound1

    hide hlestova

label Act_4_Scene_9:
    "{b}Явление 9{/b}"

    show repetilov at left
    show lakej_4_4 at right

    "<{i}Репетилов с своим лакеем.{/i}>"

    hide repetilov
    hide lakej_4_4

    show repetilov at truecenter

    $ repetilov_var = "{noalt}Репетилов"

    repetilov "Куда теперь направить путь?"

    repetilov "А дело уж идет к рассвету."

    repetilov "Поди, сажай меня в карету,"

    repetilov "Вези куда-нибудь."

    play sound1 horse_run

    repetilov "<{i}(Уезжает.){/i}>"

    stop sound1

    hide repetilov

label Act_4_Scene_10:
    "{b}Явление 10{/b}"

    "<{i}Последняя лампа гаснет.{/i}>"

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    play sound1 footsteps

    chatskij "<{i}(выходит из швейцарской){/i}>"

    stop sound1

    chatskij "Что это? слышал ли моими я ушами!"

    chatskij "Не смех, а явно злость. Какими чудесами?"

    chatskij "Через какое колдовство"

    chatskij "Нелепость обо мне все в голос повторяют!"

    chatskij "И для иных как словно торжество,"

    chatskij "Другие будто сострадают..."

    chatskij "О! если б кто в людей проник:"

    chatskij "Что хуже в них? душа или язык?"

    chatskij "Чье это сочиненье!"

    chatskij "Поверили глупцы, другим передают,"

    chatskij "Старухи вмиг тревогу бьют —"

    chatskij "И вот общественное мненье!"

    chatskij "И вот та родина... Нет, в нынешний приезд,"

    chatskij "Я вижу, что она мне скоро надоест."

    chatskij "А Софья знает ли? Конечно, рассказали,"

    chatskij "Она не то чтобы мне именно во вред"

    chatskij "Потешилась, и правда или нет —"

    chatskij "Ей все равно, другой ли, я ли,"

    chatskij "Никем по совести она не дорожит."

    chatskij "Но этот обморок? беспамятство откуда??"

    chatskij "Нерв избалованность, причуда —"

    chatskij "Возбудит малость их и малость утишит..."

    chatskij "Я признаком почел живых страстей. — Ни крошки:"

    chatskij "Она, конечно бы, лишилась так же сил,"

    chatskij "Когда бы кто-нибудь ступил"

    chatskij "На хвост собачки или кошки."

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(над лестницей во втором этаже, со свечкою){/i}>"

    sofija "Молчалин, вы?"

    play sound1 door_creak

    sofija "<{i}(Поспешно опять дверь припирает.){/i}>"

    stop sound1

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Она! она сама!"

    chatskij "Ах! голова горит, вся кровь моя в волненьи."

    chatskij "Явилась! нет ее! неу́жели в виденьи?"

    chatskij "Не впрямь ли я сошел с ума?"

    chatskij "К необычайности я точно приготовлен;"

    chatskij "Но не виденье тут, свиданья час условлен."

    chatskij "К чему обманывать себя мне самого?"

    chatskij "Звала Молчалина, вот комната его."

    hide chatskij

    show lakej_chatskogo at truecenter

    $ lakej_chatskogo_var = "{noalt}Лакей его"

    lakej_chatskogo "<{i}(с крыльца){/i}>"

    lakej_chatskogo "Каре..."

    hide lakej_chatskogo

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "{space=400}Сс!.."

    play sound1 punch

    hide chatskij

    show chatskij at left
    show lakej_chatskogo at right

    chatskij "<{i}(Выталкивает его вон.){/i}>"

    hide lakej_chatskogo

    show chatskij at truecenter

    stop sound1

    chatskij "{space=400}Буду здесь, и не смыкаю глазу,"

    chatskij "Хоть до утра. Уж коли горе пить,"

    chatskij "{space=400}Так лучше сразу,"

    chatskij "Чем медлить, — а беды медленьем не избыть."

    chatskij "Дверь отворяется."

    chatskij "<{i}(Прячется за колонну.){/i}>"

    hide chatskij

label Act_4_Scene_11:
    "{b}Явление 11{/b}"

    show chatskij at left
    show lizanka at right

    "<{i}Чацкий спрятан; Лиза со свечкой.{/i}>"

    hide chatskij
    hide lizanka

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}Ах! мочи нет! робею!"

    lizanka "В пустые сени! в ночь! боишься домовых,"

    lizanka "Боишься и людей живых."

    lizanka "Мучительница-барышня, бог с нею."

    lizanka "И Чацкий, как бельмо в глазу;"

    lizanka "Вишь, показался ей он где-то здесь внизу."

    lizanka "<{i}(Осматривается.){/i}>"

    lizanka "Да! как же! по сеням бродить ему охота!"

    lizanka "Он, чай, давно уж за ворота,"

    lizanka "{space=400}Любовь на завтра поберег,"

    lizanka "Домой, и спать залег."

    lizanka "Однако велено к сердечному толкнуться."

    play sound1 knocking

    hide lizanka

    show lizanka at left
    show molchalin at right

    lizanka "<{i}(Стучится к Молчалину.){/i}>"

    hide molchalin

    show lizanka at truecenter

    stop sound1

    lizanka "Послушайте-с. Извольте-ка проснуться."

    lizanka "Вас кличет барышня, вас барышня зовет."

    lizanka "Да поскорей, чтоб не застали."

    hide lizanka

label Act_4_Scene_12:
    "{b}Явление 12{/b}"

    show lizanka at left
    show molchalin at truecenter
    show sofija at right

    "<{i}Чацкий за колонною, Лиза, Молчалин (потягивается и зевает), София (крадется
            сверху).{/i}>"

    hide chatskij
    hide lizanka
    hide molchalin
    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Вы, сударь, камень, сударь, лед."

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Ах! Лизанька, ты от себя ли?"

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "От барышни-с."

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Кто б отгадал,"

    molchalin "Что в этих щечках, в этих жилках"

    molchalin "Любви еще румянец не играл!"

    molchalin "Охота быть тебе лишь только на посылках?"

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "А вам, искателям невест,"

    lizanka "Не нежиться и не зевать бы;"

    lizanka "Пригож и мил, кто не доест"

    lizanka "{space=400}И не доспит до свадьбы."

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Какая свадьба? с кем?"

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "{space=400}А с барышней?"

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Поди,"

    molchalin "Надежды много впереди,"

    molchalin "Без свадьбы время проволочим."

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Что вы, суда́рь! да мы кого ж"

    lizanka "Себе в мужья другого прочим?"

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Не знаю. А меня так разбирает дрожь,"

    molchalin "И при одной я мысли трушу,"

    molchalin "Что Павел Афанасьич раз"

    molchalin "Когда-нибудь поймает нас,"

    molchalin "Разгонит, проклянёт!.. Да что? открыть ли душу?"

    molchalin "Я в Софье Павловне не вижу ничего"

    molchalin "Завидного. Дай бог ей век прожить богато,"

    molchalin "Любила Чацкого когда-то,"

    molchalin "Меня разлюбит, как его."

    molchalin "Мой ангельчик, желал бы вполовину"

    molchalin "К ней то же чувствовать, что чувствую к тебе;"

    molchalin "Да нет, как ни твержу себе,"

    molchalin "Готовлюсь нежным быть, а свижусь — и простыну."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(в сторону){/i}>"

    sofija "Какие низости!"

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(за колонною){/i}>"

    chatskij "{space=400}Подлец!"

    hide chatskij

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "И вам не совестно?"

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Мне завещал отец:"

    molchalin "Во-первых, угождать всем людям без изъятья;"

    molchalin "Хозяину, где доведется жить,"

    molchalin "Начальнику, с кем буду я служить,"

    molchalin "Слуге его, который чистит платья,"

    molchalin "Швейцару, дворнику, для избежанья зла,"

    molchalin "Собаке дворника, чтоб ласкова была."

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Сказать, суда́рь, у вас огромная опека!"

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "И вот любовника я принимаю вид"

    molchalin "В угодность дочери такого человека..."

    hide molchalin

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Который кормит и поит,"

    lizanka "А иногда и чином подарит?"

    lizanka "Пойдемте же, довольно толковали."

    hide lizanka

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Пойдем любовь делить плачевной нашей крали."

    molchalin "Дай обниму тебя от сердца полноты."

    hide molchalin

    show molchalin at left
    show lizanka at right

    molchalin "<{i}Лиза не дается.{/i}>"

    hide lizanka

    show molchalin at truecenter

    molchalin "Зачем она не ты!"

    hide molchalin

    show molchalin at left
    show sofija at right

    molchalin "<{i}(хочет идти, София не пускает.){/i}>"

    hide sofija

    show molchalin at truecenter

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "<{i}(почти шепотом; вся сцена вполголоса){/i}>"

    sofija "Нейдите далее, наслушалась я много,"

    sofija "Ужасный человек! себя я, стен стыжусь."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Как! Софья Павловна..."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Ни слова, ради бога,"

    sofija "Молчите, я на все решусь."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    hide molchalin

    show molchalin at left
    show sofija at right

    molchalin "<{i}(бросается на колена, София отталкивает его){/i}>"

    hide sofija

    show molchalin at truecenter

    molchalin "Ах! вспомните! не гневайтеся, взгляньте!.."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Не помню ничего, не докучайте мне."

    sofija "Воспоминания! как острый нож оне."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "<{i}(ползает у ног ее){/i}>"

    molchalin "Помилуйте..."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Не подличайте, встаньте."

    sofija "Ответа не хочу, я знаю ваш ответ,"

    sofija "Солжете..."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "{space=400}Сделайте мне милость..."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Нет. Нет. Нет."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Шутил, и не сказал я ничего, окроме..."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "Отстаньте, говорю, сейчас,"

    sofija "Я криком разбужу всех в доме,"

    sofija "И погублю себя и вас."

    hide sofija

    show sofija at left
    show molchalin at right

    sofija "<{i}Молчалин встает.{/i}>"

    hide molchalin

    show sofija at truecenter

    sofija "Я с этих пор вас будто не знавала."

    sofija "Упреков, жалоб, слез моих"

    sofija "Не смейте ожидать, не стоите вы их;"

    sofija "Но чтобы в доме здесь заря вас не застала,"

    sofija "Чтоб никогда об вас я больше не слыхала."

    hide sofija

    show molchalin at truecenter

    $ molchalin_var = "{noalt}Молчалин"

    molchalin "Как вы прикажете."

    hide molchalin

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    sofija "{space=400}Иначе расскажу"

    sofija "Всю правду батюшке, с досады."

    sofija "Вы знаете, что я собой не дорожу."

    sofija "Подите. — Стойте, будьте рады,"

    sofija "Что при свиданиях со мной в ночной тиши"

    sofija "Держались более вы робости во нраве,"

    sofija "Чем даже днем, и при людях, и в яве,"

    sofija "В вас меньше дерзости, чем кривизны души."

    sofija "Сама довольна тем, что ночью все узнала,"

    sofija "Нет укоряющих свидетелей в глазах,"

    sofija "Как давиче, когда я в обморок упала."

    sofija "Здесь Чацкий был..."

    hide sofija

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(бросается между ними){/i}>"

    chatskij "{space=400}Он здесь, притворщица!"

    hide chatskij

    show lizanka at left
    show sofija at right

    $ lizanka_var = "{noalt}Лиза и София"

    lizanka "{space=400}Ах! Ах!.."

    hide lizanka
    hide sofija

    play sound1 footsteps

    show lizanka at left
    show molchalin at right

    "<{i}Лиза свечку роняет с испугу; Молчалин скрывается к себе в комнату.{/i}>"

    hide lizanka
    hide molchalin

    stop sound1

label Act_4_Scene_13:
    "{b}Явление 13{/b}"

    show molchalin at truecenter

    "<{i}Те же, кроме Молчалина.{/i}>"

    hide molchalin

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "Скорее в обморок, теперь оно в порядке,"

    chatskij "Важнее давишной причина есть тому,"

    chatskij "Вот наконец решение загадке!"

    chatskij "Вот я пожертвован кому!"

    chatskij "Не знаю, как в себе я бешенство умерил!"

    chatskij "Глядел, и видел, и не верил!"

    chatskij "А милый, для кого забыт"

    chatskij "И прежний друг, и женский страх и стыд, —"

    chatskij "За двери прячется, боится быть в ответе."

    chatskij "Ах! как игру судьбы постичь?"

    chatskij "Людей с душой гонительница, бич! —"

    chatskij "Молчалины блаженствуют на свете!"

    hide chatskij

    show sofija at truecenter

    $ sofija_var = "{noalt}София"

    play sound1 female_cry

    sofija "<{i}(вся в слезах){/i}>"

    stop sound1

    sofija "Не продолжайте, я виню себя кругом."

    sofija "Но кто бы думать мог, чтоб был он так коварен!"

    hide sofija

    show lizanka at truecenter

    $ lizanka_var = "{noalt}Лиза"

    lizanka "Стук! шум! ах! боже мой! сюда бежит весь дом."

    lizanka "Ваш батюшка, вот будет благодарен."

    hide lizanka

label Act_4_Scene_14:
    "{b}Явление 14{/b}"

    show lizanka at left
    show famusov at truecenter
    show sluga_2_3 at right

    "<{i}Чацкий, София, Лиза, Фамусов, толпа слуг со свечами.{/i}>"

    hide chatskij
    hide sofija
    hide lizanka
    hide famusov
    hide sluga_2_3

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Сюда! за мной! скорей! скорей!"

    famusov "Свечей побольше, фонарей!"

    famusov "Где домовые? Ба! знакомые всё лица!"

    famusov "Дочь, Софья Павловна! страмница!"

    famusov "Бесстыдница! где! с кем! Ни дать, ни взять она,"

    famusov "Как мать ее, покойница жена."

    famusov "Бывало я с дражайшей половиной"

    famusov "Чуть врознь: — уж где-нибудь с мужчиной!"

    famusov "Побойся бога, как? чем он тебя прельстил?"

    famusov "Сама его безумным называла!"

    famusov "Нет! глупость на меня и слепота напала!"

    famusov "Все это заговор, и в заговоре был"

    famusov "Он сам, и гости все. За что я так наказан!.."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    hide chatskij

    show chatskij at left
    show sofija at right

    chatskij "<{i}(Софии){/i}>"

    hide sofija

    show chatskij at truecenter

    chatskij "Так этим вымыслом я вам еще обязан?"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Брат, не финти, не дамся я в обман,"

    famusov "Хоть подеретесь, не поверю."

    famusov "Ты, Филька, ты прямой чурбан,"

    famusov "В швейцары произвел ленивую тетерю,"

    famusov "Не знает ни про что, не чует ничего."

    famusov "Где был? куда ты вышел?"

    famusov "Сеней не запер для чего?"

    famusov "И как не досмотрел? и как ты не дослышал?"

    famusov "В работу вас, на поселенье вас:"

    famusov "За грош продать меня готовы."

    famusov "Ты, быстроглазая, всё от твоих проказ;"

    famusov "Вот он. Кузнецкий мост, наряды и обновы;"

    famusov "Там выучилась ты любовников сводить,"

    famusov "Постой же, я тебя исправлю:"

    famusov "Изволь-ка в и́збу, марш, за птицами ходить;"

    famusov "Да и тебя, мой друг, я, дочка, не оставлю;"

    famusov "Еще дни два терпение возьми;"

    famusov "Не быть тебе в Москве, не жить тебе с людьми."

    famusov "Подалее от этих хватов,"

    famusov "В деревню, к тетке, в глушь, в Саратов,"

    famusov "Там будешь горе горевать."

    famusov "За пяльцами сидеть, за святцами зевать."

    famusov "А вас, суда́рь, прошу я толком"

    famusov "Туда не жаловать ни прямо, ни проселком;"

    famusov "И ваша такова последняя черта,"

    famusov "Что, чай, ко всякому дверь будет заперта:"

    famusov "Я постараюсь, я, в набат я приударю,"

    famusov "По городу всему наделаю хлопот,"

    famusov "И оглашу во весь народ:"

    famusov "В Сенат подам, министрам, государю."

    hide famusov

    show chatskij at truecenter

    $ chatskij_var = "{noalt}Чацкий"

    chatskij "<{i}(после некоторого молчания){/i}>"

    chatskij "Не образумлюсь... виноват,"

    chatskij "И слушаю, не понимаю,"

    chatskij "Как будто всё еще мне объяснить хотят,"

    chatskij "Растерян мыслями... чего-то ожидаю."

    chatskij "<{i}(С жаром.){/i}>"

    chatskij "Слепец! я в ком искал награду всех трудов!"

    chatskij "Спешил!.. летел! дрожал! вот счастье, думал, близко."

    chatskij "Пред кем я давиче так страстно и так низко"

    chatskij "Был расточитель нежных слов!"

    chatskij "А вы! О боже мой! кого себе избрали?"

    chatskij "Когда подумаю, кого вы предпочли!"

    chatskij "Зачем меня надеждой завлекли?"

    chatskij "Зачем мне прямо не сказали,"

    chatskij "Что все прошедшее вы обратили в смех?"

    chatskij "Что память даже вам постыла"

    chatskij "Тех чувств, в обоих нас движений сердца тех,"

    chatskij "Которые во мне ни даль не охладила,"

    chatskij "Ни развлечения, ни перемена мест."

    chatskij "Дышал, и ими жил, был занят беспрерывно!"

    chatskij "Сказали бы, что вам внезапный мой приезд,"

    chatskij "Мой вид, мои слова, поступки — всё противно, —"

    chatskij "Я с вами тотчас бы сношения пресек,"

    chatskij "И перед тем, как навсегда расстаться,"

    chatskij "Не стал бы очень добираться,"

    chatskij "Кто этот вам любезный человек?.."

    chatskij "<{i}(Насмешливо.){/i}>"

    chatskij "Вы помиритесь с ним, по размышленьи зрелом."

    chatskij "Себя крушить, и для чего!"

    chatskij "Подумайте, всегда вы можете его"

    chatskij "Беречь, и пеленать, и спосылать за делом."

    chatskij "Муж-мальчик, муж-слуга, из жениных пажей —"

    chatskij "Высокий идеал московских всех мужей. —"

    chatskij "Довольно!.. с вами я горжусь моим разрывом."

    chatskij "А вы, суда́рь отец, вы, страстные к чинам:"

    chatskij "Желаю вам дремать в неведеньи счастливом,"

    chatskij "Я сватаньем моим не угрожаю вам."

    chatskij "Другой найдется благонравный,"

    chatskij "Низкопоклонник и делец,"

    chatskij "Достоинствами наконец"

    chatskij "Он будущему тестю равный."

    chatskij "Так! отрезвился я сполна,"

    chatskij "Мечтанья с глаз долой — и спала пелена;"

    chatskij "Теперь не худо б было сряду"

    chatskij "На дочь и на отца"

    chatskij "И на любовника-глупца,"

    chatskij "И на весь мир излить всю желчь и всю досаду."

    chatskij "С кем был! Куда меня закинула судьба!"

    chatskij "Все гонят! все клянут! Мучителей толпа,"

    chatskij "В любви предателей, в вражде неутомимых,"

    chatskij "Рассказчиков неукротимых,"

    chatskij "Нескладных умников, лукавых простяков,"

    chatskij "Старух зловещих, стариков,"

    chatskij "Дряхлеющих над выдумками, вздором, —"

    chatskij "Безумным вы меня прославили всем хором."

    chatskij "Вы правы: из огня тот выйдет невредим,"

    chatskij "Кто с вами день пробыть успеет,"

    chatskij "Подышит воздухом одним,"

    chatskij "И в нем рассудок уцелеет."

    chatskij "Вон из Москвы! сюда я больше не ездок."

    chatskij "Бегу, не оглянусь, пойду искать по свету,"

    chatskij "Где оскорбленному есть чувству уголок! —"

    chatskij "Карету мне, карету!"

    play sound1 horse_run

    chatskij "<{i}(Уезжает.){/i}>"

    stop sound1

    hide chatskij

label Act_4_Scene_15:
    "{b}Явление 15{/b}"

    show chatskij at truecenter

    "<{i}Кроме Чацкого.{/i}>"

    hide chatskij

    show famusov at truecenter

    $ famusov_var = "{noalt}Фамусов"

    famusov "Ну что? не видишь ты, что он с ума сошел?"

    famusov "Скажи сурьезно:"

    famusov "Безумный! что он тут за чепуху молол!"

    famusov "Низкопоклонник! тесть! и про Москву так грозно!"

    famusov "А ты меня решилась уморить?"

    famusov "Моя судьба еще ли не плачевна?"

    famusov "Ах! Боже мой! что станет говорить"

    famusov "Княгиня Марья Алексевна!"

    hide famusov


