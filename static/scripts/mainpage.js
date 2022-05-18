const uploadedImg = document.getElementById("CBMI_Input");

uploadedImg.addEventListener("change", handleFiles, false);
function handleFiles() {
    const fileList = this.files;
    console.log(fileList)
}