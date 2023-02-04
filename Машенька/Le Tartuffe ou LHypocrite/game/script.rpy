define madame_pernelle = Character("madame_pernelle_var", color="#FFB300", dynamic=True)
define elmire = Character("elmire_var", color="#803E75", dynamic=True)
define dorine = Character("dorine_var", color="#FF6800", dynamic=True)
define damis = Character("damis_var", color="#A6BDD7", dynamic=True)
define cleante = Character("cleante_var", color="#C10020", dynamic=True)
define orgon = Character("orgon_var", color="#CEA262", dynamic=True)
define tartuffe = Character("tartuffe_var", color="#817066", dynamic=True)
define flipote = Character("flipote_var", color="#007D34", dynamic=True)
define laurent = Character("laurent_var", color="#F6768E", dynamic=True)

label start:
    play music "audio/music/9.mp3" fadeout 1.0 fadein 1.0

    scene poster with fade

    "LE TARTUFFE ou L'HYPOCRITE"

    "COMÉDIE"

    "\[version de 1664 reconstruite par Georges Forestier avec la complicité d'Isabelle Grellet]"

    menu:
        "ACTEURS":
            jump Characters
        "ACTE PREMIER":
            jump Act_1
        "ACTE II":
            jump Act_2
        "ACTE III":
            jump Act_3

label Characters:
    play music "audio/music/6.mp3" fadeout 1.0 fadein 1.0

    scene 3 with fade

    "{b}ACTEURS{/b}"

    show madame_pernelle at truecenter
    "MADAME PERNELLE, Mère d'Orgon."
    hide madame_pernelle

    show elmire at truecenter
    "ELMIRE, Femme d'Orgon."
    hide elmire

    show orgon at truecenter
    "ORGON, Mari d'Elmire."
    hide orgon

    show damis at truecenter
    "DAMIS, Fils d'Orgon."
    hide damis

    show cleante at truecenter
    "CLÉANTE, Beau-frère d'Orgon."
    hide cleante

    show tartuffe at truecenter
    "TARTUFFE, Faux Dévot."
    hide tartuffe

    show dorine at truecenter
    "DORINE, suivante."
    hide dorine

    show flipote at truecenter
    "FLIPOTE, servante de Mme Pernelle."
    hide flipote


label Act_1:
    play music "audio/music/1.mp3" fadeout 1.0 fadein 1.0

    scene 2 with fade

    "{b}ACTE PREMIER{/b}"

    menu:
        "SCÈNE PREMIÈRE.":
            jump Act_1_Scene_1
        "SCÈNE II.":
            jump Act_1_Scene_2
        "SCÈNE III.":
            jump Act_1_Scene_3
        "SCÈNE IV.":
            jump Act_1_Scene_4
        "SCÈNE V.":
            jump Act_1_Scene_5

label Act_1_Scene_1:
    "{b}SCÈNE PREMIÈRE.{/b}"

    show dorine at left
    show damis at truecenter
    show cleante at right

    "<{i}Madame Pernelle, et Flipotte sa Servante, Elmire, Dorine, Damis, Cléante.{/i}>"

    hide madame_pernelle
    hide flipote
    hide elmire
    hide dorine
    hide damis
    hide cleante

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Allons, Flipotte, allons ; que d'eux je me délivre."

    hide madame_pernelle

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Vous marchez d'un tel pas, qu'on a peine à vous suivre."

    hide elmire

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Laissez, ma Bru, laissez ; ne venez pas plus loin ;"

    madame_pernelle "Ce sont toutes façons, dont je n'ai pas besoin."

    hide madame_pernelle

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "De ce que l'on vous doit, envers vous on s'acquitte."

    elmire "Mais, ma Mère, d'où vient que vous sortez si vite ?"

    hide elmire

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "C'est que je ne puis voir tout ce ménage-ci,"

    madame_pernelle "Et que de me complaire, on ne prend nul souci."

    madame_pernelle "Oui, je sors de chez vous fort mal édifiée ;"

    madame_pernelle "Dans toutes mes leçons, j'y suis contrariée ;"

    madame_pernelle "On n'y respecte rien ; chacun y parle haut,"

    madame_pernelle "Et c'est, tout justement, la {a=myshow|tooltip|text=Cour du roi Pétaud : Usité dans cette locution ; la cour du roi Pétaud, un lieu de désordre et de confusion et où tout le monde est le maître. \[\[L]}cour_du_Roi_Pétaud{/a}."

    hide madame_pernelle

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Si..."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Vous êtes, Mamie, une Fille suivante"

    madame_pernelle "Un peu trop forte en gueule, et fort impertinente :"

    madame_pernelle "Vous vous mêlez sur tout de dire votre avis."

    hide madame_pernelle

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Mais..."

    hide damis

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Vous êtes un sot en trois lettres, mon Fils ;"

    madame_pernelle "C'est moi qui vous le dis, qui suis votre Grand-Mère ;"

    madame_pernelle "Et j'ai prédit cent fois à mon Fils, votre Père,"

    madame_pernelle "Que vous preniez tout l'air d'un méchant Garnement,"

    madame_pernelle "Et ne lui donneriez jamais que du tourment."

    hide madame_pernelle

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Mais, ma Mère..."

    hide elmire

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Ma Bru, qu'il ne vous en déplaise,"

    madame_pernelle "Votre conduite en tout, est tout à fait mauvaise :"

    madame_pernelle "Vous devriez leur mettre un bon exemple aux yeux,"

    madame_pernelle "Et leur défunte Mère en usait beaucoup mieux."

    madame_pernelle "Vous êtes dépensière, et cet état me blesse,"

    madame_pernelle "Que vous alliez vêtue ainsi qu'une Princesse."

    madame_pernelle "Quiconque à son mari veut plaire seulement,"

    madame_pernelle "Ma Bru, n'a pas besoin de tant d'ajustement."

    hide madame_pernelle

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Mais, Madame, après tout..."

    hide cleante

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Pour vous, Monsieur son Frère,"

    madame_pernelle "Je vous estime fort, vous aime, et vous révère :"

    madame_pernelle "Mais enfin, si j'étais de mon Fils son Époux,"

    madame_pernelle "Je vous prierais bien fort, de n'entrer point chez nous."

    madame_pernelle "Sans cesse vous prêchez des Maximes de vivre,"

    madame_pernelle "Qui par d'honnêtes Gens ne se doivent point suivre :"

    madame_pernelle "Je vous parle un peu franc, mais c'est là mon humeur,"

    madame_pernelle "Et je ne mâche point ce que j'ai sur le coeur."

    hide madame_pernelle

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Votre Monsieur Tartuffe est Bienheureux sans doute..."

    hide damis

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "C'est un Homme de bien, qu'il faut que l'on écoute ;"

    madame_pernelle "Et je ne puis souffrir, sans me mettre en courroux,"

    madame_pernelle "De le voir querellé par un Fou comme vous."

    hide madame_pernelle

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Quoi ! je souffrirai, moi, qu'un {a=myshow|tooltip|text=Cagot : Faux dévot ; hypocrite, qui affecte de montrer des apparences de dévotion pour tromper, et pour parvenir à ses fins. \[\[F]}Cagot{/a} de Critique,"

    damis "Vienne usurper céans un pouvoir tyrannique ?"

    damis "Et que nous ne puissions à rien nous divertir,"

    damis "Si ce beau Monsieur-là n'y daigne consentir ?"

    hide damis

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "S'il le faut écouter, et croire à ses Maximes,"

    dorine "On ne peut faire rien, qu'on ne fasse des crimes,"

    dorine "Car il contrôle tout, ce Critique zélé."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Et tout ce qu'il contrôle, est fort bien contrôlé."

    madame_pernelle "C'est au chemin du Ciel qu'il prétend vous conduire ;"

    madame_pernelle "Et mon Fils, à l'aimer, vous devrait tous induire."

    hide madame_pernelle

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Non, voyez-vous, ma Mère, il n'est Père, ni rien,"

    damis "Qui me puisse obliger à lui vouloir du bien."

    damis "Je trahirais mon coeur, de parler d'autre sorte ;"

    damis "Sur ses façons de faire, à tous coups je m'emporte ;"

    damis "J'en prévois une suite, et qu'avec ce {a=myshow|tooltip|text=Pied plat : Fig. et par mépris, pied plat, et quelquefois plat pied, homme qui ne mérite aucune considération.\[\[L]}Pied plat{/a}"

    damis "Il faudra que j'en vienne à quelque grand éclat."

    hide damis

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Certes, c'est une chose aussi qui scandalise,"

    dorine "De voir qu'un Inconnu céans {a=myshow|tooltip|text=Impatroniser (s') : S'emparer ; se rendre insensiblement maître de quelques chose. \[\[F]}s'impatronise{/a} ;"

    dorine "Qu'un {a=myshow|tooltip|text=Gueux : Indigent, nécessiteux, qui est réduit à mendier, à demander l'aumône. \[\[F]}Gueux{/a} qui, quand il vint, n'avait pas de souliers,"

    dorine "Et dont l'habit entier valait bien six deniers,"

    dorine "En vienne jusque-là, que de se méconnaître,"

    dorine "De contrarier tout, et de faire le Maître."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Hé, merci de ma vie il en irait bien mieux,"

    madame_pernelle "Si tout se gouvernait par ses ordres pieux."

    hide madame_pernelle

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Il passe pour un Saint dans votre fantaisie ;"

    dorine "Tout son fait, croyez-moi, n'est rien qu'hypocrisie."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Voyez la langue !"

    hide madame_pernelle

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}À lui, non plus qu'à son Laurent,"

    dorine "Je ne me fierais, moi, que sur un bon Garant."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "J'ignore ce qu'au fond le Serviteur peut être ;"

    madame_pernelle "Mais pour Homme de bien, je garantis le Maître."

    madame_pernelle "Vous ne lui voulez mal, et ne le rebutez,"

    madame_pernelle "Qu'à cause qu'il vous dit à tous vos vérités."

    madame_pernelle "C'est contre le Péché que son coeur se courrouce,"

    madame_pernelle "Et l'intérêt du Ciel est tout ce qui le pousse."

    hide madame_pernelle

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Oui ; mais pourquoi surtout, depuis un certain temps,"

    dorine "Ne saurait-il souffrir qu'aucun hante céans ?"

    dorine "En quoi blesse le Ciel une visite honnête,"

    dorine "Pour en faire un vacarme à nous rompre la tête ?"

    dorine "Veut-on que là-dessus je m'explique entre nous ?"

    dorine "Je crois que de Madame il est, ma foi, jaloux."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Taisez-vous, et songez aux choses que vous dites."

    madame_pernelle "Ce n'est pas lui tout seul qui blâme ces visites ;"

    madame_pernelle "Tout ce tracas qui suit les Gens que vous hantez,"

    madame_pernelle "Ces Carrosses sans cesse à la Porte plantés,"

    madame_pernelle "Et de tant de Laquais le bruyant assemblage,"

    madame_pernelle "Font un éclat fâcheux dans tout le voisinage."

    madame_pernelle "Je veux croire qu'au fond il ne se passe rien ;"

    madame_pernelle "Mais enfin on en parle, et cela n'est pas bien."

    hide madame_pernelle

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Hé, voulez-vous, Madame, empêcher qu'on ne cause ?"

    cleante "Ce serait dans la vie une fâcheuse chose,"

    cleante "Si pour les sots discours où l'on peut être mis,"

    cleante "Il fallait renoncer à ses meilleurs Amis :"

    cleante "Et quand même on pourrait se résoudre à le faire,"

    cleante "Croiriez-vous obliger tout le monde à se taire ?"

    cleante "Contre la Médisance il n'est point de rempart ;"

    cleante "À tous les sots caquets n'ayons donc nul égard ;"

    cleante "Efforçons-nous de vivre avec toute innocence,"

    cleante "Et laissons aux Causeurs une pleine licence."

    hide cleante

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Daphné notre voisine, et son petit époux,"

    dorine "Ne seraient-ils point ceux qui parlent mal de nous ?"

    dorine "Ceux de qui la conduite offre le plus à rire,"

    dorine "Sont toujours sur autrui les premiers à médire ;"

    dorine "Ils ne manquent jamais de saisir promptement"

    dorine "L'apparente lueur du moindre attachement,"

    dorine "D'en semer la nouvelle avec beaucoup de joie,"

    dorine "Et d'y donner le tour qu'ils veulent qu'on y croie."

    dorine "Des actions d'autrui, teintes de leurs couleurs,"

    dorine "Ils pensent dans le Monde autoriser les leurs,"

    dorine "Et sous le faux espoir de quelque ressemblance,"

    dorine "Aux intrigues qu'ils ont, donner de l'innocence,"

    dorine "Ou faire ailleurs tomber quelques traits partagés"

    dorine "De ce blâme public dont ils sont trop chargés."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Tous ces raisonnements ne font rien à l'affaire :"

    madame_pernelle "On sait qu'Orante mène une vie exemplaire ;"

    madame_pernelle "Tous ses soins vont au Ciel, et j'ai su par des Gens,"

    madame_pernelle "Qu'elle condamne fort le train qui vient céans."

    hide madame_pernelle

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "L'exemple est admirable, et cette Dame est bonne :"

    dorine "Il est vrai qu'elle vit en austère Personne ;"

    dorine "Mais l'âge, dans son âme, a mis ce zèle ardent,"

    dorine "Et l'on sait qu'elle est Prude, à son corps défendant,"

    dorine "Tant qu'elle a pu des Coeurs attirer les hommages,"

    dorine "Elle a fort bien joui de tous ses avantages :"

    dorine "Mais voyant de ses yeux tous les brillants baisser,"

    dorine "Au Monde, qui la quitte, elle veut renoncer ;"

    dorine "Et du voile pompeux d'une haute sagesse,"

    dorine "De ses attraits usés, déguiser la faiblesse."

    dorine "Ce sont là les retours des Coquettes du temps."

    dorine "Il leur est dur de voir déserter les Galants."

    dorine "Dans un tel abandon, leur sombre inquiétude"

    dorine "Ne voit d'autre recours que le métier de Prude ;"

    dorine "Et la sévérité de ces Femmes de bien,"

    dorine "Censure toute chose, et ne pardonne à rien ;"

    dorine "Hautement, d'un chacun, elles blâment la vie,"

    dorine "Non point par charité, mais par un trait d'envie"

    dorine "Qui ne saurait souffrir qu'une autre ait les plaisirs,"

    dorine "Dont le penchant de l'âge a sevré leurs désirs."

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Voilà les {a=myshow|tooltip|text=Contes bleus : contes de fées et autres récits de ce genre, ainsi dits parce qu'ils étaient d'ordinaire couverts d'un papier bleu ; et par extension, récits imaginaires, raisons sans fondement, billevesées. \[\[L]}contes bleus{/a} qu'il vous faut, pour vous plaire."

    madame_pernelle "Ma Bru, l'on est, chez vous, contrainte de se taire ;"

    madame_pernelle "Car Madame, à jaser, {a=myshow|tooltip|text=Tenir le dé : avoir les dés en main pour jouer ; et, figurément, tenir le dé dans la conversation, s'en rendre maître, la diriger. \[\[L]}tient le dé{/a} tout le jour :"

    madame_pernelle "Mais enfin, je prétends discourir à mon tour."

    madame_pernelle "Je vous dis que mon Fils n'a rien fait de plus sage,"

    madame_pernelle "Qu'en recueillant chez soi ce dévot Personnage ;"

    madame_pernelle "Que le Ciel au besoin l'a céans envoyé,"

    madame_pernelle "Pour redresser à tous votre esprit fourvoyé ;"

    madame_pernelle "Que pour votre salut vous le devez entendre,"

    madame_pernelle "Et qu'il ne reprend rien, qui ne soit à reprendre."

    madame_pernelle "Ces Visites, ces Bals, ces Conversations,"

    madame_pernelle "Sont, du malin Esprit, toutes inventions."

    madame_pernelle "Là, jamais on n'entend de pieuses paroles,"

    madame_pernelle "Ce sont propos oisifs, chansons, et {a=myshow|tooltip|text=Fariboles : Chose vaine et frivole. \[\[L]}fariboles{/a} ;"

    madame_pernelle "Bien souvent le Prochain en a sa bonne part,"

    madame_pernelle "Et l'on y sait médire, et du tiers, et du quart."

    madame_pernelle "Enfin les Gens sensés ont leurs têtes troublées,"

    madame_pernelle "De la confusion de telles assemblées :"

    madame_pernelle "Mille caquets divers s'y font en moins de rien ;"

    madame_pernelle "Et comme l'autre jour un Docteur dit fort bien,"

    madame_pernelle "C'est véritablement la Tour de Babylone,"

    madame_pernelle "Car chacun y {a=myshow|tooltip|text=Babiller : Parler beaucoup, facilement, et surtout pour le seul plaisir de parler. \[\[L]}babille{/a}, et tout du long de l'aune ;"

    madame_pernelle "Et pour conter l'Histoire où ce point l'engagea..."

    madame_pernelle "Voilà-t-il pas Monsieur qui ricane déjà ?"

    madame_pernelle "Allez chercher vos Fous qui vous donnent à rire ;"

    madame_pernelle "{a=myshow|tooltip|text=Je ne vous dis pas adieu, ou sans adieu, se dit familièrement à une personne qu'on se propose de revoir bientôt. \[\[L]}Et sans... Adieu, ma Bru, je ne veux plus rien dire{/a}."

    madame_pernelle "Sachez que pour céans j'en rabats de moitié,"

    madame_pernelle "Et qu'il fera beau temps, quand j'y mettrai le pied."

    play sound1 slap

    hide madame_pernelle

    show madame_pernelle at left
    show flipote at right

    madame_pernelle "<{i}Donnant un soufflet à Flipote.{/i}>"

    hide flipote

    show madame_pernelle at truecenter

    stop sound1

    madame_pernelle "Allons, vous ; vous rêvez, et bayez aux Corneilles ;"

    madame_pernelle "Jour de Dieu, je saurai vous frotter les oreilles ;"

    madame_pernelle "Marchons, {a=myshow|tooltip|text=Gaupe : Maussade et salope ; grosse femme mal bâtie, et mal propre. \[\[F]}gaupe{/a}, marchons."

    hide madame_pernelle

label Act_1_Scene_2:
    "{b}SCÈNE II.{/b}"

    show cleante at left
    show dorine at right

    "<{i}Cléante, Dorine.{/i}>"

    hide cleante
    hide dorine

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Je n'y veux point aller,"

    cleante "De peur qu'elle ne vînt encor me quereller ;"

    cleante "Que cette bonne Femme..."

    hide cleante

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Ah ! Certes, c'est dommage,"

    dorine "Qu'elle ne vous ouït tenir un tel langage ;"

    dorine "Elle vous dirait bien qu'elle vous trouve bon,"

    dorine "Et qu'elle n'est point d'âge à lui donner ce nom."

    hide dorine

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Comme elle s'est pour rien contre nous échauffée !"

    cleante "Et que de son Tartuffe elle paraît coiffée !"

    hide cleante

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Oh vraiment, tout cela n'est rien au prix du Fils ;"

    dorine "Et si vous l'aviez vu, vous diriez, c'est bien pis."

    dorine "Nos troubles l'avaient mis sur le pied d'homme sage,"

    dorine "Et pour servir son Prince, il montra du courage :"

    dorine "Mais il est devenu comme un Homme hébété,"

    dorine "Depuis que de Tartuffe on le voit entêté."

    dorine "Il l'appelle son Frère, et l'aime dans son âme"

    dorine "Cent fois plus qu'il ne fait Mère, Fils, Frère et Femme."

    dorine "C'est de tous ses secrets l'unique Confident,"

    dorine "Et de ses actions le Directeur prudent."

    dorine "Il le choie, il l'embrasse ; et pour une Maîtresse,"

    dorine "On ne saurait, je pense, avoir plus de tendresse."

    dorine "À table, au plus haut bout, il veut qu'il soit assis,"

    dorine "Avec joie il l'y voit manger autant que six ;"

    dorine "Les bons morceaux de tout, il faut qu'on les lui cède ;"

    dorine "Et s'il vient à roter, il lui dit, Dieu vous aide."

    dorine "Enfin il en est fou ; c'est son tout, son Héros ;"

    dorine "Il l'admire à tous coups, le cite à tout propos ;"

    dorine "Ses moindres actions lui semblent des miracles,"

    dorine "Et tous les mots qu'il dit, sont pour lui des Oracles."

    dorine "Lui qui connaît sa dupe, et qui veut en jouir,"

    dorine "Par cent dehors fardés, a l'art de l'éblouir ;"

    dorine "Son {a=myshow|tooltip|text=Cagot : Celui, celle qui a une dévotion suspecte et déplaisante. \[\[L] Par extention cagotisme, se tenir comme un cagot.}Cagotisme{/a} en tire à toute heure des sommes,"

    dorine "Et prend droit de gloser sur tous tant que nous sommes."

    dorine "Il n'est pas jusqu'au Fat, qui lui sert de Garçon,"

    dorine "Qui ne se mêle aussi de nous faire leçon."

    dorine "Il vient nous sermonner avec des yeux farouches,"

    dorine "Et jeter nos Rubans, notre Rouge, et nos Mouches."

    dorine "Le traître, l'autre jour, nous rompit de ses mains,"

    dorine "Un Mouchoir qu'il trouva dans une Fleur des Saints ;"

    dorine "Disant que nous mêlions, par un crime effroyable,"

    dorine "Avec la Sainteté, les parures du Diable."

    hide dorine

label Act_1_Scene_3:
    "{b}SCÈNE III.{/b}"

    show damis at left
    show cleante at truecenter
    show dorine at right

    "<{i}Elmire, Damis, Cléante, Dorine.{/i}>"

    hide elmire
    hide damis
    hide cleante
    hide dorine

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Vous êtes bien heureux, de n'être point venu"

    elmire "Au discours qu'à la Porte elle nous a tenu."

    elmire "Mais j'ai vu mon Mari ; comme il ne m'a point vue,"

    elmire "Je veux aller là-haut attendre sa venue."

    hide elmire

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Moi, je l'attends ici pour moins d'amusement,"

    cleante "Et je vais lui donner le bonjour seulement."

    hide cleante

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "De mon hymen prochain, touchez-lui quelque chose."

    damis "J'ai soupçon que Tartuffe à son effet s'oppose."

    damis "Qu'il oblige mon Père à des détours si grands"

    damis "Que je ne sais comment trancher ces différends"

    damis "Et s'il fallait..."

    hide damis

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=200}Il entre."

    hide dorine

