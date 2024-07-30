import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
    apiKey: "AIzaSyBZP9kakDaRO-BNRA0c-13Xiv3BTg--jSE",
    authDomain: "petstagram2-6d194.firebaseapp.com",
    projectId: "petstagram2-6d194",
    storageBucket: "petstagram2-6d194.appspot.com",
    messagingSenderId: "729626404315",
    appId: "1:729626404315:web:76acf95e5c6a4d9f18f3fe",
    measurementId: "G-B5JTN6SCC2"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

export { app, auth, firestore, storage };