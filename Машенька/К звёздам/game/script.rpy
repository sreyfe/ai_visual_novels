define inna_aleksandrovna = Character("inna_aleksandrovna_var", color="#FFB300", dynamic=True)
define petja = Character("petja_var", color="#803E75", dynamic=True)
define zhitov = Character("zhitov_var", color="#FF6800", dynamic=True)
define lunts = Character("lunts_var", color="#A6BDD7", dynamic=True)
define minna = Character("minna_var", color="#C10020", dynamic=True)
define pollak = Character("pollak_var", color="#CEA262", dynamic=True)
define anna = Character("anna_var", color="#817066", dynamic=True)
define trejch = Character("trejch_var", color="#007D34", dynamic=True)
define verhovtsev = Character("verhovtsev_var", color="#F6768E", dynamic=True)
define frants = Character("frants_var", color="#00538A", dynamic=True)
define sergej_nikolaevich = Character("sergej_nikolaevich_var", color="#FF7A5C", dynamic=True)
define marusja = Character("marusja_var", color="#53377A", dynamic=True)
define shmidt = Character("shmidt_var", color="#FF8E00", dynamic=True)
define nikolaj = Character("nikolaj_var", color="#B32851", dynamic=True)
define starucha = Character("starucha_var", color="#F4C800", dynamic=True)

label start:
    play music "audio/music/6.mp3" fadeout 1.0 fadein 1.0

    scene poster with fade

    "К звёздам"

    menu:
        "{color=#000}ДЕЙСТВУЮЩИЕ ЛИЦА:{/color}":
            jump Characters
        "{color=#000}ДЕЙСТВИЕ ПЕРВОЕ{/color}":
            jump Act_1
        "{color=#000}ДЕЙСТВИЕ ВТОРОЕ{/color}":
            jump Act_2
        "{color=#000}ДЕЙСТВИЕ ТРЕТЬЕ{/color}":
            jump Act_3
        "{color=#000}ДЕЙСТВИЕ ЧЕТВЕРТОЕ{/color}":
            jump Act_4

label Characters:
    play music "audio/music/9.mp3" fadeout 1.0 fadein 1.0

    scene 3 with fade

    "{b}ДЕЙСТВУЮЩИЕ ЛИЦА:{/b}"

    show sergej_nikolaevich at truecenter
    "Терновский Сергей Николаевич., русский ученый, уехавший за границу. Директор обсерватории. Знаменит; член многих академий и ученых обществ. Пятьдесят шесть лет, но на вид кажется моложе."
    hide sergej_nikolaevich

    show sergej_nikolaevich at truecenter
    "Движения плавные, спокойные и очень точные; так же сдержан и точен в жестикуляции - ничего лишнего. Вежлив, внимателен, но от всего этого отдает холодом."
    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter
    "Терновская Инна Александровна, жена его, тех же почти лет."
    hide inna_aleksandrovna

    "Дети Терновских:"

    show nikolaj at truecenter
    "Николай, 27 лет."
    hide nikolaj

    show anna at truecenter
    "Анна, 25 лет. Красива и суха, одета не к лицу."
    hide anna

    show petja at truecenter
    "Петя, 18 лет. Бледный, изящный, хрупкий; черные вьющиеся волосы; белый отложной воротник."
    hide petja

    show verhovtsev at truecenter
    "Верховцев. Валентин Алексеевич, муж Анны. Лет 30. Рыжий. Самоуверен, повелителен, насмешлив. Иногда груб. Инженер."
    hide verhovtsev

    show marusja at truecenter
    "Маруся., невеста Николая, 20 лет. Красивая."
    hide marusja

    "Ассистенты Терновского:"

    show pollak at truecenter
    "Поллак. Сухой, высокий, с большим лысым черепом, корректный. 32 года. Механичен. Курит сигары."
    hide pollak

    show lunts at truecenter
    "Лунц. Иосиф Абрамович. Еврей, 28 лет. Привычка обращаться с точными инструментами придает движениям сдержанность и точность; но при волнении Лунц не выдерживает и жестикулирует со страстностью южанина-семита."
    hide lunts

    show zhitov at truecenter
    "Житов Василий Васильевич. Неопределенного возраста. Велик, волосат, медведеобразен. Всегда сидит. Своеобразно красив."
    hide zhitov

    show trejch at truecenter
    "Трейч, рабочий, 30 лет. Черный, худощавый, очень красивый, сильно изогнутые брови; дальнозорок. Прост, серьезен, несловоохотлив."
    hide trejch

    show shmidt at truecenter
    "Шмидт. Молод. Маленького роста; мелкие, но правильные черты лица; одет тщательно; говорит тонким голосом. Имеет вид незначительный."
    hide shmidt

    show minna at truecenter
    "Минна, служанка."
    hide minna

    show frants at truecenter
    "Франц, слуга."
    hide frants

    show starucha at truecenter
    "Старуха."
    hide starucha


label Act_1:
    play music "audio/music/12.mp3" fadeout 1.0 fadein 1.0

    scene 2 with fade


