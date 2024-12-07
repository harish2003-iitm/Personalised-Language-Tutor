# **Personalized Language Tutor**

## **Overview**

The **Personalized Language Tutor** leverages OpenAI's cutting-edge APIs to deliver AI-enhanced tools for seamless transcription, translation, grammar checking, and pronunciation feedback. Designed for language learners, this tool provides an integrated and user-friendly platform to support cross-lingual communication and language mastery.

![Screen-1](images/Screenshot%202024-12-07%20201838.png)

![Screen-2](images/Screenshot%202024-12-07%20201852.png)

---

## **Features**

### 🎙️ **1. Audio Transcription**
- Converts spoken language from an audio file (`sample.wav`) into text using OpenAI's **Whisper-1** model.
- Provides an accurate text representation of spoken content for further analysis.

### 🌍 **2. Text Translation**
- Translates transcribed text into the target language specified by the user.
- Utilizes OpenAI's **GPT-4o-mini** model for precise and contextual translations.

### ✍️ **3. Grammar Feedback**
- Analyzes translated text for grammatical errors.
- Suggests corrections and refinements to improve the quality of the user's writing.

### 🗣️ **4. Pronunciation Feedback**
- Evaluates user pronunciation by comparing the original transcription with a user-defined target sentence.
- Offers personalized suggestions for improving pronunciation accuracy and clarity.

---

## **Workflow**

### **1. Audio Upload**
   - Users upload an audio file (`data/sample.wav`) to the system.

### **2. Transcription**
   - The uploaded audio is transcribed into text using OpenAI's **Whisper-1** model.
   - The transcribed text is stored in a variable called `transcription_text`.

### **3. Translation**
   - The transcription text is translated into the desired language specified by the user.
   - The translated text is stored in a variable called `translated_text`.

### **4. Grammar Feedback**
   - The translated text is analyzed for grammatical errors, and corrections are suggested.
   - The corrected version is stored in a variable called `grammar_feedback`.

### **5. Pronunciation Feedback**
   - User pronunciation is evaluated by comparing the transcription with a user-defined target sentence.
   - Personalized feedback is provided, stored in a variable called `pronunciation_feedback`.

---

## **Key Variables**

| **Variable**             | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| `transcription_text`      | Stores the text transcribed from the uploaded audio file.                      |
| `translated_text`         | Stores the translated version of the transcribed text in the target language.  |
| `grammar_feedback`        | Stores the grammatical corrections and feedback for the translated text.       |
| `pronunciation_feedback`  | Stores the personalized feedback for improving pronunciation.                  |

---

## **System Flow**

1. **User Input**:  
   - Upload an audio file (`sample.wav`).  
   - Specify the target language for translation.  
   - Provide a target sentence for pronunciation comparison.

2. **AI Processing**:  
   - **Transcription**: Converts audio to text.  
   - **Translation**: Translates the transcription to the desired language.  
   - **Grammar Feedback**: Analyzes grammar in the translated text.  
   - **Pronunciation Feedback**: Compares user pronunciation to the target sentence.

3. **Output**:  
   - Transcription text.  
   - Translated text.  
   - Grammar corrections.  
   - Pronunciation improvement suggestions.

---

## **Example Workflow**

### **Input**
- **Audio File**: `sample.wav`
- **Target Language**: `French`
- **Target Pronunciation**: `"Bonjour, comment ça va?"`

### **Output**
- **Transcription**: `"The patient reported mild fever and cough for three days."`  
- **Translation**: `"Le patient a signalé une légère fièvre et une toux pendant trois jours."`  
- **Grammar Feedback**: `"The translated text is grammatically correct."`  
- **Pronunciation Feedback**: `"Your pronunciation is 85% accurate. Improve clarity on 'fièvre'."`

---

## **Future Enhancements**

- **Interactive UI**: Develop an interface using frameworks like **Streamlit** for better usability.
- **Real-Time Voice Processing**: Enable live transcription and translation for real-time communication.
- **Voice-to-Voice Translation**: Support output in synthesized speech for complete language support.
- **Batch Processing**: Allow processing of multiple audio files simultaneously.

---

The **Personalized Language Tutor** seamlessly integrates transcription, translation, grammar checking, and pronunciation feedback into a single, cohesive tool. This application harnesses the power of OpenAI APIs to transform language learning into an interactive, AI-driven experience.

---

## **Credits**
- **API**: Powered by [OpenAI](https://openai.com/).
- **Development**: Built for educators, learners, and cross-lingual professionals.
