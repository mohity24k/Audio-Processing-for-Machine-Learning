"""
Text-to-Speech Model Implementation
This module provides functionality to convert text to speech using Google's TTS API.
"""

from gtts import gTTS
import os


class TextToSpeech:
    """
    A simple Text-to-Speech converter using Google's Text-to-Speech API.
    
    Attributes:
        language (str): Language code for the speech output (default: 'en')
        slow (bool): Whether to use slow speech speed (default: False)
    """
    
    def __init__(self, language='en', slow=False):
        """
        Initialize the TextToSpeech converter.
        
        Args:
            language (str): Language code (e.g., 'en' for English, 'es' for Spanish)
            slow (bool): If True, speech will be slower
        """
        self.language = language
        self.slow = slow
    
    def text_to_speech(self, text, output_file='output.mp3'):
        """
        Convert text to speech and save as an audio file.
        
        Args:
            text (str): The text to convert to speech
            output_file (str): Path to save the output audio file (default: 'output.mp3')
        
        Returns:
            str: Path to the generated audio file
        
        Raises:
            ValueError: If text is empty or None
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        # Create TTS object
        tts = gTTS(text=text, lang=self.language, slow=self.slow)
        
        # Save the audio file
        tts.save(output_file)
        
        return output_file
    
    def text_to_speech_from_file(self, input_file, output_file='output.mp3'):
        """
        Read text from a file and convert it to speech.
        
        Args:
            input_file (str): Path to the input text file
            output_file (str): Path to save the output audio file (default: 'output.mp3')
        
        Returns:
            str: Path to the generated audio file
        
        Raises:
            FileNotFoundError: If input file doesn't exist
        """
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found")
        
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        return self.text_to_speech(text, output_file)


def main():
    """
    Main function demonstrating basic usage of the TextToSpeech class.
    """
    # Example usage
    tts = TextToSpeech(language='en', slow=False)
    
    sample_text = "Hello! This is a text-to-speech model for audio processing and machine learning."
    
    print(f"Converting text to speech: '{sample_text}'")
    output_path = tts.text_to_speech(sample_text, 'sample_output.mp3')
    print(f"Audio saved to: {output_path}")


if __name__ == "__main__":
    main()