label Act_1_Scene_1:
    "{b}ДЕЙСТВИЕ ПЕРВОЕ{/b}"

    "<{i}Обсерватория в горах. Поздний вечер.{/i}>"

    "<{i}Сцена представляет две комнаты; первая - нечто вроде столовой, большая, с белыми толстыми стенами; у окон, за которыми мечется во тьме что-то белое, очень широкие подоконники; огромный камин, в котором горят поленья.{/i}>"

    "<{i}Убранство простое, строгое, отсутствие мягкой мебели и занавесок. Несколько гравюр: портреты астрономов, волхвы, приведенные звездою ко Христу. Лестница вверх, в библиотеку и кабинет Терновского.{/i}>"

    show trejch at left
    show pollak at right

    "<{i}Задняя комната - обширный рабочий кабинет, в общем похожий на первую комнату, но без камина. Несколько столов. Фотографии звезд и лунной поверхности, некоторые простейшие инструменты. Сидит за работой ассистент Терновского - Поллак.{/i}>"

    hide trejch
    hide pollak

    play sound1 footsteps
    play sound2 telephone
    play sound3 whistle

    show zhitov at left
    show petja at truecenter
    show lunts at right

    "<{i}В передней комнате Инна Александровна и Житов разговаривают; Петя. читает; Лунц ходит взад и вперед. У очага кухарка - немка готовит кофе. За окнами свист и вой горной вьюги. Потрескивают дрова в камине. Равномерно звонит колокол, сзывая заблудившихся.{/i}>"

    hide inna_aleksandrovna
    hide zhitov
    hide petja
    hide lunts

    stop sound1
    stop sound2
    stop sound3

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Звонит, звонит, а все без толку. За четыре дня хоть бы кто пришел. Сидишь, сидишь, да и подумаешь: уж живы ли там люди-то?"

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(отрываясь).{/i}>"

    petja "А кому прийти? Кто пойдет сюда?"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну, мало ли кто! Снизу может кто прийти..."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Не до того им, чтобы по горам лазить."

    hide petja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да, положение затруднительное. Дороги нет - как в осажденном городе, ни оттуда, ни отсюда."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Денька через два и есть нечего будет."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Так посидим."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Вам-то хорошо говорить, Василий Васильевич, - вы, как медведь, своим жиром неделю сыты будете, - а что мне с Сергеем Николаевичем делать?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А вы ему запас сделайте, мы и так обойдемся. Лунц, а Лунц, вы бы сели!"

    hide zhitov

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "не отвечает, ходит."

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну и сторонка! Постойте, словно постучал кто. Постойте-ка!"

    inna_aleksandrovna "<{i}(Прислушивается.){/i}>"

    inna_aleksandrovna "Нет, показалось. Какая метель, у нас такой не бывает."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Бывает... в степи."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "В степи не жила... не знаю. Как бьет в окна!"

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Ты напрасно ждешь, мама, - никто не придет."

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А может?.."

    inna_aleksandrovna "<{i}(Пауза.){/i}>"

    inna_aleksandrovna "Газеты старые почитать, что ли... да уж читаны-перечитаны. Иосиф Абрамыч, вы ничего новенького не слыхали?"

    hide inna_aleksandrovna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(останавливаясь).{/i}>"

    lunts "Откуда же я могу услышать? Как вы странно спрашиваете. Ведь это же невозможно, ей-богу. Откуда я могу услышать, сами посудите. Странно!"

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну-ну, я-так, не сердитесь. Душа кровью обливается, как подумаешь, что там делается! Господи!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Дерутся."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Дерутся! Вам-то легко говорить, Василий Васильевич, у вас там никого своих нету, а у меня ведь дети! И ничего-то не знаешь, как в лесу... да какое - в лесу! В лесу хоть птица пролетит, заяц пробежит, а тут..."

    hide inna_aleksandrovna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(на ходу).{/i}>"

    lunts "Может быть, там уже полная победа. Может быть, там уже новый мир - на развалинах старого."

    hide lunts

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Не думаю. Непохоже было."

    hide zhitov

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Почему это не думаете? Вы читали, что министерство подало в отставку, что весь город в баррикадах, что пролетариат уже овладел ратушей? А за пять дней что могло произойти!"

    hide petja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ну, может быть, не знаю. Лунц, вы бы сели. По моему расчету, вы за эти дни верст двести сделали."

    hide zhitov

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Отстаньте! Я вам не мешаю, и вы мне не мешайте. Как это некультурно: врываться в чужую жизнь. Я же не говорю вам: Житов, не дремлите по целым часам, вы уже проспали вечность. Я не говорю!"

    hide lunts

    play sound1 footsteps

    show petja at left
    show lunts at right

    "<{i}Петя подходит к Лунцу и тихо разговаривает с ним о чем-то. Ходят рядом, изредка обмениваясь словами.{/i}>"

    hide petja
    hide lunts

    stop sound1

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    hide inna_aleksandrovna

    show inna_aleksandrovna at left
    show zhitov at right

    inna_aleksandrovna "<{i}(тихо Житову).{/i}>"

    hide zhitov

    show inna_aleksandrovna at truecenter

    inna_aleksandrovna "Экий недотрога! Ну что же, Василий Васильевич, выпьем кофейку, что ли, с горя..."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Я бы чаю выпил."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Сказал! Я бы и сама, батюшка, чайку бы выпила, да где его возьмешь. С малиновым вареньем бы - хорошо."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А я так - вприкуску."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да что уж! Вы вот что скажите, Василий Васильевич, - ко всему я тут привыкла, ну ко всему - и к горам этим, и к безлюдью, а вот березку позабыть не могу. Как подумаю, как вспомню - так часа два плачу, как угорелая."

    inna_aleksandrovna "У нас в имении усадьба на горке стояла, а вокруг березовая роща - какая роща! После дождя такой, бывало, подымется запах, что... что..."

    inna_aleksandrovna "<{i}(Утирает глаза.){/i}>"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А вы бы взяли да и съездили в Россию месяца на два."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А с кем же я его оставлю? Он тоже меня сколько раз уговаривал, - да разве это можно! Ну вдруг заболеет? - года у меня с ним не маленькие."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Я останусь."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Нет, нет, и не говорите. Нету березки, и не надо, - ведь я к слову сказала. Нет, нет. Тут тоже хорошо. Вот весна идет..."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А если б его в Сибирь услали? Поехали б?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А почему ж не поехать? И в Сибири люди живут. Эка!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Вы славная, Инна Александровна."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(нежно).{/i}>"

    inna_aleksandrovna "А ты глупый, - разве старухам такие вещи говорят? А и вправду, Василий Васильевич, отчего бы вам не жениться? Жили бы тут да поживали, как мы вот с Сергеем Николаевичем."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет, куда мне... Человек я непоседливый."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 female_laughter

    inna_aleksandrovna "<{i}(смеясь).{/i}>"

    stop sound1

    inna_aleksandrovna "То-то, похоже."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет, верно. Нынче здесь, а завтра там. Я и астрономию скоро брошу. Я ведь в Австралии еще не был."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А туда зачем?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да так. Посмотреть, как люди живут."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да ведь у вас, Василий Васильевич, и денег-то нет. Это тому хорошо путешествовать, у кого есть деньги."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да я не путешествовать, я так. Поступлю на железную дорогу или на завод."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Из астрономов-то?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Что же, этому легко научиться. Я механику знаю. Мне немного надо, я человек неизбалованный."

    hide zhitov

    play sound1 whistle

    "<{i}Пауза. Свист вьюги сильнее.{/i}>"

    stop sound1

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Мама, а папа где? работает?"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да... просил не мешать ему."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(пожимая плечами).{/i}>"

    petja "Как он может работать в такое время! Не понимаю."

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А так и может. Что же, лучше, если он вот так метаться будет? Вон Поллак тоже работает."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Ну, Поллак... Про него я уж не говорю. Поллак."

    hide petja

    show petja at left
    show lunts at right

    petja "<{i}(Тихо говорит с Лунцем.){/i}>"

    hide lunts

    show petja at truecenter

    hide petja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Поллак человек талантливый, он через пять лет знаменитостью будет. Энергичный человек."

    play sound1 female_laughter

    hide zhitov

    show zhitov at left
    show inna_aleksandrovna at right

    zhitov "<{i}Инна Александровна смеется.{/i}>"

    hide inna_aleksandrovna

    show zhitov at truecenter

    stop sound1

    zhitov "Чего вы смеетесь, разве не правда?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да нет, я не тому. Очень он чудак, - иной раз и нехорошо, а не удержишься... Он на какой-то инструмент похож, - какой у вас есть инструмент вроде него?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Не знаю."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Астролябия, кажется."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Не знаю. А как вот можете вы смеяться, удивляюсь я."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 female_sigh

    inna_aleksandrovna "<{i}(вздыхает).{/i}>"

    stop sound1

    inna_aleksandrovna "Без смеха нельзя, только смехом иногда и спасаешься. Вот тоже расскажу я вам. Ехали мы тогда из России с детьми, со скарбом... дела были плохие, на билеты денег хватило, да и все тут. И как это случилось, до сих пор понять не могу - потеряла я билеты."

    inna_aleksandrovna "Никогда ничего не теряла, а тут..."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Где же это, в России?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Если бы в России, а то за границей уже. Сидим мы на какой-то австрийской станции... дети, чемоданы, подушки... взглянула я на эти подушки да как захохочу! Ей-богу! Сейчас смешно вспомнить."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А скажите, Инна Александровна, я до сих пор толком не разберусь: за что Сергей Николаевич выслан из России?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да его не высылали, сам уехал. Поссорился с начальством. Бумагу какую-то скверную заставляли его подписать, а он не стал, а потом министру дерзостей наговорил. Ну и уехали, а тут предложили ему эту обсерваторию, - вот двенадцать лет на камнях и живем."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Значит, он может вернуться, если захочет?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да зачем? В России, вы знаете, таких обсерваторий нет."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А березка-то!"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну вот, пустяки какие! Постойте, кто-то стучит."

    hide inna_aleksandrovna

    "<{i}Вой метели.{/i}>"

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет. Показалось."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А все-таки... Минна, голубушка, сходите узнайте, будто приехал кто. Этот колокол всю душу вымотает. Все кажется, словно идет кто или едет. Слышите?"

    hide inna_aleksandrovna

    "<{i}Вой метели, звук колокола.{/i}>"

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Эти мартовские бури всегда самые свирепые. Внизу весна, а у нас зима настоящая. Миндаль уже отцвел, пожалуй."

    hide zhitov

    show minna at truecenter

    $ minna_var = "{noalt}Минна."

    minna "Никого нет."

    hide minna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Что там делается! Что там делается! Главное, я за Коленьку боюсь. Ведь он такой, он ни на что не смотрит: ружья не ружья, пушки не пушки. Господи! Я и подумать об этом не могу! Хоть бы весточка какая, а то четыре дня - как в могиле."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ну, обойдется, скоро все узнаете. Барометр поднимается."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А главное, будь бы за свое дело дрался. А то и люди чужие, и страна чужая, - ну какое ему дело!"

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(горячо).{/i}>"

    petja "Николай - рыцарь. Он за всех угнетенных, кто бы они ни были. Все люди одинаковы, и чья бы страна ни была, все равно."

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Чужие! Страна, государство - не понимаю я этого. Что значит - чужие, государство? Вот это разделение и создает рабов, потому что когда в одном доме грабят, то в другом сидят спокойно, в одном доме убивают, то в другом говорят: это нас не касается."

    lunts "Свои! Чужие! Я вот еврей, а у меня своей страны нет - так, значит, я всем чужой? Нет, я всем свой, да..."

    play sound1 footsteps

    lunts "<{i}(Ходит.){/i}>"

    stop sound1

    lunts "Да!"

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Конечно. Это узость - разбивать землю на какие-то участки."

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    play sound1 footsteps

    lunts "<{i}(ходит).{/i}>"

    stop sound1

    lunts "Да. Только и слышишь-свои, чужие! Негры, жиды!"

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну, вы опять на свое повернули. Как не стыдно! Разве я что-нибудь говорю? Разве я говорю, что Коленька плохо делает? Сама ж я посылала: поезжай, голубчик, поскорее, а то здесь еще больше ты измучишься."

    inna_aleksandrovna "Господи, Коля-то да нехорошо, - я о том, что сердце у меня изболелось. Ведь я неделю в такой муке живу, в такой муке... Вы ночь-то спите, а я глаз не смыкаю, все слушаю, слушаю: вьюга да колокол, колокол да вьюга. Плачет, хоронит кого-то..."

    inna_aleksandrovna "нет, не увижу я Колюшки!"

    hide inna_aleksandrovna

    "<{i}Вьюга, колокол.{/i}>"

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(ласково).{/i}>"

    petja "Ну, успокойся, мамочка, все обойдется. Он не один там, - почему непременно с ним что-нибудь случится? Успокойся."

    hide petja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Не говоря уже о том, что с ним Маруся и Анна Сергеевна с мужем. Все-таки поберегут. Да и так, вы знаете, как его любят все, - у него теперь свита как у генерала, даром пропасть не дадут."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Знаю, знаю, да что поделаешь! Но только про Марусю вы мне не говорите. Анна - женщина благоразумная, а Маруся - та сама вперед полезет. Знаю ее."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А ты чего, мама, хотела бы? Чтоб Маруся пряталась?"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Опять... Да деритесь себе сколько хотите, разве я что говорю? Только не успокаивайте меня: сама знаю, что знаю, не маленькая. Как помоложе была, сама с волками дралась. Вот что!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "С волками? Вот вы какая, не ожидал. Как же это вы так?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да пустяки. Раз ночью зимой ехала одна на лошади, на меня и напали. Отстрелялась. А меня они и дразнят до сих пор."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А вы и стрелять умеете?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Чему, Василий Васильевич, при такой жизни не научишься. Я с Сергеем Николаевичем в Туркестан ездила на экспедицию, так полторы тысячи верст верхом сделала, по-мужски. Мало ли бывало! Тонула раз, два раза горела..."

    inna_aleksandrovna "<{i}(Тихо.){/i}>"

    inna_aleksandrovna "Только скажу вам, Василий Васильевич, - нет ничего страшнее в мире, как болезнь детей. Раз, тоже в экспедиции, у Колюшки жаба открылась. Ни доктора, ни лекарств, до ближнего жилья верст пятьдесят, а то и больше."

    inna_aleksandrovna "Выбежала я из палатки да как брякнулась о землю... вспомнить страшно. Ведь у меня двое детей умерло, вы знаете. Один на седьмом году, Сереженька, другой еще грудным. Анюта раз при смерти была, да что вспоминать..."

    inna_aleksandrovna "Тяжелая наша материнская доля, Василий Васильевич... Благодарение еще богу, что дети хорошие вышли."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да, Николай Сергеевич у вас удивительный человек."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Коля-то! Сколько я перевидала людей, а такой души еще не встречала. Вот говорила я - чужое дело, сразу видно, что эгоистка... а Коля: если увидит он, что лев разоряет муравьиную кучу, так он один с голыми руками на льва пойдет."

    inna_aleksandrovna "Вот он какой! Что-то там делается! Что-то делается!.."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Если бы мне не так хотелось в Австралию..."

    hide zhitov

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    play sound1 footsteps

    pollak "<{i}(входит).{/i}>"

    stop sound1

    pollak "У вас не найдется, уважаемая Инна Александровна, чашки черного кофе?"

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Как же не найдется? Найдется! Минна!"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(Идет.){/i}>"

    stop sound1

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ну, как дела, коллега?"

    hide zhitov

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Хорошо. А вы что же ничего не делаете?"

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Погода... Какая тут работа! Да и события такие..."

    hide zhitov

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "А не русская лень?"

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Может быть, и лень. Кто знает?"

    hide zhitov

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Нехорошо, дорогой товарищ. Лунц, вы произвели вычисления, которые поручил вам Сергей Николаевич?"

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(резко).{/i}>"

    lunts "Нет."

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Напрасно."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Напрасно, не напрасно, это вас не касается. Вы такой же ассистент, как и я, и не имеете права делать мне замечания. Да."

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    pollak "<{i}(отворачивается, пожимая плечами).{/i}>"

    pollak "Скажите, Житов, чтобы кофе мне подали туда."

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ладно. А над чем сейчас работает Сергей Николаевич? Я как-то отошел от дела за это время."

    hide zhitov

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "О, у него такая работа! Я сам могу много работать, но я удивляюсь настойчивости Сергея Николаевича, силе его мозга. Трение, это возмутительное трение, отсутствует в нем, как в наших инструментах."

    pollak "И работает он с правильностью часового механизма: я убежден, что в его вычислениях за тридцать лет нельзя найти ни одной ошибки."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(прислушиваясь).{/i}>"

    lunts "Он не только работник, он-талант."

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Совершенно верно. У него числа и цифры-живые и движутся, как солдаты."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Вы все сводите к дисциплине. Какая юнкерская поэзия!"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Без дисциплины нет победы, дорогой Лунц."

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Верно!"

    hide zhitov

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Я о нем думаю лучше, чем вы. Я думаю, что он видит вечность, видит, как мы вот эти стены. Да!"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Я не возражаю. У вас нет сведений, кончилась эта революция или нет?"

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Какие тут сведения! Слышите, что на дворе делается?"

    hide zhitov

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Я упустил это обстоятельство из виду."

    hide pollak

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "По последним газетам..."

    hide petja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Нет, нет. Вы мне скажите, когда все это кончится. Я не хочу входить в подробности."

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(входит).{/i}>"

    stop sound1

    inna_aleksandrovna "Нет никого. Выходила сама посмотреть - пустыня."

    hide inna_aleksandrovna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Так я попрошу вас, уважаемая Инна Александровна, дать мне кофе туда."

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Хорошо, хорошо, работайте. Сейчас работа - это прямо счастье."

    hide inna_aleksandrovna

    play sound1 footsteps

    show pollak at truecenter

    "<{i}Поллак уходит во вторую комнату.{/i}>"

    hide pollak

    stop sound1

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А я думаю, что бывают минуты, когда работать над чем-нибудь нечестно."

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Петя, Петя!"

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Я не могу! Отчего вы не пускаете меня туда? Я тут с ума схожу, в этой дыре!"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Петечка, голубчик, ведь тебе восемнадцати лет еще нету."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Николай в девятнадцать лет в тюрьме уже сидел!"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну что же тут хорошего?"

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Он работал!"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ах, господи, ну поговори с отцом... как он скажет, так и будет."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Он говорит: ступай."

    hide petja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "За чем же дело стало?"

    hide zhitov

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Я не знаю, я не могу. Там такая великая борьба, а я... Я не могу, я не могу!"

    play sound1 footsteps

    petja "<{i}(Уходит.){/i}>"

    stop sound1

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Петя опять нервничает. Вы, Инна Александровна, занялись бы им."

    play sound1 footsteps

    hide lunts

    show lunts at left
    show petja at right

    lunts "<{i}(Идет вслед за Петей.){/i}>"

    hide petja

    show lunts at truecenter

    stop sound1

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну что же я поделаю? Боже мой, боже мой!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ничего, пройдет."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Нежный он такой, совсем как девочка... ну куда ему! И что с ним в эти дни сделалось! А тут еще этот Лунц: нужно бы успокоить, а он..."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ну, у Лунца у самого, того и гляди, истерика сделается."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Вижу уж. Спасибо вы, Василий Васильевич, еще спокойны, а то хоть ложись в гроб да помирай."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ну, я-то что. Я всегда спокоен, у меня уж характер такой. Иной раз и рад бы поволноваться, да не выходит."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Хороший характер."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Не знаю. Удобный, конечно, характер. Жаль вот только, что газет нету: люблю почитать, как люди там волнуются."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А вы знаете, что у Лунца четыре года назад, когда он тут, за границей, еще студентом был, родителей убили? Во время еврейского погрома..."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Знаю, слыхал."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Он сам об этом никогда не говорит, не выносит. Несчастный молодой человек... я иногда на него без слез смотреть не могу. Опять стучит?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "В третьем году в такую погоду разносчик к нам попал. Чуть живой. А оттаял - сейчас же торговать начал."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Вот и я разносчиком в Австралию пойду."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да ведь вы английского не знаете."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Немного знаю. В Калифорнии научился."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну, а я все-таки газеты почитаю. Ни о чем другом думать не могу. И вы бы почитали что-нибудь, Василий Васильевич."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Не хочется. Я у камина посижу."

    hide zhitov

    show inna_aleksandrovna at left
    show zhitov at truecenter
    show pollak at right

    "<{i}Инна Александровна надевает очки и разбирает газеты; Житов садится у камина. Поллак работает. Вьюга, колокол.{/i}>"

    hide inna_aleksandrovna
    hide zhitov
    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Что-то мой Сергей Николаевич? Я уж его два дня не видала: и пьет и ест там. И входить не велел."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "М-да."

    hide zhitov

    "<{i}Пауза.{/i}>"

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(читает).{/i}>"

    inna_aleksandrovna "Какие ужасы! Что это такое пулеметы, Василий Васильевич?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Это такая пушка особенная."

    hide zhitov

    show minna at left
    show pollak at right

    "<{i}Пауза. Минна приносит Поллаку кофе.{/i}>"

    hide minna
    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Взяла бы я сама пулемет, да их бы..."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "М-да. Штука серьезная."

    hide zhitov

    "<{i}Пауза.{/i}>"

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Как воет! Читать нельзя. А мне вас жалко будет, Василий Васильевич, если вы в Австралию уедете. Не ездите, а?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Невозможно. Непоседливый я человек. Мне бы, Инна Александровна, хотелось всю землю кругом ощупать - какая она. Из Австралии я в Индию поеду, я еще тигров на свободе не видал."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А зачем они вам понадобились?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Не знаю. Я, Инна Александровна, смотреть люблю. Как все это вообще. У нас в деревне бугор был, так я, мальчишкой еще, по целым дням сидел, смотрел все."

    zhitov "Я и астрономией-то занялся, чтобы смотреть, а вычислять не люблю: не все ли равно, двадцать миллионов миль или тридцать. И разговаривать я тоже не люблю."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну-ну, не буду. Смотрите себе."

    hide inna_aleksandrovna

    "<{i}Пауза. Вьюга. Колокол.{/i}>"

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов"

    zhitov "<{i}(не оборачиваясь).{/i}>"

    zhitov "А вы и в Канаду с Сергеем Николаевичем поедете? На затмение?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А? В Канаду? Поеду. Как же он без меня?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Тяжело будет. Далеко."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Пустяки. Только бы тут все обошлось. Господи, господи, подумать страшно!"

    inna_aleksandrovna "<{i}Молчание. Вьюга. Колокол.{/i}>"

    inna_aleksandrovna "Василий Васильевич!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Что?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Вы слышите?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Опять что-то показалось."

    inna_aleksandrovna "<{i}Пауза.{/i}>"

    inna_aleksandrovna "Василий Васильевич, вы слышите?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Ну?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Выстрел был."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Откуда тут выстрел? Просто- галлюцинация слуха."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А я так ясно слышала."

    hide inna_aleksandrovna

    "<{i}Пауза. Далекий выстрел.{/i}>"

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Эге! Стреляют!"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 running

    inna_aleksandrovna "<{i}(бежит).{/i}>"

    stop sound1

    inna_aleksandrovna "Минна, Минна! Франц!"

    hide inna_aleksandrovna

    play sound1 footsteps

    show zhitov at left
    show petja at truecenter
    show lunts at right

    "<{i}Житов медленно поднимается. Второй выстрел, ближе. Быстро проходят Петя и Лунц.{/i}>"

    hide zhitov
    hide petja
    hide lunts

    stop sound1

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Что это?"

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Не знаю. Идем!"

    hide lunts

    show zhitov at left
    show pollak at right

    "<{i}Житов. слушает у окна. Поллак поворачивает голову, смотрит на пустую комнату и снова работает. Где-то хлопает дверь; собачий лай.{/i}>"

    hide zhitov
    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(входит).{/i}>"

    stop sound1

    inna_aleksandrovna "Послала людей с Вулканом. Вероятно, кто-нибудь заблудился."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А колокол?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ветер оттуда. Вы слышали, как ясны выстрелы?"

    hide inna_aleksandrovna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    play sound1 footsteps

    pollak "<{i}(входит).{/i}>"

    stop sound1

    pollak "Я ничем не могу быть полезен?"

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Пока нет. Нужно приготовить горячего."

    play sound1 footsteps

    hide inna_aleksandrovna

    show anna at left
    show trejch at truecenter
    show verhovtsev at right

    inna_aleksandrovna "<{i}Хлопает снова дверь. Слышен говор. В сопровождении всех входят закутанные и запорошенные снегом Анна и Трейч и вносят Верховцева.{/i}>"

    hide anna
    hide trejch
    hide verhovtsev

    show inna_aleksandrovna at truecenter

    stop sound1

    inna_aleksandrovna "<{i}(На пороге.){/i}>"

    inna_aleksandrovna "Что это? Анна?"

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна"

    anna "<{i}(снимая платок).{/i}>"

    anna "Мама, поскорее чего-нибудь горячего. Мы чуть живы. Я боюсь, что Валентин отморозил себе что-нибудь. Скорее!"

    play sound1 punch

    anna "<{i}(В полуобморочном состоянии падает на стул.){/i}>"

    stop sound1

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(быстро подходит к принесенному).{/i}>"

    stop sound1

    inna_aleksandrovna "Валентин! Что такое?"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Он ранен."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(слабо).{/i}>"

    verhovtsev "Не... беспокойтесь, теща, неважно... ноги..."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А это кто?"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Друг."

    hide trejch

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(осматривается с диким ужасом вокруг).{/i}>"

    inna_aleksandrovna "А Коля?"

    hide inna_aleksandrovna

    play sound1 male_cry

    show petja at left
    show inna_aleksandrovna at right

    "<{i}Пауза. Петя. со слезами бросается к Инне Александровне.{/i}>"

    hide petja
    hide inna_aleksandrovna

    stop sound1

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Мамочка, мамочка! Это ничего, ты не пугайся, это ничего."

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    hide inna_aleksandrovna

    show inna_aleksandrovna at left
    show petja at right

    inna_aleksandrovna "<{i}(слегка отстраняя его. более спокойно).{/i}>"

    hide petja

    show inna_aleksandrovna at truecenter

    inna_aleksandrovna "А Коля где?"

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна"

    play sound1 footsteps

    anna "<{i}(приходя в себя и начиная хлопотать около раненого).{/i}>"

    stop sound1

    anna "Ах, мама! Да ничего особенного, он в тюрьме."

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Значит? Постойте, погодите, я ничего не понимаю. Значит?"

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "В тюрьме! В какой тюрьме?"

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Ну, господи, как этого не понять. Мы бежали, вот и все... и хотим укрыться здесь."

    hide anna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Революция кончилась?"

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Но я не понимаю. Неужели?.."

    hide lunts

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Да. Мы разбиты."

    hide trejch

    "<{i}Пауза.{/i}>"

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Мама, да распорядись же относительно горячего! Воды, коньяку... Вата у вас есть?"

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Сейчас все будет. Минна!"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(Идет.){/i}>"

    stop sound1

    inna_aleksandrovna "В тюрьме!.."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А нужно бы позвать Сергея Николаевича."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Я пошлю за ним."

    hide inna_aleksandrovna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Расскажите, пожалуйста, как это случилось... господин..."

    hide pollak

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Трейч."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(слабо).{/i}>"

    verhovtsev "Без Трейча... я бы подох. Анна, да не суетись ты так, я чувствую себя... великолепно."

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Как мы дошли, я не понимаю! Это такой ужас. Мы сегодня с восьми часов в горах. Целый день. Нас чуть не схватили на границе."

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Я не могу поверить..."

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Валя, что у тебя? Тебе больно?"

    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ноги ободраны... осколком и... голова... немного. Вздор."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "В вас посылали бомбы?"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Буржуа... защищался... недурно."

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Валентин, тебе нельзя говорить. Какой это был ужас, какой это был ужас! Бомбы рвали на клочки, убитых тысячи - десятки тысяч. У ратуши я видела гору трупов."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(подходит).{/i}>"

    stop sound1

    inna_aleksandrovna "А Коля? Расскажите мне про Колю."

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "В сущности, неизвестно, где он."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Что? Ты же сказала..."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "И Маруси нет! Вы что-то скрываете. А вот вы говорили, Лунц..."

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Петя, Петя! Да разве я думал! Я не могу поверить..."

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Очень нужно скрывать."

    hide anna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Успокойтесь, госпожа Терновская. Я убежден, что Николай жив."

    hide trejch

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Вон Трейч расскажет. Он был рядом с Колей на баррикаде."

    hide anna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "В последний момент, когда баррикада была почти в руках войск, Николая ранили. Он стоял рядом со мной, и я видел, как он упал."

    hide trejch

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Господи! Опасно? Может быть, убит? Да говорите же!"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Не думаю, чтобы опасно."

    hide trejch

    show frants at truecenter

    $ frants_var = "{noalt}Франц"

    play sound1 footsteps

    frants "<{i}(входит).{/i}>"

    stop sound1

    frants "Господин профессор приказали сказать, что сейчас придут."

    hide frants

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Конечно, чего торопиться!"

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну-ну! Да говорите же!"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Кажется, пулевая или картечная рана в плечо. Вначале он был в сознании, но потом впал в беспамятство. Я донес его до переулка, но здесь встретился отряд драгун."

    trejch "Долго я бороться не мог, тем более что я подвергал его опасности расстрела; и я оставил тело им, а сам вернулся к нашим. Теперь, вероятно, он в тюрьме."

    hide trejch

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 female_cry

    inna_aleksandrovna "<{i}(плачет).{/i}>"

    stop sound1

    inna_aleksandrovna "Колюшка, Колюшка! А мы-то сидим и ничего не знаем. Чуяло мое сердце, чуяло. Ну, не опасно он, скажите? А?"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Не думаю."

    hide trejch

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А Маруся? Отчего вы ничего не скажете про Марусю? Она убита?"

    hide petja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Да нет! Валя, хочешь воды с коньяком?"

    hide anna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Мы видели ее на одну минуту. Она осталась, чтобы разыскать товарища Николая!"

    hide trejch

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ах, Маруська! Молодец, ей-богу! Так и надо, так и надо. Вот скажите, какая девушка! Как вас, - Трейч... хотите коньяку? На вас лица нет. Выпейте, голубчик. Я бы вас поцеловала, да знаю, что ваш брат этого не любит."

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Сочту за особенную честь."

    hide trejch

    "<{i}Целуются.{/i}>"

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ах ты, Маруська, Маруська! И этот тоже... Минна!"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(Выходит.){/i}>"

    stop sound1

    hide inna_aleksandrovna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(почти в безумии).{/i}>"

    lunts "Значит, напрасно?"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "По-видимому."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Значит, напрасно вся эта кровь, эти тысячи жертв, эта беспримерная борьба, эта... эта... Проклятье! Зачем я был здесь? Зачем я не лег там, с моими братьями?"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Как же... вы хотите, чтобы... буржуа... сразу отдал... свое владычество над землей? Буржуа... не дурак. И лечь еще успеете."

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Борьба не кончена."

    hide trejch

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Вы рабочий, господин Трейч?"

    hide pollak

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Рабочий. Кстати: я не сказал госпоже Терновской, так как не хотел тревожить ее напрасно, что Николай, может быть, расстрелян."

    hide trejch

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Расстрелян!"

    hide petja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Уже по дороге сюда я слыхал, что они расстреливают всех пленных без суда... и раненых также."

    hide trejch

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(вздрагивает и закрывает лицо руками).{/i}>"

    petja "Какой ужас!"

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Звери! Они всегда питались человеческой кровью. Они сыты ею по горло."

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да... они никогда не были... вегета... рианцами."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Как можете вы шутить."

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Валя, ведь тебе же нельзя говорить."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Это ободранные... ноги приводят меня в такое... настроение. Я замолчу, Анна, я устал. Мне только... интересно взглянуть... на физиономию звездочета."

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Тише."

    play sound1 footsteps

    hide trejch

    show trejch at left
    show inna_aleksandrovna at right

    trejch "<{i}Входит Инна Александровна.{/i}>"

    hide inna_aleksandrovna

    show trejch at truecenter

    stop sound1

    trejch "Они борются, и мы, конечно, не можем предписывать им правил борьбы."

    hide trejch

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "А вот и Сергей Николаевич."

    hide zhitov

    show sergej_nikolaevich at truecenter

    "<{i}Наверху лестницы показывается Сергей Николаевич и на ходу бросает.{/i}>"

    hide sergej_nikolaevich

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Что это? Где Николай?"

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Не пугайся, отец. Он ранен, в тюрьме."

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(останавливаясь, сверху).{/i}>"

    sergej_nikolaevich "Разве там еще убивают? Разве там еще есть тюрьмы?"

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(злобно).{/i}>"

    verhovtsev "С неба... свалился."

    hide verhovtsev

    "<{i}Занавес{/i}>"

