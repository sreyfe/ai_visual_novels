"In the public domain."

"А. П. Чехов. Полное собрание сочинений и писем в 30-ти томах. Сочинения. Том 12. М., \"Наука\", 1986."

define jat = Character("jat_var", color="#FFB300", dynamic=True)
define shafer = Character("shafer_var", color="#803E75", dynamic=True)
define aplombov = Character("aplombov_var", color="#FF6800", dynamic=True)
define lakej = Character("lakej_var", color="#A6BDD7", dynamic=True)
define zhigalov = Character("zhigalov_var", color="#C10020", dynamic=True)
define dymba = Character("dymba_var", color="#CEA262", dynamic=True)
define kavalery = Character("kavalery_var", color="#817066", dynamic=True)
define njunin = Character("njunin_var", color="#007D34", dynamic=True)
define mozgovoj = Character("mozgovoj_var", color="#F6768E", dynamic=True)
define revunov = Character("revunov_var", color="#00538A", dynamic=True)
define zmejukina = Character("zmejukina_var", color="#FF7A5C", dynamic=True)
define nastasjatimofeevna = Character("nastasjatimofeevna_var", color="#53377A", dynamic=True)
define dashenka = Character("dashenka_var", color="#FF8E00", dynamic=True)

label start:
    play music "audio/music/6.mp3" fadeout 1.0 fadein 1.0

    scene 1 with fade

    "Свадьба"

    "Сцена в одном действии"

    "Действие происходит в одной из зал кухмистера Андронова."

    menu:
        "{color=#000}ДЕЙСТВУЮЩИЕ ЛИЦА{/color}":
            jump Characters
        "{color=#000}act_1{/color}":
            jump Act_1

    label Characters:
        play music "audio/music/3.mp3" fadeout 1.0 fadein 1.0

        scene 3 with fade

        "{b}ДЕЙСТВУЮЩИЕ ЛИЦА{/b}"

        show zhigalov at truecenter
        "Евдоким Захарович Жигалов, отставной коллежский регистратор."
        hide zhigalov

        show nastasjatimofeevna at truecenter
        "Настасья Тимофеевна, его жена."
        hide nastasjatimofeevna

        show dashenka at truecenter
        "Дашенька, их дочь."
        hide dashenka

        show aplombov at truecenter
        "Эпаминонд Максимович Апломбов, ее жених."
        hide aplombov

        show revunov at truecenter
        "Федор Яковлевич Ревунов-Караулов, капитан 2-го ранга в отставке."
        hide revunov

        show njunin at truecenter
        "Андрей Андреевич Нюнин, агент страхового общества."
        hide njunin

        show zmejukina at truecenter
        "Анна Мартыновна Змеюкина, акушерка 30 лет, в ярко-пунцовом платье."
        hide zmejukina

        show jat at truecenter
        "Иван Михайлович Ять, телеграфист."
        hide jat

        show dymba at truecenter
        "Харлампий Спиридонович Дымба, грек-кондитер."
        hide dymba

        show mozgovoj at truecenter
        "Дмитрий Степанович Мозговой, матрос из Добровольного флота."
        hide mozgovoj

        "Шафера, кавалеры, лакеи и проч."


label Act_1:
    play music "audio/music/9.mp3" fadeout 1.0 fadein 1.0

    scene 6 with fade

    "{b}act_1{/b}"

    show lakej at truecenter

    show lakej at truecenter

    "<{i}Ярко освещенная зала. Большой стол, накрытый для ужина. Около стола хлопочут лакеи во фраках. За сценой музыка играет последнюю фигуру кадрили.{/i}>"

    hide lakej

    hide lakej

    menu:
        "{color=#000}configuration_1{/color}":
            jump Act_1_Scene_1
        "{color=#000}configuration_2{/color}":
            jump Act_1_Scene_2
        "{color=#000}configuration_3{/color}":
            jump Act_1_Scene_3
        "{color=#000}configuration_4{/color}":
            jump Act_1_Scene_4
        "{color=#000}configuration_5{/color}":
            jump Act_1_Scene_5
        "{color=#000}configuration_6{/color}":
            jump Act_1_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_1_Scene_6_1

