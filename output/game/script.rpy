"Emilia Galotti"

"Ein Trauerspiel in fünf Aufzügen"

"Gotthold"

"Ephraim"

"Lessing"

"Q34628"

"118572121"

"DraCor"

"https://dracor.org"

"CC0 1.0"

"Licence"

"TextGrid Repository"

"http://www.textgridrep.org/textgrid:rksp.0"

"<{i}CC-BY-3.0{/i}>"

"<{i}Lizenzvertrag{/i}>"

"<{i}Gotthold Ephraim Lessing: Werke. Herausgegeben von Herbert G. Göpfert in Zusammenarbeit mit Karl Eibl, Helmut Göbel, Karl S. Guthke, Gerd Hillen, Albert von Schirmding und Jörg Schönert, Band 1–8, München: Hanser, 1970 ff.{/i}>"

define der_prinz = Character("der_prinz_var", color="#FFB300", dynamic=True)
define der_kammerdiener = Character("der_kammerdiener_var", color="#803E75", dynamic=True)
define conti = Character("conti_var", color="#FF6800", dynamic=True)
define marinelli = Character("marinelli_var", color="#A6BDD7", dynamic=True)
define camillo_rota = Character("camillo_rota_var", color="#C10020", dynamic=True)
define pirro = Character("pirro_var", color="#CEA262", dynamic=True)
define odoardo = Character("odoardo_var", color="#817066", dynamic=True)
define angelo = Character("angelo_var", color="#007D34", dynamic=True)
define appiani = Character("appiani_var", color="#F6768E", dynamic=True)
define battista = Character("battista_var", color="#00538A", dynamic=True)
define claudia = Character("claudia_var", color="#FF7A5C", dynamic=True)
define emilia = Character("emilia_var", color="#53377A", dynamic=True)
define orsina = Character("orsina_var", color="#FF8E00", dynamic=True)

"Tragedy"

"Q80930"

"(dlina) file conversion from source"

"(ff) structural cleanup"

"(ff) unify IDs; formalities"

"(ff) formalities"

label start:
    play music "audio/music/18.mp3" fadeout 1.0 fadein 1.0

    "Gotthold Ephraim Lessing"

    "Emilia Galotti"

    "Ein Trauerspiel in fünf Aufzügen"

    menu:
        "{color=#000}Personen.{/color}":
            jump Characters_1
        "{color=#000}Erster Aufzug{/color}":
            jump Act_1
        "{color=#000}Zweiter Aufzug{/color}":
            jump Act_2
        "{color=#000}Dritter Aufzug{/color}":
            jump Act_3
        "{color=#000}Vierter Aufzug{/color}":
            jump Act_4
        "{color=#000}Fünfter Aufzug{/color}":
            jump Act_5

    label Characters_1:
        play music "audio/music/44.mp3" fadeout 1.0 fadein 1.0

        "{b}Personen.{/b}"

        show emilia at truecenter
        "Emilia Galotti."
        hide emilia

        show odoardo at truecenter
        "Odoardo,"
        hide odoardo

        show claudia at truecenter
        "Claudia Galotti,"
        hide claudia

        "Eltern der Emilia."

        "Hettore Gonzaga,"

        "Prinz von Guastalla."

        show marinelli at truecenter
        "Marinelli,"
        hide marinelli

        "Kammerherr des Prinzen."

        show camillo_rota at truecenter
        "Camillo Rota,"
        hide camillo_rota

        "einer von des Prinzen Räten."

        show conti at truecenter
        "Conti,"
        hide conti

        "Maler."

        show appiani at truecenter
        "Graf Appiani."
        hide appiani

        show orsina at truecenter
        "Gräfin Orsina."
        hide orsina

        show angelo at truecenter
        "Angelo,"
        hide angelo

        "einige Bediente."


label Act_1:
    play music "audio/music/72.mp3" fadeout 1.0 fadein 1.0

    scene 1 with fade

    "{b}Erster Aufzug{/b}"

    "<{i}Die Szene, ein Kabinett des Prinzen.{/i}>"

    menu:
        "{color=#000}Erster Auftritt{/color}":
            jump Act_0_Scene_1
        "{color=#000}Zweiter Auftritt{/color}":
            jump Act_0_Scene_2
        "{color=#000}Dritter Auftritt{/color}":
            jump Act_0_Scene_3
        "{color=#000}Vierter Auftritt{/color}":
            jump Act_0_Scene_4
        "{color=#000}Fünfter Auftritt{/color}":
            jump Act_0_Scene_5
        "{color=#000}Sechster Auftritt{/color}":
            jump Act_0_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_0_Scene_6_1

label Further_Act_0_Scene_6_1:
    menu:
        "{color=#000}Siebenter Auftritt{/color}":
            jump Act_0_Scene_7
        "{color=#000}Achter Auftritt{/color}":
            jump Act_0_Scene_8

    label Act_0_Scene_1:
        "{b}Erster Auftritt{/b}"

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}an einem Arbeitstische, voller Briefschaften und Papiere, deren einige er durchläuft.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Klagen, nichts als Klagen! Bittschriften, nichts als Bittschriften! – Die traurigen Geschäfte; und man beneidet uns noch! – Das glaub' ich; wenn wir allen helfen könnten: dann wären wir zu beneiden. – Emilia?"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Indem er noch eine von den Bittschriften aufschlägt, und nach dem unterschriebnen Namen sieht.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Eine Emilia? – Aber eine Emilia Bruneschi – nicht Galotti. Nicht Emilia Galotti! – Was will sie, diese Emilia Bruneschi?"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Er lieset.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Viel gefodert; sehr viel. – Doch sie heißt Emilia. Gewährt!"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Er unterschreibt und klingelt; worauf ein Kammerdiener hereintritt.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Es ist wohl noch keiner von den Räten in dem Vorzimmer?"

        hide der_prinz

        show der_kammerdiener at truecenter

        $ der_kammerdiener_var = "{noalt}DER KAMMERDIENER."

        der_kammerdiener "Nein."

        hide der_kammerdiener

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich habe zu früh Tag gemacht. – Der Morgen ist so schön. Ich will ausfahren. Marchese Marinelli soll mich begleiten. Laßt ihn rufen."

        hide der_prinz

        show der_prinz at left
        show der_kammerdiener at right

        hide der_prinz

        show der_prinz at left
        show der_kammerdiener at right

        der_prinz "<{i}Der Kammerdiener geht ab.{/i}>"

        hide der_kammerdiener

        show der_prinz at truecenter

        hide der_kammerdiener

        show der_prinz at truecenter

        der_prinz "– Ich kann doch nicht mehr arbeiten. – Ich war so ruhig, bild' ich mir ein, so ruhig – Auf einmal muß eine arme Bruneschi, Emilia heißen; – weg ist meine Ruhe, und alles! –"

        hide der_prinz

        show der_kammerdiener at truecenter

        $ der_kammerdiener_var = "{noalt}DER KAMMERDIENER"

        hide der_kammerdiener

        show der_kammerdiener at truecenter

        hide der_kammerdiener

        show der_kammerdiener at truecenter

        der_kammerdiener "<{i}welcher wieder herein tritt.{/i}>"

        show der_kammerdiener at truecenter

        show der_kammerdiener at truecenter

        der_kammerdiener "Nach dem Marchese ist geschickt. Und hier, ein Brief von der Gräfin Orsina."

        hide der_kammerdiener

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Der Orsina? Legt ihn hin."

        hide der_prinz

        show der_kammerdiener at truecenter

        $ der_kammerdiener_var = "{noalt}DER KAMMERDIENER."

        der_kammerdiener "Ihr Läufer wartet."

        hide der_kammerdiener

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich will die Antwort senden; wenn es einer bedarf. – Wo ist sie? In der Stadt? oder auf ihrer Villa?"

        hide der_prinz

        show der_kammerdiener at truecenter

        $ der_kammerdiener_var = "{noalt}DER KAMMERDIENER."

        der_kammerdiener "Sie ist gestern in die Stadt gekommen."

        hide der_kammerdiener

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Desto schlimmer – besser; wollt' ich sagen. So braucht der Läufer um so weniger zu warten."

        hide der_prinz

        show der_prinz at left
        show der_kammerdiener at right

        hide der_prinz

        show der_prinz at left
        show der_kammerdiener at right

        der_prinz "<{i}Der Kammerdiener geht ab.{/i}>"

        hide der_kammerdiener

        show der_prinz at truecenter

        hide der_kammerdiener

        show der_prinz at truecenter

        der_prinz "Meine teure Gräfin!"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Bitter, indem er den Brief in die Hand nimmt.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "So gut, als gelesen!"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Und ihn wieder wegwirft.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "– Nun ja; ich habe sie zu lieben geglaubt! Was glaubt man nicht alles? Kann sein, ich habe sie auch wirklich geliebt. Aber – ich habe!"

        hide der_prinz

        show der_kammerdiener at truecenter

        $ der_kammerdiener_var = "{noalt}DER KAMMERDIENER"

        hide der_kammerdiener

        show der_kammerdiener at truecenter

        hide der_kammerdiener

        show der_kammerdiener at truecenter

        der_kammerdiener "<{i}der nochmals herein tritt.{/i}>"

        show der_kammerdiener at truecenter

        show der_kammerdiener at truecenter

        der_kammerdiener "Der Maler Conti will die Gnade haben – –"

        hide der_kammerdiener

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Conti? Recht wohl; laßt ihn herein kommen. – Das wird mir andere Gedanken in den Kopf bringen. –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Steht auf.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        hide der_prinz

    label Act_0_Scene_2:
        "{b}Zweiter Auftritt{/b}"

        show conti at left
        show der_prinz at right

        show conti at left
        show der_prinz at right

        "<{i}Conti. Der Prinz.{/i}>"

        hide conti
        hide der_prinz

        hide conti
        hide der_prinz

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Guten Morgen, Conti. Wie leben Sie? Was macht die Kunst?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Prinz, die Kunst geht nach Brot."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Das muß sie nicht; das soll sie nicht, – in meinem kleinen Gebiete gewiß nicht. – Aber der Künstler muß auch arbeiten wollen."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Arbeiten? Das ist seine Lust. Nur zu viel arbeiten müssen, kann ihn um den Namen Künstler bringen."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich meine nicht vieles; sondern viel: ein weniges; aber mit Fleiß. – Sie kommen doch nicht leer, Conti?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Ich bringe das Porträt, welches Sie mir befohlen haben, gnädiger Herr. Und bringe noch eines, welches Sie mir nicht befohlen: aber weil es gesehen zu werden verdienet –"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Jenes ist? – Kann ich mich doch kaum erinnern –"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Die Gräfin Orsina."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wahr! – Der Auftrag ist nur ein wenig von lange her."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Unsere schönen Damen sind nicht alle Tage zum Malen."

        conti "Die Gräfin hat, seit drei Monaten, gerade Einmal sich entschließen können, zu sitzen."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wo sind die Stücke?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "In dem Vorzimmer: ich hole sie."

        hide conti

    label Act_0_Scene_3:
        "{b}Dritter Auftritt{/b}"

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ihr Bild! – mag! – Ihr Bild, ist sie doch nicht selber. – Und vielleicht find' ich in dem Bilde wieder, was ich in der Person nicht mehr erblicke. – Ich will es aber nicht wiederfinden. – Der beschwerliche Maler! Ich glaube gar, sie hat ihn bestochen."

        der_prinz "– Wär' es auch! Wenn ihr ein anderes Bild, das mit andern Farben, auf einen andern Grund gemalet ist, – in meinem Herzen wieder Platz machen will: – Wahrlich, ich glaube, ich wär' es zufrieden."

        der_prinz "Als ich dort liebte, war ich immer so leicht, so fröhlich, so ausgelassen. – Nun bin ich von allem das Gegenteil. – Doch nein; nein, nein! Behäglicher, oder nicht behäglicher: ich bin so besser."

        hide der_prinz

    label Act_0_Scene_4:
        "{b}Vierter Auftritt{/b}"

        show der_prinz at left
        show conti at right

        show der_prinz at left
        show conti at right

        "<{i}Der Prinz. Conti, mit den Gemälden, wovon er das eine verwandt gegen einen Stuhl lehnet.{/i}>"

        hide der_prinz
        hide conti

        hide der_prinz
        hide conti

        show conti at truecenter

        $ conti_var = "{noalt}CONTI"

        hide conti

        show conti at truecenter

        hide conti

        show conti at truecenter

        conti "<{i}indem er das andere zurecht stellet.{/i}>"

        show conti at truecenter

        show conti at truecenter

        conti "Ich bitte, Prinz, daß Sie die Schranken unserer Kunst erwägen wollen. Vieles von dem Anzüglichsten der Schönheit liegt ganz außer den Grenzen derselben. – Treten Sie so! –"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}nach einer kurzen Betrachtung.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Vortrefflich, Conti; – ganz vortrefflich! – Das gilt Ihrer Kunst, Ihrem Pinsel. – Aber geschmeichelt, Conti; ganz unendlich geschmeichelt!"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Das Original schien dieser Meinung nicht zu sein. Auch ist es in der Tat nicht mehr geschmeichelt, als die Kunst schmeicheln muß. Die Kunst muß malen, wie sich die plastische"

        conti "Natur, – wenn es eine gibt – das Bild dachte: ohne den Abfall, welchen der widerstrebende Stoff unvermeidlich macht; ohne das Verderb, mit welchem die Zeit dagegen an kämpfet."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Der denkende Künstler ist noch eins so viel wert. – Aber das Original, sagen Sie, fand dem ungeachtet –"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Verzeihen Sie, Prinz. Das Original ist eine Person, die meine Ehrerbietung fodert. Ich habe nichts Nachteiliges von ihr äußern wollen."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So viel als Ihnen beliebt! – Und was sagte das Original?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Ich bin zufrieden, sagte die Gräfin, wenn ich nicht häßlicher aussehe."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Nicht häßlicher? – O das wahre Original!"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Und mit einer Miene sagte sie das, – von der freilich dieses ihr Bild keine Spur, keinen Verdacht zeiget."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Das meint' ich ja; das ist es eben, worin ich die unendliche Schmeichelei finde. – O! ich kenne sie, jene stolze höhnische Miene, die auch das Gesicht einer Grazie entstellen würde!"

        der_prinz "– Ich leugne nicht, daß ein schöner Mund, der sich ein wenig spöttisch verziehet, nicht selten um so viel schöner ist. Aber, wohl gemerkt, ein wenig: die Verziehung muß nicht bis zur Grimasse gehen, wie bei dieser Gräfin."

        der_prinz "Und Augen müssen über den wollüstigen Spötter die Aufsicht führen, – Augen, wie sie die gute Gräfin nun gerade gar nicht hat. Auch nicht einmal hier im Bilde hat."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Gnädiger Herr, ich bin äußerst betroffen –"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und worüber? Alles, was die Kunst aus den großen, hervorragenden, stieren, starren Medusenaugen der Gräfin Gutes machen kann, das haben Sie, Conti, redlich daraus gemacht. – Redlich, sag' ich? – Nicht so redlich, wäre redlicher."

        der_prinz "Denn sagen Sie selbst, Conti, läßt sich aus diesem Bilde wohl der Charakter der Person schließen? Und das sollte doch. Stolz haben Sie in Würde, Hohn in Lächeln, Ansatz zu trübsinniger Schwärmerei in sanfte Schwermut verwandelt."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI"

        hide conti

        show conti at truecenter

        hide conti

        show conti at truecenter

        conti "<{i}etwas ärgerlich.{/i}>"

        show conti at truecenter

        show conti at truecenter

        conti "Ah, mein Prinz, – wir Maler rechnen darauf, daß das fertige Bild den Liebhaber noch eben so warm"

        conti "findet, als warm er es bestellte. Wir malen mit Augen der Liebe: und Augen der Liebe müßten uns auch nur beurteilen."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Je nun, Conti; – warum kamen Sie nicht einen Monat früher damit? – Setzen Sie weg. – Was ist das andere Stück?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI"

        hide conti

        show conti at truecenter

        hide conti

        show conti at truecenter

        conti "<{i}indem er es holt, und noch verkehrt in der Hand hält.{/i}>"

        show conti at truecenter

        show conti at truecenter

        conti "Auch ein weibliches Porträt."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So möcht' ich es bald – lieber gar nicht sehen. Denn dem Ideal hier,"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Mit dem Finger auf die Stirne.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "– oder vielmehr hier,"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Mit dem Finger auf das Herz.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "kömmt es doch nicht bei. – Ich wünschte, Conti, Ihre Kunst in andern Vorwürfen zu bewundern."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Eine bewundernswürdigere Kunst gibt es; aber sicherlich keinen bewundernswürdigern Gegenstand, als diesen."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So wett' ich, Conti, daß es des Künstlers eigene Gebieterin ist. –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Indem der Maler das Bild umwendet.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Was seh' ich? Ihr Werk, Conti? oder das Werk meiner Phantasie? – Emilia Galotti!"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Wie, mein Prinz? Sie kennen diesen Engel?"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}indem er sich zu fassen sucht, aber ohne ein Auge von dem Bilde zu verwenden.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "So halb! – um sie eben wieder zu kennen. – Es ist einige Wochen her, als ich sie mit ihrer Mutter in einer Vegghia traf. – Nachher ist sie mir nur an heiligen Stätten wieder vorgekommen, – wo das Angaffen sich weniger ziemet. – Auch kenn' ich ihren Vater."

        der_prinz "Er ist mein Freund nicht. Er war es, der sich meinen Ansprüchen auf Sabionetta am meisten widersetzte. – Ein alter Degen; stolz und rauh; sonst bieder und gut! –"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Der Vater! Aber hier haben wir seine Tochter. –"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Bei Gott! wie aus dem Spiegel gestohlen!"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Noch immer die Augen auf das Bild geheftet.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "O, Sie wissen es ja wohl, Conti, daß man den Künstler dann erst recht lobt, wenn man über sein Werk sein Lob vergißt."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Gleichwohl hat mich dieses noch sehr unzufrieden mit mir gelassen. – Und doch bin ich wiederum sehr zufrieden mit meiner Unzufriedenheit mit mir selbst. – Ha! daß wir nicht unmittelbar mit den Augen malen!"

        conti "Auf dem langen Wege, aus dem Auge durch den Arm in den Pinsel, wie viel"

        conti "geht da verloren! – Aber, wie ich sage, daß ich es weiß, was hier verloren gegangen, und wie es verloren gegangen, und warum es verloren gehen müssen: darauf bin ich eben so stolz, und stolzer, als ich auf alles das bin, was ich nicht verloren gehen lassen."

        conti "Denn aus jenem erkenne ich, mehr als aus diesem, daß ich wirklich ein großer Maler bin; daß es aber meine Hand nur nicht immer ist."

        conti "– Oder meinen Sie, Prinz, daß Raphael nicht das größte malerische Genie gewesen wäre, wenn er unglücklicher Weise ohne Hände wäre geboren worden? Meinen Sie, Prinz?"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}indem er nur eben von dem Bilde wegblickt.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Was sagen Sie, Conti? Was wollen Sie wissen?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "O nichts, nichts! – Plauderei! Ihre Seele, merk' ich, war ganz in Ihren Augen. Ich liebe solche Seelen, und solche Augen."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}mit einer erzwungenen Kälte.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Also, Conti, rechnen Sie doch wirklich Emilia Galotti mit zu den vorzüglichsten Schönheiten unserer Stadt?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Also? mit? mit zu den vorzüglichsten? und den vorzüglichsten unserer Stadt? – Sie spotten meiner, Prinz. Oder Sie sahen, die ganze Zeit, eben so wenig, als Sie hörten."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Lieber Conti, –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Die Augen wieder auf das Bild gerichtet.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "wie darf unser einer seinen Augen trauen? Eigentlich weiß doch nur allein ein Maler von der Schönheit zu urteilen."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Und eines jeden Empfindung sollte erst auf den Ausspruch eines Malers warten? – Ins Kloster mit dem, der es von uns lernen will, was schön ist!"

        conti "Aber das muß ich Ihnen doch als Maler sagen, mein Prinz: eine von den größten Glückseligkeiten meines Lebens ist es, daß Emilia Galotti mir gesessen."

        conti "Dieser Kopf, dieses Antlitz, diese Stirn, diese Augen, diese Nase, dieser Mund, dieses Kinn, dieser Hals, diese Brust, dieser Wuchs, dieser ganze Bau, sind, von der Zeit an, mein einziges Studium der weiblichen Schönheit."

        conti "– Die Schilderei selbst, wovor sie gesessen, hat ihr abwesender Vater bekommen. Aber diese Kopie –"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}der sich schnell gegen ihn kehret.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Nun, Conti? ist doch nicht schon versagt?"

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Ist für Sie, Prinz; wenn Sie Geschmack daran finden."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Geschmack! –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Lächelnd.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Dieses Ihr Studium der weiblichen Schönheit, Conti, wie könnt' ich besser tun, als es auch zu dem meinigen zu machen? – Dort, jenes Porträt nehmen Sie nur wieder mit, – einen Rahmen darum zu bestellen."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Wohl!"

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So schön, so reich, als ihn der Schnitzer nur machen kann. Es soll in der Galerie aufgestellet werden. – Aber dieses, bleibt hier. Mit einem Studio macht man so viel Umstände nicht: auch läßt man das nicht aufhängen; sondern hat es gern bei der Hand."

        der_prinz "– Ich danke Ihnen, Conti; ich danke Ihnen recht sehr. – Und wie gesagt: in meinem Gebiete soll die Kunst nicht nach Brot gehen; – bis ich selbst keines habe."

        der_prinz "– Schicken Sie, Conti, zu meinem Schatzmeister, und lassen Sie, auf Ihre Quittung, für beide Porträte sich bezahlen, – was Sie wollen. So viel Sie wollen, Conti."

        hide der_prinz

        show conti at truecenter

        $ conti_var = "{noalt}CONTI."

        conti "Sollte ich doch nun bald fürchten, Prinz, daß Sie so, noch etwas anders belohnen wollen, als die Kunst."

        hide conti

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "O des eifersüchtigen Künstlers! Nicht doch! – Hören Sie, Conti; so viel Sie wollen."

        hide der_prinz

        show der_prinz at left
        show conti at right

        hide der_prinz

        show der_prinz at left
        show conti at right

        der_prinz "<{i}Conti geht ab.{/i}>"

        hide conti

        show der_prinz at truecenter

        hide conti

        show der_prinz at truecenter

        hide der_prinz

    label Act_0_Scene_5:
        "{b}Fünfter Auftritt{/b}"

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So viel er will! –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Gegen das Bild.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Dich hab' ich für jeden Preis noch zu wohlfeil. – Ah! schönes Werk der Kunst, ist es wahr, daß ich dich besitze? – Wer dich auch besäße, schönres Meisterstück der Natur! – Was Sie dafür wollen, ehrliche Mutter! Was du willst, alter Murrkopf! Fodre nur! Fodert nur !"

        der_prinz "– Am liebsten kauft' ich dich, Zauberin, von dir selbst! – Dieses Auge voll Liebreiz und Bescheidenheit! Dieser Mund! und wenn er sich zum Reden öffnet! wenn er lächelt! Dieser Mund! – Ich höre kommen. – Noch bin ich mit dir zu neidisch."

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Indem er das Bild gegen die Wand kehret.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Es wird Marinelli sein. Hätt' ich ihn doch nicht rufen lassen! Was für einen Morgen könnt' ich haben!"

        hide der_prinz

    label Act_0_Scene_6:
        "{b}Sechster Auftritt{/b}"

        show marinelli at left
        show der_prinz at right

        show marinelli at left
        show der_prinz at right

        "<{i}Marinelli. Der Prinz.{/i}>"

        hide marinelli
        hide der_prinz

        hide marinelli
        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Gnädiger Herr, Sie werden verzeihen. – Ich war mir eines so frühen Befehls nicht gewärtig."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich bekam Lust, auszufahren. Der Morgen war so schön. – Aber nun ist er ja wohl verstrichen; und die Lust ist mir vergangen. –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Nach einem kurzen Stillschweigen.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Was haben wir Neues, Marinelli?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nichts von Belang, das ich wüßte. – Die Gräfin Orsina ist gestern zur Stadt gekommen."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Hier liegt auch schon ihr guter Morgen,"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Auf ihren Brief zeigend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "oder was es sonst sein mag! Ich bin gar nicht neugierig darauf. – Sie haben sie gesprochen?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Bin ich, leider, nicht ihr Vertrauter? – Aber, wenn ich es wieder von einer Dame werde, der es einkömmt, Sie in gutem Ernste zu lieben, Prinz: so – –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Nichts verschworen, Marinelli!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ja? In der Tat, Prinz? Könnt' es doch kommen? – O! so mag die Gräfin auch so Unrecht nicht haben."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Allerdings, sehr Unrecht! – Meine nahe Vermählung mit der Prinzessin von Massa, will durchaus, daß ich alle dergleichen Händel fürs erste abbreche."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn es nur das wäre: so müßte freilich Orsina sich in ihr Schicksal eben so wohl zu finden wissen, als der Prinz in seines."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Das unstreitig härter ist, als ihres. Mein Herz wird das Opfer eines elenden Staatsinteresse. Ihres darf sie nur zurücknehmen; aber nicht wider Willen verschenken."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Zurücknehmen? Warum zurücknehmen? fragt die Gräfin: wenn es weiter nichts, als eine Gemahlin ist, die dem Prinzen nicht die Liebe, sondern die Politik zuführet? Neben so einer Gemahlin sieht die Geliebte noch immer ihren Platz."

        marinelli "Nicht so einer Gemahlin fürchtet sie aufgeopfert zu sein, sondern – –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Einer neuen Geliebten. – Nun denn? Wollten Sie mir daraus ein Verbrechen machen, Marinelli?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich? – O! vermengen Sie mich ja nicht, mein Prinz, mit der Närrin, deren Wort ich führe, – aus Mitleid führe. Denn gestern, wahrlich, hat sie mich sonderbar gerühret. Sie wollte von ihrer Angelegenheit mit Ihnen gar nicht sprechen."

        marinelli "Sie wollte sich ganz gelassen und kalt stellen. Aber mitten in dem gleichgültigsten Gespräche, entfuhr ihr eine Wendung, eine Beziehung über die andere, die ihr gefoltertes Herz verriet."

        marinelli "Mit dem lustigsten Wesen sagte sie die melancholischsten Dinge: und wiederum die lächerlichsten Possen mit der allertraurigsten Miene. Sie hat zu den Büchern ihre Zuflucht genommen; und ich fürchte, die werden ihr den Rest geben."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So wie sie ihrem armen Verstande auch den ersten Stoß gegeben. – Aber was mich vornehmlich mit von ihr entfernt hat, das wollen Sie doch nicht brauchen, Marinelli, mich wieder zu ihr zurück zu bringen?"

        der_prinz "– Wenn sie aus Liebe närrisch wird, so wäre sie es, früher oder später, auch ohne Liebe geworden – Und nun, genug von ihr. – Von etwas anderm! – Geht denn gar nichts vor, in der Stadt? –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "So gut, wie gar nichts. – Denn daß die Verbindung des Grafen Appiani heute vollzogen wird, – ist nicht viel mehr, als gar nichts."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Des Grafen Appiani? und mit wem denn? – Ich soll ja noch hören, daß er versprochen ist."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Die Sache ist sehr geheim gehalten worden. Auch war nicht viel Aufhebens davon zu machen. – Sie werden lachen, Prinz. – Aber so geht es den Empfindsamen! Die Liebe spielet ihnen immer die schlimmsten Streiche."

        marinelli "Ein Mädchen ohne Vermögen und ohne Rang, hat ihn in ihre Schlinge zu ziehen gewußt, – mit ein wenig Larve; aber mit vielem Prunke von Tugend und Gefühl und Witz, – und was weiß ich?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wer sich den Eindrücken, die Unschuld und Schönheit auf ihn machen, ohne weitere Rücksicht, so ganz überlassen darf; – ich dächte, der wär' eher zu beneiden, als zu belachen. – Und wie heißt denn die Glückliche?"

        der_prinz "– Denn bei alle dem ist Appiani – ich weiß wohl, daß Sie, Marinelli, ihn nicht leiden können; eben so wenig als er Sie – bei alle dem"

        der_prinz "ist er doch ein sehr würdiger junger Mann, ein schöner Mann, ein reicher Mann, ein Mann voller Ehre. Ich hätte sehr gewünscht, ihn mir verbinden zu können. Ich werde noch darauf denken."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn es nicht zu spät ist. – Denn so viel ich höre, ist sein Plan gar nicht, bei Hofe sein Glück zu machen. – Er will mit seiner Gebieterin nach seinen Tälern von Piemont: – Gemsen zu jagen, auf den Alpen; und Murmeltiere abzurichten. – Was kann er Beßres tun?"

        marinelli "Hier ist es durch das Mißbündnis, welches er trifft, mit ihm doch aus. Der Zirkel der ersten Häuser ist ihm von nun an verschlossen – –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Mit euern ersten Häusern! – in welchen das Zeremoniell, der Zwang, die Langeweile, und nicht selten die Dürftigkeit herrschet. – Aber so nennen Sie mir sie doch, der er dieses so große Opfer bringt."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Es ist eine gewisse Emilia Galotti."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wie, Marinelli? eine gewisse –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Emilia Galotti."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Emilia Galotti? – Nimmermehr!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Zuverlässig, gnädiger Herr."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Nein, sag ich; das ist nicht, das kann nicht sein. – Sie irren sich in dem Namen. – Das Geschlecht der Galotti ist groß. – Eine Galotti kann es sein; aber nicht Emilia Galotti; nicht Emilia!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Emilia – Emilia Galotti!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So gibt es noch eine, die beide Namen führt. – Sie sagten ohnedem, eine gewisse Emilia Galotti – eine gewisse. Von der rechten könnte nur ein Narr so sprechen –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie sind außer sich, gnädiger Herr. – Kennen Sie denn diese Emilia?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich habe zu fragen, Marinelli, nicht Er. – Emilia Galotti? Die Tochter des Obersten Galotti, bei Sabionetta?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Eben die."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Die hier in Guastalla mit ihrer Mutter wohnet?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Eben die."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Unfern der Kirche Allerheiligen?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Eben die."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Mit einem Worte –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Indem er nach dem Porträte{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        der_prinz "<{i}springt und es dem Marinelli in die Hand gibt.{/i}>"

        hide marinelli

        show der_prinz at truecenter

        hide marinelli

        show der_prinz at truecenter

        der_prinz "springt und es dem Marinelli in die Hand gibt."

        der_prinz "Da! – Diese? Diese Emilia Galotti? – Sprich dein verdammtes »Eben die« noch einmal, und stoß mir den Dolch ins Herz!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Eben die."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Henker! – Diese? – Diese Emilia Galotti wird heute – –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Gräfin Appiani! –"

        hide marinelli

        show marinelli at left
        show der_prinz at right

        hide marinelli

        show marinelli at left
        show der_prinz at right

        marinelli "<{i}Hier reißt der Prinz dem Marinelli das Bild wieder aus der Hand, und wirft es bei Seite.{/i}>"

        hide der_prinz

        show marinelli at truecenter

        hide der_prinz

        show marinelli at truecenter

        marinelli "Die Trauung geschieht in der Stille, auf dem Landgute des Vaters bei Sabionetta. Gegen Mittag fahren Mutter und Tochter, der Graf und vielleicht ein paar Freunde dahin ab."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}der sich voll Verzweiflung in einen Stuhl wirft.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "So bin ich verloren! – So will ich nicht leben!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Aber was ist Ihnen, gnädiger Herr?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}der gegen ihn wieder aufspringt.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Verräter! – was mir ist? – Nun ja ich liebe sie; ich bete sie an. Mögt ihr es doch wissen! mögt ihr es doch längst gewußt haben, alle ihr, denen ich der tollen Orsina schimpfliche Fesseln lieber ewig tragen sollte!"

        der_prinz "– Nur daß Sie, Marinelli, der Sie so oft mich Ihrer innigsten Freundschaft versicherten – O ein Fürst hat keinen Freund! kann keinen Freund haben!"

        der_prinz "– daß Sie, Sie, so treulos, so hämisch mir bis auf diesen Augenblick die Gefahr verhöhlen dürfen, die meiner Liebe drohte: wenn ich Ihnen jemals das vergebe, – so werde mir meiner Sünden keine vergeben!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich weiß kaum Worte zu finden, Prinz, – wenn Sie mich auch dazu kommen ließen – Ihnen mein Erstaunen zu bezeigen. – Sie lieben Emilia Galotti? – Schwur dann gegen Schwur: Wenn ich von dieser Liebe das geringste gewußt, das geringste vermutet habe;"

        marinelli "so möge weder Engel noch Heiliger von mir wissen! – Eben das wollt' ich in die Seele der Orsina schwören. Ihr Verdacht schweift auf einer ganz andern Fährte."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So verzeihen Sie mir, Marinelli; –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Indem er sich ihm in die Arme wirft.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "und betauern Sie mich."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun da, Prinz! Erkennen Sie da die Frucht Ihrer Zurückhaltung! – »Fürsten haben keinen Freund! können keinen Freund haben!« – Und die Ursache, wenn dem so"

        marinelli "ist? – Weil sie keinen haben wollen. – Heute beehren sie uns mit ihrem Vertrauen, teilen uns ihre geheimsten Wünsche mit, schließen uns ihre ganze Seele auf: und morgen sind wir ihnen wieder so fremd, als hätten sie nie ein Wort mit uns gewechselt."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ach! Marinelli, wie konnt' ich Ihnen vertrauen, was ich mir selbst kaum gestehen woll te?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und also wohl noch weniger der Urheberin Ihrer Qual gestanden haben?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ihr? – Alle meine Mühe ist vergebens gewesen, sie ein zweitesmal zu sprechen. –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und das erstemal –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sprach ich sie – O, ich komme von Sinnen! Und ich soll Ihnen noch lange erzählen? – Sie sehen mich einen Raub der Wellen: was fragen sie viel, wie ich es geworden? Retten Sie mich, wenn Sie können: und fragen Sie dann."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Retten? ist da viel zu retten? – Was Sie versäumt haben, gnädiger Herr, der Emilia Galotti zu bekennen, das bekennen Sie nun der Gräfin Appiani. Waren, die man aus der ersten Hand nicht haben kann, kauft man aus der zweiten;"

        marinelli "– und solche Waren nicht selten aus der zweiten um so viel wohlfeiler."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ernsthaft, Marinelli, ernsthaft, oder –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Freilich, auch um so viel schlechter –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sie werden unverschämt!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und dazu will der Graf damit aus dem Lande. – Ja, so müßte man auf etwas anders denken. –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und auf was? – Liebster, bester Marinelli, denken Sie für mich. Was würden Sie tun, wenn Sie an meiner Stelle wären?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Vor allen Dingen, eine Kleinigkeit als eine Kleinigkeit ansehen; – und mir sagen, daß ich nicht vergebens sein wolle, was ich bin – Herr!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Schmeicheln Sie mir nicht mit einer Gewalt, von der ich hier keinen Gebrauch absehe. – Heute sagen Sie? schon heute?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Erst heute – soll es geschehen. Und nur geschehenen Dingen ist nicht zu raten. –"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Nach einer kurzen Überlegung.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Wollen Sie mir freie Hand lassen, Prinz? Wollen Sie alles genehmigen, was ich tue?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Alles, Marinelli, alles, was diesen Streich abwenden kann."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "So lassen Sie uns keine Zeit verlieren. – Aber bleiben Sie nicht in der Stadt. Fahren Sie sogleich nach Ihrem Lustschlosse, nach Dosalo. Der Weg nach Sabionetta geht da vorbei."

        marinelli "Wenn es mir nicht gelingt, den Grafen augenblicklich zu entfernen: so denk' ich – Doch, doch; ich glaube, er geht in diese Falle gewiß. Sie wollen ja, Prinz, wegen Ihrer Vermählung einen Gesandten nach Massa schicken? Lassen Sie den Grafen dieser Gesandte sein;"

        marinelli "mit dem Bedinge, daß er noch heute abreiset. – Verstehen Sie?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Vortrefflich! – Bringen Sie ihn zu mir heraus. Gehen Sie, eilen Sie. Ich werfe mich sogleich in den Wagen."

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        der_prinz "<{i}Marinelli geht ab.{/i}>"

        hide marinelli

        show der_prinz at truecenter

        hide marinelli

        show der_prinz at truecenter

        hide der_prinz

    label Act_0_Scene_7:
        "{b}Siebenter Auftritt{/b}"

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sogleich! sogleich! – Wo blieb es? –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Sich nach dem Porträte umsehend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Auf der Erde? das war zu arg!"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Indem er es aufhebt.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Doch betrachten? betrachten mag ich dich fürs erste nicht mehr. – Warum sollt' ich mir den Pfeil noch tiefer in die Wunde drücken?"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Setzt es bei Seite.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "– Geschmachtet, geseufzet hab' ich lange genung, – länger als ich gesollt hätte; aber nichts getan! und über die zärtliche Untätigkeit bei einem Haar' alles verloren! – Und wenn nun doch alles verloren wäre? Wenn Marinelli nichts ausrichtete?"

        der_prinz "– Warum will ich mich auch auf ihn allein verlassen? Es fällt mir ein, – um diese Stunde,"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Nach der Uhr sehend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "um diese nämliche Stunde pflegt das fromme Mädchen alle Morgen bei den Dominikanern die Messe zu hören. – Wie wenn ich sie da zu sprechen suchte? – Doch heute, heut' an ihrem Hochzeittage, – heute werden ihr andere Dinge am Herzen liegen, als die Messe."

        der_prinz "– Indes, wer weiß? – Es ist ein"

        der_prinz "Gang. –"

        der_prinz "Er klingelt, und indem er einige von den Papieren auf dem Tische hastig zusammen rafft, tritt der Kammerdiener herein."

        der_prinz "Laßt vorfahren! – Ist noch keiner von den Räten da?"

        hide der_prinz

        show der_kammerdiener at truecenter

        $ der_kammerdiener_var = "{noalt}DER KAMMERDIENER."

        der_kammerdiener "Camillo Rota."

        hide der_kammerdiener

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Er soll herein kommen."

        hide der_prinz

        show der_prinz at left
        show der_kammerdiener at right

        hide der_prinz

        show der_prinz at left
        show der_kammerdiener at right

        der_prinz "<{i}Der Kammerdiener geht ab.{/i}>"

        hide der_kammerdiener

        show der_prinz at truecenter

        hide der_kammerdiener

        show der_prinz at truecenter

        der_prinz "Nur aufhalten muß er mich nicht wollen. Dasmal nicht! – Ich stehe gern seinen Bedenklichkeiten ein andermal um so viel länger zu Diensten. – Da war ja noch die Bittschrift einer Emilia Bruneschi –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Sie suchend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Die ists. – Aber, gute Bruneschi, wo deine Vorsprecherin – –"

        hide der_prinz

    label Act_0_Scene_8:
        "{b}Achter Auftritt{/b}"

        show camillo_rota at left
        show der_prinz at right

        show camillo_rota at left
        show der_prinz at right

        "<{i}Camillo Rota, Schriften in der Hand. Der Prinz.{/i}>"

        hide camillo_rota
        hide der_prinz

        hide camillo_rota
        hide der_prinz

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Kommen Sie, Rota, kommen Sie. – Hier ist, was ich diesen Morgen erbrochen. Nicht viel Tröstliches! – Sie werden von selbst sehen, was darauf zu verfügen. – Nehmen Sie nur."

        hide der_prinz

        show camillo_rota at truecenter

        $ camillo_rota_var = "{noalt}CAMILLO ROTA."

        camillo_rota "Gut, gnädiger Herr."

        hide camillo_rota

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Noch ist hier eine Bittschrift einer Emilia Galot – – Bruneschi will ich sagen. – Ich habe meine Bewilligung zwar schon beigeschrieben. Aber doch – die Sache ist keine Kleinigkeit – Lassen Sie die Ausfertigung noch anstehen."

        der_prinz "– Oder auch nicht anstehen: wie Sie wollen."

        hide der_prinz

        show camillo_rota at truecenter

        $ camillo_rota_var = "{noalt}CAMILLO ROTA."

        camillo_rota "Nicht wie ich will, gnädiger Herr."

        hide camillo_rota

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Was ist sonst? Etwas zu unterschreiben?"

        hide der_prinz

        show camillo_rota at truecenter

        $ camillo_rota_var = "{noalt}CAMILLO ROTA."

        camillo_rota "Ein Todesurteil wäre zu unterschreiben."

        hide camillo_rota

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Recht gern. – Nur her! geschwind."

        hide der_prinz

        show camillo_rota at truecenter

        $ camillo_rota_var = "{noalt}CAMILLO ROTA"

        hide camillo_rota

        show camillo_rota at truecenter

        hide camillo_rota

        show camillo_rota at truecenter

        camillo_rota "<{i}stutzig und den Prinzen starr ansehend.{/i}>"

        show camillo_rota at truecenter

        show camillo_rota at truecenter

        camillo_rota "Ein Todesurteil, sagt' ich."

        hide camillo_rota

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich höre ja wohl. – Es könnte schon geschehen sein. Ich bin eilig."

        hide der_prinz

        show camillo_rota at truecenter

        $ camillo_rota_var = "{noalt}CAMILLO ROTA"

        hide camillo_rota

        show camillo_rota at truecenter

        hide camillo_rota

        show camillo_rota at truecenter

        camillo_rota "<{i}seine Schriften nachsehend.{/i}>"

        show camillo_rota at truecenter

        show camillo_rota at truecenter

        camillo_rota "Nun hab' ich es doch wohl nicht mitgenommen! – – Verzeihen Sie, gnädiger Herr. – Es kann Anstand damit haben bis morgen."

        hide camillo_rota

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Auch das! – Packen Sie nur zusammen: ich muß fort – Morgen, Rota, ein mehres!"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Geht ab.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        hide der_prinz

        show camillo_rota at truecenter

        $ camillo_rota_var = "{noalt}CAMILLO ROTA"

        hide camillo_rota

        show camillo_rota at truecenter

        hide camillo_rota

        show camillo_rota at truecenter

        camillo_rota "<{i}den Kopf schüttelnd, indem er die Papiere zu sich nimmt und abgeht.{/i}>"

        show camillo_rota at truecenter

        show camillo_rota at truecenter

        camillo_rota "Recht gern? – Ein Todesurteil recht gern? – Ich hätt' es ihn in diesem Augenblicke nicht mögen unterschreiben lassen, und wenn es den Mörder meines einzigen Sohnes betroffen hätte. – Recht gern! recht gern!"

        camillo_rota "– Es geht mir durch die Seele dieses gräßliche Recht gern!"

        hide camillo_rota

