"In the public domain."

define odin = Character("odin_var", color="#FFB300", dynamic=True)
define drugoj = Character("drugoj_var", color="#803E75", dynamic=True)
define tretij_usatyj = Character("tretij_usatyj_var", color="#FF6800", dynamic=True)
define hozjain = Character("hozjain_var", color="#A6BDD7", dynamic=True)
define seminarist = Character("seminarist_var", color="#C10020", dynamic=True)
define pervyj_sobutylnik = Character("pervyj_sobutylnik_var", color="#CEA262", dynamic=True)
define vtoroj_sobutylnik = Character("vtoroj_sobutylnik_var", color="#817066", dynamic=True)
define verlen = Character("verlen_var", color="#007D34", dynamic=True)
define muzhchina = Character("muzhchina_var", color="#F6768E", dynamic=True)
define molodoj_chelovek = Character("molodoj_chelovek_var", color="#00538A", dynamic=True)
define gauptman = Character("gauptman_var", color="#FF7A5C", dynamic=True)
define poet = Character("poet_var", color="#53377A", dynamic=True)
define polovoj = Character("polovoj_var", color="#FF8E00", dynamic=True)
define chelovek_v_palto = Character("chelovek_v_palto_var", color="#B32851", dynamic=True)
define pervyj = Character("pervyj_var", color="#F4C800", dynamic=True)
define vtoroj = Character("vtoroj_var", color="#7F180D", dynamic=True)
define sobesednik = Character("sobesednik_var", color="#93AA00", dynamic=True)
define zvezdochet = Character("zvezdochet_var", color="#593315", dynamic=True)
define goluboj = Character("goluboj_var", color="#F13A13", dynamic=True)
define gospodin = Character("gospodin_var", color="#232C16", dynamic=True)
define hozjain_trete_videnie = Character("hozjain_trete_videnie_var", color="#182D83", dynamic=True)
define gost = Character("gost_var", color="#1CAA15", dynamic=True)
define zhorzh = Character("zhorzh_var", color="#4AA750", dynamic=True)
define misha = Character("misha_var", color="#D2C20A", dynamic=True)
define starik = Character("starik_var", color="#E31244", dynamic=True)
define ryzhij_gospodin = Character("ryzhij_gospodin_var", color="#09DF8F", dynamic=True)
define drugoj_trete_videnie = Character("drugoj_trete_videnie_var", color="#19AF6A", dynamic=True)
define devushka = Character("devushka_var", color="#ECA062", dynamic=True)
define neznakomka = Character("neznakomka_var", color="#B0B7C1", dynamic=True)
define hozjajka = Character("hozjajka_var", color="#9F7F54", dynamic=True)
define dama = Character("dama_var", color="#ECE104", dynamic=True)
define razjarennye_dvorniki = Character("razjarennye_dvorniki_var", color="#B8DD03", dynamic=True)
define raznye_golosa = Character("raznye_golosa_var", color="#2B22D0", dynamic=True)
define kto_to = Character("kto_to_var", color="#C2C0A8", dynamic=True)

label start:
    play music "audio/music/6.mp3" fadeout 1.0 fadein 1.0

    scene 7 with fade

    "Незнакомка"

    "На портрете была изображена действительно необыкновенной красоты женщина. Она была сфотографирована в черном шелковом платье, чрезвычайно простого и изящного фасона; волосы, по-видимому темно-русые, были убраны просто, по-домашнему;"

    "глаза темные, глубокие, лоб задумчивый; выражение лица страстное и как бы высокомерное. Она была несколько худа лицом, может быть, и бледна..."

    "Достоевский"

    "— А как вы узнали, что это я? Где вы меня видели прежде? Что это, в самом деле, я как будто его где-то видела?"

    "— Я вас тоже будто видел где-то?"

    "— Где? — Где?"

    "— Я ваши глаза точно где-то видел... да этого быть не может!"

    "Это я так... Я здесь никогда и не был. Может быть, во сне..."

    "Достоевский"

    menu:
        "{color=#000}ДЕЙСТВУЮЩИЕ ЛИЦА{/color}":
            jump Characters
        "{color=#000}ПЕРВОЕ ВИДЕНИЕ{/color}":
            jump Act_1
        "{color=#000}ВТОРОЕ ВИДЕНИЕ{/color}":
            jump Act_2
        "{color=#000}ТРЕТЬЕ ВИДЕНИЕ{/color}":
            jump Act_3

    label Characters:
        play music "audio/music/1.mp3" fadeout 1.0 fadein 1.0

        scene 11 with fade

        "{b}ДЕЙСТВУЮЩИЕ ЛИЦА{/b}"

        show neznakomka at truecenter
        "Незнакомка."
        hide neznakomka

        show goluboj at truecenter
        "Голубой."
        hide goluboj

        show zvezdochet at truecenter
        "Звездочет."
        hide zvezdochet

        show poet at truecenter
        "Поэт."
        hide poet

        "Посетители кабачка и гостиной."

        "Два дворника."