label Further_Act_1_Scene_6_1:
    menu:
        "{color=#000}configuration_7{/color}":
            jump Act_1_Scene_7
        "{color=#000}configuration_8{/color}":
            jump Act_1_Scene_8
        "{color=#000}configuration_9{/color}":
            jump Act_1_Scene_9

    label Act_1_Scene_1:
        "{b}configuration_1{/b}"

        show zmejukina at left
        show jat at truecenter
        show shafer at right

        show zmejukina at left
        show jat at truecenter
        show shafer at right

        "<{i}Змеюкина, Ять и шафер (идут через сцену).{/i}>"

        hide zmejukina
        hide jat
        hide shafer

        hide zmejukina
        hide jat
        hide shafer

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Нет, нет, нет!"

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять"

        hide jat

        show jat at truecenter

        hide jat

        show jat at truecenter

        jat "<{i}(идя за ней).{/i}>"

        show jat at truecenter

        show jat at truecenter

        jat "Сжальтесь! Сжальтесь!"

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Нет, нет, нет!"

        hide zmejukina

        show shafer at truecenter

        $ shafer_var = "{noalt}Шафер"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(спеша за ними).{/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "Господа, так нельзя! Куда же вы? А гран-рон? Гран-рон, силь-ву-пле!"

        hide shafer

        show nastasjatimofeevna at left
        show aplombov at right

        show nastasjatimofeevna at left
        show aplombov at right

        "<{i}Уходят. Входят Настасья Тимофеевна и Апломбов.{/i}>"

        hide nastasjatimofeevna
        hide aplombov

        hide nastasjatimofeevna
        hide aplombov

    label Act_1_Scene_2:
        "{b}configuration_2{/b}"

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Чем тревожить меня разными словами, вы бы лучше шли танцевать."

        hide nastasjatimofeevna

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Я не Спиноза какой-нибудь, чтоб выделывать ногами кренделя. Я человек положительный и с характером и не вижу никакого развлечения в пустых удовольствиях. Но дело не в танцах. Простите, maman, но я многого не понимаю в ваших поступках. Например,"

        aplombov "кроме предметов домашней необходимости, вы обещали также дать мне за вашей дочерью два выигрышных билета. Где они?"

        hide aplombov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Голова у меня что-то разболелась... Должно, к непогоде... Быть оттепели!"

        hide nastasjatimofeevna

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Вы мне зубов не заговаривайте. Сегодня же я узнал, что ваши билеты в залоге. Извините, maman, но так поступают одни только эксплоататоры. Я ведь это не из эгоистицизма — мне ваши билеты не нужны, но я из принципа, и надувать себя никому не позволю."

        aplombov "Я вашу дочь осчастливил, и если вы мне не отдадите сегодня билетов, то я вашу дочь с кашей съем. Я человек благородный!"

        hide aplombov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна"

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(оглядывая стол и считая приборы).{/i}>"

        show nastasjatimofeevna at truecenter

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "Раз, два, три, четыре, пять..."

        hide nastasjatimofeevna

        show lakej at truecenter

        $ lakej_var = "{noalt}Лакей."

        lakej "Повар спрашивает, как прикажете подавать мороженое: с ромом, с мадерой или без никого?"

        hide lakej

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "С ромом. Да скажи хозяину, что вина мало. Скажи, чтоб еще го-сотерну поставил."

        hide aplombov

        show aplombov at left
        show nastasjatimofeevna at right

        hide aplombov

        show aplombov at left
        show nastasjatimofeevna at right

        aplombov "<{i}(Настасье Тимофеевне.){/i}>"

        hide nastasjatimofeevna

        show aplombov at truecenter

        hide nastasjatimofeevna

        show aplombov at truecenter

        aplombov "Вы также обещали, и уговор такой был, что сегодня за ужином будет генерал. А где он, спрашивается?"

        hide aplombov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Это, батюшка, не я виновата."

        hide nastasjatimofeevna

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Кто же?"

        hide aplombov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Андрей Андреич виноват... Вчерась он был и обещал привесть самого настоящего генерала."

        play sound1 female_sigh

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        play sound1 female_sigh

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(Вздыхает.){/i}>"

        show nastasjatimofeevna at truecenter

        stop sound1

        show nastasjatimofeevna at truecenter

        stop sound1

        nastasjatimofeevna "Должно, не нашел нигде, а то привел бы... Нешто нам жалко? Для родного дитя мы ничего не пожалеем. Генерал так генерал..."

        hide nastasjatimofeevna

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Но дальше... Всем, в том числе и вам, maman, известно, что за Дашенькой, пока я не сделал ей предложения, ухаживал этот телеграфист Ять. Зачем вы его пригласили? Разве вы не знали, что мне это неприятно?"

        hide aplombov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Ох, как тебя? — Эпаминонд Максимыч, еще и дня нет, как женился, а уж замучил ты и меня, и Дашеньку своими разговорами. А что будет через год? Нудный ты, ух нудный!"

        hide nastasjatimofeevna

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Не нравится правду слушать? Ага! То-то! А вы поступайте благородно. Я от вас хочу только одного: будьте благородны!"

        hide aplombov

    label Act_1_Scene_3:
        "{b}configuration_3{/b}"

        show dashenka at left
        show jat at truecenter
        show zmejukina at right

        show dashenka at left
        show jat at truecenter
        show zmejukina at right

        "<{i}Через залу из одной двери в другую проходят пары танцующих grand-rond. В передней паре шафер с Дашенькой, в задней Ять со Змеюкиной. Последняя пара отстает и остается в зале.{/i}>"

        hide shafer
        hide dashenka
        hide jat
        hide zmejukina

        hide shafer
        hide dashenka
        hide jat
        hide zmejukina

        show zhigalov at left
        show dymba at right

        show zhigalov at left
        show dymba at right

        "<{i}Жигалов и Дымба входят и идут к столу.{/i}>"

        hide zhigalov
        hide dymba

        hide zhigalov
        hide dymba

        show shafer at truecenter

        $ shafer_var = "{noalt}Шафер"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(кричит).{/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "Променад! Мсье, променад!"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(За сценой.){/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "Променад!"

        hide shafer

        "<{i}Пары уходят.{/i}>"

    label Act_1_Scene_4:
        "{b}configuration_4{/b}"

        show jat at truecenter

        $ jat_var = "{noalt}Ять"

        hide jat

        show jat at left
        show zmejukina at right

        hide jat

        show jat at left
        show zmejukina at right

        jat "<{i}(Змеюкиной).{/i}>"

        hide zmejukina

        show jat at truecenter

        hide zmejukina

        show jat at truecenter

        jat "Сжальтесь! Сжальтесь, очаровательная Анна Мартыновна!"

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Ах, какой вы... Я уже вам сказала, что я сегодня не в голосе."

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Умоляю вас, спойте! Одну только ноту! Сжальтесь! Одну только ноту!"

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Надоели..."

        hide zmejukina

        show zmejukina at truecenter

        hide zmejukina

        show zmejukina at truecenter

        zmejukina "<{i}(Садится и машет веером.){/i}>"

        show zmejukina at truecenter

        show zmejukina at truecenter

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Нет, вы просто безжалостны! У такого жестокого создания, позвольте вам выразиться, и такой чудный, чудный голос! С таким голосом, извините за выражение, не акушерством заниматься, а концерты петь в публичных собраниях! Например,"

        jat "как божественно выходит у вас вот эта фиоритура... вот эта..."

        hide jat

        show jat at truecenter

        hide jat

        show jat at truecenter

        jat "<{i}(Напевает.){/i}>"

        show jat at truecenter

        show jat at truecenter

        jat "«Я вас любил, любовь еще напрасно...» Чудно!"

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина"

        hide zmejukina

        show zmejukina at truecenter

        hide zmejukina

        show zmejukina at truecenter

        zmejukina "<{i}(напевает).{/i}>"

        show zmejukina at truecenter

        show zmejukina at truecenter

        zmejukina "«Я вас любил, любовь еще, быть может...» Это?"

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Вот это самое! Чудно!"

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Нет, я не в голосе сегодня. Нате, махайте на меня веером... Жарко!"

        hide zmejukina

        show zmejukina at left
        show aplombov at right

        hide zmejukina

        show zmejukina at left
        show aplombov at right

        zmejukina "<{i}(Апломбову.){/i}>"

        hide aplombov

        show zmejukina at truecenter

        hide aplombov

        show zmejukina at truecenter

        zmejukina "Эпаминонд Максимыч, что это вы в меланхолии? Разве жениху можно так? Как вам не стыдно, противный? Ну, о чем вы задумались?"

        hide zmejukina

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Женитьба шаг серьезный! Надо все обдумать всесторонне, обстоятельно."

        hide aplombov

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Какие вы все противные скептики! Возле вас я задыхаюсь... Дайте мне атмосферы! Слышите? Дайте мне атмосферы!"

        hide zmejukina

        show zmejukina at truecenter

        hide zmejukina

        show zmejukina at truecenter

        zmejukina "<{i}(Напевает.){/i}>"

        show zmejukina at truecenter

        show zmejukina at truecenter

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Чудно! Чудно!"

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Махайте на меня, махайте, а то я чувствую, у меня сейчас будет разрыв сердца. Скажите, пожалуйста, отчего мне так душно?"

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Это оттого, что вы вспотели-с..."

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Фуй, как вы вульгарны! Не смейте так выражаться!"

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Виноват! Конечно, вы привыкли, извините за выражение, к аристократическому обществу и..."

        hide jat

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Ах, оставьте меня в покое! Дайте мне поэзии, восторгов! Махайте, махайте..."

        hide zmejukina

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов"

        hide zhigalov

        show zhigalov at truecenter

        hide zhigalov

        show zhigalov at truecenter

        zhigalov "<{i}(Дымбе).{/i}>"

        show zhigalov at truecenter

        show zhigalov at truecenter

        zhigalov "Повторим, что ли?"

        hide zhigalov

        show zhigalov at truecenter

        hide zhigalov

        show zhigalov at truecenter

        zhigalov "<{i}(Наливает.){/i}>"

        show zhigalov at truecenter

        show zhigalov at truecenter

        zhigalov "Пить во всякую минуту можно. Главное действие, Харлампий Спиридоныч, чтоб дело свое не забывать. Пей, да дело разумей... А ежели насчет выпить, то почему не выпить? Выпить можно... За ваше здоровье!"

        hide zhigalov

        show zhigalov at truecenter

        hide zhigalov

        show zhigalov at truecenter

        zhigalov "<{i}Пьют.{/i}>"

        show zhigalov at truecenter

        show zhigalov at truecenter

        zhigalov "А тигры у вас в Греции есть?"

        hide zhigalov

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба."

        dymba "Есть."

        hide dymba

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "А львы?"

        hide zhigalov

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба."

        dymba "И львы есть. Это в России ницего нету, а в Греции все есть. Там у меня и отец, и дядя, и братья, а тут ницего нету."

        hide dymba

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "Гм... А кашалоты в Греции есть?"

        hide zhigalov

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба."

        dymba "Все есть."

        hide dymba

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна"

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(мужу).{/i}>"

        show nastasjatimofeevna at truecenter

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "Что ж зря-то пить и закусывать? Пора бы уж всем садиться. Не тыкай вилкой в омары... Это для генерала поставлено. Может, еще придет..."

        hide nastasjatimofeevna

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "А омары в Греции есть?"

        hide zhigalov

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба."

        dymba "Есть... Там все есть."

        hide dymba

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "Гм... А коллежские регистраторы есть?"

        hide zhigalov

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Воображаю, какая в Греции атмосфера!"

        hide zmejukina

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "И, должно быть, жульничества много. Греки ведь все равно, что армяне или цыганы. Продает тебе губку или золотую рыбку, а сам так и норовит, чтоб содрать с тебя лишнее. Повторим, что ли?"

        hide zhigalov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Что ж зря повторять? Всем бы уж пора садиться. Двенадцатый час..."

        hide nastasjatimofeevna

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "Садиться так садиться. Господа, покорнейше прошу! Пожалуйте!"

        hide zhigalov

        show zhigalov at truecenter

        hide zhigalov

        show zhigalov at truecenter

        zhigalov "<{i}(Кричит.){/i}>"

        show zhigalov at truecenter

        show zhigalov at truecenter

        zhigalov "Ужинать! Молодые люди!"

        hide zhigalov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Дорогие гости, милости просим! Садитесь!"

        hide nastasjatimofeevna

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина"

        hide zmejukina

        show zmejukina at truecenter

        hide zmejukina

        show zmejukina at truecenter

        zmejukina "<{i}(садясь за стол).{/i}>"

        show zmejukina at truecenter

        show zmejukina at truecenter

        zmejukina "Дайте мне поэзии! А он, мятежный, ищет бури, как будто в бурях есть покой. Дайте мне бурю!"

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять"

        hide jat

        show jat at truecenter

        hide jat

        show jat at truecenter

        jat "<{i}(в сторону).{/i}>"

        show jat at truecenter

        show jat at truecenter

        jat "Замечательная женщина! Влюблен! По уши влюблен!"

        hide jat

    label Act_1_Scene_5:
        "{b}configuration_5{/b}"

        show mozgovoj at left
        show shafer at truecenter
        show kavalery at right

        show mozgovoj at left
        show shafer at truecenter
        show kavalery at right

        "<{i}Входят Дашенька, Мозговой, шафера, кавалеры, барышни и проч. Все шумно усаживаются за стол; минутная пауза; музыка играет марш.{/i}>"

        hide dashenka
        hide mozgovoj
        hide shafer
        hide kavalery

        hide dashenka
        hide mozgovoj
        hide shafer
        hide kavalery

        show mozgovoj at truecenter

        $ mozgovoj_var = "{noalt}Мозговой"

        hide mozgovoj

        show mozgovoj at truecenter

        hide mozgovoj

        show mozgovoj at truecenter

        mozgovoj "<{i}(вставая).{/i}>"

        show mozgovoj at truecenter

        show mozgovoj at truecenter

        mozgovoj "Господа! Я должен сказать вам следующее... У нас приготовлено очень много тостов и речей. Не будем дожидаться и начнем сейчас же. Господа, предлагаю выпить тост за новобрачных!"

        hide mozgovoj

        "<{i}Музыка играет туш. Ура. Чоканье.{/i}>"

        show mozgovoj at truecenter

        $ mozgovoj_var = "{noalt}Мозговой."

        mozgovoj "Горько! Все. Горько! Горько!"

        hide mozgovoj

        show aplombov at left
        show dashenka at right

        show aplombov at left
        show dashenka at right

        "<{i}Апломбов и Дашенька целуются.{/i}>"

        hide aplombov
        hide dashenka

        hide aplombov
        hide dashenka

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Чудно! Чудно! Я должен вам выразиться, господа, и отдать должную справедливость, что эта зала и вообще помещение великолепны! Превосходно, очаровательно! Только знаете, чего не хватает для полного торжества? Электрического освещения, извините за выражение!"

        jat "Во всех странах уже введено электрическое освещение, и одна только Россия отстала."

        hide jat

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов"

        hide zhigalov

        show zhigalov at truecenter

        hide zhigalov

        show zhigalov at truecenter

        zhigalov "<{i}(глубокомысленно).{/i}>"

        show zhigalov at truecenter

        show zhigalov at truecenter

        zhigalov "Электричество... Гм... А по моему взгляду, электрическое освещение — одно только жульничество... Всунут туда уголек, да и думают глаза отвести! Нет, брат, уж если ты даешь освещение, то ты давай не уголек, а что-нибудь существенное, этакое что-нибудь особенное,"

        zhigalov "чтоб было за что взяться! Ты давай огня — понимаешь? — огня, который натуральный, а не умственный!"

        hide zhigalov

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Если бы вы видели электрическую батарею, из чего она составлена, то иначе бы рассуждали."

        hide jat

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "И не желаю видеть. Жульничество. Народ простой надувают... Соки последние выжимают... Знаем их, этих самых... А вы, господин молодой человек, чем за жульничество заступаться, лучше бы выпили и другим налили. Да право!"

        hide zhigalov

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Я с вами, папаша, вполне согласен. К чему заводить ученые разговоры? Я не прочь и сам поговорить о всевозможных открытиях в научном смысле, но ведь на это есть другое время!"

        hide aplombov

        show aplombov at left
        show dashenka at right

        hide aplombov

        show aplombov at left
        show dashenka at right

        aplombov "<{i}(Дашеньке.){/i}>"

        hide dashenka

        show aplombov at truecenter

        hide dashenka

        show aplombov at truecenter

        aplombov "Ты какого мнения, машер"

        hide aplombov

        show dashenka at truecenter

        $ dashenka_var = "{noalt}Дашенька."

        dashenka "Они хочут свою образованность показать и всегда говорят о непонятном."

        hide dashenka

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Слава богу, прожили век без образования и вот уж третью дочку за хорошего человека выдаем. А ежели мы, по-вашему, выходит необразованные, так зачем вы к нам ходите? Шли бы к своим образованным!"

        hide nastasjatimofeevna

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Я, Настасья Тимофеевна, всегда уважал ваше семейство, а ежели я насчет электрического освещения, так это еще не значит, что я из гордости. Даже вот выпить могу. Я всегда от всех чувств желал Дарье Евдокимовне хорошего жениха. В наше время, Настасья Тимофеевна,"

        jat "трудно выйти за хорошего человека. Нынче каждый норовит вступить в брак из-за интереса, из-за денег..."

        hide jat

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Это намек!"

        hide aplombov

        show jat at truecenter

        $ jat_var = "{noalt}Ять"

        hide jat

        show jat at truecenter

        hide jat

        show jat at truecenter

        jat "<{i}(струсив).{/i}>"

        show jat at truecenter

        show jat at truecenter

        jat "И никакого тут нет намека... Я не говорю о присутствующих... Это я так... вообще... Помилуйте! Все знают, что вы из-за любви... Приданое пустяшное."

        hide jat

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Нет, не пустяшное! Ты говори, сударь, да не заговаривайся. Кроме того, что тысячу рублей чистыми деньгами, мы три салопа даем, постель и всю мебель. Подика-сь, найди в другом месте такое приданое!"

        hide nastasjatimofeevna

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Я ничего... Мебель, действительно, хорошая и... и салопы, конечно, но я в том смысле, что вот они обижаются, что я намекнул."

        hide jat

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "А вы не намекайте. Мы вас по вашим родителям почитаем и на свадьбу пригласили, а вы разные слова. А ежели вы знали, что Эпаминонд Максимыч из интересу женится, то что же вы раньше молчали?"

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(Слезливо.){/i}>"

        show nastasjatimofeevna at truecenter

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "Я ее, может, вскормила, вспоила, взлелеяла... берегла пуще алмаза изумрудного, деточку мою..."

        hide nastasjatimofeevna

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "И вы поверили? Покорнейше вас благодарю! Очень вам благодарен!"

        hide aplombov

        show aplombov at left
        show jat at right

        hide aplombov

        show aplombov at left
        show jat at right

        aplombov "<{i}(Ятю.){/i}>"

        hide jat

        show aplombov at truecenter

        hide jat

        show aplombov at truecenter

        aplombov "А вы, господин Ять, хоть и знакомый мне, а я вам не позволю строить в чужом доме такие безобразия! Позвольте вам выйти вон!"

        hide aplombov

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "То есть как?"

        hide jat

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Желаю, чтобы и вы были таким же честным человеком, как я! Одним словом, позвольте вам выйти вон!"

        hide aplombov

        "<{i}Музыка играет туш.{/i}>"

        show kavalery at truecenter

        $ kavalery_var = "{noalt}Кавалеры"

        hide kavalery

        show kavalery at left
        show aplombov at right

        hide kavalery

        show kavalery at left
        show aplombov at right

        kavalery "<{i}(Апломбову).{/i}>"

        hide aplombov

        show kavalery at truecenter

        hide aplombov

        show kavalery at truecenter

        kavalery "Да оставь! Будет тебе! Ну стоит ли? Садись! Оставь!"

        hide kavalery

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Я ничего... Я ведь... Не понимаю даже... Извольте, я уйду... Только вы отдайте мне сначала пять рублей, что вы брали у меня в прошлом году на жилетку пике, извините за выражение. Выпью вот еще и... и уйду, только вы сначала долг отдайте."

        hide jat

        show kavalery at truecenter

        $ kavalery_var = "{noalt}Кавалеры."

        kavalery "Ну будет, будет! Довольно! Стоит ли из-за пустяков?"

        hide kavalery

        show shafer at truecenter

        $ shafer_var = "{noalt}Шафер"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(кричит).{/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "За здоровье родителей невесты Евдокима Захарыча и Настасьи Тимофеевны!"

        hide shafer

        "<{i}Музыка играет туш. Ура.{/i}>"

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов"

        hide zhigalov

        show zhigalov at truecenter

        hide zhigalov

        show zhigalov at truecenter

        zhigalov "<{i}(растроганный, кланяется во все стороны).{/i}>"

        show zhigalov at truecenter

        show zhigalov at truecenter

        zhigalov "Благодарю вас! Дорогие гости! Очень вам благодарен, что вы нас не забыли и пожаловали, не побрезгали!.. И не подумайте, чтоб я был выжига какой или жульничество с моей стороны, а просто из чувств! От прямоты души! Для хороших людей ничего не пожалею!"

        zhigalov "Благодарим покорно!"

        hide zhigalov

        show zhigalov at truecenter

        hide zhigalov

        show zhigalov at truecenter

        zhigalov "<{i}(Целуется.){/i}>"

        show zhigalov at truecenter

        show zhigalov at truecenter

        hide zhigalov

        show dashenka at truecenter

        $ dashenka_var = "{noalt}Дашенька"

        hide dashenka

        show dashenka at truecenter

        hide dashenka

        show dashenka at truecenter

        dashenka "<{i}(матери).{/i}>"

        show dashenka at truecenter

        show dashenka at truecenter

        dashenka "Мамаша, что же вы плачете? Я так счастлива!"

        hide dashenka

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Maman взволнована предстоящей разлукой. Но я посоветовал бы ей лучше вспомнить наш недавний разговор."

        hide aplombov

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Не плачьте, Настасья Тимофеевна! Вы подумайте: что такое слезы человеческие? Малодушная психиатрия и больше ничего!"

        hide jat

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "А рыжики в Греции есть?"

        hide zhigalov

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба."

        dymba "Есть. Там все есть."

        hide dymba

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "А вот груздей, небось, нету."

        hide zhigalov

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба."

        dymba "И грузди есть. Все есть."

        hide dymba

        show mozgovoj at truecenter

        $ mozgovoj_var = "{noalt}Мозговой."

        mozgovoj "Харлампий Спиридоныч, ваша очередь читать речь! Господа, пусть говорит речь!"

        hide mozgovoj

        show kavalery at left
        show shafer at truecenter
        show zmejukina at right

        $ kavalery_var = "{noalt}Все"

        hide kavalery
        hide shafer
        hide zmejukina

        show kavalery at left
        show shafer at truecenter
        show zmejukina at right

        hide kavalery
        hide shafer
        hide zmejukina

        show kavalery at left
        show shafer at truecenter
        show zmejukina at right

        kavalery "<{i}(Дымбе).{/i}>"

        show kavalery at left
        show shafer at truecenter
        show zmejukina at right

        show kavalery at left
        show shafer at truecenter
        show zmejukina at right

        kavalery "Речь! речь! Ваша очередь!"

        hide kavalery
        hide shafer
        hide zmejukina

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба."

        dymba "Зацем? Я не понимаю которое... Сто такое?"

        hide dymba

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Нет, нет! Не смейте отказываться! Ваша очередь! Вставайте!"

        hide zmejukina

        show dymba at truecenter

        $ dymba_var = "{noalt}Дымба"

        hide dymba

        show dymba at truecenter

        hide dymba

        show dymba at truecenter

        dymba "<{i}(встает, смущенно).{/i}>"

        show dymba at truecenter

        show dymba at truecenter

        dymba "Я могу говорить такое... Которая Россия и которая Греция. Теперь которые люди в России и которые в Греции... И которые по морю плавают каравия, по русскому знацит корабли, а по земле разные которые зелезные дороги. Я хоросо понимаю... Мы греки,"

        dymba "вы русские и мне ницего не надо... Я могу говорить такое... Которая Россия и которая Греция."

        hide dymba

    label Act_1_Scene_6:
        "{b}configuration_6{/b}"

        show njunin at truecenter

        show njunin at truecenter

        "<{i}Входит Нюнин.{/i}>"

        hide njunin

        hide njunin

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Постойте, господа, не ешьте! Погодите! Настасья Тимофеевна, на минуточку! Пожалуйте сюда!"

        hide njunin

        show njunin at left
        show nastasjatimofeevna at right

        hide njunin

        show njunin at left
        show nastasjatimofeevna at right

        njunin "<{i}(Ведет Настасью Тимофеевну в сторону, запыхавшись.){/i}>"

        hide nastasjatimofeevna

        show njunin at truecenter

        hide nastasjatimofeevna

        show njunin at truecenter

        njunin "Послушайте... Сейчас придет генерал... Наконец нашел-таки... Просто замучился... Генерал настоящий, солидный такой, старый, лет, пожалуй, восемьдесят, а то и девяносто..."

        hide njunin

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Когда же он придет?"

        hide nastasjatimofeevna

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Сию минуту. Будьте всю жизнь мне благодарны. Не генерал, а малина, Буланже! Не пехота какая-нибудь, не инфантерия, а флотский! По чину он капитан второго ранга, а по-ихнему, морскому, это все равно, что генерал-майор, или в гражданской — действительный статский советник."

        njunin "Решительно все равно. Даже выше."

        hide njunin

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "А ты меня не обманываешь, Андрюшенька?"

        hide nastasjatimofeevna

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Ну вот, мошенник я, что ли? Будьте покойны!"

        hide njunin

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна"

        play sound1 female_sigh

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        play sound1 female_sigh

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(вздыхая).{/i}>"

        show nastasjatimofeevna at truecenter

        stop sound1

        show nastasjatimofeevna at truecenter

        stop sound1

        nastasjatimofeevna "Не хочется зря деньги тратить, Андрюшенька..."

        hide nastasjatimofeevna

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Будьте покойны! Не генерал, а картина!"

        hide njunin

        show njunin at truecenter

        hide njunin

        show njunin at truecenter

        njunin "<{i}(Возвышая голос.){/i}>"

        show njunin at truecenter

        show njunin at truecenter

        njunin "Я и говорю: «Совсем, говорю, забыли нас, ваше превосходительство! Нехорошо, ваше превосходительство, старых знакомых забывать! Настасья, говорю, Тимофеевна на вас в большой претензии!»"

        hide njunin

        show njunin at truecenter

        hide njunin

        show njunin at truecenter

        njunin "<{i}(Идет к столу и садится.){/i}>"

        show njunin at truecenter

        show njunin at truecenter

        njunin "А он говорит: «Помилуй, мой друг, как же я пойду, если я с женихом не знаком?» — «Э, полноте, ваше превосходительство, что за церемонии? Жених, говорю, человек прекраснейший, душа нараспашку. Служит, говорю, оценщиком в ссудной кассе, но вы не подумайте,"

        njunin "ваше превосходительство, что это какой-нибудь замухрышка или червонный валет. В ссудных кассах, говорю, нынче и благородные дамы служат». Похлопал он меня по плечу, выкурили мы с ним по гаванской сигаре, и вот теперь он едет... Погодите, господа, не ешьте..."

        hide njunin

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "А когда он приедет?"

        hide aplombov

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Сию минуту. Когда я уходил от него, он уже калоши надевал. Погодите, господа, не ешьте."

        hide njunin

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Так надо приказать, чтоб марш играли..."

        hide aplombov

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин"

        hide njunin

        show njunin at truecenter

        hide njunin

        show njunin at truecenter

        njunin "<{i}(кричит).{/i}>"

        show njunin at truecenter

        show njunin at truecenter

        njunin "Эй, музыканты! Марш!"

        hide njunin

        "<{i}Музыка минуту играет марш.{/i}>"

    label Act_1_Scene_7:
        "{b}configuration_7{/b}"

        show lakej at truecenter

        $ lakej_var = "{noalt}Лакей"

        hide lakej

        show lakej at truecenter

        hide lakej

        show lakej at truecenter

        lakej "<{i}(докладывает).{/i}>"

        show lakej at truecenter

        show lakej at truecenter

        lakej "Господин Ревунов-Караулов!"

        hide lakej

    label Act_1_Scene_8:
        "{b}configuration_8{/b}"

        play sound1 running

        show zhigalov at left
        show nastasjatimofeevna at truecenter
        show njunin at right

        play sound1 running

        show zhigalov at left
        show nastasjatimofeevna at truecenter
        show njunin at right

        "<{i}Жигалов, Настасья Тимофеевна и Нюнин бегут навстречу.{/i}>"

        hide zhigalov
        hide nastasjatimofeevna
        hide njunin

        stop sound1

        hide zhigalov
        hide nastasjatimofeevna
        hide njunin

        stop sound1

        show revunov at truecenter

        show revunov at truecenter

        "<{i}Входит Ревунов-Караулов.{/i}>"

        hide revunov

        hide revunov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна"

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(кланяясь).{/i}>"

        show nastasjatimofeevna at truecenter

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "Милости просим, ваше превосходительство! Очень приятно!"

        hide nastasjatimofeevna

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Весьма!"

        hide revunov

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "Мы, ваше превосходительство, люди не знатные, не высокие, люди простые, но не подумайте, что с нашей стороны какое-нибудь жульничество. Для хороших людей у нас первое место, мы ничего не пожалеем. Милости просим!"

        hide zhigalov

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Весьма рад!"

        hide revunov

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Позвольте представить, ваше превосходительство! Новобрачный Эпаминонд Максимыч Апломбов со своей новорожд... то есть с новобрачной супругой! Иван Михайлыч Ять, служащий на телеграфе! Иностранец греческого звания по кондитерской части Харлампий Спиридоныч Дымба!"

        njunin "Осин Лукич Бабельмандебский! И прочие, и прочие... Остальные все – чепуха. Садитесь, ваше превосходительство!"

        hide njunin

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Весьма! Виноват, господа, я хочу сказать Андрюше два слова."

        hide revunov

        show revunov at left
        show njunin at right

        hide revunov

        show revunov at left
        show njunin at right

        revunov "<{i}(Отводит Нюнина в сторону.){/i}>"

        hide njunin

        show revunov at truecenter

        hide njunin

        show revunov at truecenter

        revunov "Я, братец, немножко сконфужен... Зачем ты зовешь меня вашим превосходительством? Ведь я не генерал! Капитан 2-го ранга — это даже ниже полковника."

        hide revunov

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин"

        hide njunin

        show njunin at truecenter

        hide njunin

        show njunin at truecenter

        njunin "<{i}(говорит ему в ухо, как глухому).{/i}>"

        show njunin at truecenter

        show njunin at truecenter

        njunin "Знаю, но, Федор Яковлевич, будьте добры, позвольте нам называть вас вашим превосходительством! Семья здесь, знаете ли, патриархальная, уважает старших, любит чинопочитание..."

        hide njunin

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Да, если так, то конечно..."

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}( Идя к столу.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Весьма!"

        hide revunov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Садитесь, ваше превосходительство! Будьте такие добрые! Кушайте, ваше превосходительство! Только извините, у себя там вы привыкли к деликатности, а у нас просто!"

        hide nastasjatimofeevna

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(не расслышав).{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Что-с? Гм... Да-с."

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}Пауза.{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Да-с... В старину люди всегда жили просто и были довольны. Я человек, который в чинах, и то живу просто... Сегодня Андрюша приходит ко мне и зовет меня сюда на свадьбу. Как же, говорю, я пойду, если я не знаком? Это неловко! А он говорит: «Люди они простые,"

        revunov "патриархальные, всякому гостю рады...» Ну, конечно, если так... то отчего же? Очень рад. Дома мне одинокому скучно, а если мое присутствие на свадьбе может доставить кому-нибудь удовольствие, то сделай, говорю, одолжение..."

        hide revunov

        show zhigalov at truecenter

        $ zhigalov_var = "{noalt}Жигалов."

        zhigalov "Значит, от души, ваше превосходительство? Уважаю! Сам я человек простой, без всякого жульничества, и уважаю таких. Кушайте, ваше превосходительство!"

        hide zhigalov

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Вы давно в отставке, ваше превосходительство?"

        hide aplombov

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "А? Да, да... так... Это верно. Да-с... Но позвольте, что же это, однако? Селедка горькая... и хлеб горький. Невозможно есть!"

        hide revunov

        show dymba at left
        show zmejukina at truecenter
        show njunin at right

        $ dymba_var = "{noalt}Все."

        dymba "Горько! Горько!"

        hide dymba
        hide zmejukina
        hide njunin

        show aplombov at left
        show dashenka at right

        show aplombov at left
        show dashenka at right

        "<{i}Апломбов и Дашенька целуются.{/i}>"

        hide aplombov
        hide dashenka

        hide aplombov
        hide dashenka

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Хе-хе-хе... Ваше здоровье!"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}Пауза.{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Да-с... В старину все просто было и все были довольны... Я люблю простоту... Я ведь старый, в отставку вышел в 1865 году... Мне семьдесят два года... Да. Конечно, не без того, и прежде любили при случае показать пышность, но..."

        hide revunov

        show revunov at left
        show mozgovoj at right

        hide revunov

        show revunov at left
        show mozgovoj at right

        revunov "<{i}(Увидев Мозгового.){/i}>"

        hide mozgovoj

        show revunov at truecenter

        hide mozgovoj

        show revunov at truecenter

        revunov "Вы того... матрос, стало быть?"

        hide revunov

        show mozgovoj at truecenter

        $ mozgovoj_var = "{noalt}Мозговой."

        mozgovoj "Точно так."

        hide mozgovoj

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Ага... Так... Да... Морская служба всегда была трудная. Есть над чем задуматься и голову поломать. Всякое незначительное слово имеет, так сказать, свой особый смысл! Например: марсовые по вантам на фок и грот! Что это значит? Матрос небось понимает! Хе-хе... Тонкость,"

        revunov "что твоя математика!"

        hide revunov

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "За здоровье его превосходительства Федора Яковлевича Ревунова-Караулова!"

        hide njunin

        "<{i}Музыка играет туш. Ура.{/i}>"

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Вот вы, ваше превосходительство, изволили сейчас выразиться насчет трудностей флотской службы. А разве телеграфная легче? Теперь, ваше превосходительство, никто не может поступить на телеграфную службу, если не умеет читать и писать по-французски и по-немецки."

        jat "Но самое трудное у нас, это передача телеграмм. Ужасно трудно! Извольте послушать."

        play sound1 knocking

        hide jat

        show jat at truecenter

        play sound1 knocking

        hide jat

        show jat at truecenter

        jat "<{i}(Стучит вилкой по столу, подражая телеграфному станку.){/i}>"

        show jat at truecenter

        stop sound1

        show jat at truecenter

        stop sound1

        hide jat

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Что же это значит?"

        hide revunov

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "Это значит: я уважаю вас, ваше превосходительство, за добродетели. Вы думаете, легко? А вот еще..."

        play sound1 knocking

        hide jat

        show jat at truecenter

        play sound1 knocking

        hide jat

        show jat at truecenter

        jat "<{i}(Стучит.){/i}>"

        show jat at truecenter

        stop sound1

        show jat at truecenter

        stop sound1

        hide jat

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Вы погромче... Не слышу..."

        hide revunov

        show jat at truecenter

        $ jat_var = "{noalt}Ять."

        jat "А это значит: мадам, как я счастлив, что держу вас в своих объятиях!"

        hide jat

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Вы про какую это мадам? Да..."

        hide revunov

        show revunov at left
        show mozgovoj at right

        hide revunov

        show revunov at left
        show mozgovoj at right

        revunov "<{i}(Мозговому.){/i}>"

        hide mozgovoj

        show revunov at truecenter

        hide mozgovoj

        show revunov at truecenter

        revunov "А вот, если идя полным ветром и надо... и надо поставить брамсели и бом-брамсели! Тут уж надо командовать: салинговые к вантам на брамсели и бом-брамсели... и в это время, как на реях отдают паруса, внизу становятся на брам и бом-брам-шкоты, фалы и брасы..."

        hide revunov

        show shafer at truecenter

        $ shafer_var = "{noalt}Шафер"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(вставая).{/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "Милостивые государи и милостивые госуд..."

        hide shafer

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(перебивая).{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Да-с... Мало ли разных команд... Да... Брам и бом-брам-шкоты тянуть пшел фалы!! Хорошо? Но что это значит и какой смысл? А очень просто! Тянут, знаете ли, брам и бом-брам-шкоты и поднимают фалы... все вдруг! причем уравнивают бом-брам-шкоты и бом-брам-фалы при подъеме,"

        revunov "а в это время, глядя по надобности, потравливают брасы сих парусов, а когда уж, стало быть, шкоты натянуты, фалы все до места подняты, то брам и бом-брам-брасы вытягиваются и реи брасопятся соответственно направлению ветра..."

        hide revunov

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин"

        hide njunin

        show njunin at left
        show revunov at right

        hide njunin

        show njunin at left
        show revunov at right

        njunin "<{i}(Ревунову).{/i}>"

        hide revunov

        show njunin at truecenter

        hide revunov

        show njunin at truecenter

        njunin "Федор Яковлевич, хозяйка просит вас поговорить о чем-нибудь другом. Это непонятно гостям и скучно..."

        hide njunin

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Что? Кому скучно?"

        hide revunov

        show revunov at left
        show mozgovoj at right

        hide revunov

        show revunov at left
        show mozgovoj at right

        revunov "<{i}(Мозговому.){/i}>"

        hide mozgovoj

        show revunov at truecenter

        hide mozgovoj

        show revunov at truecenter

        revunov "Молодой человек! А вот ежели корабль лежит бейдевинд правым галсом под всеми парусами и надо сделать через фордевинд. Как надо командовать? А вот как: свистать всех наверх, поворот через фордевинд!.. Хе-хе..."

        hide revunov

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Федор Яковлевич, довольно! Кушайте."

        hide njunin

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Как только все выбежали, сейчас командуют: по местам стоять, поворот через фордевинд! Эх, жизнь! Командуешь, а сам смотришь, как матросы, как молния, разбегаются по местам и разносят брамы и брасы. Этак не вытерпишь и крикнешь: молодцы, ребята!"

        play sound1 male_cough

        hide revunov

        show revunov at truecenter

        play sound1 male_cough

        hide revunov

        show revunov at truecenter

        revunov "<{i}(Поперхнулся и кашляет.){/i}>"

        show revunov at truecenter

        stop sound1

        show revunov at truecenter

        stop sound1

        hide revunov

        show shafer at truecenter

        $ shafer_var = "{noalt}Шафер"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(спешит воспользоваться наступившей паузой).{/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "В сегодняшний, так сказать, день, в который мы, собравшись все в кучу для чествования нашего любимого..."

        hide shafer

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(перебивая).{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Да-с! И ведь все это надо помнить! Например: фока-шкот, грота-шкот раздернуть!.."

        hide revunov

        show shafer at truecenter

        $ shafer_var = "{noalt}Шафер"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(обиженно).{/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "Что ж он перебивает? Этак мы ни одной речи не скажем!"

        hide shafer

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Мы люди темные, ваше превосходительство, ничего этого самого не понимаем, а вы лучше расскажите нам что-нибудь касающее..."

        hide nastasjatimofeevna

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(не расслышав).{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Я уже ел, благодарю. Вы говорите: гуся? Благодарю... Да... Старину вспомнил... А ведь приятно, молодой человек! Плывешь себе по морю, горя не знаючи, и..."

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(дрогнувшим голосом){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "помните этот восторг, когда делают поворот оверштаг! Какой моряк не зажжется при воспоминании об этом маневре?! Ведь как только раздалась команда: свистать всех наверх, поворот оверштаг — словно электрическая искра пробежала по всем."

        revunov "Начиная от командира и до последнего матроса — все встрепенулись..."

        hide revunov

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Скучно! Скучно!"

        hide zmejukina

        "<{i}Общий ропот.{/i}>"

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(не расслышав).{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Благодарю, я ел."

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(С увлечением.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Все приготовилось и впилось глазами в старшего офицера... На фоковые и гротовые брасы на правую, на крюйсельные брасы на левую, на контра-брасы на левую, командует старший офицер. Все моментально исполняется... Фока-шкот, кливер-шкот раздернуть... право на борт!"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(Встает.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Корабль покатился к ветру, и, наконец, паруса начинают заполаскивать. Старший офицер: — на брасах, на брасах не зевать, а сам впился глазами в грот-марсель и, когда, наконец, и этот парус то есть момент поворота наступил,"

        revunov "раздается громовая команда: грот-марса-булинь отдай, пшел брасы! Тут все летит, трещит — столпотворение вавилонское! — все исполняется без ошибки. Поворот удался!"

        hide revunov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна"

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(вспыхнув).{/i}>"

        show nastasjatimofeevna at truecenter

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "Генерал, а безобразите... Постыдились бы на старости лет!"

        hide nastasjatimofeevna

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Котлет? Нет, не ел... благодарю вас."

        hide revunov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна"

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        hide nastasjatimofeevna

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "<{i}(громко).{/i}>"

        show nastasjatimofeevna at truecenter

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "Я говорю, постыдились бы на старости лет! Генерал, а безобразите!"

        hide nastasjatimofeevna

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин"

        hide njunin

        show njunin at truecenter

        hide njunin

        show njunin at truecenter

        njunin "<{i}(смущенно).{/i}>"

        show njunin at truecenter

        show njunin at truecenter

        njunin "Господа, ну вот... стоит ли? Право..."

        hide njunin

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Во-первых, я не генерал, а капитан 2-го ранга, что по военной табели о рангах соответствует подполковнику."

        hide revunov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Ежели не генерал, то за что же вы деньги взяли? И мы вам не за то деньги платили, чтоб вы безобразили!"

        hide nastasjatimofeevna

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(в недоумении).{/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Какие деньги?"

        hide revunov

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Известно, какие. Небось получили через Андрея Андреевича четвертную..."

        hide nastasjatimofeevna

        show nastasjatimofeevna at left
        show njunin at right

        hide nastasjatimofeevna

        show nastasjatimofeevna at left
        show njunin at right

        nastasjatimofeevna "<{i}(Нюнину).{/i}>"

        hide njunin

        show nastasjatimofeevna at truecenter

        hide njunin

        show nastasjatimofeevna at truecenter

        nastasjatimofeevna "А тебе, Андрюшенька, грех! Я тебя не просила такого нанимать!"

        hide nastasjatimofeevna

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Ну вот... Оставьте! Стоит ли?"

        hide njunin

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Наняли... заплатили... Что такое?"

        hide revunov

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Позвольте, однако... Вы ведь получили от Андрея Андреевича двадцать пять рублей?"

        hide aplombov

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Какие двадцать пять рублей?"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(Сообразив.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Вот оно что! Теперь я все понимаю... Какая гадость! Какая гадость!"

        hide revunov

        show aplombov at truecenter

        $ aplombov_var = "{noalt}Апломбов."

        aplombov "Ведь вы получили деньги?"

        hide aplombov

        show revunov at truecenter

        $ revunov_var = "{noalt}Ревунов."

        revunov "Никаких я денег не получал! Подите прочь!"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(Выходит из-за стола.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Какая гадость! Какая низость! Оскорбить так старого человека, моряка, заслуженного офицера!.. Будь это порядочное общество, я мог бы вызвать на дуэль, а теперь что я могу сделать?"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(Растерянно.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Где дверь? В какую сторону идти? Человек, выведи меня! Человек!"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(Идет.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        revunov "Какая низость! Какая гадость!"

        hide revunov

        show revunov at truecenter

        hide revunov

        show revunov at truecenter

        revunov "<{i}(Уходит.){/i}>"

        show revunov at truecenter

        show revunov at truecenter

        hide revunov

    label Act_1_Scene_9:
        "{b}configuration_9{/b}"

        show nastasjatimofeevna at truecenter

        $ nastasjatimofeevna_var = "{noalt}Настасья Тимофеевна."

        nastasjatimofeevna "Андрюшенька, где же двадцать пять рублей?"

        hide nastasjatimofeevna

        show njunin at truecenter

        $ njunin_var = "{noalt}Нюнин."

        njunin "Ну стоит ли говорить о таких пустяках? Велика важность! Тут все радуются, а вы черт знает о чем..."

        hide njunin

        show njunin at truecenter

        hide njunin

        show njunin at truecenter

        njunin "<{i}(Кричит.){/i}>"

        show njunin at truecenter

        show njunin at truecenter

        njunin "За здоровье молодых! Музыка, марш! Музыка!"

        hide njunin

        show njunin at truecenter

        hide njunin

        show njunin at truecenter

        njunin "<{i}Музыка играет марш.{/i}>"

        show njunin at truecenter

        show njunin at truecenter

        njunin "За здоровье молодых!"

        hide njunin

        show zmejukina at truecenter

        $ zmejukina_var = "{noalt}Змеюкина."

        zmejukina "Мне душно! Дайте мне атмосферы! Возле вас я задыхаюсь!"

        hide zmejukina

        show jat at truecenter

        $ jat_var = "{noalt}Ять"

        hide jat

        show jat at truecenter

        hide jat

        show jat at truecenter

        jat "<{i}(в восторге).{/i}>"

        show jat at truecenter

        show jat at truecenter

        jat "Чудная! Чудная!"

        hide jat

        "<{i}Шум.{/i}>"

        show shafer at truecenter

        $ shafer_var = "{noalt}Шафер"

        hide shafer

        show shafer at truecenter

        hide shafer

        show shafer at truecenter

        shafer "<{i}(стараясь перекричать).{/i}>"

        show shafer at truecenter

        show shafer at truecenter

        shafer "Милостивые государи и милостивые государыни! В сегодняшний, так сказать, день..."

        hide shafer


