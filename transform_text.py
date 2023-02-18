import random
import re
import shutil
import tempfile
import warnings
from copy import copy
from pathlib import Path
from typing import *

from lxml import etree, objectify
from pymystem3 import Mystem

warnings.filterwarnings("ignore")

PLAY_NAME = "test"
MAIN_DIRECTORY = f"{PLAY_NAME}/game"
PATH_TO_INPUT_FILE: str = "texts/mayakovsky-misteriya-buff.xml"
PATH_TO_OUTPUT_FILE: str = f"{MAIN_DIRECTORY}/script.rpy"

PATH_TO_IMAGES_DIRECTORY: str = f"{MAIN_DIRECTORY}/images"
PATH_TO_PICTURES_DIRECTORY: str = "pictures"

PATH_TO_CHARACTERS_DIRECTORY: str = f"{PATH_TO_IMAGES_DIRECTORY}/characters"
PATH_TO_CHARACTERS_PICTURES: str = f"{PATH_TO_PICTURES_DIRECTORY}/characters"

PATH_TO_BACKGROUNDS_DIRECTORY: str = f"{PATH_TO_IMAGES_DIRECTORY}/bg"
PATH_TO_BACKGROUNDS_PICTURES: str = f"{PATH_TO_PICTURES_DIRECTORY}/background"

PATH_TO_GUI_DIRECTORY: str = f"{MAIN_DIRECTORY}/gui"
PATH_TO_GUI_FILES: str = f"gui"


PATH_TO_AUDIO_DIRECTORY: str = f"{MAIN_DIRECTORY}/audio"
PATH_TO_MUSIC_DIRECTORY: str = f"{PATH_TO_AUDIO_DIRECTORY}/music"
PATH_TO_SOUNDS_DIRECTORY: str = f"{PATH_TO_AUDIO_DIRECTORY}/sounds"
PATH_TO_MUSIC_AUDIO: str = f"audio/music"
PATH_TO_SOUNDS_AUDIO: str = f"audio/sounds"

XML_SCHEME: str = "{http://www.w3.org/XML/1998/namespace}"

# CHARACTERS dicts
CHARACTER_NAME_TO_CODE: OrderedDict[str, str] = OrderedDict()
CHARACTER_CODE_TO_NAME: OrderedDict[str, str] = OrderedDict()
CHARACTER_CODE_TO_SEX: Dict[str, str] = {}
SEX_TO_CHARACTER_CODE: Dict[str, List[str]] = {}
CHARACTER_CODE_TO_ROLE_DESC: OrderedDict[str, str] = OrderedDict()

# MENU labels
CHARACTERS: str = "Characters"
CHARACTERS_NAME: str = ''  # name of the `CHARACTERS` label
NUM_OF_CHARACTERS: int = 0  # number of castLists
ACT: str = "Act"
SCENE: str = "Scene"
SUB_SCENE: str = "Subscene"
FURTHER: str = "Further"

# ACTS lists
ACT_CODES: List[str] = []
ACT_NAMES: List[str] = []

# SCENES lists
SCENE_CODES: List[str] = []
SCENE_NAMES: List[str] = []

# SUB_SCENES lists
SUB_SCENE_CODES: List[str] = []
SUB_SCENE_NAMES: List[str] = []

# COLORS
KELLY_COLORS_HEX: List[str] = [
    "#FFB300",  # Vivid Yellow
    "#803E75",  # Strong Purple
    "#FF6800",  # Vivid Orange
    "#A6BDD7",  # Very Light Blue
    "#C10020",  # Vivid Red
    "#CEA262",  # Grayish Yellow
    "#817066",  # Medium Gray

    # The following don't work well for people with defective color vision
    "#007D34",  # Vivid Green
    "#F6768E",  # Strong Purplish Pink
    "#00538A",  # Strong Blue
    "#FF7A5C",  # Strong Yellowish Pink
    "#53377A",  # Strong Violet
    "#FF8E00",  # Vivid Orange Yellow
    "#B32851",  # Strong Purplish Red
    "#F4C800",  # Vivid Greenish Yellow
    "#7F180D",  # Strong Reddish Brown
    "#93AA00",  # Vivid Yellowish Green
    "#593315",  # Deep Yellowish Brown
    "#F13A13",  # Vivid Reddish Orange
    "#232C16",  # Dark Olive Green
]
KELLY_COLORS_HEX_INDEX: int = 0

# max number of options on a screen
MAX_NUM_OF_VALUES_IN_LIST: int = 6

BACKGROUNDS_TAKEN: Set[int] = set()
MUSIC_TAKEN: Set[int] = set()

PREV_CHARACTER: Optional[str] = None

BLACK_COLOR = "#000"

IDENTIFIER = None

CHARACTERS_TEXT: str = ""
FRONT_TEXTS: List[str] = []
ACTS_TEXT: str = ""
STAND_OFF: str = ""

TAB: str = "    "

mystem = Mystem()

# random
random.seed(123)


def get_random_colour():
    global KELLY_COLORS_HEX_INDEX

    if KELLY_COLORS_HEX_INDEX < len(KELLY_COLORS_HEX):
        result = KELLY_COLORS_HEX[KELLY_COLORS_HEX_INDEX]
        KELLY_COLORS_HEX_INDEX += 1
        return result

    return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])


def create_character_variables_with_given_sex(character_elems, sex: str) -> str:
    s: str = ""

    characters = []

    for character_elem in character_elems:
        sex_attrib: str = character_elem.attrib['sex']

        pers_code: str = character_elem.get(f"{XML_SCHEME}id").replace('-', '_').lower()

        main_name: Optional[str] = None
        for elem in character_elem:
            if elem.tag in ["persName", "name"]:
                name = get_text(elem)
                CHARACTER_NAME_TO_CODE[name] = pers_code
                for property in ["фам", "имя", "отч"]:
                    for key in get_lexemes(name, properties=[property], return_text=True):
                        key = key.lower()
                        if key not in CHARACTER_NAME_TO_CODE:
                            CHARACTER_NAME_TO_CODE[key] = pers_code
                # if not name.endswith("а"):
                #     # adding "а" in case of an error in morphological analysis
                #     CHARACTER_NAME_TO_CODE[name + "а"] = pers_code
                if main_name is None:
                    main_name = name
                    CHARACTER_CODE_TO_NAME[pers_code] = main_name

        if sex_attrib == sex:
            CHARACTER_CODE_TO_SEX[pers_code] = sex_attrib

            if sex_attrib not in SEX_TO_CHARACTER_CODE:
                SEX_TO_CHARACTER_CODE[sex_attrib] = []
            SEX_TO_CHARACTER_CODE[sex_attrib].append(pers_code)

            colour: str = get_random_colour()
            s += f'define {pers_code} = Character("{pers_code}_var", color="{colour}", dynamic=True)\n'

            characters.append(pers_code)

    num_of_pictures = len(list(Path(f'{PATH_TO_CHARACTERS_PICTURES}/{sex.lower()}').glob('*')))

    assert len(characters) <= num_of_pictures, \
        f'actual: {len(characters)}, current: {num_of_pictures}'

    numbers = random.sample(range(1, num_of_pictures), len(characters))

    Path(PATH_TO_CHARACTERS_DIRECTORY).mkdir(exist_ok=True)

    for i, sex_character in enumerate(characters):
        shutil.copy(
            Path(f'{PATH_TO_CHARACTERS_PICTURES}/{sex.lower()}/{numbers[i]}.png'),
            Path(f'{PATH_TO_CHARACTERS_DIRECTORY}/{sex_character}.png')
        )

    return s


