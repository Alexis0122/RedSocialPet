import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
    apiKey: "AIzaSyAVPIcvAhbIIyUnjY2IkwQoNom10vjaEDg",
    authDomain: "my-second-project-7473f.firebaseapp.com",
    projectId: "my-second-project-7473f",
    storageBucket: "my-second-project-7473f.appspot.com",
    messagingSenderId: "591499523312",
    appId: "1:591499523312:web:dc4e39d9b1562d97623e35",
    measurementId: "G-N7BWXD4NZT"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

export { app, auth, firestore, storage };