label Act_2:
    play music "audio/music/43.mp3" fadeout 1.0 fadein 1.0

    scene 2 with fade

    "{b}Zweiter Aufzug{/b}"

    "<{i}Die Szene, ein Saal in dem Hause der Galotti.{/i}>"

    menu:
        "{color=#000}Erster Auftritt{/color}":
            jump Act_1_Scene_1
        "{color=#000}Zweiter Auftritt{/color}":
            jump Act_1_Scene_2
        "{color=#000}Dritter Auftritt{/color}":
            jump Act_1_Scene_3
        "{color=#000}Vierter Auftritt{/color}":
            jump Act_1_Scene_4
        "{color=#000}Fünfter Auftritt{/color}":
            jump Act_1_Scene_5
        "{color=#000}Sechster Auftritt{/color}":
            jump Act_1_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_1_Scene_6_1

label Further_Act_1_Scene_6_1:
    menu:
        "{color=#000}Siebenter Auftritt{/color}":
            jump Act_1_Scene_7
        "{color=#000}Achter Auftritt{/color}":
            jump Act_1_Scene_8
        "{color=#000}Neunter Auftritt{/color}":
            jump Act_1_Scene_9
        "{color=#000}Zehnter Auftritt{/color}":
            jump Act_1_Scene_10
        "{color=#000}Eilfter Auftritt{/color}":
            jump Act_1_Scene_11

    label Act_1_Scene_1:
        "{b}Erster Auftritt{/b}"

        show claudia at left
        show pirro at right

        show claudia at left
        show pirro at right

        "<{i}Claudia Galotti. Pirro.{/i}>"

        hide claudia
        hide pirro

        hide claudia
        hide pirro

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA"

        hide claudia

        show claudia at left
        show pirro at right

        hide claudia

        show claudia at left
        show pirro at right

        claudia "<{i}im Heraustreten zu Pirro, der von der andern Seite hereintritt.{/i}>"

        hide pirro

        show claudia at truecenter

        hide pirro

        show claudia at truecenter

        claudia "Wer sprengte da in den Hof?"

        hide claudia

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Unser Herr, gnädige Frau."

        hide pirro

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Mein Gemahl? Ist es möglich?"

        hide claudia

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Er folgt mir auf dem Fuße."

        hide pirro

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "So unvermutet? –"

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}Ihm entgegen eilend.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        claudia "Ah! mein Bester! –"

        hide claudia

    label Act_1_Scene_2:
        "{b}Zweiter Auftritt{/b}"

        show odoardo at truecenter

        show odoardo at truecenter

        "<{i}Odoardo Galotti, und die Vorigen.{/i}>"

        hide odoardo

        hide odoardo

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Guten Morgen, meine Liebe! – Nicht wahr, das heißt überraschen?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Und auf die angenehmste Art! – Wenn es anders nur eine Überraschung sein soll."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Nichts weiter! Sei unbesorgt. – Das Glück des heutigen Tages weckte mich so früh; der Morgen war so schön; der Weg ist so kurz; ich vermutete euch hier so geschäftig – Wie leicht vergessen sie etwas: fiel mir ein."

        odoardo "– Mit einem Worte: ich komme, und sehe, und kehre sogleich wieder zurück. – Wo ist Emilia? Unstreitig beschäftigt mit dem Putze? –"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Ihrer Seele! – Sie ist in der Messe. – Ich habe heute, mehr als jeden andern Tag, Gnade von oben zu erflehen, sagte sie, und ließ alles liegen, und nahm ihren Schleier, und eilte –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ganz allein?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Die wenigen Schritte – –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Einer ist genug zu einem Fehltritt! –"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Zürnen Sie nicht, mein Bester; und kommen Sie herein, – einen Augenblick auszuruhen, und, wann Sie wollen, eine Erfrischung zu nehmen."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Wie du meinest, Claudia. – Aber sie sollte nicht allein gegangen sein. –"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Und Ihr, Pirro, bleibt hier in dem Vorzimmer, alle Besuche auf heute zu verbitten."

        hide claudia

    label Act_1_Scene_3:
        "{b}Dritter Auftritt{/b}"

        show pirro at left
        show angelo at right

        show pirro at left
        show angelo at right

        "<{i}Pirro, und bald darauf Angelo.{/i}>"

        hide pirro
        hide angelo

        hide pirro
        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Die sich nur aus Neugierde melden lassen. – Was bin ich seit einer Stunde nicht alles ausgefragt worden! – Und wer kömmt da?"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO"

        hide angelo

        show angelo at truecenter

        hide angelo

        show angelo at truecenter

        angelo "<{i}noch halb hinter der Szene, in einem kurzen Mantel, den er über das Gesicht gezogen, den Hut in die Stirne.{/i}>"

        show angelo at truecenter

        show angelo at truecenter

        angelo "Pirro! – Pirro!"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Ein Bekannter? –"

        hide pirro

        show pirro at left
        show angelo at right

        hide pirro

        show pirro at left
        show angelo at right

        pirro "<{i}In dem Angelo vollends hereintritt, und den Mantel auseinander schlägt.{/i}>"

        hide angelo

        show pirro at truecenter

        hide angelo

        show pirro at truecenter

        pirro "Himmel! Angelo? – Du?"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Wie du siehst. – Ich bin lange genug um das Haus herumgegangen, dich zu sprechen. – Auf ein Wort! –"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Und du wagst es, wieder ans Licht zu kommen? – Du bist seit deiner letzten Mordtat vogelfrei erkläret; auf deinen Kopf steht eine Belohnung –"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Die doch du nicht wirst verdienen wollen? –"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Was willst du? Ich bitte dich, mache mich nicht unglücklich."

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Damit etwa?"

        hide angelo

        show angelo at truecenter

        hide angelo

        show angelo at truecenter

        angelo "<{i}Ihm einen Beutel mit Gelde zeigend.{/i}>"

        show angelo at truecenter

        show angelo at truecenter

        angelo "– Nimm! Es gehöret dir!"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Mir?"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Hast du vergessen? Der Deutsche, dein voriger Herr, – –"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Schweig davon!"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Den du uns, auf dem Wege nach Pisa, in die Falle führtest –"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Wenn uns jemand hörte!"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Hatte ja die Güte, uns auch einen kostbaren Ring zu hinterlassen. – Weißt du nicht? – Er war zu kostbar, der Ring, als daß wir ihn sogleich ohne Verdacht hätten zu Gelde machen können. Endlich ist mir es damit gelungen."

        angelo "Ich habe hundert Pistolen dafür erhalten: und das ist dein Anteil. Nimm!"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Ich mag nichts, – behalt' alles."

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Meinetwegen! – wenn es dir gleich viel ist, wie hoch du deinen Kopf feil trägst –"

        hide angelo

        show angelo at truecenter

        hide angelo

        show angelo at truecenter

        angelo "<{i}Als ob er den Beutel wieder einstecken wollte.{/i}>"

        show angelo at truecenter

        show angelo at truecenter

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "So gib nur!"

        hide pirro

        show pirro at truecenter

        hide pirro

        show pirro at truecenter

        pirro "<{i}Nimmt ihn.{/i}>"

        show pirro at truecenter

        show pirro at truecenter

        pirro "– Und was nun? Denn daß du bloß deswegen mich aufgesucht haben solltest – –"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Das kömmt dir nicht so recht glaublich vor? – Halunke! Was denkst du von uns? – daß wir fähig sind, jemand seinen Verdienst vorzuenthalten? Das mag unter den so genannten ehrlichen Leuten Mode sein: unter uns nicht. – Leb wohl! –"

        hide angelo

        show angelo at truecenter

        hide angelo

        show angelo at truecenter

        angelo "<{i}Tut als ob er gehen wollte, und kehrt wieder um.{/i}>"

        show angelo at truecenter

        show angelo at truecenter

        angelo "Eins muß ich doch fragen. – Da kam ja der alte Galotti so ganz allein in die Stadt gesprengt. Was will der?"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Nichts will er: ein bloßer Spazierritt. Seine Tochter wird, heut' Abend, auf dem Gute, von dem er herkömmt, dem Grafen Appiani angetrauet. Er kann die Zeit nicht erwarten –"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Und reitet bald wieder hinaus?"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "So bald, daß er dich hier trifft, wo du noch lange verziehest. – Aber du hast doch keinen Anschlag auf ihn? Nimm dich in Acht. Er ist ein Mann –"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Kenn' ich ihn nicht? Hab' ich nicht unter ihm gedient? – Wenn darum bei ihm nur viel zu holen wäre! – Wenn fahren die junge Leute nach?"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Gegen Mittag."

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Mit viel Begleitung?"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "In einem einzigen Wagen: die Mutter, die Tochter und der Graf. Ein Paar Freunde kommen aus Sabionetta als Zeugen."

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Und Bediente?"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Nur zwei; außer mir, der ich zu Pferde vorauf reiten soll."

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Das ist gut. – Noch eins: wessen ist die Equipage? Ist es eure? oder des Grafen?"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Des Grafen."

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Schlimm! Da ist noch ein Vorreiter, außer einem handfesten Kutscher. Doch! –"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Ich erstaune. Aber was willst du? – Das Bißchen Schmuck, das die Braut etwa haben dürfte, wird schwerlich der Mühe lohnen –"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "So lohnt ihrer die Braut selbst!"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Und auch bei diesem Verbrechen soll ich dein Mitschuldiger sein?"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Du reitest vorauf. Reite doch, reite! und kehre dich an nichts!"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Nimmermehr!"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Wie? ich glaube gar, du willst den Gewissenhaften spielen. – Bursche! ich denke, du kennst mich. – Wo du plauderst! Wo sich ein einziger Umstand anders findet, als du mir ihn angegeben! –"

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Aber, Angelo, um des Himmels willen! –"

        hide pirro

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Tu, was du nicht lassen kannst!"

        hide angelo

        show angelo at truecenter

        hide angelo

        show angelo at truecenter

        angelo "<{i}Geht ab.{/i}>"

        show angelo at truecenter

        show angelo at truecenter

        hide angelo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Ha! Laß dich den Teufel bei Einem Haare fassen; und du bist sein auf ewig! Ich Unglücklicher!"

        hide pirro

    label Act_1_Scene_4:
        "{b}Vierter Auftritt{/b}"

        show odoardo at left
        show claudia at truecenter
        show pirro at right

        show odoardo at left
        show claudia at truecenter
        show pirro at right

        "<{i}Odoardo und Claudia Galotti. Pirro.{/i}>"

        hide odoardo
        hide claudia
        hide pirro

        hide odoardo
        hide claudia
        hide pirro

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sie bleibt mir zu lang' aus –"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Noch einen Augenblick, Odoardo! Es würde sie schmerzen, deines Anblicks so zu verfehlen."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ich muß auch bei dem Grafen noch einsprechen. Kaum kann ichs erwarten, diesen würdigen jungen Mann meinen Sohn zu nennen. Alles entzückt mich an ihm. Und vor allem der Entschluß, in seinen väterlichen Tälern sich selbst zu leben."

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Das Herz bricht mir, wenn ich hieran gedenke. – So ganz sollen wir sie verlieren, diese einzige geliebte Tochter?"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Was nennst du, sie verlieren? Sie in den Armen der Liebe zu wissen? Vermenge dein Vergnügen an ihr, nicht mit ihrem Glücke."

        odoardo "– Du möchtest meinen alten Argwohn erneuern: – daß es mehr das Geräusch und die Zerstreuung der Welt, mehr die Nähe des Hofes war, als die Notwendigkeit, unserer Tochter eine anständige Erziehung zu geben, was dich bewog, hier in der Stadt mit ihr zu bleiben;"

        odoardo "– fern von einem Manne und Vater, der euch so herzlich liebet."

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wie ungerecht, Odoardo! Aber laß mich heute nur ein einziges für diese Stadt, für diese Nähe des Hofes sprechen, die deiner strengen Tugend so verhaßt sind. – Hier, nur hier konnte die Liebe zusammen bringen, was für einander geschaffen war."

        claudia "Hier nur konnte der Graf Emilien finden; und fand sie."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Das räum' ich ein. Aber, gute Claudia, hattest du darum Recht, weil dir der Ausgang Recht gibt? – Gut, daß es mit dieser Stadterziehung so abgelaufen! Laßt uns nicht weise sein wollen, wo wir nichts, als glücklich gewesen! Gut, daß es so damit abgelaufen!"

        odoardo "– Nun haben sie sich gefunden, die für einander bestimmt waren: nun laß sie ziehen, wohin Unschuld und Ruhe sie rufen. – Was sollte der Graf hier? Sich bücken, schmeicheln und kriechen, und die Marinellis auszustechen suchen?"

        odoardo "um endlich ein Glück zu machen, dessen er nicht bedarf? um endlich einer Ehre gewürdiget zu werden, die für ihn keine wäre? – Pirro!"

        hide odoardo

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Hier bin ich."

        hide pirro

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Geh und führe mein Pferd vor das Haus des Grafen. Ich komme nach, und will mich da wieder aufsetzen."

        hide odoardo

        show odoardo at left
        show pirro at right

        hide odoardo

        show odoardo at left
        show pirro at right

        odoardo "<{i}Pirro geht.{/i}>"

        hide pirro

        show odoardo at truecenter

        hide pirro

        show odoardo at truecenter

        odoardo "– Warum soll der Graf hier dienen, wenn er dort selbst befehlen kann? – Dazu bedenkst du nicht, Claudia, daß durch unsere Tochter er es vollends mit dem Prinzen verderbt. Der Prinz haßt mich –"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Vielleicht weniger, als du besorgest."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Besorgest! Ich besorg' auch so was!"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Denn hab' ich dir schon gesagt, daß der Prinz unsere Tochter gesehen hat?"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Der Prinz? Und wo das?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "In der letzten Vegghia, bei dem Kanzler Grimaldi, die er mit seiner Gegenwart beehrte. Er bezeigte sich gegen sie so gnädig – –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "So gnädig?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Er unterhielt sich mit ihr so lange – –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Unterhielt sich mit ihr?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Schien von ihrer Munterkeit und ihrem Witze so bezaubert – –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "So bezaubert? –"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Hat von ihrer Schönheit mit so vielen Lobeserhebungen gesprochen – –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Lobeserhebungen? Und das alles erzählst du mir in einem Tone der Entzückung? O Claudia! eitle, törichte Mutter!"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wie so?"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Nun gut, nun gut! Auch das ist so abgelaufen. – Ha! wenn ich mir einbilde – Das gerade wäre der Ort, wo ich am tödlichsten zu verwunden bin! – Ein Wollüstling, der bewundert, begehrt. – Claudia! Claudia! der bloße Gedanke setzt mich in Wut."

        odoardo "– Du hättest mir das sogleich sollen gemeldet haben. – Doch, ich möchte dir heute nicht gern etwas Unangenehmes sagen. Und ich würde,"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Indem sie ihn bei der Hand ergreift.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "wenn ich länger bliebe. – Drum laß mich! laß mich! – Gott befohlen, Claudia! – Kommt glücklich nach!"

        hide odoardo

    label Act_1_Scene_5:
        "{b}Fünfter Auftritt{/b}"

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA GALOTTI."

        claudia "Welch ein Mann! – O, der rauhen Tugend! – wenn anders sie diesen Namen verdienet. – Alles scheint ihr verdächtig, alles strafbar! – Oder, wenn das die Menschen kennen heißt; – wer sollte sich wünschen, sie zu kennen? – Wo bleibt aber auch Emilia?"

        claudia "– Er ist des Vaters Feind: folglich – folglich, wenn er ein Auge für die Tochter hat, so ist es einzig, um ihn zu beschimpfen? –"

        hide claudia

    label Act_1_Scene_6:
        "{b}Sechster Auftritt{/b}"

        show emilia at left
        show claudia at right

        show emilia at left
        show claudia at right

        "<{i}Emilia und Claudia Galotti.{/i}>"

        hide emilia
        hide claudia

        hide emilia
        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}stürzet in einer ängstlichen Verwirrung herein.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Wohl mir! wohl mir! Nun bin ich in Sicherheit. Oder ist er mir gar gefolgt?"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}Indem sie den Schleier zurück wirft und ihre Mutter erblicket.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Ist er, meine Mutter? ist er? – Nein, dem Himmel sei Dank!"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Was ist dir, meine Tochter? was ist dir?"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nichts, nichts –"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Und blickest so wild um dich? Und zitterst an jedem Gliede?"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Was hab' ich hören müssen? Und wo, wo hab' ich es hören müssen?"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Ich habe dich in der Kirche geglaubt –"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Eben da! Was ist dem Laster Kirch' und Altar? – Ah, meine Mutter!"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}Sich ihr in die Arme werfend.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Rede, meine Tochter! – Mach' meiner Furcht ein Ende. – Was kann dir da, an heiliger Stätte, so Schlimmes begegnet sein?"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nie hätte meine Andacht inniger, brünstiger sein sollen, als heute: nie ist sie weniger gewesen, was sie sein sollte."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wir sind Menschen, Emilia. Die Gabe zu beten ist nicht immer in unserer Gewalt. Dem Himmel ist beten wollen, auch beten."

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Und sündigen wollen, auch sündigen."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Das hat meine Emilia nicht wollen!"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nein, meine Mutter; so tief ließ mich die Gnade nicht sinken. – Aber daß fremdes Laster uns, wider unsern Willen, zu Mitschuldigen machen kann!"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Fasse dich! – Sammle deine Gedanken, so viel dir möglich. – Sag' es mir mit eins, was dir geschehen."

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Eben hatt' ich mich – weiter von dem Altare, als ich sonst pflege, – denn ich kam zu spät – auf meine Knie gelassen. Eben fing ich an, mein Herz zu erheben: als dicht hinter mir etwas seinen Platz nahm. So dicht hinter mir! – Ich"

        emilia "konnte weder vor, noch zur Seite rücken, – so gern ich auch wollte; aus Furcht, daß eines andern Andacht mich in meiner stören möchte. – Andacht! das war das Schlimmste, was ich besorgte."

        emilia "– Aber es währte nicht lange, so hört' ich, ganz nah' an meinem Ohre, – nach einem tiefen Seufzer, – nicht den Namen einer Heiligen, – den Namen, – zürnen Sie nicht, meine Mutter – den Namen Ihrer Tochter! – Meinen Namen!"

        emilia "– O daß laute Donner mich verhindert hätten, mehr zu hören! – Es sprach von Schönheit, von Liebe – Es klagte, daß dieser Tag, welcher mein Glück mache, – wenn er es anders mache – sein Unglück auf immer entscheide."

        emilia "– Es beschwor mich – hören mußt' ich dies alles. Aber ich blickte nicht um; ich wollte tun, als ob ich es nicht hörte. – Was konnt' ich sonst? – Meinen guten Engel bitten, mich mit Taubheit zu schlagen; und wann auch, wann auch auf immer! – Das bat ich;"

        emilia "das war das einzige, was ich beten konnte. – Endlich ward es Zeit, mich wieder zu erheben. Das heilige Amt ging zu Ende. Ich zitterte, mich umzukehren. Ich zitterte, ihn zu erblicken, der sich den Frevel erlauben dürfen."

        emilia "Und da ich mich umwandte, da ich ihn erblickte –"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wen, meine Tochter?"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Raten Sie, meine Mutter; raten Sie – Ich glaubte in die Erde zu sinken – Ihn selbst."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wen, ihn selbst?"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Den Prinzen."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Den Prinzen! – O gesegnet sei die Ungeduld deines Vaters, der eben hier war, und dich nicht erwarten wollte!"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Mein Vater hier? – und wollte mich nicht erwarten?"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wenn du in deiner Verwirrung auch ihn das hättest hören lassen!"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nun, meine Mutter? – Was hätt' er an mir Strafbares finden können?"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Nichts; eben so wenig, als an mir. Und doch, doch – Ha, du kennst deinen Vater nicht! In seinem Zorne hätt' er den unschuldigen Gegenstand des Verbrechens mit dem Verbrecher verwechselt."

        claudia "In seiner Wut hätt' ich ihm geschienen, das veranlaßt zu haben, was ich weder verhindern, noch vorhersehen können. – Aber weiter, meine Tochter,"

        claudia "weiter! Als du den Prinzen erkanntest – Ich will hoffen, daß du deiner mächtig genug warest, ihm in Einem Blicke alle die Verachtung zu bezeigen, die er verdienet."

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Das war ich nicht, meine Mutter! Nach dem Blicke, mit dem ich ihn erkannte, hatt' ich nicht das Herz, einen zweiten auf ihn zu richten. Ich floh' –"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Und der Prinz dir nach –"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Was ich nicht wußte, bis ich in der Halle mich bei der Hand ergriffen fühlte. Und von ihm! Aus Scham mußt' ich Stand halten: mich von ihm loszuwinden, würde die Vorbeigehenden zu aufmerksam auf uns gemacht haben."

        emilia "Das war die einzige Überlegung, deren ich fähig war – oder deren ich nun mich wieder erinnere. Er sprach; und ich hab' ihm geantwortet. Aber was er sprach, was ich ihm geantwortet; – fällt mir es noch bei, so ist es gut, so will ich es Ihnen sagen, meine Mutter."

        emilia "Itzt weiß ich von dem allen nichts. Meine Sinne hatten mich verlassen. – Umsonst denk' ich nach, wie ich von ihm weg, und aus der Halle gekommen. Ich finde mich erst auf der Straße wieder; und höre ihn hinter mir herkommen;"

        emilia "und höre ihn mit mir zugleich in das Haus treten, mit mir die Treppe hinauf steigen – –"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Die Furcht hat ihren besondern Sinn, meine Tochter! – Ich werde es nie vergessen, mit welcher Gebärde du hereinstürztest. – Nein, so weit durfte er nicht wagen, dir zu folgen. – Gott! Gott! wenn dein Vater das wüßte!"

        claudia "– Wie wild er schon war, als er nur hörte, daß der Prinz dich jüngst nicht ohne Mißfallen gesehen! – Indes, sei ruhig, meine Tochter! Nimm es für einen Traum, was dir begegnet ist. Auch wird es noch weniger Folgen haben, als ein Traum."

        claudia "Du entgehest heute mit eins allen Nachstellungen."

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Aber nicht, meine Mutter? Der Graf muß das wissen. Ihm muß ich es sagen."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Um alle Welt nicht! – Wozu? warum? Willst du für nichts, und wieder für nichts ihn unruhig machen? Und wann er es auch itzt nicht würde: wisse, mein Kind, daß ein Gift, welches nicht gleich wirket, darum kein minder gefährliches Gift ist."

        claudia "Was auf den Liebhaber keinen Eindruck macht, kann ihn auf den Gemahl machen. Den Liebhaber könnt' es"

        claudia "sogar schmeicheln, einem so wichtigen Mitbewerber den Rang abzulaufen. Aber wenn er ihm den nun einmal abgelaufen hat: ah, mein Kind, – so wird aus dem Liebhaber oft ein ganz anderes Geschöpf. Dein gutes Gestirn behüte dich vor dieser Erfahrung."

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Sie wissen, meine Mutter, wie gern ich Ihren bessern Einsichten mich in allem unterwerfe. – Aber, wenn er es von einem andern erführe, daß der Prinz mich heute gesprochen? Würde mein Verschweigen nicht, früh oder spät, seine Unruhe vermehren?"

        emilia "– Ich dächte doch, ich behielte lieber vor ihm nichts auf dem Herzen."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Schwachheit! verliebte Schwachheit! – Nein, durchaus nicht, meine Tochter! Sag' ihm nichts. Laß ihn nichts merken!"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nun ja, meine Mutter! Ich habe keinen Willen gegen den Ihrigen. – Aha!"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}Mit einem tiefen Atemzuge.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Auch wird mir wieder ganz leicht. – Was für ein albernes, furchtsames Ding ich bin! – Nicht, meine Mutter? – Ich hätte mich noch wohl anders dabei nehmen können, und würde mir eben so wenig vergeben haben."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Ich wollte dir das nicht sagen, meine Tochter, bevor dir es dein eigner gesunder Verstand sagte. Und ich wußte, er würde dir es sagen, sobald du wieder zu dir selbst gekommen. – Der Prinz ist galant."

        claudia "Du bist die unbedeutende Sprache der Galanterie zu wenig gewohnt. Eine Höflichkeit wird in ihr zur Empfindung; eine Schmeichelei zur Beteurung; ein Einfall zum Wunsche; ein Wunsch zum Vorsatze."

        claudia "Nichts klingt in dieser Sprache wie alles: und alles ist in ihr so viel als nichts."

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "O meine Mutter! – so müßte ich mir mit meiner Furcht vollends lächerlich vorkommen! – Nun soll er gewiß nichts davon erfahren, mein guter Appiani! Er könnte mich leicht für mehr eitel, als tugendhaft, halten. – Hui! daß er da selbst kömmt! Es ist sein Gang."

        hide emilia

    label Act_1_Scene_7:
        "{b}Siebenter Auftritt{/b}"

        show appiani at truecenter

        show appiani at truecenter

        "<{i}Graf Appiani. Die Vorigen.{/i}>"

        hide appiani

        hide appiani

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI"

        hide appiani

        show appiani at left
        show emilia at right

        hide appiani

        show appiani at left
        show emilia at right

        appiani "<{i}tritt tiefsinnig, mit vor sich hingeschlagnen Augen herein, und kömmt ihnen näher, ohne sie zu erblicken; bis Emilia ihm entgegen springt.{/i}>"

        hide emilia

        show appiani at truecenter

        hide emilia

        show appiani at truecenter

        appiani "Ah, meine Teuerste! – Ich war mir Sie in dem Vorzimmer nicht vermutend."

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Ich wünschte Sie heiter, Herr Graf, auch wo Sie mich nicht vermuten. – So feierlich? so ernsthaft? – Ist dieser Tag keiner freudigern Aufwallung wert?"

        hide emilia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Er ist mehr wert, als mein ganzes Leben. Aber schwanger mit so viel Glückseligkeit für mich, – mag es wohl diese Glückseligkeit selbst sein, die mich so ernst, die mich, wie Sie es nennen, mein Fräulein, so feierlich macht. –"

        hide appiani

        show appiani at truecenter

        hide appiani

        show appiani at truecenter

        appiani "<{i}Indem er die Mutter erblickt.{/i}>"

        show appiani at truecenter

        show appiani at truecenter

        appiani "Ha! auch Sie hier, meine gnädige Frau! – nun bald mir mit einem innigern Namen zu verehrende!"

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Der mein größter Stolz sein wird! – Wie glücklich bist du, meine Emilia! – Warum hat dein Vater unsere Entzückung nicht teilen wollen?"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Eben hab' ich mich aus seinen Armen gerissen; – oder vielmehr er, sich aus meinen. – Welch ein Mann, meine Emilia, Ihr Vater! Das Muster aller männlichen Tugend! Zu was für Gesinnungen erhebt sich meine Seele in seiner Gegenwart!"

        appiani "Nie ist mein Entschluß immer gut, immer edel zu sein, lebendiger, als wenn ich ihn sehe – wenn ich ihn mir denke. Und womit sonst, als mit der Erfüllung dieses Entschlusses kann ich mich der Ehre würdig machen, sein Sohn zu heißen;"

        appiani "– der Ihrige zu sein, meine Emilia?"

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Und er wollte mich nicht erwarten!"

        hide emilia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ich urteile, weil ihn seine Emilia, für diesen augenblicklichen Besuch, zu sehr erschüttert, zu sehr sich seiner ganzen Seele bemächtiget hätte."

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Er glaubte dich mit deinem Brautschmucke beschäftiget zu finden: und hörte –"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Was ich mit der zärtlichsten Bewunderung wieder von ihm gehört habe. – So recht, meine Emilia! Ich werde eine"

        appiani "fromme Frau an Ihnen haben; und die nicht stolz auf ihre Frömmigkeit ist."

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Aber, meine Kinder, eines tun, und das andere nicht lassen! – Nun ist es hohe Zeit; nun mach', Emilia!"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Was? meine gnädige Frau."

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Sie wollen sie doch nicht so, Herr Graf, so wie sie da ist, zum Altare führen?"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Wahrlich, das werd' ich nun erst gewahr. – Wer kann Sie sehen, Emilia, und auch auf Ihren Putz achten? – Und warum nicht so, so wie sie da ist?"

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nein, mein lieber Graf, nicht so; nicht ganz so. Aber auch nicht viel prächtiger; nicht viel. – Husch, husch, und ich bin fertig! – Nichts, gar nichts von dem Geschmeide, dem letzten Geschenke Ihrer verschwendrischen Großmut!"

        emilia "Nichts, gar nichts, was sich nur zu solchem Geschmeide schickte! – Ich könnte ihm gram sein, diesem Geschmeide, wenn es nicht von Ihnen wäre. – Denn dreimal hat mir von ihm geträumet –"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Nun! davon weiß ich ja nichts."

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Als ob ich es trüge, und als ob plötzlich sich jeder Stein desselben in eine Perle verwandle. – Perlen aber, meine Mutter, Perlen bedeuten Tränen."

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Kind! Die Bedeutung ist träumerischer, als der Traum. – Warest du nicht von je her eine größere Liebhaberin von Perlen, als von Steinen? –"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Freilich, meine Mutter, freilich –"

        hide emilia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI"

        hide appiani

        show appiani at truecenter

        hide appiani

        show appiani at truecenter

        appiani "<{i}nackdenkend und schwermütig.{/i}>"

        show appiani at truecenter

        show appiani at truecenter

        appiani "Bedeuten Tränen – bedeuten Tränen!"

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Wie? Ihnen fällt das auf? Ihnen?"

        hide emilia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ja wohl; ich sollte mich schämen. – Aber, wenn die Einbildungskraft einmal zu traurigen Bildern gestimmt ist –"

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Warum ist sie das auch? – Und was meinen Sie, das ich mir ausgedacht habe? – Was trug ich, wie sah ich, als ich Ihnen zuerst gefiel, – Wissen Sie es noch?"

        hide emilia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ob ich es noch weiß? Ich sehe Sie in Gedanken nie anders, als so; und sehe Sie so, auch wenn ich Sie nicht so sehe."

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Also, ein Kleid von der nämlichen Farbe, von dem nämlichen Schnitte; fliegend und frei –"

        hide emilia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Vortrefflich!"

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Und das Haar –"

        hide emilia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "In seinem eignen braunen Glanze; in Locken, wie sie die Natur schlug –"

        hide appiani

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Die Rose darin nicht zu vergessen! Recht! recht! – Eine kleine Geduld, und ich stehe so vor Ihnen da!"

        hide emilia

    label Act_1_Scene_8:
        "{b}Achter Auftritt{/b}"

        show appiani at left
        show claudia at right

        show appiani at left
        show claudia at right

        "<{i}Graf Appiani. Claudia Galotti.{/i}>"

        hide appiani
        hide claudia

        hide appiani
        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI"

        hide appiani

        show appiani at truecenter

        hide appiani

        show appiani at truecenter

        appiani "<{i}indem er ihr mit einer niedergeschlagnen Miene nachsieht.{/i}>"

        show appiani at truecenter

        show appiani at truecenter

        appiani "Perlen bedeuten Tränen! – Eine kleine Geduld! – Ja, wenn die Zeit nur außer uns wäre! – Wenn eine Minute am Zeiger, sich in uns nicht in Jahre ausdehnen könnte! –"

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Emiliens Beobachtung, Herr Graf, war so schnell, als richtig. Sie sind heut' ernster als gewöhnlich. Nur noch einen Schritt von dem Ziele Ihrer Wünsche, – sollt' es Sie reuen, Herr Graf, daß es das Ziel Ihrer Wünsche gewesen?"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ah, meine Mutter, und Sie können das von Ihrem Sohne argwohnen? – Aber, es ist wahr; ich bin heut' ungewöhnlich trübe und finster. – Nur sehen Sie, gnädige Frau; – noch Einen Schritt vom Ziele, oder noch gar nicht ausgelaufen sein, ist im Grunde eines."

        appiani "– Alles was ich sehe, alles was ich höre, alles was ich träume, prediget mir seit gestern und ehegestern diese Wahrheit. Dieser Eine Gedanke kettet sich an jeden andern, den ich haben muß und haben will. – Was ist das? Ich versteh' es nicht. –"

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Sie machen mich unruhig, Herr Graf –"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Eines kömmt dann zum andern! – Ich bin ärgerlich; ärgerlich über meine Freunde, über mich selbst –"

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wie so?"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Meine Freunde verlangen schlechterdings, daß ich dem Prinzen von meiner Heirat ein Wort sagen soll, ehe ich sie vollziehe. Sie geben mir zu, ich sei es nicht schuldig: aber die Achtung gegen ihn woll' es nicht anders."

        appiani "– Und ich bin schwach genug gewesen, es ihnen zu versprechen. Eben wollt' ich noch bei ihm vorfahren."

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA"

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}stutzig.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        claudia "Bei dem Prinzen?"

        hide claudia

    label Act_1_Scene_9:
        "{b}Neunter Auftritt{/b}"

        show pirro at left
        show marinelli at right

        show pirro at left
        show marinelli at right

        "<{i}Pirro, gleich darauf Marinelli, und die Vorigen.{/i}>"

        hide pirro
        hide marinelli

        hide pirro
        hide marinelli

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Gnädige Frau, der Marchese Marinelli hält vor dem Hause, und erkundiget sich nach dem Herrn Grafen."

        hide pirro

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Nach mir?"

        hide appiani

        show pirro at truecenter

        $ pirro_var = "{noalt}PIRRO."

        pirro "Hier ist er schon."

        hide pirro

        show pirro at truecenter

        hide pirro

        show pirro at truecenter

        pirro "<{i}Öffnet ihm die Türe und geht ab.{/i}>"

        show pirro at truecenter

        show pirro at truecenter

        hide pirro

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich bitt' um Verzeihung, gnädige Frau. – Mein Herr Graf, ich war vor Ihrem Hause, und erfuhr, daß ich Sie hier treffen würde. Ich hab' ein dringendes Geschäft an Sie – Gnädige Frau, ich bitte nochmals um Verzeihung; es ist in einigen Minuten geschehen."

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Die ich nicht verzögern will."

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}Macht ihm eine Verbeugung und geht ab.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        hide claudia

    label Act_1_Scene_10:
        "{b}Zehnter Auftritt{/b}"

        show marinelli at left
        show appiani at right

        show marinelli at left
        show appiani at right

        "<{i}Marinelli. Appiani.{/i}>"

        hide marinelli
        hide appiani

        hide marinelli
        hide appiani

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Nun, mein Herr?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich komme von des Prinzen Durchlaucht."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Was ist zu seinem Befehl?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich bin stolz, der Überbringer einer so vorzüglichen Gnade zu sein. – Und wenn Graf Appiani nicht mit Gewalt einen seiner ergebensten Freunde in mir verkennen will – –"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ohne weitere Vorrede; wenn ich bitten darf."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Auch das! – Der Prinz muß sogleich an den Herzog von Massa, in Angelegenheit seiner Vermählung mit dessen Prinzessin Tochter, einen Bevollmächtigten senden. Er war lange unschlüssig, wen er dazu ernennen solle."

        marinelli "Endlich ist seine Wahl, Herr Graf, auf Sie gefallen."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Auf mich?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und das, – wenn die Freundschaft ruhmredig sein darf – nicht ohne mein Zutun –"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Wahrlich, Sie setzen mich wegen eines Dankes in Verlegenheit."

        appiani "– Ich habe schon längst nicht mehr erwartet, daß der Prinz mich zu brauchen geruhen werde. –"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich bin versichert, daß es ihm bloß an einer würdigen Gelegenheit gemangelt hat. Und wenn auch diese so eines Mannes, wie Graf Appiani, noch nicht würdig genug sein sollte: so ist freilich meine Freundschaft zu voreilig gewesen."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Freundschaft und Freundschaft, um das dritte Wort! – Mit wem red' ich denn? Des Marchese Marinelli Freundschaft hätt' ich mir nie träumen lassen. –"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich erkenne mein Unrecht, Herr Graf, mein unverzeihliches Unrecht, daß ich, ohne Ihre Erlaubnis, Ihr Freund sein wollen. – Bei dem allen: was tut das?"

        marinelli "Die Gnade des Prinzen, die Ihnen angetragene Ehre, bleiben, was sie sind: und ich zweifle nicht, Sie werden sie mit Begierd' ergreifen."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI"

        hide appiani

        show appiani at truecenter

        hide appiani

        show appiani at truecenter

        appiani "<{i}nach einiger Überlegung.{/i}>"

        show appiani at truecenter

        show appiani at truecenter

        appiani "Allerdings."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun so kommen Sie."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Wohin?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nach Dosalo, zu dem Prinzen. – Es liegt schon alles fertig; und Sie müssen noch heut' abreisen."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Was sagen Sie? – Noch heute?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Lieber noch in dieser nämlichen Stunde, als in der folgenden. Die Sache ist von der äußersten Eil."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "In Wahrheit? – So tut es mir leid, daß ich die Ehre, welche mir der Prinz zugedacht, verbitten muß."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wie?"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ich kann heute nicht abreisen; – auch morgen nicht; – auch übermorgen noch nicht. –"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie scherzen, Herr Graf."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Mit Ihnen?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Unvergleichlich! Wenn der Scherz den Prinzen gilt, so ist er um so viel lustiger. – Sie können nicht?"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Nein, mein Herr, nein. – Und ich hoffe, daß der Prinz selbst meine Entschuldigung wird gelten lassen."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Die bin ich begierig, zu hören."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "O, eine Kleinigkeit! – Sehen Sie; ich soll noch heut' eine Frau nehmen."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun? und dann?"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Und dann? – und dann? – Ihre Frage ist auch verzweifelt naiv."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Man hat Exempel, Herr Graf, daß sich Hochzeiten aufschieben lassen. – Ich glaube freilich nicht, daß der Braut oder dem Bräutigam immer damit gedient ist. Die Sache mag ihr Unangenehmes haben. Aber doch, dächt' ich, der Befehl des Herrn –"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Der Befehl des Herrn? – des Herrn? Ein Herr, den man sich selber wählt, ist unser Herr so eigentlich nicht – Ich gebe zu, daß Sie dem Prinzen unbedingtern Gehorsam schuldig wären. Aber nicht ich. – Ich kam an seinen Hof als ein Freiwilliger."

        appiani "Ich wollte die Ehre haben, ihm zu dienen; aber nicht sein Sklave werden. Ich bin der Vasall eines größern Herrn –"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Größer oder kleiner: Herr ist Herr."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Daß ich mit Ihnen darüber stritte! – Genug, sagen Sie dem Prinzen, was Sie gehört haben; – daß es mir leid tut, seine Gnade nicht annehmen zu können; weil ich eben heut' eine Verbindung vollzöge, die mein ganzes Glück ausmache."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wollen Sie ihn nicht zugleich wissen lassen, mit wem?"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Mit Emilia Galotti."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Der Tochter aus diesem Hause?"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Aus diesem Hause."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Hm! hm!"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Was beliebt?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich sollte meinen, daß es sonach um so weniger Schwierigkeit haben könne, die Zeremonie bis zu Ihrer Zurückkunft auszusetzen."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Die Zeremonie? Nur die Zeremonie?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Die guten Eltern werden es so genau nicht nehmen."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Die guten Eltern?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und Emilia bleibt Ihnen ja wohl gewiß."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ja wohl gewiß? – Sie sind mit Ihrem Ja wohl – ja wohl ein ganzer Affe!"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Mir das, Graf?"

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Warum nicht?"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Himmel und Hölle! – Wir werden uns sprechen."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Pah! Hämisch ist der Affe; aber –"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Tod und Verdammnis! – Graf, ich fodere Genugtuung."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Das versteht sich."

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und würde sie gleich itzt nehmen: – nur daß ich dem zärtlichen Bräutigam den heutigen Tag nicht verderben mag."

        hide marinelli

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Gutherziges Ding! Nicht doch! Nicht doch!"

        hide appiani

        show appiani at truecenter

        hide appiani

        show appiani at truecenter

        appiani "<{i}Indem er ihn bei der Hand ergreift.{/i}>"

        show appiani at truecenter

        show appiani at truecenter

        appiani "Nach Massa freilich mag ich mich heute nicht schicken lassen; aber zu einem Spaziergange mit Ihnen hab' ich Zeit übrig. – Kommen Sie, kommen Sie!"

        hide appiani

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}der sich losreißt, und abgeht.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Nur Geduld, Graf, nur Geduld!"

        hide marinelli

    label Act_1_Scene_11:
        "{b}Eilfter Auftritt{/b}"

        show appiani at left
        show claudia at right

        show appiani at left
        show claudia at right

        "<{i}Appiani. Claudia Galotti.{/i}>"

        hide appiani
        hide claudia

        hide appiani
        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Geh, Nichtswürdiger! – Ha! das hat gut getan. Mein Blut ist in Wallung gekommen. Ich fühle mich anders und besser."

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA"

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}eiligst und besorgt.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        claudia "Gott! Herr Graf – Ich hab' einen heftigen Wortwechsel gehört. – Ihr Gesicht glühet. Was ist vorgefallen?"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Nichts, gnädige Frau, gar nichts. Der Kammerherr Marinelli hat mir einen großen Dienst erwiesen. Er hat mich des Ganges zum Prinzen überhoben."

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "In der Tat?"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Wir können nun um so viel früher abfahren. Ich gehe, meine Leute zu treiben, und bin sogleich wieder hier. Emilia wird indes auch fertig."

        hide appiani

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Kann ich ganz ruhig sein, Herr Graf?"

        hide claudia

        show appiani at truecenter

        $ appiani_var = "{noalt}APPIANI."

        appiani "Ganz ruhig, gnädige Frau."

        hide appiani

        show appiani at truecenter

        hide appiani

        show appiani at truecenter

        appiani "<{i}Sie geht herein und er fort.{/i}>"

        show appiani at truecenter

        show appiani at truecenter

        hide appiani

