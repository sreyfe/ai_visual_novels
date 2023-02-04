define motja = Character("motja_var", color="#FFB300", dynamic=True)
define okaemov = Character("okaemov_var", color="#803E75", dynamic=True)
define masha = Character("masha_var", color="#FF6800", dynamic=True)
define leonid = Character("leonid_var", color="#A6BDD7", dynamic=True)
define nina = Character("nina_var", color="#C10020", dynamic=True)
define viktor = Character("viktor_var", color="#CEA262", dynamic=True)
define tumanskij = Character("tumanskij_var", color="#817066", dynamic=True)
define lelja = Character("lelja_var", color="#007D34", dynamic=True)
define senja = Character("senja_var", color="#F6768E", dynamic=True)
define galja = Character("galja_var", color="#00538A", dynamic=True)
define golos = Character("golos_var", color="#FF7A5C", dynamic=True)
define vera = Character("vera_var", color="#53377A", dynamic=True)

label start:
    play music "audio/music/3.mp3" fadeout 1.0 fadein 1.0

    scene poster with fade

    "Машенька"

    "Пьеса в 3-х актах 7-ми сценах"

    menu:
        "{color=#000}Действующие лица{/color}":
            jump Characters
        "{color=#000}Акт первый.{/color}":
            jump Act_1
        "{color=#000}Акт второй.{/color}":
            jump Act_2
        "{color=#000}Акт третий.{/color}":
            jump Act_3

label Characters:
    play music "audio/music/6.mp3" fadeout 1.0 fadein 1.0

    scene 5 with fade

    "{b}Действующие лица{/b}"

    show okaemov at truecenter
    "Окаемов Василий Иванович, 70 лет."
    hide okaemov

    show masha at truecenter
    "Маша — его внучка, 15 лет."
    hide masha

    show tumanskij at truecenter
    "Туманский Павел Павлович, 43 лет."
    hide tumanskij

    show viktor at truecenter
    "Виктор — его сын, 16 лет."
    hide viktor

    show nina at truecenter
    "Нина Александровна, 30 лет."
    hide nina

    show leonid at truecenter
    "Леонид Борисович, 35 лет."
    hide leonid

    show motja at truecenter
    "Мотя, 50 лет."
    hide motja

    show vera at truecenter
    "Вера Михайловна, 38—40 лет."
    hide vera

    "Школьники:"

    show senja at truecenter
    "Сеня, 16 лет"
    hide senja

    show lelja at truecenter
    "Леля, 16 лет"
    hide lelja

    show galja at truecenter
    "Галя, 13 лет"
    hide galja


label Act_1:
    play music "audio/music/12.mp3" fadeout 1.0 fadein 1.0

    scene 2 with fade

    "{b}Акт первый.{/b}"

    menu:
        "{color=#000}Сцена первая{/color}":
            jump Act_1_Scene_1
        "{color=#000}Сцена вторая{/color}":
            jump Act_1_Scene_2
        "{color=#000}Сцена третья{/color}":
            jump Act_1_Scene_3

