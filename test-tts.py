from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice
import torchaudio

tts = TextToSpeech(kv_cache=True)

example_texts = ["والجمهور مبسوط that's good",
                 "اليوم، إذا أرخيصة ولا غالية ولا تراك قديم ولا ما بعرف he doesn't care هو بيسأل على الـ functionality أما هاي قصة أنه مستحيل، مست",
                 "كنت أنا أصغر واحدة البنت المدللة عند العيلة كلها يعني عند أمي وأبوي وأخوتي وإحنا عيلة كبيرة اسمالله"
                ]

voices = ["tom", "train_atkins", "angie"]

for voice, text in zip(voices, example_texts):
    voice_samples, _ = load_voice(voice)
    audio = tts.tts_with_preset(text, voice_samples=voice_samples, preset='fast')
    torchaudio.save(f'{voice}.wav', audio.squeeze(0), 24000)