label Act_3:
    play music "audio/music/90.mp3" fadeout 1.0 fadein 1.0

    scene 3 with fade

    "{b}Dritter Aufzug{/b}"

    "<{i}Die Szene, ein Vorsaal auf dem Lustschlosse des Prinzen.{/i}>"

    menu:
        "{color=#000}Erster Auftritt{/color}":
            jump Act_2_Scene_1
        "{color=#000}Zweiter Auftritt{/color}":
            jump Act_2_Scene_2
        "{color=#000}Dritter Auftritt{/color}":
            jump Act_2_Scene_3
        "{color=#000}Vierter Auftritt{/color}":
            jump Act_2_Scene_4
        "{color=#000}Fünfter Auftritt{/color}":
            jump Act_2_Scene_5
        "{color=#000}Sechster Auftritt{/color}":
            jump Act_2_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_2_Scene_6_1

label Further_Act_2_Scene_6_1:
    menu:
        "{color=#000}Siebenter Auftritt{/color}":
            jump Act_2_Scene_7
        "{color=#000}Achter Auftritt{/color}":
            jump Act_2_Scene_8

    label Act_2_Scene_1:
        "{b}Erster Auftritt{/b}"

        show der_prinz at left
        show marinelli at right

        show der_prinz at left
        show marinelli at right

        "<{i}Der Prinz. Marinelli.{/i}>"

        hide der_prinz
        hide marinelli

        hide der_prinz
        hide marinelli

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Umsonst; er schlug die angetragene Ehre mit der größten Verachtung aus."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und so bleibt es dabei? So geht es vor sich? so wird Emilia noch heute die Seinige?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Allem Ansehen nach."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich versprach mir von Ihrem Einfalle so viel! – Wer weiß, wie albern Sie sich dabei genommen. – Wenn der Rat eines Toren einmal gut ist, so muß ihn ein gescheuter Mann ausführen. Das hätt' ich bedenken sollen."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Da find' ich mich schön belohnt!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und wofür belohnt?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Daß ich noch mein Leben darüber in die Schanze schlagen wollte. – Als ich sahe, daß weder Ernst noch Spott den Grafen bewegen konnte, seine Liebe der Ehre nachzusetzen: versucht' ich es, ihn in Harnisch zu jagen. Ich sagte ihm Dinge, über die er sich vergaß."

        marinelli "Er stieß Beleidigungen gegen mich aus: und ich foderte Genugtuung, – und foderte sie gleich auf der Stelle. – Ich dachte so: entweder er mich; oder ich ihn. Ich ihn: so ist das Feld ganz unser. Oder er mich: nun, wenn auch;"

        marinelli "so muß er fliehen, und der Prinz gewinnt wenigstens Zeit."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Das hätten Sie getan, Marinelli?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ha! man sollt' es voraus wissen, wenn man so töricht bereit ist, sich für die Großen aufzuopfern – man sollt' es voraus wissen, wie erkenntlich sie sein würden –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und der Graf? – Er stehet in dem Rufe, sich so etwas nicht zweimal sagen zu lassen."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nachdem es fällt, ohne Zweifel. – Wer kann es ihm auch verdenken? – Er versetzte, daß er auf heute doch noch etwas Wichtigeres zu tun habe, als sich mit mir den Hals zu brechen. Und so beschied er mich auf die ersten acht Tage nach der Hochzeit."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Mit Emilia Galotti! Der Gedanke macht mich rasend! – Darauf ließen Sie es gut sein, und gingen; – und kommen und prahlen, daß Sie Ihr Leben für mich in die Schanze geschlagen; sich mir aufgeopfert –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Was wollen Sie aber, gnädiger Herr, das ich weiter hätte tun sollen?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Weiter tun? – Als ob er etwas getan hätte!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und lassen Sie doch hören, gnädiger Herr, was Sie für sich selbst getan haben. – Sie waren so glücklich, sie noch in der Kirche zu sprechen. Was haben Sie mit ihr abgeredet?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}höhnisch.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Neugierde zur Gnüge! – Die ich nur befriedigen muß. – O, es ging alles nach Wunsch. – Sie brauchen sich nicht weiter zu bemühen, mein allzudienstfertiger Freund! – Sie kam meinem Verlangen, mehr als halbes Weges, entgegen."

        der_prinz "Ich hätte sie nur gleich mitnehmen dürfen."

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Kalt und befehlend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Nun wissen Sie, was Sie wissen wollen; – und können gehn!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und können gehn! – Ja, ja; das ist das Ende vom Liede! und würd' es sein, gesetzt auch, ich wollte noch das Unmögliche versuchen. – Das Unmögliche, sag' ich? – So unmöglich wär' es nun wohl nicht; aber kühn."

        marinelli "– Wenn wir die Braut in unserer Gewalt hätten: so stünd' ich dafür, daß aus der Hochzeit nichts werden sollte."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ei! wofür der Mann nicht alles stehen will!"

        der_prinz "Nun dürft' ich ihm nur noch ein Kommando von meiner Leibwache geben, und er legte sich an der Landstraße damit in Hinterhalt, und fiele selbst funfziger einen Wagen an, und riß ein Mädchen heraus, das er im Triumphe mir zubrächte."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Es ist eher ein Mädchen mit Gewalt entführt worden, ohne daß es einer gewaltsamen Entführung ähnlich gesehen."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wenn Sie das zu machen wüßten: so würden Sie nicht erst lange davon schwatzen."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Aber für den Ausgang müßte man nicht stehen sollen. – Es könnten sich Unglücksfälle dabei eräugnen –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und es ist meine Art, daß ich Leute Dinge verantworten lasse, wofür sie nicht können!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Also, gnädiger Herr –"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Man hört von weitem einen Schuß.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Ha! was war das? – Hört' ich recht? – Hörten Sie nicht auch, gnädiger Herr, einen Schuß fallen? – Und da noch einen!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Was ist das? was gibts?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Was meinen Sie wohl? – Wie wann ich tätiger wäre, als Sie glauben?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Tätiger? – So sagen Sie doch –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Kurz: wovon ich gesprochen, geschieht."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ist es möglich?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nur vergessen Sie nicht, Prinz, wessen Sie mich eben versichert. – Ich habe nochmals Ihr Wort – –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Aber die Anstalten sind doch so –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Als sie nur immer sein können! – Die Ausführung ist Leuten anvertrauet, auf die ich mich verlassen kann. Der Weg geht hart an der Planke des Tiergartens vorbei. Da wird ein Teil den Wagen angefallen haben; gleichsam, um ihn zu plündern."

        marinelli "Und ein andrer Teil, wobei einer von meinen Bedienten ist, wird aus dem Tiergarten gestürzt sein; den Angefallenen gleichsam zur Hülfe."

        marinelli "Während des Handgemenges, in das beide Teile zum Schein geraten, soll mein Bedienter Emilien ergreifen, als ob er sie retten wolle, und durch den Tiergarten in das Schloß bringen. – So ist die Abrede. – Was sagen Sie nun, Prinz?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sie überraschen mich auf eine sonderbare Art. – Und eine Bangigkeit überfällt mich –"

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        der_prinz "<{i}Marinelli tritt an das Fenster.{/i}>"

        hide marinelli

        show der_prinz at truecenter

        hide marinelli

        show der_prinz at truecenter

        der_prinz "Wornach sehen Sie?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Dahinaus muß es sein! – Recht! – und eine Maske kömmt bereits um die Planke gesprengt; – ohne Zweifel, mir den Erfolg zu berichten. – Entfernen Sie sich, gnädiger Herr."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ah, Marinelli –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun? Nicht wahr, nun hab' ich zu viel getan; und vorhin zu wenig?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Das nicht. Aber ich sehe bei alle dem nicht ab – –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Absehn? – Lieber alles mit eins! – Geschwind entfernen Sie sich. – Die Maske muß Sie nicht sehen."

        hide marinelli

        show marinelli at left
        show der_prinz at right

        hide marinelli

        show marinelli at left
        show der_prinz at right

        marinelli "<{i}Der Prinz geht ab.{/i}>"

        hide der_prinz

        show marinelli at truecenter

        hide der_prinz

        show marinelli at truecenter

        hide marinelli

    label Act_2_Scene_2:
        "{b}Zweiter Auftritt{/b}"

        show marinelli at left
        show angelo at right

        show marinelli at left
        show angelo at right

        "<{i}Marinelli, und bald darauf Angelo.{/i}>"

        hide marinelli
        hide angelo

        hide marinelli
        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}der wieder nach dem Fenster geht.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Dort fährt der Wagen langsam nach der Stadt zurück. – So langsam? Und in jedem Schlage ein Bedienter? – Das sind Anzeigen, die mir nicht gefallen; – daß der Streich wohl nur halb gelungen ist;"

        marinelli "– daß man einen Verwundeten gemächlich zurückführet, – und keinen Toten. – Die Maske steigt ab. – Es ist Angelo selbst. Der Tolldreiste! – Endlich, hier weiß er die Schliche. – Er winkt mir zu. Er muß seiner Sache gewiß sein."

        marinelli "– Ha, Herr Graf, der Sie nicht nach Massa wollten, und nun noch einen weitern Weg müssen! – Wer hatte Sie die Affen so kennen gelehrt?"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Indem er nach der Türe zugeht.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Ja wohl sind sie hämisch. – Nun Angelo?"

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO"

        hide angelo

        show angelo at truecenter

        hide angelo

        show angelo at truecenter

        angelo "<{i}der die Maske abgenommen.{/i}>"

        show angelo at truecenter

        show angelo at truecenter

        angelo "Passen Sie auf, Herr Kammerherr! Man muß sie gleich bringen."

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und wie lief es sonst ab?"

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Ich denke ja, recht gut."

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wie steht es mit dem Grafen?"

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Zu dienen! So, so! – Aber er muß Wind gehabt haben. Denn er war nicht so ganz unbereitet."

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Geschwind sage mir, was du mir zu sagen hast! – Ist er tot?"

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Es tut mir leid um den guten Herrn."

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun da, für dein mitleidiges Herz!"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Gibt ihm einen Beutel mit Gold.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Vollends mein braver Nicolo! der das Bad mit bezahlen müssen."

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "So? Verlust auf beiden Seiten?"

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Ich könnte weinen, um den ehrlichen Jungen! Ob mir"

        angelo "sein Tod schon das"

        angelo "Indem er den Beutel in der Hand wieget."

        angelo "um ein Vierteil verbessert. Denn ich bin sein Erbe; weil ich ihn gerächet habe. Das ist so unser Gesetz: ein so gutes, mein' ich, als für Treu und Freundschaft je gemacht worden. Dieser Nicolo, Herr Kammerherr –"

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Mit deinem Nicolo! – Aber der Graf, der Graf –"

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Blitz! der Graf hatte ihn gut gefaßt. Dafür faßt' ich auch wieder den Grafen! – Er stürzte; und wenn er noch lebendig zurück in die Kutsche kam: so steh' ich dafür, daß er nicht lebendig wieder heraus kömmt."

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn das nur gewiß ist, Angelo."

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Ich will Ihre Kundschaft verlieren, wenn es nicht gewiß ist! – Haben Sie noch was zu befehlen? denn mein Weg ist der weiteste: wir wollen heute noch über die Grenze."

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "So geh."

        hide marinelli

        show angelo at truecenter

        $ angelo_var = "{noalt}ANGELO."

        angelo "Wenn wieder was vorfällt, Herr Kammerherr, – Sie wissen, wo ich zu erfragen bin. Was sich ein andrer zu tun getrauet, wird für mich auch keine Hexerei sein. Und billiger bin ich, als jeder andere."

        hide angelo

        show angelo at truecenter

        hide angelo

        show angelo at truecenter

        angelo "<{i}Geht ab.{/i}>"

        show angelo at truecenter

        show angelo at truecenter

        hide angelo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Gut das! – Aber doch nicht so recht gut. – Pfui, Angelo! so ein Knicker zu sein! Einen zweiten Schuß wäre er ja wohl noch wert gewesen. – Und wie er sich vielleicht nun martern muß, der arme Graf! – Pfui, Angelo! Das heißt sein Handwerk sehr grausam treiben;"

        marinelli "– und verpfuschen. – Aber davon muß der Prinz noch nichts wissen. Er muß erst selbst finden, wie zuträglich ihm dieser Tod ist. – Dieser Tod! – Was gäb' ich um die Gewißheit!"

        hide marinelli

    label Act_2_Scene_3:
        "{b}Dritter Auftritt{/b}"

        show der_prinz at left
        show marinelli at right

        show der_prinz at left
        show marinelli at right

        "<{i}Der Prinz. Marinelli.{/i}>"

        hide der_prinz
        hide marinelli

        hide der_prinz
        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Dort kömmt sie, die Allee herauf. Sie eilet vor dem Bedienten her. Die Furcht, wie es scheinet, beflügelt ihre Füße. Sie muß noch nichts argwohnen. Sie glaubt sich nur vor Räubern zu retten. – Aber wie lange kann das dauern?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "So haben wir sie doch fürs erste."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und wird die Mutter sie nicht aufsuchen? Wird der Graf ihr nicht nachkommen? Was sind wir alsdann weiter? Wie kann ich sie ihnen vorenthalten?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Auf das alles weiß ich freilich noch nichts zu antworten. Aber wir müssen sehen. Gedulden Sie sich, gnädiger Herr. Der erste Schritt mußte doch getan sein. –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wozu? wenn wir ihn zurücktun müssen."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Vielleicht müssen wir nicht. – Da sind tausend Dinge, auf die sich weiter fußen läßt. – Und vergessen Sie denn das Vornehmste?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Was kann ich vergessen, woran ich sicher noch nicht gedacht habe? – Das Vornehmste? was ist das?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Die Kunst zu gefallen, zu überreden, – die einem Prinzen, welcher liebt, nie fehlet."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Nie fehlet? Außer, wo er sie gerade am nötigsten brauchte. – Ich habe von dieser Kunst schon heut' einen zu schlechten Versuch gemacht. Mit allen Schmeicheleien und Beteuerungen konnt' ich ihr auch nicht ein Wort auspressen."

        der_prinz "Stumm und niedergeschlagen und zitternd stand sie da; wie eine Verbrecherin, die ihr Todesurteil höret. Ihre Angst steckte mich an, ich zitterte mit, und schloß mit einer Bitte um Vergebung. Kaum getrau' ich mir, sie wieder anzureden."

        der_prinz "– Bei ihrem Eintritte wenigstens wag' ich es nicht zu sein. Sie, Marinelli, müssen sie empfangen. Ich will hier in der Nähe hören, wie es abläuft; und kommen, wenn ich mich mehr gesammelt habe."

        hide der_prinz

    label Act_2_Scene_4:
        "{b}Vierter Auftritt{/b}"

        show marinelli at truecenter

        show marinelli at truecenter

        "<{i}Marinelli, und bald darauf dessen Bedienter.{/i}>"

        hide marinelli

        hide marinelli

        show battista at truecenter

        show battista at truecenter

        "<{i}Battista mit Emilien.{/i}>"

        hide battista

        hide battista

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn sie ihn nicht selbst stürzen gesehen – Und das muß sie wohl nicht; da sie so fortgeeilet – Sie kömmt. Auch ich will nicht das erste sein, was ihr hier in die Augen fällt."

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Er zieht sich in einen Winkel des Saales zurück.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        hide marinelli

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Nur hier herein, gnädiges Fräulein."

        hide battista

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}außer Atem.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Ah! – Ah! – Ich danke Ihm, mein Freund; – ich dank' Ihm. – Aber Gott, Gott! wo bin ich? – Und so ganz allein? Wo bleibt meine Mutter? Wo blieb der Graf? – Sie kommen doch nach? mir auf dem Fuße nach?"

        hide emilia

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Ich vermute."

        hide battista

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Er vermutet? Er weiß es nicht? Er sah sie nicht? – Ward nicht gar hinter uns geschossen? –"

        hide emilia

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Geschossen? – Das wäre! –"

        hide battista

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Ganz gewiß! Und das hat den Grafen, oder meine Mutter getroffen. –"

        hide emilia

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Ich will gleich nach ihnen ausgehen."

        hide battista

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nicht ohne mich. – Ich will mit; ich muß mit: komm Er, mein Freund!"

        hide emilia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}der plötzlich herzu tritt, als ob er eben herein käme.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Ah, gnädiges Fräulein! Was für ein Unglück, oder vielmehr, was für ein Glück, – was für ein glückliches Unglück verschafft uns die Ehre –"

        hide marinelli

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}stutzend.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Wie? Sie hier, mein Herr? – Ich bin also wohl bei Ihnen? – Verzeihen Sie, Herr Kammerherr. Wir sind von Räubern ohnfern überfallen worden. Da kamen uns gute Leute zu Hülfe; – und dieser ehrliche Mann hob mich aus dem Wagen, und brachte mich hierher."

        emilia "– Aber ich erschrecke, mich allein gerettet zu sehen. Meine Mutter ist noch in der Gefahr. Hinter uns ward sogar geschossen. Sie ist vielleicht tot; – und ich lebe? – Verzeihen Sie. Ich muß fort; ich muß wieder hin, – wo ich gleich hätte bleiben sollen."

        hide emilia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Beruhigen Sie sich, gnädiges Fräulein. Es stehet alles gut; sie werden bald bei Ihnen sein, die geliebten Personen, für die Sie so viel zärtliche Angst empfinden. – Indes, Battista, geh', lauf: sie dürften vielleicht nicht wissen, wo das Fräulein ist."

        marinelli "Sie dürften sie vielleicht in einem von den Wirtschaftshäusern des Gartens suchen. Bringe sie unverzüglich hierher."

        hide marinelli

        show marinelli at left
        show battista at right

        hide marinelli

        show marinelli at left
        show battista at right

        marinelli "<{i}Battista geht ab.{/i}>"

        hide battista

        show marinelli at truecenter

        hide battista

        show marinelli at truecenter

        hide marinelli

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Gewiß? Sind sie alle geborgen? Ist ihnen nichts widerfahren? – Ah, was ist dieser Tag für ein Tag des Schreckens für mich! – Aber ich sollte nicht hier bleiben; ich sollte ihnen entgegen eilen –"

        hide emilia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wozu das, gnädiges Fräulein? Sie sind ohnedem"

        marinelli "schon ohne Atem und Kräfte. Erholen Sie sich vielmehr, und geruhen in ein Zimmer zu treten, wo mehr Bequemlichkeit ist. – Ich will wetten, daß der Prinz schon selbst um Ihre teuere ehrwürdige Mutter ist, und sie Ihnen zuführet."

        hide marinelli

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Wer, sagen Sie?"

        hide emilia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Unser gnädigster Prinz selbst."

        hide marinelli

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}äußerst bestürzt.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Der Prinz?"

        hide emilia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Er floh, auf die erste Nachricht, Ihnen zu Hülfe. – Er ist höchst ergrimmt, daß ein solches Verbrechen ihm so nahe, unter seinen Augen gleichsam, hat dürfen gewagt werden."

        marinelli "Er läßt den Tätern nachsetzen, und ihre Strafe, wenn sie ergriffen werden, wird unerhört sein."

        hide marinelli

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Der Prinz! – Wo bin ich denn also?"

        hide emilia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Auf Dosalo, dem Lustschlosse des Prinzen."

        hide marinelli

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Welch ein Zufall! – Und Sie glauben, daß er gleich selbst erscheinen könne? – Aber doch in Gesellschaft meiner Mutter?"

        hide emilia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Hier ist er schon."

        hide marinelli

    label Act_2_Scene_5:
        "{b}Fünfter Auftritt{/b}"

        show der_prinz at left
        show emilia at truecenter
        show marinelli at right

        show der_prinz at left
        show emilia at truecenter
        show marinelli at right

        "<{i}Der Prinz. Emilia. Marinelli.{/i}>"

        hide der_prinz
        hide emilia
        hide marinelli

        hide der_prinz
        hide emilia
        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wo ist sie? wo? – Wir suchen Sie überall, schönstes Fräulein. – Sie sind doch wohl? – Nun so ist alles wohl! Der Graf, Ihre Mutter, –"

        hide der_prinz

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Ah, gnädigster Herr! wo sind sie? Wo ist meine Mutter?"

        hide emilia

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Nicht weit; hier ganz in der Nähe."

        hide der_prinz

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Gott, in welchem Zustande werde ich die eine, oder den andern, vielleicht treffen! Ganz gewiß treffen! – denn Sie verhehlen mir, gnädiger Herr – ich seh' es, Sie verhehlen mir –"

        hide emilia

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Nicht doch, bestes Fräulein. – Geben Sie mir Ihren Arm, und folgen Sie mir getrost."

        hide der_prinz

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}unentschlossen.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Aber – wenn ihnen nichts widerfahren – wenn meine Ahnungen mich trügen; – warum sind sie"

        emilia "nicht schon hier? Warum kamen sie nicht mit Ihnen, gnädiger Herr?"

        hide emilia

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So eilen Sie doch, mein Fräulein, alle diese Schreckenbilder mit eins verschwinden zu sehen. –"

        hide der_prinz

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Was soll ich tun!"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}Die Hände ringend.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        hide emilia

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wie, mein Fräulein? Sollten Sie einen Verdacht gegen mich hegen? –"

        hide der_prinz

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}die vor ihm niederfällt.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Zu Ihren Füßen, gnädiger Herr –"

        hide emilia

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}sie aufhebend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Ich bin äußerst beschämt. – Ja, Emilia, ich verdiene diesen stummen Vorwurf. – Mein Betragen diesen Morgen, ist nicht zu rechtfertigen; – zu entschuldigen höchstens. Verzeihen Sie meiner Schwachheit."

        der_prinz "Ich hätte Sie mit keinem Geständnisse beunruhigen sollen, von dem ich keinen Vorteil zu erwarten habe. Auch ward ich durch die sprachlose Bestürzung, mit der Sie es anhörten, oder vielmehr nicht anhörten, genugsam bestraft."

        der_prinz "– Und könnt' ich schon diesen Zufall, der mir nochmals, ehe alle meine Hoffnung auf ewig verschwindet, – mir nochmals das Glück Sie zu sehen und zu sprechen verschafft; könnt' ich schon diesen Zufall für den Wink eines günstigen Glückes erklären,"

        der_prinz "– für den wunderbarsten Aufschub meiner endlichen Verurteilung erklären, um nochmals um Gnade flehen zu dürfen: so will ich doch – Beben Sie nicht, mein Fräulein – einzig und allein von Ihrem Blicke abhangen. Kein Wort, kein Seufzer, soll Sie beleidigen."

        der_prinz "– Nur kränke mich nicht Ihr Mißtrauen. Nur zweifeln Sie keinen Augenblick an der unumschränktesten Gewalt, die Sie über mich haben. Nur falle Ihnen nie bei, daß Sie eines andern Schutzes gegen mich bedürfen."

        der_prinz "– Und nun kommen Sie, mein Fräulein, – kommen Sie, wo Entzückungen auf Sie warten, die Sie mehr billigen."

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Er führt sie, nicht ohne Sträuben, ab.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Folgen Sie uns, Marinelli. –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Folgen Sie uns, – das mag heißen: folgen Sie uns nicht! – Was hätte ich ihnen auch zu folgen? Er mag sehen, wie weit er es unter vier Augen mit ihr bringt. – Alles, was ich zu tun habe, ist, – zu verhindern, daß sie nicht gestöret werden."

        marinelli "Von dem Grafen zwar, hoffe ich nun wohl nicht."

        marinelli "Aber von der Mutter; von der Mutter! Es sollte mich sehr wundern, wenn die so ruhig abgezogen wäre, und ihre Tochter im Stiche gelassen hätte. – Nun, Battista? was gibts?"

        hide marinelli

    label Act_2_Scene_6:
        "{b}Sechster Auftritt{/b}"

        show battista at left
        show marinelli at right

        show battista at left
        show marinelli at right

        "<{i}Battista. Marinelli.{/i}>"

        hide battista
        hide marinelli

        hide battista
        hide marinelli

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA"

        hide battista

        show battista at truecenter

        hide battista

        show battista at truecenter

        battista "<{i}eiligst.{/i}>"

        show battista at truecenter

        show battista at truecenter

        battista "Die Mutter, Herr Kammerherr –"

        hide battista

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Dacht' ichs doch! – Wo ist sie?"

        hide marinelli

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Wann Sie ihr nicht zuvorkommen, so wird sie den Augenblick hier sein. – Ich war gar nicht Willens, wie Sie mir zum Schein geboten, mich nach ihr umzusehen: als ich ihr Geschrei von weitem hörte."

        battista "Sie ist der Tochter auf der Spur, und wo nur nicht – unserm ganzen Anschlage! Alles, was in dieser einsamen Gegend von Menschen ist, hat sich um sie versammelt; und jeder will der sein, der ihr den Weg weiset."

        battista "Ob man ihr schon gesagt, daß der Prinz hier ist, daß Sie hier sind, weiß ich nicht. – Was wollen Sie tun?"

        hide battista

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Laß sehen! –"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Er überlegt.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Sie nicht einlassen, wenn sie weiß, daß die Tochter hier ist? – Das geht nicht. – Freilich, sie wird Augen machen, wenn sie den Wolf bei dem Schäfchen sieht. – Augen? Das möchte noch sein. Aber der Himmel sei unsern Ohren gnädig! – Nun was?"

        marinelli "die beste Lunge erschöpft sich; auch so gar eine weibliche. Sie hören alle auf zu schreien, wenn sie nicht mehr können. – Dazu, es ist doch einmal die Mutter, die wir auf unserer Seite haben müssen."

        marinelli "– Wenn ich die Mütter recht kenne: – so etwas von einer Schwiegermutter eines Prinzen zu sein, schmeichelt die meisten. – Laß sie kommen, Battista, laß sie kommen!"

        hide marinelli

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Hören Sie! hören Sie!"

        hide battista

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA GALOTTI"

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}innerhalb.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        claudia "Emilia! Emilia! Mein Kind, wo bist du?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Geh, Battista, und suche nur ihre neugierigen Begleiter zu entfernen."

        hide marinelli

    label Act_2_Scene_7:
        "{b}Siebenter Auftritt{/b}"

        show claudia at left
        show battista at truecenter
        show marinelli at right

        show claudia at left
        show battista at truecenter
        show marinelli at right

        "<{i}Claudia Galotti. Battista. Marinelli.{/i}>"

        hide claudia
        hide battista
        hide marinelli

        hide claudia
        hide battista
        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA"

        hide claudia

        show claudia at left
        show battista at right

        hide claudia

        show claudia at left
        show battista at right

        claudia "<{i}die in die Türe tritt, indem Battista heraus gehen will.{/i}>"

        hide battista

        show claudia at truecenter

        hide battista

        show claudia at truecenter

        claudia "Ha! der hob sie aus dem Wagen! Der führte sie fort! Ich erkenne dich. Wo ist sie? Sprich, Unglücklicher!"

        hide claudia

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Das ist mein Dank?"

        hide battista

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "O, wenn du Dank verdienest:"

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}In einem gelinden Tone.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        claudia "– so verzeihe mir, ehrlicher Mann! – Wo ist sie? – Laßt mich sie nicht länger entbehren. Wo ist sie?"

        hide claudia

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "O, Ihre Gnaden, sie könnte in dem Schoße der Seligkeit nicht aufgehobner sein. – Hier mein Herr wird Ihre Gnaden zu ihr führen."

        hide battista

        show battista at truecenter

        hide battista

        show battista at truecenter

        battista "<{i}Gegen einige Leute, welche nachdringen wollen.{/i}>"

        show battista at truecenter

        show battista at truecenter

        battista "Zurück da! ihr!"

        hide battista

    label Act_2_Scene_8:
        "{b}Achter Auftritt{/b}"

        show claudia at left
        show marinelli at right

        show claudia at left
        show marinelli at right

        "<{i}Claudia Galotti. Marinelli.{/i}>"

        hide claudia
        hide marinelli

        hide claudia
        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Dein Herr? –"

        hide claudia

        show claudia at left
        show marinelli at right

        hide claudia

        show claudia at left
        show marinelli at right

        claudia "<{i}Erblickt den Marinelli und fährt zurück.{/i}>"

        hide marinelli

        show claudia at truecenter

        hide marinelli

        show claudia at truecenter

        claudia "Ha! – Das dein Herr? – Sie hier, mein Herr? Und hier meine Tochter? Und Sie, Sie sollen mich zu ihr führen?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Mit vielem Vergnügen, gnädige Frau."

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Halten Sie! – Eben fällt mir es bei – Sie waren es ja – nicht? – Der den Grafen diesen Morgen in meinem Hause aufsuchte? mit dem ich ihn allein ließ? mit dem er Streit bekam?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Streit? – Was ich nicht wüßte: ein unbedeutender Wortwechsel in herrschaftlichen Angelegenheiten –"

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Und Marinelli heißen Sie?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Marchese Marinelli."

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "So ist es richtig. – Hören Sie doch, Herr Marchese. – Marinelli war – der Name Marinelli war – begleitet mit einer Verwünschung – Nein, daß ich den edeln Mann nicht verleumde! – begleitet mit keiner Verwünschung – Die Verwünschung"

        claudia "denk' ich hinzu – Der Name Marinelli war das letzte Wort des sterbenden Grafen."

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Des sterbenden Grafen? Grafen Appiani? – Sie hören, gnädige Frau, was mir in Ihrer seltsamen Rede am meisten auffällt. – Des sterbenden Grafen? – Was Sie sonst sagen wollen, versteh' ich nicht."

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA"

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}bitter und langsam.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        claudia "Der Name Marinelli war das letzte Wort des sterbenden Grafen! – Verstehen Sie nun? – Ich verstand es erst auch nicht: ob schon mit einem Tone gesprochen – mit einem Tone! – Ich höre ihn noch! Wo waren meine Sinne, daß sie diesen Ton nicht sogleich verstanden?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun, gnädige Frau? – Ich war von je her des Grafen Freund; sein vertrautester Freund. Also, wenn er mich noch im Sterben nannte –"

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Mit dem Tone? – Ich kann ihn nicht nachmachen; ich kann ihn nicht beschreiben; aber er enthielt alles! alles! – Was? Räuber wären es gewesen, die uns anfielen? – Mörder waren es; erkaufte Mörder! – Und Marinelli, Marinelli war das letzte Wort des sterbenden Grafen!"

        claudia "Mit einem Tone!"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Mit einem Tone? – Ist es erhört, auf einen Ton, in einem Augenblicke des Schreckens vernommen, die Anklage eines rechtschaffnen Mannes zu gründen?"

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Ha, könnt' ich ihn nur vor Gerichte stellen, diesen Ton! – Doch, weh mir! Ich vergesse darüber meine Tochter. – Wo ist sie? – Wie? auch tot? – Was konnte meine Tochter dafür, daß Appiani dein Feind war?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich verzeihe der bangen Mutter. – Kommen Sie, gnädige Frau – Ihre Tochter ist hier; in einem von den nächsten Zimmern: und hat sich hoffentlich von ihrem Schrecken schon völlig erholt. Mit der zärtlichsten Sorgfalt ist der Prinz selbst um sie beschäftiget –"

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wer? – Wer selbst?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Der Prinz."

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Der Prinz? – Sagen Sie wirklich, der Prinz? – Unser Prinz?"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Welcher sonst?"

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Nun dann! – Ich unglückselige Mutter! – Und ihr"

        claudia "Vater! ihr Vater! – Er wird den Tag ihrer Geburt verfluchen. Er wird mich verfluchen."

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Um des Himmels willen, gnädige Frau! Was fällt Ihnen nun ein?"

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Es ist klar! – Ist es nicht? – Heute im Tempel! vor den Augen der Allerreinesten! in der nähern Gegenwart des Ewigen! – begann das Bubenstück; da brach es aus!"

        hide claudia

        show claudia at left
        show marinelli at right

        hide claudia

        show claudia at left
        show marinelli at right

        claudia "<{i}Gegen den Marinelli.{/i}>"

        hide marinelli

        show claudia at truecenter

        hide marinelli

        show claudia at truecenter

        claudia "Ha, Mörder! feiger, elender Mörder! Nicht tapfer genug, mit eigner Hand zu morden; aber nichtswürdig genug, zu Befriedigung eines fremden Kitzels zu morden! – morden zu lassen! – Abschaum aller Mörder!"

        claudia "– Was ehrliche Mörder sind, werden dich unter sich nicht dulden! Dich! Dich! – Denn warum soll ich dir nicht alle meine Galle, allen meinen Geifer mit einem einzigen Worte ins Gesicht speien? – Dich! Dich Kuppler!"

        hide claudia

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie schwärmen, gute Frau. – Aber mäßigen Sie wenigstens Ihr wildes Geschrei, und bedenken Sie, wo Sie sind."

        hide marinelli

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wo ich bin? Bedenken, wo ich bin? – Was kümmert es die Löwin, der man die Jungen geraubet, in wessen Walde sie brüllet?"

        hide claudia

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}innerhalb.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Ha, meine Mutter! Ich höre meine Mutter!"

        hide emilia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Ihre Stimme? Das ist sie! Sie hat mich gehört; sie hat mich gehört. Und ich sollte nicht schreien? – Wo bist du, mein Kind? Ich komme, ich komme!"

        hide claudia

        show claudia at left
        show marinelli at right

        hide claudia

        show claudia at left
        show marinelli at right

        claudia "<{i}Sie stürzt in das Zimmer, und Marinelli ihr nach.{/i}>"

        hide marinelli

        show claudia at truecenter

        hide marinelli

        show claudia at truecenter

        hide claudia