label Act_2:
    play music "audio/music/3.mp3" fadeout 1.0 fadein 1.0

    scene 1 with fade


label Act_2_Scene_1:
    "{b}ДЕЙСТВИЕ ВТОРОЕ{/b}"

    "<{i}Весеннее ясное утро в горах; небо безоблачно; все залито солнцем.{/i}>"

    play sound1 footsteps

    "<{i}Справа, в глубине, угол здания обсерватории с уходящей вверх башней; середина - двор, по которому проложены асфальтовые дорожки, как в монастырях; двор неровный, опускается вниз, в задней стороне сцены, где низкий каменный забор и ворота.{/i}>"

    stop sound1

    play sound1 footsteps

    "<{i}За ним цепь гор, но не выше той, на которой расположена обсерватория. Слева и ближе к авансцене угол дома с каменной верандой над обрывом. Полное отсутствие растительности. Со времени первого действия прошло три недели.{/i}>"

    stop sound1

    show verhovtsev at left
    show anna at truecenter
    show zhitov at right

    "<{i}Верховцев в кресле на колесах: его возит взад и вперед Анна. Житов сидит у стены-греется на солнце. Все одеты по-весеннему, кроме Житова, который в одном пиджаке.{/i}>"

    hide verhovtsev
    hide anna
    hide zhitov

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов"

    zhitov "<{i}(сидит).{/i}>"

    zhitov "А то дали бы мне, Анна Сергеевна, я бы повозил."

    hide zhitov

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Нет, уж сидите, никого не люблю утруждать. Тебе хорошо, Валя?"

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Хорошо, только за каким чертом вертимся мы здесь, как крысы в крысоловке. Поставь меня рядом с Житовым, я тоже хочу запастись энергией от солнца. Так, хорошо. Приятно!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Отчего вы не работаете, Житов?"

    hide anna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Погода такая.. Я как взыграет весеннее солнце, так уж не могу в комнатах сидеть. Вот погреюсь, погреюсь, да и..."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Житов, а вы не турок?"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А как вам бы шло: сесть этак да на пупок смотреть, или как там..."

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет, я не турок."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А я вас понимаю: приятно на солнышке. Жалко Николу: ему этого удовольствия не получить. Я знаю эту Штернбергскую тюрьму: в нее не только солнце не заглядывает, в ней и неба-то не видно."

    verhovtsev "Я в ней только месяц просидел, так и то в какой-то сплошной компресс превратился от сырости. Мерзость!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Хорошо, что хоть жив. Я была убеждена, что его расстреляли."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Погоди, за этим еще дело не станет. Нужно бы разбудить Маруську, узнать все поскорее."

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Она поздно приехала."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Слыхал. Весь дом пением разбудила. Я даже удивился, кто может петь в этом мавзолее. Подумал, уж не Поллак ли новую звезду открыл."

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Раз поет, значит, все хорошо."

    hide zhitov

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Я не понимаю этого: петь, когда все спят."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(показывается на веранде).{/i}>"

    inna_aleksandrovna "А Лунц не приходил?"

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Нет."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Господи, что же это! Его Сергей Николаевич спрашивает, - ну что я скажу? Разбрелись все, как овцы, один Поллак работает. А Марусечка-то вчера - запела! Как я услышала - дух захватило... Ну, думаю..."

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Разбудите-ка ее, теща."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ни-ни. И не думай. Пусть хоть до вечера спит."

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ну, Шмидта этого."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "И Шмидта не стану будить. Человек с дороги, такую радость привез, а я ему поспать не дам! Вот вы этого Лунца пришлите, когда вернется."

    play sound1 footsteps

    inna_aleksandrovna "<{i}(Идет и у двери останавливается.){/i}>"

    stop sound1

    inna_aleksandrovna "Солнышко-то греет, Василий Васильевич! Как у нас. Я нынче утром в ящик земли насыпала да редиску посеяла. Пусть растет, кое-кому пригодится!"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(Уходит.){/i}>"

    stop sound1

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Энергичная старушка. Редиска, хм!"

    hide verhovtsev

    "<{i}Пауза.{/i}>"

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Вы думаете о чем-нибудь, Житов, когда вот так уставитесь?"

    hide anna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет. Зачем думать? Я так смотрю."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Врете вы. Как можно не думать, -ну, если не думаете, так вспоминаете что-нибудь."

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "У меня воспоминаний не бывает. А впрочем... хорошо в Нью-Йорке было: жил я в гостинице на самой шумной ихней улице, и балкон у меня был..."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ну?"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Так вот: хорошо очень было. Сидишь и смотришь: как это они там ходят, ездят. Воздушная дорога. Интересно."

    hide zhitov

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "У американцев высокая культура."

    hide anna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет, я не об этом. А так, интересно очень."

    zhitov "<{i}Пауза.{/i}>"

    zhitov "А правда, где Лунц?"

    hide zhitov

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Вчера еще с вечера с Трейчем ушел в горы."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "На исследования?"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Исследования?"

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Трейч всегда что-нибудь исследует. Он уже, наверное, исследовал ваш храм Урании и решил, что он может быть превосходным складом для оружия. Теперь он исследует горы: вероятно, ищет места для оружейного завода."

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Трейч - фантазер."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ну, не совсем. В его фантазиях есть странная черта. При всем иногда явном безумии они как-то осуществляются."

    verhovtsev "Вообще любопытный малый. Говорит немного, а пропагандировать никто так не умеет, как он. Выражаясь вашим астрономическим языком, -он луну заставит разгореться, как солнце. Откуда его Николай вытащил, не знаю."

    hide verhovtsev

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    play sound1 footsteps

    petja "<{i}(входит).{/i}>"

    stop sound1

    petja "Добрый день."

    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Что это ты. Петушок, такой хмурый?"

    hide verhovtsev

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Так."

    hide petja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Ты знаешь? Николай в тюрьме."

    hide anna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Знаю, мне мама говорила."

    hide petja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Я не понимаю, отчего ты киснешь. Точно уксусу напился - противно смотреть."

    hide anna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "И не смотри."

    hide petja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Петя, поедемте со мной в Австралию."

    hide zhitov

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Зачем?"

    hide petja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Ты, как маленькие дети, все - зачем, зачем? Его вчера в горы зовут, а он: \"Зачем?\" А зачем ты ешь?"

    hide anna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Не знаю. Отстань от меня, Анна."

    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Не могу сказать, чтобы ты был чрезмерно вежлив, мой друг. А вот и наши!"

    hide verhovtsev

    show verhovtsev at left
    show trejch at truecenter
    show lunts at right

    verhovtsev "<{i}Показываются забрызганные грязью Трейч и Лунц.{/i}>"

    hide trejch
    hide lunts

    show verhovtsev at truecenter

    verhovtsev "Лунц, вас звездочет спрашивал. Держитесь, влетит вам теперь."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "А ну его к... Виноват, Анна Сергеевна."

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Можете. Я не из нежных дочерей и присоединяюсь к вашему пожеланию."

    hide anna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Как это пошло!"

    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ну, как погуляли, Трейч? Нашли что-нибудь?"

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Местность хорошая."

    hide trejch

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "А вы знаете, что Маруся ночью приехала?"

    hide anna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч"

    trejch "<{i}(делая шаг вперед).{/i}>"

    trejch "Ну?! Николай? Николай?"

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Расстрелян. Повешен. Колесован."

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Да нет-жив, жив!"

    hide anna

    show marusja at truecenter

    "<{i}За окном музыка и пение Маруси.{/i}>"

    hide marusja

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "\"Сижу за решеткой в темнице сырой - вскормленный на воле орел молодой...\""

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Он в тюрьме? Спасен?"

    hide trejch

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "\"Мой грустный товарищ, махая крылом, кровавую пищу клюет под окном...\""

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(поет){/i}>"

    verhovtsev "\"Клюет-и бросает, и смотрит в окно, как будто со мною задумал одно."

    verhovtsev "- Зовет меня взглядом и криком своим - и вымолвить хочет: давай улетим\"."

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    play sound1 footsteps

    marusja "<{i}(выходит, страстно){/i}>"

    stop sound1

    marusja "\"Мы вольные птицы! Пора, брат, пора"

    marusja "- туда, где за тучей белеет гора,"

    marusja "- туда, где синеют морские края,"

    marusja "- туда, где гуляют - лишь ветер да я!\""

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Маруся!"

    hide trejch

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Какой неуместный концерт!"

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 footsteps

    inna_aleksandrovna "<{i}(идет сзади, утирая глаза).{/i}>"

    stop sound1

    inna_aleksandrovna "Орлятки вы мои..."

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вы, теща, произносите совершенно так же, как: цыплятки вы мои..."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да и цыплятки: вон ты как ощипан, хоть сейчас в суп."

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Анна, здравствуйте!"

    hide marusja

    show marusja at left
    show trejch at right

    marusja "<{i}(Трейчу.){/i}>"

    hide trejch

    show marusja at truecenter

    marusja "Вам - поцелуй!"

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч"

    trejch "<{i}(быстро закрывает рукой глаза и тотчас отнимает руку).{/i}>"

    trejch "Я счастлив."

    hide trejch

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "И всем, и всем. Тебе, инвалид, тоже."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да ты видела его?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Давай улетим!"

    hide marusja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Это даже нехорошо. Все так хотят знать..."

    hide lunts

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "И видела, и все... Да... вот этот господин... этот Шмидт, позвольте представить. Это удивительный господин. Пока он так, служит в банке, но со временем окажет массу услуг для революции. Он страшно похож на шпиона, и он так помог мне... Кланяйтесь, Шмидт."

    hide marusja

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "Я очень рад. Добрый день."

    hide shmidt

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Петя, милый мальчик, отчего ты такой грустный?"

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Это, Маруся, выражаясь скромно, -свинство."

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Ну-ну, калека, не сердись. Разве можно сегодня сердиться? Ну, он в Штернбергской тюрьме..."

    hide marusja

    show inna_aleksandrovna at left
    show lunts at truecenter
    show trejch at right

    $ inna_aleksandrovna_var = "{noalt}Голоса."

    inna_aleksandrovna "Знаем."

    inna_aleksandrovna "- Знаем."

    hide inna_aleksandrovna
    hide lunts
    hide trejch

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Ну - и хотели его расстрелять."

    hide marusja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Господи, Колю-то?!"

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Успокойтесь, мамочка, ничего этого не будет. А я - графиня Мориц. Родовитая ужасно, но только родовые поместья мои там."

    marusja "<{i}(Обводит рукой по воздуху.){/i}>"

    marusja "А они злы, но страшно глупы."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да, есть-таки."

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Труднее всего было узнать, где он. Они скрывают имена захваченных, чтобы иметь возможность тихонько, без суда - расправиться с ними. Но тут помог мне Шмидт. Шмидт, кланяйтесь."

    hide marusja

    play sound1 footsteps

    show sergej_nikolaevich at truecenter

    "<{i}Входит Сергей Николаевич. Он в потертом пальто и маленькой меховой шапочке; приветствуют его почтительно, но холодно.{/i}>"

    hide sergej_nikolaevich

    stop sound1

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Отец, ты послушай, что Маруся рассказывает. Они его расстрелять хотели!"

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Так вот. Долго рассказывать. Одним словом, я грозила, умоляла, ссылаясь на общественное мнение Европы, на ученый авторитет его отца, - и расправа отложена. И я была в тюрьме..."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ну, как он?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(затуманиваясь).{/i}>"

    marusja "Он... немного грустен, но это пройдет, конечно."

    hide marusja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А рана?"

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Это пустяки. Уже зарубцевалась, он ведь такой крепкий. Но что это за камера: это подвал, погреб, болото - я не знаю, как назвать."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Знаю, сиживал."

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Но я подняла такой шум, что его обещали перевести в лучшую. Вам, Сергей Николаевич, он крепко жмет руку, желает успеха в работе и вообще очень интересуется, как у вас..."

    hide marusja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "В таком положении - и думать о пустяках."

    hide anna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Милый мальчик! Я очень благодарен ему."

    hide sergej_nikolaevich

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Как великодушно!"

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Но как же вы-то сами? Как вас не схватили?"

    hide lunts

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Меня и схватили солдаты-в тот день. Но я так плакала, я так безумно рыдала о больной бабушке, которая ждет меня из магазина, что меня отпустили. Один, правда, слегка ударил прикладом..."

    hide marusja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Какая гнусность!"

    hide lunts

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "А у меня под юбкой знамя было. Наше знамя."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Оно цело?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Я приколола его английскими булавками - но какое оно тяжелое! Я привезла его сюда. В этот раз оно заменяло Шмидту фуфайку. Вообще, если бы Шмидт не был такого маленького роста..."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Он был бы большого. Отчего ты не принесла его сюда? Взглянул бы... Наше знамя! Черт возьми, а?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Нет, я разверну его, когда мы снова пойдем в битву, Трейч, вы знаете, кто предал нас?"

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Знаю."

    hide trejch

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "Изменников и предателей нужно карать смертью."

    hide shmidt

    play sound1 female_laughter

    show marusja at left
    show trejch at right

    "<{i}Маруся смеется. Трейч слегка улыбается.{/i}>"

    hide marusja
    hide trejch

    stop sound1

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Какой вы, однако, кровожадный, господин Шмидт."

    hide verhovtsev

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "Можно убивать электричеством, тогда без крови."

    hide shmidt

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну, а Колюшка-то!"

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Николай? Ну слушайте. Здесь нет никого? Прислуга у вас? Ну хорошо. Так вот - бежать."

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Я поеду с вами."

    hide trejch

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Нет, Трейч, Коля велел вам оставаться здесь. Вы знаете, как вас ищут."

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Это не имеет значения."

    hide trejch

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да и не нужно: я уже все устроила, все готово, а вы здесь, Трейч, на границе, займетесь кое-чем. Нужны только деньги - много денег; вместе с Колей бегут один солдат и смотритель. И, конечно, он приедет сюда - это само собой."

    marusja "И я сегодня же еду, - нельзя терять ни минуты."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ловко, Маруся!"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Голубчик, я так счастлива!"

    hide marusja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    hide inna_aleksandrovna

    show inna_aleksandrovna at left
    show sergej_nikolaevich at right

    inna_aleksandrovna "<{i}(смотрит на Сергея Николаевича).{/i}>"

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    inna_aleksandrovna "Деньги?"

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    hide sergej_nikolaevich

    show sergej_nikolaevich at left
    show inna_aleksandrovna at right

    sergej_nikolaevich "<{i}(смотрит на Инну Александровну).{/i}>"

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    sergej_nikolaevich "А у нас есть деньги? Инна, ты заведуешь этим делом."

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(смущенно).{/i}>"

    inna_aleksandrovna "Только те три тысячи..."

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Нужно пять."

    hide marusja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да и те..."

    hide inna_aleksandrovna

    show inna_aleksandrovna at left
    show sergej_nikolaevich at right

    inna_aleksandrovna "<{i}(Смотрит на Сергея Николаевича, тот молча кивает головой; радостно.){/i}>"

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    inna_aleksandrovna "Ну, вот три тысячи и есть. Слава богу!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов"

    zhitov "<{i}(конфузясь).{/i}>"

    zhitov "Можно собрать. Вот у меня есть двести рублей."

    hide zhitov

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Поллак - богатый человек, очень богатый."

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Неприятно к нему обращаться. Он такой сухарь."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Пустое. Вот таких и нужно обдирать! Петя, позови-ка сюда Поллака... скажи - важно, а то не пойдет."

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Ну вот, главное сделано, деньги есть."

    marusja "<{i}(Поет.){/i}>"

    marusja "\"Зовет меня взглядом и криком своим - и вымолвить хочет: давай улетим!\" Трейч, мне надо с вами поговорить. Какой вы грязный! Где вы были?"

    hide marusja

    play sound1 footsteps

    "<{i}Уходят.{/i}>"

    stop sound1

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Какая девушка! Это - солнце! Это вихрь огненных сил! Это Юдифь!"

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Да, слишком много огня. Революция не нуждается в ваших вихрях и взрывах - это, если хотите знать, ремесло, в которое нужно вносить терпение, настойчивость и спокойствие. А эти вихри..."

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "И для революции нужен талант."

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Не знаю. Люди уж очень злоупотребляют этим словом - талант. На канате хорошо ломается - талант. На звезды всю жизнь смотрят..."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да. А как у вас, уважаемый звездочет, обстоят дела на небе?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Хорошо. А у вас на земле?"

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Довольно скверно, как видите. На земле всегда скверно, уважаемый звездочет, всегда кто-нибудь кого-нибудь душит; кто-то плачет, кто-то кого-то предает... Ноги вот болят. Нам далеко до гармонии небесных сфер."

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Там не всегда гармония. Там также бывают катастрофы."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Очень жаль... значит, и на небо надежда потеряна. А вы о чем задумались, господин... господин... Шмидт?"

    hide verhovtsev

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "Я думаю, что всякий человек должен быть сильным."

    hide shmidt

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ого! А вы сильны?"

    hide verhovtsev

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "К сожалению, нет. Природа при рождении лишила меня некоторых свойств, которые составляют силу. Я очень боюсь крови и..."

    hide shmidt

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "И пауков? Кстати: вы платье готовое покупаете или на заказ?"

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    play sound1 footsteps

    pollak "<{i}(подходит).{/i}>"

    stop sound1

    pollak "Чем могу служить? Добрый день, господа!"

    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вот что, Поллак: нужны две тысячи... не скажу, чтобы взаймы, потому что едва ли вам их кто отдаст..."

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "А для какой надобности, смею спросить?"

    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Надо устроить бегство Николая Сергеевича. Можете дать?"

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "С удовольствием."

    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Он..."

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Нет, нет, прошу без подробностей. Уважаемый Сергей Николаевич, могу я сегодня воспользоваться вашим рефрактором?"

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Пожалуйста. Сегодня у меня праздник."

    hide sergej_nikolaevich

    play sound1 footsteps

    show pollak at truecenter

    "<{i}Поллак уходит, кланяясь.{/i}>"

    hide pollak

    stop sound1

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вот это ученый. Хорош, Сергей Николаевич?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он очень способный."

    hide sergej_nikolaevich

    show anna at truecenter

    $ anna_var = "{noalt}Анна"

    anna "<{i}(вообще).{/i}>"

    anna "А для чего существует астрономия?"

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Для календарей, должно быть."

    hide verhovtsev

    play sound1 footsteps

    show marusja at left
    show trejch at right

    "<{i}Маруся и Трейч подходят.{/i}>"

    hide marusja
    hide trejch

    stop sound1

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Так вы сделаете это, Трейч... На вас нападают, Сергей Николаевич? Анна так ненавидит астрономию, как будто это ее личный враг."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Я уже привык к этому, Маруся."

    hide sergej_nikolaevich

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "У меня нет личных врагов, вы это хорошо знаете. А астрономию я не люблю потому, что не понимаю, как люди могут столько времени глазеть на небо, когда на земле все устроено так плохо."

    hide anna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Астрономия - торжество разума."

    hide zhitov

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "По-моему, разум больше бы торжествовал, если бы на земле не было голодных."

    hide anna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Какие горы! Какое солнце! Как вы можете говорить, спорить, когда так светит солнце!"

    hide marusja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Вы как будто против науки, Анна Сергеевна!"

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Не против науки, а против ученых, которые науку делают предлогом, чтобы уклониться от общественных обязанностей."

    hide anna

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "Человек должен говорить: \"я хочу\", обязанность - это рабство."

    hide shmidt

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Не люблю я этих разговоров, и охота людям себе кровь портить. Василий Васильевич... да подымитесь же! Вот что"

    hide inna_aleksandrovna

    show inna_aleksandrovna at left
    show shmidt at right

    inna_aleksandrovna "<{i}(отводит его к веранде){/i}>"

    hide shmidt

    show inna_aleksandrovna at truecenter

    inna_aleksandrovna ": вы денег-то своих не давайте. Хватит. Поллак - очень великодушный молодой человек и, в случае чего..."

    play sound1 female_laughter

    inna_aleksandrovna "<{i}(Смеется.){/i}>"

    stop sound1

    inna_aleksandrovna "А все-таки - астролябия."

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Как же теперь ваша экспедиция в Канаду, Инна Александровна? Деньги-то?"

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну, достану! Год еще впереди. Я ловка денег доставать. А вы вот что, Василий Васильевич, прошу вас, как друга: нападать они будут на моего старика, - рады, что он молчит, - так вы уж постойте за него, хорошо?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Хорошо."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А я пойду. Нужно Колюшке белье приготовить, так хлопот много..."

    play sound1 footsteps

    inna_aleksandrovna "<{i}(Уходит.){/i}>"

    stop sound1

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(продолжает).{/i}>"

    sergej_nikolaevich "Я очень люблю хорошие разговоры. Во всех речах я вижу искорки света, и это так красиво, как Млечный Путь. Очень жаль, что люди большею частью говорят о пустяках."

    hide sergej_nikolaevich

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Красивыми словами люди часто отделываются от работы."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вот вы очень спокойный человек, Сергей Николаевич, вы даже неспособны, кажется, обижаться, - а случалось ли вам когда-нибудь плакать? Я, конечно, беру не тот счастливый возраст, когда вы путешествовали без штанов, а вот теперь?.."

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "О да! Я очень слезлив."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вот как!"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Когда я увидел комету Биелу, предсказанную Галлеем, я заплакал."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Причина уважительная, хотя для меня и не совсем понятная. А вы ее понимаете, господа?"

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Да, конечно. Ведь Галлей мог ошибаться."

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Что же, тогда нужно было бы рвать волосы от отчаяния?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Вы преувеличиваете, Валентин."

    hide marusja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "А когда сына чуть не расстреляли, он остался совершенно спокоен."

    hide anna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "В мире каждую секунду умирает по человеку, а во всей вселенной, вероятно, каждую секунду разрушается целый мир. Как же я могу плакать и приходить в отчаяние из-за смерти одного человека?"

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Так, Шмидт, не правда ли, это очень сильно, как раз по-вашему? Так что, если Николаю не удастся бежать, и его..."

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Конечно, это будет очень грустно, но..."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Не шутите так, Сергей Николаевич. Мне больно, когда я слышу такие шутки."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да я и не шучу, милая Маруся. Вообще я никогда не умел шутить, хотя очень люблю, когда шутят другие, например Валентин."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Благодарю вас."

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Это правда, Сергей Николаевич никогда не шутит."

    hide zhitov

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(затуманиваясь).{/i}>"

    marusja "Тем хуже."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Что значит-заткнуть уши астрономической ватой! Хорошо, спокойно. Пусть весь мир взвоет, как собака..."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Когда молодой Будда увидел голодную тигрицу, он отдал ей себя, да. Он не сказал: я бог, я занят важными делами, а ты только голодный зверь, - он отдал ей себя!"

    hide lunts

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Вы видите надпись"

    sergej_nikolaevich "<{i}(показывая на фронтон обсерватории){/i}>"

    sergej_nikolaevich ": \"Наес domus Uraniae est. Curae procul este profanae. Temnitur hic humilis tellus. Hinc ITUR AD ASTRO\". Это значит: \"Это храм Урании. Прочь, суетные заботы! Попирается здесь низменная земля - отсюда идут к звездам\"."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да, но что вы разумеете под суетными заботами, уважаемый звездочет? Вот у меня ноги содраны до кости осколком... это тоже, по-вашему, суетная забота?"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Конечно."

    hide anna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да. Смерть, несправедливость, несчастья, все черные тени земли - вот суетные заботы."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Значит, явись завтра новый Наполеон, новый деспот, и зажми весь мир в железном кулаке - это тоже будет суетная забота?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да... Я так думаю."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    play sound1 male_laughter

    verhovtsev "<{i}(обводит всех взглядом и грубо смеется).{/i}>"

    stop sound1

    verhovtsev "Так вот оно что!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Это возмутительно! Это какие-то боги, которые предоставляют людям страдать, как им угодно, а сами..."

    hide anna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Трейч, почему вы ничего не возразите?"

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Я слушаю."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Так может говорить только тот, кто живет на содержании у правительства и в полной безопасности сидит на своей крыше."

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(слегка краснея).{/i}>"

    sergej_nikolaevich "Не всегда в безопасности, Валентин. Галилей умер в темнице. Джордано Бруно погиб на костре. Путь к звездам всегда орошен кровью."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Мало ли что было... Христиан тоже преследовали, а это не помешало им, в свою очередь, поджаривать на углях невинных астрономов."

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "У отца даже свои мощи есть, и он держит их за железными дверьми."

    hide anna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Анна! Это нехорошо."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Это еще что за чепуха?"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Кусок кирпича от какой-то развалины, - обсерватория развалилась, - да клочки подлинной рукописи."

    hide anna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Анна! Как это неприятно! Коля не позволил бы себе так говорить..."

    hide marusja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Николай слишком деликатен. Это его недостаток."

    hide anna

    play sound1 footsteps

    show petja at truecenter

    "<{i}Подходит Петя. и, незамеченный, молча становится у стены.{/i}>"

    hide petja

    stop sound1

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(раздраженно).{/i}>"

    verhovtsev "Оттого-то нас и бьют на каждом шагу..."

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Не надо! Не надо!.. Трейч, да что же вы!.."

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч"

    trejch "<{i}(сдержанно).{/i}>"

    trejch "Надо идти вперед. Здесь говорили о поражениях, но их нет. Я знаю только победы. Земля - это воск в руках человека. Надо мять, давить - творить новые формы... Но надо идти вперед. Если встретится стена - ее надо разрушить."

    trejch "Если встретится гора - ее надо срыть. Если встретится пропасть - ее надо перелететь. Если нет крыльев - их надо сделать!"

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Хорошо, Трейч! Надо сделать!"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Я уже чувствую крылья!"

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч"

    trejch "<{i}(сдержанно).{/i}>"

    trejch "Но надо идти вперед. Если земля будет расступаться под ногами, нужно скрепить ее - железом. Если она начнет распадаться на части, нужно слить ее - огнем. Если небо станет валиться на головы, надо протянуть руки и отбросить его - так!"

    trejch "<{i}(Отбрасывает.){/i}>"

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "У-ах! Так!"

    hide verhovtsev

    show trejch at truecenter

    "<{i}Некоторые невольно повторяют позу Трейча - Атланта, поддерживающего мир.{/i}>"

    hide trejch

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Но надо идти вперед, пока светит солнце."

    hide trejch

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Оно погаснет, Трейч!"

    hide lunts

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Тогда нужно зажечь новое."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да, да. Говорите!"

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "И пока оно будет гореть, всегда и вечно, - надо идти вперед. Товарищи, солнце ведь тоже рабочий!"

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вот это-астрономия! Ах, черт!"

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Вперед, всегда и вечно."

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вперед! Ах, черт!"

    hide verhovtsev

    "<{i}Все в возбуждении разбиваются на группы.{/i}>"

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(волнуясь).{/i}>"

    lunts "Господа, я прошу... это нельзя так оставить. А убитые! Нет, господа, не только те, кто мужественно боролся и погиб за свободу, а вот эти... жертвы. Ведь их миллиарды, ведь они же не виноваты... И их убили!"

    hide lunts

    "<{i}Молчание.{/i}>"

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(звонко кричит).{/i}>"

    marusja "Клянусь перед вами, горы! Клянусь перед тобою, солнце: я освобожу Николая!.. У этих гор есть эхо?"

    hide marusja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Здесь нет. Но если бы было, оно ответило бы, как в сказке: да!"

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна"

    hide anna

    show anna at left
    show zhitov at right

    anna "<{i}(Житову).{/i}>"

    hide zhitov

    show anna at truecenter

    anna "Как это сентиментально. Я не понимаю Валентина..."

    hide anna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет, ничего. Знаете, я погожу ехать в Австралию: мне тоже захотелось повидать Николая Сергеевича."

    hide zhitov

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(глядя в небо).{/i}>"

    marusja "Как хочется лететь!"

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вот это - астрономия. Ну, как, звездочет, нравятся вам такие астрономы?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да. Нравятся. Его фамилия, кажется, Трейч?"

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Он такой же Трейч, как я-Бисмарк. Сам черт не знает, как его зовут по-настоящему."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    play sound1 footsteps

    hide lunts

    show lunts at left
    show verhovtsev at right

    lunts "<{i}(перебегая от одной группы к другой).{/i}>"

    hide verhovtsev

    show lunts at truecenter

    stop sound1

    lunts "Я счастлив, я так счастлив. Вы знаете... мои родители - они убиты. И сестра. Я не хотел, я никогда не хотел говорить об этом... Зачем говорить? - думал я. Пусть останется глубоко-глубоко в душе, и пусть я один только знаю. А теперь..."

    lunts "Вы знаете, как они были убиты? Трейч, вы понимаете меня? Я никогда не хотел..."

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    hide petja

    show petja at left
    show zhitov at right

    petja "<{i}(Житову).{/i}>"

    hide zhitov

    show petja at truecenter

    petja "Зачем все это?"

    hide petja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет, приятно."

    hide zhitov

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Зачем, когда все это умрет, и вы, и я, и горы. Зачем?"

    hide petja

    show sergej_nikolaevich at left
    show petja at right

    "<{i}Все разбились на группы. Сергей Николаевич. стоит один.{/i}>"

    hide sergej_nikolaevich
    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    hide verhovtsev

    show verhovtsev at left
    show marusja at right

    verhovtsev "<{i}(Марусе, в восторге).{/i}>"

    hide marusja

    show verhovtsev at truecenter

    verhovtsev "Повесить мало Трейча. Ну и откопал Николай. Ну, Марусенька, ведь убежит, а?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(затуманиваясь).{/i}>"

    marusja "Я другого боюсь..."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Чего еще?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Но - не стоит говорить. Пустое."

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да в чем дело? О чем ты задумалась?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    play sound1 female_laughter

    marusja "<{i}(не отвечает; потом неожиданно смеется и поет).{/i}>"

    stop sound1

    marusja "Давай улетим!"

    hide marusja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(высовывается в окно).{/i}>"

    inna_aleksandrovna "Орлятки! Обедать!"

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Цып-цып-цып!"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Будем пить шампанское! Мамочка, есть?"

    hide marusja

    show zhitov at left
    show lunts at truecenter
    show trejch at right

    $ zhitov_var = "{noalt}Голоса."

    zhitov "Да, да. Шампанское."

    hide zhitov
    hide lunts
    hide trejch

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Шампанского нет, киршвассер есть."

    hide inna_aleksandrovna

    play sound1 female_laughter

    "<{i}Смех, восклицания.{/i}>"

    stop sound1

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    hide sergej_nikolaevich

    show sergej_nikolaevich at left
    show marusja at right

    sergej_nikolaevich "<{i}(отводит Марусю).{/i}>"

    hide marusja

    show sergej_nikolaevich at truecenter

    sergej_nikolaevich "Ну, Маруся, я пойду к себе. Я не хочу вам мешать."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(холодно).{/i}>"

    marusja "Нет, отчего же. Сегодня так весело."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да. И я хотел устроить себе маленький праздник ради вашего приезда, но - не вышло."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Пообедайте с нами."

    hide marusja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(кричит).{/i}>"

    lunts "Нужно притащить Поллака. Он порядочный человек, он очень хороший человек. Я иду за ним."

    hide lunts

    show anna at left
    show zhitov at truecenter
    show trejch at right

    $ anna_var = "{noalt}Голоса."

    anna "Поллака!"

    anna "- Поллака!"

    hide anna
    hide zhitov
    hide trejch

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Нет, обедайте без меня."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Как жаль! Инна Александровна будет очень огорчена."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Скажите ей, что я работаю. Перед отъездом вы зайдете ко мне, Маруся?"

    play sound1 footsteps

    sergej_nikolaevich "<{i}(Никем не замеченный, уходит.){/i}>"

    stop sound1

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Шмидт, где вы? Вы будете моим кавалером. Нам еще с вами столько дела. Господа, не правда ли, как он похож на шпиона?"

    hide marusja

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Маруся становится неприлична."

    hide anna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Вы знаете: мне нужно было переночевать у него, а он говорит: нельзя, - я живу в тихом немецком семействе и дал обещание не водить к себе женщин и собак."

    hide marusja

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "И чтоб никто не ночевал. И у меня стоит диван, обитый новым шелком, и они каждый вечер смотрят, не лежит ли на нем какой-нибудь человек. Ужасные люди!"

    hide shmidt

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А вы бы уехали, Шмидт, какого черта!"

    hide verhovtsev

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "Нельзя. Они берут плату вперед."

    hide shmidt

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "А вы бы не давали!"

    hide anna

    show shmidt at truecenter

    $ shmidt_var = "{noalt}Шмидт."

    shmidt "Нельзя, они..."

    hide shmidt

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    hide lunts

    show lunts at left
    show pollak at right

    lunts "<{i}(ведет Поллака, кричит).{/i}>"

    hide pollak

    show lunts at truecenter

    lunts "Вот он! Насилу оторвал. Присосался к рефрактору, как пиявка!"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Господа, это насилие. У меня там не кончено..."

    hide pollak

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Поллак, милый Поллак! Сегодня так весело! И вы такой хороший человек, такой милый, вас так любят все."

    hide marusja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Это очень приятно слышать, но я не знаю, отчего вам так весело? Революция кончилась не в вашу пользу."

    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Мы придумали новый план. Мы..."

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    pollak "<{i}(отмахивается рукой).{/i}>"

    pollak "Да, да. Я верю, я верю вам."

    hide pollak

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Мы выпьем за астрономию. Да здравствует орбита!"

    hide marusja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Я не могу, к сожалению, принимать алкоголя: он причиняет мне головную боль и тошноту."

    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Лучший напиток для Поллака - машинное масло. Поллак, вы будете пить масло?"

    hide verhovtsev

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Нет. Мы киршвассеру выпьем. Самого чистого киршвассеру!"

    hide marusja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Идем, товарищ. Вы хороший, честный человек."

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(высовываясь).{/i}>"

    inna_aleksandrovna "Да идите же! Что же это, не дозовешься!"

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Сейчас, мамочка, сейчас. Вот Поллак упирается. Что же, господа, неужели мы так и пойдем? Житов, вы умеете петь?"

    hide marusja

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Подтягивать могу."

    hide zhitov

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Марсельезу!"

    hide lunts

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Нет, нет. Марсельезу, как и знамя, нужно беречь для боя."

    hide marusja

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Я согласен. Есть песни, которые можно петь только в храме."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Повеселей что-нибудь! Эх, как греет солнце!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Валя, не раскрывай ног."

    hide anna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(запевает){/i}>"

    marusja "Небо так ясно, - солнце прекрасно, - солнце зовет..."

    hide marusja

    show marusja at left
    show petja at right

    marusja "<{i}Все, кроме Пети, подхватывают.{/i}>"

    hide petja

    show marusja at truecenter

    marusja "В веселой работе - чужды заботе, - братья, вперед."

    marusja "Слава веселому солнцу! Солнце - рабочий земли!"

    marusja "Слава веселому солнцу! Солнце - рабочий земли!"

    hide marusja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да поживей, Аня! Ты везешь меня, как покойника."

    hide verhovtsev

    show marusja at left
    show shmidt at truecenter
    show pollak at right

    $ marusja_var = "{noalt}Все"

    hide marusja
    hide shmidt
    hide pollak

    show marusja at left
    show shmidt at truecenter
    show pollak at right

    marusja "<{i}(поют. Поллак серьезно и сдержанно дирижирует){/i}>"

    hide pollak

    show marusja at left
    show shmidt at right

    marusja "Грозы и бури - ясной лазури - не победят."

    marusja "Под бури покровом, в мраке грозовом - молньи горят!"

    marusja "Слава могучему солнцу! Солнце - властитель земли!.."

    hide marusja
    hide shmidt

    play sound1 footsteps

    show petja at truecenter

    "<{i}Последние слова песни повторяются за углом дома. Петя. остается один и угрюмо смотрит вслед ушедшим.{/i}>"

    hide petja

    stop sound1

    show marusja at left
    show shmidt at truecenter
    show pollak at right

    $ marusja_var = "{noalt}Все"

    marusja "<{i}(за сценой){/i}>"

    marusja "Слава могучему солнцу! Солнце-властитель земли!.."

    hide marusja
    hide shmidt
    hide pollak

    "<{i}Занавес{/i}>"