label Act_1:
    play music "audio/music/11.mp3" fadeout 1.0 fadein 1.0

    scene 3 with fade

    "{b}ПЕРВОЕ ВИДЕНИЕ{/b}"

    "<{i}Уличный кабачок. Подрагивает бело-матовый свет ацетиленового фонаря в смятом колпачке. На обоях изображены совершенно одинаковые корабли с огромными флагами. Они взрезают носами голубые воды.{/i}>"

    "<{i}За дверью, которая часто раскрывается, впуская посетителей, и за большими окнами, украшенными плющом, идут прохожие в шубах и девушки в платочках — под голубым вечерним снегом.{/i}>"

    "<{i}За прилавком, на котором водружена бочка с гномом и надписью «Кружка-бокал», — двое совершенно похожих друг на друга: оба с коками и проборами, в зеленых фартуках; только у хозяина усы вниз, а у брата его, полового, усы вверх.{/i}>"

    show verlen at left
    show gauptman at right

    "<{i}У одного окна, за столиком, сидит пьяный старик — вылитый Верлэн, у другого — безусый бледный человек — вылитый Гауптман. Несколько пьяных компаний.{/i}>"

    hide verlen
    hide gauptman

    "<{i}Разговор в одной компании{/i}>"

    show odin at truecenter

    $ odin_var = "{noalt}Один"

    odin "Купил я эту шубу за двадцать пять рублей. А тебе, Сашка, меньше тридцати ни за что не уступлю."

    hide odin

    show drugoj at truecenter

    $ drugoj_var = "{noalt}Другой"

    hide drugoj

    show drugoj at truecenter

    drugoj "<{i}(убедительно и с обидой){/i}>"

    show drugoj at truecenter

    drugoj "Да врешь ты!.. Да вот поди ж ты... Я тебе..."

    hide drugoj

    show tretij_usatyj at truecenter

    $ tretij_usatyj_var = "{noalt}Третий усатый"

    hide tretij_usatyj

    show tretij_usatyj at truecenter

    tretij_usatyj "<{i}(кричит){/i}>"

    show tretij_usatyj at truecenter

    tretij_usatyj "Молчать! Не ругаться! Еще бутылочку, любезный."

    hide tretij_usatyj

    show tretij_usatyj at left
    show polovoj at right

    tretij_usatyj "<{i}Половой подбегает. Слышно, как булькает пиво. Молчание. Одинокий посетитель поднимается из угла и неверной походкой идет к прилавку. Начинает шарить в блестящей посудине с вареными раками.{/i}>"

    hide polovoj

    show tretij_usatyj at truecenter

    hide tretij_usatyj

    show hozjain at truecenter

    $ hozjain_var = "{noalt}Хозяин"

    hozjain "Позвольте, господин. Так нельзя. Вы у нас всех раков руками переберете. Никто кушать не станет."

    hide hozjain

    show hozjain at truecenter

    hozjain "<{i}Посетитель, мыча, отходит.{/i}>"

    show hozjain at truecenter

    hide hozjain

    show hozjain at truecenter

    hozjain "<{i}Разговор в другой компании{/i}>"

    show hozjain at truecenter

    hide hozjain

    show seminarist at truecenter

    $ seminarist_var = "{noalt}Семинарист"

    seminarist "И танцовала она, милый друг ты мой, скажу я тебе, как небесное создание. Просто взял бы ее за белые ручки и прямо в губки, скажу тебе, поцеловал..."

    hide seminarist

    show pervyj_sobutylnik at truecenter

    $ pervyj_sobutylnik_var = "{noalt}Собутыльник"

    play sound1 male_laughter

    hide pervyj_sobutylnik

    show pervyj_sobutylnik at truecenter

    pervyj_sobutylnik "<{i}(визгливо хохочет){/i}>"

    show pervyj_sobutylnik at truecenter

    stop sound1

    pervyj_sobutylnik "Эка, эка, Васинька-то наш, размечтался, заалел, как маков цвет! А что она тебе за любовь-то? За любовь-то что?.. А?.."

    play sound1 male_laughter

    hide pervyj_sobutylnik

    show pervyj_sobutylnik at truecenter

    pervyj_sobutylnik "<{i}Все визгливо хохочут.{/i}>"

    show pervyj_sobutylnik at truecenter

    stop sound1

    hide pervyj_sobutylnik

    show seminarist at truecenter

    $ seminarist_var = "{noalt}Семинарист"

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}(совсем красный){/i}>"

    show seminarist at truecenter

    seminarist "И, милый друг ты мой, скажу тебе, нехорошо смеяться. Так бы вот взял её, и унес бы от нескромных взоров, и на улице плясала бы она передо мной на белом снегу... как птица, летала бы."

    seminarist "И откуда мои крылья взялись, — сам полетел бы за ней, над белыми снегами..."

    play sound1 male_laughter

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}Все хохочут.{/i}>"

    show seminarist at truecenter

    stop sound1

    hide seminarist

    show vtoroj_sobutylnik at truecenter

    $ vtoroj_sobutylnik_var = "{noalt}Второй собутыльник"

    vtoroj_sobutylnik "Ты, Васька, смотри, того, по первопутку-то не очень полетишь..."

    hide vtoroj_sobutylnik

    show pervyj_sobutylnik at truecenter

    $ pervyj_sobutylnik_var = "{noalt}Первый собутыльник"

    pervyj_sobutylnik "Тебе бы по морозцу-то легче, а то с твоей милой как раз в грязь угодишь..."

    hide pervyj_sobutylnik

    show vtoroj_sobutylnik at truecenter

    $ vtoroj_sobutylnik_var = "{noalt}Второй собутыльник"

    vtoroj_sobutylnik "Мечтатель."

    hide vtoroj_sobutylnik

    show seminarist at truecenter

    $ seminarist_var = "{noalt}Семинарист"

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}(совсем осоловел){/i}>"

    show seminarist at truecenter

    seminarist "Эх, милые други, в семинарии не учась, скажу я вам, вы нежных чувств не понимаете. А впрочем, еще бы пивца..."

    hide seminarist

    show verlen at truecenter

    $ verlen_var = "{noalt}Верлэн"

    hide verlen

    show verlen at truecenter

    verlen "<{i}(бормочет громко сам с собою){/i}>"

    show verlen at truecenter

    verlen "Каждому свое. Каждому свое..."

    hide verlen

    show verlen at left
    show gauptman at right

    verlen "<{i}Гауптман делает выразительные знаки половому. Входят рыжий мужчина и девушка в платочке.{/i}>"

    hide gauptman

    show verlen at truecenter

    hide verlen

    show devushka at truecenter

    $ devushka_var = "{noalt}Девушка"

    hide devushka

    show devushka at truecenter

    devushka "<{i}(половому){/i}>"

    show devushka at truecenter

    devushka "Бутылку портеру, Миша."

    hide devushka

    show devushka at truecenter

    devushka "<{i}(Продолжает быстро рассказывать мужчине.){/i}>"

    show devushka at truecenter

    devushka "...только она, милый мой, вышла, хвать — забыла хозяйку пивом угостить. Сейчас — назад, а уж он комод открыл, да и роется, все перерыл, все перерыл, думал — не скоро вернется... Она, милый мой, кричать, а он, милый мой, ей рот зажимать."

    devushka "Ну, все-таки хозяйка прибежала, да сама кричать, да дворника позвала; так его, милый мой, сейчас в участок..."

    hide devushka

    show devushka at truecenter

    devushka "<{i}(Быстро прерывает.){/i}>"

    show devushka at truecenter

    devushka "Дай двугривенный."

    hide devushka

    show devushka at left
    show muzhchina at right

    devushka "<{i}Мужчина хмуро вынимает двугривенный.{/i}>"

    hide muzhchina

    show devushka at truecenter

    hide devushka

    show devushka at truecenter

    $ devushka_var = "{noalt}Девушка"

    devushka "Тебе нешто жалко?"

    hide devushka

    show muzhchina at truecenter

    $ muzhchina_var = "{noalt}Мужчина"

    muzhchina "Пей, да помалкивай."

    hide muzhchina

    show muzhchina at left
    show gauptman at right

    muzhchina "<{i}Молчат. Пьют. Вбегает молодой человек и радостно бросается к Гауптману.{/i}>"

    hide gauptman

    show muzhchina at truecenter

    hide muzhchina

    show molodoj_chelovek at truecenter

    $ molodoj_chelovek_var = "{noalt}Молодой человек"

    molodoj_chelovek "Костя, друг, она у дверей дожидает!.."

    hide molodoj_chelovek

    show gauptman at truecenter

    $ gauptman_var = "{noalt}Гауптман"

    gauptman "Ладно. Пошляется еще. Давай выпьем."

    hide gauptman

    show verlen at truecenter

    $ verlen_var = "{noalt}Верлэн"

    hide verlen

    show verlen at truecenter

    verlen "<{i}(громко бормочет){/i}>"

    show verlen at truecenter

    verlen "И всем людям — свое занятие... И каждому — свое беспокойство."

    hide verlen

    show verlen at left
    show poet at right

    verlen "<{i}Входит Поэт. Подзывает полового.{/i}>"

    hide poet

    show verlen at truecenter

    hide verlen

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Угостить вас?"

    hide poet

    show polovoj at truecenter

    $ polovoj_var = "{noalt}Половой"

    hide polovoj

    show polovoj at truecenter

    polovoj "<{i}(прирожденный юморист){/i}>"

    show polovoj at truecenter

    polovoj "Великая честь-с... От знаменитого лица-с..."

    hide polovoj

    show polovoj at left
    show poet at right

    polovoj "<{i}Убегает за пивом. Поэт вынимает записную книжку. Тишина. Ацетилен шипит. Похрустывают бублики. Половой приносит Поэту бутылку пива и садится на край стула против него.{/i}>"

    hide poet

    show polovoj at truecenter

    hide polovoj

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Вы послушайте только. Бродить по улицам, ловить отрывки незнакомых слов. Потом — прийти вот сюда и рассказать свою душу подставному лицу."

    hide poet

    show polovoj at truecenter

    $ polovoj_var = "{noalt}Половой"

    polovoj "Непонятно-с, но весьма утонченно-с..."

    play sound1 running

    hide polovoj

    show polovoj at left
    show poet at right

    polovoj "<{i}Срывается со стула и бежит на зов посетителя. Поэт пишет в книжке.{/i}>"

    hide poet

    show polovoj at truecenter

    stop sound1

    hide polovoj

    show devushka at truecenter

    $ devushka_var = "{noalt}Девушка"

    hide devushka

    show devushka at truecenter

    devushka "<{i}(напевает){/i}>"

    show devushka at truecenter

    devushka "Как люблю я ее..."

    devushka "А она за любовь..."

    hide devushka

    show devushka at left
    show polovoj at truecenter
    show poet at right

    devushka "<{i}Половой возвращается к Поэту.{/i}>"

    hide polovoj
    hide poet

    show devushka at truecenter

    hide devushka

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    hide poet

    show poet at truecenter

    poet "<{i}(пьет){/i}>"

    show poet at truecenter

    poet "Видеть много женских лиц. Сотни глаз, больших и глубоких, синих, темных, светлых. Узких, как глаза рыси. Открытых широко, младенчески. Любить их. Желать их. Не может быть человека, который не любит. И вы их должны любить."

    hide poet

    show polovoj at truecenter

    $ polovoj_var = "{noalt}Половой"

    polovoj "Слушаю-с."

    hide polovoj

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "И среди этого огня взоров, среди вихря взоров, возникнет внезапно, как бы расцветет под голубым снегом — одно лицо: единственно прекрасный лик Незнакомки, под густою, темной вуалью... Вот качаются перья на шляпе..."

    poet "Вот узкая рука, стянутая перчаткой, держит шелестящее платье... Вот медленно проходит она... проходит она..."

    hide poet

    show poet at truecenter

    poet "<{i}Жадно пьет.{/i}>"

    show poet at truecenter

    hide poet

    show verlen at truecenter

    $ verlen_var = "{noalt}Верлэн"

    hide verlen

    show verlen at truecenter

    verlen "<{i}(бормочет){/i}>"

    show verlen at truecenter

    verlen "И все проходит. И каждому — своя забота."

    hide verlen

    show seminarist at truecenter

    $ seminarist_var = "{noalt}Семинарист"

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}(заплетающимся языком){/i}>"

    show seminarist at truecenter

    seminarist "Танцевала она, как небесный, скажу вам, ангел, а вы, черти и разбойники, не стоите ее мизинца. А впрочем, выпьем."

    hide seminarist

    show pervyj_sobutylnik at truecenter

    $ pervyj_sobutylnik_var = "{noalt}Собутыльник"

    pervyj_sobutylnik "Мечтатель. Оттого и пьешь. И все мы — мечтатели. Поцелуй меня, дружок."

    hide pervyj_sobutylnik

    show pervyj_sobutylnik at truecenter

    pervyj_sobutylnik "<{i}Обнимаются.{/i}>"

    show pervyj_sobutylnik at truecenter

    hide pervyj_sobutylnik

    show seminarist at truecenter

    $ seminarist_var = "{noalt}Семинарист"

    seminarist "И никто ее так не полюбит, как я. И будем мы на белом снегу свою грустную жизнь доживать. Она — плясать, а я — на шарманке играть. И полетим. И под самый серебряный месяц залетим."

    seminarist "И туда, черт возьми, скажу я вам, дурацким вашим грязным носам, милые други, не соваться. И все-таки я очень вас люблю и высоко ставлю. Кто из одной бутылки не пивал, тот и дружбы не видал."

    play sound1 male_laughter

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}Все хохочут.{/i}>"

    show seminarist at truecenter

    stop sound1

    hide seminarist

    show pervyj_sobutylnik at truecenter

    $ pervyj_sobutylnik_var = "{noalt}Собутыльник"

    pervyj_sobutylnik "Ай да Васька! Уж очень складно! Поцелуемся, дружок."

    hide pervyj_sobutylnik

    show molodoj_chelovek at truecenter

    $ molodoj_chelovek_var = "{noalt}Молодой человек"

    hide molodoj_chelovek

    show molodoj_chelovek at left
    show gauptman at right

    molodoj_chelovek "<{i}(Гауптману){/i}>"

    hide gauptman

    show molodoj_chelovek at truecenter

    molodoj_chelovek "Однако ж будет. Что ей столько на морозе дожидать? Замерзнет совсем. Пойдем, брат Костя."

    hide molodoj_chelovek

    show gauptman at truecenter

    $ gauptman_var = "{noalt}Гауптман"

    gauptman "Брось. Если женскому нраву потакать, так от мужчины ничего не останется — только ему в рожу плюнуть. Пусть пошляется, а мы еще посидим."

    hide gauptman

    show gauptman at left
    show molodoj_chelovek at truecenter
    show chelovek_v_palto at right

    gauptman "<{i}Молодой человек послушался. Все посетители пьют и хмелеют. Человек в желтом трепаном пальто, сидевший отдельно, встает и обращается к честно́й компании с речью.{/i}>"

    hide molodoj_chelovek
    hide chelovek_v_palto

    show gauptman at truecenter

    hide gauptman

    show chelovek_v_palto at truecenter

    $ chelovek_v_palto_var = "{noalt}Человек в пальто"

    chelovek_v_palto "Государи мои! Есть у меня небольшая вещица — весьма ценная миниатюра."

    hide chelovek_v_palto

    show chelovek_v_palto at truecenter

    chelovek_v_palto "<{i}(Вытаскивает из кармана камею.){/i}>"

    show chelovek_v_palto at truecenter

    chelovek_v_palto "Вот-с, не угодно ли: с одной стороны — изображение эмблемы, а с другой — приятная дама в тюнике на земном шаре сидит и над этим шаром держит скипетр: подчиняйтесь, мол, повинуйтесь — и больше ничего!"

    play sound1 male_laughter

    hide chelovek_v_palto

    show chelovek_v_palto at truecenter

    chelovek_v_palto "<{i}Все одобрительно смеются. Некоторые подходят и рассматривают камею.{/i}>"

    show chelovek_v_palto at truecenter

    stop sound1

    hide chelovek_v_palto

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    hide poet

    show poet at truecenter

    poet "<{i}(захмелевший){/i}>"

    show poet at truecenter

    poet "Вечная сказка. Это — Она — Мироправительница. Она держит жезл и повелевает миром. Все мы очарованы Ею."

    hide poet

    show chelovek_v_palto at truecenter

    $ chelovek_v_palto_var = "{noalt}Человек в пальто"

    chelovek_v_palto "Рад служить русской интеллигенции. Дешево продам, хотя досталось не дешево, но уж, как говорится, только по дружбе. Вижу, что любитель. Ну, так по рукам."

    hide chelovek_v_palto

    show chelovek_v_palto at left
    show poet at truecenter
    show molodoj_chelovek at right

    chelovek_v_palto "<{i}Поэт дает ему монету. Берет камею, рассматривает ее. Человек в пальто садится на свое место. Разговор продолжается только между двумя, сидящими за отдельным столиком.{/i}>"

    hide poet
    hide molodoj_chelovek

    show chelovek_v_palto at truecenter

    hide chelovek_v_palto

    show pervyj at truecenter

    $ pervyj_var = "{noalt}Первый"

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}(берёт юмористический журнал){/i}>"

    show pervyj at truecenter

    pervyj "А теперь пришло время нам повеселиться. Ну, Ваня, слушай"

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}(торжественно развертывает журнал и читает:){/i}>"

    show pervyj at truecenter

    pervyj "«Любящие супруги. Муж: — Ты, милочка, зайди сегодня к мамаше и попроси ее...»"

    play sound1 male_laughter

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}Заранее отчаянно хохочет.{/i}>"

    show pervyj at truecenter

    stop sound1

    hide pervyj

    show vtoroj at truecenter

    $ vtoroj_var = "{noalt}Второй"

    vtoroj "Ишь, черт возьми, здорово!"

    hide vtoroj

    show pervyj at truecenter

    $ pervyj_var = "{noalt}Первый"

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}(продолжает читать){/i}>"

    show pervyj at truecenter

    pervyj "«...И попроси ее... подарить Катеньке куколку...»"

    play sound1 male_laughter

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}Страшно хохочет.{/i}>"

    show pervyj at truecenter

    stop sound1

    hide pervyj

    show pervyj at truecenter

    $ pervyj_var = "{noalt}Первый"

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}(читает){/i}>"

    show pervyj at truecenter

    pervyj "«Жена: — Что ты, милочка! Катеньке уж скоро двадцать лет."

    play sound1 male_laughter

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}(Еле может прочесть от смеха.){/i}>"

    show pervyj at truecenter

    stop sound1

    pervyj "Ей уж не куколку, а женишка пора подарить»."

    play sound1 male_laughter

    hide pervyj

    show pervyj at truecenter

    pervyj "<{i}Громовой хохот.{/i}>"

    show pervyj at truecenter

    stop sound1

    hide pervyj

    show vtoroj at truecenter

    $ vtoroj_var = "{noalt}Второй"

    vtoroj "Вот так здорово!"

    hide vtoroj

    show pervyj at truecenter

    $ pervyj_var = "{noalt}Первый"

    pervyj "Что называется отбрила!"

    hide pervyj

    show vtoroj at truecenter

    $ vtoroj_var = "{noalt}Второй"

    vtoroj "Черт их дери, ловко пишут!.."

    hide vtoroj

    show vtoroj at truecenter

    vtoroj "<{i}И опять одинокий посетитель шарит в посудине. Он вытаскивает красных раков за клешни. Подержит и положит. И опять хозяин отгоняет его.{/i}>"

    show vtoroj at truecenter

    hide vtoroj

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    hide poet

    show poet at truecenter

    poet "<{i}(рассматривает камею){/i}>"

    show poet at truecenter

    poet "Вечное возвращение. Снова Она объемлет шар земной. И снова мы подвластны Ее очарованию. Вот Она кружит свой процветающий жезл. Вот Она кружит меня... И я кружусь с Нею... Под голубым... под вечерним снегом..."

    hide poet

    show seminarist at truecenter

    $ seminarist_var = "{noalt}Семинарист"

    seminarist "Танцует... Танцует... Я на шарманке, а она под шарманку."

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}(Делает пьяные жесты, как будто что-то ловит.){/i}>"

    show seminarist at truecenter

    seminarist "Вот, не поймал... опять не поймал... но и вам, черти, не поймать, если уж мне не поймать..."

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}Медленно, медленно начинают кружиться стены кабачка. Потолок наклоняется, один конец его протягивается вверх бесконечно. Корабли на обоях, кажется, плывут близко, а все не могут доплыть.{/i}>"

    show seminarist at truecenter

    hide seminarist

    show seminarist at truecenter

    seminarist "<{i}Сквозь смутный общий говор человек в пальто, уже присоединившийся к кому-то, кричит.{/i}>"

    show seminarist at truecenter

    hide seminarist

    show chelovek_v_palto at truecenter

    $ chelovek_v_palto_var = "{noalt}Человек в пальто"

    chelovek_v_palto "Нет-с, я любитель! Люблю острый сыр, знаете, такой круглый!"

    hide chelovek_v_palto

    show chelovek_v_palto at truecenter

    chelovek_v_palto "<{i}(Делает кругообразные жесты.){/i}>"

    show chelovek_v_palto at truecenter

    chelovek_v_palto "Забыл название."

    hide chelovek_v_palto

    show sobesednik at truecenter

    $ sobesednik_var = "{noalt}Его собеседник"

    hide sobesednik

    show sobesednik at truecenter

    sobesednik "<{i}(неуверенно){/i}>"

    show sobesednik at truecenter

    sobesednik "А вы... пробовали?"

    hide sobesednik

    show chelovek_v_palto at truecenter

    $ chelovek_v_palto_var = "{noalt}Человек в пальто"

    chelovek_v_palto "Что пробовал? Вы думаете, нет? Я рошефор кушал!"

    hide chelovek_v_palto

    show sobesednik at truecenter

    $ sobesednik_var = "{noalt}Собеседник"

    hide sobesednik

    show sobesednik at truecenter

    sobesednik "<{i}(под которым качается стул){/i}>"

    show sobesednik at truecenter

    sobesednik "А знаете... люксем-бургский... так пахнет нехорошо... и шевелится, шевелится..."

    hide sobesednik

    show sobesednik at truecenter

    sobesednik "<{i}(Чмокает губами, шевелит пальцами.){/i}>"

    show sobesednik at truecenter

    hide sobesednik

    show chelovek_v_palto at truecenter

    $ chelovek_v_palto_var = "{noalt}Человек в пальто"

    hide chelovek_v_palto

    show chelovek_v_palto at truecenter

    chelovek_v_palto "<{i}(вдохновенно встает){/i}>"

    show chelovek_v_palto at truecenter

    chelovek_v_palto "Швейцарский!.. Вот что-с!"

    hide chelovek_v_palto

    show chelovek_v_palto at truecenter

    chelovek_v_palto "<{i}(Щелкает пальцами.){/i}>"

    show chelovek_v_palto at truecenter

    hide chelovek_v_palto

    show sobesednik at truecenter

    $ sobesednik_var = "{noalt}Собеседник"

    hide sobesednik

    show sobesednik at truecenter

    sobesednik "<{i}(мигает и сомневается){/i}>"

    show sobesednik at truecenter

    sobesednik "Ну, этим не удивите..."

    hide sobesednik

    show chelovek_v_palto at truecenter

    $ chelovek_v_palto_var = "{noalt}Человек в пальто"

    hide chelovek_v_palto

    show chelovek_v_palto at truecenter

    chelovek_v_palto "<{i}(громко, как ружейный залп){/i}>"

    show chelovek_v_palto at truecenter

    chelovek_v_palto "Бри!"

    hide chelovek_v_palto

    show sobesednik at truecenter

    $ sobesednik_var = "{noalt}Собеседник"

    sobesednik "Ну это... это... знаете..."

    hide sobesednik

    show chelovek_v_palto at truecenter

    $ chelovek_v_palto_var = "{noalt}Человек в пальто"

    hide chelovek_v_palto

    show chelovek_v_palto at truecenter

    chelovek_v_palto "<{i}(угрожающе){/i}>"

    show chelovek_v_palto at truecenter

    chelovek_v_palto "Что знаете?"

    hide chelovek_v_palto

    show sobesednik at truecenter

    $ sobesednik_var = "{noalt}Собеседник"

    hide sobesednik

    show sobesednik at truecenter

    sobesednik "<{i}(уничтожен){/i}>"

    show sobesednik at truecenter

    sobesednik "Все вертится, кажется перевернется сейчас. Корабли на обоях плывут, вспенивая голубые воды. Одну минуту кажется, что все стоит вверх ногами."

    hide sobesednik

    show verlen at truecenter

    $ verlen_var = "{noalt}Верлэн"

    hide verlen

    show verlen at truecenter

    verlen "<{i}(бормочет){/i}>"

    show verlen at truecenter

    verlen "И всему свой черед... И всем пора идти домой..."

    hide verlen

    show gauptman at truecenter

    $ gauptman_var = "{noalt}Гауптман"

    hide gauptman

    show gauptman at truecenter

    gauptman "<{i}(орёт){/i}>"

    show gauptman at truecenter

    gauptman "Шлюха она, ну и пусть шляется! А мы выпьем!"

    hide gauptman

    show devushka at truecenter

    $ devushka_var = "{noalt}Девушка"

    hide devushka

    show devushka at truecenter

    devushka "<{i}(поет в ухо мужчине){/i}>"

    show devushka at truecenter

    devushka "Прощай, желанный мой..."

    hide devushka

    show seminarist at truecenter

    $ seminarist_var = "{noalt}Семинарист"

    seminarist "Снег танцует. И мы танцуем. И шарманка плачет. И я плачу. И мы все плачем."

    hide seminarist

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Синий снег. Кружится. Мягко падает. Синие очи. Густая вуаль. Медленно проходит Она. Небо открылось. Явись! Явись!"

    hide poet

    "<{i}Весь кабачок как будто нырнул куда-то. Стены расступаются. Окончательно наклонившийся потолок открывает небо — зимнее, синее, холодное. В голубых вечерних снегах открывается —{/i}>"


