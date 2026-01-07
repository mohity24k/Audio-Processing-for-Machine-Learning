# Text-to-Speech Model - Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/mohity24k/Audio-Processing-for-Machine-Learning.git
cd Audio-Processing-for-Machine-Learning

# Install dependencies
pip install -r requirements.txt

# Install platform-specific TTS engine (Linux only)
sudo apt-get install espeak
```

## Basic Usage

### 1. Simple Text-to-Speech
```python
from tts_model import TextToSpeech

tts = TextToSpeech()
tts.text_to_speech("Hello World!", "output.wav")
```

### 2. Direct Audio Playback (Recommended)
```python
from tts_model import TextToSpeech

tts = TextToSpeech()
tts.speak("Hello World!")  # Plays audio directly
```

### 3. Customize Speech Rate
```python
from tts_model import TextToSpeech

# Slow speech (100 words per minute)
tts_slow = TextToSpeech(rate=100)
tts_slow.speak("This is slow speech.")

# Fast speech (200 words per minute)
tts_fast = TextToSpeech(rate=200)
tts_fast.speak("This is fast speech.")
```

### 4. Select Different Voices
```python
from tts_model import TextToSpeech

tts = TextToSpeech()

# List available voices
voices = tts.get_available_voices()
for i, voice in enumerate(voices[:5]):
    print(f"{i}: {voice.name}")

# Select a specific voice
tts.set_voice(12)  # English voice
tts.speak("Speaking with selected voice.")
```

### 5. Convert Text from File
```python
from tts_model import TextToSpeech

tts = TextToSpeech()
tts.text_to_speech_from_file("input.txt", "output.wav")
```

## Running Examples

```bash
# Run all examples
python tts_examples.py

# Run tests
python test_tts.py
```

## Platform Notes

- **Linux**: Uses eSpeak engine. File saving may have limitations.
- **Windows**: Uses SAPI5. Full file saving support.
- **macOS**: Uses NSSpeechSynthesizer. Full file saving support.

For best results on all platforms, use the `speak()` method for direct audio playback.

## API Reference

### TextToSpeech Class

**Constructor:**
```python
TextToSpeech(rate=150, volume=1.0, voice_index=0)
```
- `rate`: Speech rate in words per minute (default: 150)
- `volume`: Volume level 0.0-1.0 (default: 1.0)
- `voice_index`: Voice to use (default: 0)

**Methods:**
- `text_to_speech(text, output_file)`: Convert and save to file
- `speak(text)`: Direct audio playback (recommended)
- `text_to_speech_from_file(input_file, output_file)`: Convert from file
- `get_available_voices()`: List available voices
- `set_voice(voice_index)`: Change voice

## Troubleshooting

**Issue**: No audio output
**Solution**: Check system volume and audio drivers

**Issue**: File saving doesn't work (Linux)
**Solution**: Use `speak()` method instead for direct playback

**Issue**: Import error
**Solution**: Ensure pyttsx3 is installed: `pip install pyttsx3`