def create_character_variables(character_elems) -> str:
    s: str = ""

    for sex in ["MALE", "FEMALE", "UNKNOWN"]:
        s += create_character_variables_with_given_sex(character_elems, sex)

    return s


def get_root_menu(indent: str = ""):
    s = ""

    s += f"{indent}menu:\n"

    indent += TAB

    if CHARACTERS_NAME:
        s += f'{indent}"{{color={BLACK_COLOR}}}{CHARACTERS_NAME}{{/color}}":\n'
        s += f'    {indent}jump {CHARACTERS}_1\n'

    num_of_pages: int = (len(ACT_CODES) - 1) // MAX_NUM_OF_VALUES_IN_LIST + 1
    for i in range(num_of_pages):
        for act_num, act_code in \
                enumerate(ACT_CODES[MAX_NUM_OF_VALUES_IN_LIST * i:MAX_NUM_OF_VALUES_IN_LIST * (i + 1)]):
            s += f'{indent}"{{color={BLACK_COLOR}}}{ACT_NAMES[MAX_NUM_OF_VALUES_IN_LIST * i + act_num]}{{/color}}":\n'
            s += f'    {indent}jump {act_code}\n'
        if i < num_of_pages - 1:
            further_code = f'{FURTHER}_{ACT}_{i + 1}'
            s += f'{indent}"{{color={BLACK_COLOR}}}>{{/color}}":\n'
            s += f'    {indent}jump {further_code}\n\n'
            indent = indent[8:]
            s += f'{indent}label {further_code}:\n'
            indent += TAB
            s += f"{indent}menu:\n"
            indent += TAB

    return s


def play_music(tag, indent: str = "", attrib_name: str = "music", get_random=False) -> str:
    s: str = ''

    # music
    if tag is not None and attrib_name in tag.attrib:
        names = [f"audio/music/{name}.mp3" for name in tag.attrib[attrib_name].split()]
        s += f'{indent}play music {names} fadeout 1.0 fadein 1.0\n\n'
    elif get_random:
        Path(PATH_TO_MUSIC_DIRECTORY).mkdir(exist_ok=True)

        num_of_songs: int = len(list(Path(PATH_TO_MUSIC_AUDIO).glob('*')))

        num: int = random.randint(1, num_of_songs)

        while num in MUSIC_TAKEN:
            num = random.randint(1, num_of_songs)

        MUSIC_TAKEN.add(num)

        shutil.copy(
            Path(f'{PATH_TO_MUSIC_AUDIO}/{num}.mp3'),
            Path(f'{PATH_TO_MUSIC_DIRECTORY}/{num}.mp3')
        )

        s += f'{indent}play music "audio/music/{num}.mp3" fadeout 1.0 fadein 1.0\n\n'

    return s


def get_text_parts(elem, text: str) -> List[str]:
    parts = re.split(r"(?<=[.;!?])\s+", text)

    text_parts: List[str] = []
    curr_parts: List[str] = []
    curr_length: int = 0
    for part in parts:
        inner_parts = [part]
        if len(part) >= 260:
            inner_parts = re.split(r'(?<=[,»"])\s+', part)

        for inner_part in inner_parts:
            if curr_length + len(inner_part) >= 260:
                text_parts.append(' '.join(curr_parts))
                curr_parts = []
                curr_length = 0
            curr_parts.append(inner_part)
            curr_length += len(inner_part)
    if curr_parts:
        text_parts.append(' '.join(curr_parts))

    return text_parts


def text_splitter(func):
    def inner_func(*args, **kwargs):
        item = args[0]

        s: str = ''

        text = re.sub(r"\s+", " ", item.text)

        text_parts: List[str] = get_text_parts(item, text)

        for text_part in text_parts:
            inner_elem = copy(item)
            inner_elem.text = text_part
            s += func(inner_elem, *args[1:], **kwargs)

        item.text = text

        # for parse_cast_item method
        global IDENTIFIER
        IDENTIFIER = None

        return s

    return inner_func


@text_splitter
def parse_cast_item(elem, indent: str = "", notes: List = None) -> str:
    if notes is None:
        notes = []

    was_role: bool = False
    for _ in elem:
        was_role = True

    if was_role:
        elem = elem[0]

    s: str = ''

    text: str = get_text(elem)

    text = add_notes_to_text(text, notes=notes)

    enrich_elem(elem)
    characters = elem.attrib.get("characters").split()
    identifier: str = characters[0] if characters else None
    if "id" in elem.attrib:
        identifier = elem.attrib["id"].lower()

    global IDENTIFIER
    if identifier is None:
        identifier = IDENTIFIER
    IDENTIFIER = identifier

    role_desc: str = text
    if ',' in text:
        role_desc = ' '.join(text.split(",")[1:]).strip()

    for elem in [' of ', ' de ', " d'"]:
        if elem in role_desc:
            elem_index = role_desc.index(elem)
            role_desc = role_desc[:elem_index]

    CHARACTER_CODE_TO_ROLE_DESC[identifier] = role_desc

    if identifier is not None:
        s += f'{indent}show {identifier} at truecenter\n'  # with dissolve

    s += f'{indent}"{text}"\n'

    if identifier is not None:
        s += f'{indent}hide {identifier}\n'  # with dissolve

    s += "\n"

    return s