label Act_1_Scene_1:
    "{b}Сцена первая{/b}"

    show okaemov at truecenter

    "<{i}Кабинет Окаемова. Кабинет представляет собой нагромождение книг и бумаг. Книги везде — на полках, на полу, на диване, который служит постелью Окаемову. Стол вообще заложен бумагами и книгами так, что на нем для работы осталось лишь крошечное место.{/i}>"

    hide okaemov

    "<{i}Из кабинета двери в столовую и переднюю. Передняя видна вся. Из нее одна дверь ведет на лестничную площадку, другая — в кухню и столовую. В передней висит телефон и стоят шкаф с книгами и сундук.{/i}>"

    play sound1 footsteps
    play sound2 telephone

    show okaemov at left
    show motja at right

    "<{i}Сам Окаемов в сидит в кабинете за письменным столом, работая. Звонок телефона. К телефону в передней подходит Мотя, пожилая, полноватая домашняя работница.{/i}>"

    hide okaemov
    hide motja

    stop sound1
    stop sound2

    show motja at truecenter

    $ motja_var = "{noalt}Мотя"

    motja "<{i}(в трубку).{/i}>"

    motja "Кто спрашивает? Его дома нет. И когда будет, неизвестно. Ладно, передам."

    play sound1 footsteps

    motja "<{i}(Вешает трубку, отходит к кабинету и говорит, приоткрыв дверь.){/i}>"

    stop sound1

    motja "В пятницу заседание в академии. В семь часов."

    play sound1 footsteps
    play sound2 telephone

    hide motja

    show motja at left
    show okaemov at right

    motja "<{i}Окаемов хмыкает не оборачиваясь. Мотя отходит, но ее останааливает новый звонок. Она берет трубку.{/i}>"

    hide okaemov

    show motja at truecenter

    stop sound1
    stop sound2

    motja "Дома нет. А-а, тогда погодите, спрошу."

    motja "<{i}(Говорит в дверь.){/i}>"

    motja "Кандидат Персеев. Насчет диссертации, говорит, вы позвонить велели."

    play sound1 footsteps

    motja "<{i}(Уходит.){/i}>"

    stop sound1

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(подымаясь).{/i}>"

    okaemov "Дайте-ка его сюда."

    play sound1 footsteps

    okaemov "<{i}(Идет в переднюю, говорит в телефон.){/i}>"

    stop sound1

    okaemov "Добрый день. Прочел-с. Хм-хм... Да как вам сказать..."

    play sound1 telephone

    okaemov "<{i}Робкий звонок у наружной двери.{/i}>"

    stop sound1

    okaemov "Одну секунду."

    play sound1 footsteps
    play sound2 door_creak

    okaemov "<{i}(Отпирает дверь и возвращается к телефону.){/i}>"

    stop sound1
    stop sound2

    hide okaemov

    play sound1 footsteps

    show masha at left
    show okaemov at right

    "<{i}Входит Маша. Она угловата, застенчива, высока для своих лет, в легоньком осеннем пальто не по росту. В руках у нее рюкзак. Окаемов, не обращая на нее внимания, продолжает говорить. Она, вежливо поклонившись, слушает.{/i}>"

    hide masha
    hide okaemov

    stop sound1

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(в трубку).{/i}>"

    okaemov "На мой взгляд, весьма посредственно. Точнее — просто плохо. Даже очень плохо. Помилуйте, каждый школьник знает, что Татищев открыл только новгородскую летопись «Русской правды», а вы что пишете?"

    okaemov "<{i}(Горячась все больше.){/i}>"

    okaemov "Это не диссертация, а диктант! Ни одной своей мысли. Цитатки и заимствования, без указания источников. Да-да-да! Разучились работать, хм-хм... По заседаниям бегаете, по совещаниям, а наука заседаний не любит."

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}(Вешает трубку, смотрит на Машу.){/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Мотя, к вам пришли."

    play sound1 footsteps

    okaemov "<{i}(Идет к кабинету.){/i}>"

    stop sound1

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я к вам."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Как?.."

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша молча протягивает письмо.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Хм. Письмо? Хорошо, прочту. Ответ сообщу по почте."

    play sound1 footsteps

    okaemov "<{i}(Уходит в кабинет.){/i}>"

    stop sound1

    hide okaemov

    play sound1 footsteps

    show motja at truecenter

    "<{i}В переднюю входит Мотя.{/i}>"

    hide motja

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Тебе чего, милая?"

    hide motja

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я не знаю. Я письмо привезла дедушке..."

    hide masha

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Какой он тебе дедушка? Он — академик."

    hide motja

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я... Я его внучка. Маша."

    hide masha

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Ой! Машенька? Николая Васильевича дочка? Да господи, что ж это? Да откуда же?"

    play sound1 female_cry

    motja "<{i}(Залилась слезами.){/i}>"

    stop sound1

    motja "Да сиротка ты моя родимая! Да Василий Иванович, господи!"

    play sound1 running

    motja "<{i}(Бежит в кабинет.){/i}>"

    stop sound1

    motja "Василь Иванович, что же вы, на самом деле? Вашего покойника Коленьки дочка приехала."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Какая дочка?"

    okaemov "<{i}(Хватает письмо, читает.){/i}>"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Машенька."

    motja "<{i}(Шепотом.){/i}>"

    motja "Видать, и мамаша ее померла. Ну, и приехала."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Мамаша? Нет, мамаша жива... Да-с."

    okaemov "<{i}(Читает письмо.){/i}>"

    okaemov "«Слишком сложно, да и вряд ли нужно объяснять положение Маши в моей новой жизни... Скажу одно: с вами ей будет лучше...» Со мной лучше. Вы откуда знаете, сударыня? Что я, нянька?.."

    okaemov "<{i}(Распаляясь.){/i}>"

    okaemov "Она меня с сыном поссорила, она от меня Николая в Сибирь увезла! Она мне пятнадцать лет на глаза не показывалась, а теперь нате, — посылаю вам свою дочь, приютите ее! Каково?"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Да господи, вы потише. Слышно."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Она здесь? Хм, впрочем, разумеется, где же еще..."

    play sound1 footsteps

    okaemov "<{i}(Расхаживая по кабинету.){/i}>"

    stop sound1

    okaemov "Фффу! Вот, Извольте видеть, ситуация. Так просто, взяла и прислала мне чужого человека — приютите."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Да разве ж чужая она? Внучка ведь."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "А! Оставьте! Я в дедушки не гожусь... Она шуметь будет, кричать, капризничать... Я не умею обращаться с детьми и... и... наконец, отвык от детей..."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Не будет она шуметь, я ей внушу. А спать ей и в кухне можно, со мной, там просторно."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Этого не хватало! В кухне!.. И, главное, я уверен, что характер у нее материнский... Фффу! Сколько ей лет? Хм, около пятнадцати. Скажем, года через три выйдет замуж... мужа приведет в квартиру... Потом младенца родит, пеленки на книгах развесит."

    okaemov "Да-с, Матрена Семеновна, перспектива."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Вы бы ее окликнули. Поздоровались."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм, хм. Позовите... А постель накройте в столовой."

    hide okaemov

    play sound1 footsteps

    show motja at left
    show okaemov at right

    "<{i}Мотя уходит. Окаемов шагает по кабинету.{/i}>"

    hide motja
    hide okaemov

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя"

    hide motja

    show motja at left
    show masha at right

    motja "<{i}(Маше ласково).{/i}>"

    hide masha

    show motja at truecenter

    motja "Ты иди, иди, не бойся. Он только с виду лохматый. Ты ему расскажи по правде, как есть, — он и помягчает."

    play sound1 telephone

    motja "<{i}Звонит телефон.{/i}>"

    stop sound1

    motja "<{i}(Берет трубку.){/i}>"

    motja "Дома нет!"

    play sound1 footsteps

    hide motja

    show motja at left
    show masha at right

    motja "<{i}(Провожает Машу до кабинета и уходит в кухню.){/i}>"

    hide masha

    show motja at truecenter

    stop sound1

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Ну-с, здравствуйте. Так сказать, внучка. Признаться, не ожидал. Хм."

    okaemov "<{i}Пауза.{/i}>"

    okaemov "Что же, собственно, произошло у вас с мамой?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ничего."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Так-таки ничего?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(после паузы).{/i}>"

    masha "Мама замуж вышла."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "А! Понимаю! Новая семья. Второй муж. Быстро. Еще и двух лет не прошло со дня смерти первого."

    okaemov "<{i}(Хмыкнул, отвернулся к книгам.){/i}>"

    okaemov "Должен заявить откровенно: я не разделяю образа действий вашей мамы. Да-с. Это она увезла от меня сына. Он мог бы стать крупным ученым, а из-за нее... он уехал, бросил науку, стал рядовым доктором и умер... вот..."

    okaemov "Я даже не повидал его перед смертью, она не написала мне о его болезни."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    play sound1 female_cry

    masha "<{i}(внезапно, еле сдерживая слезы).{/i}>"

    stop sound1

    masha "Вы не смеете! Вы не смеете так говорить про маму!"

    play sound1 footsteps

    masha "<{i}(Быстро идет к двери.){/i}>"

    stop sound1

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Позвольте... куда вы?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Куда-нибудь."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Фффу!"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}(Догоняет Машу, преграждает ей путь.){/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Послушайте. Так нельзя. Вы ко мне приехали. Я за вас некоторым образом отвечаю. Я согласен не затрагивать этой темы, раз вы считаете... Хм. Сядьте."

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}(Сажает Машу в кресло.){/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Так или иначе — вы приехали. Это — факт. А я — сторонник фактов. И нам необходимо как-то столковаться."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я лучше уйду."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Будет время, и вы уйдете. Вырастете и уйдете. А пока вам придется жить здесь. Хм. В столовой, скажем. Я должен предупредить вас, что живу я одиноко, работаю... даже очень занят. И не люблю, когда мне мешают. Хм."

    okaemov "И, пожалуйста, у меня в кабинете и особенно на столе ничего не трогайте... В каком вы клacce?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "В восьмом."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Придется вас определить в школу... Хм. Вы, конечно, больше любили маму, чем отца... впрочем, не будем касаться этого. Вы устали с дороги. Отдохните. Мотя даст вам покушать."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Не хочу."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Так что ж вы хотите?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    play sound1 female_cry

    masha "<{i}(вдруг заплакала){/i}>"

    stop sound1

    masha ". Домой."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм, хм. Вот, изволите видеть, слезы. Домой! Ваш дом теперь — здесь."

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша отрицательно качает головой.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Прошу вас, не плачьте. Мы подумаем. Я напишу вашей маме. Ho до тех пор придется вам, так сказать, потерпеть, хм, хм."

    play sound1 telephone

    okaemov "<{i}Звонок в передней{/i}>"

    stop sound1

    okaemov "Это ко мне. Прошу вас, отоприте."

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша выходит в переднюю.{/i}>"

    hide masha

    show okaemov at truecenter

    stop sound1

    okaemov "Ффу! Вот-с, дожил!"

    hide okaemov

    play sound1 footsteps

    show masha at left
    show leonid at truecenter
    show okaemov at right

    "<{i}Маша в передней отворяет дверь. Входит Леонид Кареев. Он высок, не особенно складен, размашист в движениях: без шапки, несмотря на позднюю осень, пальто расстегнуто.{/i}>"

    hide masha
    hide leonid
    hide okaemov

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    hide leonid

    show leonid at left
    show masha at right

    leonid "<{i}(увидев Машу).{/i}>"

    hide masha

    show leonid at truecenter

    leonid "Извините, пожалуйста, я ошибся квартирой."

    play sound1 door_creak

    leonid "<{i}(Затворяет за собой дверь.){/i}>"

    stop sound1

    play sound1 footsteps

    hide leonid

    show leonid at left
    show masha at right

    leonid "<{i}Маша хочет уйти. Но стук в наружную дверь останавливает ее. Она отворяет. Снова тот же Леонид.{/i}>"

    hide masha

    show leonid at truecenter

    stop sound1

    leonid "Извините, пожалуйста, я не ошибся квартирой. Но здесь жил Василий Иванович Окаемов... А вы?"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Он — мой дедушка."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "О-о-о! Так у него появилась внучка?! Чудесно, просто чудесно! Здравствуйте."

    hide leonid

    play sound1 kiss

    show leonid at left
    show masha at right

    "<{i}Маша протягивает руку, Леонид целует руку Маши.{/i}>"

    hide leonid
    hide masha

    stop sound1

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(страшно смущена и говорит тихо).{/i}>"

    masha "Спасибо..."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Воображаю, как он счастлив теперь! Внучка! Дочь Николая Васильевича! Я должен его поздравить. Нет, вы со мной, со мной!"

    play sound1 footsteps

    hide leonid

    show leonid at left
    show masha at right

    leonid "<{i}(Проходит с Машей в кабинет.){/i}>"

    hide masha

    show leonid at truecenter

    stop sound1

    leonid "Василий Иванович!"

    leonid "<{i}(Обнимает его.){/i}>"

    leonid "Дорогой старик, поздравляю! Внучка! Она же на вас похожа. Взгляните - глаза, форма носа, рот... К старости сходство еще больше увеличится, уверяю вас! Как ваше имя, если не секрет?"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Маша."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Чудесное имя. Тихое, домашнее — Маша. Машенька! Ах, как я рад за вас, Василий Иванович! Вам для полноты жизни не хватало именно внучки. Детского крика в доме."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Вам не хватало детских рук, которые разметали бы все ваши бумаги с письменного стола..."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм. Я нахожу, что вы, как всегда, увлекаетесь, Леонид Борисович."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Еще бы не увлекаться! Необыкновенной силы внучка! Машенька, когда будете выметать дедушкин стол, выкиньте за окно и этот пузырек с чернилами. Сколько я себя помню, он тут всегда стоит. И купите чернильницу. Большую с бронзовой крышкой... Обещаете?"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... Вы лучше о себе поведайте, Леонид Борисович, где пропадали. Полгода вас не лицезрел."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "По степям мотался, Василий Иванович. Наша жизнь такая — палатка да котелок, сапоги да планшетка. Выбирали место для строительства медного комбината. Представьте себе, к моему удивлению, выбрали именно мой проект."

    leonid "Тридцать тысяч премии отвалили, а? Я теперь богатый жених. Приехал делать подарки. Что вам подарить, Машенька?"

    hide leonid

    show leonid at left
    show masha at right

    leonid "<{i}Маша молчит.{/i}>"

    hide masha

    show leonid at truecenter

    leonid "Я вам мотоциклет куплю."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Нет-нет... не надо."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм. Вы ступайте, Маша..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Куда? Вы, Машенька, его не слушайте и, когда он вас будет бранить, не огорчайтесь и вообще делайте все по-своему, хоть он и академик..."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Леонид Борисович, я того... я серьезно прошу..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Бросьте, дорогой старик, разве вы можете просить серьезно? Вы для этого слишком умны."

    play sound1 punch

    leonid "<{i}(Хлопнул себя по лбу.){/i}>"

    stop sound1

    leonid "А, вот идея! Машенька, вы поете?"

    leonid "<{i}(Встретив ее удивленный взгляд.){/i}>"

    leonid "Вы любите петь?"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(тихо).{/i}>"

    masha "Папа меня учил. А потом он умер, а маме все было некогда."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Папа учил! Чудесно! Это просто чудесно, как все получается. Понимаете, Василий Иванович, я в поезде познакомился с женщиной... Необыкновенной силы женщина... Красива, умна, добра. И, вдобавок, живет в вашем доме. Двумя этажами ниже."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Ну, и что?"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Она учительница пения! Поняли? Я сначала думал сам у нее учиться, но она попробовала мое верхнее «до»... и послала меня за нарзаном. А теперь мы ей сосватаем Машу..."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Позвольте, позвольте! Все это настолько неожиданно..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Я ее сейчас приведу. Вы познакомитесь, и она попробует Машин голос. Одно мгновенье."

    play sound1 footsteps

    hide leonid

    show leonid at left
    show okaemov at right

    leonid "<{i}(Выскакивает в переднюю, прежде чем Окаемов успевает что-либо сказать. Уходит, едва накинув пальто.){/i}>"

    hide okaemov

    show leonid at truecenter

    stop sound1

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но позвольте... Зачем учительница? Он, в самом деле, пошел. Леонид Борисович!.."

    play sound1 punch

    okaemov "<{i}Слышно, как хлопнула входная дверь.{/i}>"

    stop sound1

    okaemov "Ушел... Как же быть?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Мaша."

    masha "Не знаю."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Вот, изволите видеть, ситуация. Побежал за учительницей... Все так, сразу. Он и со мной познакомился подобным образом. Явился как-то перед выборами в Верховный Совет. И начал меня агитировать. Да-с."

    okaemov "Опасался, что я перепутаю и вместо Калинина проголосую за Первопечатника. Хм-хм. Но тут же заявил, что, если бы Первопечатник жил в наше время, его тоже выбрали бы в Верховный Совет. Но, пожалуйста, не принимайте его слова всерьез."

    okaemov "Никакой там чернильницы... и на столе ничего не трогать. Это мое категорическое условие."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Конечно."

    hide masha

    "<{i}Пауза.{/i}>"

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Пение. Хм... Не успели умыться с дороги — и уже пение. Учительница, разумеется, станет вас хвалить. Из меня тоже хотел один итальянец сделать оперного певца... Я вовремя спохватился, благодарение господу... Да-с."

    play sound1 telephone

    okaemov "<{i}Звонок.{/i}>"

    stop sound1

    okaemov "Ну, вот... Никак в самом деле, пришел!"

    okaemov "<{i}(Прислушивается.){/i}>"

    hide okaemov

    play sound1 footsteps

    show masha at left
    show leonid at truecenter
    show nina at right

    "<{i}Маша идет отпереть. В переднюю входят Леонид и Нина. Нине тридцать лет, она одета просто и изящно.{/i}>"

    hide masha
    hide leonid
    hide nina

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Нина Александровна, знакомьтесь. Я знаю — вы ужасно заняты, мы все заняты, но вы найдете время для Машеньки."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Здравствуйте, Маша."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Пойдемте скорей, Окаемов ждет не дождется."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Скажите, вы всегда все делаете так поспешно?"

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "И, добавьте, нескладно... Но, к моему удивлению, все в общем как-то получается."

    play sound1 knocking

    hide leonid

    show leonid at left
    show nina at right

    leonid "<{i}(Стучит в кабинет. Потом вводит туда Нину.){/i}>"

    hide nina

    show leonid at truecenter

    stop sound1

    play sound1 footsteps

    hide leonid

    show leonid at left
    show masha at right

    leonid "<{i}Маша идет за ними.{/i}>"

    hide masha

    show leonid at truecenter

    stop sound1

    leonid "Нина Александровна... Представляю вам — Василий Иванович Окаемов."

    hide leonid

    show leonid at left
    show nina at right

    leonid "<{i}Нина здоровается.{/i}>"

    hide nina

    show leonid at truecenter

    leonid "Крупный ученый..."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Леонид Борисович!"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Необыкновенной силы ученый. Вот, например"

    leonid "<{i}(хватает со стола свиток, развертывает){/i}>"

    leonid ", Машенька даже не знает, что была на свете такая буква «фита»... Да и нам с вами она не очень знакома. А Василий Иванович посмотрит на фиту и скажет, кто ее написал, — Александр Невский или Иван Грозный. Вот и все, что я понимаю в палеографии."

    leonid "Знакомьтесь."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм, хм. Я бы предпочел, так сказать, ближе к делу."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я, право, несколько смущена. Леонид Борисович ворвался и увел меня, не дав опомниться. Он сказал, что вы хотите начать немедленно."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Я? Собственно, я..."

    hide okaemov

    show okaemov at left
    show leonid at right

    okaemov "<{i}(Видя жесты Леонида.){/i}>"

    hide leonid

    show okaemov at truecenter

    okaemov "Хм-хм."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я, Василий Иванович, не совсем разделяю такую стремительность с вашей стороны, но, конечно, понимаю ее. Как всякий дедушка, вы считаете, что вашей внучке суждена слава большой певицы..."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Помилуйте, я совершенно..."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Да-да. Мы теперь так любим молодые дарования, что зачастую безрассудно их портим. Скажу откровенно, Василий Иванович, меня возмущает, когда родители раздувают маленькие таланты своих деток в большие претензии."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(обрадованно).{/i}>"

    okaemov "Очень хорошо! Именно это я и хотел сказать. Легкая слава... Хлопки... и пошло — раздуют, заласкают, а голоса нет. И жизнь испорчена... Хм... хм... Крайне признателен, что и вы так думаете."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "В таком случае я просто послушаю Машу и скажу откровенно, стоит ли ей заниматься. Согласны?"

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "То есть я всецело. Весьма признателен!"

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "У вас есть рояль?"

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Где-то был... в столовой. Заперт лет пятнадцать. С отъезда сына. Маша, подайте мне коробку. Да, эту. Вот-с. Ключ и... пожалуйста, не делайте из нее певицы."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(улыбнувшись).{/i}>"

    nina "Постараюсь. Пойдемте, Маша."

    hide nina

    play sound1 footsteps

    show nina at left
    show masha at right

    "<{i}Нина уходит с Машей в столовую.{/i}>"

    hide nina
    hide masha

    stop sound1

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ффу! Вкатили вы меня в историю, молодой человек! Хорошо еще, что учительница — умная женщина."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "А я? Разве я глуп, что привел ее? Машенька будет петь вам по целым дням."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Этого недоставало! Я должен поставить вас в известность, Леонид Борисович, обо всей истории с внучкой и тому подобное."

    hide okaemov

    show okaemov at left
    show leonid at right

    okaemov "<{i}(Протягивает ему письмо.){/i}>"

    hide leonid

    show okaemov at truecenter

    okaemov "Вот-с. Прочтите."

    hide okaemov

    show leonid at truecenter

    "<{i}Леонид читает. Из столовой доносятся звуки Машиного голоса, пробуются гаммы под рояль.{/i}>"

    hide leonid

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(кончив читать).{/i}>"

    leonid "Понятно..."

    leonid "<{i}(Задумчиво.){/i}>"

    leonid "Вот что, Василий Иванович, мы возьмемся за Машенькино будущее вместе! Мы докажем, что двое холостых мужчин могут заменить одну замужнюю мать! Конечно, Машенька и без нас не пропала бы. Теперь люди не пропадают."

    leonid "Из меня — шахтерского сироты — инженера сделали... Но не в этом дело! Ребенок просветляет душу, Василий Иванович."

    leonid "Вы увидите, как из маленького существа разовьется разумный организм, как детский ее голосок станет, может быть, голосом таланта, покоряющего сердца, и вся она раскроется перед вами, как ваша мечта о лучшем, ваше продолжение в бессмертии."

    leonid "Вы согреете ее своим сердцем, а когда она вылетит в жизнь, будете любоваться ее полетом. Так, дорогой старик?"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... Вы меня совершенно сбили с толку..."

    hide okaemov

    play sound1 footsteps

    show masha at left
    show nina at right

    "<{i}Из столовой входят Маша и Нина.{/i}>"

    hide masha
    hide nina

    stop sound1

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "У Маши довольно приятный голос и хороший слух. Я думаю, ей стоит заниматься."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Я, собственно, не предполагал. Но если Вы находите..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Именно, находим. Спасибо, Машенька! Не подвели меня."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    hide nina

    show nina at left
    show okaemov at right

    nina "<{i}(прощаясь с Окаемовым).{/i}>"

    hide okaemov

    show nina at truecenter

    nina "Домашние занятия пением довольно утомительны для постороннего слуха, но мы постараемся тянуть свои гаммы в ваше отсутствие."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Вот именно. Благодарю вас."

    hide okaemov

    play sound1 footsteps

    show nina at left
    show masha at truecenter
    show leonid at right

    "<{i}Нина, Маша, Леонид проходят в переднюю.{/i}>"

    hide nina
    hide masha
    hide leonid

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(одеваясь).{/i}>"

    leonid "Нина Александровна! Скажите, чего вам особенно хочется?"

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(улыбаясь).{/i}>"

    nina "Чтобы вы подали мне пальто."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "А, черт!"

    leonid "<{i}(Кидается к вешалке, подает.){/i}>"

    leonid "Отвык, знаете. Степная жизнь."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Благодарю вас. До свиданья, Маша. Не забудь — завтра в девять."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(горячо).{/i}>"

    masha "Ни за что не забуду."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Я провожу вас. Машенька, ручку. Завтра поедем в оперу. Возьму ложу! Выше голову, Машенька! Жизнь только еще начинает вам улыбаться!"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(тихо).{/i}>"

    masha "Спасибо!"

    hide masha

    play sound1 footsteps
    play sound2 male_sigh

    show nina at left
    show okaemov at truecenter
    show masha at right

    "<{i}Леонид и Нина уходят. Машенька стоит в раздумье в передней. Окаемов — в кабинете. Оба с разных сторон подходят к двери, отделяющей кабинет от передней, и оба не решаются ее открыть. Машенька, вздохнув, уходит.{/i}>"

    hide leonid
    hide nina
    hide okaemov
    hide masha

    stop sound1
    stop sound2

    play sound1 footsteps

    show okaemov at truecenter

    "<{i}Окаемов, махнув рукой, отходит к письменному столу.{/i}>"

    hide okaemov

    stop sound1

    "<{i}Занавес{/i}>"

label Act_1_Scene_2:
    "{b}Сцена вторая{/b}"

    play sound1 footsteps

    show okaemov at left
    show masha at truecenter
    show viktor at right

    "<{i}Через несколько дней. Та же обстановка. В кабинете Окаемов полулежит в кресле. Правая нога его забинтована в колене и лежит на подушке, на табурете. Около него книги, он читает. В переднюю входят Маша и Виктор. Виктор изящен, самоуверен, хорошо одет.{/i}>"

    hide okaemov
    hide masha
    hide viktor

    stop sound1

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Heт, Маша, я разочарован в жизни."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Зачем ты говоришь так, Витя?"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Ах, жизнь, как посмотришь с холодным вниманьем вокруг, такая пустая и глупая шутка."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ты такой веселый в школе... всегда смеешься, фокусы показываешь... А тут вдруг..."

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Все это маска, Маша."

    hide viktor

    show viktor at left
    show masha at right

    viktor "<{i}Маша садится на сундук.{/i}>"

    hide masha

    show viktor at truecenter

    viktor "<{i}(Стоит около, опершись о стену.){/i}>"

    viktor "Ты любишь Блока?"

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Не знаю."

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Неплохо писал старик... «Как тяжело ходить среди людей и притворяться непогибшим. Все пройдет, как с белых яблонь дым». Впрочем, это из другой оперы... Я тебе нравлюсь, Маша?"

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Да, Витя, только ты странный сейчас... Непохожий."

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Это оттого, что никто меня не понимает. И никому меня не жаль."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Нет, Витя, нет. Я понимаю тебя. Ты, наверно, такой же одинокий, как я. Я от мамы уехала... к дедушке. А дедушка сердится, зачем я приехала. Я мешаю ему. Он молчит, а я вижу. Я ему не нужна. Я даже хотела уехать куда глаза глядят..."

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Я тоже."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(быстро).{/i}>"

    masha "Не надо, Витя. Теперь у меня есть друг, Леонид Борисович... Он такой хороший, такой хороший... Вот ты познакомишься с ним, и тебе станет Лучше."

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Мне дружбы мало, Маша. Мне нужна любовь!"

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Он будет тебя любить, Витя!"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "А ты?"

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я тоже."

    play sound1 kiss

    hide masha

    show masha at left
    show viktor at right

    masha "<{i}Виктор быстро обнимает ее и целует.{/i}>"

    hide viktor

    show masha at truecenter

    stop sound1

    masha "<{i}(Не успевает отстраниться. Растерянно.){/i}>"

    masha "Витя... зачем?"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Кого любишь, того целуешь — вот зачем. Без поцелуев нет любви."

    hide viktor

    play sound1 footsteps

    show motja at truecenter

    "<{i}Из кухни в кабинет, неся чайник, проходит Мотя.{/i}>"

    hide motja

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Шли бы в комнату, чем тут торчать."

    hide motja

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Витя сейчас уйдет... До свиданья, Витя."

    hide masha

    play sound1 footsteps

    show motja at left
    show masha at truecenter
    show okaemov at right

    "<{i}Мотя прошла в кабинет. Там она подает чай, поправляет Окаемову подушку.{/i}>"

    hide motja
    hide masha
    hide okaemov

    stop sound1

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор"

    hide viktor

    show viktor at left
    show masha at right

    viktor "<{i}(пытаясь снова обнять Машу).{/i}>"

    hide masha

    show viktor at truecenter

    viktor "Ты напишешь мне письмо. О том, как ты меня любишь."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(отстраняясь).{/i}>"

    masha "Я напишу... напишу... только не надо так..."

    hide masha

    play sound1 footsteps
    play sound2 telephone

    show masha at left
    show tumanskij at right

    "<{i}Звонок. Маша спешит отпереть. Входит Туманский — хорошо сложенный мужчина, с проседью у висков, с манерами и жестами уверенного в себе человека.{/i}>"

    hide masha
    hide tumanskij

    stop sound1
    stop sound2

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    hide tumanskij

    show tumanskij at left
    show viktor at right

    tumanskij "<{i}(увидев Виктора).{/i}>"

    hide viktor

    show tumanskij at truecenter

    tumanskij "Ба! Сын мой! И ты здесь... Наш пострел везде поспел. Ах, вы и есть та самая Маша? Здравствуйте. Говорят, вы похожи на маму. А ну, покажитесь. Да, да, есть сходство. Ваша мама была красивой женщиной, я ее хорошо знал. Говорят, она снова вышла замуж?"

    hide tumanskij

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(тихо).{/i}>"

    masha "Да."

    hide masha

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Виктор, поручаю тебе заботу о Маше. Покажи ей Москву, своди в театры, будь ей хорошим другом. Понял?"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Видишь, понял."

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вижу, вижу. Вы, Маша, держите его в руках. Сын мой — порядочный шалопай. Не давайте ему спуску. И — кстати — заставьте его учиться как следует."

    hide tumanskij

    show tumanskij at left
    show viktor at right

    tumanskij "<{i}(Виктору.){/i}>"

    hide viktor

    show tumanskij at truecenter

    tumanskij "Не дергай носом, я знаю, что говорю."

    hide tumanskij

    play sound1 footsteps
    play sound2 telephone

    show masha at left
    show nina at right

    "<{i}Звонок. Маша отпирает. Входит Нина.{/i}>"

    hide masha
    hide nina

    stop sound1
    stop sound2

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Здравствуйте, Нина Александровна."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Здравствуй, девочка."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "А-а-а, вы и есть та самая Нина Александровна? Познакомьте нас, Маша. Я именно такой и представлял вас по описанию Леонида. Он столько говорил мне о Машиной учительнице, что я горел нетерпением познакомиться. Туманский."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "А-а-а! Вы и есть тот самый доктор Туманский, которому все удается в жизни?"

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Это что — слова Леонида?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Да."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Постараюсь их оправдать в ваших глазах."

    hide tumanskij

    show tumanskij at left
    show nina at right

    tumanskij "<{i}(Быстро принимает пальто Нины, вешает.){/i}>"

    hide nina

    show tumanskij at truecenter

    tumanskij "Мой сын. Мечтаю сделать из него Козловского — при вашем содействии. Серьезно, займитесь мальчишкой. Его покойная мать была певицей. Виктор, желаешь заниматься вместе с Машей?"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Непрочь."

    hide viktor

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Почему же вы не учили сына раньше?"

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Потому что не было вас. Мы еще увидимся, не прощаюсь."

    hide tumanskij

    play sound1 footsteps

    show motja at truecenter

    "<{i}Входит Мотя.{/i}>"

    hide motja

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Шли бы в комнаты, чем тут торчать."

    hide motja

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Идем, Мотя. Идем. Где больной?"

    play sound1 footsteps

    hide tumanskij

    show tumanskij at left
    show motja at truecenter
    show okaemov at right

    tumanskij "<{i}(Проходит с Мотей в кабинет, здоровается с Окаемовым, начинает осматривать ногу.){/i}>"

    hide motja
    hide okaemov

    show tumanskij at truecenter

    stop sound1

    hide tumanskij

    play sound1 footsteps

    show nina at left
    show masha at truecenter
    show viktor at right

    "<{i}Нина, Маша и Виктор проходят в столовую. Там начинается урок, слышный в отдельных негромких звуках голосов и рояля.{/i}>"

    hide nina
    hide masha
    hide viktor

    stop sound1

    "<{i}В кабинете{/i}>"

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    tumanskij "<{i}(осматривая ноту).{/i}>"

    tumanskij "Как это вы ухитрились, Василий Иванович?"

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Да вот, извольте видеть, все из-за девочки. Получил повестку на родительское собрание, в школу. Пришлось пойти, поскольку — повестка... Только вышел из дому — хлоп, поскользнулся, и вот, пожалуйте... растяжение."

    okaemov "Я всегда знал, что с детьми много хлопот, но чтобы до такой степени... Ой, больно!"

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Это хорошо, что больно. Мотя, бинтов и компресс!"

    play sound1 footsteps

    hide tumanskij

    show tumanskij at left
    show motja at right

    tumanskij "<{i}Мотя входит.{/i}>"

    hide motja

    show tumanskij at truecenter

    stop sound1

    tumanskij "A внучка ваша похожа на свою мать."

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Можете быть уверены, что это сходство не доставляет мне особенного удовольствия."

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Пора забыть старые распри, Василий Иванович. Как-никак, Вера Михайловна искренно любила вашего сына."

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Это не мешало ей принимать даже ваши ухаживания, Павел Павлович."

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Почему «даже»? Женщина она была красивая, и вполне естественно, что я..."

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Естественно? Хм... Позволю заметить, что Николай считался вашим другом-с..."

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Дело прошлое, Василий Иванович, но там, где говорит любовь, молчит дружба."

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Странная у вас философия, Павел Павлович... и для меня неприемлемая."

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Такова жизнь, и не нам ее осуждать."

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Вот-вот! Как только необходимо оправдать натуру, сейчас изреченьице. Такова жизнь. Любви все возрасты покорны. Сегодня ты, a завтра я — и пожалуйте. Нет, нет, не продолжайте, Павел Павлович, поссоримся."

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Извольте. Переменим тему. Я человек покладистый."

    hide tumanskij

    play sound1 footsteps
    play sound2 telephone

    show motja at left
    show leonid at right

    "<{i}Звонок. Мотя идет отпереть. Входит Леонид со свертками руках.{/i}>"

    hide motja
    hide leonid

    stop sound1
    stop sound2

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Как нога?"

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Доктор смотрит, Павел Павлович."

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Чудесно! Этот вылечит. А Машенька?"

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Сидим на кухне по вечерам, — дедушка не зовет. Все один. Ей, видать, невесело, а молчит. Скрывает."

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Скрывает?"

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Ох, скрывает!"

    hide motja

    play sound1 footsteps

    show leonid at left
    show motja at right

    "<{i}Леонид проходит в кабинет со свертками. Мотя сним.{/i}>"

    hide leonid
    hide motja

    stop sound1

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "А-а! Милейший геолог! А я видел, видел!"

    hide tumanskij

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Мои покупки?"

    hide leonid

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Нину Александровну. Браво, браво! Весьма, весьма! Я к ней Виктора определяю в ученики."

    hide tumanskij

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "О, Павел Павлович, зацепился! Я так и знал. Каков ход! Виктора. Чудесно у вас получается."

    hide leonid

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "А у вас?"

    hide tumanskij

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Э! Нет уж, я не создан для женского общества. Жена будет страдать от моих привычек. Холостяком помру."

    hide leonid

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вы серьезно?"

    tumanskij "<{i}(Прислушиваясь к голосам в столовой.){/i}>"

    tumanskij "Пойду послушать Виктора."

    play sound1 footsteps

    tumanskij "<{i}(Уходит в столовую.){/i}>"

    stop sound1

    hide tumanskij

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(разворачивает сверток).{/i}>"

    leonid "Ну, дорогой старик, вот вам чернильница, наконец!"

    leonid "<{i}(Достает громадную чернильницу.){/i}>"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм. Это не чернильница, а ведро. Не возьму, Леонид Борисович."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Возьмете, Василий Иванович."

    leonid "<{i}(Ставит на стол и разворачивает второй сверток.){/i}>"

    leonid "Бюст неизвестного мудреца. Скорее всего Гераклита. Попробуйте не взять."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Позвольте, к чему мне Гераклит?"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Другого в комиссионном магазине не оказалось."

    leonid "<{i}(Разворачивает третий сверток.){/i}>"

    leonid "Домашний халат китайской работы... Но это не вам."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Вы что, собственно говоря, затеяли, Леонид Борисович?"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Трачу премию, Василий Иванович. Чертовски приятно, оказывается, делать подарки. Хожу и высматриваю, что бы еще такое купить и кому. Что вам нужно? Скажите, сделайте удовольствие одинокому богачу."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Шнурки для ботинок."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Шнурки и ботинки. Замётано. Машеньке я подарю часы."

    leonid "<{i}(Вынимает.){/i}>"

    leonid "Омега — на золотом браслете. Потом сумочку и шелковые чулки, только они почему-то разного цвета. Ну, их можно и не дарить. И присмотрел дамский велосипед — на лето..."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Нет-с, Леонид Борисович, шутки шутками, но тут я протестую категорически. Нельзя! Девочке пятнадцать, а уже золотые часы. Вы знаете, когда я себе заработал на первые часы? В тридцать лет!"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    play sound1 male_sigh

    leonid "<{i}(вздыхая).{/i}>"

    stop sound1

    leonid "Понял, понял. Прячу. Пусть полежат у вас. Подарите, когда придет время."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... Я уважаю жизнь простую и строгую. Финтифлюшки портят характер. И я, хм-хм, ничего девочке дарить не намерен... И вообще считаю, что нельзя любовь приобретать подарками. Да-с..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(смотрит на халат).{/i}>"

    leonid "В самом деле. Но я от чистого сердца... И вовсе не с целью приобретения любви. Как вы думаете, она обидится, если ей подарить xaлат?"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Раз и навсегда, молодой человек. С того дня, как девочка поселилась здесь, все пошло вверх ногами! Учительницы, подруги, уроки, нога! Я — терпелив, я все переношу, но халата в доме не будет. Этот халат — куртизанке впору. Да-с. Именно — куртизанке."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(задумчиво).{/i}>"

    leonid "Неужто он так игриво выглядит? Да вы не волнуйтесь — халат не Машеньке, а Нине Александровне."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ах, учительнице! Хм..."

    hide okaemov

    show okaemov at left
    show leonid at right

    okaemov "<{i}(Пристально смотрит на Леонида.){/i}>"

    hide leonid

    show okaemov at truecenter

    hide okaemov

    play sound1 footsteps

    show leonid at left
    show tumanskij at right

    "<{i}Леонид смущенно теребит халат. В переднюю тихо выходит Туманский. Набирает номер телефона.{/i}>"

    hide leonid
    hide tumanskij

    stop sound1

    "<{i}В передней{/i}>"

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Ирину Сергеевну. Ира? Это Павел. Я говорю из клиники. Неожиданная операция. Я задержусь и вечером не приеду. Не рассчитывай на меня. Д-да, ужасно досадно. Да. Я тоже. Конечно, крепко."

    play sound1 footsteps

    hide tumanskij

    show tumanskij at left
    show viktor at truecenter
    show okaemov at right

    tumanskij "<{i}(Вешает трубку, замечает Виктора, который тоже вышел в переднюю и слушал его разговор.){/i}>"

    hide viktor
    hide okaemov

    show tumanskij at truecenter

    stop sound1

    tumanskij "Что тебе?"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Подкинь тридцаткy, старик."

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Зачем?"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "За мое несостоявшееся пение."

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Сын, не хами!"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Такова жизнь, и не нам ее осуждать."

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    play sound1 male_laughter

    tumanskij "<{i}(смеясь).{/i}>"

    stop sound1

    tumanskij "Ох, нахал!"

    tumanskij "<{i}(Дает деньги.){/i}>"

    tumanskij "И в кого ты только растешь?"

    play sound1 footsteps

    hide tumanskij

    show tumanskij at left
    show masha at truecenter
    show nina at right

    tumanskij "<{i}В переднюю входят Маша и Нина.{/i}>"

    hide masha
    hide nina

    show tumanskij at truecenter

    stop sound1

    hide tumanskij

    show tumanskij at left
    show nina at right

    tumanskij "<{i}(Помогая Нине одеться).{/i}>"

    hide nina

    show tumanskij at truecenter

    tumanskij "Я бы хотел сам заниматься с вами. Вы так увлекательно преподаете."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я не люблю комплиментов, Павел Павлович. Они все утомительно одинаковы."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "И все одинаково приятны, несмотря на их утомительность. Но мои слова не комплимент. Я искренно восхищен вашим методом... Что вы делаете вечером?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я? Странный вопрос. Иду на концерт Прокофьева."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вот совпадение! Я — тоже. Маша, передайте дедушке мой привет. Ноге — полный покой. Заеду завтра."

    play sound1 footsteps

    hide tumanskij

    show tumanskij at left
    show nina at right

    tumanskij "<{i}(Уходит с Ниной.){/i}>"

    hide nina

    show tumanskij at truecenter

    stop sound1

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Видела?"

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "О чем ты, Витя?"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Ты еще многого не понимаешь в жизни. До свиданья, не забудь про письмо. Обещала."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "До свиданья, Витя. Я напишу."

    play sound1 footsteps

    masha "<{i}(Уходит в кабинет.){/i}>"

    stop sound1

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор"

    viktor "<{i}(набирает номер телефона).{/i}>"

    viktor "Верка? Виктор. Задержался, понимаешь, на кружке. Бегу. Билеты у меня. Успеем."

    play sound1 footsteps
    play sound2 whistle

    viktor "<{i}(Выходит, насвистывая «Кукарачу».){/i}>"

    stop sound1
    stop sound2

    hide viktor

    "<{i}В кабинете{/i}>"

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ушел. Хм-хм..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "С Ниной Александровной?"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Да. Просил передать — полный покой ноге."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Благодарю вас. Ступайте."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Пойду и я."

    leonid "<{i}(Кое-как заворачивает халат.){/i}>"

    leonid "Не скучайте, Василий Иванович."

    leonid "<{i}(Смотрит на бюст Гераклита.){/i}>"

    leonid "Все течет, все изменяется."

    play sound1 footsteps

    hide leonid

    show leonid at left
    show masha at right

    leonid "<{i}(Выходит с Машей в переднюю.){/i}>"

    hide masha

    show leonid at truecenter

    stop sound1

    hide leonid

    "<{i}В передней{/i}>"

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Машенька, по секрету."

    leonid "<{i}(Вполголоса.){/i}>"

    leonid "Деду вашему скучно. Побудьте с ним."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ему неинтересно со мной."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "А вы сделайте так, чтобы было интересHO. Расскажите ему что-нибудь."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Он не захочет. Он занят."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Он только делает вид, что занят. Вы попробуйте. Хорошо?"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Спасибо, попробую."

    hide masha

    play sound1 footsteps

    show motja at truecenter

    "<{i}Входит Мотя.{/i}>"

    hide motja

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "А-а... Мотя. Я вот купил кое-что... Как вы находите этот цвет?"

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Хорош, хорош."

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Носите на здоровье."

    play sound1 footsteps

    hide leonid

    show leonid at left
    show motja at right

    leonid "<{i}(Сует ей в руки сверток с халатом и быстро выходит.){/i}>"

    hide motja

    show leonid at truecenter

    stop sound1

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя"

    motja "<{i}(развернув халат).{/i}>"

    motja "Ой, куда же мне такой? Леонид Борисович! Убег. Этакая красота, прости господи!"

    motja "<{i}(Напяливает халат.){/i}>"

    hide motja

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ух, ты! Весь в птицах."

    hide masha

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Хороша?"

    hide motja

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Как в цирке."

    hide masha

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "До чего добёр человек. Идем — похвастаем."

    play sound1 footsteps

    hide motja

    show motja at left
    show masha at right

    motja "<{i}(Входит с Машей в кабинет.){/i}>"

    hide masha

    show motja at truecenter

    stop sound1

    motja "Гляньте, Василий Иваныч. Вашей Матрене подарочек!"

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Что-о? Опять халат?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Это ей Леонид Борисович такую штуку нашел."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Баядерка! Гурия! Ха-ха-ха! Теперь мне чалму — и можно открывать гарем. Ха-ха-ха! Ой!"

    okaemov "<{i}(Дергается от неловкого поворота.){/i}>"

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша быстро подходит и поправляет ему ногу. Он недоверчиво следит за ее движениями.{/i}>"

    hide masha

    show okaemov at truecenter

    stop sound1

    okaemov "Выше! Сюда подушку. Благодарю вас."

    hide okaemov

    show okaemov at left
    show motja at right

    okaemov "<{i}(Взглянув на Мотю.){/i}>"

    hide motja

    show okaemov at truecenter

    okaemov "Ха-ха-ха!"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Э, да будет вам изголяться!"

    play sound1 footsteps

    motja "<{i}(Сердито махнув рукой, уходит.){/i}>"

    stop sound1

    hide motja

    show okaemov at left
    show masha at right

    "<{i}Окаемов и Маша посмотрели друг на друга и засмеялись вновь.{/i}>"

    hide okaemov
    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... Золотой халат! Ну, благодарю вас. Можете итти."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    play sound1 footsteps

    masha "<{i}(отходит к двери, потом останавливается).{/i}>"

    stop sound1

    masha "Хотите, я почитаю вам вслух?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Мне? Вслух? Зачем?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Так. Папа любил, когда я ему сказки читала."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Сказки? Нет. Сказки мне уж недоступны."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ну, тогда — «Давид Копперфильд»."

    hide masha

    play sound1 footsteps

    show masha at left
    show okaemov at right

    "<{i}Маша выходит в столовую и возвращается оттуда с книгой. Она садится на маленькую скамейку у ног Окаемова и раскрывает книгу.{/i}>"

    hide masha
    hide okaemov

    stop sound1

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "А! Ах, это вы мне... Диккенс. Я родился в день его смерти. Девятого июня семидесятого года... А разве современная молодежь любит Диккенса?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(смущенно).{/i}>"

    masha "У нас в классе любят."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "У вас в классе? И у нас в классе читали Диккенса. Только это было шестьдесят лет назад."

    okaemov "<{i}(Усмехнулся.){/i}>"

    okaemov "Я как раз всхлипывал над «Крошкой Доррит», когда отец закричал, что Александр Второй убит. Мои слезы он принял за выражение верноподданнических чувств и очень этому удивился."

    okaemov "<{i}(Задумался, потом.){/i}>"

    okaemov "Как там начинается?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(читает).{/i}>"

    masha "«В самом начале моего жизнеописания я должен упомянуть, что родился я в пятницу, в полночь. Замечено было, что мой первый крик раздался, когда начали бить часы...»"

    hide masha

    play sound1 clock

    "<{i}В столовой начинают бить часы.{/i}>"

    stop sound1

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "А?"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}(Поглядел на Машу.){/i}>"

    hide masha

    show okaemov at truecenter

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Она на него. Улыбнулись.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Совпадение. Хм..."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "«Сиделка и несколько мудрых соседей, живо заинтересовавшись моей особой, объявили, что мне суждено быть несчастным в жизни...»"

    masha "<{i}(Запнулась.){/i}>"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}(посмотрел на нее, задумчиво).{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Совпадение..."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(продолжает).{/i}>"

    masha "«Они были убеждены, что такова неизбежная судьба всех злосчастных младенцев обоего пола, родившихся в пятницу»."

    hide masha

    "<{i}Занавес{/i}>"

label Act_1_Scene_3:
    "{b}Сцена третья{/b}"

    show okaemov at left
    show motja at right

    "<{i}Та же комната через неделю. Окаемов сидит у стола, работая. Больная нога его протянута под столом. Рядом — трость для ходьбы. Вечер. Горит настольная лампа. Мотя вносит чай.{/i}>"

    hide okaemov
    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(бормоча про себя, когда пишет).{/i}>"

    okaemov "«Ирское и англо-саксонское письмо, довольно далекое от римского курсива, хотя, несомненно, родственно с ним...» Да-с... родственно..."

    okaemov "<{i}(Задумался.){/i}>"

    okaemov "Маша дома?"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Гуляет, поди, с подружками."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Уже поздно."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Восьми нет. Озябнет и явится."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "То есть как озябнет?"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "А как люди зябнут? От холода. Зима на носу, а на ней одно пальтишко осеннее. Ходит, дрожит, а спросишь — отвечает: «Тепло»."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Позвольте. Почему дрожит? Если ей холодно, надо шубу. Ей надо шубу купить."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Ох, надо бы."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Неужели вы сами не могли догадаться? Странно! Девочка зябнет, а вы молчите. Не понимаю. Ходит по дому в золотом халате и молчит. Возьмите деньги. В коробке из-под сигар. Ну? Нашли?"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Нашла, Василъ Иваныч, да мало. Тут и двух сотен не наберешь."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Разве? Куда же деньги идут?"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "На книги, Василь Иваныч. Вчера на тысячу рублей принесли. Уж подождем до получки."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "А она дрожит?.."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Дрожит."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Нет-с, не будем ждать до получки. Подайте мне с той вон полки, левей, левей. Тут. Да. Три книги в толстых переплетах. Маленькие, да."

    hide okaemov

    show okaemov at left
    show motja at right

    okaemov "<{i}(Берет из рук Моти книги, смотрит на них, стирает пыль.){/i}>"

    hide motja

    show okaemov at truecenter

    okaemov "Вот отнесите их в магазин, где мы берем книги, — продайте. И купите шубу."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Смеетесь, Василь Иваныч, на них разве что варежки купишь. А вы — шубу."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "На эти три книги вы купите и шубу, и варежки. И еще коньки, коньки. И не забудьте в лавке сказать, что книги от Окаемова. А то вас заберут в милицию за продажу краденых ценностей."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя"

    motja "<{i}(качает с сомнением головой).{/i}>"

    motja "Ну и ну!"

    hide motja

    play sound1 footsteps
    play sound2 telephone

    show motja at left
    show leonid at right

    "<{i}В передней звонок. Мотя выходит отпереть. Входит Леонид с ящиком.{/i}>"

    hide motja
    hide leonid

    stop sound1
    stop sound2

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    hide leonid

    show leonid at left
    show motja at right

    leonid "<{i}(увидев у Моти книги).{/i}>"

    hide motja

    show leonid at truecenter

    leonid "Ο, тетя Мотя! И вы взялись за палеографию."

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя"

    motja "<{i}(показывая книги).{/i}>"

    motja "Вот тебе — шуба. Вот — коньки. А вот — варежки. Кто умен — догадайся, а кто глуп-молчи, жди до завтра."

    play sound1 footsteps

    motja "<{i}(Уходит.){/i}>"

    stop sound1

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(вслед).{/i}>"

    leonid "Не так, не так надо загадывать. Не дерево, а с листочками, не рубашка, а сшита. Что такое? Книга."

    play sound1 footsteps
    play sound2 knocking

    leonid "<{i}(Стучит в дверь кабинета. Входит.){/i}>"

    stop sound1
    stop sound2

    leonid "Добрый вечер, Василий Иванович."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Добрый вечер. Присядьте. Кончаю."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    hide leonid

    show leonid at left
    show okaemov at right

    leonid "<{i}(вынимает из ящика радиоприемник, пристраивает незаметно от Окаемова).{/i}>"

    hide okaemov

    show leonid at truecenter

    leonid "Меня всегда поражала в вас эта невозмутимость к внешним событиям. В мире происходит черт знает что, но вы спокойно продолжаете писать о пергаментах седьмого века. Вся Европа в бомбах, дорогой старик, а у вас даже радио нет. Поразительно!"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(продолжает писать, потом кладет перо, потирает руки).{/i}>"

    okaemov "Да-с, поразительно. Не то поразительно, что я изучаю пергаменты, а то, что мы можем позволить себе изучать пергаменты, когда кругом война."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Хорошо сказано, Василий Иванович, но радио вам все-таки необходимо."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Не люблю. Шумит."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Поздно. Я уже купил."

    leonid "<{i}(Включает радио.){/i}>"

    hide leonid

    "<{i}Музыка.{/i}>"

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ффу! Послушайте. Это же невозможно!"

    okaemov "<{i}(Прислушивается к музыке.){/i}>"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Для меня теперь нет ничего невозможного."

    play sound1 male_sigh

    leonid "<{i}(Вздыхая.){/i}>"

    stop sound1

    leonid "Впрочем, есть!.. Хотел купить кое-что Нине Александровне, но раздумал. Туманский может обидеться."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм... При чем тут Павел Павлович?"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "О, там разворачивается на полный ход! Как я и предполагал. Пришел, увидел, победил! Он каждый вечер у нее в гостях. Она из вежливости и меня зовет, но я не лыком шит — понимаю. И нахожу предлоги. Уже сочиняю, исподволь, свадебный тост."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... Торопитесь, как обычно. Так-с. Она производит приятное впечатление... эта учительница. То-то доктор не заглядывает больше. Да..."

    hide okaemov

    play sound1 footsteps
    play sound2 telephone

    show leonid at left
    show nina at right

    "<{i}Замолчали. Звонок. Леонид спешит открыть. Входит Нина.{/i}>"

    hide leonid
    hide nina

    stop sound1
    stop sound2

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "О! Легки на помине. Чем вы встревожены?"

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Ничего страшного. Проведите меня к Василию Ивановичу."

    play sound1 footsteps

    nina "<{i}Они проходят в кабинет.{/i}>"

    stop sound1

    nina "Простите мое вторжение. Маша ушла из школы и не хочет туда возвращаться."

    hide nina

    show okaemov at left
    show leonid at right

    $ okaemov_var = "{noalt}Окаемов и Леонид"

    okaemov "<{i}(вместе).{/i}>"

    hide okaemov
    hide leonid

    show okaemov at left
    show leonid at right

    okaemov "Что?.. Как ушла? Куда?"

    hide leonid

    show okaemov at truecenter

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Она прибежала ко мне... Дело в том, что один Машин однокласcник держал пари с товарищами, что Маша напишет ему письмо с объяснением в любви... Он своего добился. Она написала ему. Милое, полное глубокой нежности письмо. О том, как она одинока."

    nina "О своей тоске по настоящей дружбе. Это письмо мальчик прочел вслух перед приятелями. Новость разнеслась по классу, и когда Маша явилась, она прочитала на классной доске веселые стишки про свою любовь, про письмо и поцелуи..."

    nina "Все громко смеялись, а этот мальчик громче всех. Тогда Маша вырвала у него письмо и убежала..."

    play sound1 footsteps

    hide nina

    show nina at left
    show leonid at right

    nina "<{i}Леонид вскочил, торопится к двери.{/i}>"

    hide leonid

    show nina at truecenter

    stop sound1

    nina "Куда вы?"

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "К Машеньке."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Постойте, Маша не должна знать."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Она сама мне расскажет."

    play sound1 footsteps

    leonid "<{i}(Уходит.){/i}>"

    stop sound1

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм. Вот, извольте видеть, ситуация."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Больше всего Маша боится, что вы узнаете и рассердитесь."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Я — в роли деспота. Хм..."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Приласкайте Машу, Василий Иванович. Ведь вся ее так называемая любовь выросла из детской жажды ласки, которой она лишена. Убедите ее, что вся история с письмом пустяки и забудется через три дня. Скажите ей, что вы не сердитесь, утешьте ее..."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм. Приласкать. Утешить. Но как же? Она же не подойдет так просто. И я не умею. Не знаю, что говорить в подобных случаях."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Меньше всего думайте о словах, слова придут сами. Только будьте с ней ласковы."

    hide nina

    "<{i}Пауза.{/i}>"

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но кто же этот... молодой негодяй?"

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "К сожалению, сын Туманского. Виктор."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Как? Павла Павловича? Плоды его философии... Но насколько мне известно... Вы, так сказать, имеете некоторое влияние на Туманского..."

    hide okaemov

    show okaemov at left
    show nina at right

    okaemov "<{i}Нина молчит.{/i}>"

    hide nina

    show okaemov at truecenter

    okaemov "Я не вмешиваюсь в чужую жизнь, но позвольте заметить, что вам надо было бы заняться воспитанием юноши, который... хм-хм, может быть, станет вашим, так сказать, почти сыном..."

    okaemov "Если вы, разумеется, не намерены отправить Виктора к какому-нибудь «дедушке»."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(после паузы).{/i}>"

    nina "Наши отношения с Павлом Павловичем не таковы, чтобы я могла вмешиваться в воспитание Виктора."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Нет, отчего же. Сделайте одолжение. Я не имел в виду огорчить вас."

    hide okaemov

    show okaemov at left
    show nina at right

    okaemov "<{i}(Видя, что Нина подымается.){/i}>"

    hide nina

    show okaemov at truecenter

    okaemov "Хм. Я постараюсь... как могу."

    okaemov "<{i}(Разводя руками.){/i}>"

    okaemov "Я, разумеется, ничем не выкажу..."

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Благодарю вас. До свиданья."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Всех благ."

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show nina at right

    okaemov "<{i}Нина уходит.{/i}>"

    hide nina

    show okaemov at truecenter

    stop sound1

    okaemov "Ффу, Мотя!"

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show motja at right

    okaemov "<{i}Входит Мотя.{/i}>"

    hide motja

    show okaemov at truecenter

    stop sound1

    okaemov "Вот что, Мотя. Машу обидели в школе."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Кто обидел?"

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Не знаю. Вы, что ли, сходите за ней к Нине Александровне. Надо Машу развлечь как-нибудь. Приходите ко мне, что ли, и вообще... И подайте книгу, которую вчера купили по моей записке."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Зелененькую?"

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Да. Благодарю вас. Ступайте. И как будто вы ничего не знаете."

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Ах, они! Ах, они! Обидели! Ну, уж я им! Я дознаюсь, кто."

    play sound1 footsteps

    motja "<{i}(Выходит.){/i}>"

    stop sound1

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(смотря на книгу).{/i}>"

    okaemov "«Проблемы детской психологии». Хм."

    okaemov "<{i}(Ищет по оглавлению.){/i}>"

    okaemov "Страница восьмидесятая. «Переходный возраст...»"

    okaemov "<{i}(Читает.){/i}>"

    hide okaemov

    play sound1 footsteps

    show masha at left
    show leonid at truecenter
    show motja at right

    "<{i}В переднюю входят Маша, Леонид и Мотя.{/i}>"

    hide masha
    hide leonid
    hide motja

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Дед тебя посылал искать. В милицию заявлять собрался. Пропала. Растревожился — сам итти хотел. На костылях."

    motja "<{i}(В кабинет, громко.){/i}>"

    motja "Тут она. Умоется, к вам придет."

    play sound1 footsteps

    motja "<{i}(Уходит.){/i}>"

    stop sound1

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Машенька, мы друзья? Друзья. Так вот вам моя рука. Вы завтра придете в школу — и никто даже не вспомнит."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Нет-нет! Мне так стыдно!"

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Виктору будет стыдно, а не вам."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    play sound1 female_cry

    masha "<{i}(сквозь слезы).{/i}>"

    stop sound1

    masha "И ведь это совсем неправда. Я его не люблю. Я его пожалела, только чтобы он не грустил... а он..."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Ступайте к дедушке."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А вдруг он узнал?"

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Ступайте, как всегда шли. А я тут покараулю. Если вам будет трудно, вы стукните каблучком в пол, и я явлюсь."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(невольно улыбнулась).{/i}>"

    masha "Спасибо."

    play sound1 footsteps

    masha "<{i}(Уходит в кабинет.){/i}>"

    stop sound1

    hide masha

    show leonid at truecenter

    "<{i}Леонид садится на сундук и прислушивается.{/i}>"

    hide leonid

    "<{i}В кабинете{/i}>"

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Добрый вечер. Гуляли?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Мaша."

    masha "Да."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Озябли?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Нет. Вам подать чего-нибудь?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Подать. Хм... Нет, собственно, ничего... но, если вам не очень скучно, почитаем-ка нашего Диккенса. Хотите?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Хочу."

    masha "<{i}(Берет книгу.){/i}>"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(указывая на маленькую скамеечку у своих ног).{/i}>"

    okaemov "Вы сюда... сюда. Вам, Маша, тяжело со мной?"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша молчит.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Тяжело — это не то слово, скорее, неловко, холодно. Да-с, именно холодно. Холодный дом. Кажется, есть такой роман у Диккенса... Хм... Вам, вероятно, очень не хотелось уезжать от мамы?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(после молчания).{/i}>"

    masha "Я сама просила меня послать."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Сами? То есь как сами?.. Вы желали уехать ко мне?"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша кивает головой.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Почему?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Мамин муж... Маме трудно было со мной... Она все плакала, не знала, что со мной делать... Я и сказала ей, чтобы она послала меня... к вам... Она заплакала, а потом согласилась. И мамин муж тоже... Я и поехала..."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но позвольте... Вы же меня не знали совсем."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я знала. Папа про вас мне много рассказывал."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Так-c. И приехали."

    okaemov "<{i}Пауза.{/i}>"

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show leonid at right

    okaemov "<{i}Леонид тихонько выходит из передней.{/i}>"

    hide leonid

    show okaemov at truecenter

    stop sound1

    okaemov "Вас сегодня обидели, Машенька?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(испуганно).{/i}>"

    masha "Вы разве знаете?"

    hide masha

    show masha at left
    show okaemov at right

    masha "<{i}Окаемов кивает головой.{/i}>"

    hide okaemov

    show masha at truecenter

    masha "Не надо про это говорить, пожалуйста, мне очень стыдно."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Это пройдет, Маша. Все пройдет, я знаю. Вы только начинаете жить. Завтра это забудется."

    okaemov "<{i}(Пауза.){/i}>"

    okaemov "Папа рассказывал... Он что-нибудь не то рассказывал, Маша. Я скучный и нудный старик."

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша отрицательно качает головой.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Ну, уж мне лучше знать, какой я... Да-с... Скучный... Это оттого, что я долго живу один."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Разве вы тоже одинокий?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Да, девочка, все от меня ушли."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Куда?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Сначала ушли мои отец и мать. Потом жена. Потом сын мой — твой папа. Потом мои сверстники, один за другим. Значит, и мне пора. Настанет такой день, когда и я, наконец, уйду, и... пора."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(в страхе, шепотом).{/i}>"

    masha "Разве вы... не боитесь?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Это все равно наступит. Сегодня, завтра или через сто лет. Так уж лучше не бояться того, что все равно наступит. Я умру — будешь жить ты, твои дети, дети твоих детей. Чтобы ни происходило в мире, жизнь не может останавливаться."

    okaemov "Это надо хорошенько усвоить, и тогда перестанешь бояться неизбежного часа... А мне, например, иногда уже хочется уснуть — и не просыпаться."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Зачем вы... зачем?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "От жизни тоже иногда устаешь, девочка. Особенно, когда стар и живешь один."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А я?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ты? Хм. Разве я тебе нужен?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(горячо, шепотом).{/i}>"

    masha "Я думала, я не нужна вам... Я думала, я мешаю вам, зачем приехала, я все хотела назад поехать, чтобы вам не мешать, я видела — вы сердились, а все не знала, за что..."

    play sound1 footsteps
    play sound2 female_cry

    masha "<{i}(Не выдержала, заплакала, сквозь слезы пытается найти забытую страницу Диккенса.){/i}>"

    stop sound1
    stop sound2

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}(смотрит на ее склоненную голову, неумело гладит по волосам).{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Что ж. Будем жить, Маша. Будем жить. Вместе."

    hide okaemov

    "<{i}Занавес{/i}>"

label Act_2:
    play music "audio/music/1.mp3" fadeout 1.0 fadein 1.0

    scene 4 with fade

    "{b}Акт второй.{/b}"

    menu:
        "{color=#000}Сцена четвёртая{/color}":
            jump Act_2_Scene_1
        "{color=#000}Сцена пятая{/color}":
            jump Act_2_Scene_2

label Act_2_Scene_1:
    "{b}Сцена четвёртая{/b}"

    show okaemov at left
    show masha at right

    "<{i}Маленькая столовая в квартире Окаемова. Две двери: в его кабинет и в переднюю; дверь в кабинет закрыта. В столовой стоит кушетка, где спит Маша. У одной стены — рояль. У второй зеркало. Тут же полка с не поместившимися в кабинете книгами. Утро.{/i}>"

    hide okaemov
    hide masha

    show nina at left
    show masha at right

    "<{i}В столовой у рояля Нина и Маша. Маша тянет гаммы и сбивается.{/i}>"

    hide nina
    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Тебе не терпится поскорее запеть. Но искусство — прежде всего труд, Маша. Упорный, ежедневный труд. Тяни свое ля и не думай пока о песенках и романсах... и вдобавок ты сегодня какая-то вялая, Маша, рассеянная."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я?"

    masha "<{i}(Смущается.){/i}>"

    masha "Нина Александровна, милая. Я хочу заработать деньги. Много денег. Я умею ноты переписывать, принесите мне побольше нот переписывать, я вечером буду, после уроков..."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Зачем тебе деньги?"

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(торопливо).{/i}>"

    masha "Дедушка свои книги продал из-за меня. Он книги так любит, так любит, а взял и продал и мне шубу купил... и коньки... А я решила — заработаю деньги и куплю ему книги обратно."

    masha "Я уже в той лавке была, где книги, сказала, что буду понемногу платить, чтобы они никому не продавали. Они сначала не соглашались, а потом я им сказала, по секрету, зачем, и они согласились. Я все заплачу — возьму книги и отдам дедушке."

    masha "И скажу, чтобы больше он своих книг не продавал, потому что я поступлю в оперу, буду много петь и все деньги ему приносить..."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    hide nina

    show nina at left
    show masha at right

    nina "<{i}(смотрит на Машу, притягивает ее к себе).{/i}>"

    hide masha

    show nina at truecenter

    nina "Машенька, я помогу тебе купить книги. Я достану тебе работу, но ты больше никогда ни мне, ни дедушке не говори, что скоро поступишь в оперу за деньги. Ты только лишь начинаешь учиться."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    hide masha

    show masha at left
    show nina at right

    masha "<{i}(обнимает ее).{/i}>"

    hide nina

    show masha at truecenter

    masha "Не скажу, Нина Александровна, никогда не скажу. Мне только хотелось дедушке поскорей помочь — пусть он покупает самые дорогие книги. Я даже и не знала, что дедушка меня так любит. Совсем не знала. Мне так нравится жить, когда меня любят."

    masha "Всем, наверное, нравится, правда?"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Правда."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ах, Нина Александровна, как я вас люблю! Больше всех, после дедушки. И Леонида Борисовича я тоже очень люблю. А вы?"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Он почему-то избегает меня."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Он говорит, что вам некогда. И не хочет поэтому вам мешать. Если бы вы знали его, как я, вы бы его так полюбили... так полюбили... как я."

    masha "<{i}(Шепотом.){/i}>"

    masha "Мы в кафе сидели. Пили кофе и музыку слушали. И про вас рассуждали..."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(заинтересованно).{/i}>"

    nina "И до чего дорассуждались?"

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Он сказал: «Чудесная женщина». А я сказала: «Правильно». А он сказал: «Это я ведь вас познакомил...» А я сказала: «Правильно». Ведь верно, Нина Александровна, без него мы даже и не повстречались бы. Я бы даже не знала, что мне хочется учиться пению."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "И что он еще сказал?"

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Мы с ним Третьяковскую галлерею смотрели, потом в цирк пошли. Он сказал, что, не будь он геологом, он бы хотел поступить клоуном. Ему нравится, когда кругом смеются, он сам тогда веселый делается."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "У него хороший смех."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А вы приходите к нам как-нибудь вечером. Мы иногда в подкидного дурака играем. Дедушка, я, Леонид Борисович и Мотя."

    masha "Ох, и смеется он, когда дедушка в дураках! Мне раз жалко дедушку стало — все они с Мотей оставались, я дедушке нарочно туза подмешала в карты... а Леонид Борисович увидел. У-у, что было!"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "A вот со мной побыть у него времени не находится..."

    hide nina

    play sound1 telephone

    "<{i}Звонок в передней.{/i}>"

    stop sound1

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А вдруг это он? Хорошо бы."

    hide masha

    play sound1 footsteps

    show tumanskij at truecenter

    "<{i}Входит Туманский.{/i}>"

    hide tumanskij

    stop sound1

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Я сдержал свое обещание, Нина Александровна. Виктор через пять минут явится просить у Маши прощения. Как видите, сын мой не настолько испорчен."

    play sound1 footsteps

    tumanskij "<{i}(Подходя ближе, вполголоса.){/i}>"

    stop sound1

    tumanskij "Вы получили мое письмо?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(вполголоса).{/i}>"

    nina "Целых три."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Я говорю о последнем."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Зачем вы мне его послали?"

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Поедемте со мной. Здесь не место для объяснений. Я не привык объясняться вполголоса..."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "А вообще-то вы объясняться, значит, привыкли?"

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Не ловите на слове. Поедемте. Я сумею вас убедить."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Меня не нужно убеждать ни в чем, Павел Павлович, и мне некуда ехать."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Тогда к вам хотя бы..."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Маша, спустись ко мне, перепиши страницу нот на пробу и принеси."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Сейчас."

    hide masha

    show masha at left
    show nina at right

    masha "<{i}(Тихо, ей.){/i}>"

    hide nina

    show masha at truecenter

    masha "А с Виктором мне обязательно надо?"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Если ты сама захочешь."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я подумаю."

    play sound1 footsteps

    masha "<{i}(Уходит.){/i}>"

    stop sound1

    hide masha

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Нина..."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "...Александровна, с вашего позволения."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вы избегаете меня. Вы не отвечаете на письма. Неужели эта глупейшая история с Виктором тому причиной? Ради бога, не делайте меня ответственным за поведение моего сына. Он сам по себе, а я сам..."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Это не так, Павел Павлович... Но дело совсем не в Вите."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "А в чем тогда?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(усмехнулась).{/i}>"

    nina "В несходстве наших характеров."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Откуда вы это вывели?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Как это ни странно, прежде всего из ваших писем."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Это действительно странно. Что же вам не нравится в моих письмах?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Их ложный пафос, Павел Павлович."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вы не верите в искренность моих слов?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Не верю."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Но почему, почему?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Потому что мне уже тридцать лет и я понимаю разницу между любовью и мелодраматическим флиртом."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вы намерены оскорбить меня?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я хочу лишь сказать вам правду."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "В чем ваша правда?"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "В том, что вы не в состоянии глубоко любить, Павел Павлович."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    tumanskij "<{i}(запальчиво).{/i}>"

    tumanskij "Неправда! Я люблю вас! Люблю впервые так глубоко и сильно."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Это вам только кажется... Жизнь, которую вы вели, измельчила вас. Вы уже перешли грань молодости: прежние ваши минутные привязанности перестали радовать Вас. Вам захотелось настоящей любви. Ho привычка к легким победам оказалась сильнее новых желаний."

    nina "Я просто нравлюсь вам, как нравились до меня... и вместе со мной другие женщины."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "А-а! Вот оно! Вам наговорили обо мне!"

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Так это правда? Видите, а я ведь ничего не знала, я только догадывалась."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Но я же прошу вас стать моей женой."

    hide tumanskij

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Женой? Неужели вы думаете, я не понимаю, что первая же трудность совместной жизни, первое ваше новое увлечение — и все ваши фразы о любви разлезутся на клочки?.. Вы осуждаете Виктора, сердитесь на него, но ведь Виктор просто подражает вам..."

    nina "вашему легкомысленному отношению к жизни. Да, в других областях вы достигли положения, известности, знаний... а в вашей личной жизни, в вашем отношении к женщинам есть что-то оскорбительное."

    nina "<{i}Молчание.{/i}>"

    nina "Простите за резкость, но я не могу говорить безразлично о вещах, которые для меня так важны."

    play sound1 telephone

    nina "<{i}Звонок в передней.{/i}>"

    stop sound1

    nina "Вероятно, ваш сын. Я пришлю сюда Машу."

    hide nina

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "И все-таки я люблю вас по-настоящему."

    hide tumanskij

    play sound1 footsteps

    show nina at left
    show viktor at right

    "<{i}Нина уходит. Входит Виктор.{/i}>"

    hide nina
    hide viktor

    stop sound1

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Старик, опять звонила Ирина Сергеевна. Просила передать, что она ждет твоего звонка."

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Хорошо. А? Ирина Сергеевна?"

    tumanskij "<{i}(Резко.){/i}>"

    tumanskij "Не лезь не в свое дело!"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Подумаешь! То сам просил, а то — не лезь."

    viktor "<{i}(Вынимает папиросы, хочет закуригь.){/i}>"

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Брось папиросу!"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "С каких это пор, старик?"

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Брось немедленно! Ну!"

    hide tumanskij

    show tumanskij at left
    show viktor at right

    tumanskij "<{i}Виктор бросает.{/i}>"

    hide viktor

    show tumanskij at truecenter

    tumanskij "Сын. Сын. Будто впервые увидел. Эти жесты, манеры, даже тон голоса!.. Или и вправду ты только подражаешь отцу?"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Такова жизнь, и не нам ее осуждать."

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Замолчи!"

    hide tumanskij

    show tumanskij at left
    show viktor at right

    tumanskij "<{i}Виктор испуганно умолкает.{/i}>"

    hide viktor

    show tumanskij at truecenter

    tumanskij "<{i}(С трудом сдерживая себя, медленно.){/i}>"

    tumanskij "Неужели это я? В самом деле... я... сделал тебя таким?"

    hide tumanskij

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Каким?"

    hide viktor

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    tumanskij "<{i}(махнув рукой).{/i}>"

    tumanskij "А!"

    play sound1 footsteps

    tumanskij "<{i}(Уходит.){/i}>"

    stop sound1

    hide tumanskij

    play sound1 footsteps

    show viktor at left
    show tumanskij at truecenter
    show masha at right

    "<{i}Виктор один. Потом входит Маша. Пауза.{/i}>"

    hide viktor
    hide tumanskij
    hide masha

    stop sound1

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор"

    viktor "<{i}(мрачно).{/i}>"

    viktor "Здорово... Лелька Спирина от имени всех девчонок заявила, что со мной никто танцевать не будет на вечеринке, если я не извинюсь. Раздули из мухи слона и радуются. Ты сама во всем виновата, зачем тогда убежала. Ну, обиделась на меня — и молчи."

    viktor "Подумаешь, Мария Стюарт, — посмеяться нельзя. Я не знал, что ты мямля, разревелась, как мамина дочка с косичками, и скандал. Как будто до революции в институте воспитывалась..."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "И пусть! И пусть!"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Тебе «пусть», а мне отец заявил, что ни копейки денег не даст, пока не помиримся. Ботинок почистить не на что. А все оттого, что в Нинку твою влюбился и перед ней выслуживается."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Не смей так говорить!"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "А что, неправда? Они скоро поженятся."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Кто тебе сказал?"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Сам вижу."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А может быть, Нина Александровна не захочет..."

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор"

    play sound1 whistle

    viktor "<{i}(свистнул).{/i}>"

    stop sound1

    viktor "Еще не было такого случая, чтобы женщина замуж не захотела."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Зачем ты так разговариваешь?"

    hide masha

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Это не я, это папаша мой говорит."

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А ты все время повторяешь чужие слова. Как будто актер на сцене."

    masha "Тебе трудно самим собой быть, все кого-то изображаешь, кривляешься, как перед зеркалом, лишь бы на тебя внимание обратили, какой ты умный! А разве ты умный? Мое письмо вслух прочел? Похвастаться."

    masha "Нашел, чем хвалиться! Что я тебя пожалела, думала, ты, как я, одинокий, без мамы. Разве я тебе про любовь писала? Это ты сам приврал, чтобы смешнее было. Я с тобой хотела дружить, а тебе друзей, оказывается, не надо. Ну и уходи! И незачем нам мириться."

    masha "А если ты ботинок сам не умеешь вычистить, то вот..."

    masha "<{i}(Торопливо вынимает из тетради рубль.){/i}>"

    masha "Возьми и поди почисть..."

    hide masha

    "<{i}Пауза.{/i}>"

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор"

    viktor "<{i}(хмуро).{/i}>"

    viktor "Я соврал про ботинки... И вообще ты чертовски меня поддела. Что здорово, то здорово. Я даже, кажется, покраснел."

    hide viktor

    show viktor at left
    show masha at right

    viktor "<{i}(Протягивает ей руку.){/i}>"

    hide masha

    show viktor at truecenter

    viktor "Прости меня, Маша. Я, честное слово, осел и хам. Заявляю вслух и могу при всех. Осел и хам."

    play sound1 telephone

    viktor "<{i}В передней звонок.{/i}>"

    stop sound1

    viktor "Честное слово, при всех скажу. Ну, Маша! Хоть руку дай!"

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    hide masha

    show masha at left
    show viktor at right

    masha "<{i}(протягивает ему руку).{/i}>"

    hide viktor

    show masha at truecenter

    masha "Ах, Витя, ты еще совсем мальчик!"

    hide masha

    play sound1 footsteps

    show lelja at left
    show galja at truecenter
    show senja at right

    "<{i}В столовую входят Леля, Галя и Сеня. Леля — красивая, умная девушка; Галя — веселая толстушка; Сеня — чересчур умный мальчик в очках.{/i}>"

    hide lelja
    hide galja
    hide senja

    stop sound1

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля"

    lelja "<{i}(приветливо).{/i}>"

    lelja "Я говорила, что он придет."

    hide lelja

    show lelja at left
    show senja at right

    lelja "<{i}(Сене.){/i}>"

    hide senja

    show lelja at truecenter

    lelja "Кто был прав?"

    hide lelja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Еще неизвестна цель его прихода."

    hide senja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Пришел извиняться."

    hide lelja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Сомневаюсь."

    hide senja

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Подумаешь, какой Сократ! Сомневается!"

    hide viktor

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Подумаешь, какой Печорин! Обижается!"

    hide senja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "А вы еще подеритесь."

    hide galja

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Заявляю при всех, что я осел и хам, осел и хам, осел и хам!"

    hide viktor

    show viktor at left
    show masha at right

    viktor "<{i}(Маше.){/i}>"

    hide masha

    show viktor at truecenter

    viktor "Убедилась? Пока."

    play sound1 footsteps

    viktor "<{i}(Выходит.){/i}>"

    stop sound1

    hide viktor

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Что он этим хотел сказать?"

    hide senja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Что он «селыхам». Ха-ха-ха! «Селыхам!»"

    hide galja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Галина, остановись!"

    hide lelja

    show lelja at left
    show masha at right

    lelja "<{i}(Маше.){/i}>"

    hide masha

    show lelja at truecenter

    lelja "Он извинялся?"

    hide lelja

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Да."

    hide masha

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля"

    hide lelja

    show lelja at left
    show senja at right

    lelja "<{i}(Сене).{/i}>"

    hide senja

    show lelja at truecenter

    lelja "Видишь? Обошлись без резолюций и заседаний."

    hide lelja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Назвать себя хамом еще не значит извиниться."

    hide senja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Ах, Сеня, ты всегда придираешься, так придираешься, без конца."

    hide galja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Ребенок, не лезь в разговоры взрослых."

    hide senja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Ну, будет! Маша, зови Василия Ивановича."

    hide lelja

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Дедушка работает. Он не любит, когда мешают."

    hide masha

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Ты скажи официально, что пришла октябрьская комиссия. На пять минут. И все."

    hide senja

    play sound1 footsteps
    play sound2 knocking
    play sound3 tiptoes

    show masha at truecenter

    "<{i}Маша идет на цыпочках к двеpи кабинета. Стучит. Входит в кабинет.{/i}>"

    hide masha

    stop sound1
    stop sound2
    stop sound3

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Чур, я не говорю! Пусть Сенька."

    hide galja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Леля начнет, а я резюмирую."

    hide senja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Ты с ним о науке поговори, он — профессор, и ты — профессор. Вы друг друга с полуслова поймете."

    hide lelja

    show lelja at left
    show galja at right

    lelja "<{i}Галя засмеялась.{/i}>"

    hide galja

    show lelja at truecenter

    lelja "Галина, остановись!"

    hide lelja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "А зачем ты смешишь? Ты знаешь — я смешливая."

    play sound1 female_gag

    galja "<{i}(Зажимает рот и прыскает.){/i}>"

    stop sound1

    galja "Ну вот, теперь я за себя не ручаюсь."

    hide galja

    play sound1 footsteps

    show okaemov at left
    show masha at right

    "<{i}Входит Окаемов. За ним Маша. Окаемов еще хромает и опирается на палку.{/i}>"

    hide okaemov
    hide masha

    stop sound1

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Здравствуйте, молодые друзья!"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    hide masha

    show masha at left
    show okaemov at right

    masha "<{i}(называет тех, с кем он здоровается).{/i}>"

    hide okaemov

    show masha at truecenter

    masha "Леля, Галя, Сеня."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Прошу садиться. Чем могу быть полезен?"

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Василий Иванович, шестого ноября мы устраиваем школьный вечер в честь Октябрьской революции. И мы от имени школы просим вас выступить."

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(поражен).{/i}>"

    okaemov "Ме-ня? Выступить? С чем?"

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Во-первых, с небольшим обзором вашего жизненного пути."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но, позвольте, почему меня?"

    hide okaemov

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Как самого старшего из родителей."

    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Не-ет, друзья, я не могу. Я никогда не выступал перед детской аудиторией. Я не знаю, о чем говорить. Я, наконец, не умею говорить на митингах."

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Во-вторых, я могу составить вам конспект выступления."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Нет, я не умею излагать чужие конспекты. He-ет."

    hide okaemov

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Ничего, ничего, вы расскажите, как умеете, мы поймем."

    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но о чем, о чем? Не о том же, что знак плюс появился в тринадцатом веке."

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "А когда появилась запятая?"

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(серьезно).{/i}>"

    okaemov "Видите ли, к нам запятая перешла с пятнадцатого века, и она не отличалась сперва в своем употреблении от точки."

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Правильно."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Я полагаю, что правильно. Ибо я это, некоторым образом, первый установил."

    hide okaemov

    play sound1 female_sigh

    "<{i}Общий вздох восхищения.{/i}>"

    stop sound1

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Первый!.."

    hide senja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "А что такое крестный ход, вы знаете? Я думала, что это машина скорой помощи, которая с красным крестом всегда... а потом Сенька сказал, что это глупости, а сам не знает."

    hide galja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Попросил бы воздержаться от инсинуаций. Крестный ход — это средство одурманивания широких масс ядом религии при помощи сказок о боге и ангелах."

    hide senja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Это я и сама знаю, что ангелов нет. У них есть крылья, они живут на небе, но их нет."

    hide galja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Галина, остановись!"

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Нет, нет, весьма любопытно. Так сказать, отживающие понятия... Хм..."

    hide okaemov

    show okaemov at left
    show galja at right

    okaemov "<{i}(Гале.){/i}>"

    hide galja

    show okaemov at truecenter

    okaemov "Вы знаете, например, кто такой был «надворный советник»?"

    hide okaemov

    show galja at truecenter

    $ galja_var = "{noalt}Галя"

    galja "<{i}(несмело).{/i}>"

    galja "По-моему, они по дворам ходили и советовали."

    hide galja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Неверно. Надворный советник — это представитель эксплуататорских классов. Муж Анны Карениной был надворный советник."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Каренин был, скорее, действительным тайным советником."

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Ну да, и тайным, потому что все делал втайне от широких масс."

    hide senja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Ты мелешь глупости, хоть и профессор!"

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Вот как? Уже профессор?"

    hide okaemov

    play sound1 female_gag

    show galja at truecenter

    "<{i}Галя прыснула и зажала рот.{/i}>"

    hide galja

    stop sound1

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Мы его так зовем, потому что он ужасно много знает. Про все. Он за год прочел двести восемьдесят книг. А в нынешнем году дал обязательство прочесть триста."

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. По мне — одна усвоенная книга полезнее сотни просто прочитанных."

    hide okaemov

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Ага! Ага! Попался!"

    play sound1 female_laughter

    galja "<{i}(Заливается смехом.){/i}>"

    stop sound1

    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хотя в детстве я сам пожег немало свечей на книги."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ты был бедный, дедушка, да? У тебя не было денег на керосин?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Нет-с. Просто тогда еще и керосина не было."

    hide okaemov

    show lelja at left
    show senja at truecenter
    show galja at right

    $ lelja_var = "{noalt}Все."

    lelja "Керосина? А что ж было?"

    hide lelja
    hide senja
    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Сальные свечи и масло. Керосин появился позднее. Потом стали жечь газ. А уж недавно, лет сорок пять назад, зажглось первое электрическое освещение."

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "И вы видели первую лампочку?"

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Видел."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А еще что ты видел первое?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. При мне, например, появился первый автомобиль. Он гремел на всю улицу, а потом прохожие начали бить шофера и орали: «Бензиновый черт, бензиновый черт!»"

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Хм. Сомневаюсь."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Тем не менее это так. Я уже был бородатым, когда изобрели кинематограф. Я видел, как поднялся в воздух первый аэроплан. Он едва пролетел над забором и шлепнулся в траву, поломав крылья... А мне все казалось, что я сплю и вижу чудо."

    hide okaemov

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Ой, как интересно!"

    hide galja

    show okaemov at truecenter

    "<{i}Они сгрудились около Окаемова, не сводя с него глаз.{/i}>"

    hide okaemov

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "А когда первый раз я надел наушники и услышал голос из эфира, я возблагодарил судьбу, что дожил до такого дня... Вот сколько вещей появилось в течение одной моей жизни. Сколько же дано увидеть вам, чья жизнь едва начинается!"

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Вот обо всем этом вы и расскажите на школьном вечере, Василий Иванович."

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но кому это интересно?"

    hide okaemov

    show lelja at left
    show senja at truecenter
    show galja at right

    $ lelja_var = "{noalt}Все дети."

    lelja "Всем, всем! Пожалуйста, расскажите!"

    hide lelja
    hide senja
    hide galja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "А что мы, по-вашему, еще увидим в жизни?"

    hide lelja

    show masha at left
    show galja at truecenter
    show senja at right

    $ masha_var = "{noalt}Все."

    masha "Да, что, что?"

    hide masha
    hide galja
    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Что?.. Хм..."

    okaemov "<{i}(Задумался.){/i}>"

    okaemov "Вы увидите, как кусочек угля с мой кулак будет отапливать громадный дом... Вы увидите, как жизнь человеческая будет продлена на много лет... Вы услышите, как прозвучит на земле последний выстрел, и люди забудут, что такое война."

    okaemov "Вы будете жить в новом мире, без войн... Все это вы увидите и переживете..."

    hide okaemov

    "<{i}Тишина.{/i}>"

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Как интересно жить, дедушка!"

    hide masha

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "И это будет называться коммунизм."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(серьезно).{/i}>"

    okaemov "Совершенно с вами согласен, коллега профессор."

    hide okaemov

    "<{i}Занавес{/i}>"

label Act_2_Scene_2:
    "{b}Сцена пятая{/b}"

    "<{i}Та же столовая, убранная к Новому году. Обе двери раскрыты, соединяя квартиру в одно. Стол накрыт и раздвинут. На стене против стола висит большой лист картона с надписью, как в календаре: «31 декабря».{/i}>"

    play sound1 piano
    play sound2 telephone

    show leonid at left
    show okaemov at right

    "<{i}На крышке пианино стоит радиоприемник, передает страшно громкий марш. Леонид хлопочет около стола, дирижируя свободной рукой. В кабинете Окаемов что-то быстро пишет, не обращая внимания на марш. Звонок в передней.{/i}>"

    hide leonid
    hide okaemov

    stop sound1
    stop sound2

    show leonid at truecenter

    "<{i}Леонид кидается туда, вносит в столовую упакованную корзину, ставит ее на стол. Развязывает.{/i}>"

    hide leonid

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Маша! Машенька!"

    hide leonid

    play sound1 footsteps

    show leonid at truecenter

    "<{i}Из-за радио его не слышно. Он подходит к приемнику, выключaет.{/i}>"

    hide leonid

    stop sound1

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(поднял голову от стола).{/i}>"

    okaemov "Что случилось? Почему так тихо?"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Шампанское принесли, Машенька!"

    hide leonid

    show masha at truecenter

    "<{i}Из кухни появляется Маша, в переднике, с засученными рукавами.{/i}>"

    hide masha

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Куда это все? Куда? И так еды на сто гостей."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Все съедим, Машенька! Все выпьем. За каждого гостя — тост. Необыкновенной силы я сочинил тосты!"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я тоже хочу сегодня что-нибудь сказать. Что-нибудь ужасно радостное. Чтобы всем было весело, Kaк мне."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "А вам уже весело?"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Еще вчера стало весело."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "И сегодня скажете мне причину?"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(смутившись).{/i}>"

    masha "Вам? Нет... да... почему?"

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Потому что я тоже скажу вам одну вещь!"

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Вы?"

    masha "<{i}(Страшно смутившись.){/i}>"

    masha "Нет... Вы..."

    masha "<{i}(Села от растерянности.){/i}>"

    hide masha

    play sound1 footsteps

    show motja at truecenter

    "<{i}Входит Мотя, неся новое блюдо.{/i}>"

    hide motja

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Не рассаживайся, мать моя, гости на носу. Поди соус к рыбе отбей."

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Она устала, Мотя."

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Поди, поди, хозяйка последняя устает."

    hide motja

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(встает).{/i}>"

    masha "Все как будто во сне."

    hide masha

    show masha at left
    show leonid at right

    masha "<{i}(Леониду.){/i}>"

    hide leonid

    show masha at truecenter

    masha "Вы тоже скажете?.. Тоже?"

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Непременно, Машенька."

    hide leonid

    play sound1 footsteps

    show masha at truecenter

    "<{i}Маша быстро уходит.{/i}>"

    hide masha

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Устанешь тут, когда цельные дни ноты пишет — не разогнется. А начну выговаривать — «пожалуйста, не мешай»."

    play sound1 footsteps

    motja "<{i}(Уходит в кухню.){/i}>"

    stop sound1

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Василий Иванович, это чудовищно! Оказывается, Маша все еще переписывает эти ноты! Зачем вы позволяете?"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Секундочку! Коллекция отживших понятий растет."

    okaemov "<{i}(Перечитывает вслух.){/i}>"

    okaemov "Оказывается: «Мощи — сушеный поп. Нечистый дух — это когда в комнате много курят. Горничная — это комната. Лакей — подхалим. Записано на беседе в школе». Хм!"

    hide okaemov

    show okaemov at left
    show leonid at right

    okaemov "<{i}(Леониду.){/i}>"

    hide leonid

    show okaemov at truecenter

    okaemov "Что же касается нот, то Нина Александровна заявила, что переписка носит срочный характер и Маше не надо мешать."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "О, если Нина Александровна, — умолкаю."

    play sound1 footsteps

    hide leonid

    show leonid at left
    show okaemov at right

    leonid "<{i}(Видит, что Окаемов, вошедший в столовую, хочет приподнять лист с числом.){/i}>"

    hide okaemov

    show leonid at truecenter

    stop sound1

    leonid "Нельзя, нельзя! В полночь сорвем — увидите."

    hide leonid

    show leonid at left
    show okaemov at right

    leonid "<{i}(Берет Окаемова за талию.){/i}>"

    hide okaemov

    show leonid at truecenter

    leonid "А помните наш прошлый Новый год?"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Да-с. Я сидел за стаканом чая, а вы позвонили с опозданием на полчаса и, как всегда, перепутали. Вместо нового года пожелали спокойной ночи."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Ну, уж сегодня я не перепутаю. Это все Машенька, Василий Иванович!"

    leonid "<{i}(Широким жестом обводит стол.){/i}>"

    leonid "Ее вторжение. Я и то помолодел духом, а вы совершенно юношей стали. После вашего дебюта шестого ноября вы уже выступали в Доме пионеров, потом на каком-то слете, и все с таким же успехом."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Да-с. С гораздо большим, признаться, чем мои лекции по палеографии. Вторая профессия — рассказчик о темном прошлом."

    okaemov "<{i}(Усмехается.){/i}>"

    okaemov "И ведь отказать нельзя — просят очень."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Размечтались, а шампанское не во льду!"

    play sound1 footsteps

    leonid "<{i}(Берет бутылки, уходит.){/i}>"

    stop sound1

    hide leonid

    play sound1 footsteps

    show okaemov at left
    show leonid at right

    "<{i}Окаемов хочет все же приподнять картон, но Леонид возвращается.{/i}>"

    hide okaemov
    hide leonid

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Ай-ай-ай, Василий Иванович! Ай-ай-ай!"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(смущенно).{/i}>"

    okaemov "Да я, право..."

    hide okaemov

    play sound1 footsteps
    play sound2 telephone

    show leonid at left
    show masha at truecenter
    show nina at right

    "<{i}Звонок в передней. Леонид выходит. Входят Нина и Маша. В руках у Нины сверток.{/i}>"

    hide leonid
    hide masha
    hide nina

    stop sound1
    stop sound2

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Извольте к елочке, к елочке."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Милый Василий Иванович! У нас с Машей новогодний секрет. Покиньте, пожалуйста, столовую."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм, в собственной квартире швыряются тобой, как пешкой, из угла в угол."

    play sound1 footsteps

    okaemov "<{i}(Посмеиваясь, уходит в кабинет.){/i}>"

    stop sound1

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(берет сверток).{/i}>"

    nina "Машенька, здесь дедушкины книги."

    hide nina

    show nina at left
    show masha at right

    nina "<{i}(Видя изумление Маши.){/i}>"

    hide masha

    show nina at truecenter

    nina "Ты уже заработала двести рублей. Я одолжила тебе остальную сумму и взяла книги. Подари их Василию Ивановичу на Новый год."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(берет книги, растерянно).{/i}>"

    masha "Вы свои деньги дали?"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Ты отдашь их мне. Потом, постепенно. Не все ли равно?"

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    hide masha

    show masha at left
    show nina at right

    masha "<{i}(бурно обнимая Нину).{/i}>"

    hide nina

    show masha at truecenter

    masha "Ниночка! Я тебе очень скоро отдам. Я быстро работаю! Дедушка!"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Тcc... Положи книги под салфетку."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    play sound1 running

    masha "<{i}(бежит к столу, прячет книги).{/i}>"

    stop sound1

    masha "Ой, Нина Александровна, милая! Я даже вас на «ты» назвала от радости..."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "А ты зови."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Можно? Спасибо вам... то есть тебе."

    play sound1 female_laughter

    masha "<{i}(Смеется.){/i}>"

    stop sound1

    masha "Весь день смеюсь. Вроде Гали. Ох, дедушка удивится! Какая вы... ты добрая, Нина... Отчего ты такая добрая? Знаешь, я тебе скажу по секрету, теперь можно... Когда Витька сказал, что вы с Павлом Павловичем поженитесь, я тебе письмо написала. Длинное."

    masha "<{i}(Тихо.){/i}>"

    masha "Чтобы вы не выходили за него замуж, потому что..."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я понимаю, девочка."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А когда узнала, что вы даже совсем не собираетесь, ох, я обрадовалась!"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Ты, значит, от этого такая веселая?"

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "И от этого, и еще от одной вещи. Только это ужасная тайна, Нина. Я даже дневник себе завела — туда ее записать. И никому не могу сказать."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Конечно, если это тайна, не говори."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Но тебе я скажу ее. Я решила. Закрой глаза."

    hide masha

    show masha at left
    show nina at right

    masha "<{i}Нина закрывает глаза.{/i}>"

    hide nina

    show masha at truecenter

    hide masha

    show masha at left
    show nina at right

    masha "<{i}(Обняв ее за шею, шепчет.){/i}>"

    hide nina

    show masha at truecenter

    masha "Скажи, если очень любишь, можно ждать три года?"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Чего ждать?"

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Нет-нет, не смотри на меня, пожалуйста. Ну, ждать вообще. Чтобы дожидаться, кого любишь."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Конечно, можно, девочка."

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(еле слышно).{/i}>"

    masha "Я... я скажу сегодня, чтобы он подождал три года. Только три года. Пока мне исполнится восемнадцать лет."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Кто «он»?"

    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Ты знаешь."

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(открыв глаза).{/i}>"

    nina "Леонид Борисович?"

    hide nina

    show masha at left
    show nina at right

    "<{i}Маша молча кивает головой, не решаясь взглянуть на Нину. Нина поднимает ее лицо, смотрит пристально.{/i}>"

    hide masha
    hide nina

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(быстрым шепотом).{/i}>"

    masha "Он хочет мне сегодня одну вещь сказать... Тоже про «это», наверное. Мне ужасно страшно. И сердце колотится, ты послушай."

    hide masha

    show masha at left
    show nina at right

    masha "<{i}(Прикладывает руку Нины к своему сердцу.){/i}>"

    hide nina

    show masha at truecenter

    masha "Но все равно, я решила."

    hide masha

    show masha at left
    show nina at right

    masha "<{i}(Смотрит на Нину.){/i}>"

    hide nina

    show masha at truecenter

    masha "Что с тобой?"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Голова немного болит. Пройдет."

    hide nina

    play sound1 footsteps

    show leonid at truecenter

    "<{i}Входит Леонид.{/i}>"

    hide leonid

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "А я знаю, знаю, о чем вы шепчетесь!"

    play sound1 footsteps

    hide leonid

    show leonid at left
    show masha at right

    leonid "<{i}Маша быстро убегает в кабинет.{/i}>"

    hide masha

    show leonid at truecenter

    stop sound1

    leonid "<{i}(Вслед.){/i}>"

    leonid "Шучу, шучу, Машенька. Представления не имею. Здравствуйте, Нина Александровна! Ох, какое на вас платье, необыкновенной силы!"

    play sound1 footsteps

    leonid "<{i}(Идет к кабинету.){/i}>"

    stop sound1

    leonid "Машенька, не смущайтесь, я каждый раз попадаю впросак со своими шутками."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    hide nina

    show nina at left
    show leonid at right

    nina "<{i}(останавливая его).{/i}>"

    hide leonid

    show nina at truecenter

    nina "Особенно потому, что речь шла о вас."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "«Меж юных жен, увенчанных цветами, шел разговор веселый обо мне»."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Леонид Борисович, Маша вас любит."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Надеюсь."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я говорю о большой любви. Настоящей."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Что?"

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Маша призналась мне. Она хочет просить вас подождать три года. До ее совершеннолетия."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Подождать три года? Нет, вы серьезно?"

    hide leonid

    show leonid at left
    show nina at right

    leonid "<{i}(Поймав ее взгляд.){/i}>"

    hide nina

    show leonid at truecenter

    leonid "Так. Понимаю."

    leonid "<{i}(Весело.){/i}>"

    leonid "Я с восторгом подожду и пять лет..."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Нет, Леонид Борисович, нельзя смеяться над первой любовью девочки. Для Маши сейчас весь мир счастлив и радостен, как она сама. Она верит только своему сердцу. И в этом сердечке — вы."

    nina "Для нее сейчас не существует ни сомнений, ни вопросов, она также уверена в вашем чувстве, как и в своем. И с этим играть нельзя."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Да-да. Понимаю. Благодарю вас... за Машу. За ваше отношение к ней."

    leonid "<{i}(Пауза.){/i}>"

    leonid "Я, кажется, растерялся. Как мне ей объяснить? Может быть, вы... укажете ей на разницу лет, характеров..."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я?"

    nina "<{i}(Растерянно.){/i}>"

    nina "Нет... я не могу."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Именно вам она поверит больше всего."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Я не могу."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Хорошо, попробую сам. Вот что. Я скажу ей, конечно осторожно, подготовив, что я, к сожалению, уже люблю другую женщину. Вас! Тем более, что я действительно в вас влюблен."

    hide leonid

    show masha at truecenter

    "<{i}В дверях кабинета тихо появляется Маша. Незамеченная, она Слушает.{/i}>"

    hide masha

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Вы?"

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Я влюбился в вас с первой встречи, помните, в поезде. Я даже хотел объясниться, но вовремя удержался. Я и сейчас еще вас люблю — вы простите меня и не обращайте внимания, это скоро пройдет."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    nina "<{i}(тихо).{/i}>"

    nina "Если это пройдет, я вам никогда не прощу."

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(после паузы).{/i}>"

    leonid "Что-о-о?"

    hide leonid

    show leonid at left
    show nina at right

    leonid "<{i}(Схватив ее за руку.){/i}>"

    hide nina

    show leonid at truecenter

    leonid "Извольте объяснить ваши слова..."

    hide leonid

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Нужно ли?"

    hide nina

    show nina at left
    show leonid at right

    nina "<{i}(Смотрит на него.){/i}>"

    hide leonid

    show nina at truecenter

    hide nina

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    hide leonid

    show leonid at left
    show nina at right

    leonid "<{i}(почти кричит, схватив ее за руку).{/i}>"

    hide nina

    show leonid at truecenter

    leonid "Вы отдаете себе отчет в том, что вы сейчас натворили?"

    hide leonid

    play sound1 footsteps
    play sound2 female_laughter
    play sound3 kiss
    play sound4 telephone

    show nina at left
    show leonid at truecenter
    show okaemov at right

    "<{i}В передней громкий звонок. Маша тихо скрывается в кабинете. Нина обнимает и целует Леонида. Быстро проходит в переднюю, где слышен шум голосов, смех. В столовую входит Окаемов.{/i}>"

    hide masha
    hide nina
    hide leonid
    hide okaemov

    stop sound1
    stop sound2
    stop sound3
    stop sound4

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Молодое поколение прибыло."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "А?"

    leonid "<{i}(Схватив ето за руку.){/i}>"

    leonid "Дорогой старик! Я даже сперва не понял, что, собственно, произошло. Как будто в меня угодил метеорит... Я ощутил вдруг невыносимый подъем всех чувств... что-то такое требовательное, чему бесполезно сопротивляться... И я не сопротивляюсь."

    leonid "Я просто еще не совсем верю... но она же сама сказала — вот тут, где стоите вы, и я держал ее за руку, как вас. Это было! Было!"

    hide leonid

    show leonid at left
    show nina at right

    leonid "<{i}Голос Нины: «Просим всех в кабинет».{/i}>"

    hide nina

    show leonid at truecenter

    leonid "<{i}(Вскочил.){/i}>"

    leonid "Слышите? Она просит всех в кабинет."

    play sound1 footsteps

    leonid "<{i}(Бросается к кабинету и возвращается.){/i}>"

    stop sound1

    leonid "Все влюбленные — эгоисты! И я — тем более. Дорогой старик, объясните Маше... расскажите ей... но так, чтобы и она была счастлива... я хотел сам, но не могу, я слишком глуп сейчас, и у меня все в голове смешалось. Я уже пьян."

    leonid "Вы понимаете? Не делайте удивленного лица, конечно, вы понимаете."

    leonid "<{i}(Спешит в кабинет.){/i}>"

    hide leonid

    play sound1 footsteps
    play sound2 male_laughter

    show leonid at left
    show nina at truecenter
    show masha at right

    "<{i}В кабинете тот же шум и смех, что раздавались в передней. Голос Нины: «Маша, куда ты?» Маша входит в столовую.{/i}>"

    hide leonid
    hide nina
    hide masha

    stop sound1
    stop sound2

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я... дедушку позову."

    play sound1 door_creak

    masha "<{i}(Затворяет за собой дверь.){/i}>"

    stop sound1

    masha "Дедушка!"

    play sound1 male_cry

    hide masha

    show masha at left
    show leonid at right

    masha "<{i}(Бросается к нему, не в силах сдержать слез.){/i}>"

    hide leonid

    show masha at truecenter

    stop sound1

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм. Что случилось? Маша? Ну-ну..."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Дедушка, я уйду... ты скажи им — у меня голова болит, я уйду..."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... Вот-с изволите видеть.. Ффффy!"

    hide okaemov

    show okaemov at left
    show nina at truecenter
    show masha at right

    okaemov "<{i}В двеpях появляется Нина. Он делает ей знак. Нина понимающе вновь удаляется.{/i}>"

    hide nina
    hide masha

    show okaemov at truecenter

    okaemov "Машенька... расскажи мне."

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша отрицательно качает головой.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Ты хочешь уйти. Тебе неприятно с товарищами?"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Тот же жест Маши.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "Со мной?"

    okaemov "<{i}Тот же жест.{/i}>"

    okaemov "С Ниной Александровной, может быть?"

    okaemov "<{i}Молчание.{/i}>"

    okaemov "Неужели с ней — твоим лучшим другом?!"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    hide masha

    show masha at left
    show okaemov at right

    masha "<{i}(подымает к нему лицо и снова прячет).{/i}>"

    hide okaemov

    show masha at truecenter

    masha "Зачем она... его любит? Зачем?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(понявший все).{/i}>"

    okaemov "Хм-хм. Разве он плохой человек и его нельзя полюбить?"

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}Маша молчит.{/i}>"

    hide masha

    show okaemov at truecenter

    okaemov "И разве она — плохая женщина? Ты их обоих любила и любишь, как лучших своих друзей. Но дружба, Маша, проверяется не словами. Если ты — настоящий друг, ты должна им помочь. Как до сих пор они помогали тебе. Ведь, правда, помогали?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(тихо).{/i}>"

    masha "Да."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Сейчас тебе грустно расстаться со своей мечтой... Но твоя грусть пройдет, поверь мне. Пройдет. Растает, как снег в апреле. Ты сама, как апрель. Вчера — грело солнце, а сегодня — снег. Утром было тепло, а к вечеру снова мороз."

    okaemov "Но апрельские морозы не страшны. Потому что за апрелем обязательно наступит май. И твой май — впереди, Машенька. Поэтому я так смело и говорю: эта грусть пройдет. А их будущее может сломаться на всю жизнь. Ты ведь не хочешь этого?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(тихо).{/i}>"

    masha "Нет."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Я это знал. И мы встретим Новый год вместе с Ниной и Леонидом. Поздравим их с Новым годом и новым счастьем. Пусть их новый год начинается сразу со счастья. А?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    play sound1 female_sigh

    masha "<{i}(грустно вздохнув).{/i}>"

    stop sound1

    masha "Пусть."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "И радость наших друзей будет нашей радостью."

    play sound1 footsteps

    okaemov "<{i}(Подходит к дверям кабинета и распахивает их.){/i}>"

    stop sound1

    hide okaemov

    show galja at left
    show senja at truecenter
    show viktor at right

    okaemov "<{i}Видны сидящие в кружке гости: Леля, Галя, Сеня, Виктор и еще девочки и мальчик и из Машиной школы.{/i}>"

    hide lelja
    hide galja
    hide senja
    hide viktor

    show okaemov at truecenter

    okaemov "А теперь — пожалуйте!"

    hide okaemov

    show golos at truecenter

    $ golos_var = "{noalt}Голос."

    golos "Тсс, не мешайте!"

    hide golos

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля"

    lelja "<{i}(стоит посредине кабинета с платком в руках).{/i}>"

    lelja "Внимание! Я подбрасываю платок. Пока он летит — все должны смеяться."

    hide lelja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "Ха-ха-ха..."

    hide galja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Галина, остановись! Но как только платок коснется пола, все должны замолчать. Кто не замолчит, с того штраф. Понятно?"

    hide lelja

    show okaemov at left
    show galja at truecenter
    show senja at right

    $ okaemov_var = "{noalt}Все."

    okaemov "Понятно, понятно..."

    hide okaemov
    hide galja
    hide senja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Раз, два, три!"

    lelja "<{i}(Подбрасывает платок.){/i}>"

    lelja "Все начинают смеяться, громче всех Галя. Платок упал. Все замолчали. Окаемов, взглянув на Галю, расхохотался."

    hide lelja

    show lelja at left
    show galja at truecenter
    show senja at right

    $ lelja_var = "{noalt}Все."

    lelja "А-а-а, штраф, штраф!"

    lelja "— Какой штраф?.."

    lelja "— Спеть вдвоем."

    lelja "— Стать на руки..."

    lelja "— Нет, нет, сплясать."

    lelja "— Да, сплясать. Ха-ха-ха!"

    lelja "– Лезгинку!"

    hide lelja
    hide galja
    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но, позвольте, я не умею"

    okaemov "<{i}Его окружают, требуют, просят.{/i}>"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Дедушка... спой лучше."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Что ты, Маша... Я лет сорок не выступал перед аудиторией."

    hide okaemov

    show lelja at left
    show galja at truecenter
    show senja at right

    $ lelja_var = "{noalt}Все."

    lelja "Спойте, спойте..."

    hide lelja
    hide galja
    hide senja

    show galja at truecenter

    "<{i}Галя, схватив его за руку, тащит к роялю.{/i}>"

    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ну, что с вами делать? Придется."

    okaemov "<{i}(Сел, перебрал клавиши, запел.){/i}>"

    okaemov "Гляжу, как безумный, на черную шаль,"

    okaemov "И хладную душу терзает печаль."

    hide okaemov

    show okaemov at left
    show motja at right

    okaemov "<{i}Из передней появляется удивленная Мотя. Слушает.{/i}>"

    hide motja

    show okaemov at truecenter

    okaemov "Когда легковерен и молод я был,"

    okaemov "Младую гречанку я страстно любил."

    hide okaemov

    play sound1 clock

    "<{i}Часы ударили первый раз. Волнение.{/i}>"

    stop sound1

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Маша, Леонид Борисович, разливайте шампанское. Никто за стол не садится — все встречают Новый год на ногах."

    hide nina

    show leonid at truecenter

    "<{i}Леонид разливает вино. По радио слышен бой кремлевских часов. Все затихают. Одновременно начинают бить часы в столовой. Все ждут.{/i}>"

    hide leonid

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Десять..."

    play sound1 footsteps

    leonid "<{i}(Отбегает к картону с цифрой.){/i}>"

    stop sound1

    leonid "Одиннадцать. Двенадцать. Дорогие друзья! Поздравляю вас с Первым мая. Ура! Ой!"

    hide leonid

    play sound1 male_laughter

    show leonid at left
    show okaemov at right

    "<{i}Хохот. Крики «ура». Леонид срывает картон — под ним другой, с наспех нарисованным портретом Окаемова, который держит на руках спеленутого младенца с цифрой «1 ЯНВАРЯ». Новый взрыв смеха.{/i}>"

    hide leonid
    hide okaemov

    stop sound1

    show lelja at left
    show galja at truecenter
    show senja at right

    $ lelja_var = "{noalt}Голоса:"

    hide lelja
    hide galja
    hide senja

    show galja at left
    show masha at truecenter
    show leonid at right

    lelja "<{i}Галя, с Новым годом! — Леля, поздравляю! — Маша, где ты?.. — Леонид Борисович... — Василий Иванович, а со мной? Со мной, Василий Иванович!{/i}>"

    hide galja
    hide masha
    hide leonid

    show lelja at left
    show senja at right

    hide lelja
    hide senja

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор"

    play sound1 footsteps

    hide viktor

    show viktor at left
    show masha at right

    viktor "<{i}(подойдя к Маше).{/i}>"

    hide masha

    show viktor at truecenter

    stop sound1

    viktor "Мария! Вернись, я все прощу, упреки, подозренья... и как там дальше поется... Словом, будем в новом году дружить по-новому. И если я начну хамить по-старому, ты меня беспощадно крой. Твое здоровье, Мария!"

    hide viktor

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Спасибо, Витя."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(тем временем поднял салфеткy, увидел книги).{/i}>"

    okaemov "Позвольте! Книги?"

    okaemov "<{i}Все притихли.{/i}>"

    okaemov "Я же их продал. Откуда они снова здесь? Откуда книги, я спрашиваю?"

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина"

    hide nina

    show nina at left
    show masha at right

    nina "<{i}(видя, что Маша молчит).{/i}>"

    hide masha

    show nina at truecenter

    nina "Это подарок Маши. К Новому году. Вам."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Мне? Но позвольте! Откуда у Маши деньги? Маша, где ты? Поди сюда! Откуда ты взяла деньги?"

    hide okaemov

    show nina at truecenter

    $ nina_var = "{noalt}Нина."

    nina "Ноты, ноты, Василий Иванович. Срочная Переписка нот."

    hide nina

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Что?.."

    okaemov "<{i}(Стоит, пораженный.){/i}>"

    okaemov "Ноты?.. Хм..."

    hide okaemov

    show okaemov at left
    show masha at truecenter
    show nina at right

    okaemov "<{i}Смотрит на Машу, она на него.{/i}>"

    hide masha
    hide nina

    show okaemov at truecenter

    okaemov "С Новым годом, внучка! Спасибо! С новым счастьем, которое я нашел."

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show masha at right

    okaemov "<{i}(Обнял ее, потом торопливо отер глаза и, отвернувшись, вышел в кабинет.){/i}>"

    hide masha

    show okaemov at truecenter

    stop sound1

    hide okaemov

    "<{i}Все затихли.{/i}>"

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Да, с новым счастьем! Вы — наше счастье, Машенька. Вы наполнили наши жизни собой, и от этого они стали чище, лучше, достойнее!.. Друзья мои! Вы пришли в этот дом вместе с Машенькой. Вместе с нею я обнимаю всех вас."

    leonid "Здравствуй, племя молодое, но знакомое!"

    hide leonid

    play sound1 footsteps

    show masha at left
    show okaemov at truecenter
    show leonid at right

    "<{i}Шум. Крики. Звуки вальса. Маша идет в кабинет и возвращается с Окаемовым. Они танцуют теперь вместе плавный вальс, под звуки которого падает занавес.{/i}>"

    hide masha
    hide okaemov
    hide leonid

    stop sound1

