# Audio-Processing-for-Machine-Learning

A project which I took upon during this semester as a part of my minor degree - Artificial Intelligence and Machine Learning.

## Text-to-Speech Model

This repository includes a text-to-speech (TTS) model implementation that converts written text into spoken audio using Google's Text-to-Speech API.

### Features

- **Simple API**: Easy-to-use Python interface for text-to-speech conversion
- **Multilingual Support**: Convert text to speech in multiple languages
- **Flexible Output**: Save audio files in MP3 format
- **Speed Control**: Option for slow or normal speech speed
- **File Input**: Convert text from files directly to speech

### Installation

1. Clone this repository:
```bash
git clone https://github.com/mohity24k/Audio-Processing-for-Machine-Learning.git
cd Audio-Processing-for-Machine-Learning
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Basic Usage

```python
from tts_model import TextToSpeech

# Create TTS instance
tts = TextToSpeech(language='en')

# Convert text to speech
text = "Hello! This is a text-to-speech model."
tts.text_to_speech(text, 'output.mp3')
```

#### Advanced Usage

```python
from tts_model import TextToSpeech

# Slow speech for better clarity
tts = TextToSpeech(language='en', slow=True)
tts.text_to_speech("This is spoken slowly.", 'slow_output.mp3')

# Multilingual support
tts_spanish = TextToSpeech(language='es')
tts_spanish.text_to_speech("Hola, ¿cómo estás?", 'spanish_output.mp3')

# Convert text from a file
tts.text_to_speech_from_file('input.txt', 'file_output.mp3')
```

#### Running Examples

Run the example script to see various use cases:

```bash
python tts_examples.py
```

This will generate several audio files demonstrating:
- Basic text-to-speech conversion
- Slow speech mode
- Multilingual support (English, Spanish, French)
- Converting text from files

### API Reference

#### TextToSpeech Class

**Constructor:**
- `TextToSpeech(language='en', slow=False)`
  - `language`: Language code (e.g., 'en', 'es', 'fr')
  - `slow`: Boolean for slow speech speed

**Methods:**
- `text_to_speech(text, output_file='output.mp3')`: Convert text to speech
- `text_to_speech_from_file(input_file, output_file='output.mp3')`: Convert text from file to speech

### Supported Languages

The model supports multiple languages including:
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- And many more...

For a complete list, refer to the [gTTS documentation](https://gtts.readthedocs.io/).

### Requirements

- Python 3.6+
- gTTS 2.4.0+
- pydub 0.25.1+

### License

This project is for educational purposes as part of an AI and Machine Learning minor degree program.