label Act_3:
    play music "audio/music/7.mp3" fadeout 1.0 fadein 1.0

    scene 5 with fade


label Act_3_Scene_1:
    "{b}ДЕЙСТВИЕ ТРЕТЬЕ{/b}"

    play sound1 footsteps
    play sound2 piano

    "<{i}Большая темная комната, нечто вроде гостиной. Мебели мало, ничего мягкого, два книжных шкафа, пианино. Задняя стена: дверь и два большие итальянские окна выходят на веранду.{/i}>"

    stop sound1
    stop sound2

    show inna_aleksandrovna at left
    show anna at right

    "<{i}Окна и дверь открыты, и видно темное, почти черное небо, усеянное необыкновенно яркими мигающими звездами. В уму у стены, ближе к авансцене, стол, на нем под темным абажуром лампа. За столом Инна Александровна читает газеты. Анна что-то шьет.{/i}>"

    hide inna_aleksandrovna
    hide anna

    play sound1 footsteps

    show lunts at left
    show verhovtsev at truecenter
    show inna_aleksandrovna at right

    "<{i}Лунц ходит взад и вперед. У одного из шкапов Верховцев на костылях, достает книгу. Глубокая тишина, какая бывает только в горах. Молчание продолжается некоторое время после открытия занавеса.{/i}>"

    hide lunts
    hide verhovtsev
    hide inna_aleksandrovna

    stop sound1

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(бормочет).{/i}>"

    verhovtsev "А, черт!"

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Валя, ты читал, что президент отказал Кассовскому в помиловании?"

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Читал."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Что же это такое, а?"

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Расстреляют."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Докуда же это будет, господи? Неужели и так мало жертв?"

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(несет книгу под мышкой, роняет).{/i}>"

    verhovtsev "А, чтоб тебя черт... Анна, подними."

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна"

    anna "<{i}(медленно встает).{/i}>"

    anna "Сейчас."

    hide anna

    play sound1 footsteps

    show lunts at truecenter

    "<{i}Лунц молча поднимает книгу, кладет на стол и продолжает ходить.{/i}>"

    hide lunts

    stop sound1

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    hide verhovtsev

    show verhovtsev at left
    show anna at right

    verhovtsev "<{i}(медленно садится, перелистывает книгу; Анне).{/i}>"

    hide anna

    show verhovtsev at truecenter

    verhovtsev "Неужели тебе не надоест ковырять?"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Нужно же что-нибудь делать."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Читала бы."

    hide verhovtsev

    show verhovtsev at left
    show anna at right

    verhovtsev "<{i}Анна не отвечает. Молчание.{/i}>"

    hide anna

    show verhovtsev at truecenter

    verhovtsev "Нет, не могу. Какая дьявольская тишина, как в гробу! Еще неделя такая, и я брошусь в пропасть, запью, побью Поллака."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(нервно).{/i}>"

    lunts "Ужасная тишина! Точно осуществился сон Байрона: солнце погасло, все уже умерло на земле, и мы - последние люди. Ужасная тишина!"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Житов, вы что там делаете?"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов"

    zhitov "<{i}(с веранды).{/i}>"

    zhitov "Смотрю."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(презрительно).{/i}>"

    verhovtsev "\"Смотрю\"!"

    verhovtsev "<{i}Молчание.{/i}>"

    verhovtsev "Не могу я без работы!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Что же поделаешь, надо терпеть."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Терпи ты, если хочешь, а я... Черт!"

    verhovtsev "<{i}(Читает.){/i}>"

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    inna_aleksandrovna "<{i}(сидит, задумавшись).{/i}>"

    inna_aleksandrovna "Сереженьке теперь было бы двадцать один год уж... Красивый он был мальчик, на Колю похож был... Анюта, ты его помнишь?"

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Нет."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А я так помню... Ты, Анюта, била его, ты злая была маленькая. И как скрутило быстро - в три дня. Воспаление слепой кишки - у такого-то крошки! Как стали резать ему животик, так, поверите ли, Иосиф Абрамович..."

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да ну вас, ей-богу! Весь вечер сегодня все о покойниках. Ну, умер и умер, и хорошо сделал, что умер. Житов, идите сюда разговаривать!"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Сейчас."

    hide zhitov

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Какая тоска!"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А что Маруся-то пишет, Инна Александровна?"

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    play sound1 female_sigh

    inna_aleksandrovna "<{i}(со вздохом).{/i}>"

    stop sound1

    inna_aleksandrovna "Пишет много, да толку не добьешься. Обещает через неделю, а там опять что-нибудь задержало, а там опять через неделю. Вот и во вчерашнем письме то же..."

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Знаю, знаю, я думал, нет ли чего нового."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Уж не заболел ли Колюшка?"

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Так и заболел уж! Скажите еще: умер."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Она тогда мертвого его украдет и привезет."

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да что вы? Что вы говорите-то, подумайте!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов"

    play sound1 footsteps

    zhitov "<{i}(входит).{/i}>"

    stop sound1

    zhitov "Ну, о чем говорить?"

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Садитесь. Вы что там делаете?"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "На звезды смотрел. Какие они сегодня красивые и беспокойные."

    hide zhitov

    play sound1 footsteps

    show petja at left
    show zhitov at right

    "<{i}Входит Петя.. Вообще в течение действия он несколько раз проходит сцену.{/i}>"

    hide petja
    hide zhitov

    stop sound1

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "А я сегодня не могу смотреть на звезды. Я не знаю, куда бы от них ушел, я спрятался бы в подвал, но и там я буду их чувствовать. Понимаете: как будто нет расстояний."

    lunts "Как будто все эти громады, живые и мертвые, столпились над землей и приближаются к ней, и что-то такое в них есть... Я не знаю."

    play sound1 footsteps

    lunts "<{i}(Ходит, продолжая жестикулировать.){/i}>"

    stop sound1

    hide lunts

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Атмосфера тут очень чистая. Вот в Калифорнии..."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А вы были в Калифорнии?"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Был. Вот в Калифорнии, на обсерватории Лика, так, правда, иногда жутко смотреть."

    hide zhitov

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Мама, откуда у вас в кухне эта старуха?"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Какая? А, эта-то? Пришла, я и велела ее приютить. Снизу она, из долины. Нищенка, что ли, глухая, у нее не поймешь."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Как же она взошла на гору? Как она могла?"

    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вам бы тут, теща, богадельню устроить."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А что ты думаешь? Может быть, и устрою, если Сергей Николаевич согласится. Ты почитал бы..."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(настойчиво).{/i}>"

    petja "Мама, как она взошла?"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да не знаю, голубчик. Ты почитал бы, что Марусечка о голодных детках пишет: Мамочка, хлебца хочу, - ну и пошла мать за хлебом, и уж как она его там достала - и говорить не стоит... Пришла, а девочка-то уже мертвая."

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Благотворительностью ничего не сделаешь."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Что же, так пусть и умирают?"

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Пусть умирают. Иосиф, вы что-то грустны сегодня?"

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Да, Петя, у меня очень тяжелые мысли. Это такая ночь, я не знаю, какая это ночь. Это ночь призраков. Вы смотрели сегодня на звезды?"

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А мне вот весело!"

    petja "<{i}(Бренчит что-то дикое на рояле.){/i}>"

    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Оставь!"

    hide verhovtsev

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(играет и поет).{/i}>"

    petja "Как мне весело!"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Да ну, Петечка, оставь же!"

    hide inna_aleksandrovna

    play sound1 footsteps

    show petja at truecenter

    "<{i}Петя громко захлопывает крышку рояля и выходит на веранду. Молчание.{/i}>"

    hide petja

    stop sound1

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "А Трейч скоро вернется?"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Не вышло... значит, сегодня или завтра. Житов, что вы все молчите?"

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Так. Не хочется говорить что-то."

    hide zhitov

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "У меня такие тяжелые мысли! Такие тяжелые мысли! Так можно убить себя."

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Пустое. Среди астрономов нет самоубийц."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Я плохой астроном. Очень, очень плохой."

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Тем и лучше, вот и займитесь чем-нибудь дельным."

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Я сегодня боюсь звезд."

    lunts "Я думаю: какие они огромные, какие они равнодушные и как им нет никакого дела до меня, и я становлюсь такой маленький, такой жалкий - как, знаете, цыпленок, который во время еврейского погрома спрятался куда-нибудь, сидит и ничего не понимает."

    hide lunts

    play sound1 footsteps

    show petja at truecenter

    "<{i}Петя. входит.{/i}>"

    hide petja

    stop sound1

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Звезды - и еврейский погром... Странная комбинация."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    hide inna_aleksandrovna

    show inna_aleksandrovna at left
    show verhovtsev at right

    inna_aleksandrovna "<{i}(предостерегающе кивает головой Верховцеву).{/i}>"

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    inna_aleksandrovna "Это оттого, Иосиф Абрамович, что у всех нас нервы развинтились. Ведь подумать только: уже полтора месяца, как уехала Маруся, а ничего нет. Я сама, на что ко всему привычный человек, а и то вздрагивать начала."

    hide inna_aleksandrovna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Летает пух, звенят стекла, а он сидит - и что он думает?"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ничего не думает. Думает, что снег идет."

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Меня пугает бесконечность. Какая бесконечность? Зачем бесконечность? Вот я смотрю на звезды: одна, десять, миллион - и все нет конца. Боже мой, кому же я жаловаться буду?"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А зачем жаловаться?"

    hide verhovtsev

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Вот я, маленький еврей..."

    play sound1 footsteps

    lunts "<{i}(Ходит, продолжая жестикулировать.){/i}>"

    stop sound1

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    play sound1 footsteps

    pollak "<{i}(входит).{/i}>"

    stop sound1

    pollak "Добрый вечер. Я могу, господа, посидеть с вами? Я не помешаю?"

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Конечно, нет. Пожалуйста."

    hide inna_aleksandrovna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Магнитная стрелка очень колеблется, Лунц. Завтра нужно наблюдать солнце."

    hide pollak

    show pollak at left
    show lunts at right

    pollak "<{i}Лунц что-то бормочет.{/i}>"

    hide lunts

    show pollak at truecenter

    pollak "Вам я уж не говорю, Житов, - вы, по-видимому, окончательно бросили занятия. Вы уезжаете?"

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да. Послезавтра."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Что это? Ведь вы же, Василий Васильевич, хотели подождать Колюшку? Как же это вы так? сразу?"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да нет же. Надо ехать. Засиделся."

    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вот будет тощища, как вы уедете. Пошлите вы к черту эту Зеландию."

    hide verhovtsev

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Нет, надо."

    hide zhitov

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "А вы что же не работаете, господин Поллак?"

    hide anna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Сегодня я мечтаю, уважаемая Анна Сергеевна. Сегодня мне исполнилось тридцать два года, и именно в эту минуту. Я родился вечером, в десять часов тридцать семь минут. Вычитая разницу во времени, получается"

    pollak "<{i}(смотрит на часы){/i}>"

    pollak "как раз десять часов шестнадцать минут."

    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Поздравляю."

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Благодарю вас. И я сегодня немного мечтаю. В мои тридцать два года я уже сделал довольно много для науки, и мое имя... Впрочем, я не буду входить в подробности. И я уже имею право устраивать личную жизнь."

    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да неужели вы женитесь? Вот так штука!"

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Да, вы угадали. Я женюсь."

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "И хорошо делаете, голубчик. Только бы жена попалась хорошая."

    hide inna_aleksandrovna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Моя невеста в этом году оканчивает курс в университете, и скоро, уважаемая Инна Александровна, ваше уютное жилище перестанет считать меня своим членом."

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Вот какой тихоня! И как-то вы ни разу не проговорились."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(резко).{/i}>"

    petja "Я тоже женюсь. У меня тоже есть невеста. Красавица!"

    hide petja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Да? Вы шутите?"

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Петя!"

    hide inna_aleksandrovna

    play sound1 footsteps
    play sound2 male_laughter

    show petja at truecenter

    "<{i}Петя. хохочет и уходит на веранду.{/i}>"

    hide petja

    stop sound1
    stop sound2

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Что это с ним? Как распустился!"

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "И не знаю. С того дня, как вы приехали, прямо узнать нельзя. Иосиф Абрамович, вы ближе с Петей, не знаете, что с ним такое? Беспокоюсь я."

    hide inna_aleksandrovna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "С Петей? Он хороший мальчик, честный мальчик. И у него тоже тяжелые мысли."

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Итак, продолжайте, господа... Я сегодня немного нервно настроен и с удовольствием послушаю вашу беседу."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(бормочет).{/i}>"

    lunts "Звезды, звезды..."

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Что вы хотите рассказать нам о звездах, дорогой Лунц?"

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Вот и тогда они светили где-то над тучами, когда мы сидели, и ждали, и думали, что там уже полная победа, и теперь они светят... Можно с ума сойти..."

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Работать, работать надо, а тут сидишь как на цепи, в этом чертовом гробу. Эх!"

    play sound1 footsteps

    verhovtsev "<{i}(Ковыляет по комнате к окну, смотрит некоторое время и возвращается обратно.){/i}>"

    stop sound1

    verhovtsev "Кажется, Трейч вернулся."

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Мне очень нравится господин Трейч. Это очень серьезный человек."

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Значит, опять ничего?"

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(грубо).{/i}>"

    verhovtsev "А вы чего ждали? Ведь вам уже писали, что ничего."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Господи, господи! Колюшка мой, Колюшка! Не дождусь я тебя, голубчика, чует мое сердце."

    play sound1 female_cry

    inna_aleksandrovna "<{i}(Тихо плачет.){/i}>"

    stop sound1

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч"

    play sound1 footsteps

    trejch "<{i}(входит, здоровается со всеми и усаживается).{/i}>"

    stop sound1

    trejch "Добрый вечер!"

    hide trejch

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Устали, голубчик. Поесть не хотите?"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Благодарю вас, я кушал дорогой."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Что нового?"

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Много арестов. О том, что Занько повешен, вы, конечно, знаете?"

    hide trejch

    show verhovtsev at left
    show zhitov at truecenter
    show pollak at right

    $ verhovtsev_var = "{noalt}Голоса."

    verhovtsev "Разве?"

    verhovtsev "- Занько?"

    verhovtsev "- Нет. Когда же это?"

    hide verhovtsev
    hide zhitov
    hide pollak

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Бедный малый! Ну, как он?.."

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Такой молодой!.. Ведь это он был здесь с Колюшкой в прошлом году? Такой черненький, с усиками."

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Да, он."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Руку мне поцеловал... Такой молодой... Мать у него есть?"

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Ах, мама!.. Не знаете, Трейч, не проговорился он?"

    hide anna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Он храбро встретил смерть, хотя с ним поступили подло. Он просил, чтобы при казни присутствовал его защитник: у него нет родных, и он имел на это право. Ему обещали и обманули его, и в последнюю минуту он видел только лица палачей и звезды."

    trejch "Его казнили вечером."

    hide trejch

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Звезды, звезды!"

    hide lunts

    "<{i}Молчание.{/i}>"

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "В Тернахе солдаты убили около двухсот рабочих. Много женщин и детей. В Штернбергском округе голод. Утверждают, что были случаи поедания трупов."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Вы черный вестник, Трейч."

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "В Польше начались еврейские погромы."

    hide trejch

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Что? Опять?"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Какое варварство! Какие глупые люди!"

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ну, может быть, еще только слухи. Много говорят..."

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ну, а наши? А наши?"

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч"

    trejch "<{i}(пожимает плечами).{/i}>"

    trejch "Завтра я иду туда."

    hide trejch

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Ну, и вас повесят. Больше ничего. Нужно выждать."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "И я с вами! К черту!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Куда же ты с такими ногами пойдешь? Одумайся, Валентин, ты не ребенок."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А!.."

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "А как ваши ноги, Валентин?"

    hide trejch

    show verhovtsev at truecenter

    "<{i}Верховцев машет рукой.{/i}>"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Плохо."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "А про Колюшку - ничего?"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "В назначенный час на месте никого не было, и я понял, что дело отложено. Я сам теряюсь в догадках. Завтра я иду туда."

    hide trejch

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Бог вам в помощь, голубчик. Благословляю вас, как сына."

    hide inna_aleksandrovna

    play sound1 kiss

    show trejch at left
    show inna_aleksandrovna at right

    "<{i}Трейч целует у нее руку.{/i}>"

    hide trejch
    hide inna_aleksandrovna

    stop sound1

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    hide pollak

    show pollak at left
    show zhitov at right

    pollak "<{i}(Житову).{/i}>"

    hide zhitov

    show pollak at truecenter

    pollak "Скажите пожалуйста-рабочий, а как воспитан. Я удивлен."

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "М-да."

    hide zhitov

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "И мне очень нравится, что он рассказывает так ясно и коротко."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(кричит).{/i}>"

    lunts "Вы слышали?"

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Что с вами? Как вы кричите! Испугали..."

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Опять! Опять убивают отцов и матерей, опять рвут детей на части. О, я почувствовал это, я понял это сегодня, когда взглянул на эти проклятые звезды!"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Дорогой Лунц, успокойтесь."

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Зачем вы сказали это, Трейч!"

    hide inna_aleksandrovna

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Это ничего."

    hide trejch

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Нет, я не успокоюсь, я не хочу успокаиваться! Я довольно был спокоен. Я был спокоен, когда убили мать, и отца, и сестру. Я был спокоен, когда там, на баррикадах, убивали моих братьев. О, я долго был спокоен! Я и теперь спокоен."

    lunts "Разве я не спокоен? Трейч!.. Значит, все... напрасно?"

    hide lunts

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Нет. Мы победим."

    hide trejch

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Трейч, я любил науку. Поллак, я любил науку. Когда еще был маленький, такой маленький, что меня били все мальчики на улице, я уже тогда любил науку."

    lunts "Меня били, а я думал: вот я вырасту и стану знаменитым ученым, и буду честью своей семьи - моего дорогого отца, который отдавал мне последние гроши, моей дорогой мамы, которая плакала надо мной... О, как я любил науку!"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Мне очень жаль вас, Лунц. Я уважаю вас."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Когда я не ел, когда я не пил, когда я, как собака, бродил по улицам, ища корки хлеба, - я думал о науке. И тогда, когда убили моего отца, и мать, и сестру, я плакал, рвал волосы и думал о науке. Вот как я любил науку! А теперь..."

    lunts "<{i}(Тихо.){/i}>"

    lunts "Я ненавижу науку."

    lunts "<{i}(Кричит.){/i}>"

    lunts "Не надо науки! Долой науку!"

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Лунц, Лунц, как мне жаль..."

    hide pollak

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Лунц, возьмите себя в руки. Нельзя же так, ведь это истерия."

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Ага, истерия! Пусть истерия, и я спокоен, и вы напрасно думаете, что я не спокоен. Я не хочу науки. Я уйду отсюда. Я уйду отсюда. Вы слышите?"

    hide lunts

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Пойдемте со мной."

    hide trejch

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Да, я пойду с вами. Я не хочу науки. Проклятые звезды. Опять, опять! Ведь я слышу, как они там кричат! Вы не слышите, а я слышу! И я вижу - всех, всех, кого жгли, убивали, рвали на части."

    lunts "Били за то, что среди нас родился Христос, что среди нас были пророки и Маркс. Я вижу их."

    lunts "Они смотрят на меня в окно, холодные, истерзанные трупы, они стоят над моей головой, когда я сплю, они спрашивают меня: и ты будешь заниматься наукой, Лунц? Нет! Нет!"

    hide lunts

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Голубчик ты мой, помоги тебе бог."

    hide inna_aleksandrovna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Да, бог. Я еврей, и я зову еврейского бога! Боже отмщений, господи боже отмщений! Яви себя! Восстань! Судия земли, воздай возмездие гордым! Боже отмщений! Господи боже отмщений! Яви себя!"

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Месть палачам!"

    hide verhovtsev

    play sound1 footsteps

    show lunts at truecenter

    "<{i}Лунц молча грозит кулаком и выходит.{/i}>"

    hide lunts

    stop sound1

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Каков?"

    hide trejch

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Какой несчастный юноша! Это так тяжело, если человек любит науку и ему нельзя ей служить. Мне было так весело, а когда он говорил, я заплакал, уважаемая Инна Александровна."

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "И не говорите. Сердце у меня разрывается. Когда этому конец будет, господи! Проживешь, а светлых дней так и не увидишь. Жизнь!"

    hide inna_aleksandrovna

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да, тяжело."

    hide zhitov

    show verhovtsev at left
    show inna_aleksandrovna at truecenter
    show zhitov at right

    "<{i}Трейч отводит Верховцева в сторону и, предостерегающе показав на Инну Александровну, шепчет ему что-то. При первых словах Верховцев отдергивает голову и громко говорит.{/i}>"

    hide trejch
    hide verhovtsev
    hide inna_aleksandrovna
    hide zhitov

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Не может быть! Нико..."

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Тсс!"

    hide trejch

    "<{i}Шепчутся.{/i}>"

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Нужно уповать на бога, уважаемая Инна Александровна, но не бога отмщения, о котором говорил этот несчастный юноша, а бога милосердия и любви."

    hide pollak

    show zhitov at truecenter

    $ zhitov_var = "{noalt}Житов."

    zhitov "Да, боги бывают разные, какой кому нужен."

    hide zhitov

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ах, дети, дети! Горе с вами великое!"

    hide inna_aleksandrovna

    play sound1 footsteps

    show sergej_nikolaevich at truecenter

    "<{i}Входит Сергей Николаевич., здоровается.{/i}>"

    hide sergej_nikolaevich

    stop sound1

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "И вы здесь, Поллак?"

    hide sergej_nikolaevich

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Сегодня день моего рождения, уважаемый Сергей Николаевич."

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Поздравляю вас."

    sergej_nikolaevich "<{i}(Жмет руку.){/i}>"

    hide sergej_nikolaevich

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "И сегодня я имел честь объявить собравшимся господам о моей помолвке с девицей Фанни Эрстрем."

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Так вот вы какой счастливец!"

    hide sergej_nikolaevich

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Да. Теперь у меня будет спутник, уважаемый Сергей Николаевич."

    play sound1 male_laughter

    pollak "<{i}(Хохочет.){/i}>"

    stop sound1

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Еще раз поздравляю. А скажите, относительно Николая нет ничего нового?"

    hide sergej_nikolaevich

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "По-видимому, бегство отложено."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "А что на земле делается, почтенный звездочет, если б вы слыхали!"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "А что? Опять какие-нибудь несчастья?"

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да - суетные заботы."

    verhovtsev "<{i}(Склонив голову набок.){/i}>"

    verhovtsev "Вот смотрю я так на вас и думаю: есть у вас хоть какие-нибудь друзья или вы так - один и один?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    hide sergej_nikolaevich

    show sergej_nikolaevich at left
    show inna_aleksandrovna at right

    sergej_nikolaevich "<{i}(показывает на Инну Александровну).{/i}>"

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    sergej_nikolaevich "Вот мой друг."

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Не конфузь меня, Сергей Николаевич. Разве тебе такой друг нужен?"

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Ну, положим. А еще?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Есть и еще. Но, представьте, я их никогда не видал. Один живет в Южной Африке, у него обсерватория, другой - в Бразилии, а третий - не знаю где."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Пропал?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он умер лет полтораста назад. А еще один есть, того я совсем не знаю, хотя очень люблю, - так этот еще не родился. Он должен родиться приблизительно через семьсот пятьдесят лет, и я уже поручил ему проверить кое-какие мои наблюдения."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "И уверены, что он сделает?"

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да."

    hide sergej_nikolaevich

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Странная коллекция. Вам бы ее в какой-нибудь музей пожертвовать! Не правда ли, Трейч?"

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Мне нравятся друзья господина Терновского."

    hide trejch

    play sound1 footsteps

    show petja at truecenter

    "<{i}Быстро входит Петя. и оглядывается.{/i}>"

    hide petja

    stop sound1

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А Лунц где? Все тут? Хорошо. А Лунц?"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Он у себя, Петя, пойди к нему, поговори, он так взволнован сегодня."

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Пожалуйста, господа, посидите здесь. Я хочу устроить маленькое празднество, сегодня такой день."

    hide petja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Уж не фейерверк ли? О, хитрый Петя. Но это уж слишком, хотя, конечно, день такой..."

    hide pollak

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Я сейчас."

    play sound1 footsteps

    petja "<{i}(Уходит.){/i}>"

    stop sound1

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(прохаживается медленно).{/i}>"

    sergej_nikolaevich "Вы не знаете, Поллак, каков барометр сегодня?"

    hide sergej_nikolaevich

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Довольно низко, уважаемый Сергей Николаевич."

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Это чувствуется."

    hide sergej_nikolaevich

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "В связи с колебанием стрелки надо думать, что в южных широтах - циклон."

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да. Беспокойно."

    hide sergej_nikolaevich

    show anna at truecenter

    $ anna_var = "{noalt}Анна"

    hide anna

    show anna at left
    show inna_aleksandrovna at right

    anna "<{i}(Инне Александровне).{/i}>"

    hide inna_aleksandrovna

    show anna at truecenter

    anna "Наверное, Петя задумал какую-нибудь гадость. Напрасно вы поощряете его, мама."

    hide anna

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Что же я с ним поделаю? Ты сама видишь, что с ним..."

    hide inna_aleksandrovna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    play sound1 footsteps

    verhovtsev "<{i}(идет с Трейчем к столу).{/i}>"

    stop sound1

    verhovtsev "Какая тут у вас дьявольская тишина: точно в могиле."

    hide verhovtsev

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Разве? А мне здесь внизу кажется несколько шумно."

    hide sergej_nikolaevich

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч"

    hide trejch

    show trejch at left
    show verhovtsev at right

    trejch "<{i}(Верховцеву).{/i}>"

    hide verhovtsev

    show trejch at truecenter

    trejch "Да, вот еще: если я не вернусь, вы скажете ей, что..."

    hide trejch

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Понимаю! Фу, духота какая!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "А по мне, скорее холодно."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Духота, холодно - все один черт. Если я тут поживу еще неделю..."

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "А не устроить ли нам, господа, более или менее правильную беседу, в которой все могли бы принимать участие? Председателем мы изберем..."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    play sound1 footsteps

    lunts "<{i}(входит).{/i}>"

    stop sound1

    lunts "Меня звали? Вы звали меня, Сергей Николаевич?"

    hide lunts

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Нет."

    hide sergej_nikolaevich

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Что же Петя сказал мне?"

    play sound1 footsteps

    lunts "<{i}(Хочет уйти.){/i}>"

    stop sound1

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Посидите с нами, дорогой Лунц. Теперь, когда вы несколько успокоились, я хочу сказать вам, что я не согласен с вами относительно науки."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Ах, оставьте! Сергей Николаевич, я должен вам сказать: я оставляю обсерваторию."

    hide lunts

    show petja at truecenter

    "<{i}Голос Пети за дверью: \"Пажи! Шире дорогу герцогине!\"{/i}>"

    hide petja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    play sound1 male_laughter

    pollak "<{i}(смеется).{/i}>"

    stop sound1

    pollak "Ах, это Петя! Какой забавный мальчик! Слушайте, слушайте!"

    hide pollak

    play sound1 footsteps

    show petja at left
    show starucha at right

    "<{i}Распахиваются двери. Входят Петя. и Старуха. Она перегнулась пополам, под прямым почти углом, и еле идет - ужасный образ нищеты, старости и горя. Петя, взяв ее за руку, выступает торжественно, как в опере.{/i}>"

    hide petja
    hide starucha

    stop sound1

    show frants at left
    show petja at right

    "<{i}У дверей улыбающиеся физиономии Минны, Франца и еще кого-то из прислуги.{/i}>"

    hide frants
    hide petja

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Позвольте представить, господа, вот моя невеста - прелестная Эллен."

    hide petja

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    play sound1 male_laughter

    verhovtsev "<{i}(грубо смеется).{/i}>"

    stop sound1

    verhovtsev "Вот дурак!"

    hide verhovtsev

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Я говорила!"

    hide anna

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    pollak "<{i}(встает).{/i}>"

    pollak "Это насмешка! Я не позволю насмехаться над моей невестой!"

    hide pollak

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(громко).{/i}>"

    petja "Прелестная Эллен, поклонитесь собранию!"

    hide petja

    show starucha at truecenter

    "<{i}Старуха кланяется.{/i}>"

    hide starucha

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Я протестую! Это оскорбление!"

    hide pollak

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Он шутит, Петечка, нехорошо, не нужно шутить над старым человеком."

    hide inna_aleksandrovna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Нет, это не шутка! Я понимаю. О, я понимаю!"

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Так. Теперь поговорим, прелестная Эллен. Вам сколько лет?"

    hide petja

    show petja at left
    show starucha at right

    petja "<{i}Старуха молчит и трясет головой.{/i}>"

    hide starucha

    show petja at truecenter

    petja "Вы сказали, семнадцать? Вам семнадцать лет, очаровательная девица. Герцог, ваш отец, и герцогиня, ваша мать, согласны на наш брак?"

    hide petja

    show starucha at truecenter

    "<{i}Старуха молчит и трясет головой.{/i}>"

    hide starucha

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Глубокоуважаемый Сергей Николаевич! Меня оскорбляют в вашем доме..."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(бешено).{/i}>"

    lunts "Да что вы лезете? Кому вы нужны с вашей идиотской невестой."

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Господин Лунц, вы ответите!"

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Звезды, проклятые звезды!"

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Как я счастлив, прелестная Эллен! Вы слышите запах роз? Вы слышите, как заливается в саду соловей? Это о нашей любви поет он, прелестная Эллен."

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Проклятые звезды!"

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Ваш благоухающий ротик, прелестная Эллен..."

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Да, да..."

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "...ваши жемчужные зубки..."

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Да, да!"

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "...ваши нежные щечки-я влюблен в вас безумно, прелестная Эллен! Зачем так скромно потупили вы очаровательные глазки ваши?"

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Позор! И вам не стыдно, Поллак? Наука! А это вы видите? Это моя мать, это моя мать..."

    hide lunts

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Я не понимаю..."

    hide pollak

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Выпрямьте ваш стройный стан и гордо объявите себя моей женой, очаровательная Эллен! В ваших объятиях найдет вечный покой мое беспокойное сердце!"

    hide petja

    show starucha at truecenter

    "<{i}Старуха трясет головой.{/i}>"

    hide starucha

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Их всех надо в сумасшедший дом."

    hide anna

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    verhovtsev "<{i}(с испугом).{/i}>"

    verhovtsev "Анна, молчи!"

    hide verhovtsev

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Это такое..."

    hide pollak

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Молчи, буржуй, а не то... Это моя мать."

    hide lunts

    show lunts at left
    show starucha at right

    lunts "<{i}(К Старухе.){/i}>"

    hide starucha

    show lunts at truecenter

    lunts "Старая женщина!"

    hide lunts

    show lunts at left
    show petja at right

    lunts "<{i}(Отталкивает Петю.){/i}>"

    hide petja

    show lunts at truecenter

    lunts "Послушайте меня, старая женщина. Вот стою я перед вами на коленях, маленький еврей. Вы - моя мать, и дайте же, дайте, я поцелую вашу руку..."

    hide lunts

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(кричит).{/i}>"

    petja "Это моя невеста!"

    hide petja

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Это моя мать, оставьте ее..."

    hide lunts

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Дайте воды!"

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Старая женщина! Простите меня: я любил науку, глупый еврей... жид!.."

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев"

    hide verhovtsev

    show verhovtsev at left
    show trejch at right

    verhovtsev "<{i}(Трейчу).{/i}>"

    hide trejch

    show verhovtsev at truecenter

    verhovtsev "Нужно что-нибудь сделать!"

    hide verhovtsev

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Ничего."

    hide trejch

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Я люблю только вас, милая, старая женщина. Возьмите мою голову и сердце мое возьмите. Проклятые звезды! Проклятые звезды!"

    hide lunts

    show trejch at truecenter

    $ trejch_var = "{noalt}Трейч."

    trejch "Вы идите со мной, Лунц."

    hide trejch

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(кричит).{/i}>"

    petja "Это моя невеста!"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Господи! Петюшка! С ним дурно!"

    hide inna_aleksandrovna

    show anna at truecenter

    $ anna_var = "{noalt}Анна."

    anna "Воды!"

    hide anna

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц."

    lunts "Я иду с вами. И клянусь богом..."

    hide lunts

    show verhovtsev at truecenter

    $ verhovtsev_var = "{noalt}Верховцев."

    verhovtsev "Да замолчите вы!"

    hide verhovtsev

    show verhovtsev at left
    show sergej_nikolaevich at truecenter
    show lunts at right

    "<{i}Петя бьется в припадке. Все, кроме Трейча, бросаются к нему; Сергей Николаевич делает шаг, но останавливается и глядит на Лунца.{/i}>"

    hide petja
    hide trejch
    hide verhovtsev
    hide sergej_nikolaevich
    hide lunts

    show lunts at truecenter

    $ lunts_var = "{noalt}Лунц"

    lunts "<{i}(стоя на коленях).{/i}>"

    lunts "Старая женщина! Вы видите, я плачу, старая женщина, я - маленький еврей, который любил науку. Вы - моя мать, вы - мать моя, и, клянусь перед богом, всю жизнь мою я отдам вам, моя милая, моя старая женщина. Я плачу... Проклятые звезды!"

    hide lunts

    "<{i}Занавес{/i}>"

