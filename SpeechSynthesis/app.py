import azure.cognitiveservices.speech as speech_sdk
key_resource=""
region_resource="eastus"

translation_details=speech_sdk.translation.SpeechTranslationConfig(key_resource,region_resource)

translation_details.speech_recognition_language='en-US'

translation_details.add_target_language('fr')
translation_details.add_target_language('es')
translation_details.add_target_language('hi')
translation_details.add_target_language('kn')

speech_config=speech_sdk.SpeechConfig(key_resource,region_resource)

targetLanguage=""
while targetLanguage!="quit":
    targetLanguage=input("\nEnter a target language \n fr=French \n es=Spanish \n hi-Hindi \n kn=Kannada \n")
    if targetLanguage in translation_details.target_languages:
        audio_config=speech_sdk.AudioConfig(use_default_microphone=True)
        translator=speech_sdk.translation.TranslationRecognizer(translation_details,audio_config=audio_config)
        print("Speak Now..")
        result=translator.recognize_once_async().get()
        print("Original Text",result.text)
        translation=result.translations[targetLanguage]
        print("Translation",result.translations[targetLanguage])
        voices={
            "fr":"fr-FR-HenriNeural",
            "hi":"hi-IN-MadhurNeural",
            "es":"es-ES-ElviraNeural",
            "kn":"kn-IN-GaganNeural"
        }
        speech_config.speech_synthesis_voice_name=voices.get(targetLanguage)
        speech_synthesizer=speech_sdk.SpeechSynthesizer(speech_config)
        speech_synthesizer.speak_text_async(translation).get()
    else:
        targetLanguage="quit"