label Act_3:
    play music "audio/music/13.mp3" fadeout 1.0 fadein 1.0

    scene 1 with fade

    "{b}Акт третий.{/b}"

    menu:
        "{color=#000}Сцена шестая{/color}":
            jump Act_3_Scene_1
        "{color=#000}Сцена седьмая{/color}":
            jump Act_3_Scene_2

label Act_3_Scene_1:
    "{b}Сцена шестая{/b}"

    show okaemov at truecenter

    "<{i}Обстановка первого акта. Солнечное весеннее утро. Окно в кабинете Окаемова открыто настежь, письменный стол почти пуст. Среди книг тоже наведен порядок. Двери в столовую распахнуты, видно, что в столовой много корзин с цветами.{/i}>"

    hide okaemov

    show masha at left
    show okaemov at right

    "<{i}Одна из корзин стоит на окне в кабинете. В столовой Маша пишет, сидя за столом. В кабинете занимается Окаемов.{/i}>"

    hide masha
    hide okaemov

    "<{i}Радио: «Вчерашний весенний бал учащейся молодежи открылся концертом школьной самодеятельности. Большим успехом пользовались выступления оных танцоров 18-й школы, хора пионеров и ученицы 137-й школы Марии Окаемовой».{/i}>"

    show masha at left
    show okaemov at right

    "<{i}Маша и Окаемов одновременно подняли головы, слушают.{/i}>"

    hide masha
    hide okaemov

    show masha at truecenter

    "<{i}«Выступление Окаемовой мы записали на пленку. Слушайте!» Секундная пауза, потом слышен шум аплодисментов и голос Маши: Между небом и землей Песня раздается...{/i}>"

    hide masha

    play sound1 footsteps

    show masha at left
    show okaemov at right

    "<{i}Маша слушает себя с напряженным вниманием. Окаемов со своего места следит за ней. Песня кончилась. Слышен взрыв аплодисментов. Маша ловит на себе взгляд дедушки, подбегает к радио и выключает его.{/i}>"

    hide masha
    hide okaemov

    stop sound1

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Так ты никогда не напишешь своей книги, дедушка."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "В мире написано столько книг, что, если я не напишу еще одной, ровно ничего не изменится."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Неправда. Леонид Борисович сказал, что твою книгу ждут во всем мире."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Но во всем мире ее ждут восемь человек, которым она как-то интересна. Ты скажи лучше, что это ты с таким старанием записываешь?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    play sound1 running

    masha "<{i}(встает, бежит в кабинет, неся в руках бумату).{/i}>"

    stop sound1

    masha "Заявление."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ты умеешь сочинять заявления?"

    okaemov "<{i}(Читает.){/i}>"

    okaemov "«В комсомольскую организацию нашей школы...» Хм... «Прошу принять меня в ряды Ленинского комсомола ввиду того, что мне вчера исполнилось уже шестнадцать лет и я хочу бороться за победу коммунизма»."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А что еще добавить — не знаю."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Видишь ли, мне не приходилось подавать подобных заявлений, и я, право, не сумею тебе ответить... Но, может быть, достаточно? Ведь бороться за коммунизм — это же цель всей человеческой жизни!"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Потом анкету надо заполнить. В графе родителей мне как писать? Кто моя мама?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм. Мещанка, наверное."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Что ты, дедушка, разве можно так про маму говорить! Мещанка — это которая сплетничает, склоки любит, жадная."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Нет-нет, я имею в виду социальное происхождение, а не нравственный облик."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Все равно нельзя. Я напишу — домашняя хозяйка, и все. Я живу у дедушки, уже полтора года."

    masha "<{i}(Пишет. Потом задумчиво.){/i}>"

    masha "Шестнадцать лет. Странно. Позавчера было пятнадцать, а вчера сразу стала на год старше. А через четыре года мне будет двадцать. Поскорее бы!"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "И что тогда?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Не знаю, просто так. Двадцать лет..."

    play sound1 footsteps

    masha "<{i}(Подходит к корзине с цветами.){/i}>"

    stop sound1

    masha "Эту сирень мне подарили за концерт... Они знают, что я люблю цветы."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм... Видишь ли, внучка, меня тревожат эти цветы... Слишком много цветов. Даже аплодисменты на пленку записаны."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "О чем ты, дедушка?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "О тебе написали в газетах. Снимок с тебя поместили. Я сорок лет работаю в палеографии и еще не видел своего снимка в печати, а ты выступила на трех концертах, и тебя уже приглашают выступать постоянно. Даже за деньги."

    okaemov "Я, конечно, отбил охоту соваться с подобными предложениями, но, может быть, тебе самой хочется... может быть, ты в глубине души уже ревниво считаешь, сколько секунд аплодируют тебе и сколько твоей подруге. А?"

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Нет, дедушка, не считаю..."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Не поддавайся, Машенька, на ранние похвалы. Останься простой и милой, какой я тебя люблю и знаю..."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Дедушка, милый, я никогда не зазнаюсь! И я совсем не о том мечтаю. Ты знаешь, о чем я мечтаю? Вот... когда мне будет двадцать лет... или двадцать один... я стану настоящей певицей, знаменитой певицей... Нет, ты постой..."

    masha "Люди от моих песен будут радостными, станут думать о чем-то большом, стремиться к подвигам, помогать товарищам... и любить детей. И вот меня позовут спеть во Дворце Советов. И я перед пением выйду и скажу речь. Речь о моем дедушке."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... лишнее, внучка, лишнее..."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я скажу им — вот настоящая слава: трудиться, как дедушка, и сделать свой труд целью жизни! И все двадцать тысяч зрителей встанут тогда и устроят тебе овацию. Вот о чем мечтаю."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм."

    play sound1 footsteps

    okaemov "<{i}(Отвернувшись, отходит к книтам, якобы по делу.){/i}>"

    stop sound1

    okaemov "Я, пожалуй, оглохну."

    hide okaemov

    play sound1 footsteps
    play sound2 telephone

    show motja at left
    show leonid at right

    "<{i}Звонок. Мотя спешит отпереть. Вбегает Леонид с двумя большими кожаными чемоданами.{/i}>"

    hide motja
    hide leonid

    stop sound1
    stop sound2

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(в передней).{/i}>"

    leonid "Мотя! За мной!"

    play sound1 footsteps

    leonid "<{i}(Вбегает в кабинет.){/i}>"

    stop sound1

    hide leonid

    show leonid at left
    show motja at truecenter
    show okaemov at right

    leonid "<{i}Мотя за ним.{/i}>"

    hide motja
    hide okaemov

    show leonid at truecenter

    leonid "<{i}(Бросает чемоданы на пол.){/i}>"

    leonid "Друзья мои! Тише! Сядьте! Все сядьте! Тихо!"

    leonid "<{i}(Выдержав паузу.){/i}>"

    leonid "Час назад родилась девочка!"

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Господи!"

    hide motja

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(всплеснув руками).{/i}>"

    masha "Я так хотела, чтобы девочка!"

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "И я настаивал именно на девочке. Чтобы назвать ее Машенькой. Маша большая и Маша маленькая, каково! Говорил с Ниной по телефону. Просила обнять вас."

    leonid "<{i}(Обнимает всех троих.){/i}>"

    leonid "Необыкновенной силы ребенок! Вылитый отец! Это я — отец! Я! Ха-ха-ха!"

    leonid "<{i}(Валится на диван.){/i}>"

    leonid "Я помню первый в моей жизни поцелуй — зажмуренный, глубокий, когда все во мне было насыщено мучительным блаженством. И вот сейчас — опять. То же самое, но в кvбе! Отец! Это значит — жизнь продолжается, черт возьми!"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Как Нина?"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Чудесно! И вас всех зовет."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А зачем чемоданы?"

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Какие чемоданы? Надо же было что-нибудь купить на радостях. Продавщице я подарил неceccep. Xa-xa-xa! Я — отец!"

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Бельишка бы лучше приобрели новорожденной."

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "В этом чемодане белье, а в том — игрушки."

    hide leonid

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Где, где?"

    hide masha

    show masha at left
    show motja at truecenter
    show leonid at right

    masha "<{i}(Вместе с Мотей и Леонидом рассматривает чемоданы.){/i}>"

    hide motja
    hide leonid

    show masha at truecenter

    masha "Да ей же штанишки рано. Ей Пеленки нужны."

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Рано? Ничего, вырастет — пригодятся."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Судя по началу, она будет самой избалованной дочкой в мире."

    okaemov "<{i}(Садится, пишет.){/i}>"

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Да уж вы меня сдерживайте, дорогой старик. Я еще не представляю себе, как возьму дочку на руки. Уроню, должно быть, на радостях. Или поломаю ручки. Боже, которого нет, как идет время! Я — отец! Я должен бежать. Расспросить дежурных. Заказать цветы."

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "И от меня, пожалуйста. От нас с Машей и Мотей."

    okaemov "<{i}(Протягивает бумагу.){/i}>"

    okaemov "Я тут написал Нине... передайте. Хм..."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "И я, и я припишу."

    hide masha

    show masha at left
    show okaemov at right

    masha "<{i}(Садится, пишет на письме Окаемова свое.){/i}>"

    hide okaemov

    show masha at truecenter

    hide masha

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Все передам... И все перепутаю."

    play sound1 footsteps

    leonid "<{i}(Подхватывает чемоданы, выходит в переднюю. Возвращается.){/i}>"

    stop sound1

    leonid "Мотя, готовьтесь. Мотя, готовьтесь. Прощайтесь с этим домом, вы будете Машиной няней."

    hide leonid

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Что вы, Леонид Борисович, что вы... не могу."

    hide motja

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Никаких разговоров! Я знал, что делал, когда дарил вам золотой халат."

    play sound1 footsteps

    leonid "<{i}(Выбегает.){/i}>"

    stop sound1

    leonid "Маша"

    leonid "<{i}(задумчиво){/i}>"

    leonid ". Машенька. Как будто моя сестричка."

    play sound1 telephone

    leonid "<{i}Новый звонок.{/i}>"

    stop sound1

    leonid "<{i}(Весело.){/i}>"

    leonid "Опять он."

    leonid "<{i}(Подражая.){/i}>"

    leonid "Граждане, я — отец!"

    play sound1 footsteps

    leonid "<{i}(Надевает забытую Леонидом шляпу, идет.){/i}>"

    stop sound1

    hide leonid

    play sound1 footsteps

    show vera at left
    show masha at right

    "<{i}Входит Вера Михайловна — мать Маши, хорошо сохранившаяся женщина.{/i}>"

    hide vera
    hide masha

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Ой!"

    play sound1 running

    motja "<{i}(Бежит в кабинет.){/i}>"

    stop sound1

    motja "Василь Иваныч! Машенька! Ой!"

    play sound1 footsteps

    motja "<{i}(Убегает в кухню.){/i}>"

    stop sound1

    hide motja

    play sound1 footsteps

    show vera at truecenter

    "<{i}Вера входит в кабинет.{/i}>"

    hide vera

    stop sound1

    show masha at truecenter

    $ masha_var = "{noalt}Маша"

    masha "<{i}(потрясенная).{/i}>"

    masha "Мама?!"

    hide masha

    show vera at left
    show masha at right

    "<{i}Вера протягивает к ней руки. Маша бросается к ней. Они обнялись.{/i}>"

    hide vera
    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    play sound1 female_cry

    vera "<{i}(плачет, приговаривая).{/i}>"

    stop sound1

    vera "Прости свою маму, Maшa!"

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Что ты, мама, зачем? Мне хорошо здесь. Дедушка — это ведь моя мама."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(здороваясь).{/i}>"

    okaemov "Рад вас видеть."

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    vera "<{i}(нервно).{/i}>"

    vera "Рады? Правда? А мне казалось, что вы прогоните меня... Я едва поднялась по лестнице от волнения."

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Что вы, что вы..."

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "О, я так благодарна вам, Василий Иванович, за ваши заботы о моей дочурке. Вы приютили ее, согрели, мы с Машей будем вечно признательны. Правда, дочка?"

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Конечно, мама. Сними шляпку. Где твои вещи?"

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "В гостинице. Ты выросла, девочка, ты совсем взрослая."

    hide vera

    show vera at left
    show masha at right

    vera "<{i}(Гладит ее лицо.){/i}>"

    hide masha

    show vera at truecenter

    vera "Моя дорогая! Прости свою маму!"

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Мама, милая, не надо так... Я ведь сама, сама..."

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Но я не должна была тебя отпускать. Но теперь я с тобой не расстанусь. Ты у меня одна на свете. Я слишком поздно это поняла, дочурка... Я была слишком занята собой. Своей жизнью. Василий Иванович, мы вам мешаем?.."

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(на ходу).{/i}>"

    okaemov "Вы... хм-хм... вы беседуйте, я тут... по делу..."

    play sound1 footsteps

    okaemov "<{i}(Выходит из кабинета.){/i}>"

    stop sound1

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    vera "<{i}(опять обнимая дочь).{/i}>"

    vera "Мое сокровище! Моя ли ты еще? Или уж чужая, дедушкина? Чья ты, Маша?"

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я... я не понимаю тебя, мама."

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Кого ты больше любишь? Меня или дедушку?"

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я... я... зачем ты спрашиваешь?"

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "О, скажи мне, что ты моя... что ты поедешь со мной..."

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Куда?"

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "В наш город. Тебя ждут там. Твои подруги по школе."

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А как же дедушка?"

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Ты будешь писать ему. Часто-часто."

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Писать?.. Но, мама... значит... А разве нельзя, мама, нам с дедушкой... вместе... тут..."

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Нет, Maшa."

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Почему?"

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    vera "<{i}(после паузы).{/i}>"

    vera "Он меня не любит, Маша."

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Не любит? Как же?.. Я спрошу его, мaма."

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Нет, Маша, нет. Не спрашивай. Нельзя. Я тоже не люблю его, девочка."

    vera "<{i}(Пауза.){/i}>"

    vera "Пойдем со мной, в гостиницу."

    hide vera

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "А? В гостиницу?.. Нет... я в школу должна. В школу... Меня ждут... Я... я пойду, мама..."

    hide masha

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Хорошо, ступай. Я приду за тобой в школу..."

    play sound1 footsteps

    hide vera

    show vera at left
    show masha at right

    vera "<{i}(Провожает Машу и возвращается. Шепчет про себя.){/i}>"

    hide masha

    show vera at truecenter

    stop sound1

    vera "Лишь бы хватило сил, лишь бы не показать ему, что я боюсь... нет-нет..."

    play sound1 footsteps

    hide vera

    show vera at left
    show okaemov at right

    vera "<{i}(Выпрямляется, принимает непринужденный вид, когда входит Окаемов.){/i}>"

    hide okaemov

    show vera at truecenter

    stop sound1

    vera "Все те же книги. Так же стоит диван. Как будто и не было этих семнадцати лет. Разве на столе только стало чище. И появились цветы. Цветов раньше не было... Но даже Мотя совершенно не изменилась. А вот я постарела. Да?"

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Людям это свойственно."

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Да, постарела. Но такова жизнь — и не нам осуждать ее, как любил повторять один из моих знакомых."

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Доктор Туманский?"

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Разве? Да, вспоминаю, он... А вы, как всегда, пишете новую книгу о каком-нибудь пятнадцатом веке... Не буду дольше отвлекать вас своей болтовней... До свиданья, милый Василий Иванович. Еще раз благодарю вас за все, что вы для Маши сделали."

    play sound1 footsteps

    vera "<{i}(Прощается, идет к двери.){/i}>"

    stop sound1

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(глухим, надтреснутым голосом).{/i}>"

    okaemov "Вера Михайловна..."

    hide okaemov

    show okaemov at left
    show vera at right

    okaemov "<{i}Вера обернулась{/i}>"

    hide vera

    show okaemov at truecenter

    okaemov "Не отнимайтс у меня Машу."

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    vera "<{i}(вздрогнула).{/i}>"

    vera "Василий Иванович, Маша — это все, что у меня осталось в жизни."

    vera "<{i}(Хочет еще говорить, но повернулась, пошла.){/i}>"

    hide vera

    show okaemov at truecenter

    "<{i}Окаемов молча стоит.{/i}>"

    hide okaemov

    "<{i}Занавес{/i}>"