label Act_4:
    play music "audio/music/2.mp3" fadeout 1.0 fadein 1.0

    scene 6 with fade


label Act_4_Scene_1:
    "{b}ДЕЙСТВИЕ ЧЕТВЕРТОЕ{/b}"

    play sound1 footsteps

    "<{i}В правом углу сцены купол обсерватории в разрезе, одной третью своей уходящей за кулисы. Вокруг купола галерейка с чугунной прозрачной решеткой.{/i}>"

    stop sound1

    "<{i}Низ сцены - часть какой-то крыши, примыкающей к главному зданию обсерватории, и еле намеченные контуры гор. Все же остальное - одно огромное пространство ночного неба. Созвездия.{/i}>"

    play sound1 footsteps

    "<{i}Внутри купола очень темно; налево смутно уходят очертания огромного рефрактора; два стола, на них лампы с темными, непрозрачными колпаками. Створы купола раскрыты, и в них проглядывает звездное небо. Лестница вниз также в разрезе.{/i}>"

    stop sound1

    show sergej_nikolaevich at left
    show petja at truecenter
    show pollak at right

    "<{i}Тишина, тихий стук метронома. Сергей Николаевич., Петя. и Поллак.{/i}>"

    hide sergej_nikolaevich
    hide petja
    hide pollak

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Итак, уважаемый Сергей Николаевич, вы будете любезны наблюдать за камерой. Я ухожу, необходимо окончить таблицы."

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Работайте, работайте! До свиданья!"

    hide sergej_nikolaevich

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак"

    hide pollak

    show pollak at left
    show petja at right

    pollak "<{i}(обращаясь к Пете).{/i}>"

    hide petja

    show pollak at truecenter

    pollak "Ну, как мы себя чувствуем сегодня, юный жрец богини Урании?"

    hide pollak

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Хорошо. Благодарю вас."

    hide petja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "И мы уже больше не будем насмехаться над бедным Поллаком, которому так хочется жениться?"

    hide pollak

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Честное слово, я не хотел..."

    hide petja

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Я знаю, знаю..."

    hide pollak

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он уже тогда был нездоров."

    hide sergej_nikolaevich

    show pollak at truecenter

    $ pollak_var = "{noalt}Поллак."

    pollak "Я шучу, уважаемый Сергей Николаевич. Вообще я должен с удивлением отметить, что открыл в себе огромные запасы юмора. Когда сегодня Франц разлил молоко, я сказал ему: Франц, вы оставляете за собой млечный путь, - и он очень смеялся."

    play sound1 male_laughter

    pollak "<{i}(Хохочет.){/i}>"

    stop sound1

    pollak "Но я не буду входить в подробности. До свидания."

    play sound1 footsteps

    pollak "<{i}(Уходит.){/i}>"

    stop sound1

    hide pollak

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Какой смешной этот Поллак! Папа, я тебе не помешаю, если останусь здесь?"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Нет, дружок."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Мне не хочется вниз. Теперь там так скучно. Ты знаешь, Житов вчера прислал телеграмму из Каира: \"Сижу и смотрю на пирамиды\". А ты видал пирамиды?"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Видал. Я боюсь, дружок, что маме одной будет тяжело."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Сейчас она уже спит. А днем я с ней много бываю. Она все толкует, папа, о Коле."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да ведь ничего не известно. От Анны нет известий?"

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Нет. Она не любит писать письма. Конечно, ничего еще не известно, я все время твержу это маме, но ты знаешь, как трудно говорить с женщинами... Ну, я не буду мешать тебе. Ты тоже будешь вычислять?"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да. Немного. Я что-то устал."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А я почитаю... Да, папа, вчера я в журнале прочел, что ты совершил какое-то громадное открытие относительно туманностей и что это ставит тебя наряду..."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Это открытие, дружок, я совершил уже десять лет тому назад. Астрономическая слава приходит поздно - нами интересуются мало."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "И я не знал!"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Мы по-прежнему остаемся обособленными, как египетские жрецы, хотя и против воли."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Как это глупо! Папочка, а почему ты, когда я был болен, велел положить меня сюда? Ведь я, наверное, мешал тебе."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Нет. Но когда что-нибудь становится мне очень мило, мне хочется поднять его сюда. У меня, Петя, смешное убеждение, что здесь не может быть страданий, болезни. Тут - звезды."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Раз ночью я проснулся и увидел тебя: ты смотрел на звезды. Было тихо, и ты смотрел на звезды. И вот тогда я что-то понял... Нет, почувствовал. Не знаю - что, я не умею объяснить. Как будто в мире мы одни: ты, звезды и я... или как будто мы уже умерли."

    petja "И от этого не было страшно, а спокойно, как-то хорошо - чисто. Мне теперь так хочется жить - отчего это? Ведь я по-прежнему не понимаю, зачем жизнь, зачем старость и смерть? - а мне все равно."

    petja "Ну, работай, работай, я не буду входить в подробности, как говорит Поллак."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(задумчиво).{/i}>"

    sergej_nikolaevich "Да. Человек думает только о своей жизни и о своей смерти - и от этого ему так страшно жить и так скучно, как блохе, заблудившейся в склепе..."

    sergej_nikolaevich "Чтобы заполнить страшную пустоту, он много выдумывает, красиво и сильно, но и в вымыслах - он говорит только о своей смерти, только о своей жизни, и страх его растет."

    sergej_nikolaevich "И становится он похож на содержателя музея из восковых фигур, - да, на содержателя музея из восковых фигур. Днем он болтает с посетителями и берет с них деньги, а ночью - одинокий - он бродит с ужасом среди смертей, неживого, бездушного."

    sergej_nikolaevich "Если бы он знал, что всюду жизнь!"

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Ты знаешь, папа, чего я первый раз испугался? Я увидел стул в пустой комнате, самый простой стул - и вдруг мне стало так страшно, что я закричал."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Его мысль рождена птицей-могучей и свободной царицей пространств, а он связал ей крылья и посадил ее в птичник - с проволочными, бесстыдно лгущими стенами."

    sergej_nikolaevich "И небо сквозь сетку дразнит ее, и она ссорится с другими птицами, тупеет, становится глупой - вместо того чтоб летать."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Бедная царица!"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да, все живет. И когда поймет это человек, ему станет радостно жить, как греку, как язычнику. Явятся снова дриады и нимфы, и эльфы запляшут в лунном свете. Человек будет ходить по лесу и разговаривать с деревьями и цветами."

    sergej_nikolaevich "Он никогда не будет один, ибо все живет: и металл, и камень, и дерево."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    play sound1 male_laughter

    petja "<{i}(смеется).{/i}>"

    stop sound1

    petja "Ты очень смешной, папа."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да? Разве?"

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Ты вежлив со стульями. Нет, это правда, и ты вежлив с предметами. Когда ты берешь что-нибудь в руки, ты делаешь это как-то вежливо. Я не умею объяснить. Ты очень рассеянный, а ходишь так ловко, что никогда ничего не зацепишь, не толкнешь, не уронишь."

    petja "Когда стулья, шкалы, стаканы собираются ночью, как у Андерсена, и начинают разговаривать, они, вероятно, очень хвалят тебя."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да? Это мне нравится, что стулья разговаривают."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А что тут делается, когда ты уходишь? Вероятно, все поет?"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Оно и при мне поет."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Труба басом, да?"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "А ты слышишь, мой мальчик, что поют звезды?"

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Нет."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Они поют, и песнь их таинственна, как вечность. Кто хоть раз услышит их голос, идущий из глубины бесконечных пространств, тот становится сыном вечности! Сын вечности! - да, Петя, так когда-нибудь назовется человек."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    play sound1 male_laughter

    petja "<{i}(смеется).{/i}>"

    stop sound1

    petja "Папочка, не сердись: неужели и Поллак- сын вечности?"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Может быть."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Но он такой нелепый, такой узкий... Ну, ну, я не буду. Сажусь. Какой у тебя здесь воздух - в комнатах такого никогда не бывает. Ты все думаешь?"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да."

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Ну, думай. Кончено, читаю."

    petja "<{i}Молчание.{/i}>"

    petja "Сегодня ровно три недели, как уехал Лунц."

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Да?"

    hide sergej_nikolaevich

    play sound1 footsteps

    show petja at left
    show sergej_nikolaevich at right

    "<{i}Молчание. Петя. читает. Сергей Николаевич. выходит из задумчивости и медленно придвигает к себе работу. Работает.{/i}>"

    hide petja
    hide sergej_nikolaevich

    stop sound1

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Первые ночи, когда у меня был жар, я очень боялся рефрактора. Он двигался по кругу за звездой, и когда я снова открывал глаза, он уже успевал немного передвинуться. И мне казалось - не знаю - как будто это один огромный черный глаз..."

    petja "в сюртуке и с фал-дочками."

    hide petja

    show sergej_nikolaevich at truecenter

    "<{i}Молчание. Сергей Николаевич откладывает работу и думает, опершись подбородком на руку.{/i}>"

    hide sergej_nikolaevich

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Петя, ты знаешь, какие стихи написал астроном Тихо Браге по поводу одного инструмента."

    sergej_nikolaevich "Это был параллактический инструмент, которым пользовался Коперник во всех своих работах и который сделал он сам из трех деревянных жердочек, ужасно плохой инструмент: у арабов были лучше. Так вот послушай:"

    sergej_nikolaevich "Тот, солнцу кто сказал: \"Сойди с небес и стой\","

    sergej_nikolaevich "Кто землю на небо, луну на землю вскинул,"

    sergej_nikolaevich "И, весь перевернув порядок мировой,"

    sergej_nikolaevich "Скреп мира не расторг нигде и не раздвинул,"

    sergej_nikolaevich "А проще не в пример представил и стройней"

    sergej_nikolaevich "Нам твердь, знакомую по опыту очей, -"

    sergej_nikolaevich "Тот муж, Коперник сам, кого я разумею,"

    sergej_nikolaevich "Вот эти палочки в простой сложив прибор"

    sergej_nikolaevich "И им осуществив столь дерзкую затею,"

    sergej_nikolaevich "Законы наложил на весь небес простор,"

    sergej_nikolaevich "Светила горния во славе их теченья"

    sergej_nikolaevich "Кусочкам дерева ничтожным подчинил,"

    sergej_nikolaevich "К самим проник богам, куда со дня творенья"

    sergej_nikolaevich "Рок смертным всем почти дорогу возбранил."

    sergej_nikolaevich "Каких преодолеть преград не может разум!"

    sergej_nikolaevich "Нагроможденные когда-то Пелион"

    sergej_nikolaevich "И Осса с Этною, Олимп с другими разом"

    sergej_nikolaevich "Горами многими вотще со всех сторон -"

    sergej_nikolaevich "Свидетели тому, что силой тела дикой"

    sergej_nikolaevich "Гиганты мощные, но слабые умом,"

    sergej_nikolaevich "Не досягнули звезд. Он, он один, великий,"

    sergej_nikolaevich "Искавший помощи лишь в разуме своем,"

    sergej_nikolaevich "Не мышцы крепкие, а тоненькие жерди"

    sergej_nikolaevich "Орудием избрав, - возвысился до тверди."

    sergej_nikolaevich "Каких могучих здесь произведенье дум!"

    sergej_nikolaevich "Хотя по существу в нем стоимости мало,"

    sergej_nikolaevich "Но золото само, когда б имело ум,"

    sergej_nikolaevich "Такому дереву завидовать бы стало!.."

    hide sergej_nikolaevich

    "<{i}Молчание. Внизу музыка - несколько нерешительных и грустных аккордов: \"Сижу за решеткой... в темнице сырой...\"{/i}>"

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(вскакивает).{/i}>"

    petja "Что это, музыка? Кто же это-там только мама!"

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(обернувшись).{/i}>"

    sergej_nikolaevich "Да. Не Маруся ли?"

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя"

    petja "<{i}(кричит).{/i}>"

    petja "Маруська приехала! Я сейчас, сейчас!.."

    play sound1 running

    petja "<{i}(Бежит вниз.){/i}>"

    stop sound1

    hide petja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(повторяет).{/i}>"

    sergej_nikolaevich "\"...Но золото само, когда б имело ум, такому дереву завидовать бы стало!..\""

    hide sergej_nikolaevich

    show marusja at left
    show petja at right

    "<{i}Длительное молчание. На лестнице показываются Маруся и Петя.{/i}>"

    hide marusja
    hide petja

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Не плачь. Что плакать? Пойди к маме."

    play sound1 male_cry

    hide marusja

    show marusja at left
    show petja at right

    marusja "<{i}Петя. плачет, сдерживая рыдания.{/i}>"

    hide petja

    show marusja at truecenter

    stop sound1

    marusja "Пойди, пойди, она одна. Поддержи ее - ты мужчина."

    hide marusja

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "А ты?"

    hide petja

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Я ничего. Ступай."

    play sound1 kiss

    hide marusja

    show marusja at left
    show petja at right

    marusja "<{i}(Целует его в голову; расходятся.){/i}>"

    hide petja

    show marusja at truecenter

    stop sound1

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Маруся, милая! Как я рад, что вы приехали. Вы не верите в то, что я могу чувствовать что-нибудь, а я сегодня весь день чувствовал ваш приезд."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Здравствуйте, Сергей Николаевич. Вы работаете?"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "А что Николай? Он бежал?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да. Он ушел из тюрьмы."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он здесь?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Нет."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Но он в безопасности, Маруся?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Бедная Маруся! Как вы устали, вероятно. Сегодня весь день я думаю о вас и о нем, - о вас и о нем."

    sergej_nikolaevich "О вас я говорить не смею, но вы - как музыка, Маруся! Я так рад! Позвольте мне поцеловать вашу руку - вашу нежную ручку, которая так много поработала над железными замками и решетками."

    play sound1 kiss

    sergej_nikolaevich "<{i}(Церемонно целует руку.){/i}>"

    stop sound1

    sergej_nikolaevich "Садитесь, рассказывайте."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(показывая на галерею).{/i}>"

    marusja "Пойдем туда."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Я так рад. Я возьму для вас стул - вы так устали, Маруся."

    play sound1 footsteps

    sergej_nikolaevich "<{i}Выходят.{/i}>"

    stop sound1

    sergej_nikolaevich "Ну, садитесь. Здесь, правда, хорошо?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да. Очень хорошо."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "А я сидел здесь с Петей. Он такой милый мальчик! Он в последнее время напоминает мне Николая..."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Но в Пете много женственного, слабого, иногда я беспокоюсь за него. А Николай - он такой энергичный, такой смелый."

    sergej_nikolaevich "Как в нем все гармонично и стройно, как нежно и сильно! Это прекрасный образец человека мужественного, редкая, красивая форма, которую природа разбивает, чтобы не было повторений."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да. Разбивает. Я хотела сказать..."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он пленителен, как юный бог, в нем какие-то чары, против которых нельзя устоять. Ведь его, Маруся, так любят все, даже Анна, - даже Анна. И он так красив! Вам, Маруся, покажется это нелепо: он напоминает мне звездное небо перед зарею."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да. Звездное небо перед зарею."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он не мог не бежать, я был уверен в этом. Тюрьма! Что такое тюрьма - эти ржавые замки и трухлявые глупые решетки. Я удивляюсь, как они могли так долго держать его: они должны были улыбнуться и дать ему дорогу, как молодому счастливому принцу!"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    play sound1 punch

    marusja "<{i}(падая на колени, с тоской).{/i}>"

    stop sound1

    marusja "Отец, отец, какой это ужас!"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Что, что с вами, Маруся?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Разбита прекрасная форма! Отец, разбита, разбита прекрасная форма!"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он умер! Да говори же!"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Он... Его покинул разум."

    marusja "<{i}Молчание.{/i}>"

    marusja "<{i}(Вскакивает.){/i}>"

    marusja "Что же это! Проклятая жизнь! Где же бог этой жизни, куда он смотрит? Проклятая жизнь! Изойти слезами, умереть, уйти! Зачем жить, когда лучшие погибают, когда - разбита прекрасная форма! Ты понимаешь это, отец? Нет оправдания жизни - нет ей оправдания."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Расскажи мне все."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Зачем? Разве можно это рассказать? Чтобы рассказать, нужно понять, - а разве это можно понять?"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Расскажи."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Он был моим знаменем. Когда варвары бросили его в тюрьму, я думала: но ведь это варвары, а он - солнце. Я думала: вот сейчас поднимутся все, кто любит его, и разрушат тюрьму, - и снова засияет мое солнце. Мое солнце!"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Как это случилось?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Как гаснет звезда? Как умирает птица в неволе? Перестал петь, стал бледен и грустен, - но успокаивал меня. Раз только сказал: я не могу понять железной решетки. Что такое железная решетка, - она между мною и небом."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Между мною и небом."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "А тут их избили. Да, да. Они подняли бунт в тюрьме. В их камеры ворвались тюремщики и били их - по одному. Били руками, ногами, их топтали, уродовали лица. Долго, ужасно их били - тупые, холодные звери."

    marusja "Не пощадили они и твоего сына: когда я увидела его, его лицо было ужасно."

    marusja "Милое, прекрасное лицо, которое улыбалось всему миру! Разорвали ему рот, уста, которые никогда не произносили слова лжи; чуть не вырвали глаза - глаза, который видел только прекрасное. Ты понимаешь это, отец? Ты можешь это оправдать?"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Говори."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "И уже тут в нем проснулась эта страшная смертельная тоска. Он никого не упрекал, он защищал предо мною тюремщиков - своих убийц, - но в его глазах росла эта черная тоска: душа его умирала. И все еще успокаивал меня, все еще утешал."

    marusja "И раз только сказал: всю тоску мира ношу я в душе."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Дальше."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Стал забываться. Потом умолк. Молча выходил ко мне - молчал, пока я говорила, и молча уходил."

    marusja "Глаза у него стали огромные, черные, как будто из них смотрела тоска всего мира, - и такой красоты я не видала, отец! А когда сегодня я пришла на свидание, он был уже в больнице."

    marusja "Когда вчера вели его на прогулку, он хотел броситься с лестницы, в пролет, но его удержали. Потом - безумие, горячечная рубашка - и все."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Ты видела его?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Я видела его. Но об этом я не стану говорить. Я не могу. Разбита прекрасная форма!"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Они всегда избивали своих пророков!"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Отец! Как же можно жить среди тех, кто избивает своих пророков? Куда мне уйти, я не могу больше. Я не могу смотреть на лицо человека - мне страшно! Лицо человека - это так ужасно: лицо человека."

    marusja "Я выплакала мои слезы - та же тоска впереди - смертельная, последняя тоска. Ты видишь: я спокойна. Как много звезд! Пауза."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "А Инна знает?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Что говорят врачи?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Они говорят: идиот."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Николай - идиот?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да. Он будет долго жить. Он станет равнодушен, он будет много пить, есть, потолстеет, он проживет долго. Он будет счастлив."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Николай - идиот! Как трудно это представить. Этот прекрасный человек, этот гармоничный, светлый дух погружен во тьму, в скучный, бедный, еле колышущийся хаос. Он некрасив теперь, Маруся?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(с горечью).{/i}>"

    marusja "Да, он некрасив. А тебя это беспокоит?"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Я рад, что ты так спокойна, я не думал, что ты так сильна."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Уж месяц я переживаю изо дня в день эту муку. Я привыкла. Что, отец, привычка: это, должно быть, тоже что-то вроде сумасшествия?"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Что же ты хочешь делать теперь?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Не знаю, я еще не думала об этом. Как-то стыдно, отец, над свежей могилой думать о своей - новой жизни. Даже собаке нужно время, чтобы привыкнуть к потере щенка."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Николая я устрою, ему теперь не много надо. А ты, Маруся, больше не ходи к нему. Совсем не ходи."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Нет, я буду ходить!"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Это кощунство. Это такое же кощунство, как оставить в своей комнате труп. Трупы надо сжигать на огне."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Я и труп оставила бы у себя в комнате."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Зачем?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Ты знаешь прелестную Эллен? Я беру ее с собой."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Против кого это?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Не знаю. Против тебя."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Против меня?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Да. Я нашла, я знаю теперь, что я буду делать. Я построю город и поселю в нем всех старых, как прелестная Эллен, всех убогих, калек, сумасшедших, слепых. Там будут глухонемые от рождения и идиоты, там будут изъеденные язвами, разбитые параличом."

    marusja "Там будут убийцы..."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Мне жаль тебя, Маруся."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Там будут предатели и лжецы и существа, подобные людям, но более ужасные, чем звери. И дома будут такие же, как жители: кривые, горбатые, слепые, изъязвленные; дома-убийцы, предатели."

    marusja "Они будут падать на головы тех, кто в них поселится, они будут лгать и душить мягко. И у нас будут постоянные убийства, голод и плач; и царем города я поставлю Иуду и назову город: \"К звездам!\""

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Бедная Маруся, мне жаль тебя!"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Оставь! Ты не жалеешь сына."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "У меня нет детей. Для меня одинаковы все люди."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Как это бездушно! Нет, я не пойму тебя."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Это оттого, что я думаю обо всем. Я думаю о прошлом и о будущем, и о земле, и о тех звездах - обо всем."

    sergej_nikolaevich "И в тумане прошлого я вижу мириады погибших; и в тумане будущего я вижу мириады тех, кто погибнет; и я вижу космос, и я вижу везде торжествующую безбрежную жизнь - и я не могу плакать об одном!"

    hide sergej_nikolaevich

    play sound1 footsteps

    show petja at left
    show inna_aleksandrovna at right

    "<{i}На лестнице показываются Петя. и Инна Александровна. Она идет с трудом, и Петя. ее поддерживает. Медленно проходит через купол.{/i}>"

    hide petja
    hide inna_aleksandrovna

    stop sound1

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна"

    hide inna_aleksandrovna

    show inna_aleksandrovna at left
    show verhovtsev at right

    inna_aleksandrovna "<{i}(бросается к мужу).{/i}>"

    hide verhovtsev

    show inna_aleksandrovna at truecenter

    inna_aleksandrovna "Колюшка наш, Колюшка!"

    hide inna_aleksandrovna

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Мамочка, мамочка! Не плачь!"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Колюшка!"

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    hide sergej_nikolaevich

    show sergej_nikolaevich at left
    show inna_aleksandrovna at right

    sergej_nikolaevich "<{i}(усаживает ее, выпрямляется, кричит).{/i}>"

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    sergej_nikolaevich "Отняли сына! Безумцы! Слепцы, на себя поднимающие руку!"

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Ничего... отец, проживем. Колюшка мой, Колюшка..."

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Если бы солнце висело ниже, они погасили бы солнце, - чтобы издохнуть во мраке. Отняли сына! Отняли сына! Свет отняли!"

    sergej_nikolaevich "<{i}(Топает ногой.){/i}>"

    hide sergej_nikolaevich

    play sound1 footsteps
    play sound2 male_cry

    show marusja at left
    show inna_aleksandrovna at truecenter
    show sergej_nikolaevich at right

    "<{i}Петя и Маруся., плача, становятся на колени и ласкают Инна Александровну. Сергей Николаевич. отходит на несколько шагов и возвращается.{/i}>"

    hide petja
    hide marusja
    hide inna_aleksandrovna
    hide sergej_nikolaevich

    stop sound1
    stop sound2

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Прости меня, отец."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Не надо плакать, не надо. У нас есть мысль. У нас есть мысль. Да помоги же ты!.. Да, должно быть, я стар."

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Колюшка!"

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Это ничего. Жизнь, жизнь везде. Сейчас, в эту минуту - да, в эту минуту! - родится кто-то - такой же, как Николай, лучше, чем он, - у природы нет повторений."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Родится для безумия, для гибели! Родится для того, чтобы так же плакала над ним мать! Ты это хочешь сказать?"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Мать? Да. Да. Он погибнет, Маруся. Как садовник, жизнь срезает лучшие цветы, - но их благоуханием полна земля... Взгляни туда, в этот беспредельный простор, в этот неиссякаемый океан творческих сил."

    sergej_nikolaevich "Взгляни туда! Там тихо, - но если бы ты могла слышать сквозь пространство и видеть сквозь вечность, ты, может быть, умерла бы от ужаса, а быть может - сгорела бы от восторга."

    sergej_nikolaevich "С холодным бешенством, покорные железной силе тяготения, несутся в пространстве по своим путям бесконечные миры, - и над всеми ими господствует один великий, один бессмертный дух."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(вставая).{/i}>"

    marusja "Не говори мне о боге!"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Я говорю о существе, подобном нам, о том, кто так же страдает, и так же мыслит, и так же ищет, как и мы. Я его не знаю - но я люблю его, как друга, как товарища."

    sergej_nikolaevich "В тот миг, как при случайной встрече двух неведомых сил загорелась первая жизнь - маленькая, крохотная жизнь амебы, протоплазмы, - уже в этот миг все эти сверкающие громады нашли своего господина. Это мы - те, кто здесь, и те, кто там."

    sergej_nikolaevich "Великий простор небес! Древняя тайна! Ты над головою моею, ты в душе моей - и ты уже у моих ног, у ног твоего господина."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Оно молчит, отец! Оно смеется над вами!"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Но я хочу - и оно говорит! Туда, в эту синюю глубину, посылаю я мой взор, и он скользит в пространствах и настигает то, чего никогда еще не видел человек. Я зову, и оттуда, из мрака преисподней, выползает на мой зов трепещущая тайна."

    sergej_nikolaevich "Она корчится от злобы и страха, и грозит раздвоенным языком, и моргает ослепшими глазами - бессильное, жалкое чудовище. И тогда я радуюсь, и тогда я говорю в века и пространства: привет тебе, сын вечности! Привет тебе, мой неизвестный и далекий друг!"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Но смерть, но безумие, но дикое торжество рабов? Отец, я не могу уйти от земли, я не хочу уходить от нее: она так несчастна. Она дышит ужасом и тоской, - но я рождена ею, и в крови моей я ношу страдания земли."

    marusja "Мне чужды звезды, я не знаю, кто обитает там... Как подстреленная птица, душа моя вновь и вновь падает на землю."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Смерти нет."

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "А Николай? А сын твой?"

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Он в тебе, он в Пете, он во мне-он во всех, кто свято хранит благоухание его души. Разве умер Джордано Бруно?"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Он был велик."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Умирают только звери, у которых нет лица. Умирают только те, кто убивает, а те, кто убит, кто растерзан, кто сожжен, - те живут вечно. Нет смерти для человека, нет смерти для сына вечности."

    hide sergej_nikolaevich

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Колюшка! Колюшка!"

    hide inna_aleksandrovna

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "В храмах древних поддерживался вечный огонь. Испепелялось дерево, выгорало масло, но огонь поддерживался вечно."

    sergej_nikolaevich "Разве ты не чувствуешь его - тут, везде? Разве в себе не ощущаешь его чистого пламени? Кто дал тебе эту нежную душу, чья мысль, улетевшая из бренного тела, живет в тебе, - ты можешь ли сказать, что это мысль твоя? Твоя душа - лишь алтарь, на котором свершает служение сын вечности!"

    sergej_nikolaevich "<{i}(Протягивает руку к звездам.){/i}>"

    sergej_nikolaevich "Привет тебе, мой неизвестный, мой далекий друг!"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Я пойду в жизнь."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич."

    sergej_nikolaevich "Иди! Отдай ей то, что ты взяла у нее же. Отдай солнцу его тепло! Ты погибнешь, как погиб Николай, как гибнут те, кому душой своей, безмерно счастливой, поддерживать вечный суждено огонь. Но в гибели твоей ты обретешь бессмертие. К звездам!"

    hide sergej_nikolaevich

    show petja at truecenter

    $ petja_var = "{noalt}Петя."

    petja "Ты плачешь, отец. Дай поцеловать мне руку, дай!"

    hide petja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Уж ты... не плачь, отец. Как-нибудь... проживем..."

    hide inna_aleksandrovna

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся."

    marusja "Я пойду. Как святыню, сохраню я то, что осталось от Николая, - его мысль, его чуткую любовь, его нежность. Пусть снова и снова убивают его во мне - высоко над землей понесу я его чистую, непорочную душу."

    hide marusja

    show sergej_nikolaevich at truecenter

    $ sergej_nikolaevich_var = "{noalt}Сергей Николаевич"

    sergej_nikolaevich "<{i}(протягивая руки к звездам).{/i}>"

    sergej_nikolaevich "Привет тебе, мой далекий, мой неизвестный друг!"

    hide sergej_nikolaevich

    show marusja at truecenter

    $ marusja_var = "{noalt}Маруся"

    marusja "<{i}(протягивая руки к земле).{/i}>"

    marusja "Привет тебе, мой милый, мой страдающий брат!"

    hide marusja

    show inna_aleksandrovna at truecenter

    $ inna_aleksandrovna_var = "{noalt}Инна Александровна."

    inna_aleksandrovna "Колюшка... Колюшка!.."

    hide inna_aleksandrovna

    "<{i}Занавес{/i}>"


