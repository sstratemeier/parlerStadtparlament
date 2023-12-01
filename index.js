// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.FIREBASE_API_KEY,
  authDomain: "demoproject-82b16.firebaseapp.com",
  databaseURL: "https://demoproject-82b16.firebaseio.com",
  projectId: "demoproject-82b16",
  storageBucket: "demoproject-82b16.appspot.com",
  messagingSenderId: "548211765397",
  appId: "1:548211765397:web:18657e33145f8b4b002b9c"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