label Act_2:
    play music "audio/music/7.mp3" fadeout 1.0 fadein 1.0

    scene 2 with fade

    "{b}ВТОРОЕ ВИДЕНИЕ{/b}"

    "<{i}Тот же вечер. Конец улицы на краю города. Последние дома, обрываясь внезапно, открывают широкую перспективу: темный пустынный мост через большую реку. По обеим сторонам моста дремлют тихие корабли с сигнальными огнями.{/i}>"

    "<{i}За мостом тянется бесконечная, прямая, как стрела, аллея, обрамленная цепочками фонарей и белыми от инея деревьями. В воздухе порхает и звездится снег.{/i}>"

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    hide zvezdochet

    show zvezdochet at truecenter

    zvezdochet "<{i}(на мосту){/i}>"

    show zvezdochet at truecenter

    zvezdochet "Ночь полнозвездная светла."

    zvezdochet "У взора — только два крыла."

    zvezdochet "Но счет звезда́м вести нельзя —"

    zvezdochet "Туманна млечная стезя,"

    zvezdochet "И бедный взор туманится..."

    zvezdochet "Кто этот пьяница?"

    hide zvezdochet

    show zvezdochet at left
    show poet at right

    zvezdochet "<{i}Два дворника волокут под руки пьяного Поэта.{/i}>"

    hide poet

    show zvezdochet at truecenter

    hide zvezdochet

    show razjarennye_dvorniki at truecenter

    $ razjarennye_dvorniki_var = "{noalt}Разъяренные дворники"

    razjarennye_dvorniki "Он — посетитель кабачка,"

    razjarennye_dvorniki "И с ним расправа коротка!"

    razjarennye_dvorniki "Эй, Ванька, дай ему щелчка!"

    razjarennye_dvorniki "Эй, Васька, дай ему толчка!"

    hide razjarennye_dvorniki

    show razjarennye_dvorniki at left
    show poet at right

    razjarennye_dvorniki "<{i}Волокут Поэта дальше.{/i}>"

    hide poet

    show razjarennye_dvorniki at truecenter

    hide razjarennye_dvorniki

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Восходит новая звезда."

    zvezdochet "Всех ослепительней она."

    zvezdochet "Недвижна темная вода,"

    zvezdochet "И в ней звезда отражена."

    zvezdochet "Ах! падает, летит звезда..."

    zvezdochet "Лети сюда! сюда! сюда!"

    hide zvezdochet

    show zvezdochet at truecenter

    zvezdochet "<{i}По небу, описывая медленную дугу, скатывается яркая и тяжелая звезда. Через миг по мосту идет прекрасная женщина в черном, с удивленным взором расширенных глаз. Все становится сказочным — темный мост и дремлющие голубые корабли.{/i}>"

    show zvezdochet at truecenter

    hide zvezdochet

    show zvezdochet at left
    show neznakomka at right

    zvezdochet "<{i}Незнакомка застывает у перил моста, еще храня свой бледный падучий блеск. Снег, вечно юный, одевает ее плечи, опушает стан. Она, как статуя, ждет.{/i}>"

    hide neznakomka

    show zvezdochet at truecenter

    hide zvezdochet

    show zvezdochet at left
    show goluboj at right

    zvezdochet "<{i}Такой же Голубой, как она, восходит на мост из темной аллеи. Также в снегу. Также прекрасен. Он колеблется, как тихое, синее пламя.{/i}>"

    hide goluboj

    show zvezdochet at truecenter

    hide zvezdochet

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "В блеске зимней ночи тающая,"

    goluboj "Обрати ко мне твой лик."

    goluboj "Ты, снегами тихо веющая,"

    goluboj "Подари мне легкий снег."

    hide goluboj

    show goluboj at truecenter

    goluboj "<{i}Она обращает очи к нему.{/i}>"

    show goluboj at truecenter

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Очи — звезды умирающие,"

    neznakomka "Уклонившись от пути."

    neznakomka "О тебе, мой легковеющий,"

    neznakomka "Я грустила в высоте."

    hide neznakomka

    show neznakomka at truecenter

    neznakomka "<{i}Его голубой плащ осыпан снежными звездами.{/i}>"

    show neznakomka at truecenter

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "В синеве твоей морозной"

    goluboj "Много звезд."

    goluboj "Под рукой моей железной"

    goluboj "Светлый меч."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Опусти в руке железной"

    neznakomka "Светлый меч."

    neznakomka "В синеве моей морозной"

    neznakomka "Звезд не счесть."

    hide neznakomka

    show neznakomka at left
    show goluboj at right

    neznakomka "<{i}Голубой дремлет в бледном свете. На фоне плаща его светится луч, как будто он оперся на меч.{/i}>"

    hide goluboj

    show neznakomka at truecenter

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Протекали столетья, как сны."

    goluboj "Долго ждал я тебя на земле."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Протекали столетья, как миги."

    neznakomka "Я звездою в пространствах текла."

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Ты мерцала с твоей высоты"

    goluboj "На моем голубом плаще."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты гляделся в мои глаза."

    neznakomka "Часто на́ небо смотришь ты?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Больше взора поднять не могу:"

    goluboj "Тобою, падучей, скован мой взор."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты можешь сказать мне земные слова?"

    neznakomka "Отчего ты весь в голубом?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Я слишком долго в небо смотрел:"

    goluboj "Оттого — голубые глаза и плащ."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Кто ты?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "{space=200}Поэт."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "{space=400}О чем ты поешь?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Все о тебе."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "{space=400}Давно ли ты ждешь?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Много столетий."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "{space=400}Ты мертв или жив?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Не знаю."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "{space=200}Ты юн?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "{space=400}Я красив."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Падучая дева-звезда"

    neznakomka "Хочет земных речей."

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Только о тайнах знаю слова,"

    goluboj "Только торжественны речи мои."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Знаешь ты имя мое?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Не знаю — и лучше не знать."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Видишь ты очи мои?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Вижу. Как звезды — они."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты видишь мой стройный стан?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Да. Ослепительна ты."

    hide goluboj

    show goluboj at truecenter

    goluboj "<{i}В голосе Ее просыпается земная страсть.{/i}>"

    show goluboj at truecenter

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты хочешь меня обнять?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    goluboj "Я коснуться не смею тебя."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты можешь коснуться уст."

    hide neznakomka

    show neznakomka at left
    show goluboj at right

    neznakomka "<{i}Плащ Голубого колеблется, исчезая под снегом.{/i}>"

    hide goluboj

    show neznakomka at truecenter

    hide neznakomka

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты знаешь ли страсть?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    hide goluboj

    show goluboj at truecenter

    goluboj "<{i}(тихо){/i}>"

    show goluboj at truecenter

    goluboj "Кровь молчалива моя."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты знаешь вино?"

    hide neznakomka

    show goluboj at truecenter

    $ goluboj_var = "{noalt}Голубой"

    hide goluboj

    show goluboj at truecenter

    goluboj "<{i}(еще тише){/i}>"

    show goluboj at truecenter

    goluboj "Звездный напиток — слаще вина."

    hide goluboj

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты любишь меня?"

    hide neznakomka

    show neznakomka at left
    show goluboj at right

    neznakomka "<{i}Голубой молчит.{/i}>"

    hide goluboj

    show neznakomka at truecenter

    hide neznakomka

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Кровь запевает во мне."

    hide neznakomka

    show neznakomka at truecenter

    neznakomka "<{i}Тишина.{/i}>"

    show neznakomka at truecenter

    hide neznakomka

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ядом исполнено сердце."

    neznakomka "Я стройнее всех ваших дев."

    neznakomka "Я красивее ваших дам."

    neznakomka "Я страстнее ваших невест."

    hide neznakomka

    show neznakomka at left
    show goluboj at right

    neznakomka "<{i}Голубой дремлет, весь осыпанный снегом.{/i}>"

    hide goluboj

    show neznakomka at truecenter

    neznakomka "Как сладко у вас на земле!"

    hide neznakomka

    show neznakomka at left
    show goluboj at right

    neznakomka "<{i}Голубого больше нет. Закрутился голубоватый снежный столб, и кажется, на этом месте и не было никого. Зато рядом с Незнакомкой проходящий господин приподнимает котелок.{/i}>"

    hide goluboj

    show neznakomka at truecenter

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "Вы с кем-то беседу вели?"

    gospodin "Но здесь не видать никого."

    gospodin "Прелестный ваш голос звучал"

    gospodin "В пространстве пустом..."

    hide gospodin

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "{space=400}Где он?"

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "О, да, без сомнения, вы"

    gospodin "Кого-то ждали сейчас!"

    gospodin "Позвольте — нескромный вопрос..."

    gospodin "Кто был ваш незримый друг?"

    hide gospodin

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Он был красив. В голубом плаще."

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "О, романтика женской души!"

    gospodin "И на улице видите вы"

    gospodin "Мужчин в голубых плащах!"

    gospodin "Но как же звали его?"

    hide gospodin

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Он назвал себя: поэт."

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "Я тоже поэт! я тоже поэт!"

    gospodin "По крайней мере, смотря"

    gospodin "В прекрасные ваши глаза,"

    gospodin "Я мог спеть вам куплет:"

    gospodin "«Ах, как ты хороша!»"

    hide gospodin

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты хочешь любить меня?"

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "О, да! И очень не прочь."

    hide gospodin

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Ты можешь обнять меня?"

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "Хотел бы знать, почему"

    gospodin "Не могу я тебя обнять?"

    hide gospodin

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "И, уст касаясь моих,"

    neznakomka "Ты будешь ласкать меня?"

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "Пойдем, красотка моя!"

    gospodin "«Исполню все, что велишь»,"

    gospodin "Как сказал старичок Шекспир..."

    gospodin "Ты видишь теперь, что и я"

    gospodin "Поэзии очень не чужд!"

    hide gospodin

    show gospodin at left
    show neznakomka at right

    gospodin "<{i}Незнакомка покорно дает ему руку.{/i}>"

    hide neznakomka

    show gospodin at truecenter

    hide gospodin

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "Как имя твое?"

    hide gospodin

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "{space=400}Постой."

    neznakomka "Дай вспомнить. В небе, средь звезд,"

    neznakomka "Не носила имени я..."

    neznakomka "Но здесь, на синей земле,"

    neznakomka "Мне нравится имя «Мария»..."

    neznakomka "«Мария» — зови меня."

    hide neznakomka

    show gospodin at truecenter

    $ gospodin_var = "{noalt}Господин"

    gospodin "Как хочешь, красотка моя."

    gospodin "Ведь мне лишь только бы знать,"

    gospodin "Что ночью тебе шептать."

    hide gospodin

    show gospodin at left
    show neznakomka at truecenter
    show zvezdochet at right

    gospodin "<{i}Уводит Незнакомку под руку. След их заметает голубой снег. Звездочет снова на мосту. Он — в тоске. Простирает руки в небо. Поднял взоры.{/i}>"

    hide neznakomka
    hide zvezdochet

    show gospodin at truecenter

    hide gospodin

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Нет больше прекрасной звезды!"

    zvezdochet "Синяя бездна пуста!"

    zvezdochet "Я ритмы утратил"

    zvezdochet "Астральных песен моих!"

    zvezdochet "Отныне режут мне слух"

    zvezdochet "Дребезжащие песни светил!"

    zvezdochet "Сегодня в башне моей"

    zvezdochet "Скорбной рукой занесу"

    zvezdochet "В длинные свитки мои"

    zvezdochet "Весть о паденьи светлейшей звезды..."

    zvezdochet "И тихо ее назову"

    zvezdochet "Именем дальним,"

    zvezdochet "Именем, нежащим слух:"

    zvezdochet "«Мария» — да будет имя ее."

    zvezdochet "В желтых свитках"

    zvezdochet "Начертано будет"

    zvezdochet "Моей одинокой рукой:"

    zvezdochet "«Пала Мария — звезда."

    zvezdochet "Больше не будет смотреть мне в глаза."

    zvezdochet "Звездочет остался один!»"

    play sound1 male_cry

    hide zvezdochet

    show zvezdochet at left
    show poet at right

    zvezdochet "<{i}Тихо плачет. Поэт поднимается на мост из аллеи.{/i}>"

    hide poet

    show zvezdochet at truecenter

    stop sound1

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "О, заклинаю вас всем святым!"

    poet "Вашей тоской!"

    poet "Вашей невестой, когда"

    poet "Есть невеста у вас!"

    poet "Скажите, была ли здесь"

    poet "Высокая женщина в черном?"

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Грубые люди! Оставьте меня."

    zvezdochet "Я женщин не вижу с тех пор,"

    zvezdochet "Как пала моя звезда."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Понятна мне ваша скорбь."

    poet "Я так же, как вы, одинок."

    poet "Вы, верно, как я, — поэт."

    poet "Случайно, не видели ль вы"

    poet "Незнакомку в снегах голубых?"

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Не помню. Здесь многие шли,"

    zvezdochet "И очень прискорбно мне,"

    zvezdochet "Что вашей не мог я узнать..."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "О, если б видели вы, —"

    poet "Забыли б свою звезду!"

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Не вам говорить о звездах;"

    zvezdochet "Чересчур легкомысленны вы,"

    zvezdochet "И я попросил бы вас"

    zvezdochet "В мою профессию нос не совать."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Все ваши обиды снесу!"

    poet "Поверьте, унижен я"

    poet "Ничуть не меньше, чем вы..."

    poet "О, если б я не был пьян,"

    poet "Я шел бы следом за ней!"

    poet "Но двое тащили меня,"

    poet "Когда я заметил ее..."

    poet "Потом я упал в сугроб,"

    poet "Они, ругаясь, ушли,"

    poet "Решившись бросить меня..."

    poet "Не помню, долго ль я спал..."

    poet "Проснувшись, вспомнил, что снег"

    poet "Замел ее нежный след!"

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Я смутно припомнить могу"

    zvezdochet "Печальную вещь для вас;"

    zvezdochet "Действительно, вас вели,"

    zvezdochet "Вам давали толчки и пинки,"

    zvezdochet "И был неуверен ваш шаг..."

    zvezdochet "Потом я помню сквозь сон,"

    zvezdochet "Как на мост дама взошла,"

    zvezdochet "И к ней подошел голубой господин..."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "О, нет!.. Голубой господин..."

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Не знаю, о чем говорили они."

    zvezdochet "Я больше на них не смотрел."

    zvezdochet "Потом они, верно, ушли..."

    zvezdochet "Я так был занят своим..."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "И снег замел их следы!.."

    poet "Мне больше не встретить Ее!"

    poet "Встречи такие"

    poet "Бывают в жизни лишь раз..."

    play sound1 male_cry

    hide poet

    show poet at truecenter

    poet "<{i}Оба плачут под голубым снегом.{/i}>"

    show poet at truecenter

    stop sound1

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Стоит ли плакать об этом?"

    zvezdochet "Гораздо глубже горе мое:"

    zvezdochet "Я утратил астральный ритм!"

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Я ритм души потерял."

    poet "Надеюсь, это — важней!"

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Скорбь занесет в мои свитки:"

    zvezdochet "«Пала звезда — Мария!»"

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Прекрасное имя: «Мария»!"

    poet "Я буду писать в стихах:"

    poet "«Где ты, Мария?"

    poet "Не вижу зари я»."

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Ну, ваше горе пройдет!"

    zvezdochet "Вам надо только стихи"

    zvezdochet "Как можно длинней сочинять!"

    zvezdochet "О чем же плакать тогда?"

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "А вам, господин звездочет,"

    poet "Довольно в свитки свои"

    poet "На пользу студентам вписать:"

    poet "«Пала Мария — Звезда!»"

    hide poet

    "<{i}Оба грустят под голубым снегом. Пропадают в нем. И снег грустит. Он запорошил уже и мост, и корабли. Он построил белые стены на канве деревьев, вдоль стен домов, на телеграфных проволоках.{/i}>"

    "<{i}И даль земная и даль речная поднялись белыми стенами, так что все бело, кроме сигнальных огней на кораблях и освещенных окон домов. Снежные стены уплотняются. Они кажутся близкими одна к другой. Понемногу открывается —{/i}>"


