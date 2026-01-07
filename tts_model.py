"""
Text-to-Speech Model Implementation
This module provides functionality to convert text to speech using pyttsx3 (offline TTS).
"""

import pyttsx3
import os
import sys


class TextToSpeech:
    """
    A simple Text-to-Speech converter using pyttsx3 (offline TTS engine).
    
    Attributes:
        engine: The pyttsx3 TTS engine instance
        rate (int): Speech rate (words per minute)
        volume (float): Volume level (0.0 to 1.0)
    """
    
    def __init__(self, rate=150, volume=1.0, voice_index=0):
        """
        Initialize the TextToSpeech converter.
        
        Args:
            rate (int): Speech rate in words per minute (default: 150)
            volume (float): Volume level from 0.0 to 1.0 (default: 1.0)
            voice_index (int): Index of the voice to use (default: 0)
        """
        try:
            self.engine = pyttsx3.init()
        except Exception as e:
            print(f"Warning: Could not initialize TTS engine: {e}")
            print("TTS functionality will be limited.")
            self.engine = None
            return
            
        self.rate = rate
        self.volume = volume
        
        # Set properties
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Set voice
        voices = self.engine.getProperty('voices')
        if voices and voice_index < len(voices):
            self.engine.setProperty('voice', voices[voice_index].id)
    
    def get_available_voices(self):
        """
        Get list of available voices on the system.
        
        Returns:
            list: List of available voice objects
        """
        if not self.engine:
            return []
        return self.engine.getProperty('voices')
    
    def set_voice(self, voice_index):
        """
        Set the voice to use for speech.
        
        Args:
            voice_index (int): Index of the voice from available voices
        """
        if not self.engine:
            return
        voices = self.get_available_voices()
        if voices and 0 <= voice_index < len(voices):
            self.engine.setProperty('voice', voices[voice_index].id)
    
    def text_to_speech(self, text, output_file='output.wav'):
        """
        Convert text to speech and save as an audio file.
        
        Note: File saving may not work on all platforms with eSpeak.
        On Linux with eSpeak, use the speak() method instead for audio playback,
        or install festival/SAPI5 voices for better file output support.
        
        Args:
            text (str): The text to convert to speech
            output_file (str): Path to save the output audio file (default: 'output.wav')
        
        Returns:
            str: Path to the generated audio file
        
        Raises:
            ValueError: If text is empty or None
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        if not self.engine:
            print(f"TTS engine not available. Would generate: {output_file}")
            return output_file
        
        # Save to file
        try:
            self.engine.save_to_file(text, output_file)
            self.engine.runAndWait()
            
            # Check if file was actually created
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                return output_file
            else:
                print(f"Note: File saving not fully supported on this platform.")
                print(f"Audio file '{output_file}' was created but may be empty.")
                print("Consider using the speak() method for direct audio playback.")
                return output_file
        except Exception as e:
            print(f"Error saving audio file: {e}")
            print("You can still use the speak() method for audio playback.")
            return output_file
    
    def text_to_speech_from_file(self, input_file, output_file='output.wav'):
        """
        Read text from a file and convert it to speech.
        
        Args:
            input_file (str): Path to the input text file
            output_file (str): Path to save the output audio file (default: 'output.wav')
        
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
    
    def speak(self, text):
        """
        Convert text to speech and play it (without saving to file).
        This method is more reliable across different platforms.
        
        Args:
            text (str): The text to convert to speech
        
        Raises:
            ValueError: If text is empty or None
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        if not self.engine:
            print(f"TTS engine not available. Would speak: '{text}'")
            return
        
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error during speech: {e}")


def main():
    """
    Main function demonstrating basic usage of the TextToSpeech class.
    """
    # Example usage
    tts = TextToSpeech(rate=150, volume=1.0)
    
    sample_text = "Hello! This is a text-to-speech model for audio processing and machine learning."
    
    print(f"Converting text to speech: '{sample_text}'")
    output_path = tts.text_to_speech(sample_text, 'sample_output.wav')
    print(f"Audio file created: {output_path}")
    
    # List available voices
    print("\nAvailable voices:")
    voices = tts.get_available_voices()
    for i, voice in enumerate(voices):
        print(f"  {i}: {voice.name} ({voice.languages})")
    
    # Demonstrate speak method (more reliable)
    print("\nDemonstrating speak() method (direct audio playback):")
    print("Speaking: 'This is a demonstration of direct audio playback.'")
    # Uncomment the line below to hear the speech (requires audio output)
    # tts.speak("This is a demonstration of direct audio playback.")


if __name__ == "__main__":
    main()
