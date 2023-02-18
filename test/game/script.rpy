"Благородный театр"

"The Noble Theatre"

"Комедия в четырех действиях, в стихах"

"A Comedy in Four Act, in Verse"

"Михаил"

"Николаевич"

"Загоскин"

"Mikhail"

"Zagoskin"

"Q629784"

"DraCor"

"CC0 1.0"

"Licence"

"Библиотека Максима Мошкова (lib.ru)"

"http://az.lib.ru/z/zagoskin_m_n/text_0160.shtml"

"<{i}In the public domain.{/i}>"

"<{i}Серия \"Библиотека поэта\". Большая серия. Второе издание. М.-Л., \"Советский писатель\", 1964{/i}>"

define lyubskij = Character("lyubskij_var", color="#FFB300", dynamic=True)
define izvedov = Character("izvedov_var", color="#803E75", dynamic=True)
define pososhkov = Character("pososhkov_var", color="#FF6800", dynamic=True)
define velskij = Character("velskij_var", color="#A6BDD7", dynamic=True)
define biryulkin = Character("biryulkin_var", color="#C10020", dynamic=True)
define lileev = Character("lileev_var", color="#CEA262", dynamic=True)
define chestonov = Character("chestonov_var", color="#817066", dynamic=True)
define mestonov = Character("mestonov_var", color="#007D34", dynamic=True)
define pervyj_sluga = Character("pervyj_sluga_var", color="#F6768E", dynamic=True)
define pervyj_plemyannik = Character("pervyj_plemyannik_var", color="#00538A", dynamic=True)
define vtoroj_plemyannik = Character("vtoroj_plemyannik_var", color="#FF7A5C", dynamic=True)
define volgin = Character("volgin_var", color="#53377A", dynamic=True)
define vtoroj_sluga = Character("vtoroj_sluga_var", color="#FF8E00", dynamic=True)
define uchitel = Character("uchitel_var", color="#B32851", dynamic=True)
define lyubskaya = Character("lyubskaya_var", color="#F4C800", dynamic=True)
define olenka = Character("olenka_var", color="#7F180D", dynamic=True)
define natasha = Character("natasha_var", color="#93AA00", dynamic=True)
define kutermina = Character("kutermina_var", color="#593315", dynamic=True)
define pervaja_plemyannica = Character("pervaja_plemyannica_var", color="#F13A13", dynamic=True)
define vtoraja_plemyannica = Character("vtoraja_plemyannica_var", color="#232C16", dynamic=True)
define guvernantka = Character("guvernantka_var", color="#AA750D", dynamic=True)
define nyanjushka = Character("nyanjushka_var", color="#2C20AE", dynamic=True)

"Comedy"

"Q40831"

"(eg) convert from source"

label start:
    play music "audio/music/117.mp3" fadeout 1.0 fadein 1.0

    scene 56 with fade

    "Благородный театр"

    "Комедия в четырех действиях, в стихах"

    menu:
        "{color=#000}ДЕЙСТВУЮЩИЕ ЛИЦА{/color}":
            jump Characters_1
        "{color=#000}epigraph{/color}":
            jump EPIGRAPH_1_1_1
        "{color=#000}set{/color}":
            jump SET_2_2_1
        "{color=#000}ДЕЙСТВИЕ ПЕРВОЕ{/color}":
            jump Act_3
        "{color=#000}ДЕЙСТВИЕ ВТОРОЕ{/color}":
            jump Act_4
        "{color=#000}ДЕЙСТВИЕ ТРЕТЬЕ{/color}":
            jump Act_5
        "{color=#000}ДЕЙСТВИЕ ЧЕТВЕРТОЕ{/color}":
            jump Act_6

    label Characters_1:
        play music "audio/music/34.mp3" fadeout 1.0 fadein 1.0

        scene 61 with fade

        "{b}ДЕЙСТВУЮЩИЕ ЛИЦА{/b}"

        show lyubskij at truecenter
        "Г. Любский, дядя Оленьки."
        hide lyubskij

        show lyubskaya at truecenter
        "Г-жа Любская, жена его."
        hide lyubskaya

        show olenka at truecenter
        "Оленька, племянница их."
        hide olenka

        show velskij at truecenter
        "Вельский, влюбленный в Оленьку."
        hide velskij

        show chestonov at truecenter
        "Честонов, брат Любского, от другого отца."
        hide chestonov

        show volgin at truecenter
        "Волгин, дядя Вельского."
        hide volgin

        show pososhkov at truecenter
        "Посошков, жених Оленьки."
        hide pososhkov

        show kutermina at truecenter
        "Кутермина, знакомая Любских."
        hide kutermina

        show lileev at truecenter
        "Лилеев"
        hide lileev

        show biryulkin at truecenter
        "Бирюлькин"
        hide biryulkin

        "актеры Благородной труппы"

        show izvedov at truecenter
        "Изведов, отставной придворный актер."
        hide izvedov

        show natasha at truecenter
        "Наташа, горничная Оленьки."
        hide natasha

        show pervaja_plemyannica at truecenter
        "1-я племянница"
        hide pervaja_plemyannica

        show vtoraja_plemyannica at truecenter
        "2-я племянница"
        hide vtoraja_plemyannica

        show pervyj_plemyannik at truecenter
        "1-й племянник"
        hide pervyj_plemyannik

        show vtoroj_plemyannik at truecenter
        "2-й племянник"
        hide vtoroj_plemyannik

        "Кутерминой."

        show pervyj_sluga at truecenter
        "1-й"
        hide pervyj_sluga

        show vtoroj_sluga at truecenter
        "и 2-й"
        hide vtoroj_sluga

        "слуги Любского"

        "4 девочки"

        "2 мальчика"

        show uchitel at truecenter
        "Учитель"
        hide uchitel

        show guvernantka at truecenter
        "Гувернантка"
        hide guvernantka

        show nyanjushka at truecenter
        "Нянюшка"
        hide nyanjushka

        "без слов."


    label EPIGRAPH_1_1_1:
        play music "audio/music/74.mp3" fadeout 1.0 fadein 1.0

        scene 62 with fade

        "{b}epigraph{/b}"

        "{a=myshow|tooltip|text=Это для тех, кто молод, влюблен, для принцев или принцесс. А театр - часто прелестный сюжет для пьесы.}C'est a qui sera jeune, amant, prince ou princesse. Et la troupe est souvent un beau sujet de piece.{/a}"

        "<{i}{a=myshow|tooltip|text=Делиль (франц.). - Ред.}Delille{/a}{/i}>"




    label SET_2_2_1:
        play music "audio/music/108.mp3" fadeout 1.0 fadein 1.0

        scene 5 with fade

        "{b}set{/b}"

        show lyubskij at truecenter

        show lyubskij at truecenter

        "<{i}Действие происходит в губернском городе, в доме Любского.{/i}>"

        hide lyubskij

        hide lyubskij




label Act_3:
    play music "audio/music/99.mp3" fadeout 1.0 fadein 1.0

    scene 40 with fade

    "{b}ДЕЙСТВИЕ ПЕРВОЕ{/b}"

    menu:
        "{color=#000}ЯВЛЕНИЕ 1{/color}":
            jump Act_0_Scene_1
        "{color=#000}ЯВЛЕНИЕ 2{/color}":
            jump Act_0_Scene_2
        "{color=#000}ЯВЛЕНИЕ 3{/color}":
            jump Act_0_Scene_3
        "{color=#000}ЯВЛЕНИЕ 4{/color}":
            jump Act_0_Scene_4
        "{color=#000}ЯВЛЕНИЕ 5{/color}":
            jump Act_0_Scene_5
        "{color=#000}ЯВЛЕНИЕ 6{/color}":
            jump Act_0_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_0_Scene_6_1

label Further_Act_0_Scene_6_1:
    menu:
        "{color=#000}ЯВЛЕНИЕ 7{/color}":
            jump Act_0_Scene_7
        "{color=#000}ЯВЛЕНИЕ 8{/color}":
            jump Act_0_Scene_8
        "{color=#000}ЯВЛЕНИЕ 9{/color}":
            jump Act_0_Scene_9
        "{color=#000}ЯВЛЕНИЕ 10{/color}":
            jump Act_0_Scene_10
        "{color=#000}ЯВЛЕНИЕ 11{/color}":
            jump Act_0_Scene_11
        "{color=#000}ЯВЛЕНИЕ 12{/color}":
            jump Act_0_Scene_12
        "{color=#000}>{/color}":
            jump Further_Act_0_Scene_12_2