label Act_1_Scene_4:
    "{b}SCÈNE IV.{/b}"

    show orgon at left
    show cleante at truecenter
    show dorine at right

    "<{i}Orgon, Cléante, Dorine.{/i}>"

    hide orgon
    hide cleante
    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Ah, mon Frère, bonjour."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Je sortais, et j'ai joie à vous voir de retour :"

    cleante "La Campagne, à présent, n'est pas beaucoup fleurie."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Dorine, mon Beau-frère, attendez, je vous prie."

    orgon "Vous voulez bien souffrir, pour m'ôter de souci,"

    orgon "Que je m'informe un peu des nouvelles d'ici."

    orgon "Tout s'est-il, ces deux jours, passé de bonne sorte ?"

    orgon "Qu'est-ce qu'on fait céans ? Comme est-ce qu'on s'y porte ?"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Madame eut, avant-hier, la fièvre jusqu'au soir,"

    dorine "Avec un mal de tête étrange à concevoir."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Et Tartuffe ?"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Tartuffe ? Il se porte à merveille,"

    dorine "Gros, et gras, le teint frais, et la bouche vermeille."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Le pauvre Homme !"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Le soir elle eut un grand dégoût,"

    dorine "Et ne put au Souper toucher à rien du tout,"

    dorine "Tant sa douleur de tête était encor cruelle."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Et Tartuffe ?"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Il soupa, lui tout seul, devant elle,"

    dorine "Et fort dévotement il mangea deux Perdrix,"

    dorine "Avec une moitié de Gigot en hachis."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Le pauvre Homme !"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}La nuit se passa toute entière,"

    dorine "Sans qu'elle pût fermer un moment la paupière ;"

    dorine "Des chaleurs l'empêchaient de pouvoir sommeiller,"

    dorine "Et jusqu'au jour, près d'elle, il nous fallut veiller."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Et Tartuffe ?"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Pressé d'un sommeil agréable,"

    dorine "Il passa dans sa Chambre, au sortir de la Table ;"

    dorine "Et dans son Lit bien chaud, il se mit tout soudain,"

    dorine "Où sans trouble il dormit jusques au lendemain."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Le pauvre Homme !"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}À la fin, par nos raisons gagnée,"

    dorine "Elle se résolut à souffrir la {a=myshow|tooltip|text=Saignée : Ouverture de la veine pour tirer du sang. \[\[L]}saignée{/a},"

    dorine "Et le soulagement suivit tout aussitôt."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Et Tartuffe ?"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Il reprit courage comme il faut ;"

    dorine "Et contre tous les maux fortifiant son âme,"

    dorine "Pour réparer le sang qu'avait perdu Madame,"

    dorine "But à son déjeuner, quatre grands coups de Vin."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Le pauvre Homme !"

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Tous deux se portent bien enfin ;"

    dorine "Et je vais à Madame annoncer par avance,"

    dorine "La part que vous prenez à sa convalescence."

    hide dorine

