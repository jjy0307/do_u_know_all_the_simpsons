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

// 변수 선언
let DragImg = null;
let InputImg = null;


// 인풋으로 이미지 넘기기
const uploadedImg = document.getElementById("CBMI_Input");
uploadedImg.addEventListener("change", handleFiles, false);
function handleFiles() {
  const fileList = this.files;
  if(fileList !== undefined) {
    for (let i = 0; i < fileList.length; i++) {
      const file = fileList[i];
      InputImg = file;

      let drop = document.getElementById('DropImg');
      drop.src = window.URL.createObjectURL(file)
      let span = document.getElementById('IfDropInvisible');
      let input = document.getElementById("CBMI_Input");
      span.style.display = "none"
      input.style.display = "none"
    }
  }
}

//이미지 끌어서 넣기
let drop = document.getElementById('DropImg');
drop.addEventListener("dragover", dragOver);
drop.addEventListener("dragleave", dragOver);
drop.addEventListener("drop", uploadfiles);

function dragOver(e) {
  e.stopPropagation();
  e.preventDefault();

  if (e.type == "dragover") {
        e.target.style.backgroundColor = "blue"
    } else {
        e.target.style.backgroundColor = "transparent"
    }
}

function uploadfiles(e) {
  e.stopPropagation();
  e.preventDefault();
  dragOver(e);

  let files = e.target.files || e.dataTransfer.files;
  if (files.length > 1) {
      alert('하나만 올려라.');
  }

  if (files[0].type.match(/image.*/)) {
    DragImg = files[0]
    drop.src = window.URL.createObjectURL(files[0])
    let span = document.getElementById('IfDropInvisible');
    let input = document.getElementById("CBMI_Input");
    span.style.display = "none"
    input.style.display = "none"
  } else {
      alert('이미지가 아닙니다.');
  }
}

//이미지 firebase에 보내기
const SearchButton = document.getElementById("Search-Image");
SearchButton.addEventListener("click", searchImage);
function searchImage() {
  let file = null;
  if (DragImg !== null) {
    file = DragImg
  } else if (InputImg !== null) {
    file = InputImg
  }
  const fileName = file.lastModified.toString() + file.name;
  console.log(fileName)
  const storageRef = ref(storage, fileName);
  uploadBytes(storageRef, file)
        .then((snapshot) => {
    console.log('Uploaded a blob or file!');
  });

  let formData = new FormData();
  formData.append("Img_Path", fileName)
  formData.append("haha", "sexy")
  axios.post('/recognize_img', formData, {
      header: {
          "Content-Type": "multipart/form-data",
      }
    })
      .then(function (response) {
        console.log(response)
        if (response['result'] == 'success') {
          alert("Your picture confirmed as " + response['rec_result'])
        }
    }).catch(function (error) {
    })
}



//이미지 불러오기
// const testButton = document.getElementById("Search-Image");
// testButton.addEventListener("click", checkImage);
// function checkImage() {
//   const fileName = "1636813959771logo no hat.jpg";
//   getDownloadURL(ref(storage, fileName))
//     .then((url) => {
//       console.log(url);
//       const uploadedImg = document.getElementById("Test-Image");
//       uploadedImg.src = url;
//     })
//     .catch((error) => {
//       // Handle any errors
//     });
// }