def before_characters(elem, characters: List[str], indent: str = "") -> str:
    s: str = ''

    if "characters" in elem.attrib:
        # add character for one speech or one stage
        s += hide_characters(characters, indent)

        new_characters = elem.attrib["characters"].split()
        prev_characters = characters[:]

        characters.clear()
        characters.extend(value for value in prev_characters if value not in new_characters)

        s += show_stage_characters(characters + new_characters, indent)

    return s


def after_characters(elem, characters: List[str], indent: str = "") -> str:
    s: str = ''

    if "characters" in elem.attrib:
        # add character for one speech or one stage
        s += hide_characters(elem.attrib["characters"].split(), indent)

        s += show_stage_characters(characters, indent)

    return s


def enrich_stage(stage, main_character: str):
    stage_types = stage.attrib["type"].split("/") if "type" in stage.attrib else []
    stage_text = stage.text.lower().strip()

    lexemes_dict = get_lexemes(stage_text)
    lexemes = [key for key in lexemes_dict.keys()]

    sounds = []

    prefix = 'male' if CHARACTER_CODE_TO_SEX.get(main_character) == 'MALE' else 'female'
    if any(stage_type in stage_types for stage_type in ['slap']) or \
            any(word in lexemes for word in ['soufflet']):
        sounds.append('slap')
    # if any(stage_type in stage_types for stage_type in ['exit']) or \
    #         any(word in lexemes
    #             for word in ["aller", "sortie", "sortir", "отправляться", "разбредаться", "возвращаться",
    #                          "скрываться", "идти", "расхаживать", "водить"]) or \
    #         any(any(lexeme.endswith(word) for lexeme in lexemes) for word in ["ходить", "бегать"]) or \
    #         any(lexemes[i:i + 2] in [["к", "дверь"], ["от", "дверь"]] for i in range(len(lexemes) - 1)):
    #     sounds.append('footsteps')
    if any(stage_type in stage_types for stage_type in ['furniture']) or \
            any(word in lexemes for word in ["chaise"]):
        sounds.append('chair')
    if any(stage_type in stage_types for stage_type in ['run']) or \
            any(word in lexemes for word in ["courir", "бежать", "бегать"]):
        sounds.append('running')
    if any(stage_type in stage_types for stage_type in ['cry']) or \
            any(word in lexemes for word in ["larme", "слеза", "плач"]) or \
            any(any(lexeme.endswith(word) for lexeme in lexemes) for word in ["плакать", "рыдать"]):
        sounds.append(f'{prefix}_cry')
    if any(word in lexemes for word in ["вздох", "вздыхать"]):
        sounds.append(f'{prefix}_sigh')
    if any(word in lexemes for word in ["уезжать"]):
        sounds.append('horse_run')
    if any(word in lexemes for word in ["хохотать", "хохот", "смех", "смеяться"]):
        sounds.append(f'{prefix}_laughter')
    if any(stage_type in stage_types for stage_type in ['cough']) or \
            any(word in lexemes for word in ["tousser", "покашливать", "кашлять"]):
        sounds.append(f'{prefix}_cough')
    if any(word in lexemes for word in ['фортопиять', 'фортопияно', 'фортепияно', 'пианино']):
        sounds.append('piano')
    if any(word in lexemes for word in ['флейта']):
        sounds.append('flute')
    if any(word in lexemes for word in ['целовать', 'целоваться']):
        sounds.append('kiss')
    if any(word in lexemes for word in ['лобызание']):
        sounds.append('kisses')
    if any(word in lexemes for word in ['стучаться', "стучать", "стук"]):
        sounds.append('knocking')
    if any(lexemes[i:i + 2] in [["часы", "бить"], ["бить", "часы"], ["часовой", "музыка"], ["часы", "ударять"],
                                ["часы", "ударить"]]
           for i in range(len(lexemes) - 1)):
        sounds.append('clock')
    if "зажимать" in lexemes and "рот" in lexemes and lexemes.index("зажимать") < lexemes.index("рот"):
        sounds.append(f'{prefix}_gag')
    if any(word in lexemes for word in ['цыпочки']):
        sounds.append('tiptoes')
    if any(lexemes[i:i + 2] in [["тушить", "свеча"]] for i in range(len(lexemes) - 1)):
        sounds.append(f'{prefix}_blow_candle')
    if any(word in lexemes for word in ['сталкиваться', "выталкивать", "хлопнуть", "бросить", "падать"]):
        sounds.append('punch')

    for verb in ["затворять", "закрывать", "прикрывать", "отпирать"]:
        if verb in lexemes and "дверь" in lexemes and lexemes.index(verb) < lexemes.index("дверь"):
            sounds.append('door_creak')
            break

    if any(word in lexemes for word in ['звонок', 'звонить']):
        sounds.append('telephone')
    if any(word in lexemes for word in ['свистеть', 'насвистывать', 'свистнуть', 'свист']):
        sounds.append('whistle')

    for sound in sounds:
        Path(PATH_TO_SOUNDS_DIRECTORY).mkdir(exist_ok=True)

        shutil.copy(
            Path(f'{PATH_TO_SOUNDS_AUDIO}/{sound}.mp3'),
            Path(f'{PATH_TO_SOUNDS_DIRECTORY}/{sound}.mp3')
        )

    if sounds:
        stage.set("sound", " ".join(sounds))


def play_sound(elem, indent: str = "") -> str:
    s: str = ''

    if "sound" in elem.attrib:
        for i, sound in enumerate(elem.attrib["sound"].split(), start=1):
            s += f'{indent}play sound{i} {sound}\n'
        s += "\n"

    return s


def stop_sound(elem, indent: str = "") -> str:
    s: str = ''

    if "sound" in elem.attrib:
        for i, sound in enumerate(elem.attrib["sound"].split(), start=1):
            s += f'{indent}stop sound{i}\n'
        s += '\n'

    return s


@text_splitter
def add_stage(elem, characters: List[str], indent: str, notes: List) -> str:
    enrich_elem(elem, characters[0] if characters else None)

    s: str = ""

    s += show_background(elem, indent)

    s += play_sound(elem, indent)

    s += before_characters(elem, characters, indent)

    s += add_line(elem, characters, indent, notes)

    s += after_characters(elem, characters, indent)

    s += stop_sound(elem, indent)

    return s


def add_notes_to_text(text: str, notes: List) -> str:
    if notes is None:
        notes = []

    for note in notes:
        key_text = ''
        value_text = ''
        for elem in note:
            if elem.tag == "key":
                key_text = get_text(elem)
            elif elem.tag == "value":
                value_text = get_text(elem)

        value_text = value_text.replace('{i}', '').replace('{/i}', '')

        text = text.replace(
            key_text,
            f'{{a=myshow|tooltip|text={value_text}}}{key_text}{{/a}}'
        )

    return text