label Act_1_Scene_5:
    "{b}SCÈNE V.{/b}"

    show orgon at left
    show cleante at right

    "<{i}Orgon, Cléante.{/i}>"

    hide orgon
    hide cleante

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "À votre nez, mon Frère, elle se rit de vous ;"

    cleante "Et sans avoir dessein de vous mettre en courroux,"

    cleante "Je vous dirai tout franc, que c'est avec justice."

    cleante "A-t-on jamais parlé d'un semblable caprice ?"

    cleante "Et se peut-il qu'un Homme ait un charme aujourd'hui"

    cleante "À vous faire oublier toutes choses pour lui ?"

    cleante "Qu'après avoir chez vous réparé sa misère,"

    cleante "Vous en veniez au point..."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Halte-là, mon Beau-frère,"

    orgon "Vous ne connaissez pas celui dont vous parlez."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Je ne le connais pas, puisque vous le voulez :"

    cleante "Mais enfin, pour savoir quel Homme ce peut être..."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Mon Frère, vous seriez charmé de le connaître,"

    orgon "Et vos ravissements ne prendraient point de fin."

    orgon "C'est un Homme... qui... ha... un Homme... un Homme enfin."

    orgon "Qui suit bien ses leçons, goûte une paix profonde,"

    orgon "Et comme du fumier, regarde tout le monde."

    orgon "Oui, je deviens tout autre avec son entretien,"

    orgon "Il m'enseigne à n'avoir affection pour rien ;"

    orgon "De toutes amitiés il détache mon âme ;"

    orgon "Et je verrais mourir Frère, Enfants, Mère, et Femme,"

    orgon "Que je m'en soucierais autant que de cela."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Les sentiments humains, mon Frère, que voilà !"

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Ha, si vous aviez vu comme j'en fis rencontre,"

    orgon "Vous auriez pris pour lui l'amitié que je montre."

    orgon "Chaque jour à l'Église il venait d'un air doux,"

    orgon "Tout vis-à-vis de moi, se mettre à deux genoux."

    orgon "Il attirait les yeux de l'assemblée entière,"

    orgon "Par l'ardeur dont au Ciel il poussait sa prière :"

    orgon "Il faisait des soupirs, de grands élancements,"

    orgon "Et baisait humblement la terre à tous moments ;"

    orgon "Et lorsque je sortais, il me devançait vite,"

    orgon "Pour m'aller à la Porte offrir de l'Eau bénite."

    orgon "Instruit par son Garçon, qui dans tout l'imitait,"

    orgon "Et de son indigence, et de ce qu'il était,"

    orgon "Je lui faisais des dons ; mais avec modestie,"

    orgon "Il me voulait toujours en rendre une partie."

    orgon "C'est trop, me disait-il, c'est trop de la moitié,"

    orgon "Je ne mérite pas de vous faire pitié :"

    orgon "Et quand je refusais de le vouloir reprendre,"

    orgon "Aux Pauvres, à mes yeux, il allait le répandre."

    orgon "Enfin le Ciel, chez moi, me le fit retirer,"

    orgon "Et depuis ce temps-là, tout semble y prospérer."

    orgon "Je vois qu'il reprend tout, et qu'à ma Femme même,"

    orgon "Il prend pour mon honneur un intérêt extrême ;"

    orgon "Il m'avertit des Gens qui lui font les yeux doux,"

    orgon "Et plus que moi, six fois, il s'en montre jaloux."

    orgon "Mais vous ne croiriez point jusqu'où monte son zèle ;"

    orgon "Il s'impute à péché la moindre bagatelle,"

    orgon "Un rien presque suffit pour le scandaliser,"

    orgon "Jusque-là qu'il se vint l'autre jour accuser"

    orgon "D'avoir pris une Puce en faisant sa prière,"

    orgon "Et de l'avoir tuée avec trop de colère."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Parbleu, vous êtes fou, mon Frère, que je crois."

    cleante "Avec de tels discours vous moquez-vous de moi ?"

    cleante "Et que prétendez-vous que tout ce badinage..."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Mon Frère, ce discours sent le libertinage."

    orgon "Vous en êtes un peu dans votre âme {a=myshow|tooltip|text=Enticher : Fig. Gâter par quelque chose de faux ou de moralement mauvais. \[\[L]}entiché{/a} ;"

    orgon "Et comme je vous l'ai plus de dix fois prêché,"

    orgon "Vous vous attirerez quelque méchante affaire."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Voilà de vos pareils le discours ordinaire."

    cleante "Ils veulent que chacun soit aveugle comme eux."

    cleante "C'est être libertin, que d'avoir de bons yeux ;"

    cleante "Et qui n'adore pas de vaines simagrées,"

    cleante "N'a ni respect, ni foi, pour les choses sacrées."

    cleante "Allez, tous vos discours ne me font point de peur ;"

    cleante "Je sais comme je parle, et le Ciel voit mon coeur."

    cleante "De tous vos {a=myshow|tooltip|text=Façonnier : Qui fait trop de façons, de cérémonies. \[\[L]}Façonniers{/a} on n'est point les Esclaves,"

    cleante "Il est de faux Dévots, ainsi que de faux Braves :"

    cleante "Et comme on ne voit pas qu'où l'honneur les conduit,"

    cleante "Les vrais Braves soient ceux qui font beaucoup de bruit ;"

    cleante "Les bons et vrais Dévots qu'on doit suivre à la trace,"

    cleante "Ne sont pas ceux aussi qui font tant de grimace."

    cleante "Les Hommes, la plupart, sont étrangement faits !"

    cleante "Dans la juste nature on ne les voit jamais."

    cleante "La raison a pour eux des bornes trop petites."

    cleante "En chaque caractère ils passent ses limites,"

    cleante "Et la plus noble chose, ils la gâtent souvent,"

    cleante "Pour la vouloir outrer, et pousser trop avant."

    cleante "Que cela vous soit dit en passant, mon Beau-frère."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Oui, vous êtes, sans doute, un Docteur qu'on révère ;"

    orgon "Tout le savoir du Monde est chez vous retiré,"

    orgon "Vous êtes le seul Sage, et le seul éclairé,"

    orgon "Un Oracle, un {a=myshow|tooltip|text=Caton \[\[-234 - -149] : surnommé l'Ancien ou le Censeur, romain célèbre par ses vertus, né à Tusculum, l'an 234 av. J.-C. d'une famille obscure. Il mourut l'an 149 après J.-C. à 85 ans. Censeur, il exerça ses fonctions avec une sévérité qui passa en proverbe. }Caton{/a}, dans le Siècle où nous sommes,"

    orgon "Et près de vous ce sont des Sots, que tous les Hommes."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Je ne suis point, mon Frère, un Docteur révéré,"

    cleante "Et le Savoir, chez moi, n'est pas tout retiré."

    cleante "Mais en un mot je sais, pour toute ma science,"

    cleante "Du faux, avec le vrai, faire la différence :"

    cleante "Et comme je ne vois nul genre de Héros"

    cleante "Qui soient plus à priser que les parfaits Dévots ;"

    cleante "Aucune chose au Monde, et plus noble, et plus belle,"

    cleante "Que la sainte ferveur d'un véritable zèle ;"

    cleante "Aussi ne vois-je rien qui soit plus odieux,"

    cleante "Que le dehors {a=myshow|tooltip|text=Plâtré : Fig. Fardé, peint. \[\[L]}plâtré{/a} d'un zèle spécieux ;"

    cleante "De ce faux caractère, on en voit trop paraître ;"

    cleante "Mais les Dévots de coeur sont aisés à connaître."

    cleante "Notre Siècle, mon Frère, en expose à nos yeux,"

    cleante "Qui peuvent nous servir d'exemples glorieux."

    cleante "Regardez Ariston, regardez Périandre,"

    cleante "Oronte, Alcidamas, Polydore, Clitandre :"

    cleante "Ce titre par aucun ne leur est débattu,"

    cleante "Ce ne sont point du tout Fanfarons de vertu,"

    cleante "On ne voit point en eux ce faste insupportable,"

    cleante "Et leur Dévotion est humaine, est {a=myshow|tooltip|text=Traitable : Doux, maniable, facile. \[\[L]}traitable{/a}."

    cleante "Ils ne censurent point toutes nos actions,"

    cleante "Ils trouvent trop d'orgueil dans ces corrections,"

    cleante "Et laissant la fierté des paroles aux autres,"

    cleante "C'est par leurs actions, qu'ils reprennent les nôtres."

    cleante "Jamais contre un Pêcheur ils n'ont d'acharnement."

    cleante "Ils attachent leur haine au Péché seulement,"

    cleante "Et ne veulent point prendre, avec un zèle extrême,"

    cleante "Les intérêts du Ciel, plus qu'il ne veut lui-même."

    cleante "Voilà mes Gens, voilà comme il faut en user,"

    cleante "Voilà l'exemple enfin qu'il se faut proposer."

    cleante "Votre homme, à dire vrai, n'est pas de ce modèle,"

    cleante "C'est de fort bonne foi que vous vantez son zèle,"

    cleante "Mais par un faux éclat je vous crois ébloui."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Monsieur mon cher Beau-frère, avez-vous tout dit ?"

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Oui."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Je suis votre valet."

    play sound1 footsteps

    orgon "<{i}Il veut s'en aller.{/i}>"

    stop sound1

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}De grâce, un mot, mon Frère,"

    cleante "Votre fils m'a chargé de parler d'une affaire ;"

    cleante "Damis pour son hymen a parole de vous."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Oui."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Vous aviez pris jour pour un lien si doux."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Il est vrai."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Pourquoi donc en différer la fête ?"

    cleante "Avez-vous bien toujours ce mariage en tête ?"

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Peut-être."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Vous voulez manquer à votre foi ?"

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Je ne dis pas cela."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Nul obstacle, je crois,"

    cleante "Ne vous peut empêcher d'accomplir vos promesses."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Selon."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Pour dire un mot, faut-il tant de finesses ?"

    cleante "Damis m'a demandé de vous interroger."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Le Ciel en soit loué."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Mais que lui reporter ?"

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Tout ce qu'il vous plaira."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Mais il est nécessaire"

    cleante "De savoir vos desseins. Quels sont-ils donc ?"

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}De faire"

    orgon "Ce que le Ciel voudra."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Mais parlons tout de bon."

    cleante "Damis a votre foi. La tiendrez-vous, ou non ?"

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Adieu."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "{space=400}Pour son amour, je crains une disgrâce,"

    cleante "Et je dois l'avertir de tout ce qui se passe."

    hide cleante

label Act_2:
    play music "audio/music/3.mp3" fadeout 1.0 fadein 1.0

    scene 5 with fade

    "{b}ACTE II{/b}"

    menu:
        "SCÈNE PREMIÈRE.":
            jump Act_2_Scene_1
        "SCÈNE II.":
            jump Act_2_Scene_2
        "SCÈNE III.":
            jump Act_2_Scene_3
        "SCÈNE IV.":
            jump Act_2_Scene_4
        "SCÈNE V.":
            jump Act_2_Scene_5
        "SCÈNE VI.":
            jump Act_2_Scene_6
        ">":
            jump Further_Act_2_Scene_6_1

label Further_Act_2_Scene_6_1:
    menu:
        "SCÈNE VII.":
            jump Act_2_Scene_7

label Act_2_Scene_1:
    "{b}SCÈNE PREMIÈRE.{/b}"

    show damis at left
    show dorine at right

    "<{i}Damis, Dorine.{/i}>"

    hide damis
    hide dorine

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Que la Foudre, sur l'heure, achève mes destins ;"

    damis "Qu'on me traite partout, du plus grand des {a=myshow|tooltip|text=Faquin : Crocheteur, homme de la lie du peuple, vil et méprisable. Se dit aussi en quelque sorte au figuré, pour un homme sans honneur, sans mérite, sans coeur, digne de toue sorte de mépris. \[\[F]}Faquins{/a},"

    damis "S'il est aucun respect, ni pouvoir, qui m'arrête,"

    damis "Et si je ne fais pas quelque coup de ma tête."

    damis "Il faut que de ce Fat j'arrête les complots,"

    damis "Et qu'à l'oreille, un peu, je lui dise deux mots."

    hide damis

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Ha, tout doux ; envers lui, comme envers votre Père,"

    dorine "Laissez agir les soins de votre Belle-Mère."

    dorine "Sur l'esprit de Tartuffe, elle a quelque crédit ;"

    dorine "Il se rend complaisant à tout ce qu'elle dit,"

    dorine "Et pourrait bien avoir douceur de coeur pour elle."

    dorine "Plût à Dieu qu'il fut vrai ! la chose serait belle."

    dorine "Enfin votre intérêt l'oblige à le mander ;"

    dorine "Sur votre hymen rompu elle veut le sonder,"

    dorine "Savoir ses sentiments et lui faire connaître"

    dorine "Quels fâcheux démêlés il pourra faire naître,"

    dorine "S'il persiste au dessein de nuire à votre espoir."

    dorine "Son Valet dit qu'il prie, et je n'ai pu le voir :"

    dorine "Mais ce Valet m'a dit qu'il s'en allait descendre."

    dorine "Sortez donc, je vous prie, et me laissez l'attendre."

    hide dorine

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Je puis être présent à tout cet entretien."

    hide damis

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Point, il faut qu'ils soient seuls."

    hide dorine

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=400}Je ne lui dirai rien."

    hide damis

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Vous vous moquez ; on sait vos transports ordinaires,"

    dorine "Et c'est le vrai moyen de gâter les affaires."

    dorine "Sortez."

    hide dorine

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=400}Non, je veux voir, sans me mettre en courroux."

    hide damis

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Que vous êtes fâcheux ! Il vient, retirez-vous."

    hide dorine

