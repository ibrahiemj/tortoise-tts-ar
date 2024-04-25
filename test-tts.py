from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice
import torchaudio

tts = TextToSpeech(kv_cache=True, device="cuda")

example_texts = ["مرحبا جميعاً كيف الحال؟",
                 "Hello where is the catch here?",
                 "كنت أنا أصغر واحدة البنت المدللة عند العيلة كلها يعني عند أمي وأبوي وأخوتي وإحنا عيلة كبيرة اسمالله"
                ]

voice = "mona"

for i, text in enumerate(example_texts):
    voice_samples, _ = load_voice(voice)
    print(tts.device)
    audio = tts.tts_with_preset(text, voice_samples=voice_samples, preset='high_quality')
    torchaudio.save(f'{voice}-{i}.wav', audio.squeeze(0), 24000)