@text_splitter
def add_line(line, characters: List[str], indent: str = "", notes: List = None) -> str:
    if notes is None:
        notes = []

    s: str = ""

    text: str = line.text.replace('"', '\\"').replace("[", "[[").strip()

    if not text.strip():
        return s

    s += play_sound(line, indent)

    s += before_characters(line, characters, indent)

    additional_spaces = ''
    if "part" in line.attrib:
        if line.attrib["part"] == 'M':
            additional_spaces = '{space=200}'
        elif line.attrib["part"] == 'F':
            additional_spaces = '{space=400}'
    if "rend" in line.attrib:
        if line.attrib["rend"] == 'indent':
            additional_spaces = '{space=400}'

    text = add_notes_to_text(text, notes)

    if is_stage(line):
        text = f'<{{i}}{text}{{/i}}>'
    elif line.tag == 'head':
        text = f'{{b}}{text}{{/b}}'

    s += f'{indent}{characters[0] + " " if characters else ""}"{additional_spaces}{text}"\n\n'

    s += after_characters(line, characters, indent)

    s += stop_sound(line, indent)

    return s


def show_stage_characters(characters: List[str], indent: str = "") -> str:
    s: str = ''

    if len(characters) >= 3:
        new_characters = characters[-3:]
        characters.clear()
        characters.extend(new_characters)
        s += f'{indent}show {characters[0]} at left\n'
        s += f'{indent}show {characters[1]} at truecenter\n'
        s += f'{indent}show {characters[2]} at right\n\n'
    elif len(characters) == 2:
        s += f'{indent}show {characters[0]} at left\n'
        s += f'{indent}show {characters[1]} at right\n\n'
    elif len(characters) == 1:
        s += f'{indent}show {characters[0]} at truecenter\n\n'

    return s


def hide_characters(characters: List[str], indent: str = "") -> str:
    s: str = ''

    for character in characters:
        s += f'{indent}hide {character}\n'

    if s:
        s += '\n'

    return s


def get_sp(sp_elem, characters: List[str], indent: str = ""):
    s: str = ""

    for speaker in sp_elem.get("who").split():
        characters.append(speaker[1:].replace('-', '_').lower())

    s += show_stage_characters(characters, indent)

    if sp_elem.find('./speaker') is None:
        s += f'{indent}$ {characters[0]}_var = "{{noalt}}{CHARACTER_CODE_TO_NAME[characters[0]]}"\n\n'

    notes = []
    for outer_elem in sp_elem:
        s += parse_any(outer_elem, characters, indent, notes)

    s += hide_characters(characters, indent)

    return s


def get_text(elem) -> str:
    return re.sub(r"\s+", " ", "".join(elem.itertext())) \
        .replace("[", "[[") \
        .replace('"', '\\"').strip()


def show_background(tag, indent: str = "", get_random: bool = False) -> str:
    s: str = ''

    # background
    if tag is not None and "background" in tag.attrib:
        s += f'{indent}scene {tag.attrib["background"]} with fade\n\n'
    elif get_random:
        Path(PATH_TO_BACKGROUNDS_DIRECTORY).mkdir(exist_ok=True)

        num_of_background_pictures: int = len(list(Path(PATH_TO_BACKGROUNDS_PICTURES).glob('*')))

        num: int = random.randint(1, num_of_background_pictures)

        while num in BACKGROUNDS_TAKEN:
            num = random.randint(1, num_of_background_pictures)

        BACKGROUNDS_TAKEN.add(num)

        shutil.copy(
            Path(f'{PATH_TO_BACKGROUNDS_PICTURES}/{num}.jpeg'),
            Path(f'{PATH_TO_BACKGROUNDS_DIRECTORY}/{num}.jpeg')
        )

        s += f'{indent}scene {num} with fade\n\n'

    return s


def get_lexemes(text: str, parts_of_speech: List[str] = None, add_text: bool = False, properties: List[str] = None,
                return_text: bool = False) -> OrderedDict[str, str]:
    if properties is None:
        properties = []
    text_analysis = mystem.analyze(text)

    lexemes = OrderedDict()
    for text_analysis_elem in text_analysis:
        if "analysis" in text_analysis_elem and text_analysis_elem["analysis"]:
            analysis = text_analysis_elem["analysis"][0]
            source_text = text_analysis_elem["text"]
            text_elem = source_text.lower()
            if " " in text_elem:
                continue

            grammar = re.split("[^a-zA-Zа-яА-ЯёЁ]", analysis['gr'])

            was_break: bool = False
            for property_ in properties:
                if ',' in property_:
                    if property_ not in analysis['gr']:
                        was_break = True
                        break
                elif property_.lower() not in grammar:
                    was_break = True
                    break

            if was_break:
                continue

            if parts_of_speech is not None and grammar[0] not in parts_of_speech:
                continue

            if add_text:
                lexemes[text_elem] = source_text

            lexeme: str = source_text if return_text else analysis['lex']
            lexemes[lexeme] = source_text
            # if lexeme.endswith("а"):
            #     lexemes[lexeme[:-1]] = source_text

    return lexemes


def character_name_to_lexemes(text: str) -> List[str]:
    return [elem for elem in re.split("[^a-zA-zа-яА-ЯёЁ0-9]+", text) if elem]  #


def search_for_characters(elem, items, characters, main_character, lexemes, text, used_lexemes_indices,
                          character_code_to_index, index_to_character_code, index_to_character_name):
    split_text_lexemes = character_name_to_lexemes(text)

    for text_lexemes in [split_text_lexemes, lexemes]:
        for character_name, character_code in items:
            if character_code == main_character:
                continue

            character_name_lexemes = character_name_to_lexemes(character_name)

            for i in range(0, len(text_lexemes) - len(character_name_lexemes) + 1):
                if character_name_lexemes and \
                        [value.lower() for value in text_lexemes[i: i + len(character_name_lexemes)]] == \
                        [value.lower() for value in character_name_lexemes]:

                    # # name should start with a capital letter unless elem.tag is "castItem"
                    # if elem.tag != "castItem" and text_lexemes[i][0].isalpha() and \
                    #         text_lexemes[i][0] == text_lexemes[i][0].lower():
                    #     continue

                    index: int = i
                    if index in used_lexemes_indices and \
                            len(character_name_to_lexemes(index_to_character_name[index])) >= len(character_name_lexemes):
                        continue
                    new_indices = {i for i in range(index, index + len(character_name_lexemes))}
                    intersection = used_lexemes_indices & new_indices

                    if intersection:
                        for elem_index in intersection & index_to_character_code.keys():
                            key_to_remove = index_to_character_code[elem_index]
                            characters.remove(key_to_remove)
                            used_lexemes_indices.remove(character_code_to_index[key_to_remove])
                            del character_code_to_index[key_to_remove]
                            del index_to_character_code[elem_index]
                            del index_to_character_name[elem_index]

                    if character_code in characters:
                        continue

                    used_lexemes_indices.add(index)
                    character_code_to_index[character_code] = index
                    index_to_character_code[index] = character_code
                    index_to_character_name[index] = character_name
                    characters.append(character_code)

                    break