label Act_4:
    play music "audio/music/32.mp3" fadeout 1.0 fadein 1.0

    scene 4 with fade

    "{b}Vierter Aufzug{/b}"

    "<{i}Die Szene bleibt.{/i}>"

    menu:
        "{color=#000}Erster Auftritt{/color}":
            jump Act_3_Scene_1
        "{color=#000}Zweiter Auftritt{/color}":
            jump Act_3_Scene_2
        "{color=#000}Dritter Auftritt{/color}":
            jump Act_3_Scene_3
        "{color=#000}Vierter Auftritt{/color}":
            jump Act_3_Scene_4
        "{color=#000}Fünfter Auftritt{/color}":
            jump Act_3_Scene_5
        "{color=#000}Sechster Auftritt{/color}":
            jump Act_3_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_3_Scene_6_1

label Further_Act_3_Scene_6_1:
    menu:
        "{color=#000}Siebenter Auftritt{/color}":
            jump Act_3_Scene_7
        "{color=#000}Achter Auftritt{/color}":
            jump Act_3_Scene_8

    label Act_3_Scene_1:
        "{b}Erster Auftritt{/b}"

        show der_prinz at left
        show marinelli at right

        show der_prinz at left
        show marinelli at right

        "<{i}Der Prinz. Marinelli.{/i}>"

        hide der_prinz
        hide marinelli

        hide der_prinz
        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}als aus dem Zimmer von Emilien kommend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Kommen Sie, Marinelli! Ich muß mich erholen – und muß Licht von Ihnen haben."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "O der mütterlichen Wut! Ha! ha! ha!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sie lachen?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn Sie gesehen hätten, Prinz, wie toll sich hier, hier im Saale, die Mutter gebärdete – Sie hörten sie ja wohl schreien! – und wie zahm sie auf einmal ward, bei dem ersten Anblicke von Ihnen – – Ha! ha!"

        marinelli "– Das weiß ich ja wohl, daß keine Mutter einem Prinzen die Augen auskratzt, weil er ihre Tochter schön findet!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sie sind ein schlechter Beobachter! – Die Tochter stürzte der Mutter ohnmächtig in die Arme. Darüber vergaß die Mutter ihre Wut: nicht über mir. Ihre Tochter schonte sie, nicht mich;"

        der_prinz "wenn sie es nicht lauter, nicht deutlicher sagte, – was ich lieber selbst nicht gehört, nicht verstanden haben will."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Was, gnädiger Herr?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wozu die Verstellung? – Heraus damit. Ist es wahr? oder ist es nicht wahr?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und wenn es denn wäre!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wenn es denn wäre? – Also ist es? – Er ist tot? tot? –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Drohend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Marinelli! Marinelli!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Bei Gott! bei dem allgerechten Gott! ich bin unschuldig an diesem Blute. – Wenn Sie mir vorher gesagt hätten, daß es dem Grafen das Leben kosten werde – Nein, nein! und wenn es mir selbst das Leben gekostet hätte! –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn ich Ihnen vorher gesagt hätte? – Als ob sein Tod in meinem Plane gewesen wäre! Ich hatte es dem Angelo auf die Seele gebunden, zu verhüten, daß niemanden Leides geschähe."

        marinelli "Es würde auch ohne die geringste Gewalttätigkeit abgelaufen sein, wenn sich der Graf nicht die erste erlaubt hätte. Er schoß Knall und Fall den einen nieder."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wahrlich; er hätte sollen Spaß verstehen!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Daß Angelo sodann in Wut kam, und den Tod seines Gefährten rächte –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Freilich, das ist sehr natürlich!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich hab' es ihm genug verwiesen."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Verwiesen? Wie freundschaftlich! – Warnen Sie ihn, daß er sich in meinem Gebiete nicht betreten läßt. Mein Verweis möchte so freundschaftlich nicht sein."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Recht wohl! – Ich und Angelo; Vorsatz und Zufall: alles ist eins. – Zwar ward es voraus bedungen, zwar ward es voraus versprochen, daß keiner der Unglücksfälle, die sich dabei eräugnen könnten, mir zu Schulden kommen solle –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Die sich dabei eräugnen – könnten, sagen Sie? oder sollten?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Immer besser! – Doch, gnädiger Herr, – ehe Sie mir es mit dem trocknen Worte sagen, wofür Sie mich halten – eine einzige Vorstellung! Der Tod des Grafen ist mir nichts weniger, als gleichgültig. Ich hatte ihn ausgefodert; er war mir Genugtuung schuldig;"

        marinelli "er ist ohne diese aus der Welt gegangen; und meine Ehre bleibt beleidiget. Gesetzt, ich verdiente unter jeden andern Umständen den Verdacht, den Sie gegen mich hegen: aber auch unter diesen? –"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Mit einer angenommenen Hitze.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Wer das von mir denken kann! –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}nachgebend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Nun gut, nun gut –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Daß er noch lebte! O daß er noch lebte! Alles, alles in der Welt wollte ich darum geben –"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Bitter.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "selbst die Gnade meines Prinzen, – diese unschätzbare, nie zu verscherzende Gnade – wollt' ich drum geben!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich verstehe. – Nun gut, nun gut. Sein Tod war Zufall, bloßer Zufall. Sie versichern es; und ich, ich glaub' es."

        der_prinz "– Aber wer mehr? Wer wird es mehr glauben? Auch der Vater? Auch die Mutter? Auch Emilia? – Auch die Welt?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}kalt.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Schwerlich."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Und wenn man es nicht glaubt, was wird man denn glauben? – Sie zucken die Achsel? – Ihren Angelo wird man für das Werkzeug, und mich für den Täter halten –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}noch kälter.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Wahrscheinlich genug."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Mich! mich selbst! – Oder ich muß von Stund an alle Absicht auf Emilien aufgeben –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}höchst gleichgültig.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Was Sie auch gemußt hätten – wenn der Graf noch lebte. –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}heftig, aber sich gleich wieder fassend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Marinelli! – Doch, Sie sollen mich nicht wild machen. – Es sei so – Es ist so!"

        der_prinz "Und das wollen Sie doch nur sagen: der Tod des Grafen ist für mich ein Glück – das größte Glück, was mir begegnen konnte, – das einzige Glück, was meiner Liebe zu statten kommen konnte. Und als dieses, – mag er doch geschehen sein, wie er will!"

        der_prinz "– Ein Graf mehr in der Welt, oder weniger! Denke ich Ihnen so recht? – Topp! auch ich erschrecke vor einem kleinen Verbrechen nicht. Nur, guter Freund, muß es ein kleines stilles Verbrechen, ein kleines heilsames Verbrechen sein."

        der_prinz "Und sehen Sie, unseres da, wäre nun gerade weder stille noch heilsam. Es hätte den Weg zwar gereiniget, aber zugleich gesperrt. Jedermann würde es uns auf den Kopf zusagen, – und leider hätten wir es gar nicht einmal begangen!"

        der_prinz "– Das liegt doch wohl nur bloß an Ihren weisen, wunderbaren Anstalten?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn Sie so befehlen –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Woran sonst? – Ich will Rede!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Es kömmt mehr auf meine Rechnung, was nicht darauf gehört."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Rede will ich!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun dann! Was läge an meinen Anstalten? daß den Prinzen bei diesem Unfalle ein so sichtbarer Verdacht trifft? – An dem Meisterstreiche liegt das, den er selbst meinen Anstalten mit einzumengen die Gnade hatte."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Er erlaube mir, ihm zu sagen, daß der Schritt, den"

        marinelli "er heute Morgen in der Kirche getan, – mit so vielem Anstande er ihn auch getan – so unvermeidlich er ihn auch tun mußte – daß dieser Schritt dennoch nicht in den Tanz gehörte."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Was verdarb er denn auch?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Freilich nicht den ganzen Tanz: aber doch voritzo den Takt."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Hm! Versteh' ich Sie?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Also, kurz und einfältig. Da ich die Sache übernahm, nicht wahr, da wußte Emilia von der Liebe des Prinzen noch nichts? Emiliens Mutter noch weniger. Wenn ich nun auf diesen Umstand baute? und der Prinz indes den Grund meines Gebäudes untergrub? –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}sich vor die Stirne schlagend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Verwünscht!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn er es nun selbst verriet, was er im Schilde führe?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Verdammter Einfall!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und wenn er es nicht selbst verraten hätte? – Traun! ich möchte doch wissen, aus welcher meiner Anstalten, Mutter oder Tochter den geringsten Argwohn gegen ihn schöpfen könnte?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Daß Sie Recht haben!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Daran tu' ich freilich sehr Unrecht – Sie werden verzeihen, gnädiger Herr –"

        hide marinelli

    label Act_3_Scene_2:
        "{b}Zweiter Auftritt{/b}"

        show battista at left
        show der_prinz at truecenter
        show marinelli at right

        show battista at left
        show der_prinz at truecenter
        show marinelli at right

        "<{i}Battista. Der Prinz. Marinelli.{/i}>"

        hide battista
        hide der_prinz
        hide marinelli

        hide battista
        hide der_prinz
        hide marinelli

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA"

        hide battista

        show battista at truecenter

        hide battista

        show battista at truecenter

        battista "<{i}eiligst.{/i}>"

        show battista at truecenter

        show battista at truecenter

        battista "Eben kömmt die Gräfin an."

        hide battista

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Die Gräfin? Was für eine Gräfin?"

        hide der_prinz

        show battista at truecenter

        $ battista_var = "{noalt}BATTISTA."

        battista "Orsina."

        hide battista

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Orsina? – Marinelli! – Orsina? – Marinelli!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ich erstaune darüber, nicht weniger als Sie selbst."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Geh, lauf, Battista: sie soll nicht aussteigen. Ich bin nicht hier. Ich bin für sie nicht hier. Sie soll augenblicklich wieder umkehren. Geh, lauf! –"

        hide der_prinz

        show der_prinz at left
        show battista at right

        hide der_prinz

        show der_prinz at left
        show battista at right

        der_prinz "<{i}Battista geht ab.{/i}>"

        hide battista

        show der_prinz at truecenter

        hide battista

        show der_prinz at truecenter

        der_prinz "Was will die Närrin? Was untersteht sie sich? Wie weiß sie, daß"

        der_prinz "wir hier sind? Sollte sie wohl auf Kundschaft kommen? Sollte sie wohl schon etwas vernommen haben? – Ah, Marinelli! So reden Sie, so antworten Sie doch! – Ist er beleidiget der Mann, der mein Freund sein will? Und durch einen elenden Wortwechsel beleidiget?"

        der_prinz "Soll ich ihn um Verzeihung bitten?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ah, mein Prinz, so bald Sie wieder Sie sind, bin ich mit ganzer Seele wieder der Ihrige! – Die Ankunft der Orsina ist mir ein Rätsel, wie Ihnen. Doch abweisen wird sie schwerlich sich lassen. Was wollen Sie tun?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sie durchaus nicht sprechen; mich entfernen –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wohl! und nur geschwind. Ich will sie empfangen –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Aber bloß, um sie gehen zu heißen. – Weiter geben Sie mit ihr sich nicht ab. Wir haben andere Dinge hier zu tun –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nicht doch, Prinz! Diese andern Dinge sind getan. Fassen Sie doch Mut! Was noch fehlt, kömmt sicherlich von selbst. – Aber hör' ich sie nicht schon? – Eilen Sie, Prinz! – Da,"

        hide marinelli

        show marinelli at left
        show der_prinz at right

        hide marinelli

        show marinelli at left
        show der_prinz at right

        marinelli "<{i}Auf ein Kabinett zeigend, in welches sich der Prinz begibt.{/i}>"

        hide der_prinz

        show marinelli at truecenter

        hide der_prinz

        show marinelli at truecenter

        marinelli "wenn Sie wollen, werden Sie uns hören können. – Ich fürchte, ich fürchte, sie ist nicht zu ihrer besten Stunde ausgefahren."

        hide marinelli

    label Act_3_Scene_3:
        "{b}Dritter Auftritt{/b}"

        show orsina at left
        show marinelli at right

        show orsina at left
        show marinelli at right

        "<{i}Die Gräfin Orsina. Marinelli.{/i}>"

        hide orsina
        hide marinelli

        hide orsina
        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at left
        show marinelli at right

        hide orsina

        show orsina at left
        show marinelli at right

        orsina "<{i}ohne den Marinelli anfangs zu erblicken.{/i}>"

        hide marinelli

        show orsina at truecenter

        hide marinelli

        show orsina at truecenter

        orsina "Was ist das? – Niemand kömmt mir entgegen, außer ein Unverschämter, der mir lieber gar den Eintritt verweigert hätte? – Ich bin doch zu Dosalo? Zu dem Dosalo, wo mir sonst ein ganzes Heer geschäftiger Augendiener entgegen stürzte?"

        orsina "wo mich sonst Liebe und Entzücken erwarteten? – Der Ort ist es; aber, aber! – Sieh' da, Marinelli! – Recht gut, daß der Prinz Sie mitgenommen. – Nein, nicht gut! Was ich mit ihm auszumachen hätte, hätte ich nur mit ihm auszumachen. – Wo ist er?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Der Prinz, meine gnädige Gräfin?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wer sonst?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie vermuten ihn also hier? wissen ihn hier? – Er wenigstens ist der Gräfin Orsina hier nicht vermutend."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nicht? So hat er meinen Brief heute Morgen nicht erhalten?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ihren Brief? Doch ja; ich erinnere mich, daß er eines Briefes von Ihnen erwähnte."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nun? habe ich ihn nicht in diesem Briefe auf heute um eine Zusammenkunft hier auf Dosalo gebeten? – Es ist wahr, es hat ihm nicht beliebet, mir schriftlich zu antworten. Aber ich erfuhr, daß er eine Stunde darauf wirklich nach Dosalo abgefahren."

        orsina "Ich glaubte, das sei Antworts genug; und ich komme."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ein sonderbarer Zufall!"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Zufall? – Sie hören ja, daß es verabredet worden. So gut, als verabredet. Von meiner Seite, der Brief: von seiner, die Tat. – Wie er da steht, der Herr Marchese! Was er für Augen macht! Wundert sich das Gehirnchen? und worüber denn?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie schienen gestern so weit entfernt, dem Prinzen jemals wieder vor die Augen zu kommen."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Beßrer Rat kömmt über Nacht. – Wo ist er? wo ist er? – Was gilts, er ist in dem Zimmer, wo ich das Gequicke, das Gekreusche hörte? – Ich wollte herein, und der Schurke vom Bedienten trat vor."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Meine liebste, beste Gräfin –"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Es war ein weibliches Gekreusche. Was gilts, Marinelli? – O sagen Sie mir doch, sagen Sie mir – wenn ich anders Ihre liebste, beste Gräfin bin – Verdammt, über das Hofgeschmeiß! So viel Worte, so viel Lügen!"

        orsina "– Nun was liegt daran, ob Sie mir es voraus sagen, oder nicht? Ich werd' es ja wohl sehen."

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Will gehen.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}der sie zurück hält.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Wohin?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wo ich längst sein sollte. – Denken Sie, daß es schicklich ist, mit Ihnen hier in dem Vorgemache einen elenden Schnickschnack zu halten, indes der Prinz in dem Gemache auf mich wartet?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie irren sich, gnädige Gräfin. Der Prinz erwartet"

        marinelli "Sie nicht. Der Prinz kann Sie hier nicht sprechen, – will Sie nicht sprechen."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Und wäre doch hier? und wäre doch auf meinen Brief hier?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nicht auf Ihren Brief –"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Den er ja erhalten, sagen Sie –"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Erhalten, aber nicht gelesen."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}heftig.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Nicht gelesen? –"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Minder heftig.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Nicht gelesen? –"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Wehmütig, und eine Träne aus dem Auge wischend.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Nicht einmal gelesen?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Aus Zerstreuung, weiß ich. – Nicht aus Verachtung."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}stolz.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Verachtung? – Wer denkt daran? – Wem brauchen Sie das zu sagen? – Sie sind ein unverschämter Tröster, Marinelli! – Verachtung! Verachtung! Mich verachtet man auch! mich! –"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Gelinder, bis zum Tone der Schwermut.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Freilich liebt er mich nicht mehr. Das ist ausgemacht. Und an die Stelle der Liebe trat in seiner Seele etwas anders. Das ist natürlich. Aber warum denn eben Verachtung? Es braucht ja nur Gleichgültigkeit zu sein. Nicht wahr, Marinelli?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Allerdings, allerdings."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}höhnisch.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Allerdings? – O des weisen Mannes, den man sagen lassen kann, was man will! – Gleichgültigkeit! Gleichgültigkeit an die Stelle der Liebe? – Das heißt, Nichts an die Stelle von Etwas."

        orsina "Denn lernen Sie, nachplauderndes Hofmännchen, lernen Sie von einem Weibe, daß Gleichgültigkeit ein leeres Wort, ein bloßer Schall ist, dem nichts, gar nichts entspricht. Gleichgültig ist die Seele nur gegen das, woran sie nicht denkt;"

        orsina "nur gegen ein Ding, das für sie kein Ding ist. Und nur gleichgültig für ein Ding, das kein Ding ist, – das ist so viel, als gar nicht gleichgültig. – Ist dir das zu hoch, Mensch?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}vor sich.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "O weh! wie wahr ist es, was ich fürchtete!"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Was murmeln Sie da?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Lauter Bewunderung! – Und wem ist es nicht bekannt, gnädige Gräfin, daß Sie eine Philosophin sind?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nicht wahr? – Ja, ja; ich bin eine. – Aber habe ich mir es itzt merken lassen, daß ich eine bin? – O pfui, wenn ich mir es habe merken lassen; und wenn ich mir es öftrer"

        orsina "habe merken lassen! Ist es wohl noch Wunder, daß mich der Prinz verachtet? Wie kann ein Mann ein Ding lieben, das, ihm zum Trotze, auch denken will? Ein Frauenzimmer, das denket, ist eben so ekel als ein Mann, der sich schminket."

        orsina "Lachen soll es, nichts als lachen, um immerdar den gestrengen Herrn der Schöpfung bei guter Laune zu erhalten. – Nun, worüber lach' ich denn gleich, Marinelli? – Ach, ja wohl! Über den Zufall! daß ich dem Prinzen schreibe, er soll nach Dosalo kommen;"

        orsina "daß der Prinz meinen Brief nicht lieset, und daß er doch nach Dosalo kömmt. Ha! ha! ha! Wahrlich ein sonderbarer Zufall! Sehr lustig, sehr närrisch! – Und Sie lachen nicht mit, Marinelli?"

        orsina "– Mitlachen kann ja wohl der gestrenge Herr der Schöpfung, ob wir arme Geschöpfe gleich nicht mitdenken dürfen. –"

        orsina "Ernsthaft und befehlend."

        orsina "So lachen Sie doch!"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Gleich, gnädige Gräfin, gleich!"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Stock! Und darüber geht der Augenblick vorbei. Nein, nein, lachen Sie nur nicht. – Denn sehen Sie, Marinelli,"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Nachdenkend bis zur Rührung.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "was mich so herzlich zu lachen macht, das hat auch seine ernsthafte – sehr ernsthafte Seite. Wie alles in der Welt! – Zufall? Ein Zufall wär' es, daß der Prinz nicht daran gedacht, mich hier zu sprechen, und mich doch hier sprechen muß? Ein Zufall?"

        orsina "– Glauben Sie mir, Marinelli: das Wort Zufall ist Gotteslästerung. Nichts unter der Sonne ist Zufall; – am wenigsten das, wovon die Absicht so klar in die Augen leuchtet."

        orsina "– Allmächtige, allgütige Vorsicht, vergib mir, daß ich mit diesem albernen Sünder einen Zufall genennet habe, was so offenbar dein Werk, wohl gar dein unmittelbares Werk ist! –"

        hide orsina

        show orsina at left
        show marinelli at right

        hide orsina

        show orsina at left
        show marinelli at right

        orsina "<{i}Hastig gegen Marinelli.{/i}>"

        hide marinelli

        show orsina at truecenter

        hide marinelli

        show orsina at truecenter

        orsina "Kommen Sie mir, und verleiten Sie mich noch einmal zu so einem Frevel!"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}vor sich.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Das geht weit! – Aber gnädige Gräfin –"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Still mit dem Aber! Die Aber kosten Überlegung; – und mein Kopf! mein Kopf!"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Sich mit der Hand die Stirne haltend.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "– Machen Sie, Marinelli, machen Sie, daß ich ihn bald spreche, den Prinzen; sonst bin ich es wohl gar nicht im Stande. – Sie sehen, wir sollen uns sprechen; wir müssen uns sprechen –"

        hide orsina

    label Act_3_Scene_4:
        "{b}Vierter Auftritt{/b}"

        show der_prinz at left
        show orsina at truecenter
        show marinelli at right

        show der_prinz at left
        show orsina at truecenter
        show marinelli at right

        "<{i}Der Prinz. Orsina. Marinelli.{/i}>"

        hide der_prinz
        hide orsina
        hide marinelli

        hide der_prinz
        hide orsina
        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}indem er aus dem Kabinette tritt, vor sich.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Ich muß ihm zu Hülfe kommen –"

        hide der_prinz

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}die ihn erblickt, aber unentschlüssig bleibt, ob sie auf ihn zugehen soll.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Ha! da ist er."

        hide orsina

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}geht quer über den Saal, bei ihr vorbei, nach den andern Zimmern, ohne sich im Reden aufzuhalten.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Sieh da! unsere schöne Gräfin. – Wie sehr betaure ich, Madame, daß ich mir die Ehre Ihres Besuchs für heute so wenig zu Nutze machen kann! Ich bin beschäftiget. Ich bin nicht allein. – Ein andermal, meine liebe Gräfin! Ein andermal."

        der_prinz "– Itzt halten Sie länger sich nicht auf. Ja nicht länger! – Und Sie, Marinelli, ich erwarte Sie. –"

        hide der_prinz

    label Act_3_Scene_5:
        "{b}Fünfter Auftritt{/b}"

        show orsina at left
        show marinelli at right

        show orsina at left
        show marinelli at right

        "<{i}Orsina. Marinelli.{/i}>"

        hide orsina
        hide marinelli

        hide orsina
        hide marinelli

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Haben Sie es, gnädige Gräfin, nun von ihm selbst gehört, was Sie mir nicht glauben wollen?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}wie betäubt.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Hab' ich? hab' ich wirklich?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wirklich."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}mit Rührung.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "»Ich bin beschäftiget. Ich bin nicht allein.« Ist das die Entschuldigung ganz, die ich wert bin? Wen weiset man damit nicht ab? Jeden Überlästigen, jeden Bettler. Für mich keine einzige Lüge mehr? Keine einzige kleine Lüge mehr, für mich? – Beschäftiget? womit denn?"

        orsina "Nicht allein? wer wäre denn bei ihm? – Kommen Sie, Marinelli; aus Barmherzigkeit, lieber Marinelli! Lügen Sie mir eines auf eigene Rechnung vor. Was kostet Ihnen denn eine Lüge? – Was hat er zu tun? Wer ist bei ihm? – Sagen Sie mir;"

        orsina "sagen sie mir, was Ihnen zuerst in den Mund kömmt, – und ich gehe."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}vor sich.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Mit dieser Bedingung, kann ich ihr ja wohl einen Teil der Wahrheit sagen."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nun? Geschwind, Marinelli; und ich gehe. – Er sagte ohnedem, der Prinz: »Ein andermal, meine liebe Gräfin!« Sagte er nicht so? – Damit er mir Wort hält, damit er keinen Vorwand hat, mir nicht Wort zu halten: geschwind, Marinelli, Ihre Lüge; und ich gehe."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Der Prinz, liebe Gräfin, ist wahrlich nicht allein. Es sind Personen bei ihm, von denen er sich keinen Augenblick abmüßigen kann; Personen, die eben einer großen Gefahr entgangen sind. Der Graf Appiani –"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wäre bei ihm? – Schade, daß ich über diese Lüge Sie ertappen muß. Geschwind eine andere. – Denn Graf Appiani, wenn Sie es noch nicht wissen, ist eben von Räubern erschossen worden. Der Wagen mit seinem Leichname begegnete mir kurz vor der Stadt."

        orsina "– Oder ist er nicht? Hätte es mir bloß geträumet?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Leider nicht bloß geträumet! – Aber die andern, die mit dem Grafen waren, haben sich glücklich hierher nach dem Schlosse gerettet: seine Braut nämlich, und die Mutter der Braut, mit welchen er nach Sabionetta zu seiner feierlichen Verbindung fahren wollte."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Also die? Die sind bei dem Prinzen? die Braut? und die Mutter der Braut? – Ist die Braut schön?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Dem Prinzen geht ihr Unfall ungemein nahe."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Ich will hoffen; auch wenn sie häßlich wäre. Denn ihr Schicksal ist schrecklich. – Armes, gutes Mädchen, eben da er dein auf immer werden sollte, wird er dir auf immer entrissen! – Wer ist sie denn, diese Braut? Kenn' ich sie gar?"

        orsina "– Ich bin so lange aus der Stadt, daß ich von nichts weiß."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Es ist Emilia Galotti."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wer? – Emilia Galotti? Emilia Galotti? – Marinelli! daß ich diese Lüge nicht für Wahrheit nehme!"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wie so?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Emilia Galotti?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Die Sie schwerlich kennen werden –"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Doch! doch! Wenn es auch nur von heute wäre. – Im Ernst, Marinelli? Emilia Galotti? – Emilia Galotti wäre die unglückliche Braut, die der Prinz tröstet?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}vor sich.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Sollte ich ihr schon zu viel gesagt haben?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Und Graf Appiani war der Bräutigam dieser Braut? der eben erschossene Appiani?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nicht anders."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Bravo! o bravo! bravo!"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}In die Hände schlagend.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wie das?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Küssen möcht' ich den Teufel, der ihn dazu verleitet hat!"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wen? verleitet? wozu?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Ja, küssen, küssen möcht' ich ihn – Und wenn Sie selbst dieser Teufel wären, Marinelli."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Gräfin!"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Kommen Sie her! Sehen Sie mich an! steif an! Aug' in Auge!"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wissen Sie nicht, was ich denke?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wie kann ich das?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Haben Sie keinen Anteil daran?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Woran?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Schwören Sie! – Nein, schwören Sie nicht. Sie möchten eine Sünde mehr begehen – Oder ja; schwören Sie nur. Eine Sünde mehr oder weniger für einen, der doch verdammt ist! – Haben Sie keinen Anteil daran?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie erschrecken mich, Gräfin."

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Gewiß? – Nun, Marinelli, argwohnet Ihr gutes Herz auch nichts?"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Was? worüber?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wohl, – so will ich Ihnen etwas vertrauen; – etwas, das Ihnen jedes Haar auf dem Kopfe zu Berge sträuben soll. – Aber hier, so nahe an der Türe, möchte uns jemand hören. Kommen Sie hieher. – Und!"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Indem sie den Finger auf den Mund legt.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Hören Sie! ganz in geheim! ganz in geheim!"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Und ihren Mund seinem Ohre nähert, als ob sie ihm zuflüstern wollte, was sie aber sehr laut ihm zuschreiet.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Der Prinz ist ein Mörder!"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Gräfin, – Gräfin – sind Sie ganz von Sinnen?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Von Sinnen? Ha! ha! ha!"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Aus vollem Halse lachend.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Ich bin selten, oder nie, mit meinem Verstande so wohl zufrieden gewesen, als eben itzt. – Zuverlässig, Marinelli; –"

        orsina "aber es bleibt unter uns –"

        orsina "Leise."

        orsina "der Prinz ist ein Mörder! des Grafen Appiani Mörder! – Den haben nicht Räuber, den haben Helfershelfer des Prinzen, den hat der Prinz umgebracht!"

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wie kann Ihnen so eine Abscheuligkeit in den Mund, in die Gedanken kommen?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wie? – Ganz natürlich."

        orsina "– Mit dieser Emilia Galotti, die hier bei ihm ist, – deren Bräutigam so über Hals über Kopf sich aus der Welt trollen müssen, – mit dieser Emilia Galotti hat der Prinz heute Morgen, in der Halle bei den Dominikanern, ein langes und breites gesprochen."

        orsina "Das weiß ich; das haben meine Kundschafter gesehen. Sie haben auch gehört, was er mit ihr gesprochen. – Nun, guter Herr? Bin ich von Sinnen? Ich reime, dächt' ich, doch noch so ziemlich zusammen, was zusammen gehört. – Oder trifft auch das nur so von ungefähr zu?"

        orsina "Ist Ihnen auch das Zufall? O, Marinelli, so verstehen Sie auf die Bosheit der Menschen sich eben so schlecht, als auf die Vorsicht."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Gräfin, Sie würden sich um den Hals reden –"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wenn ich das mehrern sagte? – Desto besser, desto besser! – Morgen will ich es auf dem Markte ausrufen. – Und wer mir widerspricht – wer mir widerspricht, der war des Mörders Spießgeselle. – Leben Sie wohl."

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Indem sie fortgehen will, begegnet sie an der Türe dem alten Galotti, der eiligst hereintritt.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        hide orsina

    label Act_3_Scene_6:
        "{b}Sechster Auftritt{/b}"

        show odoardo at left
        show marinelli at right

        show odoardo at left
        show marinelli at right

        "<{i}Odoardo Galotti. Die Gräfin. Marinelli.{/i}>"

        hide odoardo
        hide marinelli

        hide odoardo
        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO GALOTTI."

        odoardo "Verzeihen Sie, gnädige Frau –"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Ich habe hier nichts zu verzeihen. Denn ich habe hier nichts übel zu nehmen – An diesen Herrn wenden Sie sich."

        hide orsina

        show orsina at left
        show marinelli at right

        hide orsina

        show orsina at left
        show marinelli at right

        orsina "<{i}Ihn nach dem Marinelli weisend.{/i}>"

        hide marinelli

        show orsina at truecenter

        hide marinelli

        show orsina at truecenter

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}indem er ihn erblicket, vor sich.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Nun vollends! der Alte! –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Vergeben Sie, mein Herr, einem Vater, der in der"

        odoardo "äußersten Bestürzung ist, – daß er so unangemeldet hereintritt."

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Vater?"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Kehrt wieder um.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Der Emilia, ohne Zweifel. – Ha, willkommen!"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ein Bedienter kam mir entgegen gesprengt, mit der Nachricht, daß hierherum die Meinigen in Gefahr wären. Ich fliege herzu, und höre, daß der Graf Appiani verwundet worden; daß er nach der Stadt zurückgekehret;"

        odoardo "daß meine Frau und Tochter sich in das Schloß gerettet. – Wo sind sie, mein Herr? wo sind sie?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sein Sie ruhig, Herr Oberster. Ihrer Gemahlin und Ihrer Tochter ist nichts Übles widerfahren; den Schreck ausgenommen. Sie befinden sich beide wohl. Der Prinz ist bei ihnen. Ich gehe sogleich, Sie zu melden."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Warum melden? erst melden?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Aus Ursachen – von wegen – Von wegen des Prinzen. Sie wissen, Herr Oberster, wie Sie mit dem Prinzen stehen. Nicht auf dem freundschaftlichsten Fuße."

        marinelli "So gnädig er sich gegen Ihre Gemahlin und Tochter bezeiget: – es sind Damen – Wird darum auch Ihr unvermuteter Anblick ihm gelegen sein?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sie haben Recht, mein Herr; Sie haben Recht."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Aber, gnädige Gräfin, – kann ich vorher die Ehre haben, Sie nach Ihrem Wagen zu begleiten?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nicht doch, nicht doch."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}sie bei der Hand nicht unsanft ergreifend.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Erlauben Sie, daß ich meine Schuldigkeit beobachte. –"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nur gemach! – Ich erlasse Sie deren, mein Herr. – Daß doch immer Ihres gleichen Höflichkeit zur Schuldigkeit machen; um was eigentlich ihre Schuldigkeit wäre, als die Nebensache betreiben zu dürfen!"

        orsina "– Diesen würdigen Mann je eher je lieber zu melden, das ist Ihre Schuldigkeit."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Vergessen Sie, was Ihnen der Prinz selbst befohlen?"

        hide marinelli

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Er komme, und befehle es mir noch einmal. Ich erwarte ihn."

        hide orsina

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}leise zu dem Obersten, den er bei Seite ziehet.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Mein Herr, ich muß Sie hier mit einer Dame lassen, die – der – mit deren Verstande – Sie verstehen mich. Ich sage Ihnen"

        marinelli "dieses, damit Sie wissen, was Sie auf ihre Reden zu geben haben, – deren sie oft sehr seltsame führet. Am besten, Sie lassen sich mit ihr nicht ins Wort."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Recht wohl. – Eilen Sie nur, mein Herr."

        hide odoardo

    label Act_3_Scene_7:
        "{b}Siebenter Auftritt{/b}"

        show orsina at left
        show odoardo at right

        show orsina at left
        show odoardo at right

        "<{i}Die Gräfin Orsina. Odoardo Galotti.{/i}>"

        hide orsina
        hide odoardo

        hide orsina
        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}nach einigem Stillschweigen, unter welchem sie den Obersten mit Mitleid betrachtet; so wie er sie, mit einer flüchtigen Neugierde.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Was er Ihnen auch da gesagt hat, unglücklicher Mann! –"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}halb vor sich, halb gegen sie.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Unglücklicher?"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Eine Wahrheit war es gewiß nicht; – am wenigsten eine von denen, die auf Sie warten."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Auf mich warten? – Weiß ich nicht schon genug? – Madame! – Aber, reden Sie nur, reden Sie nur."

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Sie wissen nichts."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Nichts?"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Guter, lieber Vater! – Was gäbe ich darum, wann Sie auch mein Vater wären! – Verzeihen Sie! die Unglücklichen ketten sich so gern an einander. – Ich wollte treulich Schmerz und Wut mit Ihnen teilen."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Schmerz und Wut? Madame! – Aber ich vergesse – Reden Sie nur."

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wenn es gar Ihre einzige Tochter – Ihr einziges Kind wäre! – Zwar einzig, oder nicht. Das unglückliche Kind, ist immer das einzige."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Das unglückliche? – Madame! – Was will ich von ihr? – Doch, bei Gott, so spricht keine Wahnwitzige!"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wahnwitzige? Das war es also, was er Ihnen von mir vertraute? – Nun, nun; es mag leicht keine von seinen gröbsten Lügen sein. – Ich fühle so was! – Und glauben Sie, glauben Sie mir: wer über gewisse Dinge den Verstand nicht verlieret, der hat keinen zu verlieren. –"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Was soll ich denken?"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Daß Sie mich also ja nicht verachten! – Denn auch Sie haben Verstand, guter Alter; auch Sie. – Ich seh' es an dieser entschlossenen, ehrwürdigen Miene. Auch Sie haben Verstand; und es kostet mich ein Wort, – so haben Sie keinen."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Madame! – Madame! – Ich habe schon keinen mehr, noch ehe Sie mir dieses Wort sagen, wenn Sie mir es nicht bald sagen. – Sagen Sie es! sagen Sie es!"

        odoardo "– Oder es ist nicht wahr, – es ist nicht wahr, daß Sie von jener guten, unsres Mitleids, unsrer Hochachtung so würdigen Gattung der Wahnwitzigen sind – Sie sind eine gemeine Törin. Sie haben nicht, was Sie nie hatten."

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "So merken Sie auf! – Was wissen Sie, der Sie schon genug wissen wollen? Daß Appiani verwundet worden? Nur verwundet? – Appiani ist tot!"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Tot? tot? – Ha, Frau, das ist wider die Abrede. Sie wollten mich um den Verstand bringen: und Sie brechen mir das Herz."

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Das beiher! – Nur weiter. – Der Bräutigam ist tot: und die Braut – Ihre Tochter – schlimmer als tot."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Schlimmer? schlimmer als tot? – Aber doch zugleich, auch tot? – Denn ich kenne nur Ein Schlimmeres –"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nicht zugleich auch tot. Nein, guter Vater, nein! – Sie lebt, sie lebt. Sie wird nun erst recht anfangen zu leben. – Ein Leben voll Wonne! Das schönste, lustigste Schlaraffenleben, – so lang' es dauert."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Das Wort, Madame; das einzige Wort, das mich um den Verstand bringen soll! heraus damit! – Schütten Sie nicht Ihren Tropfen Gift in einen Eimer. – Das einzige Wort! geschwind."

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nun da; buchstabieren Sie es zusammen! – Des Morgens, sprach der Prinz Ihre Tochter in der Messe; des Nachmittags, hat er sie auf seinem Lust – Lustschlosse."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sprach sie in der Messe? Der Prinz meine Tochter?"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Mit einer Vertraulichkeit! mit einer Inbrunst! – Sie hatten nichts Kleines abzureden. Und recht gut, wenn es abgeredet worden; recht gut, wenn Ihre Tochter freiwillig sich hierher gerettet! Sehen Sie: so ist es doch keine gewaltsame Entführung;"

        orsina "sondern bloß ein kleiner – kleiner Meuchelmord."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Verleumdung! verdammte Verleumdung! Ich kenne meine Tochter. Ist es Meuchelmord: so ist es auch Entführung. –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Blickt wild um sich, und stampft, und schäumet.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Nun, Claudia? Nun, Mütterchen? – Haben wir nicht Freude erlebt! O des gnädigen Prinzen! O der ganz besondern Ehre!"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Wirkt es, Alter! wirkt es?"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Da steh' ich nun vor der Höhle des Räubers –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Indem er den Rock von beiden Seiten aus einander schlägt, und sich ohne Gewehr sieht.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Wunder, daß ich aus Eilfertigkeit nicht auch die Hände zurück gelassen! –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}An alle Schubsäcke fühlend, als etwas suchend.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Nichts! gar nichts! nirgends!"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Ha, ich verstehe! – Damit kann ich aushelfen! – Ich hab' einen mitgebracht."

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Einen Dolch hervorziehend.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Da nehmen Sie! Nehmen Sie geschwind, eh uns jemand sieht. – Auch hätte ich noch etwas, – Gift. Aber Gift ist nur für uns Weiber; nicht für Männer. – Nehmen Sie ihn!"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Ihm den Dolch aufdringend.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "Nehmen Sie!"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ich danke, ich danke. – Liebes Kind, wer wieder sagt, daß du eine Närrin bist, der hat es mit mir zu tun."

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Stecken Sie bei Seite! geschwind bei Seite! – Mir wird die Gelegenheit versagt, Gebrauch davon zu machen. Ihnen wird sie nicht fehlen, diese Gelegenheit: und Sie werden sie ergreifen, die erste, die beste, – wenn Sie ein Mann sind."

        orsina "– Ich, ich bin nur ein Weib: aber so kam ich her! fest entschlossen! – Wir, Alter, wir können uns alles vertrauen. Denn wir sind beide beleidiget; von dem nämlichen Verführer beleidiget."

        orsina "– Ah, wenn Sie wüßten, – wenn Sie wüßten, wie überschwenglich, wie unaussprechlich, wie unbegreiflich ich von ihm beleidiget worden, und noch werde: – Sie könnten, Sie würden Ihre eigene Beleidigung darüber vergessen. – Kennen Sie mich? Ich bin Orsina;"

        orsina "die betrogene, verlassene Orsina. – Zwar vielleicht nur um Ihre Tochter verlassen. – Doch was kann Ihre Tochter dafür? – Bald wird auch sie verlassen sein. – Und dann wieder eine! – Und wieder eine! – Ha!"

        hide orsina

        show orsina at truecenter

        hide orsina

        show orsina at truecenter

        orsina "<{i}Wie in der Entzückung.{/i}>"

        show orsina at truecenter

        show orsina at truecenter

        orsina "welch eine himmlische Phantasie! Wann wir einmal alle, – wir, das ganze Heer der Verlassenen, – wir alle in Bacchantinnen, in Furien verwandelt, wenn wir alle"

        orsina "ihn unter uns hätten, ihn unter uns zerrissen, zerfleischten, sein Eingeweide durchwühlten, – um das Herz zu finden, das der Verräter einer jeden versprach, und keiner gab! Ha! das sollte ein Tanz werden! das sollte!"

        hide orsina

    label Act_3_Scene_8:
        "{b}Achter Auftritt{/b}"

        show claudia at truecenter

        show claudia at truecenter

        "<{i}Claudia Galotti. Die Vorigen.{/i}>"

        hide claudia

        hide claudia

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA"

        hide claudia

        show claudia at truecenter

        hide claudia

        show claudia at truecenter

        claudia "<{i}die im Hereintreten sich umsiehet, und sobald sie ihren Gemahl erblickt, auf ihn zuflieget.{/i}>"

        show claudia at truecenter

        show claudia at truecenter

        claudia "Erraten! – Ah, unser Beschützer, unser Retter! Bist du da, Odoardo? Bist du da? – Aus ihren Wispern, aus ihren Mienen schloß ich es. – Was soll ich dir sagen, wenn du noch nichts weißt? – Was soll ich dir sagen, wenn du schon alles weißt? – Aber wir sind unschuldig."

        claudia "Ich bin unschuldig. Deine Tochter ist unschuldig. Unschuldig, in allem unschuldig!"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}der sich bei Erblickung seiner Gemahlin zu fassen gesucht.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Gut, gut. Sei nur ruhig, nur ruhig, – und antworte mir."

        hide odoardo

        show odoardo at left
        show orsina at right

        hide odoardo

        show odoardo at left
        show orsina at right

        odoardo "<{i}Gegen die Orsina.{/i}>"

        hide orsina

        show odoardo at truecenter

        hide orsina

        show odoardo at truecenter

        odoardo "Nicht Madame, als ob ich noch zweifelte – Ist der Graf tot?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Tot."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ist es wahr, daß der Prinz heute Morgen Emilien in der Messe gesprochen?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wahr. Aber wenn du wüßtest, welchen Schreck es ihr verursacht; in welcher Bestürzung sie nach Hause kam –"

        hide claudia

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nun, hab' ich gelogen?"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}mit einem bittern Lachen.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Ich wollt' auch nicht, Sie hätten! Um wie vieles nicht!"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Bin ich wahnwitzig?"

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}wild hin und her gehend.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "O, – noch bin ich es auch nicht."

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Du gebotest mir ruhig zu sein; und ich bin ruhig. – Bester Mann, darf auch ich – ich dich bitten –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Was willst du? Bin ich nicht ruhig? Kann man ruhiger sein, als ich bin? –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Sich zwingend.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Weiß es Emilia, daß Appiani tot ist?"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Wissen kann sie es nicht. Aber ich fürchte, daß sie es argwohnet; weil er nicht erscheinet. –"

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Und sie jammert und winselt –"

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Nicht mehr. – Das ist vorbei: nach Ihrer Art, die du kennest. Sie ist die Furchtsamste und Entschlossenste unsers Geschlechts. Ihrer ersten Eindrücke nie mächtig; aber nach der geringsten Überlegung, in alles sich findend, auf alles gefaßt."

        claudia "Sie hält den Prinzen in einer Entfernung; sie spricht mit ihm in einem Tone – Mache nur, Odoardo, daß wir wegkommen."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ich bin zu Pferde. – Was zu tun? – Doch, Madame, Sie fahren ja nach der Stadt zurück?"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Nicht anders."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Hätten Sie wohl die Gewogenheit, meine Frau mit sich zu nehmen?"

        hide odoardo

        show orsina at truecenter

        $ orsina_var = "{noalt}ORSINA."

        orsina "Warum nicht? Sehr gern."

        hide orsina

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Claudia, –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Ihr die Gräfin bekannt machend.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Die Gräfin Orsina; eine Dame von großem Verstande; meine Freundin, meine Wohltäterin. – Du mußt mit ihr herein; um uns sogleich den Wagen heraus zu schicken. Emilia darf nicht wieder nach Guastalla. Sie soll mit mir."

        hide odoardo

        show claudia at truecenter

        $ claudia_var = "{noalt}CLAUDIA."

        claudia "Aber – wenn nur – Ich trenne mich ungern von dem Kinde."

        hide claudia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Bleibt der Vater nicht in der Nähe? Man wird ihn endlich doch vorlassen. Keine Einwendung! – Kommen Sie, gnädige Frau."

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Leise zu ihr.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Sie werden von mir hören. – Komm, Claudia."

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Er führt sie ab.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        hide odoardo

