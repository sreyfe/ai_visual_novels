# ai_visual_novels
AI generation of RenPy visual novels from tagged plays on [DraCor.org]. Uses ChatGPT and DALL-E to generate backgrounds and character sprites.

You can either input your OpenAI API key as an option (`--key`) or modify the code (`openai.api_key = ""`). 

```
usage: AI Visual Novels from DraCor [-h] [--key KEY] [--output OUTPUT] [--character_style CHARACTER_STYLE]
                                    [--background_style BACKGROUND_STYLE]
                                    text

positional arguments:
  text                  Path to DraCor tagged drama to be transformed

options:
  -h, --help            show this help message and exit
  --key KEY             Your OpenAI key
  --output OUTPUT       Specifies an output directory
  --character_style CHARACTER_STYLE
                        Gives a style reference for the character sprites. Defaults to "yugioh."
  --background_style BACKGROUND_STYLE
                        Gives a style reference for the backgrounds.

 ```


Some screenshots from Lessing's Emilia Galotti:
![Screenshot from 2023-03-13 13-51-51](https://user-images.githubusercontent.com/127442578/224787010-aaba4d56-5b87-4305-9fc7-b5c16258541b.jpg)
![Screenshot from 2023-03-13 13-51-27](https://user-images.githubusercontent.com/127442578/224787145-99a849c4-cc48-463c-b88a-16f390cbec0a.png)
![Screenshot from 2023-03-13 13-50-50](https://user-images.githubusercontent.com/127442578/224787350-574fc373-6d0f-4eb2-8e42-7204b2f09994.png)