def enrich_elem(elem, main_character: str = None):
    text: str = elem.text.strip()
    lexemes_dict = get_lexemes(text)  # , parts_of_speech=["S", "A", "ANUM"], add_text=True
    lexemes = [key for key in lexemes_dict.keys()]

    character_code_to_index = {}
    index_to_character_code = {}
    index_to_character_name = {}
    characters = []

    used_lexemes_indices = set()
    search_for_characters(elem, CHARACTER_NAME_TO_CODE.items(), characters, main_character, lexemes, text,
                          used_lexemes_indices, character_code_to_index, index_to_character_code,
                          index_to_character_name)

    # for character_code, role_desc in CHARACTER_CODE_TO_ROLE_DESC.items():
    #     if character_code in characters or character_code == main_character or character_code is None:
    #         continue
    #
    #     role_desc_lexemes_dict = get_lexemes(role_desc, parts_of_speech=["S"], properties=["им,ед"])
    #     for lower_role_desc in role_desc_lexemes_dict:
    #         if lower_role_desc in lexemes:
    #             index: int = text.index(lexemes_dict[lower_role_desc])
    #             if index in used_lexemes_indices:
    #                 continue
    #             used_lexemes_indices.add(index)
    #             character_code_to_index[character_code] = index
    #             characters.append(character_code)
    #             break

    # global PREV_CHARACTER
    # if PREV_CHARACTER is not None and PREV_CHARACTER not in characters and PREV_CHARACTER != main_character:
    #     pronoun_lexemes_dict = get_lexemes(
    #         text, parts_of_speech=["SPRO", "APRO"],  # if you will add "APRO" then there would be a lot of noise
    #         properties=["муж" if CHARACTER_CODE_TO_SEX.get(PREV_CHARACTER) == 'MALE' else "жен"],
    #         return_text=True
    #     )
    #
    #     if pronoun_lexemes_dict:
    #         character_code_to_index[PREV_CHARACTER] = text.index(next(iter(pronoun_lexemes_dict)))
    #         characters.append(PREV_CHARACTER)

    # if not characters and main_character is None and 'UNKNOWN' in SEX_TO_CHARACTER_CODE:
    #     # weren't able to find male/female characters, so we are searching for unknown characters
    #     search_for_characters(
    #         elem, {CHARACTER_CODE_TO_NAME[code]: code for code in SEX_TO_CHARACTER_CODE['UNKNOWN']}.items(),
    #         characters, main_character, lexemes, text, lexemes_dict, used_lexemes_indices, character_code_to_index
    #     )

    characters.sort(key=lambda e: character_code_to_index[e])

    elem.set("characters", " ".join(characters))

    if characters:
        global PREV_CHARACTER
        PREV_CHARACTER = characters[0]
    enrich_stage(elem, characters[0] if characters else main_character)


def get_menu(codes: List[str], names: List[str], indent: str) -> str:
    s: str = ""

    if not codes:
        return s

    s += f"{indent}menu:\n"

    indent += TAB

    num_of_pages: int = (len(codes) - 1) // MAX_NUM_OF_VALUES_IN_LIST + 1
    for i in range(num_of_pages):
        scene_code: int = 0
        for scene_num, scene_code in \
                enumerate(codes[MAX_NUM_OF_VALUES_IN_LIST * i:MAX_NUM_OF_VALUES_IN_LIST * (i + 1)]):
            s += f'{indent}"{{color={BLACK_COLOR}}}{names[MAX_NUM_OF_VALUES_IN_LIST * i + scene_num]}{{/color}}":\n'
            s += f'    {indent}jump {scene_code}\n'
        if i < num_of_pages - 1:
            further_code = f'{FURTHER}_{scene_code}_{i + 1}'
            s += f'{indent}"{{color={BLACK_COLOR}}}>{{/color}}":\n'
            s += f'    {indent}jump {further_code}\n\n'
            indent = indent[8:]
            s += f'{indent}label {further_code}:\n'
            indent += TAB
            s += f"{indent}menu:\n"
            indent += TAB

    return s


def parse_scene_div(scene_div, act_num: str, indent: str, scene_codes: List[str], scene_names: List[str]) -> str:
    s: str = ""

    global PREV_CHARACTER
    PREV_CHARACTER = None

    scene_num = len(scene_codes) + 1
    scene_code: str = f'{ACT}_{act_num}_{SCENE}_{scene_num}'

    s += f'{indent}label {scene_code}:\n'

    indent = indent + TAB

    # music
    s += play_music(scene_div, indent)

    # background
    s += show_background(scene_div, indent)

    scene_name = f'{scene_div.attrib.get("type")}_{scene_num}'

    if not scene_div.findall("head"):
        s += f'{indent}"{{b}}{scene_name}{{/b}}"\n\n'
        scene_names.append(scene_name)

    characters = []
    notes: List = []
    for elem in scene_div:
        if characters and characters[0] != PREV_CHARACTER:
            PREV_CHARACTER = characters[0]

        if elem.tag == "head":
            scene_text: str = get_text(elem)
            scene_parts: List[str] = re.split(r"(?<=[.])", scene_text)
            scene_name: str = scene_parts[0]
            scene_names.append(scene_name)

            elem.text = scene_name
            s += add_line(elem, characters, indent, notes)

            if len(scene_parts) > 1 and not (len(scene_parts) == 2 and not scene_parts[1]):
                scene_stage = etree.Element("stage")
                scene_stage.text = "".join(scene_parts[1:]).strip()

                s += add_stage(scene_stage, [], indent, notes)
        elif elem.tag == "castList":
            s += parse_cast_list(elem, indent, from_tag="scene")
        else:
            s += parse_any(elem, characters, indent, notes)

    PREV_CHARACTER = None

    scene_codes.append(scene_code)

    return s


