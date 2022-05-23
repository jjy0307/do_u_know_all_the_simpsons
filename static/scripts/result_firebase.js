// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-analytics.js";
import { getStorage, ref, uploadBytes,getDownloadURL } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-storage.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCEOZvCtL6YJF7NDOJo01SMk1-BfFUYF4M",
  authDomain: "rs-object-recognition.firebaseapp.com",
  projectId: "rs-object-recognition",
  storageBucket: "rs-object-recognition.appspot.com",
  messagingSenderId: "95927745266",
  appId: "1:95927745266:web:9ce88f8d96b5c338846e6b",
  measurementId: "G-BQY2YXKKCP",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const storage = getStorage(app);

window.addEventListener('DOMContentLoaded', function ()
    {
        getCookie();
    }
)

function getCookie() {
    const result = document.cookie.split(';')[1].split('result=')[1]
    const img = document.cookie.split(';')[2].split('img_name=')[1]
    const changeText = document.getElementById("result-text");
    changeText.innerText = "분류 결과 " + result + "로 판명되었습니다"
    getDownloadURL(ref(storage, img))
        .then((url) => {
          const getImg = document.getElementById("result-img");
          getImg.src = url;
        })
        .catch((error) => {
          // Handle any errors
        });
}