label Act_2_Scene_2:
    "{b}SCÈNE II.{/b}"

    show tartuffe at left
    show laurent at truecenter
    show dorine at right

    "<{i}Tartuffe, Laurent, Dorine.{/i}>"

    hide tartuffe
    hide laurent
    hide dorine

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE, apercevant Dorine."

    hide tartuffe

    show tartuffe at left
    show dorine at right

    tartuffe "Laurent, serrez ma {a=myshow|tooltip|text=Haire : Petit vêtement tissu de crin en forme de corps de chemise, qui est rude et piquant, que les religieux austères, ou les dévots mettent sur leur chair nue pour se mortifier et faire pénitence. \[\[F]}Haire{/a}, avec ma {a=myshow|tooltip|text=Discipline : est aussi le châtiment ou la peine que souffrent les Religieux qui ont failli, ou ceux qui se veulent mortifier. \[\[F]}Discipline{/a},"

    hide dorine

    show tartuffe at truecenter

    tartuffe "Et priez que toujours le Ciel vous illumine."

    tartuffe "Si l'on vient pour me voir, je vais aux Prisonniers,"

    tartuffe "Des aumônes que j'ai, partager les deniers."

    hide tartuffe

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Que d'affectation, et de {a=myshow|tooltip|text=Forfanterie : Action de forfante. Les Comédiens Italiens font mille forfanteries sur le théâtre. \[\[F]}forfanterie{/a} !"

    hide dorine

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Que voulez-vous ?"

    hide tartuffe

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=200}Vous dire..."

    hide dorine

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "<{i}Il tire un mouchoir de sa poche.{/i}>"

    tartuffe "{space=400}Ah ! mon Dieu, je vous prie,"

    tartuffe "Avant que de parler, prenez-moi ce mouchoir."

    hide tartuffe

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Comment ?"

    hide dorine

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}Couvrez ce Sein, que je ne saurais voir."

    tartuffe "Par de pareils objets les âmes sont blessées,"

    tartuffe "Et cela fait venir de coupables pensées."

    hide tartuffe

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Vous êtes donc bien tendre à la tentation ;"

    dorine "Et la Chair, sur vos sens, fait grande impression ?"

    dorine "Certes, je ne sais pas quelle chaleur vous monte :"

    dorine "Mais à convoiter, moi, je ne suis point si prompte ;"

    dorine "Et je vous verrais nu du haut jusques en bas,"

    dorine "Que toute votre peau ne me tenterait pas."

    hide dorine

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Mettez dans vos discours un peu de modestie,"

    tartuffe "Ou je vais, sur-le-champ, vous quitter la partie."

    hide tartuffe

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Non, non, c'est moi qui vais vous laisser en repos,"

    dorine "Et je n'ai seulement qu'à vous dire deux mots."

    dorine "Madame va venir dans cette Salle basse,"

    dorine "Et d'un mot d'entretien vous demande la grâce."

    hide dorine

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Hélas ! très volontiers."

    hide tartuffe

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE, en soi-même."

    dorine "{space=400}Comme il se radoucit !"

    dorine "Ma foi, je suis toujours pour ce que j'en ai dit."

    hide dorine

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Viendra-t-elle bientôt ?"

    hide tartuffe

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Je l'entends, ce me semble."

    dorine "Oui, c'est elle en personne, et je vous laisse ensemble."

    hide dorine

