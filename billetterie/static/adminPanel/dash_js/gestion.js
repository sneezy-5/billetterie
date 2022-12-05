const popup = document.getElementById('popup');
const popupedit = document.getElementById('popupedit');


function popupToggle(){
    popup.classList.toggle('active');
    popupedit.classList.remove('active');
}


function popupToggleEdit(){
    popupedit.classList.toggle('active');
    popup.classList.remove('active');
}

window.onscroll = () =>{
    popup.classList.remove('active');
    popupedit.classList.remove('active');
}
  