# Document-Question-Answering-System
#### To Run this app, go through the following steps:

- #### First, install all the libraries mentioned in the requirements.txt.

![Alt text](<https://github.com/ShoaibMajidDar/Document-Question-Answering-System/blob/main/images/Screenshot%20(172).png>) ![Alt text](<https://github.com/ShoaibMajidDar/Document-Question-Answering-System/blob/main/images/Screenshot%20(173).png>)


- #### And then create a .env file and add "OPENAI_API_KEY=Your OpenAI API key"
![Alt text](<https://github.com/ShoaibMajidDar/Document-Question-Answering-System/blob/main/images/Screenshot%20(174).png>)


- #### After doing these step, open the terminal in the folder containing app.py and .env and type `streamlit run app.py`
![Alt text](<https://github.com/ShoaibMajidDar/Document-Question-Answering-System/blob/main/images/Screenshot%20(175).png>)






#### The app looks like this:
![Alt text](<https://github.com/ShoaibMajidDar/Document-Question-Answering-System/blob/main/images/Screenshot%20(176).png>)

#### Upload a PDF on the app and a chatbox will appear on the screen where you can ask any question regarding the pdf and it will answer the question.
![Alt text](<https://github.com/ShoaibMajidDar/Document-Question-Answering-System/blob/main/images/Screenshot%20(179).png>)

### The app will save the embeddings of your pdf as a .pkl file on your system, so if you upload same PDF again it will reuse the older embeddings rather than creating a new one.
### Also gpt-3.5-turbo is used as an LLM.