label Act_2_Scene_3:
    "{b}SCÈNE III.{/b}"

    show elmire at left
    show tartuffe at right

    "<{i}Elmire, Tartuffe.{/i}>"

    hide elmire
    hide tartuffe

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Que le Ciel à jamais, par sa toute bonté,"

    tartuffe "Et de l'âme, et du corps, vous donne la santé ;"

    tartuffe "Et bénisse vos jours autant que le désire"

    tartuffe "Le plus humble de ceux que son amour inspire."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Je suis fort obligée à ce souhait pieux :"

    elmire "Mais prenons une Chaise, afin d'être un peu mieux."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Comment, de votre mal, vous sentez-vous remise ?"

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Fort bien ; et cette fièvre a bientôt quitté prise."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Mes prières n'ont pas le mérite qu'il faut"

    tartuffe "Pour avoir attiré cette {a=myshow|tooltip|text=Grâce d'En haut : puissance divine.}grâce d'En haut{/a} :"

    tartuffe "Mais je n'ai fait au Ciel nulle dévote instance"

    tartuffe "Qui n'ait eu pour objet votre convalescence."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Votre zèle pour moi s'est trop inquiété."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "On ne peut trop chérir votre chère santé ;"

    tartuffe "Et pour la rétablir, j'aurais donné la mienne."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "C'est pousser bien avant la charité Chrétienne ;"

    elmire "Et je vous dois beaucoup, pour toutes ces bontés."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Je fais bien moins pour vous, que vous ne méritez."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "J'ai voulu vous parler en secret, d'une affaire,"

    elmire "Et suis bien aise, ici qu'aucun ne nous éclaire."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "J'en suis ravi de même ; et sans doute il m'est doux,"

    tartuffe "Madame, de me voir, seul à seul, avec vous."

    tartuffe "C'est une occasion qu'au Ciel j'ai demandée,"

    tartuffe "Sans que, jusqu'à cette heure, il me l'ait accordée."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Pour moi, ce que je veux, c'est un mot d'entretien,"

    elmire "Où tout votre coeur s'ouvre, et ne me cache rien."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Et je ne veux aussi, pour grâce singulière,"

    tartuffe "Que montrer à vos yeux mon âme toute entière ;"

    tartuffe "Et vous faire serment, que les bruits que j'ai faits,"

    tartuffe "Des visites qu'ici reçoivent vos attraits,"

    tartuffe "Ne sont pas, envers vous, l'effet d'aucune haine,"

    tartuffe "Mais plutôt d'un transport de zèle qui m'entraîne,"

    tartuffe "Et d'un pur mouvement..."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Je le prends bien aussi,"

    elmire "Et crois que mon salut vous donne ce souci."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    hide tartuffe

    show tartuffe at left
    show elmire at right

    tartuffe "<{i}Il lui serre les bouts des doigts.{/i}>"

    hide elmire

    show tartuffe at truecenter

    tartuffe "Oui, Madame, sans doute ; et ma ferveur est telle..."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Ouf, vous me serrez trop."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}C'est par excès de zèle."

    tartuffe "De vous faire aucun mal, je n'eus jamais dessein,"

    tartuffe "Et j'aurais bien plutôt ..."

    hide tartuffe

    show tartuffe at left
    show elmire at right

    tartuffe "<{i}Il lui met la main sur le genou.{/i}>"

    hide elmire

    show tartuffe at truecenter

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Que fait là votre main ?"

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Je tâte votre habit, l'étoffe en est moelleuse."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Ah ! de grâce, laissez, je suis fort chatouilleuse."

    play sound1 chair

    hide elmire

    show elmire at left
    show tartuffe at right

    elmire "<{i}Elle recule sa chaise et Tartuffe rapproche la sienne.{/i}>"

    hide tartuffe

    show elmire at truecenter

    stop sound1

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Mon Dieu, que de ce Point l'ouvrage est merveilleux !"

    tartuffe "On travaille aujourd'hui, d'un air miraculeux ;"

    tartuffe "Jamais, en toute chose, on n'a vu si bien faire."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Il est vrai. Mais parlons un peu de notre affaire."

    elmire "On tient que mon Mari pour suivre votre loi,"

    elmire "Veut contraindre son Fils et dégager sa foi."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Il m'en a dit deux mots : mais, Madame, à vrai dire,"

    tartuffe "Le salut de Damis n'est pas ce qui m'inspire."

    tartuffe "Et je vois autre part les merveilleux attraits"

    tartuffe "De la félicité qui fait tous mes souhaits."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "C'est que vous n'aimez rien des choses de la Terre."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Mon sein n'enferme pas un coeur qui soit de pierre."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Pour moi, je crois qu'au Ciel tendent tous vos soupirs,"

    elmire "Et que rien, ici-bas, n'arrête vos désirs."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "L'amour qui nous attache aux Beautés éternelles,"

    tartuffe "N'étouffe pas en nous l'amour des temporelles."

    tartuffe "Nos sens facilement peuvent être charmés"

    tartuffe "Des ouvrages parfaits que le Ciel a formés."

    tartuffe "Ses attraits réfléchis brillent dans vos pareilles :"

    tartuffe "Mais il étale en vous ses plus rares merveilles."

    tartuffe "Il a sur votre face épanché des beautés,"

    tartuffe "Dont les yeux sont surpris, et les coeurs transportés ;"

    tartuffe "Et je n'ai pu vous voir, parfaite Créature,"

    tartuffe "Sans admirer en vous l'Auteur de la Nature,"

    tartuffe "Et d'une ardente amour sentir mon coeur atteint,"

    tartuffe "Au plus beau des Portraits où lui-même il s'est peint."

    tartuffe "D'abord j'appréhendai que cette ardeur secrète"

    tartuffe "Ne fût du noir Esprit une surprise adroite ;"

    tartuffe "Et même à fuir vos yeux, mon coeur se résolut,"

    tartuffe "Vous croyant un obstacle à faire mon salut."

    tartuffe "Mais enfin je connus, ô Beauté toute aimable,"

    tartuffe "Que cette passion peut n'être point coupable ;"

    tartuffe "Que je puis l'ajuster avecque la pudeur,"

    tartuffe "Et c'est ce qui m'y fait abandonner mon coeur."

    tartuffe "Ce m'est, je le confesse, une audace bien grande,"

    tartuffe "Que d'oser, de ce coeur, vous adresser l'offrande ;"

    tartuffe "Mais j'attends, en mes voeux, tout de votre bonté,"

    tartuffe "Et rien des vains efforts de mon infirmité."

    tartuffe "En vous est mon espoir, mon bien, ma quiétude :"

    tartuffe "De vous dépend ma peine, ou ma béatitude ;"

    tartuffe "Et je vais être enfin, par votre seul Arrêt,"

    tartuffe "Heureux, si vous voulez ; malheureux, s'il vous plaît."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "La déclaration est tout à fait galante :"

    elmire "Mais elle est, à vrai dire, un peu bien surprenante."

    elmire "Vous deviez, ce me semble, armer mieux votre sein,"

    elmire "Et raisonner un peu sur un pareil dessein."

    elmire "Un Dévot comme vous, et que partout on nomme..."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{a=myshow|tooltip|text=Voir \"Ah ! Pour être romain, je n'en suis pas moins homme :\" dans Sertorius de Pierre Corneille, SERTORIUS, Acte IV, scène 1, vers 1194.}Ah ! pour être Dévot, je n'en suis pas moins homme{/a} ;"

    tartuffe "Et lorsqu'on vient à voir vos célestes appas,"

    tartuffe "Un coeur se laisse prendre, et ne raisonne pas."

    tartuffe "Je sais qu'un tel discours de moi paraît étrange ;"

    tartuffe "Mais, Madame, après tout, je ne suis pas un Ange ;"

    tartuffe "Et si vous condamnez l'aveu que je vous fais,"

    tartuffe "Vous devez vous en prendre à vos charmants attraits."

    tartuffe "Dès que j'en vis briller la splendeur plus qu'humaine,"

    tartuffe "De mon intérieur vous fûtes souveraine."

    tartuffe "De vos regards divins, l'ineffable douceur,"

    tartuffe "Força la résistance où s'obstinait mon coeur ;"

    tartuffe "Elle surmonta tout, jeûnes, prières, larmes,"

    tartuffe "Et tourna tous mes voeux du côté de vos charmes."

    tartuffe "Mes yeux, et mes soupirs, vous l'ont dit mille fois ;"

    tartuffe "Et pour mieux m'expliquer, j'emploie ici la voix."

    tartuffe "Que si vous contemplez, d'une âme un peu bénigne,"

    tartuffe "Les tribulations de votre Esclave indigne ;"

    tartuffe "S'il faut que vos bontés veuillent me consoler,"

    tartuffe "Et jusqu'à mon néant daignent se ravaler,"

    tartuffe "J'aurai toujours pour vous, ô suave merveille,"

    tartuffe "Une dévotion à nulle autre pareille."

    tartuffe "Votre honneur, avec moi, ne court point de hasard ;"

    tartuffe "Et n'a nulle disgrâce à craindre de ma part."

    tartuffe "Tous ces Galants de Cour, dont les Femmes sont folles,"

    tartuffe "Sont bruyants dans leurs faits, et vains dans leurs paroles."

    tartuffe "De leurs progrès sans cesse on les voit se targuer ;"

    tartuffe "Ils n'ont point de faveurs, qu'ils n'aillent divulguer ;"

    tartuffe "Et leur langue indiscrète, en qui l'on se confie,"

    tartuffe "Déshonore l'Autel où leur coeur sacrifie :"

    tartuffe "Mais les Gens comme nous, brûlent d'un feu discret,"

    tartuffe "Avec qui pour toujours on est sûr du secret."

    tartuffe "Le soin que nous prenons de notre renommée,"

    tartuffe "Répond de toute chose à la Personne aimée ;"

    tartuffe "Et c'est en nous qu'on trouve, acceptant notre coeur,"

    tartuffe "De l'amour sans scandale, et du plaisir sans peur."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Je vous écoute dire, et votre Rhétorique,"

    elmire "En termes assez forts, à mon âme s'explique."

    elmire "N'appréhendez-vous point, que je ne sois d'humeur"

    elmire "À dire à mon Mari cette galante ardeur ?"

    elmire "Et que le prompt avis d'un amour de la sorte,"

    elmire "Ne pût bien altérer l'amitié qu'il vous porte ?"

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Je sais que vous avez trop de {a=myshow|tooltip|text=Bénignité : Humanité, douceur, indulgence. \[\[F]}bénignité{/a},"

    tartuffe "Et que vous ferez grâce à ma témérité ;"

    tartuffe "Que vous m'excuserez sur l'humaine faiblesse"

    tartuffe "Des violents transports d'un amour qui vous blesse ;"

    tartuffe "Et considérerez, en regardant votre air,"

    tartuffe "Que l'on n'est pas aveugle, et qu'un Homme est de chair."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "D'autres prendraient cela d'autre façon, peut-être ;"

    elmire "Mais ma discrétion se veut faire paraître."

    elmire "Je ne redirai point l'affaire à mon Époux ;"

    elmire "Mais je veux en revanche une chose de vous."

    elmire "Et..."

    hide elmire

label Act_2_Scene_4:
    "{b}SCÈNE IV.{/b}"

    show damis at left
    show elmire at truecenter
    show tartuffe at right

    "<{i}DAMIS, ELMIRE, TARTUFFE.{/i}>"

    hide damis
    hide elmire
    hide tartuffe

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS, sortant du petit cabinet où il s'était retiré."

    play sound1 footsteps

    damis "{space=400}Non, Madame, non ceci doit se répandre."

    stop sound1

    damis "J'étais en cet endroit, d'où j'ai pu tout entendre ;"

    damis "Et la bonté du Ciel m'y semble avoir conduit,"

    damis "Pour confondre l'orgueil d'un Traître qui me nuit ;"

    damis "Pour m'ouvrir une voie à prendre la vengeance"

    damis "De son hypocrisie, et de son insolence ;"

    damis "A détromper mon Père, et lui mettre en plein jour,"

    damis "L'âme d'un Scélérat qui vous parle d'amour."

    hide damis

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Non, Damis, il suffit qu'il se rende plus sage,"

    elmire "Et tâche à mériter la grâce où je m'engage."

    elmire "Puisque je l'ai promis, ne m'en dédites pas."

    elmire "Ce n'est point mon humeur de faire des éclats ;"

    elmire "Une Femme se rit de sottises pareilles,"

    elmire "Et jamais d'un Mari n'en trouble les oreilles."

    hide elmire

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Vous avez vos raisons pour en user ainsi ;"

    damis "Et pour faire autrement, j'ai les miennes aussi."

    damis "Le vouloir épargner, est une raillerie,"

    damis "Et l'insolent orgueil de sa Cagoterie,"

    damis "N'a triomphé que trop de mon juste courroux,"

    damis "Et que trop excité de désordre chez nous."

    damis "Le Fourbe, trop longtemps, a gouverné mon Père,"

    damis "Et desservi mes feux sans craindre ma colère."

    damis "Il faut que du Perfide il soit désabusé,"

    damis "Et le ciel, pour cela, m'offre un moyen aisé."

    damis "De cette occasion, je lui suis redevable ;"

    damis "Et pour la négliger, elle est trop favorable."

    damis "Ce serait mériter qu'il me la vînt ravir,"

    damis "Que de l'avoir en main, et ne pas m'en servir."

    hide damis

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Damis..."

    hide elmire

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=400}Non, s'il vous plaît, il faut que je me croie."

    damis "Mon âme est maintenant au comble de sa joie ;"

    damis "Et vos discours en vain prétendent m'obliger"

    damis "À quitter le plaisir de me pouvoir venger."

    damis "Sans aller plus avant, je vais vider d'affaire ;"

    damis "Et voici justement de quoi me satisfaire."

    hide damis

label Act_2_Scene_5:
    "{b}SCÈNE V.{/b}"

    show damis at left
    show tartuffe at truecenter
    show elmire at right

    "<{i}Orgon, Damis, Tartuffe, Elmire.{/i}>"

    hide orgon
    hide damis
    hide tartuffe
    hide elmire

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Nous allons régaler, mon Père, votre abord,"

    damis "D'un incident tout frais, qui vous surprendra fort."

    damis "Vous êtes bien payé de toutes vos caresses ;"

    damis "Et Monsieur, d'un beau prix, reconnaît vos tendresses."

    damis "Son grand zèle, pour vous, vient de se déclarer."

    damis "Il ne va pas à moins qu'à vous déshonorer ;"

    damis "Et je l'ai surpris, là, qui faisait à Madame"

    damis "L'injurieux aveu d'une coupable flamme."

    damis "Elle est d'une humeur douce, et son coeur trop discret"

    damis "Voulait, à toute force, en garder le secret :"

    damis "Mais je ne puis flatter une telle impudence,"

    damis "Et crois que vous la taire, est vous faire une offense."

    hide damis

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Oui, je tiens que jamais, de tous ces vains propos,"

    elmire "On ne doit d'un Mari {a=myshow|tooltip|text=Traverser : Susciter des obstacles, des embarras. \[\[L]}traverser{/a} le repos ;"

    elmire "Que ce n'est point de là que l'honneur peut dépendre,"

    elmire "Et qu'il suffit, pour nous, de savoir nous défendre."

    elmire "Ce sont mes sentiments ; et vous n'auriez rien dit,"

    elmire "Damis, si j'avais eu sur vous quelque crédit."

    hide elmire

label Act_2_Scene_6:
    "{b}SCÈNE VI.{/b}"

    show orgon at left
    show damis at truecenter
    show tartuffe at right

    "<{i}Orgon, Damis, Tartuffe.{/i}>"

    hide orgon
    hide damis
    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Ce que je viens d'entendre, ô Ciel ! est-il croyable ?"

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Oui, mon Frère, je suis un méchant, un coupable,"

    tartuffe "Un malheureux Pécheur, tout plein d'iniquité,"

    tartuffe "Le plus grand scélérat qui jamais ait été."

    tartuffe "Chaque instant de ma vie est chargé de souillures,"

    tartuffe "Elle n'est qu'un amas de crimes, et d'ordures ;"

    tartuffe "Et je vois que le Ciel, pour ma punition,"

    tartuffe "Me veut mortifier en cette occasion."

    tartuffe "De quelque grand forfait qu'on me puisse reprendre,"

    tartuffe "Je n'ai garde d'avoir l'orgueil de m'en défendre."

    tartuffe "Croyez ce qu'on vous dit, armez votre courroux,"

    tartuffe "Et comme un Criminel, chassez-moi de chez vous."

    tartuffe "Je ne saurais avoir tant de honte en partage,"

    tartuffe "Que je n'en aie encor mérité davantage."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON, à son fils."

    hide orgon

    show orgon at left
    show damis at right

    orgon "Ah ! traître, oses-tu bien, par cette fausseté,"

    hide damis

    show orgon at truecenter

    orgon "Vouloir de sa vertu ternir la pureté ?"

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Quoi! la feinte douceur de cette âme hypocrite"

    damis "Vous fera démentir..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Tais-toi, peste maudite."

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Ah ! laissez-le parler, vous l'accusez à tort,"

    tartuffe "Et vous ferez bien mieux de croire à son rapport."

    tartuffe "Pourquoi, sur un tel fait, m'être si favorable ?"

    tartuffe "Savez-vous, après tout, de quoi je suis capable ?"

    tartuffe "Vous fiez-vous, mon Frère, à mon extérieur ?"

    tartuffe "Et pour tout ce qu'on voit, me croyez-vous meilleur ?"

    tartuffe "Non, non, vous vous laissez tromper à l'apparence,"

    tartuffe "Et je ne suis rien moins, hélas ! que ce qu'on pense."

    tartuffe "Tout le monde me prend pour un Homme de bien ;"

    tartuffe "Mais la vérité pure, est, que je ne vaux rien."

    hide tartuffe

    show tartuffe at left
    show damis at right

    tartuffe "<{i}S'adressant à Damis.{/i}>"

    hide damis

    show tartuffe at truecenter

    tartuffe "Oui, mon cher Fils, parlez, traitez-moi de perfide,"

    tartuffe "D'infâme, de perdu, de voleur, d'homicide."

    tartuffe "Accablez-moi de noms encor plus détestés."

    tartuffe "Je n'y contredis point, je les ai mérités,"

    tartuffe "Et j'en veux à genoux souffrir l'ignominie,"

    tartuffe "Comme une honte due aux crimes de ma vie."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON, à Tartuffe."

    hide orgon

    show orgon at left
    show tartuffe at right

    orgon "Mon Frère, c'en est trop."

    hide tartuffe

    show orgon at truecenter

    hide orgon

    show orgon at left
    show damis at right

    orgon "<{i}À son Fils.{/i}>"

    hide damis

    show orgon at truecenter

    orgon "{space=400}Ton coeur ne se rend point,"

    orgon "Traître."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=400}Quoi ! ses discours vous séduiront au point..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Tais-toi, pendard."

    hide orgon

    show orgon at left
    show tartuffe at right

    orgon "<{i}À Tartuffe.{/i}>"

    hide tartuffe

    show orgon at truecenter

    orgon "{space=400}Mon Frère, eh ! levez-vous, de grâce."

    hide orgon

    show orgon at left
    show damis at right

    orgon "<{i}À son Fils.{/i}>"

    hide damis

    show orgon at truecenter

    orgon "Infâme."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=200}Il peut..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=200}Tais-toi."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=400}J'enrage ! Quoi, je passe..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Si tu dis un seul mot, je te romprai les bras."

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Mon Frère, au nom de Dieu, ne vous emportez pas."

    tartuffe "J'aimerais mieux souffrir la peine la plus dure,"

    tartuffe "Qu'il eût reçu pour moi la moindre égratignure."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON, à son fils."

    hide orgon

    show orgon at left
    show damis at right

    orgon "Ingrat."

    hide damis

    show orgon at truecenter

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}Laissez-le en paix. S'il faut à deux genoux"

    tartuffe "Vous demander sa grâce..."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON, à Tartuffe."

    hide orgon

    show orgon at left
    show tartuffe at right

    orgon "{space=400}Hélas ! vous moquez-vous ?"

    hide tartuffe

    show orgon at truecenter

    hide orgon

    show orgon at left
    show damis at right

    orgon "<{i}À son Fils.{/i}>"

    hide damis

    show orgon at truecenter

    orgon "Coquin, vois sa bonté."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=200}Donc..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=200}Paix."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "{space=200}Quoi, je..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Paix, dis-je."

    orgon "Je sais bien quel motif, à l'attaquer, t'oblige."

    orgon "Vous le haïssez tous, et je vois aujourd'hui,"

    orgon "Femme, Enfants, et Valets, déchaînés contre lui."

    orgon "On met impudemment toute chose en usage,"

    orgon "Pour ôter de chez moi ce dévot Personnage :"

    orgon "Mais plus on fait d'effort afin de l'en bannir,"

    orgon "Plus j'en veux employer à l'y mieux retenir."

    orgon "Ah ! je vous brave tous, et vous ferai connaître,"

    orgon "Qu'il faut qu'on m'obéisse, et que je suis le Maître."

    orgon "Allons, qu'on se rétracte, et qu'à l'instant, fripon,"

    orgon "On se jette à ses pieds, pour demander pardon."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Qui, moi ? de ce coquin, qui par ses impostures..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Ah ! tu résistes, gueux, et lui dis des injures ?"

    orgon "Un bâton, un bâton,"

    hide orgon

    show orgon at left
    show tartuffe at right

    orgon "<{i}À Tartuffe.{/i}>"

    hide tartuffe

    show orgon at truecenter

    orgon "{space=400}Ne me retenez pas."

    hide orgon

    show orgon at left
    show damis at right

    orgon "<{i}À son Fils.{/i}>"

    hide damis

    show orgon at truecenter

    orgon "Sus, que de ma Maison on sorte de ce pas,"

    orgon "Et que d'y revenir, on n'ait jamais l'audace."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Oui, je sortirai, mais..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Vite, quittons la place."

    orgon "Je te prive, pendard, de ma succession,"

    orgon "Et te donne, de plus, ma malédiction."

    hide orgon