label Act_3_Scene_2:
    "{b}Сцена седьмая{/b}"

    play sound1 footsteps

    show okaemov at truecenter

    "<{i}Та же обстановка. Такое же утро. На диване аккуратно постланная постель. На столе недопитый крепкий чай и груда окурков в пепельнице. Из столовой в кабинет вошел Окаемов. Он курит. Осмотрелся, ткнул папиросу в пепельницу, взял книгу, другую. Положил опять.{/i}>"

    hide okaemov

    stop sound1

    play sound1 footsteps

    show okaemov at left
    show motja at right

    "<{i}Потом вышел в столовую. Видно, как ходит он там, от предмета к предмету, не зная, за что приняться. В кабинет входит Мотя.{/i}>"

    hide okaemov
    hide motja

    stop sound1

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Прилегли бы на часок, Василий Иванович. Вторую ночь, всю как есть, на ногах."

    motja "<{i}(Убирая постель.){/i}>"

    motja "Двадцать лет не курили, а тут нате вам."

    motja "<{i}(Шепотом.){/i}>"

    motja "А вы позвоните внучке. В гостиницу. Приходи, мол, и все такое."

    hide motja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "А?"

    okaemov "<{i}(Смотрит непонимающе, потом.){/i}>"

    okaemov "В возмездие, Мотя, верите? Верьте! Возмездие существует. Что Маша ушла — это мне возмезлие. Месть жизни. Я ведь не хотел Машиного приезда. Что ж, желание мое выполнено. Маши нет со мной. Могу быть снова один."

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show motja at right

    okaemov "<{i}Мотя выходит.{/i}>"

    hide motja

    show okaemov at truecenter

    stop sound1

    play sound1 footsteps

    okaemov "<{i}(Закрывает лицо руками. Потом, овладев собой, подходит к столу.){/i}>"

    stop sound1

    okaemov "Кажется, у меня сегодня лекция. В котором часу? Забыл. Все забыл."

    play sound1 telephone

    okaemov "<{i}Звонок в передней.{/i}>"

    stop sound1

    play sound1 running

    okaemov "<{i}(Вздрагивает, бежит, бормочет на ходу.){/i}>"

    stop sound1

    okaemov "Сам, сам отопру..."

    play sound1 door_creak

    okaemov "<{i}(В передней не может сразу отпереть дверь — так сильно дрожат руки.){/i}>"

    stop sound1

    okaemov "Отпираю... Сейчас... сейчас..."

    okaemov "<{i}(Отпер.){/i}>"

    play sound1 footsteps

    hide okaemov

    show galja at left
    show senja at truecenter
    show viktor at right

    okaemov "<{i}Входят Леля, Галя, Сеня и Виктор.{/i}>"

    hide lelja
    hide galja
    hide senja
    hide viktor

    show okaemov at truecenter

    stop sound1

    hide okaemov

    show okaemov at left
    show lelja at truecenter
    show masha at right

    okaemov "<{i}(Заглядывая за их спину, ищет Машу.){/i}>"

    hide lelja
    hide masha

    show okaemov at truecenter

    okaemov "А-а-а. Вы к Маше. Машеньки нет. Нет Маши."

    hide okaemov

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Мы к вам пришли, Василий Иванович. Можно?"

    hide viktor

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ко мне? Прошу, прошу."

    okaemov "<{i}(Проводит их в кабинет.){/i}>"

    okaemov "Снова выступить? Увольте. Не в состоянии. И рад бы, но решительно не в состоянии. И надолго. Да-с. Весьма надолго."

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Нам нужен ваш совет, Василий Иванович."

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Почему мой совет?"

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Вот Сеня расскажет."

    hide lelja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Вопрос поставлен нами весьма развернуто. Мы категорически осуждаем поведение гражданки Олониной."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Кого?"

    hide okaemov

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Машиной мамы. Веры Михайловны."

    hide viktor

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "То есть? Хм. Осуждаете. Неясно."

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Во избежание абстрактности буду конкретным. Гражданка Олонина намерена взять свою дочь из школы до окончания учебного года ввиду переезда в другой город. Но, во-первых, переезд не вызывается такой срочностью, так как вы Машу из дому не гоните."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Я? Что вы!"

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Леля, неплохо бы коротенько фиксировать наше совещание."

    hide senja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Говори так!"

    hide lelja

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "А главное, Вера Михайловна соглашается на включение Маши в концертную группу молодых дарований для турне по Крыму и Кавказу."

    hide viktor

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Она говорит — это для того, чтобы развлечь Машу, а то ей очень грустно уезжать от вас."

    hide lelja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Но, во-первых, нам известно, что турне состоится лишь по окончании учебного года, а во-вторых..."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "«Во-первых, во-вторых»!.. Машенька на гастроли едет, а вы — «во-вторых». Да разве ж она певица? Ведь и поет-то она больше сердцем, чем голосом: молода, правдива, чиста — вот что публику привлекает в Машеньке."

    okaemov "Одна такая поездка — и Маша отравлена на всю жизнь."

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Василий Иванович, я об этом и хотел сказать. Ну точь-в-точь... Мы собрали комсомольское классное собрание и все в один голос говорили, что это неправильно!"

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ах, друзья мои, что собрание! У Маши есть мать — и мать за все отвечает. Я родной дед, и то могу лишь молча разводить руками."

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Нет, Василий Иванович, это неправильно."

    hide lelja

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "Дай, я скажу, почему неправильно..."

    hide viktor

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Нет, я первая... Василий Иванович, Маша не только дочь или внучка... Маша еще и член нашего коллектива."

    hide lelja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Коллектива? Какого?"

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Комсомольского. Мы уже рассматривали ее заявление на бюро. И мы отвечаем теперь за Машу."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Вы?"

    hide okaemov

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор."

    viktor "И все равно — пусть она даже не комсомолка — все равно отвечаем."

    hide viktor

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Да. И мы не можем просто молчать... Если мы видим, что портят Машин талант..."

    hide lelja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "И характер."

    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Да-да. Именно характер! Эгоизм. Тщеславие. Самовлюбленность. Вот удел легкого успеха."

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Мы постановили поэтому, во-первых, поговорить с Машей."

    hide senja

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Я уже виделась с Машей. Оказывается, мама сказала ей, что умрет, если Маша ее покинет."

    hide lelja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Во-вторых..."

    senja "<{i}(осекается){/i}>"

    senja ", то есть не во-вторых, а затем, мы поставим вопрос развернуто. И для этого нам нужна ваша помощь."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Моя? Хм. Чем могу быть полезен?"

    hide okaemov

    show senja at truecenter

    $ senja_var = "{noalt}Сеня."

    senja "Мы знаем, что вы согласны с нами, и поэтому просим вас написать статью в «Комсомольскую правду» под заглавием «Воспитание молодых талантов». Статью мы подпишем все и будем требовать отмены этого турне."

    senja "Мы добьемся, я знаю, — я уже говорил в редакции, они вас там ждут."

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Меня? В «Комсомольской правде»?"

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля."

    lelja "Они даже просили, чтобы вы скорее пришли. Они вам еще хотят статьи заказать..."

    hide lelja

    show galja at truecenter

    $ galja_var = "{noalt}Галя."

    galja "О подрастающем поколении."

    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Хм-хм... Польщен, но, право... да-с..."

    okaemov "<{i}(Внезапно.){/i}>"

    okaemov "Но статью я им напишу... Сегодня же. Да-с."

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля"

    hide lelja

    show lelja at left
    show galja at right

    lelja "<{i}(подталкивая Галю, шепотом).{/i}>"

    hide galja

    show lelja at truecenter

    lelja "Ну, скажи. Скажи."

    hide lelja

    show galja at truecenter

    $ galja_var = "{noalt}Галя"

    play sound1 footsteps

    hide galja

    show galja at left
    show okaemov at right

    galja "<{i}(подходя к Окаемову).{/i}>"

    hide okaemov

    show galja at truecenter

    stop sound1

    galja "А потом... Мы хотим еще... чтобы вы и без Маши к нам приходили — на родительские собрания... и выступали у нас... и в гости нас приглашали.. иногда."

    hide galja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Спасибо. Хм."

    okaemov "<{i}(Молчит, потом.){/i}>"

    okaemov "Обязательно. Приходите. Непременно. И часто. Да. Вот-с."

    okaemov "<{i}(Отвернулся к окну.){/i}>"

    hide okaemov

    show lelja at truecenter

    $ lelja_var = "{noalt}Леля"

    lelja "<{i}(подымается).{/i}>"

    lelja "До свиданья, Василий Иванович."

    hide lelja

    show senja at truecenter

    $ senja_var = "{noalt}Сеня"

    senja "<{i}(прощаясь).{/i}>"

    senja "За статьей забегу вечером. Значит, поборемся!"

    hide senja

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(провожая их до двери).{/i}>"

    okaemov "Да. Поборемся!"

    hide okaemov

    show okaemov at left
    show viktor at right

    okaemov "<{i}(Виктору.){/i}>"

    hide viktor

    show okaemov at truecenter

    okaemov "А вы... Хм. Вы, стало быть, тоже друг Машеньки?"

    hide okaemov

    show viktor at truecenter

    $ viktor_var = "{noalt}Виктор"

    viktor "<{i}(смутившись).{/i}>"

    viktor "Стараюсь им быть. Жизнь — сложная штука, Василий Иванович."

    hide viktor

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Вот именно, Виктор Павлович."

    play sound1 footsteps

    okaemov "<{i}(Возвращается к себе, возбужденно шатает по кабинету.){/i}>"

    stop sound1

    okaemov "Так. Что же, собственно, произошло?.."

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show motja at right

    okaemov "<{i}(Вошедшей Моте.){/i}>"

    hide motja

    show okaemov at truecenter

    stop sound1

    okaemov "Мотя! Сварите крепкого кофе. Я буду работать... Да-с. Вы знаете, кто приходил сейчас? Друзья. Да-с, очень большие друзья. И мы поборемся за Машу, Мотя!"

    okaemov "<{i}(Садится к столу, достает бумагу, начинает писать.){/i}>"

    hide okaemov

    show motja at truecenter

    $ motja_var = "{noalt}Мотя."

    motja "Дай-то бог!"

    hide motja

    play sound1 telephone

    "<{i}Звонок в передней.{/i}>"

    stop sound1

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Отоприте."

    hide okaemov

    play sound1 footsteps

    show motja at left
    show tumanskij at truecenter
    show vera at right

    "<{i}Мотя спешит в переднюю, открывает дверь. Входят Туманский и Вера.{/i}>"

    hide motja
    hide tumanskij
    hide vera

    stop sound1

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Дома?"

    play sound1 footsteps

    vera "<{i}(Не дождавшись ответа, быстро проходит в кабинет. Страшно возбуждена.){/i}>"

    stop sound1

    vera "О, вы, как всегда, сидите спокойно! Вы уверены в своей силе. Но нет! Вы не отнимете у меня дочери, не отнимете!"

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    hide okaemov

    show okaemov at left
    show vera at right

    okaemov "<{i}(пораженный ее появлением).{/i}>"

    hide vera

    show okaemov at truecenter

    okaemov "Вы?"

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Я — мать. Я не остановлюсь ни перед чем."

    hide vera

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вера Михайловна..."

    hide tumanskij

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Вы надеетесь, что Маша вернется к вам! Не надейтесь!"

    hide vera

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вера Михайловна, вы просили меня помочь вам в этом трудном для вас положении. Если моя помощь вам не нужна, удаляюсь."

    hide tumanskij

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Нет, нет, останьтесь! Я не могу одна... я... я..."

    hide vera

    show vera at left
    show tumanskij at right

    vera "<{i}(Рыдает, цепляясь за Туманского.){/i}>"

    hide tumanskij

    show vera at truecenter

    hide vera

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    play sound1 footsteps

    hide tumanskij

    show tumanskij at left
    show vera at truecenter
    show okaemov at right

    tumanskij "<{i}(усаживает ее на диван и подходит к Окаемову).{/i}>"

    hide vera
    hide okaemov

    show tumanskij at truecenter

    stop sound1

    tumanskij "Я — друг Веры Михайловны и, смею думать, вaш. Поэтому я надеюсь быть беспристрастным. Согласны вы меня выслушать?"

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Ну-с?"

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Советский закон на стороне матери. И это справедливый закон. Но тот же закон предоставляет ребенку право выбора. И вы, Василий Иванович, должны помочь Маше определить именно этот выбор, несмотря на ее стремление к вам."

    tumanskij "Поймите, Василий Иванович, ребенок — это самое дорогое в жизни матери. Вам очень тяжело расставаться с Машей, но вы не должны думать только о своих чувствах..."

    hide tumanskij

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Пока я думал о своих чувствах, я молчал. Нет-с, Павел Павлович, тут речь не о чувствах дедушки или матери. Тут — судьба будущего гражданина, его воспитание. Я, седобородый старик, в комсомольскую газету статью пишу."

    okaemov "Машина жизнь не только семейный вопрос, хоть и сидим мы в четырех стенах... Я вмешиваюсь и бороться буду за правильное воспитание нового поколения... в духе нашей страны... и нашего общества."

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Ну что же... Пишите, топчите меня, — вы уж однажды сделали это... может быть, и теперь вам удастся снова, еще раз разбить мою жизнь..."

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Вера Михайловна, опомнитесь! Когда я разбивал вашу жизнь?"

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "О, я знаю, вы до сих пор убеждены в своей правоте. Я для вас всегда была капризной и вздорной женщиной, поссорившей сына с вами... и вы объявили войну. Вы стали между мной и Николаем. Вы хорошо и тонко выставляли ему напоказ мои дурные стороны."

    vera "Я постоянно оказывалась лишней в ваших умных разговоpax, я всегда была виноватой в домашних неурядицах, тысячью мелких, еле заметных уколов вы вызывали меня на ссоры с Николаем по пустякам."

    vera "И Николай, уважавший вас, начал упрекать меня, сердиться, потом ссориться со мной из-за вас. Я была молода, неопытна, я не умела сдерживать себя, промолчать или ответить вам по-серьезному."

    vera "Я просто возненавидела вас и стала действительно злой, раздражительной и упрямой... Даже когда мы оставались одни с Николаем, вместо отдыха мы начинали бесконечные объяснения о моем характере, о вашем уме."

    vera "Я кончала слезами, он — молчаливым протестом... Все, все, вами сказанное обо мне при Николае, носило в себе этот яд разрушения нашей любви — мы ведь очень любили друг друга, Василий Иванович."

    vera "Будь вы чуточку внимательнее ко мне тогда, ко мне, ставшей женой вашему сыну, найди вы в себе сотую долю той заботы, какую вы сейчас проявляете к Маше... и наша жизнь сложилась бы по-другому..."

    vera "Какой я была молодой, счастливой и доброй, когда Николай привез меня к вам и сказал: «Отец, Вера — моя жена»... Я так стремилась понять вас, быть вами любимой и нужной вам... А что я встретила? Недоверие. Холод."

    vera "Раздражение от того, что вторгся чужой человек. Представьте хоть на мгновение на моем месте Машу... Машу, которую вы так любите, за которую вы так хотите бороться... и вам самому станет страшно."

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(глухо).{/i}>"

    okaemov "Да."

    hide okaemov

    "<{i}Молчание.{/i}>"

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    hide vera

    show vera at left
    show okaemov at right

    vera "<{i}(сидит, обессиленная сказанным, потом начинает вновь, уже другим, тихим, усталым голосом).{/i}>"

    hide okaemov

    show vera at truecenter

    vera "Помните вы тот вечер? Николай собирался в Ленинград на Съезд хирургов. Я должна была ехать с ним и радовалась этой поездке. Я хотела отдохнуть... от вас... Вы же бросили сыну вскользь: «Не думаю, чтобы поездка вдвоем укрепила твою репутацию хирурга»."

    vera "Все взорвалось во мне! Вы боялись, что я испорчу репутацию сына! Я вскочила, закричала что-то ужасно грубо вам в лицо... Вы вздохнули и молча вышли из комнаты. Никола за вами. О, я до сих пор вижу его уничтожающий взгляд."

    vera "До сих пор слышу ледяные слова: «Мне стыдно, что у меня такая жена...» Все мне казалось конченным. Я выбежала из дома, не зная, зачем и куда. У ворот меня встретил Туманский. Он удержал меня, стал расспрашивать, утешать."

    vera "Он единственный понял меня тогда, и я пошла к нему с твердым намерением не возвращаться обратно..."

    hide vera

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Вера Михайловна, может быть, я лишний сейчас?"

    hide tumanskij

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Останьтесь. Теперь можно говорить и об этом."

    hide vera

    show vera at left
    show okaemov at right

    vera "<{i}(Окаемову.){/i}>"

    hide okaemov

    show vera at truecenter

    vera "Тогда вы знали только, что капризная ваша невестка покинула дом, потом вернулась и через месяц увезла сына. Вы так и не узнали тогда, что я рассказала Николаю обо всем, когда он нашел меня у Туманского."

    vera "И что он сам, сам решил уехать со мной от вас... чтобы хоть как-то спасти остатки нашей любви. Да, именно остатки, потому что никогда, до самой своей смерти, он уже не был со мной прежним Николаем..."

    vera "Вам он тоже перестал писать и весь ушел в воспитание Машеньки... А потом смерть. Одиночество. Новая попытка создать семью. Но Маша не могла простить мне измены памяти обожаемого ею отца. Да, я отослала Машу к вам."

    vera "Я еще мечтала тогда о возможности личного счастья... но теперь, когда и эта последняя попытка потерпела крах, я решила жить только для дочери и найти свое счастье в ней..."

    vera "И теперь вы снова на моем пути: в конце моей жизни, как и в ее начале, вы хотите отнять у меня единственное оставшееся мне — дочь мою..."

    hide vera

    "<{i}Молчание.{/i}>"

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    okaemov "<{i}(медленно поднялся, говорит тихо).{/i}>"

    okaemov "Прошу вас... Вера Михайловна... оберегайте Машу, пусть она живет и учится... без всяких гастролей... Пусть она растет... Ее в коллектив приняли... Побольше ей хороших товарищей... Вы позаботьтесь, прошу вас..."

    okaemov "а уж я позабочусь, чтобы Маша осталась с матерью. Моя вина — я знаю. Мне и отвечать за нее."

    play sound1 footsteps
    play sound2 door_creak

    okaemov "<{i}(Вышел в столовую, затворив за собой дверь.){/i}>"

    stop sound1
    stop sound2

    hide okaemov

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    tumanskij "<{i}(после паузы).{/i}>"

    tumanskij "Вы потрясли старика вашим рассказом. Вот так, вдруг, понять, что именно ты сломал жизнь сыну. Это, знаете, нелегко."

    play sound1 footsteps

    tumanskij "<{i}(Встает, отходит к окну.){/i}>"

    stop sound1

    tumanskij "Как часто, искренно полагая, что мы заботимся о наших детях, мы, на самом деле, думаем лишь о себе — о своих желаниях, о своей жизни... Да... Ваш рассказ заставляет задуматься..."

    tumanskij "<{i}(Пауза.){/i}>"

    tumanskij "Вера Михайловна, не сердитесь. Но вдруг мне пришло на ум: вот сейчас с Машей вы не повторяете той же ошибки?.."

    hide tumanskij

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Я не понимаю, Павел Павлович. О чем вы?"

    hide vera

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский."

    tumanskij "Когда вы боролись за Машу... Вы уверены, что Маше лучше с вами, чем с дедом? Если вы действительно думаете о ней. О ее будущем!"

    hide tumanskij

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    vera "<{i}(растерянно).{/i}>"

    vera "Я... не понимаю. Я — мать, Павел Павлович. И думаю только о Маше."

    hide vera

    show tumanskij at truecenter

    $ tumanskij_var = "{noalt}Туманский"

    tumanskij "<{i}(вздрогнув).{/i}>"

    tumanskij "Да-а. Я тоже — отец."

    hide tumanskij

    play sound1 footsteps
    play sound2 telephone

    show motja at left
    show leonid at right

    "<{i}Звонок. Мотя идет отпереть. Входит Леонид.{/i}>"

    hide motja
    hide leonid

    stop sound1
    stop sound2

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(быстро).{/i}>"

    leonid "Маша здесь?"

    hide leonid

    play sound1 footsteps

    show motja at left
    show leonid at right

    "<{i}Мотя, горестно махнув рукой, проходит в кухню. Леонид проходит в кабинет. Молчаливая встреча.{/i}>"

    hide motja
    hide leonid

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Вера Михайловна, Маша у вас?"

    hide leonid

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Да."

    hide vera

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Могу я видеть ее? Поговорить с ней?"

    hide leonid

    show vera at truecenter

    $ vera_var = "{noalt}Вера."

    vera "Конечно. В любое время. Прошу вас."

    hide vera

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов"

    play sound1 footsteps

    hide okaemov

    show okaemov at left
    show vera at right

    okaemov "<{i}(входит, протягивает Вере письмо).{/i}>"

    hide vera

    show okaemov at truecenter

    stop sound1

    okaemov "Вот, написал. Передайте Машеньке. Она поймет. Она останется с вами."

    hide okaemov

    show vera at truecenter

    $ vera_var = "{noalt}Вера"

    vera "<{i}(поднимаясь).{/i}>"

    vera "Василий Иванович! Я — обыкновенная женщина, может быть плохая мать. Ho, Beрьте, я понимаю, чего стоило вам это письмо. Прощайте."

    hide vera

    play sound1 footsteps

    show okaemov at left
    show vera at truecenter
    show tumanskij at right

    "<{i}Окаемов молча жмет ей руку. Вера и Туманский выходят.{/i}>"

    hide okaemov
    hide vera
    hide tumanskij

    stop sound1

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    hide leonid

    show leonid at left
    show okaemov at right

    leonid "<{i}(ошеломленный, смотрит на Окаемова).{/i}>"

    hide okaemov

    show leonid at truecenter

    leonid "Боже мой! Что вы наделали! Я побегу к Маше, я скажу ей, все равно ее приведу!"

    hide leonid

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Не надо. Все сказано. Все понятно. До конца."

    okaemov "<{i}(Пауза.){/i}>"

    okaemov "Жизнь справедлива. За ошибки нужно платить. И я заплатил. Полной мерой последнего одиночества."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид"

    leonid "<{i}(после паузы).{/i}>"

    leonid "Может быть, я не понимаю всего, что произошло здесь."

    play sound1 footsteps

    hide leonid

    show leonid at left
    show okaemov at right

    leonid "<{i}(Подошел к Окаемову.){/i}>"

    hide okaemov

    show leonid at truecenter

    stop sound1

    leonid "Я не знаю причин... Василий Иванович. Может быть, действительно надо было поступить так... Но все равно, вы не будете больше один."

    hide leonid

    show leonid at left
    show okaemov at right

    leonid "<{i}(Ласково обняв его за плечи.){/i}>"

    hide okaemov

    show leonid at truecenter

    leonid "Слишком многое изменилось в вашей жизни. Вы уже не сможете жить без тех, кто пришел в дом вместе с Машей... и остались с вами, несмотря на ее уход. Маленькая Маша ждет своего деда... А товарищи большой Машеньки — ваши друзья."

    hide leonid

    play sound1 footsteps

    show okaemov at left
    show leonid at truecenter
    show masha at right

    "<{i}Окаемов молча жмет руку Леониду и отходит к окну, где стоят цветы. Он садится на стул, где сидела Маша. В переднюю тихо входит Маша.{/i}>"

    hide okaemov
    hide leonid
    hide masha

    stop sound1

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Дедушка... у тебя сегодня лекция. В пять часов."

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Машенька!.."

    hide okaemov

    show masha at truecenter

    $ masha_var = "{noalt}Маша."

    masha "Я от тебя не уеду — никогда... дедушка. Но мама моя — тоже... мало что раньше было... сколько лет прошло... За что же теперь не любить? Она же тебя совсем не знает, какой ты. Ты должен так сделать, дедушка, чтобы мама с нами жила. Должен, правда?"

    hide masha

    show okaemov at truecenter

    $ okaemov_var = "{noalt}Окаемов."

    okaemov "Правда, внучка... Я сам думал об этом... Много думал эти дни... Да-а, сорок лет я читаю лекции. И сегодня пойду. Только сегодня я буду говорить не о пергаментах. Почти три четверти века я хожу по земле. Пятьдесят лет я изучал пергаменты и свитки..."

    okaemov "А теперь другая наука волнует и привлекает меня — нетронутая, нераскрытая... потому что она даже и не считалась наукой... Наука о родителях. Да-с..."

    okaemov "Вот я, профессор, интеллигент, всегда считавший себя прекрасным отцом, я испортил жизнь сыну, как самый неграмотный невежда... Я стучал кулаком по дорогому роялю и всю жизнь был убежден, что играю на нем... Откуда взялось у меня подобное самомнение?.."

    okaemov "Свои пергаменты я изучал годами — это было моей профессией... Но никогда до сего дня не задумался я над тем, что быть отцом или матерью — это тоже профессия, да-да, вторая профессия каждого, у кого есть дети..."

    okaemov "И эта вторая профессия есть искусство воспитания нового поколения граждан... Я знаю, усмехнутся, но я скажу — я, как гражданин, скажу и заставлю слушателей моих задуматься — они ведь сами родители или будут ими. Вот-с."

    okaemov "И пусть они не ссылаются, что общество детей воспитает. Государство... Мы слишком часто сваливаем все на государство. Это же гораздо легче, чем думать и заботиться самому. Да-с! Вот о чем я сегодня прочитаю лекцию..."

    hide okaemov

    show leonid at truecenter

    $ leonid_var = "{noalt}Леонид."

    leonid "Необыкновенной силы лекция!"

    hide leonid

    "<{i}Занавес{/i}>"