label Act_5:
    play music "audio/music/21.mp3" fadeout 1.0 fadein 1.0

    scene 5 with fade

    "{b}Fünfter Aufzug{/b}"

    "<{i}Die Szene bleibt.{/i}>"

    menu:
        "{color=#000}Erster Auftritt{/color}":
            jump Act_4_Scene_1
        "{color=#000}Zweiter Auftritt{/color}":
            jump Act_4_Scene_2
        "{color=#000}Dritter Auftritt{/color}":
            jump Act_4_Scene_3
        "{color=#000}Vierter Auftritt{/color}":
            jump Act_4_Scene_4
        "{color=#000}Fünfter Auftritt{/color}":
            jump Act_4_Scene_5
        "{color=#000}Sechster Auftritt{/color}":
            jump Act_4_Scene_6
        "{color=#000}>{/color}":
            jump Further_Act_4_Scene_6_1

label Further_Act_4_Scene_6_1:
    menu:
        "{color=#000}Siebenter Auftritt{/color}":
            jump Act_4_Scene_7
        "{color=#000}Achter Auftritt{/color}":
            jump Act_4_Scene_8

    label Act_4_Scene_1:
        "{b}Erster Auftritt{/b}"

        show marinelli at left
        show der_prinz at right

        show marinelli at left
        show der_prinz at right

        "<{i}Marinelli. Der Prinz.{/i}>"

        hide marinelli
        hide der_prinz

        hide marinelli
        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Hier, gnädiger Herr, aus diesem Fenster können Sie ihn sehen. Er geht die Arkade auf und nieder. – Eben biegt er ein; er kömmt. – Nein, er kehrt wieder um. – Ganz einig ist er mit sich noch nicht. Aber um ein großes ruhiger ist er, – oder scheinet er."

        marinelli "Für uns gleich viel! – Natürlich! Was ihm auch beide Weiber in den Kopf gesetzt haben, wird er es wagen zu äußern? – Wie Battista gehört, soll ihm seine Frau den Wagen sogleich heraus senden. Denn er kam zu Pferde."

        marinelli "– Geben Sie Acht, wenn er nun vor Ihnen erscheinet, wird er ganz untertänigst Eurer Durchlaucht für den gnädigen Schutz danken, den seine Familie bei diesem so traurigen Zufalle hier gefunden; wird sich, mit samt seiner Tochter, zu fernerer Gnade empfehlen;"

        marinelli "wird sie ruhig nach der Stadt bringen, und es in tiefster Unterwerfung erwarten, welchen weitern Anteil Euer Durchlaucht an seinem unglücklichen, lieben Mädchen zu nehmen geruhen wollen."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wenn er nun aber so zahm nicht ist? Und schwerlich, schwerlich wird er es sein. Ich kenne ihn zu gut. – Wenn er höchstens seinen Argwohn erstickt, seine Wut verbeißt: aber Emilien, anstatt sie nach der Stadt zu fahren, mit sich nimmt? bei sich behält?"

        der_prinz "oder wohl gar in ein Kloster, außer meinem Gebiete, verschließt? Wie dann?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Die fürchtende Liebe sieht weit. Wahrlich! – Aber er wird ja nicht –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wenn er nun aber! Wie dann? Was wird es uns dann helfen, daß der unglückliche Graf sein Leben darüber verloren?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wozu dieser traurige Seitenblick? Vorwärts! denkt der Sieger: es falle neben ihm Feind oder Freund. – Und wenn auch! Wenn er es auch wollte, der alte Neidhart, was Sie von ihm fürchten, Prinz: –"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Überlegend.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Das geht! Ich hab' es! – Weiter als zum Wollen, soll er es gewiß nicht bringen. Gewiß nicht! – Aber daß wir ihn nicht aus dem Gesichte verlieren. –"

        hide marinelli

        show marinelli at truecenter

        hide marinelli

        show marinelli at truecenter

        marinelli "<{i}Tritt wieder ans Fenster.{/i}>"

        show marinelli at truecenter

        show marinelli at truecenter

        marinelli "Bald hätt' er uns überrascht! Er kömmt. – Lassen Sie uns ihm noch ausweichen: und hören Sie erst, Prinz, was wir auf den zu befürchtenden Fall tun müssen."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}drohend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Nur, Marinelli! –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Das Unschuldigste von der Welt!"

        hide marinelli

    label Act_4_Scene_2:
        "{b}Zweiter Auftritt{/b}"

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO GALOTTI."

        odoardo "Noch niemand hier? – Gut; ich soll noch kälter werden. Es ist mein Glück. – Nichts verächtlicher, als ein brausender Jünglingskopf mit grauen Haaren! Ich hab' es mir so oft gesagt. Und doch ließ ich mich fortreißen: und von wem? Von einer Eifersüchtigen;"

        odoardo "von einer für Eifersucht Wahnwitzigen. – Was hat die gekränkte Tugend mit der Rache des Lasters zu schaffen? Jene allein hab' ich zu retten. – Und deine Sache, – mein Sohn! mein Sohn! – Weinen konnt' ich nie;"

        odoardo "– und will es nun nicht erst lernen – Deine Sache wird ein ganz anderer zu seiner machen! Genug für mich, wenn dein Mörder die Frucht seines Verbrechens nicht genießt. – Dies martere ihn mehr, als das Verbrechen!"

        odoardo "Wenn nun bald ihn Sättigung und Ekel von Lüsten zu Lüsten treiben; so vergälle die Erinnerung, diese eine Lust nicht gebüßet zu haben, ihm den Genuß aller! In jedem Traume führe der blutige Bräutigam ihm die Braut vor das Bette;"

        odoardo "und wann er dennoch den wollüstigen Arm nach ihr ausstreckt: so höre er plötzlich das Hohngelächter der Hölle, und erwache!"

        hide odoardo

    label Act_4_Scene_3:
        "{b}Dritter Auftritt{/b}"

        show marinelli at left
        show odoardo at right

        show marinelli at left
        show odoardo at right

        "<{i}Marinelli. Odoardo Galotti.{/i}>"

        hide marinelli
        hide odoardo

        hide marinelli
        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wo blieben Sie, mein Herr? wo blieben Sie?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "War meine Tochter hier?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nicht sie; aber der Prinz."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Er verzeihe. – Ich habe die Gräfin begleitet."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nun?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Die gute Dame!"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und Ihre Gemahlin?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ist mit der Gräfin; – um uns den Wagen sogleich heraus zu senden. Der Prinz vergönne nur, daß ich mich so lange mit meiner Tochter noch hier verweile."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wozu diese Umstände? Würde sich der Prinz nicht ein Vergnügen daraus gemacht haben, sie beide, Mutter und Tochter, selbst nach der Stadt zu bringen?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Die Tochter wenigstens würde diese Ehre haben verbitten müssen."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wie so?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sie soll nicht mehr nach Guastalla."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nicht? und warum nicht?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Der Graf ist tot."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Um so viel mehr –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sie soll mit mir."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Mit Ihnen?"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Mit mir. Ich sage Ihnen ja, der Graf ist tot. – Wenn Sie es noch nicht wissen – Was hat sie nun weiter in Guastalla zu tun? – Sie soll mit mir."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Allerdings wird der künftige Aufenthalt der Tochter einzig von dem Willen des Vaters abhangen. Nur vors erste –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Was vors erste?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Werden Sie wohl erlauben müssen, Herr Oberster, daß sie nach Guastalla gebracht wird."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Meine Tochter? nach Guastalla gebracht wird? und warum?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Warum? Erwägen Sie doch nur –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}hitzig.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Erwägen! erwägen! Ich erwäge, daß hier nichts zu erwägen ist. – Sie soll, sie muß mit mir."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "O mein Herr, – was brauchen wir, uns hierüber zu ereifern? Es kann sein, daß ich mich irre; daß es nicht nötig ist, was ich für nötig halte. – Der Prinz wird es am besten zu beurteilen wissen. Der Prinz entscheide. – Ich geh' und hole ihn."

        hide marinelli

    label Act_4_Scene_4:
        "{b}Vierter Auftritt{/b}"

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO GALOTTI."

        odoardo "Wie? – Nimmermehr! – Mir vorschreiben, wo sie hin soll? – Mir sie vorenthalten? – Wer will das? Wer darf das? – Der hier alles darf, was er will? Gut, gut; so soll er sehen, wie viel auch ich darf, ob ich es schon nicht dürfte! Kurzsichtiger Wüterich!"

        odoardo "Mit dir will ich es wohl aufnehmen. Wer kein Gesetz achtet, ist eben so mächtig, als wer kein Gesetz hat. Das weißt du nicht? Komm an! komm an! – Aber, sieh da! Schon wieder; schon wieder rennet der Zorn mit dem Verstande davon. – Was will ich?"

        odoardo "Erst müßt' es doch geschehen sein, worüber ich tobe. Was plaudert nicht eine Hofschranze! Und hätte ich ihn doch nur plaudern lassen! Hätte ich seinen Vorwand, warum sie wieder nach Guastalla soll, doch nur angehört!"

        odoardo "– So könnte ich mich itzt auf eine Antwort gefaßt machen. – Zwar auf welchen kann mir eine fehlen? – Sollte sie mir aber fehlen; sollte sie – Man kömmt. Ruhig, alter Knabe, ruhig!"

        hide odoardo

    label Act_4_Scene_5:
        "{b}Fünfter Auftritt{/b}"

        show der_prinz at left
        show marinelli at truecenter
        show odoardo at right

        show der_prinz at left
        show marinelli at truecenter
        show odoardo at right

        "<{i}Der Prinz. Marinelli. Odoardo Galotti.{/i}>"

        hide der_prinz
        hide marinelli
        hide odoardo

        hide der_prinz
        hide marinelli
        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ah, mein lieber, rechtschaffner Galotti, – so etwas muß auch geschehen, wenn ich Sie bei mir sehen soll. Um ein geringeres tun Sie es nicht. Doch keine Vorwürfe!"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Gnädiger Herr, ich halte es in allen Fällen für unanständig,"

        odoardo "sich zu seinem Fürsten zu drängen. Wen er kennt, den wird er fodern lassen, wenn er seiner bedarf. Selbst itzt bitte ich um Verzeihung –"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wie manchem andern wollte ich diese stolze Bescheidenheit wünschen! – Doch zur Sache. Sie werden begierig sein, Ihre Tochter zu sehen. Sie ist in neuer Unruhe, wegen der plötzlichen Entfernung einer so zärtlichen Mutter. – Wozu auch diese Entfernung?"

        der_prinz "Ich wartete nur, daß die liebenswürdige Emilie sich völlig erholet hätte, um beide im Triumphe nach der Stadt zu bringen. Sie haben mir diesen Triumph um die Hälfte verkümmert; aber ganz werde ich mir ihn nicht nehmen lassen."

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Zu viel Gnade! – Erlauben Sie, Prinz, daß ich meinem unglücklichen Kinde alle die mannichfaltigen Kränkungen erspare, die Freund und Feind, Mitleid und Schadenfreude in Guastalla für sie bereit halten."

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Um die süßen Kränkungen des Freundes und des Mitleids, würde es Grausamkeit sein, sie zu bringen. Daß aber die Kränkungen des Feindes und der Schadenfreude sie nicht erreichen sollen; dafür, lieber Galotti, lassen Sie mich sorgen."

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Prinz, die väterliche Liebe teilet ihre Sorgen nicht gern. – Ich denke, ich weiß es, was meiner Tochter in ihren itzigen Umständen einzig ziemet. – Entfernung aus der Welt; – ein Kloster, – sobald als möglich."

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ein Kloster?"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Bis dahin weine sie unter den Augen ihres Vaters."

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So viel Schönheit soll in einem Kloster verblühen? – Darf eine einzige fehlgeschlagene Hoffnung uns gegen die Welt so unversöhnlich machen? – Doch allerdings: dem Vater hat niemand einzureden. Bringen Sie Ihre Tochter, Galotti, wohin Sie wollen."

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at left
        show marinelli at right

        hide odoardo

        show odoardo at left
        show marinelli at right

        odoardo "<{i}gegen Marinelli.{/i}>"

        hide marinelli

        show odoardo at truecenter

        hide marinelli

        show odoardo at truecenter

        odoardo "Nun, mein Herr?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Wenn Sie mich so gar auffodern! –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "O mit nichten, mit nichten."

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Was haben Sie beide?"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Nichts, gnädiger Herr, nichts. – Wir erwägen bloß, welcher von uns sich in Ihnen geirret hat."

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Wie so? – Reden Sie, Marinelli."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Es geht mir nahe, der Gnade meines Fürsten in den Weg zu treten. Doch wenn die Freundschaft gebietet, vor allem in ihm den Richter aufzufodern –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Welche Freundschaft? –"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sie wissen, gnädiger Herr, wie sehr ich den Grafen Appiani liebte; wie sehr unser beider Seelen in einander verwebt schienen –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Das wissen Sie, Prinz? So wissen Sie es wahrlich allein."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Von ihm selbst zu seinem Rächer bestellet –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sie?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Fragen Sie nur Ihre Gemahlin. Marinelli, der Name Marinelli war das letzte Wort des sterbenden Grafen: und in einem Tone! in einem Tone!"

        marinelli "– Daß er mir nie aus dem Gehöre komme dieser schreckliche Ton, wenn ich nicht alles anwende, daß seine Mörder entdeckt und bestraft werden!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Rechnen Sie auf meine kräftigste Mitwirkung."

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Und meine heißesten Wünsche! – Gut, gut! – Aber was weiter?"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Das frag' ich, Marinelli."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Man hat Verdacht, daß es nicht Räuber gewesen, welche den Grafen angefallen."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}höhnisch.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Nicht? wirklich nicht?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Daß ein Nebenbuhler ihn aus dem Wege räumen lassen."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}bitter.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Ei! ein Nebenbuhler?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nicht anders."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Nun dann, – Gott verdamm' ihn den meuchelmörderschen Buben!"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Ein Nebenbuhler, und ein begünstigter Nebenbuhler –"

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Was? ein begünstigter? – Was sagen Sie?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Nichts' als was das Gerüchte verbreitet."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ein begünstigter? von meiner Tochter begünstiget?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Das ist gewiß nicht. Das kann nicht sein. Dem widersprech' ich, trotz Ihnen. – Aber bei dem allen, gnädiger Herr, – Denn das gegründetste Vorurteil wieget auf der"

        marinelli "Waage der Gerechtigkeit so viel als nichts – bei dem allen wird man doch nicht umhin können, die schöne Unglückliche darüber zu vernehmen."

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ja wohl, allerdings."

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Und wo anders? wo kann das anders geschehen, als in Guastalla?"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Da haben Sie Recht, Marinelli; da haben Sie Recht. – Ja so: das verändert die Sache, lieber Galotti. Nicht wahr? Sie sehen selbst –"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "O ja, ich sehe – Ich sehe, was ich sehe. – Gott! Gott!"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Was ist Ihnen? was haben Sie mit sich?"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Daß ich es nicht vorausgesehen, was ich da sehe. Das ärgert mich: weiter nichts. – Nun ja; sie soll wieder nach Guastalla."

        odoardo "Ich will sie wieder zu ihrer Mutter bringen: und bis die strengste Untersuchung sie frei gesprochen, will ich selbst aus Guastalla nicht weichen. Denn wer weiß, –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Mit einem bittern Lachen.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "wer weiß, ob die Gerechtigkeit nicht auch nötig findet, mich zu vernehmen."

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Sehr möglich! In solchen Fällen tut die Gerechtigkeit lieber zu viel, als zu wenig. – Daher fürchte ich sogar –"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Was? was fürchten Sie?"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Man werde vor der Hand nicht verstatten können, daß Mutter und Tochter sich sprechen."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sich nicht sprechen?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Man werde genötiget sein, Mutter und Tochter zu trennen."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Mutter und Tochter zu trennen?"

        hide odoardo

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Mutter und Tochter und Vater. Die Form des Verhörs erfodert diese Vorsichtigkeit schlechterdings. Und es tut mir leid, gnädiger Herr, daß ich mich gezwungen sehe, ausdrücklich darauf anzutragen, wenigstens Emilien in eine besondere Verwahrung zu bringen."

        hide marinelli

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Besondere Verwahrung? – Prinz! Prinz! – Doch ja; freilich, freilich! Ganz recht: in eine besondere Verwahrung! Nicht, Prinz? nicht? – O wie fein die Gerechtigkeit ist! Vortrefflich!"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Fährt schnell nach dem Schubsacke, in welchem er den Dolch hat.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}schmeichelhaft auf ihn zutretend.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Fassen Sie sich, lieber Galotti –"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}bei Seite, indem er die Hand leer wieder heraus zieht.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Das sprach sein Engel!"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Sie sind irrig; Sie verstehen ihn nicht. Sie denken bei dem Worte Verwahrung, wohl gar an Gefängnis und Kerker."

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Lassen Sie mich daran denken: und ich bin ruhig!"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Kein Wort von Gefängnis, Marinelli! Hier ist die Strenge der Gesetze mit der Achtung gegen unbescholtene Tugend leicht zu vereinigen. Wenn Emilia in besondere Verwahrung gebracht werden muß: so weiß ich schon – die alleranständigste."

        der_prinz "Das Haus meines Kanzlers – Keinen Widerspruch, Marinelli! – Da will ich sie selbst hinbringen, da will ich sie der Aufsicht einer der würdigsten Damen übergeben. Die soll mir für sie bürgen, haften."

        der_prinz "– Sie gehen zu weit, Marinelli, wirklich zu weit, wenn Sie mehr verlangen. – Sie kennen doch, Galotti, meinen Kanzler Grimaldi, und seine Gemahlin?"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Was sollt' ich nicht? Sogar die liebenswürdigen Töchter dieses edeln Paares kenn' ich. Wer kennt sie nicht? –"

        hide odoardo

        show odoardo at left
        show marinelli at right

        hide odoardo

        show odoardo at left
        show marinelli at right

        odoardo "<{i}Zu Marinelli.{/i}>"

        hide marinelli

        show odoardo at truecenter

        hide marinelli

        show odoardo at truecenter

        odoardo "Nein, mein Herr, geben Sie das nicht zu. Wenn Emilia verwahret werden muß: so müsse sie in dem tiefsten Kerker verwahret werden. Dringen Sie darauf; ich bitte Sie. – Ich Tor, mit meiner Bitte! ich alter Geck!"

        odoardo "– Ja wohl hat sie Recht die gute Sibylle: Wer über gewisse Dinge seinen Verstand nicht verlieret, der hat keinen zu verlieren!"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Ich verstehe Sie nicht. – Lieber Galotti, was kann ich mehr tun? – Lassen Sie es dabei: ich bitte Sie. – Ja, ja, in das Haus meines Kanzlers! da soll sie hin; da bring' ich sie selbst hin;"

        der_prinz "und wenn ihr da nicht mit der äußersten Achtung begegnet wird, so hat mein Wort nichts gegolten. Aber sorgen Sie nicht. – Dabei bleibt es! dabei bleibt es! – Sie selbst, Galotti, mit sich, können es halten, wie Sie wollen. Sie können uns nach Guastalla folgen;"

        der_prinz "Sie können nach Sabionetta zurückkehren: wie Sie wollen. Es wäre lächerlich, Ihnen vorzuschreiben. – Und nun, auf Wiedersehen, lieber Galotti! – Kommen Sie, Marinelli: es wird spät."

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}der in tiefen Gedanken gestanden.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Wie? so soll ich sie gar nicht sprechen meine Tochter? Auch hier nicht? – Ich lasse mir ja alles gefallen; ich finde ja alles ganz vortrefflich. Das Haus eines Kanzlers ist natürlicher Weise eine Freistatt der Tugend."

        odoardo "O, gnädiger Herr, bringen Sie ja meine Tochter dahin; nirgends anders als dahin. – Aber sprechen wollt' ich sie doch gern vorher. Der Tod des Grafen ist ihr noch unbekannt. Sie wird nicht begreifen können, warum man sie von ihren Eltern trennet."

        odoardo "Ihr jenen auf gute Art beizubringen; sie dieser Trennung wegen zu beruhigen; – muß ich sie sprechen, gnädiger Herr, muß ich sie sprechen."

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "So kommen Sie denn –"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "O, die Tochter kann auch wohl zu dem Vater kommen. – Hier, unter vier Augen, bin ich gleich mit ihr fertig. Senden Sie mir sie nur, gnädiger Herr."

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Auch das! – O Galotti, wenn Sie mein Freund, mein Führer, mein Vater sein wollten!"

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        der_prinz "<{i}Der Prinz und Marinelli gehen ab.{/i}>"

        hide marinelli

        show der_prinz at truecenter

        hide marinelli

        show der_prinz at truecenter

        hide der_prinz

    label Act_4_Scene_6:
        "{b}Sechster Auftritt{/b}"

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO GALOTTI"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}ihm nachsehend; nach einer Pause.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Warum nicht? – Herzlich gern – Ha! ha! ha! –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Blickt wild umher.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Wer lacht da? – Bei Gott, ich glaub', ich war es selbst. – Schon recht! Lustig, lustig. Das Spiel geht zu Ende. So, oder so! – Aber –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Pause.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "wenn sie mit ihm sich verstünde? Wenn es das alltägliche Possenspiel wäre? Wenn sie es nicht wert wäre, was ich für sie tun will? –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Pause.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Für sie tun will? Was will ich denn für sie tun? – Hab' ich das Herz, es mir zu sagen? – Da denk' ich so was: So was, was sich nur denken läßt. – Gräßlich! Fort, fort! Ich will sie nicht erwarten. Nein! –"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Gegen den Himmel.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Wer sie unschuldig in diesen Abgrund gestürzt hat, der ziehe sie wieder heraus. Was braucht er meine Hand dazu? Fort!"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Er will gehen, und sieht Emilien kommen.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Zu spät! Ah! er will meine Hand; er will sie!"

        hide odoardo

    label Act_4_Scene_7:
        "{b}Siebenter Auftritt{/b}"

        show emilia at left
        show odoardo at right

        show emilia at left
        show odoardo at right

        "<{i}Emilia. Odoardo.{/i}>"

        hide emilia
        hide odoardo

        hide emilia
        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Wie? Sie hier, mein Vater? – Und nur Sie? – Und meine Mutter? nicht hier? – Und der Graf? nicht hier? – Und Sie so unruhig, mein Vater?"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Und du so ruhig, meine Tochter?"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Warum nicht, mein Vater? – Entweder ist nichts verloren: oder alles. Ruhig sein können, und ruhig sein müssen: kömmt es nicht auf eines?"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Aber, was meinest du, daß der Fall ist?"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Daß alles verloren ist; – und daß wir wohl ruhig sein müssen, mein Vater."

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Und du wärest ruhig, weil du ruhig sein mußt? – Wer bist du? Ein Mädchen? und meine Tochter? So sollte der Mann, und der Vater sich wohl vor dir schämen? – Aber laß doch hören: was nennest du, alles verloren? – daß der Graf tot ist?"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Und warum er tot ist! Warum! – Ha, so ist es wahr, mein Vater? So ist sie wahr die ganze schreckliche Geschichte, die ich in dem nassen und wilden Auge meiner Mutter las? – Wo ist meine Mutter? Wo ist sie hin, mein Vater?"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Voraus; – wann wir anders ihr nachkommen."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Je eher, je besser. Denn wenn der Graf tot ist; wenn er darum tot ist – darum! was verweilen wir noch hier? Lassen Sie uns fliehen, mein Vater!"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Fliehen? – Was hätt' es dann für Not? – Du bist, du bleibst in den Händen deines Räubers."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Ich bleibe in seinen Händen?"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Und allein; ohne deine Mutter; ohne mich."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Ich allein in seinen Händen? – Nimmermehr, mein Vater. – Oder Sie sind nicht mein Vater. – Ich allein in seinen Händen? – Gut, lassen Sie mich nur; lassen sie mich nur."

        emilia "– Ich will doch sehn, wer mich hält, – wer mich zwingt, – wer der Mensch ist, der einen Menschen zwingen kann."

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ich meine, du bist ruhig, mein Kind."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Das bin ich. Aber was nennen Sie ruhig sein? Die Hände"

        emilia "in den Schoß legen? Leiden, was man nicht sollte? Dulden, was man nicht dürfte?"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ha! wenn du so denkest! – Laß dich umarmen, meine Tochter! – Ich hab' es immer gesagt: das Weib wollte die Natur zu ihrem Meisterstücke machen. Aber sie vergriff sich im Tone; sie nahm ihn zu fein. Sonst ist alles besser an euch, als an uns."

        odoardo "– Ha, wenn das deine Ruhe ist: so habe ich meine in ihr wiedergefunden! Laß dich umarmen, meine Tochter! – Denke nur: unter dem Vorwande einer gerichtlichen Untersuchung, – o des höllischen Gaukelspieles!"

        odoardo "– reißt er dich aus unsern Armen, und bringt dich zur Grimaldi."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Reißt mich? bringt mich? – Will mich reißen; will mich bringen: will! will! – Als ob wir, wir keinen Willen hätten, mein Vater!"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Ich ward auch so wütend, daß ich schon nach diesem Dolche griff,"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Ihn herausziehend.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "um einem von beiden – beiden! – das Herz zu durchstoßen."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Um des Himmels willen nicht, mein Vater! – Dieses Leben ist alles, was die Lasterhaften haben. – Mir, mein Vater, mir geben Sie diesen Dolch."

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Kind, es ist keine Haarnadel."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "So werde die Haarnadel zum Dolche! – Gleichviel."

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Was? Dahin wär' es gekommen? Nicht doch; nicht doch! Besinne dich. – Auch du hast nur Ein Leben zu verlieren."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Und nur Eine Unschuld!"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Die über alle Gewalt erhaben ist. –"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Aber nicht über alle Verführung. – Gewalt! Gewalt! wer kann der Gewalt nicht trotzen? Was Gewalt heißt, ist nichts: Verführung ist die wahre Gewalt. – Ich habe Blut, mein Vater; so jugendliches, so warmes Blut, als eine. Auch meine Sinne, sind Sinne."

        emilia "Ich stehe für nichts. Ich bin für nichts gut. Ich kenne das Haus der Grimaldi. Es ist das Haus der Freude. Eine Stunde da, unter den Augen meiner Mutter;"

        emilia "– und es erhob sich so mancher Tumult in meiner Seele, den die strengsten Übungen der Religion kaum in Wochen besänftigen konnten! – Der Religion! Und welcher Religion?"

        emilia "– Nichts Schlimmers zu vermeiden, sprangen Tausende in die Fluten, und sind Heilige! – Geben Sie mir, mein Vater, geben Sie mir diesen Dolch."

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Und wenn du ihn kenntest diesen Dolch! –"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Wenn ich ihn auch nicht kenne! – Ein unbekannter Freund, ist auch ein Freund. – Geben Sie mir ihn, mein Vater; geben Sie mir ihn."

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Wenn ich dir ihn nun gebe – da!"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Gibt ihr ihn.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Und da!"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}Im Begriffe sich damit zu durchstoßen, reißt der Vater ihr ihn wieder aus der Hand.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sieh, wie rasch! – Nein, das ist nicht für deine Hand."

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Es ist wahr, mit einer Haarnadel soll ich –"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}Sie fährt mit der Hand nach dem Haare, eine zu suchen, und bekömmt die Rose zu fassen.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Du noch hier? – Herunter mit dir! Du gehörest nicht in das Haar einer, – wie mein Vater will, daß ich werden soll!"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "O, meine Tochter! –"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "O, mein Vater, wenn ich Sie erriete! – Doch nein; das wollen Sie auch nicht. Warum zauderten Sie sonst? –"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}In einem bittern Tone, während daß sie die Rose zerpflückt.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        emilia "Ehedem wohl gab es einen Vater, der seine Tochter von der Schande zu retten, ihr den ersten den besten Stahl in das Herz senkte – ihr zum zweiten das Leben gab. Aber alle solche Taten sind von ehedem! Solcher Väter gibt es keinen mehr!"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Doch, meine Tochter, doch!"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Indem er sie durchsticht.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Gott, was hab' ich getan!"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Sie will sinken, und er faßt sie in seine Arme.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Eine Rose gebrochen, ehe der Sturm sie entblättert. – Lassen Sie mich sie küssen, diese väterliche Hand."

        hide emilia

    label Act_4_Scene_8:
        "{b}Achter Auftritt{/b}"

        show der_prinz at left
        show marinelli at right

        show der_prinz at left
        show marinelli at right

        "<{i}Der Prinz. Marinelli. Die Vorigen.{/i}>"

        hide der_prinz
        hide marinelli

        hide der_prinz
        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}im Hereintreten.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Was ist das? – Ist Emilien nicht wohl?"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Sehr wohl; sehr wohl!"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}indem er näher kömmt.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Was seh' ich? – Entsetzen!"

        hide der_prinz

        show marinelli at truecenter

        $ marinelli_var = "{noalt}MARINELLI."

        marinelli "Weh mir!"

        hide marinelli

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ."

        der_prinz "Grausamer Vater, was haben Sie getan?"

        hide der_prinz

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Eine Rose gebrochen, ehe der Sturm sie entblättert. – War es nicht so, meine Tochter?"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Nicht Sie, mein Vater – Ich selbst – ich selbst –"

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Nicht du, meine Tochter; – nicht du! – Gehe mit keiner Unwahrheit aus der Welt. Nicht du, meine Tochter! Dein Vater, dein unglücklicher Vater!"

        hide odoardo

        show emilia at truecenter

        $ emilia_var = "{noalt}EMILIA."

        emilia "Ah – mein Vater –"

        hide emilia

        show emilia at truecenter

        hide emilia

        show emilia at truecenter

        emilia "<{i}Sie stirbt, und er legt sie sanft auf den Boden.{/i}>"

        show emilia at truecenter

        show emilia at truecenter

        hide emilia

        show odoardo at truecenter

        $ odoardo_var = "{noalt}ODOARDO."

        odoardo "Zieh hin! – Nun da, Prinz! Gefällt sie Ihnen noch? Reizt sie noch Ihre Lüste? Noch, in diesem Blute, das wider Sie um Rache schreiet?"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Nach einer Pause.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Aber Sie erwarten, wo das alles hinaus soll? Sie erwarten vielleicht, daß ich den Stahl wider mich selbst kehren werde, um meine Tat wie eine schale Tragödie zu beschließen? – Sie irren sich. Hier!"

        hide odoardo

        show odoardo at truecenter

        hide odoardo

        show odoardo at truecenter

        odoardo "<{i}Indem er ihm den Dolch vor die Füße wirft.{/i}>"

        show odoardo at truecenter

        show odoardo at truecenter

        odoardo "Hier liegt er, der blutige Zeuge meines Verbrechens! Ich gehe und liefere mich selbst in das Gefängnis. Ich gehe, und erwarte Sie, als Richter. – Und dann dort – erwarte ich Sie vor dem Richter unser aller!"

        hide odoardo

        show der_prinz at truecenter

        $ der_prinz_var = "{noalt}DER PRINZ"

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        hide der_prinz

        show der_prinz at left
        show marinelli at right

        der_prinz "<{i}nach einigem Stillschweigen, unter welchem er den Körper mit Entsetzen und Verzweiflung betrachtet, zu Marinelli.{/i}>"

        hide marinelli

        show der_prinz at truecenter

        hide marinelli

        show der_prinz at truecenter

        der_prinz "Hier! heb' ihn auf. – Nun? Du bedenkst dich? – Elender! –"

        hide der_prinz

        show der_prinz at truecenter

        hide der_prinz

        show der_prinz at truecenter

        der_prinz "<{i}Indem er ihn den Dolch aus der Hand reißt.{/i}>"

        show der_prinz at truecenter

        show der_prinz at truecenter

        der_prinz "Nein, dein Blut soll mit diesem Blute sich nicht mischen. – Geh, dich auf ewig zu verbergen! – Geh! sag' ich. – Gott! Gott! – Ist es, zum Unglücke so mancher, nicht genug, daß Fürsten Menschen sind: müssen sich auch noch Teufel in ihren Freund verstellen?"

        hide der_prinz

        "<{i}Ende des Trauerspiels.{/i}>"