def parse_act_div(act_div, indent: str, scene_codes: List[str], scene_names: List[str],
                  act_codes: List[str], act_names: List[str], act: str) -> str:
    s: str = ""

    global PREV_CHARACTER
    PREV_CHARACTER = None

    act_num: str = f'{len(ACT_CODES) + 1}' \
        if act == ACT \
        else f'{len(ACT_CODES) + 1}_{len(act_codes) + 1}_{len(scene_codes) + 1}'
    act_code: str = f'{act}_{act_num}'

    act_num: int = len([elem for elem in act_codes if elem.startswith(act)])
    act_codes.append(act_code)

    s += f'{indent}label {act_code}:\n'

    indent = indent + TAB

    # music
    s += play_music(act_div, indent, get_random=True)

    # background
    s += show_background(act_div, indent, get_random=True)

    act_name = f'{act_div.attrib.get("type")}_{act_num + 1}' if act_div.attrib.get("type") else act_div.tag

    if not act_div.findall("head"):
        s += f'{indent}"{{b}}{act_name}{{/b}}"\n\n'
        act_names.append(act_name)

    s_content: str = ""

    characters = []
    scenes: str = ''
    notes = []

    was_sp_or_div: bool = False

    for elem in act_div:
        if elem.tag in ["sp", "div"]:
            was_sp_or_div = True

        tmp_s = scenes if was_sp_or_div else s_content

        if elem.tag == "head":
            act_text: str = get_text(elem)
            act_parts: List[str] = re.split(r"(?<=[.])", act_text)
            act_name: str = act_parts[0]
            if len(act_codes) != len(act_names):
                act_names.append(act_name)

            elem.text = act_name
            tmp_s += add_line(elem, characters, indent, notes)

            if len(act_parts) > 1 and not (len(act_parts) == 2 and not act_parts[1]):
                act_stage = etree.Element("stage")
                act_stage.text = "".join(act_parts[1:]).strip()

                tmp_s += add_stage(act_stage, [], indent, notes)
        elif elem.tag == "div" and elem.attrib["type"] == "scene":
            tmp_s += parse_scene_div(elem, act_num, indent,
                                     SUB_SCENE_CODES if act == SCENE else SCENE_CODES,
                                     SUB_SCENE_NAMES if act == SCENE else SCENE_NAMES)
        elif elem.tag == "div":
            tmp_s += parse_act_div(elem, indent, SUB_SCENE_CODES, SUB_SCENE_NAMES, SCENE_CODES, SCENE_NAMES, SCENE)
        elif elem.tag in ["trailer", "dateline"]:
            tmp_s += add_stage(elem, characters, indent, notes)
        elif act_div.tag == "set" and elem.tag in ["p", "l"]:  # hardcode
            elem.tag = "stage"
            tmp_s += add_stage(elem, characters, indent, notes)
        elif elem.tag == "castList":
            scenes += parse_cast_list(elem, indent, from_tag="act")
        else:
            tmp_s += parse_any(elem, characters, indent, notes)

        if was_sp_or_div:
            scenes = tmp_s
        else:
            s_content = tmp_s

    s_content += get_menu(scene_codes, scene_names, indent)

    s_content += f'\n{scenes}'

    scene_codes.clear()
    scene_names.clear()

    if s_content.strip():
        s += s_content
    else:
        del act_codes[-1]
        del act_names[-1]
        s = ''

    return s


def parse_body(body, indent: str = "") -> str:
    s: str = ""

    SCENE_CODES.clear()
    SCENE_NAMES.clear()

    for elem in body:
        if elem.tag == "div":  # and elem.attrib["type"] in ["act", "scene"]
            s += parse_act_div(elem, indent, SCENE_CODES, SCENE_NAMES, ACT_CODES, ACT_NAMES, ACT)
        else:
            s += parse_any(elem, [], indent)

    return s