label Further_Act_0_Scene_12_2:
    menu:
        "{color=#000}ЯВЛЕНИЕ 13{/color}":
            jump Act_0_Scene_13
        "{color=#000}ЯВЛЕНИЕ 14{/color}":
            jump Act_0_Scene_14

    label Act_0_Scene_1:
        "{b}ЯВЛЕНИЕ 1{/b}"

        show pososhkov at left
        show velskij at truecenter
        show izvedov at right

        show pososhkov at left
        show velskij at truecenter
        show izvedov at right

        "<{i}Г-жа Любская, Оленька, Наташа, Любский, Посошков, Вельский и Изведов.{/i}>"

        hide lyubskaya
        hide olenka
        hide natasha
        hide lyubskij
        hide pososhkov
        hide velskij
        hide izvedov

        hide lyubskaya
        hide olenka
        hide natasha
        hide lyubskij
        hide pososhkov
        hide velskij
        hide izvedov

        show natasha at truecenter

        show natasha at truecenter

        "<{i}Все сидят, включая Изведова и Наташу.{/i}>"

        hide natasha

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Итак, мои друзья, спектаклю должно быть"

        lyubskij "Сегодня ввечеру. Прошу не позабыть,"

        lyubskij "Что ровно в семь часов начнется представленье;"

        lyubskij "Потом дадим мы бал, и, верно, угощенье"

        lyubskij "Весь город удивит. Не правда ли, жена?"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Конечно, удивит. Ну, те ли времена,"

        lyubskaya "Чтоб праздники давать?"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Опять браниться стала!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Да, да! Рублей пятьсот как будто б не бывало."

        lyubskaya "К чему, сударь, зачем? Большая ведь нужда..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "И полно, матушка! - Ну, что же, господа?"

        lyubskij "Пора бы, кажется, за пробу приниматься."

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Конечно бы пора; но должно всем собраться."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Слуги и дяди нет."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да что за чудеса!"

        lyubskij "Их вечно нет как нет."

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}А скоро два часа."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Мне кажется, в таких делах единодушно"

        pososhkov "Все действовать должны, а это уж и скучно,"

        pososhkov "Всё я, да я: толкуй, показывай, учи,"

        pososhkov "Пиесу сочиняй, со всеми хлопочи."

        pososhkov "За что?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ох, эти мне Бирюлькин и Лилеев!"

        lyubskij "Всегда последние."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}От этих нам злодеев"

        pososhkov "Житья уж вовсе нет, играют хуже всех ..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Сердись на них, брани, - а им лишь только смех."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Последней не хотят порядком сделать пробы."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Изволь их ждать! Да что за важные особы?"

        lyubskij "Уж им опаздывать! - Бирюлькин, например,"

        lyubskij "Ведь барин небольшой - в отставке землемер,"

        lyubskij "Актер весьма плохой и человек прескучный."

        lyubskij "По милости моей имеет хлеб насущный,"

        lyubskij "И если б только я хотел его прижать..."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Вот то-то, батюшка, всех хочешь одолжать,"

        lyubskaya "Готов хоть всё отдать за пару комплиментов."

        lyubskaya "Он год по векселю не платит и процентов,"

        lyubskaya "А ты, сударь, молчишь."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну да, теперь молчу,"

        lyubskij "Зато уж после я порядкам проучу,"

        lyubskij "И если вечером по нашему желанью"

        lyubskij "Пиеса не пойдет, так вексель ко взысканыо."

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Он болен, может быть."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И это не резон,"

        lyubskij "Уж мне наскучило терпеть."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да вот и он."

        hide pososhkov

    label Act_0_Scene_2:
        "{b}ЯВЛЕНИЕ 2{/b}"

        show biryulkin at truecenter

        show biryulkin at truecenter

        "<{i}Те же и Бирюлькин.{/i}>"

        hide biryulkin

        hide biryulkin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Помилуй, батюшка! на что это похоже?"

        hide lyubskij

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Простите, виноват!"

        hide biryulkin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Всегда одно и то же!"

        hide pososhkov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Делишки завелись: сейчас в Палате был,"

        biryulkin "Насилу вырвался."

        hide biryulkin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}А это позабыл,"

        lyubskij "Что ты еще путем своей не знаешь роли?"

        hide lyubskij

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Не смея выступить никак из вашей воли,"

        biryulkin "Я всячески твержу, учусь, измучен весь, -"

        biryulkin "И если б не дела..."

        hide biryulkin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Дела-то, сударь, здесь."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Не знаете ль, куда Лилеев наш девался?"

        hide pososhkov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Гуляет, кажется, сейчас лишь мне попался."

        hide biryulkin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Гуляет! Боже мой!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ну есть ли совесть в нем!"

        pososhkov "Уж скоро третий час, когда же мы начнем?"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(Любскому){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        pososhkov "Хоть этот раз его порядком побраните."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Всё это, братец, ты."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}За что ж меня вините?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "За то, что без тебя мне в ум бы не пришло"

        lyubskij "Театры заводить."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Когда на то пошло,"

        pososhkov "Позвольте ж вам сказать, и вы не слишком правы:"

        pososhkov "Театр мы завели для собственной забавы,"

        pososhkov "Так вам бы пригласить порядочных людей,"

        pososhkov "На что Лилеев вам?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Уж подлинно злодей!"

        lyubskij "И как смел думать он, что может нас дурачить?"

        lyubskij "Откуда спесь взялась? И что он в свете значит?"

        lyubskij "Беспутный мот, давно известный за глупца,"

        lyubskij "Седой столетний франт, пленяющий сердца,"

        lyubskij "Всемирный шут, нахал, болтун и лжец бесстыдный,"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "А сверх того талант нимало не завидный:"

        pososhkov "Бормочет прозою, коверкает стихи,"

        pososhkov "Ну словом, истинно актер он за грехи."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Какой актер! Пустой актеришка, превздорный!"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Тс! тише, он идет."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Так что ж?.."

        hide lyubskij

    label Act_0_Scene_3:
        "{b}ЯВЛЕНИЕ 3{/b}"

        show lileev at truecenter

        show lileev at truecenter

        "<{i}Те же и Лилеев.{/i}>"

        hide lileev

        hide lileev

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        hide lileev

        show lileev at truecenter

        hide lileev

        show lileev at truecenter

        lileev "<{i}(кланяясь){/i}>"

        show lileev at truecenter

        show lileev at truecenter

        lileev "{space=400}Слуга покорный!"

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Насилу дождались."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Здорово, милый мой!"

        lyubskij "А я было хотел послать к тебе домой."

        lyubskij "Скажи, пожалуйста, боишься ли ты бога!.."

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "А что?"

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Уж третий час."

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Я опоздал немного."

        lileev "Ну что же? Не беда."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Конечно, не беда,"

        pososhkov "И это может быть со всяким - иногда,"

        pososhkov "Но каждый раз..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Мы всё сносили терпеливо,"

        lyubskij "Теперь позволь сказать: ведь это неучтиво,"

        lyubskij "Заставить ждать..."

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Так что ж? Вина невелика."

        lileev "К тому ж вы знаете, я ролю старика"

        lileev "Взялся играть у вас единственно из дружбы."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Но вы..."

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Ах, боже мой! да это хуже службы!"

        lileev "Неужто должен я для ваших всех затей"

        lileev "Забыть родных своих, знакомых и друзей,"

        lileev "С утра до вечера ничем не заниматься,"

        lileev "От всех веселостей охотой отказаться -"

        lileev "И даже не гулять? - Нет, нет! благодарю!"

        lileev "Да этак я себя в неделю уморю."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Зачем брались..."

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Зачем?.. Вы точно, сударь, правы:"

        lileev "Не должно бы никак, для собственной мне славы,"

        lileev "Везде любовников играя молодых,"

        lileev "Показывать себя в таких ролях пустых."

        lileev "Возьмите, вот она!"

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И как тебе не стыдно!"

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "Да что ж? помилуйте! Мне это уж обидно:"

        lileev "Я жертвую собой, хочу вам угодить,"

        lileev "Меня ж бранят."

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну вот! нельзя и пошутить."

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        hide lileev

        show lileev at left
        show pososhkov at right

        hide lileev

        show lileev at left
        show pososhkov at right

        lileev "<{i}(Посошкову){/i}>"

        hide pososhkov

        show lileev at truecenter

        hide pososhkov

        show lileev at truecenter

        lileev "Я, кажется, от вас нимало не завишу."

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "И полно, брат!"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Прочесть позволите ль афишу?"

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "А что, затейлива?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Старался сколько мог."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Напрасно не сказал, а то бы я помог."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Уж верно, хороша! Он был актер придворный"

        lyubskij "И малый умница - досужий и проворный."

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(кланяясь){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Помилуйте!"

        hide izvedov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Да, да! и ловок и остер."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "К тому ж, при нем скажу, отличнейший суфлер."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(читает афишу){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "\"Сегодня, в пятницу, в доме Степана Ивановича Любского Обществом любителей театра представлена будет в первый раз \"Осмеянный опекун\", комедия в трех действиях, сочинение г-на Посошкова...\""

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Нельзя ли это вон?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Зачем, сударь? Напрасно!"

        lyubskij "Комедия твоя написана прекрасно."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Но я бы не хотел..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И полно, братец, вздор!"

        lyubskij "Пусть знают все, что ты и автор и актер."

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(читает){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "\"Действующие лица: г. Сундуков, опекун Лизы - Авдей Михайлович Посошков; Лиза, богатая сирота - Ольга Дмитриевна Любская...\""

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Смотри, племянница, всю ролю знать до слова!"

        hide lyubskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "Она уж у меня недели две готова."

        hide olenka

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(читает){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "\"Эраст, влюбленный в Лизу, Андрей Степанович Вельский\"."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "Вот истинный талант! От вас я без души."

        pososhkov "В любовных сценах вы отлично хороши:"

        pososhkov "Натура чистая!"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(читает){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "\"Сурский, дядя Лизы Сергей Иванович Лилеев; Антропка, Эрастов слуга Максим Петрович Бирюлькин; Машенька, служанка Лизы - госпожа... госпожа...\""

        izvedov "{space=400}Признаться откровенно,"

        izvedov "Об вас не сказано."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}А должно непременно."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Конечно, так, но я ужасно затруднен:"

        izvedov "Не знаю, как назвать."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ты, право, мне смешон,"

        lyubskij "Неужто позабыл? Она питомка наша,"

        lyubskij "Дочь крестная моя, по имени Наташа."

        lyubskij "Ну вот тебе и всё!"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Я это знаю сам."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Так что ж еще?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Нельзя ж актрис по именам"

        izvedov "В афише называть, - ведь это неучтиво:"

        izvedov "Фамилия нужна."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Она, брат, неспесива."

        lyubskij "Как хочешь назови. Отец ее Панфил"

        lyubskij "Был управителем, а чванства не любил,"

        lyubskij "Служил мне попросту и верен был до гроба,"

        lyubskij "За то и дочь его люблю."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Когда же проба?"

        pososhkov "Мы вечно не начнем."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Позвольте дочитать."

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(Читает){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "\"Начало в 7 часов. Все гости равно любезны хозяину, следовательно, и места все равные; плата за оные дружба и снисхождение зрителей: это отменно дорого, но хозяин дешевле уступить не может\"."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Прекрасно, милый мой!"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Так можно и в печать?"

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Пошли скорей. Смотри, чтоб к вечеру поспела."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Теперь всё кончено, пора бы нам за дело."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "А что, позавтракать у вас охоты нет?"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "И, батюшка! к чему? Испортите обед."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Всё лучше закусить."

        hide lyubskij

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}И я такой же веры."

        hide biryulkin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Пойдемте ж, господа, - по рюмочке мадеры,"

        lyubskij "А там и на театр."

        hide lyubskij

        show izvedov at left
        show natasha at right

        show izvedov at left
        show natasha at right

        "<{i}Уходят все. Изведов останавливает Наташу.{/i}>"

        hide izvedov
        hide natasha

        hide izvedov
        hide natasha

    label Act_0_Scene_4:
        "{b}ЯВЛЕНИЕ 4{/b}"

        show izvedov at left
        show natasha at right

        show izvedov at left
        show natasha at right

        "<{i}Изведов и Наташа.{/i}>"

        hide izvedov
        hide natasha

        hide izvedov
        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Постой, моя душа!"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Ну что?"

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Сегодня ты как ангел хороша."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Благодарю."

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(Хочет идти.){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=200}Куда ж?"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}С тобой болтать пустого"

        natasha "Мне некогда, прощай!"

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Позволь сказать два слова."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Какой привязчивый! - Чего же хочешь ты?"

        natasha "Ну, говори скорей."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}О, чудо красоты!"

        izvedov "Собор всех прелестей! и горничных царица!"

        izvedov "Скажи, доколь судьбы жестокая десница,"

        izvedov "Или ясней сказать: свирепая рука ..."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Ты что-то говоришь некстати свысока."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Служив пять месяцев с успехом Мельпомене,"

        izvedov "Я точно так всегда говаривал на сцене."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Да здесь ведь не театр, и ты уж не актер."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Зато артист в душе - и страшный аматер."

        izvedov "Но дело не о том: когда же наша свадьба?"

        izvedov "Ты знаешь, у меня прекрасная усадьба"

        izvedov "И домик щегольской; есть деньги по рукам,"

        izvedov "И если крестный твой отец поможет нам,"

        izvedov "Откроем здесь театр; лишь надобно терпенье,"

        izvedov "А труппу заведем, без всякого сомненья;"

        izvedov "Ты будешь представлять цариц, а я царей."

        izvedov "Ну, что же, ангел мой, решайся поскорей."

        izvedov "Тут думать нечего."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Прошу не торопиться."

        natasha "Во-первых, барин мой..."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Он, верно, согласится."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Всё так, но признаюсь, мне свадьба в ум нейдет;"

        natasha "Как вспомню барышню, так сердце и замрет."

        natasha "Вот, милый, каково остаться сиротою!"

        natasha "Что к Вельскому она привязана душою."

        natasha "Ты это знаешь сам, а что еще верней -"

        natasha "Несносный Посошков всего противней ей,"

        natasha "И несмотря на то, ему уж слово дали."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Неужто Вельскому сегодня отказали?"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "О, нет еще: теперь он надобен для нас."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Так завтра поутру..."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Решительный отказ."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "А всё, чай, дядюшка! Да как ему не стыдно"

        izvedov "Губить племянницу! - Подумать-то обидно:"

        izvedov "Ну этот Посошков годится ль ей в мужья?"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "На месте Вельского на всё б решилась я."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Не знаю, как тебе, а мне он очень жалок:"

        izvedov "Влюблен, надежды нет, и к этому вдобавок"

        izvedov "Сегодня должен с ней любовника играть -"

        izvedov "Не больно ли, скажи?"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Уж нечего сказать."

        natasha "Поверишь ли? На них измучилась я глядя."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "А что, мой друг, ведь ей Честонов также дядя."

        izvedov "Неужели и он не хочет ей помочь?"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "О нет! Он барышню любил всегда, как дочь,"

        natasha "И этой свадьбою не может быть доволен,"

        natasha "Но он теперь в Москве, два месяца как болен"

        natasha "И - об заклад побьюсь - не знает ничего."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Нельзя ли как-нибудь уведомить его?"

        izvedov "Что, если б ты к нему об этом написала?"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Недолго написать, да пользы будет мало."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "А я так думаю, что он поможет нам."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Ох, трудно, милый мой! Старик наш так упрям,"

        natasha "Что Вельскому помочь нет средства никакого."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Постигнуть не могу! И как для Посошкова"

        izvedov "Решиться отказать такому молодцу!"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Молчи! Мне кажется, подъехали к крыльцу..."

        natasha "Ну, так и есть."

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(Хочет идти.){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Постой! Чего ж ты испугалась?"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Пусти! И так с тобой я слишком заболталась."

        natasha "Прощай!"

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(Убегает.){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        hide natasha

    label Act_0_Scene_5:
        "{b}ЯВЛЕНИЕ 5{/b}"

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at left
        show natasha at right

        hide izvedov

        show izvedov at left
        show natasha at right

        izvedov "<{i}(один, глядя вслед за Наташей){/i}>"

        hide natasha

        show izvedov at truecenter

        hide natasha

        show izvedov at truecenter

        izvedov "{space=400}Вот золото! - Решительно скажу:"

        izvedov "Женясь на ней, театр я смело завожу,"

        izvedov "С такой актрисою мне нечего бояться."

        izvedov "Ей только надобно на сцену показаться,"

        izvedov "А то сведет с ума всю нашу молодежь."

        izvedov "И подлинно, такой субретки не найдешь,"

        izvedov "Хоть из конца в конец объезди всю Европу;"

        izvedov "А здесь, в губернии, - сыграет и Меропу!"

        hide izvedov

    label Act_0_Scene_6:
        "{b}ЯВЛЕНИЕ 6{/b}"

        show izvedov at left
        show chestonov at right

        show izvedov at left
        show chestonov at right

        "<{i}Изведов и Честонов.{/i}>"

        hide izvedov
        hide chestonov

        hide izvedov
        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Возможно ль! Николай Степаныч - это вы!"

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Изведов! Здравствуй, брат!"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Давно ли из Москвы?"

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Вчера приехал в ночь."

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Вы нас совсем забыли."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Я болен был; к тому ж мне голову вскружили,"

        chestonov "Измучили совсем проклятые дела."

        chestonov "Ну, что племянница? Здорова, весела?"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "О нет, сударь! Она теперь..."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Степенней стала?"

        chestonov "Тем лучше для нее."

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Вы помните, бывало,"

        izvedov "Смеется целый день, а нынче иногда..."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Не резвится? Так что ж? На всё свои года,"

        chestonov "И резвость прежняя была бы не у места:"

        chestonov "Ей скоро двадцать лет, к тому ж она невеста..."

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Так вы уж знаете?.."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Сегодня поутру"

        chestonov "Узнал я всё. Как жаль покойную сестру!"

        chestonov "Какая б радость ей! Но жалобы напрасны:"

        chestonov "Ее не воскресишь!"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(с удивлением){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=400}Так вы, сударь, согласны?"

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "На что?.. На свадьбу их? А почему ж не так?"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(в сторону){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Возможно ли! И вы!.. Попался я впросак!"

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "И что тут странного! - Что Оленька счастлива,"

        chestonov "Сомненья в этом нет. Хоть очень прихотлива"

        chestonov "На выбор женихов покойница была,"

        chestonov "А лучше б мужа ей, конечно, не нашла:"

        chestonov "Он добр, умен; хотя фамилии незнатной,"

        chestonov "Но старый дворянин, наружности приятной..."

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Помилуйте!"

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}К тому ж отменно скромен, тих..."

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Кто? Он, сударь?"

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Ну да! Племянницын жених."

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Так вы найдете в нем большую перемену,"

        izvedov "Позвольте вам сказать..."

        hide izvedov

    label Act_0_Scene_7:
        "{b}ЯВЛЕНИЕ 7{/b}"

        show biryulkin at truecenter

        show biryulkin at truecenter

        "<{i}Те же и Бирюлькин.{/i}>"

        hide biryulkin

        hide biryulkin

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        hide biryulkin

        show biryulkin at left
        show izvedov at right

        hide biryulkin

        show biryulkin at left
        show izvedov at right

        biryulkin "<{i}(Изведову){/i}>"

        hide izvedov

        show biryulkin at truecenter

        hide izvedov

        show biryulkin at truecenter

        biryulkin "{space=400}Вас ждут давно на сцену."

        hide biryulkin

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Начните без меня."

        hide izvedov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Без вас нельзя никак."

        hide biryulkin

        show biryulkin at truecenter

        hide biryulkin

        show biryulkin at truecenter

        biryulkin "<{i}(Тихо){/i}>"

        show biryulkin at truecenter

        show biryulkin at truecenter

        biryulkin "Кто этот господин? Честонов, точно так!"

        biryulkin "Позвольте, батюшка, с приездом вас поздравить."

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "А, старый друг!"

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Во сне не мог себе представить"

        biryulkin "Такой я радости, - и вижу наяву."

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Как поживаешь, брат?"

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Да так, кой-как живу."

        hide biryulkin

        show biryulkin at left
        show izvedov at right

        hide biryulkin

        show biryulkin at left
        show izvedov at right

        biryulkin "<{i}(Изведову){/i}>"

        hide izvedov

        show biryulkin at truecenter

        hide izvedov

        show biryulkin at truecenter

        biryulkin "Ступайте же!"

        hide biryulkin

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Мы вас должны оставить оба:"

        izvedov "На пробу нас зовут."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да что у вас за проба?"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Сегодня здесь театр."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}Театр?"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}А после бал."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Театр? - Вот этого никак не ожидал!"

        chestonov "Кой черт! Да кто ж у вас? Хозяин сам актером?"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "О нет, сударь!"

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}Так вы?"

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Я только что суфлером,"

        izvedov "А вот один артист."

        hide izvedov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Бирюлькин! Что ты, брат!"

        chestonov "В своем ли ты уме!"

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Отец! и сам не рад,"

        biryulkin "Да делать нечего."

        hide biryulkin

        show biryulkin at left
        show izvedov at right

        hide biryulkin

        show biryulkin at left
        show izvedov at right

        biryulkin "<{i}(Изведову){/i}>"

        hide izvedov

        show biryulkin at truecenter

        hide izvedov

        show biryulkin at truecenter

        biryulkin "{space=400}Уж вам прочтут рацею!"

        biryulkin "Ступайте поскорей!"

        hide biryulkin

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=200}А вы, сударь?"

        hide izvedov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Успею."

        biryulkin "Я в первом действии совсем не выхожу."

        hide biryulkin

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at left
        show chestonov at right

        hide izvedov

        show izvedov at left
        show chestonov at right

        izvedov "<{i}(Честонову){/i}>"

        hide chestonov

        show izvedov at truecenter

        hide chestonov

        show izvedov at truecenter

        izvedov "Позвольте мне! - Об вас я братцу доложу."

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(Уходит.){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        hide izvedov

    label Act_0_Scene_8:
        "{b}ЯВЛЕНИЕ 8{/b}"

        show biryulkin at left
        show chestonov at right

        show biryulkin at left
        show chestonov at right

        "<{i}Бирюлькин и Честонов.{/i}>"

        hide biryulkin
        hide chestonov

        hide biryulkin
        hide chestonov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(улыбаясь){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "Так вы, сударь, актер? Неужто в самом деле?"

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Эх, батюшка! Чуть-чуть душа осталась в теле!"

        biryulkin "Совсем замучили! - Пускай бы два стиха!"

        biryulkin "Нет, сотню выучи!.. А память-та плоха:"

        biryulkin "Твердить примусь - беда! начнет душить зевота,"

        biryulkin "К тому же у меня и кашель и перхота -"

        biryulkin "Ну что я за актер!"

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Нельзя же без труда"

        chestonov "Актером быть. Когда старик в твои года"

        chestonov "Захочет в резвостях тягаться с молодыми,"

        chestonov "Так должен всё сносить."

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Конечно, так - кто с ними"

        biryulkin "Проказит заодно, а я, почтенный мой,"

        biryulkin "И знать их не хочу: мне надобен покой."

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Но разве ты не мог отделаться от роли?"

        chestonov "Зачем брался?"

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Зачем? Возьмешься поневоле,"

        biryulkin "Когда на старости пугнут тебя судом."

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Судом?"

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Я думаю, известны вы о том,"

        biryulkin "Что братцу вашему еще в запрошлом лете,"

        biryulkin "Имея на беду покупочку в предмете,"

        biryulkin "Рублей до тысячи я как-то задолжал."

        biryulkin "Хоть тысяча рублей неважный капитал,"

        biryulkin "Но так как у меня весь хлеб побило градом,"

        biryulkin "А что осталося, пришлось продать с накладом,"

        biryulkin "К тому же мужички не выслали оброк,"

        biryulkin "Так деньги я внести по векселю не мог."

        biryulkin "Ваш братец, знаете, зовет меня соседом"

        biryulkin "И жалует. Ну вот - однажды за обедом"

        biryulkin "Изволит говорить: \"Послушай-ка, сосед,"

        biryulkin "Заводим мы театр, в тебе хоть толку нет,"

        biryulkin "Однако ж так и быть, ступай и ты в актеры\"."

        biryulkin "Вот я было и прочь! - Куда-те! Хоть до ссоры!"

        biryulkin "Как крикнет, батюшка: \"Со мною не шути!"

        biryulkin "Прошу играть, не то - по векселю плати!\""

        biryulkin "-\"Да что я за актер? Ведь мне шестой десяток\"."

        biryulkin "- \"Не хочешь, так плати!\" - \"Дождитеся хоть святок!"

        biryulkin "Я всё с процентами сполна вам заплачу\"."

        biryulkin "- \"Нет! В суд!\" - \"Помилуйте!\" - \"И слышать не хочу!"

        biryulkin "А впрочем, не играй - ведь я, брат, не неволю\"."

        biryulkin "Что делать? Замолчал. В карман пихнули ролю,"

        biryulkin "Очнуться не дали..."

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}И жалко и смешно."

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Дурачить так меня, ей-ей, отец, грешно!"

        biryulkin "Во мне же вовсе нет способностей природных."

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(улыбаясь){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "А, верно, ты попал на роли благородных"

        chestonov "Отцов, - а может быть, и знатный господин?.."

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "И должно б так: ведь я природный дворянин."

        biryulkin "Так нет, сударь. Меня упрятали в холопы."

        biryulkin "Ну, легче б, кажется, идти мне в рудокопы,"

        biryulkin "А делать нечего: хоть плачь, а будь актер."

        biryulkin "Век с честию служил, уж двадцать лет майор -"

        biryulkin "И мне лакеем быть!.."

        hide biryulkin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}По чести, это больно."

        hide chestonov

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Вестимо, батюшка! да дело-то не вольно."

        biryulkin "Одно из двух: плати - не то играй слугу,"

        biryulkin "Попробуй отказать, так он согнет в дугу."

        hide biryulkin

    label Act_0_Scene_9:
        "{b}ЯВЛЕНИЕ 9{/b}"

        show lyubskij at left
        show lyubskaya at truecenter
        show olenka at right

        show lyubskij at left
        show lyubskaya at truecenter
        show olenka at right

        "<{i}Те же, Любский, Любская и Оленька.{/i}>"

        hide lyubskij
        hide lyubskaya
        hide olenka

        hide lyubskij
        hide lyubskaya
        hide olenka

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(обнимается){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Насилу бог принес! Какими, брат, судьбами?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Хотелось поскорей увидеться мне с вами."

        hide chestonov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "Любезный дядюшка!"

        hide olenka

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(обнимая ее){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "{space=400}Здорово, милый друг."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ты здесь? - Послушай, брат! Теперь ей недосуг -"

        lyubskij "Позволь..."

        hide lyubskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "{space=400}Ах, дядюшка!.. - А я было хотела..."

        hide olenka

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ступай, сударыня!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}Зачем?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да так, есть дело."

        hide lyubskij

        show lyubskij at left
        show biryulkin at right

        hide lyubskij

        show lyubskij at left
        show biryulkin at right

        lyubskij "<{i}(Бирюлькину){/i}>"

        hide biryulkin

        show lyubskij at truecenter

        hide biryulkin

        show lyubskij at truecenter

        lyubskij "А ты что здесь?"

        hide lyubskij

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Охти! Попался я в беду!"

        hide biryulkin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну, что стоишь! пошел!"

        hide lyubskij

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Иду, сударь, иду!"

        hide biryulkin

        show biryulkin at left
        show olenka at right

        show biryulkin at left
        show olenka at right

        "<{i}Бирюлькин и Оленька уходят.{/i}>"

        hide biryulkin
        hide olenka

        hide biryulkin
        hide olenka

    label Act_0_Scene_10:
        "{b}ЯВЛЕНИЕ 10{/b}"

        show olenka at truecenter

        show olenka at truecenter

        "<{i}Те же, без Бирюлькина и Оленьки.{/i}>"

        hide olenka

        hide olenka

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Как это, батюшка, пустился ты в дорогу?"

        lyubskaya "Проезду вовсе нет."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Однако ж, слава богу,"

        chestonov "Доехал как-нибудь."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ты, верно, брат, устал?"

        lyubskij "Но делать нечего: у нас сегодня бал."

        lyubskij "Как хочешь, а прошу со мною веселиться."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Нельзя ль помиловать?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Вот это не годится."

        lyubskij "В столице побывал, так с ним не говори."

        lyubskij "Наш город не Москва, однако ж посмотри,"

        lyubskij "Как мы пируем здесь - не хуже вашей знати!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Ох, эти мне пиры! Совсем бы нам некстати!"

        lyubskaya "Доходов нет..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну, так! Одно всё в голове!"

        lyubskij "Да полно, матушка!"

        hide lyubskij

        show lyubskij at left
        show chestonov at right

        hide lyubskij

        show lyubskij at left
        show chestonov at right

        lyubskij "<{i}(Честонову){/i}>"

        hide chestonov

        show lyubskij at truecenter

        hide chestonov

        show lyubskij at truecenter

        lyubskij "{space=400}Услышат и в Москве,"

        lyubskij "Как мы живем. Ни в чем не будет упущенья:"

        lyubskij "И танцы и театр - а что за угощенье!"

        lyubskij "Какого подадут отличного вина!.."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "И верно, выпьют всё!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Уймешься ль ты, жена?"

        hide lyubskij

        show lyubskij at left
        show chestonov at right

        hide lyubskij

        show lyubskij at left
        show chestonov at right

        lyubskij "<{i}(Честонову){/i}>"

        hide chestonov

        show lyubskij at truecenter

        hide chestonov

        show lyubskij at truecenter

        lyubskij "Послушай, милый мой, сказать ли по секрету?"

        lyubskij "Есть свадебка у нас."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да я уж новость эту"

        chestonov "Узнал и без тебя и всей душою рад."

        chestonov "Жених мне по сердцу."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Не правда ли, что клад?"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Живет расчетисто, богат и здешний житель."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Преумный человек! Актер и сочинитель."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Я этого не знал."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да это ничего:"

        lyubskij "Здесь в обществах и жить не могут без него,"

        lyubskij "На всё готов: завесть игру, затеять фанты..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Так Вельский от меня скрывал свои таланты?"

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Что, что?"

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}По чести! Я совсем не знал об них."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Как Вельский? - Что за вздор!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Кто ж Оленькин жених?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да разве жениха не может быть другого?"

        lyubskij "С чего ты взял?"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Она идет за Посошкова."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Возможно ли!"

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Жених, надеюсь, не худой!"

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Старик!.."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Какой старик! Он малый молодой."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Ему за пятьдесят..."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Но все единогласно"

        lyubskij "Со мною повторят, что можно даже страстно"

        lyubskij "В него быть влюблену, - племянница сама..."

        lyubskij "Со временем его полюбит без ума."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Когда со временем, так, видно, это значит..."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Что, может быть, теперь немного и поплачет,"

        lyubskaya "Да слюбится вперед."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Эй! на душу греха"

        chestonov "Не должно брать."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}На что ей лучше жениха?"

        lyubskij "Известен всем, умен."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}И к этому придачи"

        lyubskaya "Шестьсот наличных душ, луга, лесные дачи..."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "И десять тысяч душ без собственной души"

        chestonov "Не значат ничего."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Эй, братец, не греши!"

        lyubskaya "Не значит ничего богатое именье!"

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Богатство при слезах - плохое утешенье,"

        chestonov "Оно должно быть здесь! - Поверь, кто сердцем чист..."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Ты судишь, батюшка, как сущий атеист:"

        lyubskaya "Ведь деньги божий дар."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}А чаще - наказанье."

        chestonov "Но дело не о том. При первом я свиданьи"

        chestonov "Намерен Волгина порядком побранить:"

        chestonov "Он дядя Вельскому, и, кажется, шутить"

        chestonov "Насчет племянника ему бы неприлично..."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Как! Волгин здесь?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да, здесь! и говорит публично"

        chestonov "О свадьбе Вельского."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}С чего ж он это взял?"

        lyubskij "Хоть Вельский сватался..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Но ты ведь отказал?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Не то чтоб отказал... однако не дал слова."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Но если Оленька идет за Посошкова,"

        chestonov "Так должно отказать."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Я это знаю сам."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Зачем же ты молчишь?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ответ я завтра дам,"

        lyubskij "Всё кончу поутру."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}А что ж тебе мешает"

        chestonov "Сказать теперь?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(вполголоса){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Нельзя! Сегодня он играет."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Сегодня? У тебя?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Вот то-то и беда!"

        lyubskij "Пришлось молчать. Зато уж после никогда"

        lyubskij "Я Вельскому к себе и ездить не позволю."

        lyubskij "Лишь нынче б как-нибудь сыграл свою он ролю,"

        lyubskij "А завтра кончено! Решительный отказ!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Я, право, от тебя не ждал таких проказ:"

        chestonov "Во всех делах твоих и тени нет рассудка."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "И, полно! Шутишь, брат."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Какая это шутка!"

        chestonov "Ну, пусть племянница идет за старика,"

        chestonov "За что ж из Вельского вам делать дурака?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Но мой театр..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Скажи! походит ли на дело?"

        chestonov "По милости твоей теперь он может смело"

        chestonov "С утра до вечера с ней роли проходить,"

        chestonov "Шептать ей на ухо, о страсти говорить, -"

        chestonov "И это всё сносить ты должен терпеливо."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Конечно, так, мой друг! Ты судишь справедливо,"

        lyubskij "Да как же мой театр?.."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Эй, братец, не шути!"

        chestonov "Ну, если Оленька задумает уйти?.."

        chestonov "Хотя племянница во всем тебе послушна,"

        chestonov "Но если к Вельскому она неравнодушна..."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Недолго до греха!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ты точно, милый, прав!"

        lyubskij "И если б не театр..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Какой несносный нрав!"

        chestonov "Кой черт! Да что тебя к театру привязало?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Меня?.. По мне, его хоть век бы не бывало,"

        lyubskij "Но делать нечего - и плачу, да люблю:"

        lyubskij "Ведь я, мой друг, один весь город веселю,"

        lyubskij "Так хочешь или нет, а рассылай билеты."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Да, батюшка! Что день, то новые банкеты..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Молчи, жена!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Ну, вот! Всегда один ответ."

        lyubskaya "Помилуй, мой отец! Расходам счету нет."

        lyubskaya "Уж этот нас театр доедет непременно."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Пустое! Вздор! - Хотя, признаться откровенно,"

        lyubskij "Он несколько и мне становится тяжел."

        lyubskij "Что грех таить! С тех пор как я его завел,"

        lyubskij "Покою нет; когда ж дойдет до представленья,"

        lyubskij "Вот тут-то, брат, вертись: костюмы, освещенье..."

        lyubskij "Ну, словом, голова у всех пойдет кругом."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Весь дом в последний раз поставили вверх дном;"

        lyubskaya "А сколько извели холстины на кулисы!.."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Спасибо, что теперь домашние актрисы,"

        lyubskij "А то - хоть из дому беги! С ума сойдешь."

        lyubskij "Бывало, никого на пробу не сберешь:"

        lyubskij "То некогда прийти, то роля не готова,"

        lyubskij "То на вечер звана, другая нездорова..."

        lyubskij "Поверишь ли? Тоска! - Подчас хоть в петлю рад."

        lyubskij "Сегодня, например, хоть всё идет на лад,"

        lyubskij "А несмотря на то дрожу, боюсь..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Чего же?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну, если мой театр, чего избави боже!"

        lyubskij "Навыворот пойдет? Что делать мне тогда?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "А что! И подлинно, большая ведь беда!"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Шути себе, шути! А я меж тем уверен,"

        lyubskij "Что если бы и ты..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Я спорить не намерен,"

        chestonov "А просто мнение мое тебе скажу:"

        chestonov "Что ты завел театр, нимало не тужу,"

        chestonov "Я сам любил играть, но только не для славы."

        chestonov "Бывало - в два часа, для собственной забавы,"

        chestonov "Готов я вытвердить хоть дюжину страниц,"

        chestonov "Но если эта страсть выходит из границ,"

        chestonov "То верь, мой друг, придет с веселостью проститься"

        chestonov "И скуки ждать одной. Тот худо веселится,"

        chestonov "Кто, смыслу здравому идя наперелом,"

        chestonov "Забаву делает каким-то ремеслом."

        chestonov "Вот сам ты, например, скажи мне, ради бога..."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да ты не знаешь, брат, судить-та будут строго."

        lyubskij "Здесь много знатоков, недолго до беды:"

        lyubskij "Распишут так..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}И вот тщеславия плоды!"

        chestonov "Чтоб только твой театр хорошим называли,"

        chestonov "Готов ты уморить племянницу с печали,"

        chestonov "Замучить сам себя, именье разорить..."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Ну, слышишь, батюшка?"

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да что тут говорить!"

        chestonov "Бывало, в старину мы резвимся для смеха,"

        chestonov "А нынче заведи театр - пошла потеха!"

        chestonov "Волненье страшное, тревога, кутерьма!"

        chestonov "Хозяева в чаду, актеры без ума;"

        chestonov "Тот пламенной игрой и чувством удивляет:"

        chestonov "Забытого детьми Эдипа представляет,"

        chestonov "А сам детей своих давно уже забыл."

        chestonov "На сцене, для другой, один супруг лишь мил,"

        chestonov "Им дышит, им живет - тогда как в самом деле"

        chestonov "Действительный супруг лежит больной в постеле."

        chestonov "Интригам нет конца, насмешки, сплетни, лесть..."

        chestonov "А ссоры вздорные нельзя и перечесть:"

        chestonov "Один желает быть отцом, другой тираном,"

        chestonov "Тот ролю выплакал, тот взял ее обманом,"

        chestonov "Та теткой хочет быть, тот просится в слуги,"

        chestonov "Тому любовника давай - ну, вон беги!"

        chestonov "И, словом, труппа вся, признаться должно в этом,"

        chestonov "Прекрасным может быть комическим сюжетом."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Всё это пустяки, мой друг, одни слова!"

        lyubskij "Хоть в этом мне поверь, я труппе всей глава;"

        lyubskij "Так дело ведь мое, чтоб жили мы согласно."

        hide lyubskij

        show mestonov at truecenter

        $ mestonov_var = "{noalt}Местонов"

        mestonov "Не верю, милый мой."

        hide mestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Зачем судить пристрастно?"

        lyubskij "Ты прежде посмотри, а после уж брани."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "И вы не ссоритесь?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}О! Боже сохрани!"

        lyubskij "И знать не знаем мы, что есть на свете ссоры."

        hide lyubskij

    label Act_0_Scene_11:
        "{b}ЯВЛЕНИЕ 11{/b}"

        show natasha at truecenter

        show natasha at truecenter

        "<{i}Те же и Наташа.{/i}>"

        hide natasha

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show natasha at right

        hide lyubskij

        show lyubskij at left
        show natasha at right

        lyubskij "<{i}(Наташе){/i}>"

        hide natasha

        show lyubskij at truecenter

        hide natasha

        show lyubskij at truecenter

        lyubskij "Зачем?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Беда, сударь! Поссорились актеры."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Охти! За что?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}А вот, спросите сами их."

        hide natasha

    label Act_0_Scene_12:
        "{b}ЯВЛЕНИЕ 12{/b}"

        show velskij at left
        show izvedov at truecenter
        show olenka at right

        show velskij at left
        show izvedov at truecenter
        show olenka at right

        "<{i}Те же, Посошков, Лилеев, Бирюлькин, Вельский, Изведов и Оленька.{/i}>"

        hide pososhkov
        hide lileev
        hide biryulkin
        hide velskij
        hide izvedov
        hide olenka

        hide pososhkov
        hide lileev
        hide biryulkin
        hide velskij
        hide izvedov
        hide olenka

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "Я вам, сударь, сказал, что грубостей таких"

        lileev "Сносить я не хочу."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Играть изволит франта!"

        pososhkov "Тогда как надобно..."

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Так нет во мне таланта?"

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Я это говорил, еще вам говорю"

        pososhkov "И буду говорить."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show chestonov at right

        hide lyubskij

        show lyubskij at left
        show chestonov at right

        lyubskij "<{i}(Честонову){/i}>"

        hide chestonov

        show lyubskij at truecenter

        hide chestonov

        show lyubskij at truecenter

        lyubskij "{space=400}Сейчас их помирю."

        lyubskij "Стыдитесь, господа! На что это похоже!"

        lyubskij "За что вы ссоритесь?"

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Мне честь всего дороже,"

        lileev "И я не дам себя обидеть никому!"

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да что, скажите мне!"

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Прилично ли тому,"

        lileev "Кто сам плохой актер..."

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И, как тебе не стыдно!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Торжественно скажу, он хочет, очевидно,"

        pososhkov "Испортить всё."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да что? Добьюсь ли толку я?"

        lyubskij "О чем вы спорите?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Так будьте ж вы судья!"

        pososhkov "Он ролю старика взялся без принужденья,"

        pososhkov "Охотой, сам, играть..."

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Ну, да! Из снисхожденья."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "И что ж играет он? Терпенья, право, нет!"

        pososhkov "Наместо старика - мальчишку в двадцать лет."

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "За что ж винить меня? Вините в том натуру,"

        lileev "Которая дала такую мне фигуру."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Так знайте ж, господин столетний Селадон..."

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "Столетний!.."

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Ну, беда!"

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Что значит этот тон?"

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Послушайте!"

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Кому вы это говорите?"

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "О, верно уж не вам! Вот зеркало, взгляните!"

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "Насмешки, дерзости... но я вам отплачу,"

        lileev "Извольте ролю взять, играть я не хочу."

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Как! Что! Помилуй, брат! Сегодня представленье,"

        lyubskij "А ты..."

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Чтоб я сносил такие оскорбленья!.."

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Позволь..."

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Я вам сказал, что честь мне дорога."

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да выслушай!.."

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Нет, нет! Покорный ваш слуга!"

        hide lileev

        show lileev at truecenter

        hide lileev

        show lileev at truecenter

        lileev "<{i}(Уходит.){/i}>"

        show lileev at truecenter

        show lileev at truecenter

        hide lileev

    label Act_0_Scene_13:
        "{b}ЯВЛЕНИЕ 13{/b}"

        show lileev at truecenter

        show lileev at truecenter

        "<{i}Те же, без Лилеева.{/i}>"

        hide lileev

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        play sound1 running

        hide lyubskij

        show lyubskij at left
        show lileev at right

        play sound1 running

        hide lyubskij

        show lyubskij at left
        show lileev at right

        lyubskij "<{i}(бежит за Лилеевым){/i}>"

        hide lileev

        show lyubskij at truecenter

        stop sound1

        hide lileev

        show lyubskij at truecenter

        stop sound1

        lyubskij "В уме ли ты! Постой!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}О, глупое созданье!"

        pososhkov "Поверьте мне, в нем нет и капли дарованья."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(возвращаясь с отчаянием){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Ушел! Совсем ушел!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Тем лучше, очень рад!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Зарезал без ножа!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Я бьюся об заклад,"

        pososhkov "Что он и смолоду прескверным был актером,"

        pososhkov "Ему под шестьдесят - а хочет быть Линдором."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Что делать мне теперь? Весь город приглашен,"

        lyubskij "А наш театр..."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Никак попасть не может в тон."

        pososhkov "Где должно говорить с душой - одни лишь крики."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Эх, братец!.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Никогда не ждет своей реплики."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Несносный человек!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Что скажет, то соврет."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да, слышишь ли, злодей! Театр наш не пойдет!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "И, что вы! Для него? Да это уж безбожно!"

        pososhkov "Неужто заменить Лилеева не можно?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Посмотрим! Говори! Кого ты назовешь?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Хоть это не легко..."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Не вдруг теперь найдешь"

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну, что молчишь? Скорей зарежь одним уж разом!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Послать бы, батюшка, скорей ко всем с отказом."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "С отказом! Боже мой! Вот дожил до чего!"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Позвольте... точно так! Я знаю одного"

        velskij "Охотника играть, старинный мой приятель,"

        velskij "И дальний родственник... Уездный заседатель..."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да, кто такой?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Андрей Степаныч Прямиков."

        velskij "Он был всегда в числе хороших знатоков,"

        velskij "И мастер сам играть."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ах, сделай одолженье!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Возьмется ль выучить?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Без всякого сомненья."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "И! Роля ничего! Решился б только взять..."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Она ж невелика, всего страничек пять."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ступай же поскорей!"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Я не прощаюсь с вами."

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at left
        show velskij at right

        hide chestonov

        show chestonov at left
        show velskij at right

        chestonov "<{i}(Вельскому){/i}>"

        hide velskij

        show chestonov at truecenter

        hide velskij

        show chestonov at truecenter

        chestonov "И я с тобой."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}А ты куда? Обедай с нами."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Нельзя, мне надобно кой-что распорядить."

        hide chestonov

        show chestonov at left
        show velskij at right

        hide chestonov

        show chestonov at left
        show velskij at right

        chestonov "<{i}(Тихо Вельскому){/i}>"

        hide velskij

        show chestonov at truecenter

        hide velskij

        show chestonov at truecenter

        chestonov "С тобою должен я о многом говорить."

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(Уходят.){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        hide chestonov

    label Act_0_Scene_14:
        "{b}ЯВЛЕНИЕ 14{/b}"

        show velskij at left
        show chestonov at right

        show velskij at left
        show chestonov at right

        "<{i}Те же, без Вельского и Честонова.{/i}>"

        hide velskij
        hide chestonov

        hide velskij
        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ох, этот мне театр! Прекрасная забава!"

        lyubskij "Ложись да умирай!"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Зато какая слава!"

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Кто этот Прямиков? Я здесь живу давно,"

        pososhkov "А что-то не слыхал."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Эх, братец, всё равно!"

        lyubskij "Ну, что тут спрашивать? Актера нет другого,"

        lyubskij "Пойдемте, господа! Чай, кушанье готово."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Придется попоздней сегодня нам начать."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        lyubskij "<{i}(уходя, Посошкову){/i}>"

        hide pososhkov

        show lyubskij at truecenter

        hide pososhkov

        show lyubskij at truecenter

        lyubskij "Добро, мой друг! За всё ты будешь отвечать."

        hide lyubskij

        "<{i}Все уходят в боковые двери.{/i}>"

label Act_4:
    play music "audio/music/44.mp3" fadeout 1.0 fadein 1.0

    scene 67 with fade

    "{b}ДЕЙСТВИЕ ВТОРОЕ{/b}"

    "<{i}Та же комната.{/i}>"

    menu:
        "{color=#000}ЯВЛЕНИЕ 1{/color}":
            jump Act_1_Scene_1
        "{color=#000}ЯВЛЕНИЕ 2{/color}":
            jump Act_1_Scene_2
        "{color=#000}ЯВЛЕНИЕ 3{/color}":
            jump Act_1_Scene_3
        "{color=#000}ЯВЛЕНИЕ 4{/color}":
            jump Act_1_Scene_4
        "{color=#000}ЯВЛЕНИЕ 5{/color}":
            jump Act_1_Scene_5
        "{color=#000}ЯВЛЕНИЕ 6{/color}":
            jump Act_1_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_1_Scene_6_1

label Further_Act_1_Scene_6_1:
    menu:
        "{color=#000}ЯВЛЕНИЕ 7{/color}":
            jump Act_1_Scene_7
        "{color=#000}ЯВЛЕНИЕ 8{/color}":
            jump Act_1_Scene_8
        "{color=#000}ЯВЛЕНИЕ 9{/color}":
            jump Act_1_Scene_9
        "{color=#000}ЯВЛЕНИЕ 10{/color}":
            jump Act_1_Scene_10

    label Act_1_Scene_1:
        "{b}ЯВЛЕНИЕ 1{/b}"

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(один){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Мы нынче, кажется, обедали по моде."

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(Смотрит на часы.){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Ну, так и есть! Легко ль! Четвертый час в исходе,"

        izvedov "А Вельского всё нет как нет! Эй, быть беде!"

        izvedov "Такого удальца не сыщет он нигде,"

        izvedov "Кто б ролю выучил сурьезно, не для шутки,"

        izvedov "Не только в несколько часов, но даже в сутки."

        izvedov "Уж я ли в старину не делал чудеса?"

        izvedov "Бывало, выучить придется в два часа"

        izvedov "Осьмушек до шести, а всё, играть как станут,"

        izvedov "Такую дичь начнешь пороть, что уши вянут."

        izvedov "Нет! Видно по всему, театру не бывать."

        izvedov "А право, жаль! - Старик наш будет горевать."

        izvedov "Что, если б мне?.. А что ж? Чем хуже я другого? -"

        izvedov "Лилеев дворянин - об этом я ни слова,"

        izvedov "Зато какой актер, последней уж руки,"

        izvedov "А я, сомненья нет, сыграю мастерски,"

        izvedov "И мой талант..."

        hide izvedov

    label Act_1_Scene_2:
        "{b}ЯВЛЕНИЕ 2{/b}"

        show pososhkov at left
        show olenka at truecenter
        show natasha at right

        show pososhkov at left
        show olenka at truecenter
        show natasha at right

        "<{i}Тот же, Посошков, Оленька и Наташа.{/i}>"

        hide pososhkov
        hide olenka
        hide natasha

        hide pososhkov
        hide olenka
        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Да, да! Вам с Вельским должно вместе"

        pososhkov "Всю сцену повторить. Ну, что? Какие вести?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Покуда никаких."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Так Вельский не бывал?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "И слуху нет о нем."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Куда же он пропал?"

        pososhkov "Не стыдно ли ему! Он дал честное слово"

        pososhkov "Как можно поскорей привесть к нам Прямикова..."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Да вряд ли приведет."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}И, что ты, братец! Вздор!"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(глядя в окно){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Постойте! Вот и он въезжает к нам на двор."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Один?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=200}Один, сударь."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Неужто в самом деле?"

        play sound1 running

        hide pososhkov

        show pososhkov at truecenter

        play sound1 running

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Бежит к нему навстречу){/i}>"

        show pososhkov at truecenter

        stop sound1

        show pososhkov at truecenter

        stop sound1

        pososhkov "Ну, что? - Ах, боже мой! Войдите хоть в шинели,"

        pososhkov "Да только поскорей."

        hide pososhkov

    label Act_1_Scene_3:
        "{b}ЯВЛЕНИЕ 3{/b}"

        show velskij at truecenter

        show velskij at truecenter

        "<{i}Те же и Вельский.{/i}>"

        hide velskij

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Скажите, отчего"

        pososhkov "Не с вами Прямиков?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Нет в городе его."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Нет в городе!.. Так мы остались без актера?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(кланяясь){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Когда позволите, так я..."

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(прерывая){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}Он очень скоро"

        velskij "Воротится домой, наверно в пять часов."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(с досадою){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Да в роли у него не десять только слов:"

        izvedov "Когда ж успеть ему..."

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Я вам ручаюсь смело,"

        velskij "Что он..."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=200}Сыграет как-нибудь."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да что за дело?"

        pososhkov "Лишь только бы сыграл, но точно ль будет он?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Сомненья в этом нет."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Попасть как должно в тон,"

        izvedov "Реплики выучить - всё это не безделки."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "И, вздор!"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(в сторону){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=400}Ох, эти мне актеры-скороспелки!"

        izvedov "Везде от них беда."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "{space=400}Так ровно через час"

        pososhkov "Он будет здесь?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(тихо Оленьке){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}Теперь, сударыня, от вас"

        velskij "Зависит всё."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "{space=400}И вы уверены, что может"

        pososhkov "Он к вечеру поспеть?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Старанье всё приложит,"

        velskij "Ручаюсь за него."

        hide velskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(стараясь отвлечь Посошкова){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        natasha "{space=400}Позвольте вас спросить:"

        natasha "Здесь в роли у меня должны ошибки быть, -"

        natasha "Вот тут?"

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Посмотрим. Где?"

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(показывая рукою){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        natasha "{space=200}Внизу."

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(тихо Оленьке){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}Мне очень нужно"

        velskij "Сказать вам слова два."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(читает ролю){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}\"С ним жить я стану дружно\"."

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "А, дружно? Точно так."

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(тихо Оленьке){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}Мне с вами говорить"

        velskij "Теперь нельзя, но я..."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "{space=400}А что б нам повторить..."

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(показывая свою ролю){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        natasha "Позвольте! Вот еще тут что-то непонятно."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(читает ролю){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "\"Как этих стариков обманывать приятно!"

        pososhkov "Ну им ли женщин быть умнее и хитрей\"."

        pososhkov "Помилуй, матушка! Что ж этого ясней?"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "Андрей Степанович! За чем же дело стало?"

        pososhkov "Пройдемте сценки две."

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Не лучше ли сначала"

        natasha "Заняться вам со мной?"

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}На что же нам одним?"

        pososhkov "Мы сцены две иль три все вместе повторим."

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "Не правда ли?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=200}От всей души."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=200}А вы?"

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "{space=400}Извольте."

        hide olenka

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "С чего бы нам начать?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=200}Мне кажется..."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Постойте!"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Смотрит в тетрадь){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Явленье пятое... да! Точно с этих пор"

        pososhkov "Мы можем повторить. А где же наш суфлер?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Я здесь, сударь."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Вот стул, прошу садиться."

        pososhkov "Возьми комедию... Да, чур, не торопиться."

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "Вы в этом действии отменно хороши,"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "А в вас бы я желал поболее души."

        pososhkov "Натура и душа! - без этих двух условий"

        pososhkov "Искусство - ничего."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(в сторону){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=400}Нельзя без предисловий."

        izvedov "Прикажете начать?"

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да, душенька, начни."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Явленье пятое. Сначала вы одни,"

        izvedov "Потом Эраст."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Живей как можно эту сцену!"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at left
        show natasha at right

        hide izvedov

        show izvedov at left
        show natasha at right

        izvedov "<{i}(Наташе){/i}>"

        hide natasha

        show izvedov at truecenter

        hide natasha

        show izvedov at truecenter

        izvedov "Извольте. Вам."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(Оленьке){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        natasha "{space=400}\"Я в вас большую перемену"

        natasha "Сегодня нахожу."

        natasha "Быть может, вас я этим рассержу,"

        natasha "Но, право, мне смешно: вы плакали в постеле,"

        natasha "Теперь вздыхаете... неужто в самом деле"

        natasha "{space=200}Боитесь вы?..\""

        hide natasha

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "{space=400}\"Всего!"

        olenka "Ах, Машенька! Я так люблю его!"

        olenka "И вот уж пятый день...\""

        hide olenka

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"К окну он не подходит."

        natasha "Так это-то с ума вас сводит?"

        natasha "Да он уж не живет напротив нас\"."

        hide natasha

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Возможно ли? Эраст...\""

        hide olenka

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Из нашего соседства"

        natasha "Давно уж выехал и, верно, ищет средства"

        natasha "Увидеть ближе вас."

        natasha "Ваш опекун хитер, а он еще хитрее"

        natasha "И, может быть...\""

        hide natasha

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "{space=400}\"А мне так кажется вернее,"

        olenka "Что он уехал из Москвы\"."

        hide olenka

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Да вот он налицо\"."

        hide natasha

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Возможно ль! Это вы?\""

        hide olenka

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Не то, совсем не то! Простое удивленье"

        pososhkov "Не значит ничего. Где ж радость, восхищенье?"

        pososhkov "Нет, нет, сударыня! Вы слишком холодны..."

        pososhkov "Не правда ль, что в него вы страстно влюблены?"

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Конечно, так."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Что с ним и видеться хотели?"

        pososhkov "Что он любовник ваш... Ну, вот и покраснели!"

        pososhkov "Ох, эта скромность мне! Пора вам быть смелей."

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Я то же говорю."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Скажите веселей:"

        pososhkov "\"Возможно ль! Это вы!\" Ну, что же! Говорите!"

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Возможно ль! Это вы...\""

        hide olenka

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Куда же вы глядите?"

        pososhkov "Смотрите на него: он главный персонаж."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Да, Лиза, это я - любовник верный ваш!"

        velskij "Я с вами, вижу вас... и всё теперь, разлуку,"

        velskij "Печаль, тоску... всё, всё забыл!\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "{space=400}Целуйте руку!"

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Вы здесь, Эраст! И вы пять дней могли"

        olenka "Не видеться со мной!\""

        hide olenka

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Да будьте ж с ним построже:"

        natasha "Легко ль, пять дней! - На дело не похоже!"

        natasha "Мы чуть было от вас в постелю не слегли,"

        natasha "С утра до вечера всё плакали, грустили...\""

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Я ездил из Москвы\"."

        hide velskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Вы ездили? Куда?\""

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Оленьке){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "\"Но вы везде со мною вместе были!"

        velskij "Вы здесь и навсегда!\""

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        hide olenka

        show olenka at left
        show natasha at right

        hide olenka

        show olenka at left
        show natasha at right

        olenka "<{i}(Наташе){/i}>"

        hide natasha

        show olenka at truecenter

        hide natasha

        show olenka at truecenter

        olenka "\"Ах, как он мил!\""

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Я с вами расставался"

        velskij "Затем, чтоб вечно вашим быть:"

        velskij "Я ездил к дядюшке, во всем ему признался,"

        velskij "Клялся ему вас век любить."

        velskij "Кто чувствует, как я, тому красноречивым"

        velskij "Нетрудно быть: я все сомненья превозмог,"

        velskij "Он мне позволил быть счастливым."

        velskij "Теперь я здесь, у ваших ног!"

        velskij "От вашего зависит приговора"

        velskij "Всё счастье, жизнь моя...\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ах, если бы актера"

        pososhkov "Еще такого нам!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Скажите только: да!"

        velskij "И я навеки, навсегда"

        velskij "Любовник ваш, супруг...\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Прекрасно, превосходно!"

        pososhkov "Вот истинный талант!"

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "{space=400}\"Притворство мне не сродно..."

        olenka "Я вас люблю...\""

        hide olenka

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Нежней, сударыня, нежней!"

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Я вас люблю, Эраст!..\""

        hide olenka

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "{space=400}Подвиньтесь ближе к ней."

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Но я, к несчастию, свободы не имею"

        olenka "Располагать собой\"."

        hide olenka

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Я вас не разумею\"."

        hide natasha

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Мой опекун...\""

        hide olenka

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Да что он за указ?"

        natasha "И есть ли что-нибудь с ним общего у вас?"

        natasha "Он стар - вы молоды; он дурен - вы прекрасны\"."

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Что значит власть опекуна,"

        velskij "Когда вы будете согласны"

        velskij "Супругой быть моей?\""

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "{space=400}\"Так я должна...\""

        hide olenka

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "\"Должны, как следует, сначала колебаться,"

        natasha "Твердить о том о сем,"

        natasha "Поплакать, и потом -"

        natasha "Сегодня убежать, а завтра обвенчаться\"."

        hide natasha

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Что ждет меня? Насмешки, клеветы..."

        olenka "Ах! Участь сироты"

        olenka "Достойна сожаленья!\""

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Решитесь быть моей, и мы сегодня в ночь"

        velskij "Уедем к дядюшке, он примет вас, как дочь...\""

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Но как решиться мне? Какое положенье!"

        olenka "Предметом сделаться злословья, клеветы..."

        olenka "Нет, нет, Эраст!\""

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"О, если всё напрасно,"

        velskij "И просьбы, и любовь...\""

        hide velskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Чего ж хотите вы?"

        natasha "Не вдруг же ей сказать: - Извольте! Я согласна!\""

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Как долго я обманывал себя!"

        velskij "Вас пламенно любя,"

        velskij "Я смел мечтать, что те же чувства"

        velskij "Понятны и для вас,"

        velskij "Что с сердцем искренним, без всякого искусства,"

        velskij "Сказав: люблю! мне в первый раз,"

        velskij "Навек вы сделались моею...\""

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Вы сердитесь?..\""

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"О нет! Я холоден как лед,"

        velskij "Упреки делать вам я права не имею, -"

        velskij "Его любовь дает."

        velskij "А вы...\""

        hide velskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Помилуйте! Ну то ли"

        natasha "Вам должно говорить?\""

        hide natasha

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Но я не век остануся в неволе:"

        olenka "Быть может, через год...\""

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Без вас год целый жить!"

        velskij "Без вас! - Ах, боже мой! Кто может быть порукой,"

        velskij "Что я, измученный тоской и скукой,"

        velskij "Еще год целый проживу?\""

        hide velskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "\"И больше проживете\"."

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Нет! Лучше навсегда оставлю я Москву,"

        velskij "Тогда вы, верно, предпочтете"

        velskij "Моей любви ваш собственный покой."

        velskij "Тогда соперник мой...\""

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "{space=400}\"Соперник ваш?.. Какой?\""

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Ваш милый опекун...\""

        hide velskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Ну, есть кого бояться!\""

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Быть может, наконец ему повиноваться"

        velskij "Решитесь вы, и целый свет"

        velskij "Вас будет прославлять. Он сам... Нет, Лиза, нет!"

        velskij "Ему ль понять блаженство"

        velskij "Супругом вашим быть!..\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Какое совершенство!"

        pososhkov "Ну, Вельский, признаюсь, от вас я без ума!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Недурно я сыграл?"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Как Гаррик, как Тальма,"

        pososhkov "Почти как я!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}О нет! Уж это слишком много."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Поверьте мне, я вас сужу отменно строго,"

        pososhkov "Да иначе судить вас было бы грешно:"

        pososhkov "Ведь вы талант! Вам всё натурою дано:"

        pososhkov "Наружность славная, орган отлично гибок,"

        pososhkov "Конечно, есть кой-что - нельзя же без ошибок,"

        pososhkov "Подчас играете вы слишком горячо,"

        pososhkov "Руками машете, да левое плечо"

        pososhkov "Немножечко шалит."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Нет, это уж нападки:"

        izvedov "Позвольте вам сказать, все эти недостатки"

        izvedov "Так мелочны, что их смешно и замечать."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да Вельскому нельзя и мелочи прощать -"

        pososhkov "Он истинный артист."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Всё так, но рассудите..."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Нам спорить некогда. Извольте! Повторите"

        pososhkov "Последние слова."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Последние?.. Да, да!"

        velskij "\"Супругом вашим быть\"."

        hide velskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Ну, барышня, беда!"

        natasha "Нам нет спасенья никакого\"."

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(суфлируя){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "\"За сценой голос Сундукова\"."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(начиная играть свою ролю){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "\"Эй, люди! Дурачье! Да слышите ль? Кто там?\""

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Ах, боже мой! Куда деваться нам?\""

        hide olenka

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "\"Я вас, разбойники!\""

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=200}\"Пропали мы!\""

        hide natasha

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Пустое!"

        velskij "Не бойтесь ничего!\""

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(суфлируя){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=400}\"Явление шестое."

        izvedov "Лишь только я с двора...\""

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Эх, братец! Не спеши!"

        pososhkov "\"Лишь только я с двора, так в доме ни души..."

        pososhkov "Кой черт! Да здесь проезжая дорога\"."

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "\"Ах! ради бога,"

        olenka "Уйдите поскорей!\""

        hide olenka

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "\"Ворота на запор! Ключи от всех дверей"

        pososhkov "Принесть ко мне. Уж я тебя, скотина!"

        pososhkov "Шататься всё, а нет, чтоб двор подместь..."

        pososhkov "Пошел, болван!.. Эге! Да здесь и гости есть!"

        pososhkov "Возможно ли - мужчина!"

        pososhkov "Вы кто, сударь? Зачем и почему?"

        pososhkov "Кого вам надобно?\""

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Извините!"

        velskij "Я только что взошел\"."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Взошли... К кому?.."

        pososhkov "Что вижу, к вам?.. Вот я вас! Погодите!"

        pososhkov "Взошли!.. Зачем, сударь? Да разве здесь корчма?"

        pososhkov "Взошли, когда хозяина нет дома...\""

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Вы всё узнаете из этого письма\"."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "\"Рука, мне кажется, знакома\"."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"От дяди моего\"."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Да это всё равно."

        pososhkov "Письмо - письмом, а вам бы не мешало"

        pososhkov "Без спроса не входить\"."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Вы дружны с ним давно."

        velskij "Степан Кондратьевич Окнов\"."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Окнов? Так стало,"

        pososhkov "Он жив еще?"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Читает){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "\"Любезный друг! Податель сего племянник мой Сурский...\""

        pososhkov "{space=400}Вы Сурский? Очень рад!"

        pososhkov "Покойный ваш отец со мной знаком был лично, -"

        pososhkov "А всё скажу, что вовсе неприлично"

        pososhkov "Вломиться силой в дом\"."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Что ж делать - виноват!\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(читает){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "\"Он любит одну весьма достойную девицу, но, к несчастию, у него есть соперник. Я стараюсь уладить это дело, а между тем, боясь, чтоб он не наделал дурачеств, отправил его в Москву, не оставляйте его вашими советами. Надеясь на дружбу вашу, я уверен, и проч."

        pososhkov "и проч.\""

        pososhkov "\"Так вы намерены жениться?"

        pososhkov "Вот это хорошо! Я с вами подружиться"

        pososhkov "Душою рад... Да только вот беда!"

        pososhkov "Вы ездить будете напрасно -"

        pososhkov "Меня нет дома никогда."

        pososhkov "Итак, вы любите? И очень страстно?..\""

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at left
        show olenka at right

        hide velskij

        show velskij at left
        show olenka at right

        velskij "<{i}(глядя на Оленьку){/i}>"

        hide olenka

        show velskij at truecenter

        hide olenka

        show velskij at truecenter

        velskij "\"И сердце и душа -"

        velskij "Всё ей принадлежит\"."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Уж, верно, хороша?"

        pososhkov "И спрашивать не надо\"."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"Все в мире женщины ее не стоят взгляда\"."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "\"Похвально! Хорошо! Прошу ко мне вперед!"

        pososhkov "А что, соперник ваш и молод и прекрасен?\""

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "\"О нет! Он вовсе не опасен:"

        velskij "Седой старик, скупец, животное, урод...\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(своим голосом){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Эх, батюшка, не то! Вам должно обозначить"

        pososhkov "Насмешку тут: ведь вы должны меня дурачить."

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Да он, мне кажется, и так дурачит вас."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Побольше тонкостей! Играя в первый раз,"

        pososhkov "Их все нельзя схватить, а вы, сударь, не внове:"

        pososhkov "Вам стыдно их не знать. - \"Урод!\" - При этом слове"

        pososhkov "Взгляните на меня."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(повторяя){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}\"Седой старик! скупец!..\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Вот, так!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=200}\"Урод!\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Брависсимо!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}\"Глупец!\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Отлично! Хорошо!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=200}\"А сверх того...\""

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(начинает опять играть){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}\"Увольте!.."

        hide pososhkov

        show pososhkov at left
        show natasha at truecenter
        show olenka at right

        hide pososhkov

        show pososhkov at left
        show natasha at truecenter
        show olenka at right

        pososhkov "<{i}(Наташе и Оленьке){/i}>"

        hide natasha
        hide olenka

        show pososhkov at truecenter

        hide natasha
        hide olenka

        show pososhkov at truecenter

        pososhkov "Я брани не люблю. Ступайте вон!\""

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Позвольте"

        natasha "Сказать вам слова два\"."

        hide natasha

        show natasha at left
        show velskij at truecenter
        show olenka at right

        hide natasha

        show natasha at left
        show velskij at truecenter
        show olenka at right

        natasha "<{i}(Отводит Посошкова к стороне, а между тем Вельский и Оленька говорят тихо.){/i}>"

        hide velskij
        hide olenka

        show natasha at truecenter

        hide velskij
        hide olenka

        show natasha at truecenter

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Ну, что же, говори!\""

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "\"Хотите ли держать пари,"

        natasha "Что этот господин приехал к вам недаром?\""

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "\"Неужели?\""

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}\"Тут что-нибудь да есть."

        natasha "Заметили ль, с каким он жаром"

        natasha "Описывал любовь свою, а между тем"

        natasha "Смотрел на барышню?\""

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Смотрел? Зачем?\""

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "\"Я этих сорванцов ужасно ненавижу."

        natasha "От них того и жди...\""

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(своим голосом){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Да, стань сюда! Я вижу."

        pososhkov "Закрой побольше их! Ах, нет! Еще вперед!"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}Вельский отдает записку Оленьке.{/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "Всё вижу, матушка: записку отдает,"

        pososhkov "Вот шепчет на ухо!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(тихо Оленьке){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}Прочтите поскорее!"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "Не так!"

        hide pososhkov

        show pososhkov at left
        show olenka at right

        hide pososhkov

        show pososhkov at left
        show olenka at right

        pososhkov "<{i}(Берет у Оленьки записку){/i}>"

        hide olenka

        show pososhkov at truecenter

        hide olenka

        show pososhkov at truecenter

        pososhkov "{space=400}Позвольте мне! Проворней и хитрее;"

        pososhkov "Смотрите на меня! Совсем не тот прием."

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Отдает записку Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Мы вот как, батюшка, записки отдаем."

        hide pososhkov

        show pososhkov at left
        show natasha at right

        hide pososhkov

        show pososhkov at left
        show natasha at right

        pososhkov "<{i}(Наташе, продолжая играть свою ролю){/i}>"

        hide natasha

        show pososhkov at truecenter

        hide natasha

        show pososhkov at truecenter

        pososhkov "\"Итак, мне должно опасаться?\""

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "\"Большой опасности тут нет\"."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Всё может статься."

        pososhkov "Эх, Машенька, недолго до греха...\""

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Позвольте! У меня последнего стиха"

        izvedov "В пиесе нет."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(берет тетрадь и смотрит){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Ну, так! Вперед я сам засяду"

        pososhkov "И буду списывать. Тут две ошибки сряду."

        pososhkov "Кто списывал ее?"

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Фома, буфетчик наш."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        pososhkov "<{i}(Изведову){/i}>"

        hide izvedov

        show pososhkov at truecenter

        hide izvedov

        show pososhkov at truecenter

        pososhkov "Ох, эти мне писцы! - Подай мне карандаш!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Угодно мой?"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Подает ему.){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        hide velskij

        show pososhkov at left
        show olenka at right

        show pososhkov at left
        show olenka at right

        "<{i}Посошков делает поправки, а между тем Оленька вполголоса читает письмо.{/i}>"

        hide pososhkov
        hide olenka

        hide pososhkov
        hide olenka

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        hide olenka

        show olenka at truecenter

        hide olenka

        show olenka at truecenter

        olenka "<{i}(читает){/i}>"

        show olenka at truecenter

        show olenka at truecenter

        olenka "\"Я боялся, что не найду свободной минуты переговорить с вами, и для того заготовил это письмо. Почтенный благодетель мой, ваш дядюшка Честонов, и слышать не хочет, чтоб вы были за Посошковым. Он дал слово помогать нам, и если вы согласитесь...\""

        hide olenka

        show olenka at truecenter

        hide olenka

        show olenka at truecenter

        olenka "<{i}(Прячет письмо.){/i}>"

        show olenka at truecenter

        show olenka at truecenter

        hide olenka

    label Act_1_Scene_4:
        "{b}ЯВЛЕНИЕ 4{/b}"

        show lyubskij at left
        show lyubskaya at truecenter
        show biryulkin at right

        show lyubskij at left
        show lyubskaya at truecenter
        show biryulkin at right

        "<{i}Те же, Любский, Любская и Бирюлькин.{/i}>"

        hide lyubskij
        hide lyubskaya
        hide biryulkin

        hide lyubskij
        hide lyubskaya
        hide biryulkin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну, вот они! А мы искали"

        lyubskij "Вас целый час в саду."

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Мы роли повторяли."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(перевертывая листы в тетради){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Постой, еще! Да тут премножество грехов!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ага! И Вельский здесь? Ну, что твой Прямиков?"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Уехал за город, однако же к обеду"

        velskij "Хотел он быть домой."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Так что же ты?"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Я еду"

        velskij "Опять к нему."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Боюсь, откажется злодей!"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "О, верно, нет!"

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да ты узнал бы от людей,"

        lyubskij "Куда уехал он."

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Теперь его застану,"

        velskij "Уж скоро пятый час."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}А если нет?"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Так стану"

        velskij "Искать его везде, и где-нибудь найду."

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Тихо Оленьке){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "Вы всё прочли?.."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Ступай, скорей!"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Сейчас, иду."

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Уходит.){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        hide velskij

    label Act_1_Scene_5:
        "{b}ЯВЛЕНИЕ 5{/b}"

        show velskij at truecenter

        show velskij at truecenter

        "<{i}Те же, без Вельского.{/i}>"

        hide velskij

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да этот Прямиков, как клад, нам не дается."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Эй, батюшка, поверь, нам вечером придется"

        lyubskaya "С отказом посылать ко всем..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Молчи, жена!"

        lyubskij "И без тебя тоска!"

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        lyubskij "<{i}(Посошкову){/i}>"

        hide pososhkov

        show lyubskij at truecenter

        hide pososhkov

        show lyubskij at truecenter

        lyubskij "{space=400}А всё твоя вина."

        lyubskij "Не знать наверное - да это хуже пытки!"

        lyubskij "Один бы уж конец."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Напрасные убытки,"

        lyubskaya "Расходы, хлопоты и больше ничего."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        lyubskij "<{i}(Посошкову, который смотрит в окно){/i}>"

        hide pososhkov

        show lyubskij at truecenter

        hide pososhkov

        show lyubskij at truecenter

        lyubskij "Ну, что?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Отправился."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Нельзя ли без него"

        lyubskij "Кой-что пройти? Ведь он не нужен вам?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Нимало,"

        pososhkov "Мы можем повторить весь первый акт сначала."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Так что же? Повтори."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        pososhkov "<{i}(берет тетрадь у Изведова){/i}>"

        hide izvedov

        show pososhkov at truecenter

        hide izvedov

        show pososhkov at truecenter

        pososhkov "{space=400}Извольте по местам."

        pososhkov "Явленье первое."

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Куда же вы?.. Не там,"

        pososhkov "Вы здесь должны сидеть."

        hide pososhkov

        show pososhkov at left
        show natasha at right

        hide pososhkov

        show pososhkov at left
        show natasha at right

        pososhkov "<{i}(Наташе){/i}>"

        hide natasha

        show pososhkov at truecenter

        hide natasha

        show pososhkov at truecenter

        pososhkov "{space=400}А вы сюда поближе."

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Держите голову немножечко пониже!"

        pososhkov "Да кто же в горести так весело глядит?"

        pososhkov "Задумайтесь! Вот так! Еще печальней вид,"

        pososhkov "Чтоб тотчас же была заметна горесть ваша."

        pososhkov "Явленье первое..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Постой, постой! Наташа,"

        lyubskij "Подвинься-ка вперед - еще левей! Вот так."

        hide lyubskij

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}Слуга"

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        pervyj_sluga "<{i}(входит и говорит громко){/i}>"

        show pervyj_sluga at truecenter

        show pervyj_sluga at truecenter

        pervyj_sluga "Матрена Савишна Кутермина."

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Дурак!"

        lyubskij "Скажи, что дома нет."

        hide lyubskij

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}Слуга"

        pervyj_sluga "{space=200}Докладывал."

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Так что же?"

        hide lyubskij

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}Слуга"

        pervyj_sluga "Изволит всё идти."

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну, вот! На что похоже!"

        lyubskij "Ступай, животное! Скажи, что я..."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Молчи!"

        lyubskaya "Она идет!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Что мы..."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Да полно, не кричи!"

        hide lyubskaya

    label Act_1_Scene_6:
        "{b}ЯВЛЕНИЕ 6{/b}"

        show kutermina at left
        show pervaja_plemyannica at truecenter
        show vtoraja_plemyannica at right

        show kutermina at left
        show pervaja_plemyannica at truecenter
        show vtoraja_plemyannica at right

        "<{i}Те же, Кутермина, 1-я племянница и 2-я племянница.{/i}>"

        hide kutermina
        hide pervaja_plemyannica
        hide vtoraja_plemyannica

        hide kutermina
        hide pervaja_plemyannica
        hide vtoraja_plemyannica

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        hide kutermina

        show kutermina at left
        show lyubskaya at right

        hide kutermina

        show kutermina at left
        show lyubskaya at right

        kutermina "<{i}(Любской){/i}>"

        hide lyubskaya

        show kutermina at truecenter

        hide lyubskaya

        show kutermina at truecenter

        kutermina "Здорово, матушка! А, здравствуй, Федор Львович!"

        kutermina "Каков ты, мой отец?"

        hide kutermina

        show kutermina at left
        show biryulkin at right

        hide kutermina

        show kutermina at left
        show biryulkin at right

        kutermina "<{i}(Бирюлькину){/i}>"

        hide biryulkin

        show kutermina at truecenter

        hide biryulkin

        show kutermina at truecenter

        kutermina "{space=400}Ты здесь, Максим Петрович?"

        kutermina "Не стыдно ли? Совсем изволил нас забыть."

        hide kutermina

        show kutermina at left
        show lyubskaya at right

        hide kutermina

        show kutermina at left
        show lyubskaya at right

        kutermina "<{i}(Любской, представляя племянниц){/i}>"

        hide lyubskaya

        show kutermina at truecenter

        hide lyubskaya

        show kutermina at truecenter

        kutermina "Племянницы мои! Прошу их полюбить."

        kutermina "Они сбирались к вам вчера, да поздно встали:"

        kutermina "На дежене дансан всю ночь протанцевали."

        kutermina "Прыгуньи страшные."

        hide kutermina

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=200}Давно ли здесь?"

        hide lyubskaya

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Дней пять."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Поверите ль, гляжу и не могу понять,"

        lyubskij "Как можно вырость так."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}А что, ведь не узнаешь."

        kutermina "Вот Софья, старшая. - Ну, что ж не приседаешь?"

        kutermina "Вся в матушку свою, привычками, лицом,"

        kutermina "Ну, словом, сходства нет с покойником отцом, -"

        kutermina "Предобрая! А вот меньшая, Катерина,"

        kutermina "Не правда ль, что в отца? - Красавец был мужчина,"

        kutermina "А дочка вся в него."

        hide kutermina

        show pervaja_plemyannica at truecenter

        $ pervaja_plemyannica_var = "{noalt}1-я племянница"

        pervaja_plemyannica "{space=400}И полноте, {a=myshow|tooltip|text=Тетушка! (франц.). - Ред.}ma tante!{/a}"

        hide pervaja_plemyannica

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Когда бы знали вы, какой у них талант!"

        kutermina "Да вот на этих днях заедем к вам пораньше,"

        kutermina "И вы услышите! Большие музыкантши:"

        kutermina "Везде от их пенья все были без ума,"

        kutermina "Об этом из Москвы писала мне кума,"

        kutermina "Глафира Савишна, а кумушка не лгунья."

        kutermina "Ты знаешь, чай, ее?"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(в сторону){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Проклятая болтунья!"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Громко){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Я звал вас на вечер и очень буду рад..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "А кстати! Что у вас сегодня? Маскерад?.."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Театр, сударыня."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Да, точно - виновата!"

        kutermina "Не знаю от кого, а помнится, от свата,"

        kutermina "Андрея Карпыча, я слышала... иль нет!"

        kutermina "От Ленской, кажется, что вы не то балет,"

        kutermina "Не то трагедию, а что-то дать хотите."

        kutermina "Да дело не о том: племянницы, просите,"

        kutermina "Чтоб мне позволили и вас с собой привесть."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(в сторону){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Ну, так! Я это знал!.."

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Громко){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Мы, верно бы, за честь"

        lyubskij "Почли себе... и нам конечно... очень лестно,"

        lyubskij "Что вы... Но, я боюсь, не будет ли им тесно..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        hide kutermina

        show kutermina at left
        show lyubskaya at right

        hide kutermina

        show kutermina at left
        show lyubskaya at right

        kutermina "<{i}(Любской){/i}>"

        hide lyubskaya

        show kutermina at truecenter

        hide lyubskaya

        show kutermina at truecenter

        kutermina "Я вас, мои друзья, считаю за родных,"

        kutermina "Однако ж все-таки хотела прежде их"

        kutermina "Представить вам сама."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Напрасно вы трудились."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Помилуй, матушка! На что б они годились,"

        kutermina "Когда б учтивости не стали наблюдать?"

        kutermina "А нынче, нечего, лишь стоит волю дать,"

        kutermina "Тотчас нагрянут все - и даже есть нахалы,"

        kutermina "Которые везде втираются на балы,"

        kutermina "Хоть не были б никем туда приглашены."

        kutermina "Вот я так нет! Люблю держаться старины"

        kutermina "И долг мой не считать за вежливость пустую."

        kutermina "Всегда, как следует, сперва рекомендую,"

        kutermina "А там и привезу - и трудно ль в первый раз"

        kutermina "С визитом побывать? Сегодня я приказ"

        kutermina "Моим племянникам дала, и очень строго,"

        kutermina "Чтоб им... Ты знаешь их?"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}У вас родных так много..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Отец их, Пустельгин, двоюродный мой брат."

        kutermina "Я знала наперед, что ты им будешь рад,"

        kutermina "Однако же сюда приехать им велела."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Помилуйте! На что?"

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Я просто бы не смела"

        kutermina "Их на вечер привесть."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(в сторону){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Да что же я молчу?"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Громко){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Позвольте вам сказать..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}И слушать не хочу!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Вы беспокоили племянников напрасно."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Эх, батюшка, поверь, их баловать опасно:"

        kutermina "Как раз зазнаются, повадку только дай!"

        kutermina "Нет! Дружба дружбою, а долг свой наблюдай!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Не спорю, матушка, всё это справедливо..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "О, я на этот счет отменно щекотлива."

        kutermina "Невежу не пущу к себе на полдвора."

        kutermina "Да что ж они? Давно б приехать им нора,"

        kutermina "Мне кажется: я к ним сегодня до рассвета"

        kutermina "Отправила слугу..."

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(Смотрит в окно){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "{space=400}А вот и их карета!"

        kutermina "Приехали!"

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(Идет к дверям.){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        lyubskij "<{i}(Посошкову){/i}>"

        hide pososhkov

        show lyubskij at truecenter

        hide pososhkov

        show lyubskij at truecenter

        lyubskij "{space=400}В ней нет и на волос стыда."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Какой в ней стыд!"

        hide pososhkov

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Сюда, голубчики! Сюда!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну, можно ль быть кому бесстыдней и наглее!"

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Андрюша, Ванечка! Ступайте же скорее!"

        hide kutermina

    label Act_1_Scene_7:
        "{b}ЯВЛЕНИЕ 7{/b}"

        show pervyj_plemyannik at left
        show vtoroj_plemyannik at right

        show pervyj_plemyannik at left
        show vtoroj_plemyannik at right

        "<{i}Те же, 1-й племянник и 2-й племянник.{/i}>"

        hide pervyj_plemyannik
        hide vtoroj_plemyannik

        hide pervyj_plemyannik
        hide vtoroj_plemyannik

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Вот, батюшка, они! С рук на руки сдаю."

        kutermina "Племянник мой Андрей, от вас не потаю,"

        kutermina "Отцовский фаворит."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}О, в этом я уверен!"

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Да то беда, служить он в коннице намерен,"

        kutermina "И вот, как видите, усы уж отпустил."

        kutermina "Ох, эта молодежь! Отец его просил,"

        kutermina "Мы все: \"Андрюшенька, убьют!\" - Так нет! Всё даром -"

        kutermina "Решительно сказал, что хочет быть гусаром,"

        kutermina "И служба статская ему как острый нож."

        kutermina "Вот Ванечка совсем на брата не похож,"

        kutermina "Ученый человек и даже был студентом."

        kutermina "Племянник не сочтет, конечно, комплиментом,"

        kutermina "Когда при всех ему скажу в глаза, что он"

        kutermina "Чуть-чуть не философ, учен, переучен,"

        kutermina "Науки нет такой, где б он не отличился,"

        kutermina "Всё знает, мой отец, и - физике учился."

        hide kutermina

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да этой болтовне не будет и конца."

        hide pososhkov

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Со свечкой поискать такого мудреца."

        hide kutermina

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(тихо Любскому){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        pososhkov "Отделайтесь скорей!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Я крайне сожалею,"

        lyubskij "Что не могу никак... и даже их не смею"

        lyubskij "Сегодня пригласить. Я очень бы желал"

        lyubskij "Иметь их у себя, но наш театр так мал,"

        lyubskij "Ко мне же назвалось гостей, конечно, вдвое,"

        lyubskij "Чем мог я ожидать..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}И, батюшка, пустое!"

        kutermina "Два гостя лишние не значат ничего."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Клянусь вам, не могу..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Я ж места одного"

        kutermina "Для Ванечки прошу."

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(Показывая на другого племянника){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "{space=400}Об этом, мой почтенный,"

        kutermina "Прошу не хлопотать: ведь он полувоенный -"

        kutermina "Протрется как-нибудь."

        hide kutermina

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(Любскому){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        pososhkov "{space=400}Охота ж время длить!"

        pososhkov "Решитесь поскорей."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Извольте, так и быть!"

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Спасибо, мой отец!.."

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(Племянникам){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "{space=400}Ну, что ж? Благодарите!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Быть может, господа, в дверях вы постоите -"

        lyubskij "Вперед вам говорю."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Взойти бы только в дверь,"

        kutermina "А там уж их беда."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Позвольте нам теперь"

        lyubskij "Заняться пробою, нам, право, недосужно."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Сейчас, почтенный мой, сейчас! мне только нужно"

        kutermina "Минутки две."

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(Племянникам){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "{space=400}При мне карету запрягли,"

        kutermina "Так что ж они?"

        hide kutermina

        show pervyj_plemyannik at truecenter

        $ pervyj_plemyannik_var = "{noalt}1-й племянник"

        pervyj_plemyannik "{space=400}В одну усесться не могли."

        hide pervyj_plemyannik

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ах, боже мой! Еще? Нет, это уж злодейство!"

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Да, да! Еще кой-кто из нашего семейства:"

        kutermina "Сейчас представлю вам, сейчас!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Напрасный труд!"

        lyubskij "Я вам уж объяснял."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Их тотчас привезут."

        kutermina "Что ж делать, мой отец! Уж я дала им слово!"

        kutermina "К тому же всё свои, ни одного чужого:"

        kutermina "Мусьё Ле Гро, жена его, мадам Ад ель,"

        kutermina "Отличный человек; немецкая мамзель"

        kutermina "Шарлотта Карловна, немножечко болтлива,"

        kutermina "Зато уж как добра, тиха, неприхотлива!"

        kutermina "Как ходит за детьми! На шаг не отстает."

        kutermina "Старательна, умна и дешево берет."

        kutermina "А там еще кой-кто, но этою безделкой"

        kutermina "Не стоит затруднять тебя - народ всё мелкой."

        kutermina "Послушай, душенька, голубчик, золотой!"

        kutermina "Потешь моих внучат! - Всего-то их... постой!"

        kutermina "Танюша, Верочка, Акуленька и Глаша,"

        kutermina "Да, кажется, еще..."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Еще? - Нет, воля ваша..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        play sound1 running

        hide kutermina

        show kutermina at truecenter

        play sound1 running

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(бежит к дверям){/i}>"

        show kutermina at truecenter

        stop sound1

        show kutermina at truecenter

        stop sound1

        kutermina "Приехали. Сюда, мусьё, ведите их!"

        hide kutermina

    label Act_1_Scene_8:
        "{b}ЯВЛЕНИЕ 8{/b}"

        show uchitel at left
        show guvernantka at truecenter
        show nyanjushka at right

        show uchitel at left
        show guvernantka at truecenter
        show nyanjushka at right

        "<{i}Те же, учитель, гувернантка, нянюшка, четыре девочки и два мальчика.{/i}>"

        hide uchitel
        hide guvernantka
        hide nyanjushka

        hide uchitel
        hide guvernantka
        hide nyanjushka

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Что вижу! Боже мой! Весь род Кутерминых!"

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Позволь им, батюшка! Ты этим мне докажешь,"

        kutermina "Что истинный мой друг! Неужели откажешь?"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да что ж, помилуйте! Ведь дом мой не трактир."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "И! Что ты, мой отец!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Вы этак целый мир"

        lyubskij "Готовы привести."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Но ты мне сам позволил..."

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Где видано?.."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}За что разгневаться изволил?"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "За что? Да вы ко мне пристали, как с ножом."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Ах, батюшки! - И век не загляну в твой дом,"

        kutermina "А с горя не умру. Ступайте вон!.. Ну что же!"

        hide kutermina

        show kutermina at left
        show uchitel at truecenter
        show guvernantka at right

        hide kutermina

        show kutermina at left
        show uchitel at truecenter
        show guvernantka at right

        kutermina "<{i}Учитель, гувернантка и дети уходят.{/i}>"

        hide uchitel
        hide guvernantka

        show kutermina at truecenter

        hide uchitel
        hide guvernantka

        show kutermina at truecenter

        kutermina "Не знала, батюшка, что вам театр дороже"

        kutermina "Таких друзей, как я! Возможно ль! Отказать"

        kutermina "В такой безделице! А правду-то сказать:"

        kutermina "Чего смотреть?"

        hide kutermina

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Чего? Нет, это уж бесстыдство"

        pososhkov "Из меры вон!"

        hide pososhkov

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Да, да! И что за любопытство?"

        kutermina "Большая невидаль - театр! Ах, боже мой!"

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(Племянницам){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "Вы с братьями сейчас в карету и домой!"

        kutermina "Племянницы и племянники уходят."

        hide kutermina

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Позвольте доложить! Вы сердитесь напрасно..."

        hide pososhkov

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "За вежливость мою наказана прекрасно!"

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(В сторону){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "Добро, ты грубиян!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Мне, право, очень жаль..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Конечно, и для нас ужасная печаль!"

        kutermina "Я знаю, ваш театр - осьмое в свете чудо."

        hide kutermina

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(тихо Любскому){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        pososhkov "Мы целый день ее не выживем отсюда,"

        pososhkov "Уйдемте поскорей."

        hide pososhkov

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(в сторону){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "{space=400}О, если б я могла"

        kutermina "Порядком отплатить!"

        hide kutermina

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show kutermina at right

        hide lyubskij

        show lyubskij at left
        show kutermina at right

        lyubskij "<{i}(Кутерминой){/i}>"

        hide kutermina

        show lyubskij at truecenter

        hide kutermina

        show lyubskij at truecenter

        lyubskij "{space=400}У нас свои дела,"

        lyubskij "Итак, позвольте нам..."

        hide lyubskij

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Кто держит вас? Идите."

        hide kutermina

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "На пробу нам пора."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Прошу вас, не взыщите,"

        lyubskij "Что мы оставим вас одних. Пойдем, жена!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Позволь хоть мне..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И, вздор! Пускай сидит одна!"

        hide lyubskij

        show kutermina at left
        show biryulkin at right

        show kutermina at left
        show biryulkin at right

        "<{i}Все уходят; Кутермина останавливает Бирюлькина.{/i}>"

        hide kutermina
        hide biryulkin

        hide kutermina
        hide biryulkin

    label Act_1_Scene_9:
        "{b}ЯВЛЕНИЕ 9{/b}"

        show kutermina at left
        show biryulkin at right

        show kutermina at left
        show biryulkin at right

        "<{i}Кутермина и Бирюлькин.{/i}>"

        hide kutermina
        hide biryulkin

        hide kutermina
        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Два слова, душенька! Но только с уговором:"

        kutermina "Всю правду мне скажи! Ты также здесь актером?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Кто, я-с? Что грех таить! Уж, видно, так судьбе"

        biryulkin "Угодно, матушка..."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Не стыдно ли тебе,"

        kutermina "Проживши столько лет, на старости срамиться!"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Так, так, сударыня!"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Ну, можно ль согласиться?.."

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Всё знаю, матушка! - Меня как на убой"

        biryulkin "Ведут..."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Они в глаза смеются над тобой."

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "А что! И подлинно!"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Да, это очевидно."

        kutermina "Эх, батюшка, Максим Петрович! - Как не стыдно"

        kutermina "Хотеть в твои лета нарядным шутом быть!"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Так, так!"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Эй, будешь ты в бубенчиках ходить!"

        kutermina "Ну, ежели они тебя оденут франтом?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Навеки осрамят."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Добро б ты был с талантом,"

        kutermina "А то - подумай сам! Ну, что ты за актер?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Ох, точно так! Беда! - Бесчестье и позор!"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Да что ты охаешь? К чему все эти вздохи?"

        kutermina "Не сам ли ты пошел охотой в скоморохи?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Охотой, матушка? Да кто бы мне велел!"

        biryulkin "Помилуйте, за что?"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Так ты, сударь, хотел"

        kutermina "Всем разом угодить?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Какое угожденье!"

        biryulkin "Я Любского боюсь: опишет всё именье."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Опишет? - Почему?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Ведь я его должник."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Должник?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}По векселю, хоть долг мой невелик,"

        biryulkin "Но я уплатою отменно озабочен."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "И срок уже прошел?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Давным-давно просрочен -"

        biryulkin "Как раз потянет в суд."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Смотри, какой злодей!"

        kutermina "А сколько должен ты?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}До тысячи рублей."

        biryulkin "Поверите ль, какой терплю я недостаток:"

        biryulkin "Копейки в доме нет. Вот если бы до Святок"

        biryulkin "Хотел он подождать, иль только до зимы..."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Послушай! Так и быть! Я дам тебе взаймы,"

        kutermina "Но только с тем, чтоб ты от роли отказался."

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "Ах, боже мой! Да как?"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "{space=400}Чего ж ты испугался?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "А Любский, матушка? Беда! Ведь он презлой!"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Так хочешь ты, чтоб все смеялись над тобой,"

        kutermina "Не только взрослые, но даже и ребята?"

        kutermina "Подумай, у тебя давно уж есть внучата,"

        kutermina "Хоть их-то не срами!"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Всё так... я знаю сам..."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Послушай, душенька! Ведь я отсрочку дам"

        kutermina "Еще на целый год."

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}О, если так - извольте!"

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Нельзя ль еще кого?.. Да много ль вас?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Постойте!"

        biryulkin "Во-первых я, потом какой-то Прямиков,"

        biryulkin "Которого все ждут, там Вельский, Посошков..."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "И этот Вельский здесь? - Мальчишка преупрямый,"

        kutermina "Племянник Волгина?"

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Да, матушка, тот самый."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Что, если б мне?.. А что ж? Попытка не беда."

        kutermina "Отправлюсь к Волгину. - А ты ступай туда,"

        kutermina "Молчи, и в пять часов иль около шестого"

        kutermina "Явись ко мне домой. - Да слышишь ли - ни слова!"

        kutermina "Чтобы никто не знал..."

        hide kutermina

        show biryulkin at truecenter

        $ biryulkin_var = "{noalt}Бирюлькин"

        biryulkin "{space=400}Когда угодно вам,"

        biryulkin "Так я, сударыня, и виду не подам."

        hide biryulkin

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        kutermina "Ну то-то же, ступай!"

        hide kutermina

        show biryulkin at truecenter

        show biryulkin at truecenter

        "<{i}Бирюлькин уходит.{/i}>"

        hide biryulkin

        hide biryulkin

    label Act_1_Scene_10:
        "{b}ЯВЛЕНИЕ 10{/b}"

        show kutermina at truecenter

        $ kutermina_var = "{noalt}Кутермина"

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(одна){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        kutermina "{space=400}Теперь-то постараюсь!"

        kutermina "Добро, мой друг! Уж я с тобою расквитаюсь,"

        kutermina "Все мерзости твои на деле докажу:"

        kutermina "Поеду к Волгину, о всем ему скажу,"

        kutermina "Раскрашу, распишу, где надобно прибавлю,"

        kutermina "Взбешу его - и ваш театр вверх дном поставлю."

        hide kutermina

        show kutermina at truecenter

        hide kutermina

        show kutermina at truecenter

        kutermina "<{i}(Уходит.){/i}>"

        show kutermina at truecenter

        show kutermina at truecenter

        hide kutermina

label Act_5:
    play music "audio/music/103.mp3" fadeout 1.0 fadein 1.0

    scene 27 with fade

    "{b}ДЕЙСТВИЕ ТРЕТЬЕ{/b}"

    "<{i}Та же комната.{/i}>"

    menu:
        "{color=#000}ЯВЛЕНИЕ 1{/color}":
            jump Act_2_Scene_1
        "{color=#000}ЯВЛЕНИЕ 2{/color}":
            jump Act_2_Scene_2
        "{color=#000}ЯВЛЕНИЕ 3{/color}":
            jump Act_2_Scene_3
        "{color=#000}ЯВЛЕНИЕ 4{/color}":
            jump Act_2_Scene_4
        "{color=#000}ЯВЛЕНИЕ 5{/color}":
            jump Act_2_Scene_5
        "{color=#000}ЯВЛЕНИЕ 6{/color}":
            jump Act_2_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_2_Scene_6_1

label Further_Act_2_Scene_6_1:
    menu:
        "{color=#000}ЯВЛЕНИЕ 7{/color}":
            jump Act_2_Scene_7
        "{color=#000}ЯВЛЕНИЕ 8{/color}":
            jump Act_2_Scene_8
        "{color=#000}ЯВЛЕНИЕ 9{/color}":
            jump Act_2_Scene_9
        "{color=#000}ЯВЛЕНИЕ 10{/color}":
            jump Act_2_Scene_10
        "{color=#000}ЯВЛЕНИЕ 11{/color}":
            jump Act_2_Scene_11

    label Act_2_Scene_1:
        "{b}ЯВЛЕНИЕ 1{/b}"

        show velskij at left
        show izvedov at right

        show velskij at left
        show izvedov at right

        "<{i}Вельский и Изведов. Входят на сцену из средних дверей.{/i}>"

        hide velskij
        hide izvedov

        hide velskij
        hide izvedov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Итак, спектакель наш придется отложить?"

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Что ж делать? Прямиков..."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Неужто упросить"

        izvedov "Его нельзя никак?"

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}К несчастию - нет средства,"

        velskij "На днях он получил какое-то наследство"

        velskij "И едет за сто верст."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=200}Когда?"

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Сегодня в ночь."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Так горю вашему придется мне помочь,"

        izvedov "Отдайте ролю мне, я дело всё поправлю."

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Ты хочешь сам играть?"

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}За счастие поставлю."

        izvedov "Не спорю, эта честь отменно велика,"

        izvedov "Зато, ручаюсь вам, что в роли старика"

        izvedov "Увидите во мне отличного актера."

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Всё так, но как же нам остаться без суфлера?"

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Да разве приказать не можно никому?"

        izvedov "Заставьте, например, буфетчика Фому."

        izvedov "Он малый грамотный: не только что свободно,"

        izvedov "Читает мастерски - а впрочем, как угодно."

        izvedov "Принять и не принять вольны вы мой совет,"

        izvedov "А только, верьте мне, другого средства нет."

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Ступай же поскорей, узнай от Посошкова..."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Сейчас, сударь, иду! - Одно лишь только слово:"

        izvedov "Скажите мне, что вам Честонов говорил?"

        izvedov "За вас он или нет?"

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Он жизнь мне возвратил."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Так он не против вас?"

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=200}Нимало."

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Что за диво!"

        izvedov "К чему ж он говорил: \"Племянница счастлива:"

        izvedov "Жених мне по сердцу; он скромен, тих, с умом...\""

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Да знаешь ли, кого считал он женихом?"

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Кого? Неужто вас?"

        hide izvedov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Насилу догадался!"

        hide velskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Вот что! - Ах я дурак! Чего же я боялся?"

        izvedov "Хоть дядя против вас, но это пустяки. -"

        izvedov "Ура, сударь! Когда Честонов вам с руки,"

        izvedov "Бояться нечего, теперь нам всё возможно."

        hide izvedov

    label Act_2_Scene_2:
        "{b}ЯВЛЕНИЕ 2{/b}"

        show chestonov at truecenter

        show chestonov at truecenter

        "<{i}Те же и Честонов.{/i}>"

        hide chestonov

        hide chestonov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at left
        show velskij at right

        hide chestonov

        show chestonov at left
        show velskij at right

        chestonov "<{i}(Вельскому){/i}>"

        hide velskij

        show chestonov at truecenter

        hide velskij

        show chestonov at truecenter

        chestonov "Скорей, мой друг, скорей! Тебе сейчас же должно"

        chestonov "Отправиться домой. Ужасная беда!"

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "А что?.."

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Твой дядюшка сбирается сюда."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Сюда?.."

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Не знаю, кто изволил потрудиться"

        chestonov "И всё ему сказать; он хочет объясниться,"

        chestonov "От Любских получить решительный ответ,"

        chestonov "Кричит, что совести ни на волос в них нет,"

        chestonov "Что он никак не даст племянника дурачить,"

        chestonov "Что свадьбы день должны сегодня же назначить,"

        chestonov "Что быть игрушкой их никто не сотворен,"

        chestonov "Бранит весь свет, шумит и, словом, так взбешен,"

        chestonov "Что с братом он тебя поссорит непременно."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Ах, боже мой! Он всё испортит совершенно,"

        velskij "Рассердит Любского."

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}И наш расстроит план."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "А скоро будет он?"

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}При мне надел кафтан,"

        chestonov "И я его почти оставил за порогом."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Что ж делать мне?"

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Скачи домой и под предлогом"

        chestonov "Каким-нибудь его старайся удержать."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Но вот беда: пешком придется мне бежать."

        velskij "Я дрожки отпустил."

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Ступай в моей карете,"

        chestonov "А я к своим пойду."

        hide chestonov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Ваш братец в кабинете!"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(Показывая, куда идти){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "Вот здесь!"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(Уходит вместе с Честоновым.){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        hide izvedov

    label Act_2_Scene_3:
        "{b}ЯВЛЕНИЕ 3{/b}"

        show velskij at left
        show pososhkov at right

        show velskij at left
        show pososhkov at right

        "<{i}Вельский и потом Посошков в французском шитом кафтане.{/i}>"

        hide velskij
        hide pososhkov

        hide velskij
        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Ну, если он?.. И вздумать не могу!"

        hide velskij

        show velskij at left
        show pososhkov at right

        hide velskij

        show velskij at left
        show pososhkov at right

        velskij "<{i}(Хочет идти, но в дверях встречается с Посошковым){/i}>"

        hide pososhkov

        show velskij at truecenter

        hide pososhkov

        show velskij at truecenter

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(оборотясь назад){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Я завтра с деньгами пришлю к нему слугу."

        pososhkov "Что, что?.. И, вздор! Уж мы условились о плате"

        pososhkov "С хозяином твоим, ступай! - А, Вельский! - Кстати!"

        pososhkov "Я уважал всегда ваш тонкий вкус и ум -"

        pososhkov "Извольте-ка взглянуть! - Каков, сударь, костюм?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Хорош..."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Не правда ли? Уж мы не ошибемся."

        pososhkov "Ну, что ваш дядюшка? Когда его дождемся?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(с удивлением){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "Так вы уж знаете, что будет он сюда?"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да это знают все."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=200}Ах, боже мой!"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Хочет идти.){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(удерживая){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Куда?"

        pososhkov "Позвольте вас спросить: он родственник вам дальний?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Кто? Дядя мой?"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ну да! - Ваш дядя театральный,"

        pososhkov "Вот этот - как его? - Не помню..."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Прямиков?"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да, точно так! - А что, он роли стариков"

        pososhkov "Всегда играл?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(с нетерпением){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=200}Всегда."

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Хочет идти.){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(удерживая){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Да что за нетерпенье?"

        pososhkov "Куда спешите вы? Итак - уж нет сомненья -"

        pososhkov "Спектакель наш пойдет?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Пойдет! Я слышу стук!"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "И вы уверены..."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Мне, право, недосуг!"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Смотрит в окно){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "Так точно! - Дядюшка!"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}А можете ль ручаться,"

        pososhkov "Что скоро будет он?"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Сейчас! - Куда деваться?"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Смотрите же!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(в сторону){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}Пошлю Честонова скорей!"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(Уходит в боковую дверь.){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        hide velskij

    label Act_2_Scene_4:
        "{b}ЯВЛЕНИЕ 4{/b}"

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(один){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Куда же вы? - Чуть-чуть не изломал дверей."

        pososhkov "Да что с ним сделалось? О чем он так хлопочет?"

        pososhkov "Когда уж и меня он выслушать не хочет,"

        pososhkov "Так, видно, чем-нибудь, а занят не шутя."

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Смотрит в зеркало){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Какой костюм! Я рад и весел, как дитя!"

        pososhkov "Куда, подумаешь, как мода прихотлива!"

        pososhkov "Что лучше этого? - И прочно и красиво,"

        pososhkov "Так нет! Дай выдумать - и что ж? Дурацкий фрак..."

        pososhkov "Ну можно ли сравнить?.."

        hide pososhkov

    label Act_2_Scene_5:
        "{b}ЯВЛЕНИЕ 5{/b}"

        show pososhkov at left
        show volgin at right

        show pososhkov at left
        show volgin at right

        "<{i}Посошков и Волгин.{/i}>"

        hide pososhkov
        hide volgin

        hide pososhkov
        hide volgin

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(говорит человеку, который за ним входит){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Как нет? Ты врешь, дурак!"

        volgin "Я видел их в окно."

        hide volgin

        "<{i}Человек уходит.{/i}>"

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show volgin at right

        hide pososhkov

        show pososhkov at left
        show volgin at right

        pososhkov "<{i}(продолжает смотреться в зеркало, не замечая Волгина){/i}>"

        hide volgin

        show pososhkov at truecenter

        hide volgin

        show pososhkov at truecenter

        pososhkov "{space=400}Хоть в этом я наряде"

        pososhkov "Постарее кажусь, зато при первом взгляде"

        pososhkov "Заметен уж актер, во всех движеньях жар,"

        pososhkov "Экспрессия, душа!.."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(глядя с удивлением на Посошкова){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Что это за фигляр?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Прочесть бы мне теперь тирады две из роли."

        pososhkov "Во фраке всё не то: нельзя и третьей доли"

        pososhkov "Таланта показать, всего важней костюм."

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Декламируя){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Постой! - да, да! \"Тебе наскучил этот шум,"

        pososhkov "Так знай, сударыня, скажу тебе заране,"

        pososhkov "Что я...\" - Опять забыл!"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Вынимает ролю.){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}В узорчатом кафтане..."

        volgin "Бормочет про себя... Так точно! Это шут."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(читая по роле){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "\"Все хитрости твои к чему тебя ведут?"

        pososhkov "Что прибыли тебе в увертке бесполезной?"

        pososhkov "Скажи, бесстыдная...\""

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(ударив по плечу Посошкова){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Послушай-ка, любезный!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Чего хотите вы? - Кто б это был таков?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Скажи, пожалуйста..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Неужто Прямиков?"

        pososhkov "Кого вам надобно?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Хозяина мне нужно."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Хозяина? На что?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Мне, право, недосужно."

        volgin "Ступай и доложи ему..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Какой чудак!"

        pososhkov "Конечно, Вельский вас сюда..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Да, точно так,"

        volgin "Я здесь для Вельского."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Теперь я понимаю."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Ты хочешь знать, кто я таков?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Всё знаю."

        pososhkov "Мы ждали вас..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=200}Меня?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ну да! конечно, вас."

        pososhkov "Хоть с вами видимся мы в первый раз,"

        pososhkov "Но я наслышался о вашем дарованьи,"

        pososhkov "Давно хотел вас знать: теперь мое желанье"

        pososhkov "Исполнилось, и я..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(в сторону){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Как Тришка мой, точь-в-точь!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Надеждой льщу себя..."

        hide pososhkov

        show pososhkov at left
        show volgin at right

        hide pososhkov

        show pososhkov at left
        show volgin at right

        pososhkov "<{i}(Подает Волгину руку.){/i}>"

        hide volgin

        show pososhkov at truecenter

        hide volgin

        show pososhkov at truecenter

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(подавая ему также руку){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Пожалуй! Я не прочь."

        volgin "До вашей братьи я охотник пресмертельный:"

        volgin "Да ты ж, мне кажется, и вовсе неподдельный,"

        volgin "С природы, так. - Давно ль ты к Любскому попал?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(в сторону){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Уж не ошибся ль я? Что ж это за нахал?"

        pososhkov "Спрошу!.."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(в сторону){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Ну можно ли, на эту рожу глядя,"

        volgin "Не треснуть со смеху?.."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ведь вы должны быть дядя?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Конечно, я! - И что я этим дорожу,"

        volgin "Сегодня же при всех на деле покажу."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Так точно - это он!"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Мне доказать нетрудно..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Хоть изъясняетесь вы несколько и чудно,"

        pososhkov "Но вашим истинно любуюсь я лицом:"

        pososhkov "Вы рождены, чтоб быть комическим отцом."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Каким?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Комическим, и точно есть надежда,"

        pososhkov "Что в вашем амплуа..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=200}Что, что?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(в сторону){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Да он невежда!"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "О чем ты говоришь?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Я говорю о том,"

        pososhkov "Что вы..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}И я хорош, связался с дураком."

        volgin "Послушай, брат! С тобой я только время трачу,"

        volgin "А мне бы надобно..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Пущуся наудачу!"

        pososhkov "Позвольте прежде мне кой-что вам пояснить."

        pososhkov "Характер ваш: его нетрудно вам схватить,"

        pososhkov "Он прост, зато на вас племянник не походит"

        pososhkov "И дядю, то есть вас, порядком за нос водит."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Ну так! Я это знал."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Племянник ваш влюблен,"

        pososhkov "Так вас обманывать невольно принужден."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Вот что! - Прекрасную ж играть я должен ролю!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да, роля хороша!.."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}И я себя позволю..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Послушайте! Когда я вместе вас свожу,"

        pososhkov "Вы скажете ему..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Я знаю, что скажу:"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(С жаром){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "Бессовестный! Тебя как сына я родного"

        volgin "С ребячества любил! - Пусть дядю б ты другого"

        volgin "Не ставил в грош, а то, кого ж? - Меня, злодей!"

        volgin "Обманывать, срамить и всех честных людей"

        volgin "Заставить надо мной почти в глаза смеяться!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Ого! Какой талант!"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Прошу со мной не знаться!"

        volgin "Когда намеренье тобою принято"

        volgin "Дурачить старика..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Прекрасно, - а не то!"

        pososhkov "Горячий этот тон вам вовсе неприличен."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Таков характер мой..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Он тем-то и отличен,"

        pososhkov "Что вы других во всем гораздо холодней."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "С чего ты это взял?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Кому же знать верней?"

        pososhkov "Вы смирный человек, ни бедны, ни богаты,"

        pososhkov "Недальнего ума и даже глуповаты..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Кто? Я?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Ну да! Вот весь характер ваш."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ты врешь!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Я вру? - Как смели вы?.."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Да что ты пристаешь?"

        volgin "Пошел, дурак!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Дурак! - На что это похоже?"

        pososhkov "Позвольте вам сказать - за это бьют по роже."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Эй, слушай, брат, отстань!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Зажмите, сударь, рот!"

        pososhkov "Да знаете ль, кто вы? Вы сущий готтентот!"

        pososhkov "Вы варвар, вы мужик, вы в лицах век прошедший..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Эге! Да он не шут, а просто сумасшедший."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Возможно ли? И как вам в голову взошло!.."

        pososhkov "Как смели вы сказать!.."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Чтоб худо не пришло,"

        volgin "Убраться поскорей!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Нет, кончено! Вам роли"

        pososhkov "В пиэсе не даю."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ну можно ли по воле"

        volgin "Пускать таких людей!"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(Хочет идти.){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}И кто вам право дал!"

        pososhkov "Я вас не выпущу. - Куда?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Вот черт пристал!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Не думаете ль вы, что важную находку"

        pososhkov "Мы в вас нашли?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ну, ну! - Я дам тебе на водку,"

        volgin "Лишь только отвяжись! - На гривенник, возьми!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Как, гривенник! - Кому?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Да полно, не шуми!"

        volgin "Я дам еще."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Как? Что? - Так дерзко насмехаться!"

        pososhkov "Да знаете ль, что я..."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ахти! Он хочет драться!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Куда, сударь! - Я вас заставлю отвечать!"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Ах, батюшки! - Да он презлой! Пришлось кричать!"

        play sound1 running

        hide volgin

        show volgin at truecenter

        play sound1 running

        hide volgin

        show volgin at truecenter

        volgin "<{i}(Бежит к дверям и кричит){/i}>"

        show volgin at truecenter

        stop sound1

        show volgin at truecenter

        stop sound1

        volgin "Послушайте!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(становится в дверях){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Я вас не подпущу к порогу."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(кричит){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "Эй, кто-нибудь! - Сюда!"

        hide volgin

    label Act_2_Scene_6:
        "{b}ЯВЛЕНИЕ 6{/b}"

        show chestonov at truecenter

        show chestonov at truecenter

        "<{i}Те же и Честонов.{/i}>"

        hide chestonov

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Честонов! - Слава богу!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Ага! Вы струсили теперь!"

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Что здесь за шум?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Поди сюда, скорей!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Ба-ба! - Любезный кум!"

        chestonov "Давно ли здесь?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(прячется за него){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Постой! - Дай отдохнуть немного."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Что сделалось с тобой?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Боитесь ли вы бога?"

        volgin "К чему держать таких опасных дураков?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(отводя Честонова){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Позвольте вас спросить - ведь это Прямиков?"

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(в сторону){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "Вот кстати!"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(Громко){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "{space=200}Точно так."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Предерзкое творенье!"

        pososhkov "Какой трактирный тон, какое обращенье!"

        pososhkov "Таких людей, как он, животными зовут."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at left
        show chestonov at right

        hide volgin

        show volgin at left
        show chestonov at right

        volgin "<{i}(тихо Честонову){/i}>"

        hide chestonov

        show volgin at truecenter

        hide chestonov

        show volgin at truecenter

        volgin "Скажи, пожалуйста! Безумный он иль шут?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(так же){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "Да как тебе сказать? - Я думаю, всё вместе."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show chestonov at right

        hide pososhkov

        show pososhkov at left
        show chestonov at right

        pososhkov "<{i}(Честонову){/i}>"

        hide chestonov

        show pososhkov at truecenter

        hide chestonov

        show pososhkov at truecenter

        pososhkov "Я вовсе не бретер, но ежели до чести"

        pososhkov "Коснется кто моей, то боже сохрани!"

        pososhkov "Я этим не шучу."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at left
        show chestonov at right

        hide volgin

        show volgin at left
        show chestonov at right

        volgin "<{i}(Честонову){/i}>"

        hide chestonov

        show volgin at truecenter

        hide chestonov

        show volgin at truecenter

        volgin "{space=400}Эх, братец! - Прогони"

        volgin "Его!"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show chestonov at right

        hide pososhkov

        show pososhkov at left
        show chestonov at right

        pososhkov "<{i}(Честонову){/i}>"

        hide chestonov

        show pososhkov at truecenter

        hide chestonov

        show pososhkov at truecenter

        pososhkov "{space=400}Чтоб я спустил такому грубияну!"

        pososhkov "Во-первых, с ним играть решительно не стану,"

        pososhkov "Хоть, правда, без него придется худо нам,"

        pososhkov "Но так и быть."

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да он совсем не нужен вам."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Вот то-то и беда! Актера нет другого."

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Напротив, ваш театр идет без Прямикова."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Нет, шутите?"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at left
        show chestonov at right

        hide volgin

        show volgin at left
        show chestonov at right

        volgin "<{i}(Честонову){/i}>"

        hide chestonov

        show volgin at truecenter

        hide chestonov

        show volgin at truecenter

        volgin "{space=400}Ну, что ж! - Спровадь скорей его."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "И чтоб уладить всё, ждут вас лишь одного."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Иду, бегу, сейчас!"

        hide pososhkov

        show pososhkov at left
        show volgin at right

        hide pososhkov

        show pososhkov at left
        show volgin at right

        pososhkov "<{i}(Волгину){/i}>"

        hide volgin

        show pososhkov at truecenter

        hide volgin

        show pososhkov at truecenter

        pososhkov "{space=400}Мне должно бы отчета"

        pososhkov "От вас потребовать..."

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(отводя Посошкова){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "{space=400}И что вам за охота!"

        chestonov "Он человек простой, к тому же мне родня..."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Ну, если бы не вы - узнал бы он меня!"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Уходит.){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        hide pososhkov

    label Act_2_Scene_7:
        "{b}ЯВЛЕНИЕ 7{/b}"

        show volgin at left
        show chestonov at right

        show volgin at left
        show chestonov at right

        "<{i}Волгин и Честонов.{/i}>"

        hide volgin
        hide chestonov

        hide volgin
        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Тьфу, черт его возьми! Насилу провалился!"

        volgin "Когда б послушал ты, как он со мной бранился!"

        volgin "Сначала всё шутил, да вдруг перед концом"

        volgin "И ну ругать меня комическим отцом,"

        volgin "Невежей, мужиком, - вот так и лез на драку."

        volgin "Охота же держать такого забияку!"

        volgin "Нет! Тришка мой хоть зол, а всё-таки смирней:"

        volgin "С ним можно пошутить, а этого не смей"

        volgin "Назвать и дураком..."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}А ты назвал?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Так что же!"

        volgin "По-моему, дурак и шут - одно и то же."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Да что он говорил с тобой?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Какой-то вздор."

        volgin "О роле мне твердил, как будто б я актер,"

        volgin "Да это ничего - из этих слов лишь видно,"

        volgin "Что вовсе он дурак, а вот что, брат, обидно,"

        volgin "Что я теперь и сам попался в дураки."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Попался! - Как?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}А что? - Чай, скажешь пустяки?"

        volgin "Вот этот глупый шут и тот, сударь, находит,"

        volgin "Что дядю своего племянник за нос водит,"

        volgin "А дядя-то ведь я!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Охота ж о пустом"

        chestonov "Так долго толковать. - Да дело не о том:"

        chestonov "Зачем приехал ты?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Зачем? Чтоб изъясниться,"

        volgin "Ты это знаешь сам."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Эх, братец! Торопиться"

        chestonov "Не должно бы."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Я ждал и так четыре дня,"

        volgin "И буду ждать еще?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да выслушай меня!"

        chestonov "Не лучше ль подождать, и, выбрав час свободный"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Чтоб я, премьер-майор и дворянин природный,"

        volgin "Позволил над собой шутить?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}С чего ты взял?.."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "С чего? Так слушай же! Племянник мне писал,"

        volgin "Что он посватался, что всё идет порядком:"

        volgin "Девица умная, хорошая, с достатком,"

        volgin "Что ей он нравится, и сам в нее влюблен,"

        volgin "Обласкан дядею, родными ободрен"

        volgin "И прочее. Вот я ну шить скорей наряды;"

        volgin "Домашние дела: покос, жнитво, подряды -"

        volgin "Бросаю всё, скачу, приехал наконец."

        volgin "\"Здорово, брат! - Ну что? Когда же под венец?"

        volgin "Я мешкать не люблю и на твоем бы месте"

        volgin "Всё мигом повернул. Вези меня к невесте\"."

        volgin "- \"Ах, дядюшка, нельзя! Ведь Оленька больна\"."

        volgin "- \"А Любский?\" - \"Нездоров\". - \"Так Любского жена?..\""

        volgin "- \"Могла бы вас принять, но также нездорова\"."

        volgin "- \"Помилуй, что за мор? Неужто дали слово"

        volgin "Все разом захворать?\" - \"Весь дом в постелю слег\"."

        volgin "Ну, так и быть! Я ж сам с дороги занемог;"

        volgin "Так нехотя пришлось мне дома оставаться."

        volgin "Сегодня, лишь успел со мной ты распрощаться,"

        volgin "Вдруг шасть ко мне на двор - и кто ж? Кутермина!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Матрена Савишна?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ты знаешь, что она"

        volgin "Болтунья страшная."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}За ней одно лишь дело:"

        chestonov "Злословить всех."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}А тут как будто онемела."

        volgin "Я то, я се - молчит. Конечно, есть печаль,"

        volgin "Подумал я. Спросил. \"Да, батюшка, мне ноль\"."

        volgin "- \"Кого, сударыня?\" - \"О, если непременно"

        volgin "Ты хочешь знать - тебя! Признайся откровенно:"

        volgin "Зачем ты прискакал?\" - \"Племянника женить\"."

        volgin "- \"Охота же себя на старости срамить!\""

        volgin "- \"Как так?\" - \"Да так! Тебя с племянником дурачат\"."

        volgin "- \"Но он ко мне писал\". - \"Что эти письма значат!"

        volgin "Пустое, вздор! Его, бедняжку, завели."

        volgin "Не веришь мне? Так что ж! Попробуй и вели"

        volgin "Узнать ему: когда его судьба решится?"

        volgin "А лучше и того, ступай-ка изъясниться"

        volgin "И Любских сам спроси\". - \"Спросить-то я готов,"

        volgin "Да только у кого? Ведь Любский нездоров,"

        volgin "Жена его больна, племянница в постеле\"."

        volgin "- \"Как! Любский нездоров? Неужто в самом деле?\""

        volgin "- \"Добро б один; а то, как на смех, вся семья\"."

        volgin "- \"Давно ли, мой отец?\" - \"Об этом слышал я"

        volgin "Дня три тому назад\". -\"Дня три! Ах, мой создатель!"

        volgin "Вчерась их угощал гражданский председатель,"

        volgin "А нынче был у них губернский прокурор."

        volgin "Ну, видишь ли теперь, что это всё подбор,"

        volgin "И Любские тобой как пешкою играют\"."

        volgin "Как пешкою! Меня за пешку почитают! -"

        volgin "И после этого прикажешь мне молчать?"

        volgin "Молчать! Нет, черт возьми! Да я готов кричать"

        volgin "Не только здесь, везде - в Москве на лобном месте,"

        volgin "Что в Любских нет стыда, ни совести, ни чести,"

        volgin "Что братец твой..."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Злодей! Что вся его семья,"

        chestonov "Весь Любских род: все братья, сваты, кумовья,"

        chestonov "Сестрицы, тетушки в двенадцатом колене,"

        chestonov "Все внуки, правнуки и даже предков тени"

        chestonov "Тобой решительно, навеки прокляты."

        chestonov "Довольно, кажется? - Теперь спокоен ты?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Да! Смейся, брат! Куда смешно! Умора!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Мы долго продолжать не можем разговора."

        chestonov "Итак, прошу мне дать решительный ответ,"

        chestonov "Но только в двух словах: ты хочешь или нет,"

        chestonov "Чтоб Вельский был женат?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Хочу ль, чтоб он женился!"

        volgin "Да разве двести верст я даром прокатился?"

        volgin "Нет, вздор! Хоть плачь, а мне невесту подавай!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Так дело кончено. Теперь, мой друг, ступай"

        chestonov "Скорей домой!"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=200}Домой?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Ты можешь быть спокоен:"

        chestonov "Мне Вельский по сердцу, он Оленьки достоин"

        chestonov "И будет мужем ей - за это я берусь."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Нет, милый, извини! - Пока не изъяснюсь,"

        volgin "Я с места не сойду."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Но это изъясненье"

        chestonov "Поссорит вас."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=200}Так что ж?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да сделай одолженье,"

        chestonov "Послушайся меня! Ступай скорей домой!"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "И слышать не хочу."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Так знай, любезный мой,"

        chestonov "Ты этой скоростью племянника погубишь."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Мне всё равно."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Равно? Так ты его не любишь?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Вот то-то и беда! К несчастию, люблю."

        volgin "Ну, так и быть, изволь! Сегодня потерплю,"

        volgin "Но завтра ни за что, я больше не намерен"

        volgin "Минуты ждать одной."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Сегодня ж, я уверен,"

        chestonov "Всё будет кончено."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ну, то-то же, смотри!"

        volgin "Помолвка через день, а свадьба через три. -"

        volgin "Даешь ли слово мне?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да, да, мой друг! Согласен."

        chestonov "Ступай!"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(идет и возвращается назад){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Чтоб был ответ решителен и ясен."

        volgin "Иль да, иль нет..."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Я всё порядком поведу,"

        chestonov "Лишь только уезжай скорей."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(уходя){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Иду, иду!"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(Возвращаясь){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "Смотри! - Чтоб Вельскому сегодня ж слово дали,"

        volgin "Не то - в кибитку с ним, и поминай как звали!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Уйдешь ли ты?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ведь я на это молодец,"

        volgin "И если уж решусь..."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да будет ли конец?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Иду! - Но слушай, брат, ты дал мне обещанье,"

        volgin "И я!.."

        hide volgin

        show volgin at left
        show chestonov at right

        hide volgin

        show volgin at left
        show chestonov at right

        volgin "<{i}Честонов показывает большое нетерпенье.{/i}>"

        hide chestonov

        show volgin at truecenter

        hide chestonov

        show volgin at truecenter

        volgin "{space=400}Ну-ну! - Прощай покамест, до свиданья!"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(Уходит.){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        hide volgin

    label Act_2_Scene_8:
        "{b}ЯВЛЕНИЕ 8{/b}"

        show chestonov at left
        show velskij at right

        show chestonov at left
        show velskij at right

        "<{i}Честонов, один, и потом Вельский.{/i}>"

        hide chestonov
        hide velskij

        hide chestonov
        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Уйдет ли он? - Ахти! Никак, идет назад!"

        chestonov "Ну, если как-нибудь с ним встретится мой брат?"

        chestonov "Беда! Нет! Кажется, уехал. Слава богу!"

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(выглядывая из боковых дверей){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "Что дядюшка?"

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}Ушел."

        hide chestonov

        show chestonov at left
        show velskij at right

        hide chestonov

        show chestonov at left
        show velskij at right

        chestonov "<{i}Вельский выходит.{/i}>"

        hide velskij

        show chestonov at truecenter

        hide velskij

        show chestonov at truecenter

        chestonov "{space=400}Наделал он тревогу!"

        chestonov "С ним был соперник твой."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Я это ожидал."

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "И если бы меня позвать ты опоздал,"

        chestonov "То плохо бы ему пришлось от Посошкова."

        chestonov "Он дядю твоего почел за Прямикова,"

        chestonov "А тот его назвать изволил дураком -"

        chestonov "Чуть, чуть не подрались. Но дело не о том:"

        chestonov "Мне Оленька во всем призналась откровенно,"

        chestonov "Я наш открыл ей план, и должно непременно"

        chestonov "Сегодня кончить всё. - Какой сюрприз для всех!"

        chestonov "И смело можно бы ручаться за успех,"

        chestonov "Да то беда - она ужасно боязлива."

        chestonov "Послушай, милый мой! Любовь красноречива, -"

        chestonov "Поверь, один твой взгляд подействует сильней,"

        chestonov "Чем все мои слова, а чтоб успеть верней,"

        chestonov "Решительно скажи, что средства нет другого."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Она сюда прийти сейчас дала мне слово,"

        velskij "И чтоб склонить ее, я всё употреблю."

        velskij "Ах! если б знали вы, как я ее люблю!"

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Тем лучше, милый друг! На свете всё непрочно,"

        chestonov "Но добрая жена... Идут! - Она? Так точно!"

        chestonov "Смотри не опоздай! У заднего крыльца"

        chestonov "Карета в шесть часов, а в восемь от венца."

        chestonov "Прощай, мой друг!"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(Уходит.){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        hide chestonov

    label Act_2_Scene_9:
        "{b}ЯВЛЕНИЕ 9{/b}"

        show velskij at left
        show olenka at right

        show velskij at left
        show olenka at right

        "<{i}Вельский и Оленька.{/i}>"

        hide velskij
        hide olenka

        hide velskij
        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at left
        show olenka at right

        hide velskij

        show velskij at left
        show olenka at right

        velskij "<{i}(идя навстречу к Оленьке){/i}>"

        hide olenka

        show velskij at truecenter

        hide olenka

        show velskij at truecenter

        velskij "{space=400}С каким я ждал вас нетерпеньем!"

        velskij "Всё кончено! Одно осталось нам спасеньем."

        velskij "И если уж ничто не может тронуть вас,"

        velskij "Так знайте же, что мы теперь в последний раз"

        velskij "Не только говорим, но видимся друг с другом,"

        velskij "Что нынче ж вы должны назвать меня супругом"

        velskij "Иль, может быть, со мной расстаться навсегда."

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "Расстаться? Боже мой! - Нет, Вельский! Никогда!"

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "А если завтра же откажут мне от дому?.."

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "Хотя рука моя обещана другому,"

        olenka "Хоть сердцем я могу лишь вам принадлежать,"

        olenka "Но долг забыть к родным, решиться убежать..."

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Так будьте ж им во всем, сударыня, послушны,"

        velskij "Когда к судьбе моей вы вовсе равнодушны..."

        hide velskij

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "Ах, нет!.. - Я вам клянусь!.."

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}Что значат все слова!"

        velskij "Что клятвы все! Когда священные права"

        velskij "И дружбы и любви и всё - забыто вами!"

        velskij "Любви, в которой мне сто раз клялись вы сами,"

        velskij "Мечтая с радостью о том счастливом дне,"

        velskij "Когда я буду ваш навек! Ах! Верьте мне,"

        velskij "Что счастие мое, а может быть и ваше,"

        velskij "В руках теперь у вас. Я всё сказал Наташе -"

        velskij "Сегодня в шесть часов нас будет ждать к себе"

        velskij "Ваш дядюшка... - Когда и он в моей судьбе"

        velskij "Участие берет,"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(бросаясь на колена){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}так вы ли захотите..."

        hide velskij

    label Act_2_Scene_10:
        "{b}ЯВЛЕНИЕ 10{/b}"

        show lyubskij at left
        show pososhkov at right

        show lyubskij at left
        show pososhkov at right

        "<{i}Те же, Любский и Посошков.{/i}>"

        hide lyubskij
        hide pososhkov

        hide lyubskij
        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Что вижу! Боже мой!.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Эх! Тише, не шумите!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at left
        show lyubskij at truecenter
        show pososhkov at right

        hide velskij

        show velskij at left
        show lyubskij at truecenter
        show pososhkov at right

        velskij "<{i}(не видя Любского и Посошкова){/i}>"

        hide lyubskij
        hide pososhkov

        show velskij at truecenter

        hide lyubskij
        hide pososhkov

        show velskij at truecenter

        velskij "Минуты дороги - решайтеся скорей!"

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Возможно ли! - Одна!.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Так что ж?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И Вельский с ней."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да как же иначе? Они проходят роли."

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "И вы колеблетесь! Когда от вашей воли"

        velskij "Зависит всё."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Как сметь!.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Еще! Какой болтун!"

        hide pososhkov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Решитесь быть моей!.."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(Любскому){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}Тут входит опекун.{/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at left
        show velskij at truecenter
        show olenka at right

        hide pososhkov

        show pososhkov at left
        show velskij at truecenter
        show olenka at right

        pososhkov "<{i}(Подходит к Вельскому и Оленьке){/i}>"

        hide velskij
        hide olenka

        show pososhkov at truecenter

        hide velskij
        hide olenka

        show pososhkov at truecenter

        pososhkov "{space=400}\"Ага, сударыня! Попались!\""

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "Ах, боже мой!"

        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(в сторону){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=200}Ай, ай!"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"Чего ж вы испугались?"

        pososhkov "Ведь я не муж, а только что жених."

        pososhkov "Где видано!.. - Застать вдвоем - одних!"

        pososhkov "Да как вы смели?"

        pososhkov "К чему, сударыня, зачем он с вами был?"

        pososhkov "Что, матушка! - Я вижу, онемели!.."

        pososhkov "А вас, сударь... А вас...\" - Кой черт! Опять забыл."

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Вынимает ролю и читает по ней){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "\"А вас, сударь, велю...\""

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "{space=400}Подвиньтеся немножко!"

        pososhkov "\"Велю сейчас я выкинуть в окошко!"

        pososhkov "И этот сорванец, и этот глупый франт"

        pososhkov "Подумать смел, что я...\""

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(Любскому){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        pososhkov "{space=400}Вот, батюшка, талант!"

        pososhkov "Вот гений истинный! Смотрите, удивляйтесь!"

        pososhkov "Каков испуг?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(с досадою){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=200}Хорош!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да что же! Восхищайтесь!"

        pososhkov "Взгляните на него! Как истукан стоит!"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "И вы! Брависсимо! Какой смущенный вид!"

        pososhkov "Вот это мимика! - Смотрите, побледнела!"

        pososhkov "Давно ль двух слов сказать порядком не умела?"

        pososhkov "А всё ведь я!.."

        hide pososhkov

        show pososhkov at left
        show velskij at right

        hide pososhkov

        show pososhkov at left
        show velskij at right

        pososhkov "<{i}(Вельскому){/i}>"

        hide velskij

        show pososhkov at truecenter

        hide velskij

        show pososhkov at truecenter

        pososhkov "{space=400}Одно заметить должен вам, -"

        pososhkov "Напрасно вы к ее бросаетесь ногам."

        pososhkov "Оно не худо бы, да слишком театрально."

        pososhkov "Но испугались вы..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show velskij at right

        hide lyubskij

        show lyubskij at left
        show velskij at right

        lyubskij "<{i}(поглядывая на Вельского){/i}>"

        hide velskij

        show lyubskij at truecenter

        hide velskij

        show lyubskij at truecenter

        lyubskij "{space=400}Да! Очень натурально."

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Тихо Оленьке){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Сто раз я говорил, не быть наедине!"

        lyubskij "Негодная!.."

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Громко){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Ступай в гостиную, к жене."

        hide lyubskij

        show olenka at truecenter

        show olenka at truecenter

        "<{i}Оленька уходит.{/i}>"

        hide olenka

        hide olenka

    label Act_2_Scene_11:
        "{b}ЯВЛЕНИЕ 11{/b}"

        show olenka at left
        show izvedov at right

        show olenka at left
        show izvedov at right

        "<{i}Те же, без Оленьки. Изведов, входит из средних дверей.{/i}>"

        hide olenka
        hide izvedov

        hide olenka
        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        lyubskij "<{i}(Изведову){/i}>"

        hide izvedov

        show lyubskij at truecenter

        hide izvedov

        show lyubskij at truecenter

        lyubskij "Ну что? Ты был в саду?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Обегал все дорожки:"

        izvedov "Его там нет."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Вели запречь скорее дрожки"

        lyubskij "И съезди сам к нему."

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        lyubskij "<{i}Изведов уходит и тотчас возвращается.{/i}>"

        hide izvedov

        show lyubskij at truecenter

        hide izvedov

        show lyubskij at truecenter

        lyubskij "{space=400}Бирюлькин наш пропал."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да что с ним сделалось? На пробе он всё спал,"

        pososhkov "Забыл все выходы, раз двадцать ошибался..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Вот я его пугну! Совсем избаловался."

        hide lyubskij

        show lyubskij at left
        show velskij at right

        hide lyubskij

        show lyubskij at left
        show velskij at right

        lyubskij "<{i}(Вельскому){/i}>"

        hide velskij

        show lyubskij at truecenter

        hide velskij

        show lyubskij at truecenter

        lyubskij "А что же твой Андрей Степаныч Прямиков?"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Ушел домой."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Эх, жаль!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Я повторить готов:"

        pososhkov "В нем есть талант, но с ним играть - слуга покорный!"

        pososhkov "Он страшный грубиян и человек превздорный."

        pososhkov "К тому ж, и без него у нас охотник есть:"

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        pososhkov "<{i}(Изведову){/i}>"

        hide izvedov

        show pososhkov at truecenter

        hide izvedov

        show pososhkov at truecenter

        pososhkov "Ты, кажется, взялся?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(кланяясь){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=400}Я чувствую всю честь"

        izvedov "Актером в труппе быть, где важные особы..."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Я думаю, что ты сыграешь и без пробы?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Извольте, я готов."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Смотри, не осрамись."

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Кто? - Я, сударь?"

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да, ты! Не больно, брат, храбрись!"

        lyubskij "Я что-то за тебя ужасно как робею."

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Но ролю выучить я к вечеру поспею."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "И! Как не выучить! Она невелика."

        hide pososhkov

        "<{i}Входит слуга.{/i}>"

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}Слуга"

        hide pervyj_sluga

        show pervyj_sluga at left
        show lyubskij at right

        hide pervyj_sluga

        show pervyj_sluga at left
        show lyubskij at right

        pervyj_sluga "<{i}(подавая Любскому письмо){/i}>"

        hide lyubskij

        show pervyj_sluga at truecenter

        hide lyubskij

        show pervyj_sluga at truecenter

        pervyj_sluga "Письмо, сударь!"

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Подай! - Знакомая рука..."

        lyubskij "Бирюлькин! Что за вздор!.. Как! Что!.. Ах, мой создатель!"

        lyubskij "Возможно ли? - Злодей! Разбойник и предатель!"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Что с вами сделалось?"

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Что сделалось? - Нет сил!"

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        lyubskij "<{i}(Подает письмо Посошкову){/i}>"

        hide pososhkov

        show lyubskij at truecenter

        hide pososhkov

        show lyubskij at truecenter

        lyubskij "Прочти!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(читает){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "\"Милостивый государь и благодетель! Убедись просьбами всех моих знакомых и чувствуя сам, что в мои лета неприлично быть актером, я решился не играть сегодня и возвращаю при сем мою ролю."

        pososhkov "Должные мною тысячу рублей по векселю, с глубочайшей моей благодарностию, завтрешнего числа не премину к вам доставить. - По гроб обязанный вами и всепокорнейший слуга Максим Бирюлькин\"."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Что скажешь, брат?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да кто его подбил?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Весь город - все!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}И, нет! Какой-нибудь проказник"

        pososhkov "Некстати пошутил..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Чтоб наш испортить праздник!"

        lyubskij "И после этого театры затевай!"

        lyubskij "Придумывай, трудись, здоровье убивай,"

        lyubskij "Тешь этих неучей! - Давай пиры и балы!"

        lyubskij "О, варвары! Мордва!.. Чуваши!.. Камчадалы! .."

        lyubskij "Вам хочется самим? - Извольте, господа!"

        lyubskij "Театр мой не пойдет."

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at truecenter

        hide velskij

        show velskij at truecenter

        velskij "<{i}(в сторону){/i}>"

        show velskij at truecenter

        show velskij at truecenter

        velskij "{space=400}Вот новая беда!"

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Неблагодарные!"

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=400}За что ж на всех сердиться?"

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Посмотрим, без меня как станут веселиться!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Поверьте мне - всему виной Кутермина."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Матрена Савишна?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Она сотворена"

        pososhkov "На эти мерзости."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну, так! Она хотела"

        lyubskij "Сгубить меня за то, что я... Да что за дело!.."

        lyubskij "Она иль нет - теперь и сам я не хочу:"

        lyubskij "Велю сломать театр, в деревню ускачу..."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Постойте! Точно так! - Театр мы не отложим."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(с радостию){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Неужели?.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да, да! Мы всё поправить можем,"

        pososhkov "Но меры сильные теперь нам должно брать;"

        pososhkov "Изведов может роль Бирюлькина сыграть -"

        pososhkov "И очень будет мил в Антропкином наряде,"

        pososhkov "А вы попробуйте, - сыграйте ролю дяди."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Кто? Я? - В уме ли ты? С чего ты взял?"

        lyubskij "Да я и смолоду актером не бывал."

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Всему начало есть."

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Попробуйте, начните!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Нет, братец! Ни за что!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Так вы себя вините,"

        pososhkov "Что наш театр нейдет: я средство вам даю."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Я знаю наизусть комедию твою"

        lyubskij "И мог бы, кажется, - мне роль учить не надо..."

        lyubskij "Да нет! - Нельзя никак!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Уж как же будет рада"

        pososhkov "Матрена Савишна! Начнет по всем домам"

        pososhkov "Скакать, рассказывать, шутить - заедет к вам..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ко мне? - Нет, душенька! И носу не покажет."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Куда бы ни взошла - поклон и тотчас скажет:"

        pososhkov "\"Что, матушка, каков вчерась спектакель был?"

        pososhkov "Уж верно, Любский вас отлично угостил,"

        pososhkov "Сбирался целый год, так диво ли?..\""

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Злодейка!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "\"Ведь у него ребром последняя копейка\"."

        pososhkov "- \"Театра не было\". - \"Так что же он кричал?"

        pososhkov "Зачем так чванился? - По выбору всех звал?"

        pososhkov "К чему? - Да он и тем быть должен благодарен,"

        pososhkov "Что ездили к нему! - Ну, что за важный барин?"

        pososhkov "С его ль именьишком мотать?..\""

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ах! Черт возьми!.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "\"Пусть это водится меж знатными людьми,"

        pososhkov "А он-то что?..\""

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Как что!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}\"На дело не похоже!"

        pososhkov "А уж хвастун какой! Хвастун - избави боже!"

        pososhkov "\"Сегодня принимать гостей я не велю -"

        pososhkov "Я так устал! Один весь город веселю,"

        pososhkov "Театры завожу, актеров набираю...\""

        pososhkov "Ан, вот ваш и театр!\""

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Так врет она! - Играю!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Решились наконец! Теперь мы спасены."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Я знаю, мне житья не будет от жены,"

        lyubskij "Да так и быть! Пойдем!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Я думаю, на сцену?"

        pososhkov "Там лучше роль пройти."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}А что же я надену?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Кафтан, большой парик..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да в нем на дурака"

        lyubskij "Я буду походить! - Нельзя ль без парика?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Никак нельзя: таков характер вашей роли."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Хорош же буду я! Куда красив! - В камзоле,"

        lyubskij "В косматом парике... в узорчатых чулках..."

        hide lyubskij

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Зато подумайте! - кто будет в дураках!"

        hide velskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Что этой может быть приятнее награды:"

        pososhkov "Матрена Савишна задохнется с досады!"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Да ништо ей! - А мы поставим на своем."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Так пусть задохнется! - Негодная!.. Пойдем!"

        hide lyubskij

        "<{i}Все уходят.{/i}>"

label Act_6:
    play music "audio/music/106.mp3" fadeout 1.0 fadein 1.0

    scene 78 with fade

    "{b}ДЕЙСТВИЕ ЧЕТВЕРТОЕ{/b}"

    "<{i}Театр представляет комнату позади домашнего театра, на правой и левой стороне двери; прямо небольшая лесенка, приставленная к дверям, которыми входят на сцену; несколько кресел, два стола и большое зеркало.{/i}>"

    menu:
        "{color=#000}ЯВЛЕНИЕ 1{/color}":
            jump Act_3_Scene_1
        "{color=#000}ЯВЛЕНИЕ 2{/color}":
            jump Act_3_Scene_2
        "{color=#000}ЯВЛЕНИЕ 3{/color}":
            jump Act_3_Scene_3
        "{color=#000}ЯВЛЕНИЕ 4{/color}":
            jump Act_3_Scene_4
        "{color=#000}ЯВЛЕНИЕ 5{/color}":
            jump Act_3_Scene_5
        "{color=#000}ЯВЛЕНИЕ 6{/color}":
            jump Act_3_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_3_Scene_6_1

label Further_Act_3_Scene_6_1:
    menu:
        "{color=#000}ЯВЛЕНИЕ 7{/color}":
            jump Act_3_Scene_7
        "{color=#000}ЯВЛЕНИЕ 8{/color}":
            jump Act_3_Scene_8
        "{color=#000}ЯВЛЕНИЕ 9{/color}":
            jump Act_3_Scene_9
        "{color=#000}ЯВЛЕНИЕ 10{/color}":
            jump Act_3_Scene_10
        "{color=#000}ЯВЛЕНИЕ 11{/color}":
            jump Act_3_Scene_11
        "{color=#000}ЯВЛЕНИЕ 12{/color}":
            jump Act_3_Scene_12

    label Act_3_Scene_1:
        "{b}ЯВЛЕНИЕ 1{/b}"

        show lyubskij at left
        show pososhkov at right

        show lyubskij at left
        show pososhkov at right

        "<{i}Любский сидит, Посошков расписывает ему лицо, парикмахер держит парик; слуга.{/i}>"

        hide lyubskij
        hide pososhkov

        hide lyubskij
        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(одному слуге){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "По окнам шкалики, а плошки на крыльцо."

        lyubskij "Ступай!"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}Слуга уходит.{/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Эх, полно, брат! Испачкал всё лицо."

        lyubskij "Да будет ли конец?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Еще одну морщину;"

        pososhkov "Ведь вы играете не средних лет мужчину,"

        pososhkov "Вам должно походить лицом на старика."

        pososhkov "Взгляните на меня! - Да, левая щека"

        pososhkov "Бледней, а вот сейчас мы разом подрумяним."

        pososhkov "Сидите же смирней! Вот так! - Теперь мы станем"

        pososhkov "Прилаживать парик! - Подай!"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(Берет парик и надевает на Любского.){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну что, надел?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Постойте! надобно, чтоб ловко он сидел."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ай! Волосы дерешь! Терпения не стало!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Мне кажется, парик напудрен очень мало."

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Парикмахеру){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Вот с этой стороны!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да полно! Не тирань!"

        lyubskij "Пусти меня!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Сейчас!"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}Парикмахер пудрит Любского.{/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(вспрыгивает с кресел){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Довольно! - Перестань!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(парикмахеру){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Пошли Изведова."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(смотрясь в зеркало){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Ну, так! Урод уродом!"

        lyubskij "И кто мог следовать таким дурацким модам?"

        lyubskij "Какой нечистый дух придумал парики!"

        lyubskij "Да ништо мне! Пошел охотой в дураки..."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "А мне так кажется, что в этом вы наряде..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да, батюшка, красив! - И спереди и сзади"

        lyubskij "Святочный пугало."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Охота вам терзать"

        pososhkov "Самих себя..."

        hide pososhkov

    label Act_3_Scene_2:
        "{b}ЯВЛЕНИЕ 2{/b}"

        show izvedov at truecenter

        show izvedov at truecenter

        "<{i}Те же и Изведов, из средних дверей.{/i}>"

        hide izvedov

        hide izvedov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at left
        show pososhkov at right

        hide izvedov

        show izvedov at left
        show pososhkov at right

        izvedov "<{i}(Посошкову){/i}>"

        hide pososhkov

        show izvedov at truecenter

        hide pososhkov

        show izvedov at truecenter

        izvedov "{space=400}Что вам угодно приказать?"

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Готово ль у тебя?"

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}На сцене всё готово."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "А что, который час?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Три четверти седьмого."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Что ж Оленька нейдет?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Я к ней сейчас послал."

        pososhkov "А Вельский где? И он опаздывать уж стал."

        pososhkov "Я прежде не знавал за ним привычки этой."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Он из дому хотел совсем уже одетый"

        izvedov "Приехать в шесть часов."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Нельзя ж ему забыть,"

        pososhkov "Что ровно в семь часов на сцене должно быть."

        hide pososhkov

        "<{i}Входит слуга.{/i}>"

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну, что ты?"

        hide lyubskij

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}Слуга"

        pervyj_sluga "{space=400}Доложить, что начали съезжаться."

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ух! Сердце замерло! - Хоть вовсе отказаться."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Помилуйте!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да я наверно осрамлюсь,"

        lyubskij "Я знаю наперед; лишь только появлюсь,"

        lyubskij "Все лопнут со смеху."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ах, как вы малодушны!"

        pososhkov "Не стыдно ли?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Боюсь!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да будьте же послушны"

        pososhkov "Рассудку вашему. Чего бояться вам?"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Слуге){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Ступай! Проси сюда скорее наших дам."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Эй, братец, быть беде! - Недаром лихорадка"

        lyubskij "Меня трясет."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Да вы сыграете..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Прегадко!"

        lyubskij "Я ж в этом парике на чучелу похож..."

        lyubskij "Ах, батюшки мои! То бросит в жар, то в дрожь!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Неужели на вас не действуют примеры?"

        pososhkov "Ну вот, боюсь ли я?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Не выпить ли мадеры?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Помилуйте! Зачем? - Чтоб ролю позабыть?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Хоть рюмочку одну."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Нет, нет!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да как же быть?"

        lyubskij "Смотри, я весь дрожу."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Вам это не поможет."

        pososhkov "И что, скажите мне, так сильно вас тревожит?"

        pososhkov "Вы знаете, у нас партер неприхотлив,"

        pososhkov "Сыграйте как-нибудь!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ты видишь, я чуть жив."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Добро, останьтесь здесь, а я пойду на сцену."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Нет, вечно не прощу Бирюлькину измену!"

        lyubskij "По милости его теперь я в западне."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Когда сберутся все, махните только мне,"

        pososhkov "И я начать велю тотчас же увертюру."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(смотрясь в зеркало){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "И эту глупую, несчастную фигуру"

        lyubskij "Я должен выставить сегодня напоказ!"

        lyubskij "Добро б я был талант!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Таланта много в вас."

        pososhkov "Хотя заметна в нем какая-то незрелость,"

        pososhkov "Но это ничего: вы знаете, что смелость"

        pososhkov "Берет и города. - Смелей, сударь, смелей!"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Уходит на сцену.){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        hide pososhkov

    label Act_3_Scene_3:
        "{b}ЯВЛЕНИЕ 3{/b}"

        "<{i}Те же, без Посошкова.{/i}>"

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да, да! Толкуй! - А всё по милости твоей."

        lyubskij "Нет, душенька! Вперед театра не затеешь!"

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        lyubskij "<{i}(Изведову){/i}>"

        hide izvedov

        show lyubskij at truecenter

        hide izvedov

        show lyubskij at truecenter

        lyubskij "Признайся, брат! И ты немножечко робеешь?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Кто! - Я-с?"

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Чай, скажешь, нет?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Так это в первый раз."

        izvedov "Помилуйте! Ну, что за публика у вас?"

        izvedov "Кого робеть? - Друзья, приятели, старушки,"

        izvedov "Полдюжины детей. Да это что? Игрушки!"

        izvedov "И роля-то моя всего странички две."

        izvedov "Нет, сударь! В старину, как я играл в Москве,"

        izvedov "Так есть чего робеть: не мало и не много"

        izvedov "Три тысячи персон. А судят-то как строго!"

        izvedov "Уж милости от них не жди и не проси:"

        izvedov "Как шикать примутся, так боже упаси!"

        izvedov "Беда! - Не так, как здесь: там публика не наша,"

        izvedov "Соврать не смей!"

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}А вот идет сюда Наташа."

        hide lyubskij

    label Act_3_Scene_4:
        "{b}ЯВЛЕНИЕ 4{/b}"

        play sound1 running

        show natasha at truecenter

        play sound1 running

        show natasha at truecenter

        "<{i}Те же и Наташа, входит с левой стороны и бежит на сцену.{/i}>"

        hide natasha

        stop sound1

        hide natasha

        stop sound1

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at left
        show lyubskij at right

        hide natasha

        show natasha at left
        show lyubskij at right

        natasha "<{i}(не видя Любского){/i}>"

        hide lyubskij

        show natasha at truecenter

        hide lyubskij

        show natasha at truecenter

        natasha "Где Федор Львович? - Где?"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Куда бежишь? Куда?"

        lyubskij "Я здесь."

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=200}Ах, боже мой!"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Что сделалось?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Беда!"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ахти! - Спектакель наш нейдет?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Ах, сударь! Хуже!"

        natasha "Ведь Ольга Дмитревна..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Племянница? - Да ну же!"

        lyubskij "Злодейка, говори!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=200}Она..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Я жду всего!.."

        lyubskij "С ней дурно сделалось?.."

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Ох! Это б ничего,"

        natasha "А то как вздумаю... Какое приключенье!"

        natasha "Какой удар!"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну вот, прошу иметь терпенье!"

        lyubskij "Негодная! - Да что?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=200}Она..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Занемогла?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Нет, хуже..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Что за вздор?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Она, сударь... Ушла!"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ушла?.. Куда?.. Зачем?.. Не может это статься!"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at left
        show natasha at right

        hide izvedov

        show izvedov at left
        show natasha at right

        izvedov "<{i}(тихо Наташе){/i}>"

        hide natasha

        show izvedov at truecenter

        hide natasha

        show izvedov at truecenter

        izvedov "Так барышня твоя."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(так же){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        natasha "{space=400}Уехала венчаться."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ушла?.. Нет, нет! - Ты врешь!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Я всё вам расскажу."

        natasha "Вот с час тому назад в уборной я сижу,"

        natasha "И барышня со мной, совсем уже одета;"

        natasha "Вдруг к заднему крыльцу подъехала карета..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну, ну!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Дверь скрипнула - и кто-то на крыльцо"

        natasha "Тихонечко взошел; глядь барышне в лицо -"

        natasha "Она - как смерть!"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Ну, ну!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Заплакала, вскочила,"

        natasha "Накинула платок и в дверь..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}А ты пустила?.."

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Эх, сударь! Слушайте!"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Ну, ну!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Я вслед за ней."

        natasha "Выходим на крыльцо; гляжу - в сенях лакей,"

        natasha "Он под руку ее, тут барышня взглянула"

        natasha "Так жалко на меня, платочком мне махнула,"

        natasha "В карету прыг! И след простыл..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}А ты? - Ну, ну!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Не вспомнилась."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И ты не кликнула жену,"

        lyubskij "Людей, весь дом?.."

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Без чувств я целый час лежала,"

        natasha "А после, кажется - да, точно так -кричала."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Злодей-то кто?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Да как увидеть в темноте?"

        natasha "Помилуйте!"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ты врешь! - Нет, душенька! Не те"

        lyubskij "Уловки у тебя! Ты знала шашни эти!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Кто? - Я-с?"

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Да, ты! - Сейчас скажи, кто был в карете?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Сказать наверное не смею я никак,"

        natasha "А Вельский, кажется..."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ах, старый я дурак!"

        lyubskij "Так точно! Это он."

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Я, впрочем, не ручаюсь."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Молчи, негодная! Чего ж я дожидаюсь?"

        lyubskij "Пошлю! - Пойду! - Куда? - Я вовсе без ума."

        hide lyubskij

        show lyubskij at left
        show natasha at right

        hide lyubskij

        show lyubskij at left
        show natasha at right

        lyubskij "<{i}(Наташе){/i}>"

        hide natasha

        show lyubskij at truecenter

        hide natasha

        show lyubskij at truecenter

        lyubskij "Пошли жену!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Да вот она идет сама."

        hide natasha

    label Act_3_Scene_5:
        "{b}ЯВЛЕНИЕ 5{/b}"

        show lyubskaya at truecenter

        show lyubskaya at truecenter

        "<{i}Те же и Любская.{/i}>"

        hide lyubskaya

        hide lyubskaya

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Ах я несчастная! - Ну, сгибла да пропала!"

        lyubskaya "Вот грех какой!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ага! Теперь ты плакать стала!"

        lyubskij "Безумная!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Кричи,сударик мой, кричи!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Чего смотрела ты?"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=200}А ты, сударь?"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Молчи!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Чтоб стала я молчать! - Нет, батюшка, довольно!"

        lyubskaya "Век целый поступать ты хочешь своевольно,"

        lyubskaya "А я должна..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Жена!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Так нет, не замолчу!"

        lyubskaya "Терпеть не буду я, не стану, не хочу!"

        lyubskaya "Всё выскажу..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Жена!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Ну вот твои затеи,"

        lyubskaya "Вот глупый твой театр! Актеры все - злодеи,"

        lyubskaya "Губители твои, и даже Посошков."

        lyubskaya "Кого ты набрал в дом? - Фигляров, дураков,"

        lyubskaya "Срамил себя, мотал, расстроил всё именье."

        lyubskaya "Что праздники твои? - Беспутство, разоренье!"

        lyubskaya "А твой театр..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Жена!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Разбойничий вертеп!"

        lyubskaya "Скажи мне, батюшка, иль вовсе ты ослеп?"

        lyubskaya "Бывало, при тебе шушуканье, бесстыдство,"

        lyubskaya "Одно лишь на уме: амуры, волокитство, -"

        lyubskaya "И с кем? - С племянницей! Что ж вышло наконец"

        lyubskaya "Она из-за кулис бежала под венец."

        lyubskaya "Не я ль сто раз одно и то же говорила..."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ты только об одном, сударыня, вопила,"

        lyubskij "Что деньги трачу я..."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}А кто твердил о том,"

        lyubskaya "Что должно запереть от Вельского наш дом"

        lyubskaya "И выдать поскорей племянницу-злодейку!"

        lyubskaya "Да я бы отдала последнюю копейку,"

        lyubskaya "Лишь только б этот срам поправить чем-нибудь,"

        lyubskaya "Лишь только б этот грех... Нет сил!.. - Стеснило грудь!.."

        play sound1 punch

        hide lyubskaya

        show lyubskaya at truecenter

        play sound1 punch

        hide lyubskaya

        show lyubskaya at truecenter

        lyubskaya "<{i}(Падает на кресла.){/i}>"

        show lyubskaya at truecenter

        stop sound1

        show lyubskaya at truecenter

        stop sound1

        hide lyubskaya

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Пойдемте к вам..."

        hide natasha

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Нет, нет!.. - Пускай умру при муже!"

        lyubskaya "Ах, душно!.. - Смерть моя!.."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Час от часу всё хуже!"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at truecenter

        hide natasha

        show natasha at truecenter

        natasha "<{i}(ищет в карманах){/i}>"

        show natasha at truecenter

        show natasha at truecenter

        natasha "Куда девался спирт?"

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(подавая бутылку со стола){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=400}Вот здесь ло-де-лаван."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Подай сюда!"

        hide natasha

        show natasha at left
        show lyubskaya at right

        hide natasha

        show natasha at left
        show lyubskaya at right

        natasha "<{i}(Льет Любской на голову и трет виски.){/i}>"

        hide lyubskaya

        show natasha at truecenter

        hide lyubskaya

        show natasha at truecenter

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(кричит){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Воды! Скорей воды стакан!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        hide lyubskaya

        show lyubskaya at truecenter

        hide lyubskaya

        show lyubskaya at truecenter

        lyubskaya "<{i}(хватает себя за голову и вскакивает){/i}>"

        show lyubskaya at truecenter

        show lyubskaya at truecenter

        lyubskaya "Ах, боже мой! - Ты век останешься скотиной!"

        lyubskaya "Ну что ты, дура, льешь? - Бутылка два с полтиной."

        lyubskaya "Подай!"

        hide lyubskaya

        show lyubskaya at truecenter

        hide lyubskaya

        show lyubskaya at truecenter

        lyubskaya "<{i}(Берет бутылку и прячет в ридикюль.){/i}>"

        show lyubskaya at truecenter

        show lyubskaya at truecenter

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(глядит в окно){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Смотрите-ка! Полнехонек весь двор!"

        lyubskij "Карет до двадцати!"

        hide lyubskij

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}1-й слуга"

        pervyj_sluga "{space=400}Приехал прокурор!"

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        pervyj_sluga "<{i}(Уходит.){/i}>"

        show pervyj_sluga at truecenter

        show pervyj_sluga at truecenter

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Зачем я звал его! - Ведь он московский житель,"

        lyubskij "Насмешник, зубоскал!"

        hide lyubskij

        show vtoroj_sluga at truecenter

        $ vtoroj_sluga_var = "{noalt}2-й слуга"

        vtoroj_sluga "{space=400}Губернский предводитель."

        hide vtoroj_sluga

        show vtoroj_sluga at truecenter

        hide vtoroj_sluga

        show vtoroj_sluga at truecenter

        vtoroj_sluga "<{i}(Уходит.){/i}>"

        show vtoroj_sluga at truecenter

        show vtoroj_sluga at truecenter

        hide vtoroj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "И, верно, не один, с невесткой и женой!"

        lyubskij "Съезжайтесь, господа! Потешьтесь надо мной!"

        hide lyubskij

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}1-й слуга"

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        pervyj_sluga "<{i}(вбегает запыхавшись){/i}>"

        show pervyj_sluga at truecenter

        show pervyj_sluga at truecenter

        pervyj_sluga "Его сиятельство!.."

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Гражданский губернатор?"

        hide lyubskij

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}1-й слуга"

        pervyj_sluga "И с ним приезжий князь."

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        pervyj_sluga "<{i}(Уходит.){/i}>"

        show pervyj_sluga at truecenter

        show pervyj_sluga at truecenter

        hide pervyj_sluga

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Возможно ли! - Сенатор!"

        lyubskij "Зачем?"

        hide lyubskij

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Его Авдей Михайлыч пригласил."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Негодный Посошков! - И кто его просил!"

        lyubskij "Подай его!"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(подходит к средним дверям и кричит){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=400}Авдей Михайлович! - Два слова!"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        hide natasha

        show natasha at left
        show lyubskij at right

        hide natasha

        show natasha at left
        show lyubskij at right

        natasha "<{i}(Любскому){/i}>"

        hide lyubskij

        show natasha at truecenter

        hide lyubskij

        show natasha at truecenter

        natasha "Он сделать вам сюрприз хотел."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(показываясь в дверях){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Что? - Всё готово?"

        pososhkov "Сейчас!"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Уходит.){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Постой! Постой! Куда бежишь? Зачем?"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}За кулисами начинают играть увертюру.{/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Что слышу! Музыка!.. Прирезали совсем!.."

        lyubskij "Всё кончено!.. - Погиб!.. - Куда себя я дену? .."

        lyubskij "Где спрятаться?.."

        hide lyubskij

    label Act_3_Scene_6:
        "{b}ЯВЛЕНИЕ 6{/b}"

        show pososhkov at truecenter

        show pososhkov at truecenter

        "<{i}Те же и Посошков, сходит поспешно вниз.{/i}>"

        hide pososhkov

        hide pososhkov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ну, что нейдете вы на сцену?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Идти?.. Куда идти?.. На что?.. Зачем?.. К чему?.."

        lyubskij "Ну! Что молчишь?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Играть пора."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Играть?.. Кому?"

        lyubskij "Играй, голубчик мой!.. - Играй! И точно кстати!"

        lyubskij "Не хочешь ли один попрыгать на канате?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Что с вами сделалось?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Со мною?.. Ничего!.."

        lyubskij "Я здесь... а Вельский где?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Неужто нет его?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "А где племянница?.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Как где?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Я жду ответа."

        lyubskij "Ну, что же? Говори!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Она была одета... -"

        pososhkov "Я это видел сам."

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}И даже прежде всех."

        hide natasha

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Что с нею сделаться могло?"

        hide pososhkov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Такой-то грех,"

        lyubskaya "Что вымолвить нельзя!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ступай к своей невесте!"

        lyubskij "Ступай! Ищи ее!.. Она и Вельский вместе."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Как вместе? Где? - Так что ж! Зовите их сюда."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Так знай! - Племянница ушла."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Ушла?.. - Куда?"

        pososhkov "Возможно ль! - Как ушла?"

        hide pososhkov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "{space=400}Да так, как все уходят."

        hide natasha

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Что, видишь ли теперь? - Вот роли как проходят!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Уйти, когда гостей полнехонек весь двор!"

        hide pososhkov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Когда назначены помолвка и сговор!"

        hide lyubskaya

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Как будто б убежать и завтра не успела!"

        pososhkov "Ах, боже мой!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Тебе, голубчик мой, за дело!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да я чем виноват?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Кто в петлю-то втащил"

        lyubskij "Себя, меня, всех нас - зарезал, погубил?"

        lyubskij "Злодей! - Не ты ль завел все эти представлень"

        lyubskij "По милости твоей в каком мы положеньи!"

        lyubskij "Что делать нам?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Театр вам должно отказать."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Но как и для чего?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Вы можете сказать,"

        pososhkov "Что Оленька больна."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}И все единогласно"

        lyubskij "Начнут кричать..."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}К чему убытчиться напрасно!"

        lyubskaya "Отказывай скорей!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Эх, матушка! Молчи!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        hide lyubskaya

        show lyubskaya at left
        show izvedov at right

        hide lyubskaya

        show lyubskaya at left
        show izvedov at right

        lyubskaya "<{i}(Изведову){/i}>"

        hide izvedov

        show lyubskaya at truecenter

        hide izvedov

        show lyubskaya at truecenter

        lyubskaya "Ступай, вели гасить все лампы и свечи!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Зачем, сударыня! - Всё думаешь о вздоре!"

        hide lyubskij

    label Act_3_Scene_7:
        "{b}ЯВЛЕНИЕ 7{/b}"

        show chestonov at truecenter

        show chestonov at truecenter

        "<{i}Те же и Честонов.{/i}>"

        hide chestonov

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(идя к нему навстречу){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "Ты здесь? Поди сюда! - Ты слышал наше горе"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Какое горе?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Как! Не знаешь ничего?"

        lyubskij "Ведь Оленька..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}Ушла."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ты слышал? От кого?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Я видел их."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ага, голубчики! Попались!"

        lyubskij "Ну, где ж они?.. - Пойдем!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Они при мне венчались."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Возможно ли! Они венчались при тебе?.."

        lyubskij "И ты?.."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Послушай, брат! Противиться судьбе"

        chestonov "Не должно и нельзя."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Эге, сударь! Так, стало,"

        lyubskij "Вы были заодно?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Сердиться пользы мало:"

        chestonov "Они обвенчаны. - Что думать, брат, решись!"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Простить племянницу?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Да полно, не сердись!"

        chestonov "Что сделано, того поправить невозможно."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Чтоб я простил ее! - Она, сударь, безбожно,"

        lyubskij "Злодейским образом зарезала меня."

        lyubskij "Представь себе, пойдет какая болтовня:"

        lyubskij "Прибавки, выдумки, расспросы, пересуды!"

        lyubskij "И завтра же ко мне приятели - Иуды"

        lyubskij "Нагрянут все! А что мне будет от старух!"

        lyubskij "Начнут терзать меня - не шепотом, а вслух,"

        lyubskij "Читать мораль, бранить, ругать, давать советы;"

        lyubskij "Засудят, заказнят... а здешние газеты..."

        lyubskij "Матрена Савишна!.. Нет! Вечно не прощу!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Но выслушай!.."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Нет, нет!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Пожалуй, замолчу."

        chestonov "А жаль! Они теперь сыграли б превосходно."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Что, что?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Так, братец, вздор!.. - Вам это не угодно..."

        chestonov "Так что ж и говорить."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ты холоден как лед,"

        lyubskij "Тогда как я - твой брат..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Спектакель ваш пойдет,"

        chestonov "И даже не с тобой, мой друг! С другим актером."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Неужели пойдет?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Но только с уговором:"

        chestonov "Прости племянницу."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Нет, братец! Ни за что!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "О, если так!.. - Прощай!"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(Хочет идти.){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Постой!.. - Да я не то"

        lyubskij "Хотел сказать... Злодей! Как он меня терзает!"

        lyubskij "Добро! Уж так и быть... пускай она играет."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Так ты прощаешь их? - Ну, милый! Очень рад!"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да, да!.. - Я... завтра их прощу."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Нет, шутишь, брат!"

        chestonov "Теперь иль никогда."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Так вздор! Я не намерен..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "О, если так..."

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(Хочет идти.){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Постой! Да точно ль ты уверен,"

        lyubskij "Что наш театр..."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}Пойдет."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Кто ж выкупит меня?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Найдем кого-нибудь."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Кого? - Моя родня,"

        lyubskij "Приятели, весь свет составлен из злодеев."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "А прежний друг - Сергей Иванович Лилеев?"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Возможно ли?"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Я с ним об этом говорил."

        chestonov "Вы с ним поссорились, но я вас помирил."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да точно ли?.."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Уж я за это отвечаю."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну! Делать нечего!.. - Изволь, мой друг!.. прощаю!"

        lyubskij "Давай же их скорей."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}А я так не прощу."

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Вот выскочка! - Когда уж я простить хочу,"

        lyubskij "Так кстати ли тебе!.."

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Сестра! Побойся бога!"

        chestonov "Ведь ты их уморишь!"

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Туда им и дорога!"

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Жена!"

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Ну слыхано ль! Невесте уходить!.."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "А что б вам стоило их свадьбу снарядить?"

        chestonov "Скромненько обвенчать нельзя - не те уж годы."

        chestonov "Какие бы тогда пошли у вас расходы?"

        chestonov "На мелочи, на вздор последний рубль отдашь:"

        chestonov "Подумай-ка, сочти! - Нарядный экипаж,"

        chestonov "Четверка вороных, богатые ливреи,"

        chestonov "Кафтаны кучерам и прочие затеи,"

        chestonov "Которым нет конца..."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Так, батюшка! Ты прав!"

        lyubskaya "Беда!"

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Вот то-то же! Ты знаешь братнин нрав:"

        chestonov "Что вышло б у него на разные предметы?"

        chestonov "Чего бы стоили сюрпризы и конфекты,"

        chestonov "Один вечерний стол, десерт, питье, еда,"

        chestonov "Шампанское вино..."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}Ох, подлинно беда!"

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Вот то-то же! - А там визиты, посещенья,"

        chestonov "Обеды, вечера, театры, угощенья..."

        chestonov "Да боже сохрани! Он сряду б целый год"

        chestonov "Пиры давал."

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=200}Так, так!"

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Теперь же без хлопот:"

        chestonov "Они обвенчаны без всякого парада."

        chestonov "Эх, матушка, прости! - Приданого не надо!"

        hide chestonov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Пришлось простить."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Так дело и с концом!"

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "А я-то, сударь, что?"

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Вы были женихом..."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "И точно был любим."

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Не Оленькой, а братом."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Да что же я теперь?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Остался, брат, за штатом."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Так я же не один останусь в дураках."

        hide pososhkov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "Что, что еще?"

        hide lyubskaya

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Теперь вы все в моих руках:"

        pososhkov "Театр ваш не пойдет."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ну, так! - Недоставало,"

        lyubskij "Чтоб он еще!.. Злодей! - Бессовестный! Так стало..."

        lyubskij "Да нет! - Ты шутишь, брат!.."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Поверьте, не шучу."

        pososhkov "Играть не буду я."

        hide pososhkov

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=200}Не хочешь?"

        hide lyubskaya

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Не хочу."

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at left
        show pososhkov at right

        hide chestonov

        show chestonov at left
        show pososhkov at right

        chestonov "<{i}(Посошкову){/i}>"

        hide pososhkov

        show chestonov at truecenter

        hide pososhkov

        show chestonov at truecenter

        chestonov "Авдей Михайлович! - Мы все молчим покуда,"

        chestonov "А как рассердимся, так не было б вам худо:"

        chestonov "Сыграют и без вас."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(в сторону){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Не хочет ли уж он..."

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Нам стоит выкинуть всю ролю вашу вон."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Но как?.."

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Помилуйте! - Да это сплошь бывает."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Неужели?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Один лишь автор пострадает,"

        izvedov "А мы свое возьмем."

        hide izvedov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Но автор-то ведь я!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Твоя комедия и так галиматья:"

        lyubskij "Так всё равно!"

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        lyubskij "<{i}(Изведову){/i}>"

        hide izvedov

        show lyubskij at truecenter

        hide izvedov

        show lyubskij at truecenter

        lyubskij "{space=200}Марай!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Но я вам не позволю..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Да! Стану я смотреть!"

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        hide lyubskij

        show lyubskij at left
        show izvedov at right

        lyubskij "<{i}(Изведову){/i}>"

        hide izvedov

        show lyubskij at truecenter

        hide izvedov

        show lyubskij at truecenter

        lyubskij "{space=400}Вымарывай всю ролю!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Помилуйте!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Ступай!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(подавая карандаш){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "{space=400}А вот и карандаш."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Как можно выкинуть главнейший персонаж?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "А вот увидишь как!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Совсем не будет связи!.."

        pososhkov "За что ж срамить меня при публике, при князе?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Всё это, душенька, зависит от тебя -"

        lyubskij "Играй!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at left
        show pososhkov at right

        hide chestonov

        show chestonov at left
        show pososhkov at right

        chestonov "<{i}(Посошкову){/i}>"

        hide pososhkov

        show chestonov at truecenter

        hide pososhkov

        show chestonov at truecenter

        chestonov "{space=400}Послушайте! Вас искренно любя,"

        chestonov "Я должен вам сказать, что это представленье..."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Убьет комедию!.."

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Без всякого сомненья."

        chestonov "Вы знаете: кому охота разбирать,"

        chestonov "Кто прав, кто виноват..."

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        hide lyubskij

        show lyubskij at left
        show pososhkov at right

        lyubskij "<{i}(Посошкову){/i}>"

        hide pososhkov

        show lyubskij at truecenter

        hide pososhkov

        show lyubskij at truecenter

        lyubskij "{space=200}Ну, что?"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Пришлось играть."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Вот так-то лучше, брат!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Но будьте справедливы:"

        pososhkov "Легко ли мне сносить! - Они теперь счастливы,"

        pososhkov "А я..."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}А ты кричал: \"Им надо роль пройти!"

        lyubskij "Не троньте их!..\""

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(в боковые двери){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "{space=400}Теперь вы можете взойти."

        hide chestonov

    label Act_3_Scene_8:
        "{b}ЯВЛЕНИЕ 8{/b}"

        show velskij at left
        show olenka at truecenter
        show lileev at right

        show velskij at left
        show olenka at truecenter
        show lileev at right

        "<{i}Те же, Вельский, Оленька и Лилеев, в костюме.{/i}>"

        hide velskij
        hide olenka
        hide lileev

        hide velskij
        hide olenka
        hide lileev

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        olenka "Ах, дядюшка!"

        hide olenka

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(Оленьке){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "{space=400}Смелей! Всё кончилось прощеньем."

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        hide velskij

        show velskij at left
        show lyubskij at right

        hide velskij

        show velskij at left
        show lyubskij at right

        velskij "<{i}(Любскому){/i}>"

        hide lyubskij

        show velskij at truecenter

        hide lyubskij

        show velskij at truecenter

        velskij "Одна любовь моя мне служит извиненьем..."

        hide velskij

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Добро! Уж так и быть."

        hide lyubskij

        show lyubskaya at truecenter

        $ lyubskaya_var = "{noalt}Любская"

        lyubskaya "{space=400}И я прощаю вас."

        hide lyubskaya

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at left
        show lyubskij at truecenter
        show lileev at right

        hide chestonov

        show chestonov at left
        show lyubskij at truecenter
        show lileev at right

        chestonov "<{i}(подводя к Любскому Лилеева){/i}>"

        hide lyubskij
        hide lileev

        show chestonov at truecenter

        hide lyubskij
        hide lileev

        show chestonov at truecenter

        chestonov "А вот вам и актер!"

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at left
        show lileev at right

        hide lyubskij

        show lyubskij at left
        show lileev at right

        lyubskij "<{i}(Лилееву){/i}>"

        hide lileev

        show lyubskij at truecenter

        hide lileev

        show lyubskij at truecenter

        lyubskij "{space=400}Наделал ты проказ!"

        lyubskij "Не стыдно ли тебе?"

        hide lyubskij

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Забудемте об этом!"

        hide lileev

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Ему не надобно сидеть за туалетом:"

        chestonov "Как видишь, он готов."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        hide pososhkov

        show pososhkov at left
        show izvedov at right

        pososhkov "<{i}(Изведову){/i}>"

        hide izvedov

        show pososhkov at truecenter

        hide izvedov

        show pososhkov at truecenter

        pososhkov "{space=400}Совсем не стариком"

        pososhkov "Одет."

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Так я могу расстаться с париком!"

        lyubskij "Долой его!"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Сбрасывает парик.){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Теперь играйте как хотите!"

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(Оленьке){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "Ну, Ольга Дмитревна!.."

        hide pososhkov

        show olenka at truecenter

        $ olenka_var = "{noalt}Оленька"

        hide olenka

        show olenka at truecenter

        hide olenka

        show olenka at truecenter

        olenka "<{i}(приседая){/i}>"

        show olenka at truecenter

        show olenka at truecenter

        olenka "{space=400}Что ж делать! Извините!"

        hide olenka

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(жене){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "А ты, сударыня, ступай теперь к гостям."

        hide lyubskij

        show lyubskaya at truecenter

        show lyubskaya at truecenter

        "<{i}Любская уходит.{/i}>"

        hide lyubskaya

        hide lyubskaya

    label Act_3_Scene_9:
        "{b}ЯВЛЕНИЕ 9{/b}"

        show lyubskaya at truecenter

        show lyubskaya at truecenter

        "<{i}Те же, без Любской.{/i}>"

        hide lyubskaya

        hide lyubskaya

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Ну что же, господа!"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at left
        show natasha at right

        hide izvedov

        show izvedov at left
        show natasha at right

        izvedov "<{i}(подводя Наташу){/i}>"

        hide natasha

        show izvedov at truecenter

        hide natasha

        show izvedov at truecenter

        izvedov "{space=400}Позвольте уж и нам..."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "На всех пошло! И вы жениться захотели?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Когда позволите, на будущей неделе..."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Хоть завтра поутру, лишь только не теперь."

        lyubskij "Гей, малый! Кто-нибудь!"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}Входит слуга.{/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        lyubskij "{space=400}Смотри, чтоб в эту дверь"

        lyubskij "Никто не проходил."

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Показывает направо.){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show velskij at truecenter
        show olenka at right

        hide pososhkov

        show pososhkov at left
        show velskij at truecenter
        show olenka at right

        pososhkov "<{i}(Вельскому и Оленьке){/i}>"

        hide velskij
        hide olenka

        show pososhkov at truecenter

        hide velskij
        hide olenka

        show pososhkov at truecenter

        pososhkov "{space=400}Подите, подрумяньтесь:"

        pososhkov "Вам так играть нельзя."

        hide pososhkov

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        hide izvedov

        show izvedov at truecenter

        hide izvedov

        show izvedov at truecenter

        izvedov "<{i}(отворяя дверь налево){/i}>"

        show izvedov at truecenter

        show izvedov at truecenter

        izvedov "{space=200}Пожалуйте!"

        hide izvedov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        hide lileev

        show lileev at left
        show izvedov at right

        hide lileev

        show lileev at left
        show izvedov at right

        lileev "<{i}(Изведову){/i}>"

        hide izvedov

        show lileev at truecenter

        hide izvedov

        show lileev at truecenter

        lileev "{space=400}Останьтесь!"

        lileev "Я это сделаю."

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(с насмешкою){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}И, верно, лучше всех,"

        pososhkov "Кто опытен, как вы..."

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Что значит этот смех?"

        hide lileev

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Эх, полноте!"

        hide lyubskij

        show lyubskij at left
        show lileev at right

        hide lyubskij

        show lyubskij at left
        show lileev at right

        lyubskij "<{i}(Лилееву){/i}>"

        hide lileev

        show lyubskij at truecenter

        hide lileev

        show lyubskij at truecenter

        lyubskij "{space=200}Ступай!"

        hide lyubskij

        show velskij at left
        show lileev at truecenter
        show olenka at right

        show velskij at left
        show lileev at truecenter
        show olenka at right

        "<{i}Вельский, Лилеев и Оленька уходят налево.{/i}>"

        hide velskij
        hide lileev
        hide olenka

        hide velskij
        hide lileev
        hide olenka

    label Act_3_Scene_10:
        "{b}ЯВЛЕНИЕ 10{/b}"

        show olenka at left
        show velskij at truecenter
        show volgin at right

        show olenka at left
        show velskij at truecenter
        show volgin at right

        "<{i}Те же, без Лилеева, Оленьки и Вельского; а вскоре Волгин.{/i}>"

        hide lileev
        hide olenka
        hide velskij
        hide volgin

        hide lileev
        hide olenka
        hide velskij
        hide volgin

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=200}Он сердится."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Вот то-то!"

        lyubskij "К чему шутить! И что за смертная охота"

        lyubskij "Дразнить Лилеева!"

        hide lyubskij

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(за кулисами с правой стороны){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Прошу же не толкать!"

        hide volgin

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}Слуга"

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        hide pervyj_sluga

        show pervyj_sluga at truecenter

        pervyj_sluga "<{i}(за кулисами){/i}>"

        show pervyj_sluga at truecenter

        show pervyj_sluga at truecenter

        pervyj_sluga "Нельзя, сударь!"

        hide pervyj_sluga

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(врываясь насильно){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=200}Пусти!"

        hide volgin

        show pervyj_sluga at truecenter

        $ pervyj_sluga_var = "{noalt}Слуга"

        pervyj_sluga "{space=400}Не велено пускать!"

        hide pervyj_sluga

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Возможно ль! - Прямиков!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Как? Этот заседатель,"

        lyubskij "Что к нам в актеры-то хотел?"

        hide lyubskij

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at left
        show chestonov at right

        hide volgin

        show volgin at left
        show chestonov at right

        volgin "<{i}(Честонову){/i}>"

        hide chestonov

        show volgin at truecenter

        hide chestonov

        show volgin at truecenter

        volgin "{space=400}Ага, приятель!"

        volgin "Ты спрятался!.. - Да вздор! Тебя везде найдут."

        volgin "Скажи-ка мне..."

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(Увидя Посошкова){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Ахти! Опять проклятый шут!"

        volgin "И, кажется, хмелен..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Да что ж он в самом деле!"

        pososhkov "Вот я его!"

        hide pososhkov

        show pososhkov at left
        show volgin at right

        hide pososhkov

        show pososhkov at left
        show volgin at right

        pososhkov "<{i}(Кричит Волгину){/i}>"

        hide volgin

        show pososhkov at truecenter

        hide volgin

        show pososhkov at truecenter

        pososhkov "{space=400}Зачем вы здесь? - И как вы смели?"

        pososhkov "Ступайте, сударь, вон!"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Ну, так! Совсем готов!"

        hide volgin

        show volgin at left
        show lyubskij at right

        hide volgin

        show volgin at left
        show lyubskij at right

        volgin "<{i}(Увидя Изведова и Любского в костюмах){/i}>"

        hide lyubskij

        show volgin at truecenter

        hide lyubskij

        show volgin at truecenter

        volgin "Ах, батюшки! Да здесь коллекция шутов!"

        volgin "Один, два... три!.."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show volgin at right

        hide pososhkov

        show pososhkov at left
        show volgin at right

        pososhkov "<{i}(подходя ближе к Волгину){/i}>"

        hide volgin

        show pososhkov at truecenter

        hide volgin

        show pososhkov at truecenter

        pososhkov "{space=400}Вы что! - Упрямы или глупы?"

        pososhkov "Вам, сударь, сказано, что вы для нашей труппы"

        pososhkov "Ненадобны, - и вам актером не бывать!"

        pososhkov "Ступайте вон сейчас!"

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Прошу не приставать!"

        volgin "Послушай, брат! Ведь я сердит! - Ей, будет схватка!"

        hide volgin

        show volgin at left
        show chestonov at right

        hide volgin

        show volgin at left
        show chestonov at right

        volgin "<{i}(Честонову){/i}>"

        hide chestonov

        show volgin at truecenter

        hide chestonov

        show volgin at truecenter

        volgin "Уйми его! - Кой черт! Пристал, как лихорадка!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Не трогайте его!"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Пожалуйста, отстань!"

        volgin "Поди-ка, брат, сюда! - Вот так, - поближе стань!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Что значит твой приезд?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}А это, сударь, значит,"

        volgin "Что Волгина никто никак не одурачит."

        volgin "Ты что мне обещал?.. Твердил и то и се..."

        volgin "Нет, шутишь, душенька! - Теперь я знаю всё."

        volgin "Подай племянника! Подай!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}А что ты знаешь?"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Что ты со мной и с ним прескверно поступаешь,"

        volgin "Что все вы заодно, - твой брат, его жена"

        volgin "И даже Оленька. Сейчас Кутермина,"

        volgin "Матрена Савишна, мне всё пересказала."

        volgin "Вот дело в чем: у вас актера недостало -"

        volgin "Так вы племянника ласкали для того,"

        volgin "Чтоб он играл. Теперь вы держите его"

        volgin "Для ваших нужд, игры, комиссий и рассылок,"

        volgin "А после этого забреете затылок?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Но выслушай меня!.."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Нет! Я ведь не дурак..."

        volgin "Подай племянника!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}Да он женат!"

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Кто!.. Как!.."

        volgin "На ком?.."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=200}На Оленьке."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Когда ж они успели?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Сейчас лишь от венца."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Неужто в самом деле?"

        hide volgin

    label Act_3_Scene_11:
        "{b}ЯВЛЕНИЕ 11{/b}"

        show velskij at left
        show lileev at truecenter
        show olenka at right

        show velskij at left
        show lileev at truecenter
        show olenka at right

        "<{i}Те же и Вельский, а вскоре Лилеев и Оленька выходят из левых дверей.{/i}>"

        hide velskij
        hide lileev
        hide olenka

        hide velskij
        hide lileev
        hide olenka

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "Ах, дядюшка! Вы здесь!"

        hide velskij

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Поди сюда, пострел!"

        volgin "Так ты меня позвать на свадьбу не хотел?"

        volgin "Он женится, а я себе и в ус не дую."

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Где Оленька?"

        hide chestonov

        show chestonov at left
        show lileev at truecenter
        show olenka at right

        hide chestonov

        show chestonov at left
        show lileev at truecenter
        show olenka at right

        chestonov "<{i}Лилеев и Оленька входят.{/i}>"

        hide lileev
        hide olenka

        show chestonov at truecenter

        hide lileev
        hide olenka

        show chestonov at truecenter

        hide chestonov

        show velskij at truecenter

        $ velskij_var = "{noalt}Вельский"

        velskij "{space=200}А вот она."

        hide velskij

        show velskij at left
        show volgin at right

        hide velskij

        show velskij at left
        show volgin at right

        velskij "<{i}(Подводит ее к Волгину){/i}>"

        hide volgin

        show velskij at truecenter

        hide volgin

        show velskij at truecenter

        velskij "{space=400}Рекомендую!"

        hide velskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Его жена, мой друг."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Я очень, очень рад!"

        volgin "Прошу любить меня!.."

        hide volgin

        show volgin at left
        show velskij at right

        hide volgin

        show volgin at left
        show velskij at right

        volgin "<{i}(Вельскому){/i}>"

        hide velskij

        show volgin at truecenter

        hide velskij

        show volgin at truecenter

        volgin "{space=400}Да точно ль ты женат?"

        volgin "Смотри!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}О! В этом нет сомненья никакого."

        hide chestonov

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Что это значит всё?"

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        hide pososhkov

        show pososhkov at left
        show lyubskij at right

        pososhkov "<{i}(Любскому){/i}>"

        hide lyubskij

        show pososhkov at truecenter

        hide lyubskij

        show pososhkov at truecenter

        pososhkov "{space=200}Вы поняли?"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Ни слова!"

        hide lyubskij

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at left
        show volgin at truecenter
        show lyubskij at right

        hide chestonov

        show chestonov at left
        show volgin at truecenter
        show lyubskij at right

        chestonov "<{i}(Волгину, подводя его к Любскому){/i}>"

        hide volgin
        hide lyubskij

        show chestonov at truecenter

        hide volgin
        hide lyubskij

        show chestonov at truecenter

        chestonov "А вот мой брат."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at left
        show lyubskij at right

        hide volgin

        show volgin at left
        show lyubskij at right

        volgin "<{i}(Любскому){/i}>"

        hide lyubskij

        show volgin at truecenter

        hide lyubskij

        show volgin at truecenter

        volgin "{space=400}С тобой мы с лишком сорок лет"

        volgin "Не виделись..."

        hide volgin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Так вы?.."

        hide lyubskij

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "{space=400}Гусарский тот корнет,"

        volgin "Проказник, балагур, твой старый сослуживец,"

        volgin "Ну - Волгин!"

        hide volgin

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=200}Как?"

        hide lyubskij

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        hide volgin

        show volgin at truecenter

        hide volgin

        show volgin at truecenter

        volgin "<{i}(обнимая его){/i}>"

        show volgin at truecenter

        show volgin at truecenter

        volgin "{space=400}Да, да! - Ты был всегда счастливец"

        volgin "И в картах и в любви, теперь, чай, не таков?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(подводя Посошкова){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        chestonov "Приятель наш, Авдей Михайлыч Посошков."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Неужели?"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "{space=400}Вы с ним немного посчитались..."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Так вы, сударь, не шут?"

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}Мы оба ошибались,"

        pososhkov "И я вас принимал совсем не за того."

        hide pososhkov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Мне, право, совестно..."

        hide volgin

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=400}И, сударь, - ничего!"

        hide pososhkov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "А что - который час?"

        hide lyubskij

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Без малого уж восемь."

        hide izvedov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "Пора бы начинать."

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "{space=200}Сейчас!"

        hide pososhkov

        show pososhkov at truecenter

        hide pososhkov

        show pososhkov at truecenter

        pososhkov "<{i}(К другим актерам){/i}>"

        show pososhkov at truecenter

        show pososhkov at truecenter

        pososhkov "{space=400}Покорно просим!"

        hide pososhkov

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        hide chestonov

        show chestonov at left
        show volgin at right

        hide chestonov

        show chestonov at left
        show volgin at right

        chestonov "<{i}(Волгину){/i}>"

        hide volgin

        show chestonov at truecenter

        hide volgin

        show chestonov at truecenter

        chestonov "Пойдем-ка, милый мой! Посмотрим молодых."

        hide chestonov

        show volgin at truecenter

        $ volgin_var = "{noalt}Волгин"

        volgin "Вот так-то бы всегда, без вычуров пустых,"

        volgin "Женились, да и всё! - А то, глядишь, бедняжки"

        volgin "Прождали б целый год. Отсрочки да оттяжки! -"

        volgin "А всё ведь я, мой друг, их свадьбой повернул!"

        hide volgin

        show chestonov at truecenter

        $ chestonov_var = "{noalt}Честонов"

        chestonov "Конечно, ты!.. - Пойдем!"

        hide chestonov

        show chestonov at truecenter

        hide chestonov

        show chestonov at truecenter

        chestonov "<{i}(Уходят.){/i}>"

        show chestonov at truecenter

        show chestonov at truecenter

        hide chestonov

        show lyubskij at truecenter

        $ lyubskij_var = "{noalt}Любский"

        lyubskij "{space=400}Насилу отдохнул."

        lyubskij "Ступайте же!"

        hide lyubskij

        show lyubskij at truecenter

        hide lyubskij

        show lyubskij at truecenter

        lyubskij "<{i}(Уходит на сцену.){/i}>"

        show lyubskij at truecenter

        show lyubskij at truecenter

        hide lyubskij

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        hide pososhkov

        show pososhkov at left
        show lileev at right

        hide pososhkov

        show pososhkov at left
        show lileev at right

        pososhkov "<{i}(Лилееву){/i}>"

        hide lileev

        show pososhkov at truecenter

        hide lileev

        show pososhkov at truecenter

        pososhkov "{space=400}Я вас прошу: не молодитесь!"

        pososhkov "Играйте старика!"

        hide pososhkov

        show lileev at truecenter

        $ lileev_var = "{noalt}Лилеев"

        lileev "{space=400}Тьфу пропасть! - Отвяжитесь!"

        lileev "Я знаю лучше вас, как должно мне играть."

        hide lileev

        show lileev at truecenter

        hide lileev

        show lileev at truecenter

        lileev "<{i}(Уходит.){/i}>"

        show lileev at truecenter

        show lileev at truecenter

        hide lileev

        show pososhkov at truecenter

        $ pososhkov_var = "{noalt}Посошков"

        pososhkov "Ну, вот увидите! Он точно будет врать!"

        hide pososhkov

        show natasha at left
        show izvedov at right

        show natasha at left
        show izvedov at right

        "<{i}Все уходят на сцену, кроме Наташи и Изведова.{/i}>"

        hide natasha
        hide izvedov

        hide natasha
        hide izvedov

    label Act_3_Scene_12:
        "{b}ЯВЛЕНИЕ 12{/b}"

        show izvedov at left
        show natasha at right

        show izvedov at left
        show natasha at right

        "<{i}Изведов и Наташа.{/i}>"

        hide izvedov
        hide natasha

        hide izvedov
        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Я счастья своего никак не постигаю:"

        izvedov "Афишку сочинял, женюсь - и сам играю!"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Всё это хорошо; однако же пойдем!"

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "Теперь сомненья нет, театр мы заведем"

        izvedov "И, верно, с честию поддержим наше званье!"

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Ну, что ж! Пойдем!"

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Постой! - Еще одно желанье:"

        izvedov "Без этого, мой друг, всё прочее хоть брось,"

        izvedov "А признаюсь, когда б и это удалось -"

        izvedov "Афишку бы тогда я в рамочки повесил..."

        hide izvedov

        show natasha at truecenter

        $ natasha_var = "{noalt}Наташа"

        natasha "Что ж надобно?"

        hide natasha

        show izvedov at truecenter

        $ izvedov_var = "{noalt}Изведов"

        izvedov "{space=400}Чтоб нам похлопали из кресел!"

        hide izvedov

"<{i}<1828>{/i}>"