label Act_2_Scene_7:
    "{b}SCÈNE VII.{/b}"

    show orgon at left
    show tartuffe at right

    "<{i}Orgon, Tartuffe.{/i}>"

    hide orgon
    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Offenser de la sorte une sainte Personne !"

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Ô Ciel ! pardonne-lui la douleur qu'il me donne."

    hide tartuffe

    show tartuffe at left
    show orgon at right

    tartuffe "<{i}À Orgon.{/i}>"

    hide orgon

    show tartuffe at truecenter

    tartuffe "Si vous pouviez savoir avec quel déplaisir"

    tartuffe "Je vois qu'envers mon Frère, on tâche à me noircir..."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Hélas !"

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}Le seul penser de cette ingratitude"

    tartuffe "Fait souffrir à mon âme un supplice si rude..."

    tartuffe "L'horreur que j'en conçois... J'ai le coeur si serré,"

    tartuffe "Que je ne puis parler, et crois que j'en mourrai."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    play sound1 running
    play sound2 male_cry

    hide orgon

    show orgon at left
    show damis at right

    orgon "<{i}Il court tout en larmes à la Porte par où il a chassé son Fils.{/i}>"

    hide damis

    show orgon at truecenter

    stop sound1
    stop sound2

    orgon "Coquin. Je me repens que ma main t'ait fait grâce,"

    orgon "Et ne t'ait pas d'abord assommé sur la place."

    orgon "Remettez-vous, mon Frère, et ne vous fâchez pas."

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Rompons, rompons le cours de ces fâcheux débats."

    tartuffe "Je regarde céans quels grands troubles j'apporte,"

    tartuffe "Et crois qu'il est besoin, mon Frère, que j'en sorte."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Comment ? Vous moquez-vous ?"

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}On m'y hait, et je vois"

    tartuffe "Qu'on cherche à vous donner des soupçons de ma foi."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Qu'importe ; voyez-vous que mon coeur les écoute ?"

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "On ne manquera pas de poursuivre, sans doute ;"

    tartuffe "Et ces mêmes rapports, qu'ici vous rejetez,"

    tartuffe "Peut-être, une autre fois, seront-ils écoutés."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Non, mon Frère, jamais."

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}Ah ! mon Frère, une Femme"

    tartuffe "Aisément, d'un Mari, peut bien surprendre l'âme."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Non, non."

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}Laissez-moi vite, en m'éloignant d'ici,"

    tartuffe "Leur ôter tout sujet de m'attaquer ainsi."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Non, vous demeurerez, il y va de ma vie."

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Hé bien, il faudra donc que je me mortifie."

    tartuffe "Pourtant, si vous vouliez..."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=200}Ah !"

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}Soit, n'en parlons plus."

    tartuffe "Mais je sais comme il faut en user là-dessus."

    tartuffe "L'honneur est délicat, et l'amitié m'engage"

    tartuffe "À prévenir les bruits, et les sujets d'ombrage."

    tartuffe "Je fuirai votre Épouse, et vous ne me verrez..."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Non, en dépit de tous, vous la fréquenterez."

    orgon "Faire enrager le monde, est ma plus grande joie,"

    orgon "Et je veux qu'à toute heure avec elle on vous voie."

    orgon "Ce n'est pas tout encor ; pour les mieux braver tous,"

    orgon "Je ne veux point avoir d'autre héritier que vous ;"

    orgon "Et je vais de ce pas, en fort bonne manière,"

    orgon "Vous faire de mon bien donation entière."

    orgon "Un bon et franc Ami, que pour Frère je prends,"

    orgon "M'est bien plus cher que Fils, que Femme et que Parents."

    orgon "N'accepteriez-vous pas ce que je vous propose ?"

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "La volonté du Ciel soit faite en toute chose."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Le pauvre Homme ! Allons vite en dresser un Écrit,"

    orgon "Et que puisse l'Envie en crever de dépit."

    hide orgon

label Act_3:
    play music "audio/music/12.mp3" fadeout 1.0 fadein 1.0

    scene 1 with fade

    "{b}ACTE III{/b}"

    menu:
        "SCÈNE PREMIÈRE.":
            jump Act_3_Scene_1
        "SCÈNE II.":
            jump Act_3_Scene_2
        "SCÈNE III.":
            jump Act_3_Scene_3
        "SCENE IV.":
            jump Act_3_Scene_4
        "SCÈNE V.":
            jump Act_3_Scene_5
        "SCÈNE VI.":
            jump Act_3_Scene_6
        ">":
            jump Further_Act_3_Scene_6_1

label Further_Act_3_Scene_6_1:
    menu:
        "SCÈNE VII.":
            jump Act_3_Scene_7
        "SCÈNE VIII.":
            jump Act_3_Scene_8
        "SCÈNE IX ET DERNIÈRE.":
            jump Act_3_Scene_9

label Act_3_Scene_1:
    "{b}SCÈNE PREMIÈRE.{/b}"

    show cleante at left
    show tartuffe at right

    "<{i}Cléante, Tartuffe.{/i}>"

    hide cleante
    hide tartuffe

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Oui, tout le monde en parle, et vous pouvez m'en croire."

    cleante "L'éclat que fait ce bruit, n'est point à votre gloire ;"

    cleante "Et je vous ai trouvé, Monsieur, fort à propos,"

    cleante "Pour vous en dire net ma pensée en deux mots."

    cleante "Je n'examine point à fond ce qu'on expose,"

    cleante "Je passe là-dessus, et prends au pis la chose."

    cleante "Supposons que Damis n'en ait pas bien usé,"

    cleante "Et que ce soit à tort qu'on vous ait accusé :"

    cleante "N'est-il pas d'un Chrétien, de pardonner l'offense,"

    cleante "Et d'éteindre en son coeur tout désir de vengeance ?"

    cleante "Et devez-vous souffrir, pour votre démêlé,"

    cleante "Que du Logis d'un Père, un Fils soit exilé ?"

    cleante "Je vous le dis encore, et parle avec franchise ;"

    cleante "Il n'est petit, ni grand, qui ne s'en scandalise ;"

    cleante "Et si vous m'en croyez, vous pacifierez tout,"

    cleante "Et ne pousserez point les affaires à bout."

    cleante "Sacrifiez à Dieu toute votre colère,"

    cleante "Et remettez le Fils en grâce avec le père."

    hide cleante

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Hélas ! je le voudrais, quant à moi, de bon coeur ;"

    tartuffe "Je ne garde pour lui, Monsieur, aucune aigreur,"

    tartuffe "Je lui pardonne tout, de rien je ne le blâme,"

    tartuffe "Et voudrais le servir du meilleur de mon âme :"

    tartuffe "Mais l'intérêt du Ciel n'y saurait consentir ;"

    tartuffe "Et s'il rentre céans, c'est à moi d'en sortir."

    tartuffe "Après son action qui n'eut jamais d'égale,"

    tartuffe "Le commerce, entre nous, porterait du scandale :"

    tartuffe "Dieu sait ce que d'abord tout le monde en croirait ;"

    tartuffe "À pure politique, on me l'imputerait ;"

    tartuffe "Et l'on dirait partout, que me sentant coupable,"

    tartuffe "Je feins, pour qui m'accuse, un zèle charitable ;"

    tartuffe "Que mon coeur l'appréhende, et veut le ménager,"

    tartuffe "Pour le pouvoir, sous main, au silence engager."

    hide tartuffe

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Vous nous payez ici d'excuses colorées,"

    cleante "Et toutes vos raisons, Monsieur, sont trop tirées."

    cleante "Des intérêts du Ciel, pourquoi vous chargez-vous ?"

    cleante "Pour punir le coupable, a-t-il besoin de nous ?"

    cleante "Laissez-lui, laissez-lui le soin de ses vengeances,"

    cleante "Ne songez qu'au pardon qu'il prescrit des offenses ;"

    cleante "Et ne regardez point aux jugements humains,"

    cleante "Quand vous suivez du Ciel les ordres souverains."

    cleante "Quoi ! le faible intérêt de ce qu'on pourra croire,"

    cleante "D'une bonne action, empêchera la gloire ?"

    cleante "Non, non, faisons toujours ce que le Ciel prescrit,"

    cleante "Et d'aucun autre soin ne nous brouillons l'esprit."

    hide cleante

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Je vous ai déjà dit que mon coeur lui pardonne,"

    tartuffe "Et c'est faire, Monsieur, ce que le Ciel ordonne :"

    tartuffe "Mais après le scandale, et l'affront d'aujourd'hui,"

    tartuffe "Le Ciel n'ordonne pas que je vive avec lui."

    hide tartuffe

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Et vous ordonne-t-il, Monsieur, d'ouvrir l'oreille"

    cleante "À ce qu'un pur caprice à son Père conseille ?"

    cleante "Et d'accepter le don qui vous est fait d'un bien"

    cleante "Où le droit vous oblige à ne prétendre rien."

    hide cleante

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Ceux qui me connaîtront, n'auront pas la pensée"

    tartuffe "Que ce soit un effet d'une âme intéressée."

    tartuffe "Tous les biens de ce monde ont pour moi peu d'appas,"

    tartuffe "De leur éclat trompeur je ne m'éblouis pas ;"

    tartuffe "Et si je me résous à recevoir du Père"

    tartuffe "Cette donation qu'il a voulu me faire,"

    tartuffe "Ce n'est à dire vrai, que parce que je crains"

    tartuffe "Que tout ce bien ne tombe en de méchantes mains ;"

    tartuffe "Qu'il ne trouve des Gens, qui l'ayant en partage,"

    tartuffe "En fassent, dans le Monde, un criminel usage ;"

    tartuffe "Et ne s'en servent pas, ainsi que j'ai dessein,"

    tartuffe "Pour la gloire du Ciel, et le bien du prochain."

    hide tartuffe

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Hé, Monsieur, n'ayez point ces délicates craintes,"

    cleante "Qui d'un juste héritier peuvent causer les plaintes."

    cleante "Souffrez, sans vous vouloir embarrasser de rien,"

    cleante "Qu'il soit, à ses périls, possesseur de son bien ;"

    cleante "Et songez qu'il vaut mieux encor qu'il en {a=myshow|tooltip|text=Mésuser : User mal de quelque chose, en abuser. \[\[F]}mésuse{/a},"

    cleante "Que si de l'en frustrer, il faut qu'on vous accuse."

    cleante "J'admire seulement que, sans confusion,"

    cleante "Vous en ayez souffert la proposition :"

    cleante "Car enfin, le vrai zèle a-t-il quelque maxime"

    cleante "Qui montre à dépouiller l'héritier légitime ?"

    cleante "Et s'il faut que le Ciel dans votre coeur ait mis"

    cleante "Un invincible obstacle à vivre avec Damis,"

    cleante "Ne vaudrait-il pas mieux, qu'en Personne discrète,"

    cleante "Vous fissiez de céans une honnête retraite,"

    cleante "Que de souffrir ainsi, contre toute raison,"

    cleante "Qu'on en chasse, pour vous, le Fils de la Maison ?"

    cleante "Croyez-moi, c'est donner de votre {a=myshow|tooltip|text=Prud'homie : Probité. \[\[F]}prud'homie{/a},"

    cleante "Monsieur ..."

    hide cleante

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "{space=400}Il est, Monsieur, trois heures et demie ;"

    tartuffe "Certain devoir pieux me demande là-haut,"

    tartuffe "Et vous m'excuserez, de vous quitter sitôt."

    hide tartuffe

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Ah !"

    hide cleante

label Act_3_Scene_2:
    "{b}SCÈNE II.{/b}"

    show damis at left
    show dorine at truecenter
    show cleante at right

    "<{i}Elmire, Damis, Dorine, Cléante.{/i}>"

    hide elmire
    hide damis
    hide dorine
    hide cleante

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}De grâce, aidez nous à dissiper l'orage,"

    dorine "Monsieur, son âme souffre une douleur sauvage,"

    dorine "Condamné à sortir du logis dès ce soir,"

    dorine "Damis, tout courroucé, succombe au désespoir."

    dorine "Son père vient ; joignons nos efforts, je vous prie,"

    dorine "Et tâchons d'ébranler de force, ou d'industrie,"

    dorine "Ce malheureux dessein qui nous a tous troublés."

    hide dorine