def set_global_variables():
    # editing screens.rpy
    with open(f'{MAIN_DIRECTORY}/screens.rpy', 'r', encoding='utf-8') as screens_f:
        screens_text = screens_f.read()

    if 'properties gui.button_properties("choice_button")\n    background "#ffffff"' not in screens_text:
        screens_text = screens_text.replace(
            'properties gui.button_properties("choice_button")',
            'properties gui.button_properties("choice_button")\n    background "#ffffff"'
        )

    if 'screen tooltip(text):' not in screens_text:
        screens_text += """
style slider_slider:
    variant "small"
    xsize 900

style myFrame is default:
    background Solid("#ffffff")

screen tooltip(text):
    frame:
        style "myFrame"
        xalign 0.5
        yalign 0
        has vbox

        text text

init python:
    def hyperlink_styler(hi):
        return style.hyperlink_text

    def hyperlink_callback(data):
        if data is None:
            renpy.hide_screen("tooltip")
        else:
            args = data.split('|')

            _ = args.pop(0)
            screen_name = args.pop(0)

            args = dict([arg.split('=') for arg in args])

            renpy.show_screen(screen_name, **args)

        renpy.restart_interaction()

    config.hyperlink_handlers['myshow'] = hyperlink_callback

style default hyperlink_functions(hyperlink_styler,  None, hyperlink_callback)
"""

    with open(f'{MAIN_DIRECTORY}/screens.rpy', 'w', encoding='utf-8') as screens_f:
        screens_f.write(screens_text)

    # editing options.rpy
    with open(f'{MAIN_DIRECTORY}/options.rpy', 'r', encoding='utf-8') as options_f:
        options_text = options_f.read()

    if 'renpy.music.register_channel("sound5", "sfx", False)' not in options_text:
        options_text += """
init python:
    ## register new channels "sound1" - "sound5" to combine several sounds
    renpy.music.register_channel("sound1", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound5", "sfx", False)
"""

        with open(f'{MAIN_DIRECTORY}/options.rpy', 'w', encoding='utf-8') as options_f:
            options_f.write(options_text)

    # todo: make options random
    # copying textbox.png
    shutil.copy(
        Path(f'{PATH_TO_GUI_FILES}/textbox.png'),
        Path(f'{PATH_TO_GUI_DIRECTORY}/textbox.png')
    )

    # copying font NotepadFont.ttf
    shutil.copy(
        Path(f'fonts/NotepadFont.ttf'),
        Path(f'{MAIN_DIRECTORY}/NotepadFont.ttf')
    )

    # editing gui.rpy
    with open(f'{MAIN_DIRECTORY}/gui.rpy', 'r', encoding='utf-8') as gui_f:
        gui_text_lines: List[str] = gui_f.readlines()

    # todo: add more random options
    for i, gui_text_line in enumerate(gui_text_lines):
        if gui_text_line.startswith("define gui.text_color = "):
            gui_text_lines[i] = re.sub("'.*?'", "'#000000'", gui_text_line)
        elif gui_text_line.startswith("define gui.main_menu_background = "):
            gui_text_lines[i] = re.sub('".*?"', '"gui/main_menu.jpeg"', gui_text_line)
        elif gui_text_line.startswith("define gui.text_font = "):
            gui_text_lines[i] = re.sub('".*?"', '"NotepadFont.ttf"', gui_text_line)
        elif gui_text_line.startswith("define gui.name_text_font = "):
            gui_text_lines[i] = re.sub('".*?"', '"NotepadFont.ttf"', gui_text_line)
        elif gui_text_line.startswith("define gui.interface_text_font = "):
            gui_text_lines[i] = re.sub('".*?"', '"NotepadFont.ttf"', gui_text_line)

    with open(f'{MAIN_DIRECTORY}/gui.rpy', 'w', encoding='utf-8') as gui_f:
        gui_f.writelines(gui_text_lines)

    main_menu_file = Path(f'{PATH_TO_PICTURES_DIRECTORY}/{PLAY_NAME}/main_menu.jpeg')
    if main_menu_file.is_file():
        shutil.copy(
            main_menu_file,
            Path(f'{PATH_TO_GUI_DIRECTORY}/main_menu.jpeg')
        )
    else:
        shutil.copy(
            Path(f'{PATH_TO_PICTURES_DIRECTORY}/default_background.jpeg'),
            Path(f'{PATH_TO_GUI_DIRECTORY}/main_menu.jpeg')
        )

    textbox_file = Path(f'{PATH_TO_PICTURES_DIRECTORY}/{PLAY_NAME}/textbox.png')
    if textbox_file.is_file():
        shutil.copy(
            textbox_file,
            Path(f'{PATH_TO_GUI_DIRECTORY}/textbox.png')
        )

    window_icon_file = Path(f'{PATH_TO_PICTURES_DIRECTORY}/{PLAY_NAME}/window_icon.png')
    if textbox_file.is_file():
        shutil.copy(
            window_icon_file,
            Path(f'{PATH_TO_GUI_DIRECTORY}/window_icon.png')
        )

    poster_file = Path(f'{PATH_TO_PICTURES_DIRECTORY}/{PLAY_NAME}/poster.jpeg')
    if poster_file.is_file():
        shutil.copy(
            poster_file,
            Path(f'{PATH_TO_BACKGROUNDS_DIRECTORY}/poster.jpeg')
        )


def parse_tei_header(tei_header, indent: str) -> str:
    s: str = ""

    for elem in tei_header:
        s += parse_any(elem, [], indent)

    return s


def parse_stand_off(stand_off, indent: str) -> str:
    s: str = ""

    # global STAND_OFF
    # STAND_OFF = parse_act_div(stand_off, indent)

    return s


def parse_doc_title(doc_title, indent: str) -> str:
    s: str = ""

    notes: List[str] = []
    main_title_elems = []
    sub_title_elems = []
    for elem in doc_title:
        if elem.tag == "titlePart":
            if elem.attrib["type"] == "main":
                main_title_elems.append(elem)
            elif elem.attrib["type"] == "sub":
                sub_title_elems.append(elem)
            else:
                raise NotImplementedError
        else:
            s += parse_any(elem, [], indent, notes)

    for main_title_elem in main_title_elems:
        s += add_line(main_title_elem, [], indent, notes)

    for sub_title_elem in sub_title_elems:
        s += add_line(sub_title_elem, [], indent, notes)

    return s


def parse_cast_group(cast_group, indent: str, notes: List = None) -> str:
    s: str = ""

    for elem in cast_group:
        if elem.tag in ["head", "roleDesc"]:
            s += add_line(elem, [], indent, notes=notes)
        elif elem.tag == "castItem":
            if elem:
                for inner_elem in elem:
                    if inner_elem.tag == "note":
                        notes.append(inner_elem)
                    else:
                        s += parse_cast_item(inner_elem, indent, notes=notes)
            else:
                s += parse_cast_item(elem, indent, notes=notes)

            notes.clear()
        elif elem.tag == "castGroup":
            s += parse_cast_group(elem, indent, notes=notes)

            notes.clear()
        elif elem.tag == "note":
            notes.append(elem)
        else:
            print(elem.tag)
            raise NotImplementedError

    return s


def parse_cast_list(cast_list, indent: str, from_tag: str) -> str:
    s: str = ""

    global NUM_OF_CHARACTERS

    NUM_OF_CHARACTERS += 1
    scene_code: str = f'{CHARACTERS}_{NUM_OF_CHARACTERS}'
    global SCENE_CODES
    if from_tag == "scene":
        SCENE_CODES.insert(-1, scene_code)
    else:
        SCENE_CODES.append(scene_code)

    s += f'{indent}label {scene_code}:\n'

    indent += TAB

    # music
    s += play_music(cast_list, indent, get_random=True)

    # background
    s += show_background(cast_list, indent, get_random=True)

    global SCENE_NAMES
    notes: List = []
    for elem in cast_list:
        if elem.tag == "head":
            elem_text: str = get_text(elem)

            if from_tag == "scene":
                elem_text = f"({SCENE_NAMES[-1]}) {elem_text}"
                SCENE_NAMES.insert(-1, elem_text)
            else:
                SCENE_NAMES.append(elem_text)

            if from_tag == "front":
                global CHARACTERS_NAME
                CHARACTERS_NAME = elem_text

            s += f'{indent}"{{b}}{elem_text}{{/b}}"\n\n'
        elif elem.tag == "castItem":
            if elem:
                for inner_elem in elem:
                    if inner_elem.tag == "note":
                        notes.append(inner_elem)
                    else:
                        s += parse_cast_item(inner_elem, indent, notes=notes)
            else:
                s += parse_cast_item(elem, indent, notes=notes)

            notes.clear()
        elif elem.tag == "castGroup":
            s += parse_cast_group(elem, indent, notes=notes)

            notes.clear()
        elif elem.tag == "note":
            notes.append(elem)

    return s


