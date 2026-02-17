# AI PDF Chat App

AI PDF Chat App হলো একটি Django এবং LangChain ভিত্তিক ওয়েব অ্যাপ যা ব্যবহারকারীদের PDF আপলোড করার পর তার উপর ভিত্তি করে চ্যাট করতে দেয়। এটি **FAISS** ব্যবহার করে PDF এর content কে semanticভাবে index করে এবং **LangChain + Ollama embeddings** ব্যবহার করে প্রশ্নের উত্তর তৈরি করে।  

---

## Features

- ✅ PDF আপলোড  
- ✅ প্রতিটি PDF এর জন্য **unique UUID** generate  
- ✅ Multi PDF support  
- ✅ FAISS vector store ব্যবহার করে **semantic search**  
- ✅ Chat with PDF content  
- ✅ Chat history save in database  
- ✅ REST API via Django REST Framework  
- ✅ Auth-optional (পরবর্তীতে JWT সহজে integrate করা যাবে)  

---

## Tech Stack

- **Backend:** Django 5.x, Django REST Framework  
- **AI / NLP:** LangChain, Ollama Embeddings, ChatGroq  
- **Vector Database:** FAISS (local)  
- **Database:** SQLite (development), PostgreSQL (recommended for production)  
- **Environment Variables:** `.env` file (OpenAI API key, Django SECRET_KEY)  

---