label Act_3:
    play music "audio/music/12.mp3" fadeout 1.0 fadein 1.0

    scene 6 with fade

    "{b}ТРЕТЬЕ ВИДЕНИЕ{/b}"

    play sound1 telephone

    "<{i}Большая гостиная комната с белыми стенами, на которых ярко горят электрические лампы. Дверь в переднюю открыта. Тоненький звонок часто извещает о приходе гостей. На диванах, креслах и стульях уже сидят хозяева и гости;{/i}>"

    stop sound1

    "<{i}хозяйка дома — пожилая дама, как бы проглотившая аршин; перед нею — корзинка с бисквитами, ваза с фруктами и чашка дымящегося чаю; против нее — глухой старик с глупым лицом жует и хлебает.{/i}>"

    show molodoj_chelovek at truecenter

    "<{i}Молодые люди, в безукоризненных смокингах, частью разговаривают с другими дамами, частью толпятся стадами в углах. Общий гул бессмысленных разговоров.{/i}>"

    hide molodoj_chelovek

    show hozjain_trete_videnie at truecenter

    "<{i}Хозяин дома встречает гостей в передней и каждому сначала деревянным голосом кричит: «А-а-а!», а потом говорит пошлость. В настоящий момент он занят тем же.{/i}>"

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at truecenter

    $ hozjain_trete_videnie_var = "{noalt}Хозяин дома"

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at truecenter

    hozjain_trete_videnie "<{i}(в передней){/i}>"

    show hozjain_trete_videnie at truecenter

    hozjain_trete_videnie "А-а-а! Ну и закутались же вы, батюшка!"

    hide hozjain_trete_videnie

    show gost at truecenter

    $ gost_var = "{noalt}Голос гостя"

    gost "И холод же, доложу я вам! В шубе — и то замерз."

    hide gost

    show gost at truecenter

    gost "<{i}Гость сморкается. Так как разговор в гостиной почему-то исчерпался, слышно, как хозяин конфиденциально говорит гостю:{/i}>"

    show gost at truecenter

    hide gost

    show hozjain_trete_videnie at truecenter

    $ hozjain_trete_videnie_var = "{noalt}Хозяин"

    hozjain_trete_videnie "А где шили?"

    hide hozjain_trete_videnie

    show gost at truecenter

    $ gost_var = "{noalt}Гость"

    gost "У Шевалье."

    hide gost

    show gost at left
    show hozjain_trete_videnie at right

    gost "<{i}Из двери торчат фалды хозяйского сюртука. Хозяин рассматривает шубу.{/i}>"

    hide hozjain_trete_videnie

    show gost at truecenter

    hide gost

    show hozjain_trete_videnie at truecenter

    $ hozjain_trete_videnie_var = "{noalt}Хозяин"

    hozjain_trete_videnie "А сколько платили?"

    hide hozjain_trete_videnie

    show gost at truecenter

    $ gost_var = "{noalt}Гость"

    gost "Тысячу."

    hide gost

    show gost at left
    show hozjajka at right

    gost "<{i}Хозяйка, стараясь замять разговор, кричит:{/i}>"

    hide hozjajka

    show gost at truecenter

    hide gost

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "{a=myshow|tooltip|text=Cher : Дорогой (франц.). – Ред.}Cher{/a} Иван Павлович! Идите скорее! Только вас и ждали! Вот, Аркадий Романович обещался нам сегодня спеть!"

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}Аркадий Романович, подходя к хозяйке, делает различные жесты, долженствующие показать, что он невысокого о себе мнения. Хозяйка жестами же старается показать ему обратное.{/i}>"

    show hozjajka at truecenter

    hide hozjajka

    show zhorzh at truecenter

    $ zhorzh_var = "{noalt}Молодой человек Жорж"

    zhorzh "Совершенная дура твоя Серпантини, Миша. Так танцевать, как она вчера, значит — не иметь никакого стыда."

    hide zhorzh

    show misha at truecenter

    $ misha_var = "{noalt}Молодой человек Миша"

    misha "Ты, Жорж, ровно ничего не понимаешь! Я совершенно влюблен. Это — для немногих. Вспомни, у нее совсем классическая фигура — руки, ноги..."

    hide misha

    show zhorzh at truecenter

    $ zhorzh_var = "{noalt}Жорж"

    zhorzh "Я пошел туда затем, чтобы наслаждаться искусством. На ножки я могу смотреть и в другом месте."

    hide zhorzh

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "О чем это вы там, Георгий Николаевич? Ах, о Серпантини! Какой ужас, не правда ли? Во-первых — интерпретировать музыку — это уж одно — наглость. Я так страстно люблю музыку и ни за что, ни за что не допущу, чтоб над ней надругались."

    hozjajka "Потом — танцевать без костюма — это... это я не знаю, что! Я увела мою дочь."

    hide hozjajka

    show zhorzh at truecenter

    $ zhorzh_var = "{noalt}Жорж"

    zhorzh "Я совершенно согласен с вами. А вот Михаил Иванович — другого мнения..."

    hide zhorzh

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "Что вы, Михаил Иванович! По-моему, здесь двух мнений не может быть! Я понимаю, молодые людям свойственно увлекаться, но на публичном концерте... когда ногами изображают Баха... Я сама музыкантша... страстно люблю музыку... Как хотите..."

    hide hozjajka

    show hozjajka at left
    show starik at right

    hozjajka "<{i}Старик, сидящий против хозяйки, неожиданно и просто выпаливает:{/i}>"

    hide starik

    show hozjajka at truecenter

    hide hozjajka

    show starik at truecenter

    $ starik_var = "{noalt}Старик"

    starik "Публичный дом."

    hide starik

    show starik at left
    show hozjajka at right

    starik "<{i}Продолжает хлебать чай и жевать бисквиты. Хозяйка краснеет и обращается к одной из дам.{/i}>"

    hide hozjajka

    show starik at truecenter

    hide starik

    show misha at truecenter

    $ misha_var = "{noalt}Миша"

    misha "Ах, Жорж, все вы ничего не понимаете! Разве это — интерпретация музыки? Серпантини сама — воплощение музыки. Она плывет на волнах звуков, и, кажется, сам плывешь за нею."

    misha "Неужели тело, его линии, его гармонические движения — сами по себе не поют так же, как звуки? Тот, кто истинно чувствует музыку, не оскорбляется за нее. У вас отвлеченное отношение к музыке..."

    hide misha

    show zhorzh at truecenter

    $ zhorzh_var = "{noalt}Жорж"

    zhorzh "Мечтатель! Завел машину. Строишь какие-то теории и ничего не слушаешь и не видишь. Я о музыке даже не говорю, и мне в конце концов наплевать! И я был бы очень рад видеть все это в отдельном кабинете."

    zhorzh "Но согласись же, не объявить на афише, что Серпантини будет завернута в одну тряпку, — это значит поставить всех в пренеловкое положение. Если б я знал, я не повел бы туда мою невесту."

    hide zhorzh

    show zhorzh at left
    show misha at right

    zhorzh "<{i}(Миша рассеянно шарит в корзинке с бисквитами.){/i}>"

    hide misha

    show zhorzh at truecenter

    zhorzh "Послушай, оставь бисквиты. Ведь противно есть, если все перетрогаешь. Смотри, как на тебя смотрит кузина. А все оттого, что ты рассеян. Эх, мечтатели."

    hide zhorzh

    show zhorzh at left
    show misha at right

    zhorzh "<{i}Миша, сконфуженно мыча, удаляется в другой угол.{/i}>"

    hide misha

    show zhorzh at truecenter

    hide zhorzh

    show starik at truecenter

    $ starik_var = "{noalt}Старик"

    hide starik

    show starik at truecenter

    starik "<{i}(внезапно, хозяйке){/i}>"

    show starik at truecenter

    starik "Нина! Сиди смирно. У тебя на спине платье расстегнулось."

    hide starik

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}(вспыхнув){/i}>"

    show hozjajka at truecenter

    hozjajka "Да полно, дядя, нельзя же при всех! Вы слишком... откровенны..."

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}Старается незаметно застегнуть платье. В комнату впархивает молодая дама, за ней идет огромный рыжий господин.{/i}>"

    show hozjajka at truecenter

    hide hozjajka

    show dama at truecenter

    $ dama_var = "{noalt}Дама"

    dama "Ах, здравствуйте, здравствуйте! Вот, позвольте вас познакомить: мой жених."

    hide dama

    show ryzhij_gospodin at truecenter

    $ ryzhij_gospodin_var = "{noalt}Рыжий господин"

    ryzhij_gospodin "Очень приятно."

    hide ryzhij_gospodin

    show ryzhij_gospodin at truecenter

    ryzhij_gospodin "<{i}Угрюмо удаляется в угол.{/i}>"

    show ryzhij_gospodin at truecenter

    hide ryzhij_gospodin

    show dama at truecenter

    $ dama_var = "{noalt}Дама"

    dama "Пожалуйста, не обращайте на него внимания. Он очень застенчив. Ах, представьте, какой случай!.."

    hide dama

    show dama at truecenter

    dama "<{i}Торопливо пьет чай и шопотом рассказывает хозяйке что-то пикантное, судя по тому, что обе ерзают по дивану и хихикают.{/i}>"

    show dama at truecenter

    hide dama

    show dama at truecenter

    $ dama_var = "{noalt}Дама"

    hide dama

    show dama at truecenter

    dama "<{i}(вдруг оборачивается к жениху){/i}>"

    show dama at truecenter

    dama "У тебя мой платок?"

    hide dama

    show dama at truecenter

    dama "<{i}Жених угрюмо вытаскивает платок.{/i}>"

    show dama at truecenter

    hide dama

    show dama at truecenter

    $ dama_var = "{noalt}Дама"

    dama "Тебе жалко, что ли?"

    hide dama

    show ryzhij_gospodin at truecenter

    $ ryzhij_gospodin_var = "{noalt}Рыжий господин"

    hide ryzhij_gospodin

    show ryzhij_gospodin at truecenter

    ryzhij_gospodin "<{i}(неожиданно угрюмо){/i}>"

    show ryzhij_gospodin at truecenter

    ryzhij_gospodin "Пей, да помалкивай."

    hide ryzhij_gospodin

    show ryzhij_gospodin at left
    show neznakomka at right

    ryzhij_gospodin "<{i}Молчат. Пьют. Вбегает молодой человек и радостно бросается к другому. В последнем легко узнать того, кто увел незнакомку.{/i}>"

    hide neznakomka

    show ryzhij_gospodin at truecenter

    hide ryzhij_gospodin

    show molodoj_chelovek at truecenter

    $ molodoj_chelovek_var = "{noalt}Молодой человек"

    molodoj_chelovek "Костя, друг, да она у дверей дожида..."

    hide molodoj_chelovek

    show molodoj_chelovek at left
    show poet at right

    molodoj_chelovek "<{i}Запинается на полуслове. Все становится необычайно странным. Как будто все внезапно вспомнили, что где-то произносились те же слова и в том же порядке. Михаил Иванович смотрит странными глазами на Поэта, который входит в эту минуту.{/i}>"

    hide poet

    show molodoj_chelovek at truecenter

    hide molodoj_chelovek

    show molodoj_chelovek at left
    show poet at right

    molodoj_chelovek "<{i}Поэт, бледный, делает общий поклон на пороге притихшей гостиной.{/i}>"

    hide poet

    show molodoj_chelovek at truecenter

    hide molodoj_chelovek

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}(с натянутым видом){/i}>"

    show hozjajka at truecenter

    hozjajka "Мы только вас и ждали. Надеюсь, вы прочтете нам что-нибудь. Сегодня престранный вечер! Наша мирная беседа не клеится."

    hide hozjajka

    show starik at truecenter

    $ starik_var = "{noalt}Старик"

    hide starik

    show starik at truecenter

    starik "<{i}(выпаливает){/i}>"

    show starik at truecenter

    starik "Точно кто-нибудь умер. Богу душу отдал."

    hide starik

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "Ах, дядя, перестаньте! Вы всех окончательно спугнете... Господа! Обновим наш разговор..."

    hide hozjajka

    show hozjajka at left
    show poet at right

    hozjajka "<{i}(Поэту.){/i}>"

    hide poet

    show hozjajka at truecenter

    hozjajka "Вы прочтете нам что-нибудь, не правда ли?"

    hide hozjajka

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "С удовольствием... если это займет..."

    hide poet

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "Господа! Молчание! Наш прекрасный поэт прочтет нам свое прекрасное стихотворение, и, надеюсь, опять о прекрасной даме..."

    hide hozjajka

    show hozjajka at left
    show poet at right

    hozjajka "<{i}Все замолкают. Поэт становится у стены, прямо против двери в переднюю, и читает:{/i}>"

    hide poet

    show hozjajka at truecenter

    hide hozjajka

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Уже сбегали с плит снега,"

    poet "Блестели, обнажаясь крыши,"

    poet "Когда в соборе, в темной нише,"

    poet "Ее блеснули жемчуга."

    poet "И от иконы в нежных розах"

    poet "Медлительно сошла Она..."

    play sound1 telephone

    hide poet

    show poet at left
    show hozjajka at right

    poet "<{i}Тоненький звонок в передней. Хозяйка умоляюще складывает руки по направлению к Поэту. Он прерывает чтение. Все с любопытством заглядывают в переднюю.{/i}>"

    hide hozjajka

    show poet at truecenter

    stop sound1

    hide poet

    show hozjain_trete_videnie at truecenter

    $ hozjain_trete_videnie_var = "{noalt}Хозяин"

    hozjain_trete_videnie "Сию минуту. Прошу извинения."

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at truecenter

    hozjain_trete_videnie "<{i}Выходит в переднюю, но не кричит там: «А-а-а!» Молчание.{/i}>"

    show hozjain_trete_videnie at truecenter

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at truecenter

    $ hozjain_trete_videnie_var = "{noalt}Голос хозяина"

    hozjain_trete_videnie "Чем могу служить?"

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at truecenter

    hozjain_trete_videnie "<{i}Женский голос отвечает что-то. Хозяин появляется на пороге.{/i}>"

    show hozjain_trete_videnie at truecenter

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at truecenter

    $ hozjain_trete_videnie_var = "{noalt}Хозяин"

    hozjain_trete_videnie "Ниночка, какая-то дама. Ничего не могу разобрать. Вероятно, к тебе. Извините, господа, извините..."

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at left
    show hozjajka at truecenter
    show gost at right

    hozjain_trete_videnie "<{i}Сконфуженно улыбается во все стороны. Хозяйка идет в переднюю и запирает за собой дверь. Гости шепчутся.{/i}>"

    hide hozjajka
    hide gost

    show hozjain_trete_videnie at truecenter

    hide hozjain_trete_videnie

    show molodoj_chelovek at truecenter

    $ molodoj_chelovek_var = "{noalt}Молодой человек "

    hide molodoj_chelovek

    show molodoj_chelovek at truecenter

    molodoj_chelovek "<{i}(в углу){/i}>"

    show molodoj_chelovek at truecenter

    molodoj_chelovek "Да не может быть..."

    hide molodoj_chelovek

    show drugoj_trete_videnie at truecenter

    $ drugoj_trete_videnie_var = "{noalt}Другой"

    hide drugoj_trete_videnie

    show drugoj_trete_videnie at truecenter

    drugoj_trete_videnie "<{i}(прячась за него){/i}>"

    show drugoj_trete_videnie at truecenter

    drugoj_trete_videnie "Да уверяю тебя... вот скандал!.. Я слышал ее голос..."

    hide drugoj_trete_videnie

    show poet at left
    show hozjajka at truecenter
    show neznakomka at right

    drugoj_trete_videnie "<{i}Поэт стоит неподвижно против дверей. Двери открываются. Хозяйка вводит Незнакомку.{/i}>"

    hide poet
    hide hozjajka
    hide neznakomka

    show drugoj_trete_videnie at truecenter

    hide drugoj_trete_videnie

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "Господа, приятный сюрприз. Моя очаровательная новая знакомая. Надеюсь, мы примем ее с радостью в наш дружеский кружок. Мария... извините, я не расслышала, как вас называть?"

    hide hozjajka

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Мария."

    hide neznakomka

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "Но... ваше отчество?"

    hide hozjajka

    show neznakomka at truecenter

    $ neznakomka_var = "{noalt}Незнакомка"

    neznakomka "Мария. Я зову себя: Мария."

    hide neznakomka

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "Хорошо, милочка. Я буду звать вас: Мэри. В вас есть некоторая эксцентричность, не правда ли? Но тем веселее мы проведем сегодняшний вечер с нашей восхитительной гостьей. Не правда ли, господа?"

    hide hozjajka

    show hozjajka at left
    show hozjain_trete_videnie at truecenter
    show poet at right

    hozjajka "<{i}Все сконфужены. Неловкое молчание. Хозяин замечает, что один из гостей проскользнул в переднюю, и выходит за ним. Слышен извиняющийся шопот, слова: «не совсем здоров». Поэт стоит неподвижно.{/i}>"

    hide hozjain_trete_videnie
    hide poet

    show hozjajka at truecenter

    hide hozjajka

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hozjajka "Итак, может быть, наш прекрасный поэт продолжит прерванное чтение? Дорогая Мэри, когда вы вошли, наш известный поэт как раз читал нам... читал нам."

    hide hozjajka

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Простите. Позвольте мне прочесть в другой раз. Я так извиняюсь."

    hide poet

    show poet at left
    show neznakomka at right

    "<{i}Никто не выражает неудовольствия. Поэт подходит к хозяйке, которая некоторое время делает умоляющие жесты, но скоро перестает. Поэт спокойно садится в дальний угол. Задумчиво смотрит на Незнакомку. Горничная разносит, что полагается.{/i}>"

    hide poet
    hide neznakomka

    play sound1 female_laughter

    "<{i}Из общего бессмысленного говора вырывается хохот, отдельные слова и целые фразы:{/i}>"

    stop sound1

    show raznye_golosa at truecenter

    $ raznye_golosa_var = "{noalt}Разные голоса"

    raznye_golosa "Нет, как она танцевала! Да ты послушай! Русская интеллигенция..."

    hide raznye_golosa

    show kto_to at truecenter

    $ kto_to_var = "{noalt}Кто-то"

    hide kto_to

    show kto_to at truecenter

    kto_to "<{i}(особенно громко){/i}>"

    show kto_to at truecenter

    kto_to "Да и вам не поймать! Да и вам не поймать!"

    hide kto_to

    show kto_to at left
    show poet at right

    kto_to "<{i}Все забыли о Поэте. Он медленно поднимается со своего места. Он проводит рукою по лбу. Делает несколько шагов взад и вперед по комнате. По лицу его заметно, что он с мучительным усилием припоминает что-то.{/i}>"

    hide poet

    show kto_to at truecenter

    hide kto_to

    show kto_to at truecenter

    kto_to "<{i}В это время из общего говора доносятся слова: «рокфор», «камамбер». Вдруг толстый человек, в страшном увлечении, делая кругообразные жесты, выскакивает на середину комнаты с криком:{/i}>"

    show kto_to at truecenter

    kto_to "Бри!"

    hide kto_to

    show poet at left
    show neznakomka at truecenter
    show zvezdochet at right

    kto_to "<{i}Поэт сразу останавливается. Мгновение кажется, что он вспомнил все. Он делает несколько быстрых шагов в сторону Незнакомки. Но дорогу ему заслоняет Звездочет в голубом вицмундире, входящий из передней.{/i}>"

    hide poet
    hide neznakomka
    hide zvezdochet

    show kto_to at truecenter

    hide kto_to

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Извините, я в вицмундире и запоздал. Прямо из заседания. Пришлось делать доклад. Астрономия..."

    hide zvezdochet

    show zvezdochet at truecenter

    zvezdochet "<{i}Поднимает палец кверху.{/i}>"

    show zvezdochet at truecenter

    hide zvezdochet

    show hozjain_trete_videnie at truecenter

    $ hozjain_trete_videnie_var = "{noalt}Хозяин"

    hide hozjain_trete_videnie

    show hozjain_trete_videnie at truecenter

    hozjain_trete_videnie "<{i}(подходя){/i}>"

    show hozjain_trete_videnie at truecenter

    hozjain_trete_videnie "Вот и мы только что говорили о гастрономии. Ниночка, не пора ли ужинать?"

    hide hozjain_trete_videnie

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}(встает){/i}>"

    show hozjajka at truecenter

    hozjajka "Господа, прошу вас!"

    hide hozjajka

    show neznakomka at left
    show zvezdochet at truecenter
    show poet at right

    hozjajka "<{i}Все выходят вслед за нею. В потемневшей гостиной остаются некоторое время Незнакомка, Звездочет и Поэт. Поэт и Звездочет стоят в дверях, готовые выйти. Незнакомка медлит в глубине у темной полуоткрытой занавеси окна.{/i}>"

    hide neznakomka
    hide zvezdochet
    hide poet

    show hozjajka at truecenter

    hide hozjajka

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Нам опять привелось встретиться с вами. Я очень рад. Но пусть обстоятельства нашей первой встречи останутся между нами."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Прошу о том же и вас."

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    zvezdochet "Я только что сделал доклад в астрономическом обществе — о том, чему вы были невольным свидетелем. Поразительный факт: звезда первой величины..."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Да, это очень интересно."

    hide poet

    show zvezdochet at truecenter

    $ zvezdochet_var = "{noalt}Звездочет"

    hide zvezdochet

    show zvezdochet at truecenter

    zvezdochet "<{i}(восторженно){/i}>"

    show zvezdochet at truecenter

    zvezdochet "Да! Я занес в мои списки новый параграф: «Пала звезда Мария!» Наука в первый раз... Ах, извините, что я не спрашиваю вас о результатах ваших поисков..."

    hide zvezdochet

    show poet at truecenter

    $ poet_var = "{noalt}Поэт"

    poet "Поиски мои были безрезультатны."

    hide poet

    show poet at truecenter

    poet "<{i}Он оборачивается в глубь комнаты. Безнадежно смотрит. На лице его — томление, в глазах — пустота и мрак. Он шатается от страшного напряжения. Но он все забыл.{/i}>"

    show poet at truecenter

    hide poet

    show hozjajka at truecenter

    $ hozjajka_var = "{noalt}Хозяйка"

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}(на пороге){/i}>"

    show hozjajka at truecenter

    hozjajka "Господа! Идите же в столовую! Я не вижу Мэри..."

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}Грозит им пальцем.{/i}>"

    show hozjajka at truecenter

    hozjajka "Ах, молодые люди! Вы спрятали куда-нибудь мою Мэри?"

    hide hozjajka

    show hozjajka at truecenter

    hozjajka "<{i}Всматривается в глубь комнаты.{/i}>"

    show hozjajka at truecenter

    hozjajka "Где же Мэри? Да где же Мэри?"

    hide hozjajka

    play sound1 punch

    show zvezdochet at truecenter

    "<{i}У темной занавеси уже нет никого. За окном горит яркая звезда. Падает голубой снег, такой же голубой, как вицмундир исчезнувшего Звездочета.{/i}>"

    hide zvezdochet

    stop sound1

    "<{i}〈1906〉{/i}>"