def add_cast_list_from_header(indent: str) -> str:
    s: str = ""

    global NUM_OF_CHARACTERS
    NUM_OF_CHARACTERS += 1
    s += f'{indent}label {CHARACTERS}_{NUM_OF_CHARACTERS}:\n'

    indent += TAB

    # music
    s += play_music(None, indent, get_random=True)

    # background
    s += show_background(None, indent, get_random=True)

    s += f'{indent}"{{b}}{CHARACTERS}{{/b}}"\n\n'

    for character_code, character_name in CHARACTER_CODE_TO_NAME.items():
        s += f'{indent}show {character_code} at truecenter\n'  # with dissolve
        s += f'{indent}"{character_name}"\n'
        s += f'{indent}hide {character_code}\n\n'  # with dissolve

    return s


def parse_front(front, indent: str) -> str:
    s: str = ""

    global CHARACTERS_TEXT
    was_cast_list: bool = False
    for elem in front:
        if elem.tag == "docTitle":
            s += parse_doc_title(elem, indent)
        elif elem.tag == "castList":
            CHARACTERS_TEXT = parse_cast_list(elem, indent, "front")

            was_cast_list = True
            SCENE_CODES.clear()
            SCENE_NAMES.clear()
        elif elem.tag in ["performance", "div", "set", "epigraph"]:
            global FRONT_TEXTS

            FRONT_TEXTS.append(parse_act_div(
                elem, indent, SCENE_CODES, SCENE_NAMES, ACT_CODES, ACT_NAMES, elem.tag.upper()
            ))
        else:
            s += parse_any(elem, [], indent)

    if not was_cast_list:
        global CHARACTERS_NAME
        CHARACTERS_NAME = CHARACTERS
        CHARACTERS_TEXT = add_cast_list_from_header(indent)

    return s


def parse_text_elem(text_elem, indent: str) -> str:
    s: str = ""

    was_front: bool = False
    for elem in text_elem:
        if elem.tag == "front":
            s += parse_front(elem, indent)
            was_front = True
        elif elem.tag == "body":
            global ACTS_TEXT

            ACTS_TEXT = parse_body(elem)

    if not was_front:
        global CHARACTERS_NAME
        global CHARACTERS_TEXT
        CHARACTERS_NAME = CHARACTERS
        CHARACTERS_TEXT = add_cast_list_from_header(indent)

    return s


def parse_list_person(list_person, indent: str) -> str:
    s: str = ""

    characters = []
    for elem in list_person:
        if elem.tag in ["person", "personGrp"]:
            if elem.tag == "personGrp":
                elem.attrib["sex"] = "UNKNOWN"
            characters.append(elem)

    s += f'{indent}{create_character_variables(characters)}\n'

    return s


def is_line(value):
    return value.tag in ["p", "l", "bibl", "head", "docAuthor", "ab"] and \
        (value.text is not None or value.itertext())


def is_stage(value):
    return value.tag in ["stage", "trailer", "dateline", "bibl"]


def divide_any(check_func, add_func, elem, characters, indent: str, notes: List = None):
    if notes is None:
        notes = []

    s: str = ""

    outer_elems = []

    texts = [value for value in elem.itertext()]

    elem_i = 0
    for text in texts:
        if elem_i < len(elem) and text == elem[elem_i].text:
            outer_elems.append(elem[elem_i])
            elem_i += 1
        else:
            new_elem = copy(elem)
            new_elem.text = text
            outer_elems.append(new_elem)

    for outer_elem in outer_elems:
        if check_func(outer_elem):
            s += add_func(outer_elem, characters, indent, notes)
        else:
            s += parse_any(outer_elem, characters, indent, notes)

    return s


def parse_any(elem, characters, indent: str, notes: List = None) -> str:
    if notes is None:
        notes = []

    s: str = ""

    if is_line(elem):
        s += divide_any(is_line, add_line, elem, characters, indent, notes)
        notes.clear()
    elif is_stage(elem):
        s += divide_any(is_stage, add_stage, elem, characters, indent, notes)
    elif elem.tag == "set":
        for inner_elem in elem:
            inner_elem.tag = "stage"
            s += add_stage(inner_elem, characters, indent, notes)
    elif elem.tag == "sp":
        characters.clear()
        s += get_sp(elem, characters, indent)
        characters.clear()
    elif elem.tag == "listPerson":
        s += parse_list_person(elem, indent)
    elif elem.tag == "note":
        notes.append(elem)
    elif elem.tag == "speaker":
        s += f'{indent}$ {characters[0]}_var = "{{noalt}}{get_text(elem)}"\n\n'
    else:
        if elem:
            for inner_elem in elem:
                s += parse_any(inner_elem, characters, indent, notes)
        elif elem.text is not None:
            s += add_line(elem, characters, indent, notes)

    return s


def parse_root(root) -> str:
    s: str = ""

    set_global_variables()

    indent: str = ""

    for elem in root:
        if elem.tag == "teiHeader":
            s += parse_tei_header(elem, indent)

            # start
            s += f'{indent}label start:\n'

            indent += TAB

            # music
            s += play_music(root, indent, get_random=True)

            # background
            if Path(f'{PATH_TO_BACKGROUNDS_DIRECTORY}/poster.jpeg').is_file():
                root.set("background", "poster")

            s += show_background(root, indent, get_random=True)
        elif elem.tag == "standOff":
            s += parse_stand_off(elem, indent)
        elif elem.tag == "text":
            s += parse_text_elem(elem, indent)
        else:
            raise NotImplementedError

    # MENU
    s += f'{get_root_menu(indent)}\n'

    # CHARACTERS
    s += f'{CHARACTERS_TEXT}\n'

    if STAND_OFF.strip():
        s += f'{STAND_OFF}\n'

    # FRONT_TEXTS
    for front_text in FRONT_TEXTS:
        s += f'{front_text}\n\n'

    # ACTS
    s += f'{ACTS_TEXT}\n'

    return s


def main():
    with open(PATH_TO_INPUT_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace("<emph>", "{i}").replace("</emph>", "{/i}")

    with tempfile.NamedTemporaryFile() as tmp:
        with open(tmp.name, 'w', encoding='utf-8') as f:
            f.write(text)

        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(tmp.name, parser)

    root = tree.getroot()

    for elem in root.getiterator():
        if not hasattr(elem.tag, 'find'):
            continue  # guard for Comment tags
        i = elem.tag.find('}')
        if i >= 0:
            elem.tag = elem.tag[i + 1:]
    objectify.deannotate(root, cleanup_namespaces=True)

    s: str = parse_root(root)

    with open(PATH_TO_OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(s)


if __name__ == '__main__':
    main()