label Act_3_Scene_3:
    "{b}SCÈNE III.{/b}"

    show damis at left
    show cleante at truecenter
    show dorine at right

    "<{i}Orgon, Elmire, Damis, Cléante, Dorine.{/i}>"

    hide orgon
    hide elmire
    hide damis
    hide cleante
    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Ha, je me réjouis de vous voir assemblés."

    hide orgon

    show orgon at left
    show damis at right

    orgon "<{i}À Damis.{/i}>"

    hide damis

    show orgon at truecenter

    orgon "Je porte, en cet écrit, de quoi vous faire rire,"

    orgon "Et vous savez déjà ce que cela veut dire..."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS, à genoux."

    damis "Mon père, au nom du Ciel, qui connaît ma douleur,"

    damis "Et par tout ce qui peut émouvoir votre coeur,"

    damis "Relâchez-vous un peu des droits de la naissance,"

    damis "Et dispensez mes voeux de cette obéissance."

    damis "Ne me réduisez point, par cette dure Loi,"

    damis "Jusqu'à me plaindre au Ciel de ce que je vous dois :"

    damis "Et cette vie, hélas ! que vous m'avez donnée,"

    damis "Ne me la rendez pas, mon Père, infortunée."

    damis "Si contre un doux espoir que j'avais pu former,"

    damis "Vous me défendez d'être à ce que j'ose aimer ;"

    damis "Au moins, par vos bontés, qu'à vos genoux j'implore,"

    damis "Ne me privez donc pas de ces lieux que j'adore ;"

    damis "Et ne me portez point à quelque désespoir,"

    damis "En vous servant, sur moi, de tout votre pouvoir."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON, se sentant attendrir."

    orgon "Allons, ferme, mon coeur, point de faiblesse humaine."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Vos tendresses pour lui, ne me font point de peine ;"

    damis "Faites-les éclater, donnez-lui votre bien ;"

    damis "Et si ce n'est assez, joignez-y tout le mien,"

    damis "J'y consens de bon coeur, et je vous l'abandonne."

    damis "Mais, de grâce laissez..."

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Debout. Je vous l'ordonne."

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Mais quoi..."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Taisez-vous, vous. Parlez à votre écot,"

    orgon "Je vous défends, tout net, d'oser dire un seul mot."

    hide orgon

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Si par quelque conseil, vous souffrez qu'on réponde..."

    hide cleante

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Mon Frère, vos conseils sont les meilleurs du monde,"

    orgon "Ils sont bien raisonnés, et j'en fais un grand cas ;"

    orgon "Mais vous trouverez bon que je n'en use pas."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE, à son mari."

    hide elmire

    show elmire at left
    show orgon at right

    elmire "À voir ce que je vois, je ne sais plus que dire,"

    hide orgon

    show elmire at truecenter

    elmire "Et votre aveuglement fait que je vous admire."

    elmire "C'est être bien coiffé, bien prévenu de lui,"

    elmire "Que de nous démentir sur le fait d'aujourd'hui."

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Je suis votre Valet, et crois les apparences."

    orgon "Pour mon fripon de Fils, je sais vos complaisances,"

    orgon "Et vous avez eu peur de le désavouer"

    orgon "Du trait qu'à ce pauvre Homme il a voulu jouer."

    orgon "Vous étiez trop tranquille enfin, pour être crue,"

    orgon "Et vous auriez paru d'autre manière émue."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Est-ce qu'au simple aveu d'un amoureux transport,"

    elmire "Il faut que notre honneur se gendarme si fort ?"

    elmire "Et ne peut-on répondre à tout ce qui le touche,"

    elmire "Que le feu dans les yeux, et l'injure à la bouche ?"

    elmire "Pour moi, de tels propos, je me ris simplement,"

    elmire "Et l'éclat, là-dessus, ne me plaît nullement."

    elmire "J'aime qu'avec douceur nous nous montrions sages,"

    elmire "Et ne suis point, du tout, pour ces prudes sauvages,"

    elmire "Dont l'honneur est armé de griffes, et de dents,"

    elmire "Et veut, au moindre mot, dévisager les Gens."

    elmire "Me préserve le Ciel d'une telle sagesse !"

    elmire "Je veux une Vertu qui ne soit point diablesse,"

    elmire "Et crois que d'un refus, la discrète froideur,"

    elmire "N'en est pas moins puissante à rebuter un coeur."

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Enfin je sais l'affaire, et ne prends point le change."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "J'admire, encore un coup, cette faiblesse étrange."

    elmire "Mais que me répondrait votre incrédulité,"

    elmire "Si je vous faisais voir qu'on vous dit vérité ?"

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Voir ?"

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=200}Oui."

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=200}Chansons."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Mais quoi ! si je trouvais manière"

    elmire "De vous le faire voir avec pleine lumière ?"

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Contes en l'air."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Quel homme ! Au moins répondez-moi."

    elmire "Je ne vous parle pas de nous ajouter foi :"

    elmire "Mais supposons ici, que d'un lieu qu'on peut prendre,"

    elmire "On vous fît clairement tout voir, et tout entendre,"

    elmire "Que diriez-vous alors de votre Homme de bien ?"

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "En ce cas, je dirais que... Je ne dirais rien,"

    orgon "Car cela ne se peut."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}L'erreur trop longtemps dure,"

    elmire "Et c'est trop condamner ma bouche d'imposture."

    elmire "Il faut que par plaisir, et sans aller plus loin,"

    elmire "De tout ce qu'on vous dit, je vous fasse témoin."

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Soit, je vous prends au mot. Nous verrons votre adresse"

    orgon "Et comment vous pourrez remplir cette promesse."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Faites-le-moi venir."

    hide elmire

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "{space=400}Son esprit est rusé,"

    dorine "Et peut-être, à surprendre, il sera malaisé."

    hide dorine

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Non, on est aisément dupé par ce qu'on aime,"

    elmire "Et l'amour-propre, engage à se tromper soi-même."

    elmire "Faites-le-moi descendre ; et vous, retirez-vous."

    hide elmire

    show elmire at left
    show cleante at truecenter
    show damis at right

    elmire "<{i}Parlant à Cléante et à Damis.{/i}>"

    hide cleante
    hide damis

    show elmire at truecenter

    hide elmire

label Act_3_Scene_4:
    "{b}SCENE IV.{/b}"

    show elmire at left
    show orgon at right

    "<{i}Elmire, Orgon.{/i}>"

    hide elmire
    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Approchons cette Table, et vous mettez dessous"

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Comment ?"

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Vous bien cacher, est un point nécessaire."

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Pourquoi sous cette Table ?"

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Ah ! mon Dieu, laissez faire,"

    elmire "J'ai mon dessein en tête, et vous en jugerez."

    elmire "Mettez-vous là, vous dis-je ; et quand vous y serez,"

    elmire "Gardez qu'on ne vous voie, et qu'on ne vous entende."

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Je confesse qu'ici ma complaisance est grande ;"

    orgon "Mais de votre entreprise, il vous faut voir sortir."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Vous n'aurez, que je crois, rien à me repartir."

    hide elmire

    show elmire at left
    show orgon at right

    elmire "<{i}À son Mari qui est sous la Table.{/i}>"

    hide orgon

    show elmire at truecenter

    elmire "Au moins, je vais toucher une étrange matière,"

    elmire "Ne vous scandalisez en aucune manière."

    elmire "Quoi que je puisse dire, il doit m'être permis,"

    elmire "Et c'est pour vous convaincre, ainsi que j'ai promis."

    elmire "Je vais par des douceurs, puisque j'y suis réduite,"

    elmire "Faire poser le masque à cette âme hypocrite,"

    elmire "Flatter, de son amour, les désirs effrontés,"

    elmire "Et donner un champ libre à ses témérités."

    elmire "Comme c'est pour vous seul, et pour mieux le confondre,"

    elmire "Que mon âme à ses voeux va feindre de répondre,"

    elmire "J'aurai lieu de cesser dès que vous vous rendrez,"

    elmire "Et les choses n'iront que jusqu'où vous voudrez."

    elmire "C'est à vous d'arrêter son ardeur insensée,"

    elmire "Quand vous croirez l'affaire assez avant poussée ;"

    elmire "D'épargner votre Femme, et de ne m'exposer"

    elmire "Qu'à ce qu'il vous faudra pour vous désabuser."

    elmire "Ce sont vos intérêts, vous en serez le maître,"

    elmire "Et... L'on vient, tenez-vous, et gardez de paraître."

    hide elmire

label Act_3_Scene_5:
    "{b}SCÈNE V.{/b}"

    show tartuffe at left
    show elmire at truecenter
    show orgon at right

    "<{i}Tartuffe, Elmire, Orgon.{/i}>"

    hide tartuffe
    hide elmire
    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "On m'a dit qu'en ce lieu vous me vouliez parler."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Oui, l'on a des secrets à vous y révéler :"

    elmire "Mais tirez cette Porte avant qu'on vous les dise,"

    elmire "Et regardez partout, de crainte de surprise :"

    elmire "Une affaire pareille à celle de tantôt,"

    elmire "N'est pas assurément ici ce qu'il nous faut."

    elmire "Jamais il ne s'est vu de surprise de même,"

    elmire "Damis m'a fait, pour vous, une frayeur extrême,"

    elmire "Et vous avez bien vu que j'ai fait mes efforts"

    elmire "Pour rompre son dessein, et calmer ses transports."

    elmire "Mon trouble, il est bien vrai, m'a si fort possédée,"

    elmire "Que de le démentir je n'ai point eu l'idée :"

    elmire "Mais par là, grâce au Ciel, tout a bien mieux été,"

    elmire "Et les choses en sont dans plus de sûreté."

    elmire "L'estime où l'on vous tient, a dissipé l'orage,"

    elmire "Et mon Mari, de vous, ne peut prendre d'ombrage."

    elmire "Pour mieux braver l'éclat des mauvais jugements,"

    elmire "Il veut que nous soyons ensemble à tous moments ;"

    elmire "Et c'est par où je puis, sans peur d'être blâmée,"

    elmire "Me trouver ici seule avec vous enfermée,"

    elmire "Et ce qui m'autorise à vous ouvrir un coeur"

    elmire "Un peu trop prompt, peut-être, à souffrir votre ardeur."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Ce langage, à comprendre, est assez difficile,"

    tartuffe "Madame, et vous parliez tantôt d'un autre style."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Ah ! si d'un tel refus vous êtes en courroux,"

    elmire "Que le coeur d'une femme est mal connu de vous !"

    elmire "Et que vous savez peu ce qu'il veut faire entendre,"

    elmire "Lorsque si faiblement on le voit se défendre !"

    elmire "Toujours notre pudeur combat, dans ces moments,"

    elmire "Ce qu'on peut nous donner de tendres sentiments."

    elmire "Quelque raison qu'on trouve à l'amour qui nous dompte,"

    elmire "On trouve à l'avouer, toujours un peu de honte ;"

    elmire "On s'en défend d'abord ; mais de l'air qu'on s'y prend,"

    elmire "On fait connaître assez que notre coeur se rend ;"

    elmire "Qu'à nos voeux, par honneur, notre bouche s'oppose,"

    elmire "Et que de tels refus promettent toute chose."

    elmire "C'est vous faire, sans doute, un assez libre aveu,"

    elmire "Et sur notre pudeur me ménager bien peu :"

    elmire "Mais puisque la parole enfin en est lâchée,"

    elmire "À retenir Damis, me serais-je attachée ?"

    elmire "Aurais-je, je vous prie, avec tant de douceur,"

    elmire "Écouté tout au long l'offre de votre coeur ?"

    elmire "Aurais-je pris la chose ainsi qu'on m'a vu faire,"

    elmire "Si l'offre de ce coeur n'eût eu de quoi me plaire ?"

    elmire "Et lorsque j'ai voulu moi-même vous forcer"

    elmire "À soutenir l'hymen qu'on disait dénoncer,"

    elmire "Qu'est-ce que cette instance a dû vous faire entendre,"

    elmire "Que l'intérêt qu'en vous on s'avise de prendre,"

    elmire "Et l'ennui qu'on aurait que ce noeud qu'on dissout,"

    elmire "Vînt éloigner un coeur qu'on aime plus que tout."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "C'est sans doute, Madame, une douceur extrême,"

    tartuffe "Que d'entendre ces mots d'une bouche qu'on aime ;"

    tartuffe "Leur miel, dans tous mes sens, fait couler à longs traits"

    tartuffe "Une suavité qu'on ne goûta jamais."

    tartuffe "Le bonheur de vous plaire, est ma suprême étude,"

    tartuffe "Et mon coeur, de vos voeux, fait sa béatitude ;"

    tartuffe "Mais ce coeur vous demande ici la liberté,"

    tartuffe "D'oser douter un peu de sa félicité."

    tartuffe "Je puis croire ces mots un artifice honnête,"

    tartuffe "Pour m'obliger à faire une honnête retraite ;"

    tartuffe "Et s'il faut librement m'expliquer avec vous,"

    tartuffe "Je ne me fierai point à des propos si doux,"

    tartuffe "Qu'un peu de vos faveurs, après quoi je soupire,"

    tartuffe "Ne vienne m'assurer tout ce qu'ils m'ont pu dire,"

    tartuffe "Et planter dans mon âme une constante foi"

    tartuffe "Des charmantes bontés que vous avez pour moi."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    play sound1 female_cough

    hide elmire

    show elmire at left
    show orgon at right

    elmire "<{i}Elle tousse pour avertir son mari.{/i}>"

    hide orgon

    show elmire at truecenter

    stop sound1

    elmire "Quoi ! vous voulez aller avec cette vitesse,"

    elmire "Et d'un coeur, tout d'abord, épuiser la tendresse ?"

    elmire "On se tue à vous faire un aveu des plus doux,"

    elmire "Cependant ce n'est pas encore assez pour vous ;"

    elmire "Et l'on ne peut aller jusqu'à vous satisfaire,"

    elmire "Qu'aux dernières faveurs on ne pousse l'affaire ?"

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Moins on mérite un bien, moins on l'ose espérer ;"

    tartuffe "Nos voeux, sur des discours, ont peine à s'assurer ;"

    tartuffe "On soupçonne aisément un sort tout plein de gloire,"

    tartuffe "Et l'on veut en jouir, avant que de le croire."

    tartuffe "Pour moi, qui crois si peu mériter vos bontés,"

    tartuffe "Je doute du bonheur de mes témérités ;"

    tartuffe "Et je ne croirai rien, que vous n'ayez, Madame,"

    tartuffe "Par des réalités, su convaincre ma flamme."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Mon Dieu, que votre amour, en vrai Tyran agit !"

    elmire "Et qu'en un trouble étrange, il me jette l'esprit !"

    elmire "Que sur les coeurs, il prend un furieux empire !"

    elmire "Et qu'avec violence il veut ce qu'il désire !"

    elmire "Quoi ! de votre poursuite, on ne peut se parer,"

    elmire "Et vous ne donnez pas le temps de respirer ?"

    elmire "Sied-il bien de tenir une rigueur si grande ?"

    elmire "De vouloir sans quartier, les choses qu'on demande ?"

    elmire "Et d'abuser ainsi, par vos efforts pressants,"

    elmire "Du faible que pour vous, vous voyez qu'ont les Gens ?"

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Mais si d'un oeil {a=myshow|tooltip|text=Bénin : Qui ne se dit guère que des remèdes et des influences célestes. Un remède bénin, est celui qui purge doucement, sans de grandes évacuations, ni tranchées. Les cieux bénins, les astres bénins ont favorisés son voyage. Hors de là bénin ne se dit guère qu'en riant. Molière \[\[Ecole des Femmes, v. 296] dit en parlant des maris de Paris : \"Et les maris aussi les plus bénins du monde\". \[\[F]}bénin{/a} vous voyez mes hommages,"

    tartuffe "Pourquoi m'en refuser d'assurés témoignages ?"

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Mais comment consentir à ce que vous voulez,"

    elmire "Sans offenser le Ciel, dont toujours vous parlez ?"

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Si ce n'est que le Ciel qu'à mes voeux on oppose,"

    tartuffe "Lever un tel obstacle, est à moi peu de chose,"

    tartuffe "Et cela ne doit pas retenir votre coeur."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Mais des Arrêts du Ciel on nous fait tant de peur."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Je puis vous dissiper ces craintes ridicules,"

    tartuffe "Madame, et je sais l'art de lever les scrupules."

    tartuffe "Le Ciel défend, de vrai, certains contentements ;"

    tartuffe "Mais on trouve avec lui des accommodements."

    tartuffe "Selon divers besoins, il est une Science,"

    tartuffe "D'étendre les liens de notre conscience,"

    tartuffe "Et de rectifier le mal de l'action"

    tartuffe "Avec la pureté de notre intention."

    tartuffe "De ces secrets, Madame, on saura vous instruire ;"

    tartuffe "Vous n'avez seulement qu'à vous laisser conduire."

    tartuffe "Contentez mon désir, et n'ayez point d'effroi,"

    tartuffe "Je vous réponds de tout, et prends le mal sur moi."

    tartuffe "Vous toussez fort, Madame."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Oui, je suis au supplice."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Vous plaît-il un morceau de ce jus de Réglisse ?"

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "C'est un rhume obstiné, sans doute, et je vois bien"

    elmire "Que tous les jus du Monde, ici, ne feront rien."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Cela, certes, est fâcheux."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "{space=400}Oui, plus qu'on ne peut dire."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Enfin votre scrupule est facile à détruire,"

    tartuffe "Vous êtes assurée ici d'un plein secret,"

    tartuffe "Et le mal n'est jamais que dans l'éclat qu'on fait."

    tartuffe "{a=myshow|tooltip|text=Les vers 1051 et 1052 sont repris à l'identique dans \"La critique du Tartuffe\", de Villiers (1670) vers 433, 434.}Le scandale du monde, est ce qui fait l'offense {/a};"

    tartuffe "Et ce n'est pas pécher, que pécher en silence."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE, après avoir encore toussé."

    elmire "Enfin je vois qu'il faut se résoudre à céder,"

    elmire "Qu'il faut que je consente à vous tout accorder ;"

    elmire "Et qu'à moins de cela, je ne dois point prétendre"

    elmire "Qu'on puisse être content, et qu'on veuille se rendre."

    elmire "Sans doute, il est fâcheux d'en venir jusque-là,"

    elmire "Et c'est bien malgré moi, que je franchis cela :"

    elmire "Mais puisque l'on s'obstine à m'y vouloir réduire,"

    elmire "Puisqu'on ne veut point croire à tout ce qu'on peut dire,"

    elmire "Et qu'on veut des témoins qui soient plus convaincants,"

    elmire "Il faut bien s'y résoudre, et contenter les Gens."

    elmire "Si ce consentement porte en soi quelque offense,"

    elmire "Tant pis pour qui me force à cette violence ;"

    elmire "La faute assurément n'en doit pas être à moi."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Oui, Madame, on s'en charge, et la chose de soi..."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Ouvrez un peu la Porte, et voyez, je vous prie,"

    elmire "Si mon Mari n'est point dans cette Galerie."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Qu'est-il besoin pour lui, du soin que vous prenez ?"

    tartuffe "C'est un Homme, entre nous, à mener par le nez."

    tartuffe "De tous nos entretiens, il est pour faire gloire,"

    tartuffe "Et je l'ai mis au point de voir tout, sans rien croire."

    hide tartuffe

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Il n'importe, sortez, je vous prie, un moment,"

    elmire "Et partout, là dehors, voyez exactement."

    hide elmire

label Act_3_Scene_6:
    "{b}SCÈNE VI.{/b}"

    show orgon at left
    show elmire at right

    "<{i}Orgon, Elmire.{/i}>"

    hide orgon
    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON, sortant de dessous la Table."

    play sound1 footsteps

    orgon "Voilà, je vous l'avoue, un abominable Homme !"

    stop sound1

    orgon "Je n'en puis revenir, et tout ceci m'assomme."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Quoi ! vous sortez sitôt ? Vous vous moquez des Gens."

    elmire "Rentrez sous le Tapis, il n'est pas encor temps ;"

    elmire "Attendez jusqu'au bout, pour voir les choses sûres,"

    elmire "Et ne vous fiez point aux simples conjectures."

    hide elmire

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Non, rien de plus méchant n'est sorti de l'Enfer."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE."

    elmire "Mon Dieu, l'on ne doit point croire trop de léger ;"

    elmire "Laissez-vous bien convaincre, avant de vous rendre,"

    elmire "Et ne vous hâtez point, de peur de vous méprendre."

    hide elmire

    show elmire at left
    show orgon at right

    elmire "<{i}Elle fait mettre son Mari derrière elle.{/i}>"

    hide orgon

    show elmire at truecenter

    hide elmire

label Act_3_Scene_7:
    "{b}SCÈNE VII.{/b}"

    show tartuffe at left
    show elmire at truecenter
    show orgon at right

    "<{i}Tartuffe, Elmire, Orgon.{/i}>"

    hide tartuffe
    hide elmire
    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Tout conspire, Madame, à mon contentement :"

    tartuffe "J'ai visité, de l'oeil, tout cet appartement,"

    tartuffe "Personne ne s'y trouve, et mon âme ravie..."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON, en l'arrêtant."

    orgon "Tout doux, vous suivez trop votre amoureuse envie,"

    orgon "Et vous ne devez pas vous tant passionner."

    orgon "Ah, ah, l'Homme de bien, vous m'en voulez donner !"

    orgon "Comme aux tentations s'abandonne votre âme !"

    orgon "Vous écartiez mon fils, et convoitiez ma femme !"

    orgon "J'ai douté fort longtemps, que ce fût tout de bon,"

    orgon "Et je croyais toujours qu'on changerait de ton :"

    orgon "Mais c'est assez avant pousser le témoignage,"

    orgon "Je m'y tiens, et n'en veux pour moi pas davantage."

    hide orgon

    show elmire at truecenter

    $ elmire_var = "{noalt}ELMIRE, à Tartuffe."

    hide elmire

    show elmire at left
    show tartuffe at right

    elmire "C'est contre mon humeur, que j'ai fait tout ceci ;"

    hide tartuffe

    show elmire at truecenter

    elmire "Mais on m'a mise au point de vous traiter ainsi."

    hide elmire

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Quoi ! vous croyez..."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Allons, point de bruit, je vous prie ;"

    orgon "Dénichons de céans, et sans cérémonie."

    hide orgon

    show tartuffe at truecenter

    $ tartuffe_var = "{noalt}TARTUFFE."

    tartuffe "Mon dessein..."

    hide tartuffe

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "{space=400}Ces discours ne sont plus de saison,"

    orgon "Il faut, tout sur le champ, sortir de la Maison."

    hide orgon

label Act_3_Scene_8:
    "{b}SCÈNE VIII.{/b}"

    show orgon at left
    show damis at truecenter
    show cleante at right

    "<{i}Tartuffe, Elmire, Orgon, Damis, Cléante.{/i}>"

    hide tartuffe
    hide elmire
    hide orgon
    hide damis
    hide cleante

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Eh bien, vous le voyez, vous frôliez la disgrâce,"

    damis "Il n'est point de bienfait qu'en son âme il n'efface ;"

    damis "Et son trop lâche orgueil, trop digne de courroux,"

    damis "Faisait de vos bontés des armes contre vous !"

    hide damis

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Oui, mon Fils, et j'en sens des douleurs nonpareilles."

    hide orgon

    show damis at truecenter

    $ damis_var = "{noalt}DAMIS."

    damis "Laissez-moi, je lui veux couper les deux oreilles."

    damis "Contre son insolence, on ne doit point gauchir."

    damis "C'est à moi, tout d'un coup, de vous en affranchir ;"

    damis "Et pour sortir d'affaire, il faut que je l'assomme."

    hide damis

    show cleante at truecenter

    $ cleante_var = "{noalt}CLÉANTE."

    cleante "Voilà, tout justement, parler en vrai jeune Homme."

    cleante "Modérez, s'il vous plaît, ces transports éclatants ;"

    cleante "Nous vivons sous un règne, et sommes dans un temps,"

    cleante "Où par la violence, on fait mal ses affaires."

    play sound1 footsteps

    hide cleante

    show cleante at left
    show tartuffe at right

    cleante "<{i}\[Sortie de Tartuffe]{/i}>"

    hide tartuffe

    show cleante at truecenter

    stop sound1

    hide cleante

label Act_3_Scene_9:
    "{b}SCÈNE IX ET DERNIÈRE.{/b}"

    show orgon at left
    show cleante at truecenter
    show dorine at right

    "<{i}Madame Pernelle, Elmire, Damis, Orgon, Cléante, Dorine.{/i}>"

    hide madame_pernelle
    hide elmire
    hide damis
    hide orgon
    hide cleante
    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Qu'est-ce ? J'apprends ici de terribles mystères."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Ce sont des nouveautés dont mes yeux sont témoins,"

    orgon "Et vous voyez le prix dont sont payés mes soins."

    orgon "Je recueille, avec zèle, un Homme en sa misère,"

    orgon "Je le loge, et le tiens comme mon propre Frère ;"

    orgon "De bienfaits, chaque jour, il est par moi chargé,"

    orgon "Je lui livre mon âme, et tout le bien que j'ai ;"

    orgon "Et dans le même temps, le Perfide, l'Infâme,"

    orgon "Tente le noir dessein de suborner ma Femme ;"

    orgon "Et non content encor de ces lâches essais,"

    orgon "Il tente d'abuser de mes propres bienfaits,"

    orgon "Et veut, sur ma famille, user des avantages"

    orgon "Dont le viennent d'armer mes bontés trop peu sages ;"

    orgon "Priver Damis des biens où je l'ai transféré,"

    orgon "Et le réduire au point d'où je l'ai retiré."

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Le pauvre Homme !"

    hide dorine

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Mon fils, je ne puis du tout croire"

    madame_pernelle "Qu'il ait voulu commettre une action si noire."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Comment ?"

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Les Gens de bien sont enviés toujours."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Que voulez-vous donc dire avec votre discours,"

    orgon "Ma Mère ?"

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Que chez vous on vit d'étrange sorte,"

    madame_pernelle "Et qu'on ne sait que trop la haine qu'on lui porte."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Qu'a cette haine à faire avec ce qu'on vous dit ?"

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Je vous l'ai dit cent fois, quand vous étiez petit."

    madame_pernelle "La Vertu, dans le Monde, est toujours poursuivie ;"

    madame_pernelle "Les Envieux mourront, mais non jamais l'Envie."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Mais que fait ce discours aux choses d'aujourd'hui ?"

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "On vous aura forgé cent sots contes de lui."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Je vous ai dit déjà, que j'ai vu tout moi-même."

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Des Esprits médisants, la malice est extrême."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Vous me feriez damner, ma Mère. Je vous dis,"

    orgon "Que j'ai vu de mes yeux, un crime si hardi."

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Les langues ont toujours du venin à répandre ;"

    madame_pernelle "Et rien n'est, ici-bas, qui s'en puisse défendre."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "C'est tenir un propos de sens bien dépourvu !"

    orgon "Je l'ai vu, dis-je, vu, de mes propres yeux vu,"

    orgon "Ce qu'on appelle vu : Faut-il vous le rebattre"

    orgon "Aux oreilles cent fois, et crier comme quatre ?"

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Mon Dieu, le plus souvent, l'apparence déçoit."

    madame_pernelle "Il ne faut pas toujours juger sur ce qu'on voit."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "J'enrage."

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Aux faux soupçons la Nature est sujette ;"

    madame_pernelle "Et c'est souvent à mal que le bien s'interprète."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Je dois interpréter à charitable soin,"

    orgon "Le désir d'embrasser ma Femme ?"

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "{space=400}Il est besoin,"

    madame_pernelle "Pour accuser les gens, d'avoir de justes causes,"

    madame_pernelle "Et vous deviez attendre à vous voir sûr des choses."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Hé, diantre, le moyen de m'en assurer mieux ?"

    orgon "Je devais donc, ma Mère, attendre qu'à mes yeux"

    orgon "Il eût... vous me feriez dire quelque sottise."

    hide orgon

    show madame_pernelle at truecenter

    $ madame_pernelle_var = "{noalt}MADAME PERNELLE."

    madame_pernelle "Enfin d'un trop pur zèle on voit son âme éprise,"

    madame_pernelle "Et je ne puis du tout me mettre dans l'esprit,"

    madame_pernelle "Qu'il ait voulu tenter les choses que l'on dit."

    hide madame_pernelle

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Allez. Je ne sais pas, si vous n'étiez ma Mère,"

    orgon "Ce que je vous dirais, tant je suis en colère."

    hide orgon

    show dorine at truecenter

    $ dorine_var = "{noalt}DORINE."

    dorine "Juste retour, Monsieur, des choses d'ici-bas."

    dorine "Vous ne vouliez point croire, et l'on ne vous croit pas."

    hide dorine

    show orgon at truecenter

    $ orgon_var = "{noalt}ORGON."

    orgon "Vous mettez votre nez où vous n'avez que faire."

    orgon "Laissons au Ciel le soin de détromper ma mère,"

    orgon "Puis par un doux hymen couronnons en Damis"

    orgon "La constance et l'ardeur d'un coeur vraiment épris."

    hide orgon


