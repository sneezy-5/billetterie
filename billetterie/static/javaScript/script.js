let navBar = document.querySelector('.navbar');
  document.querySelector('#menu_btn').onclick = () =>{
    document.querySelector('#menu_btn').classList.toggle('fa-times');
    navBar.classList.toggle('active');

}


window.onscroll = () =>{
  navBar.classList.remove('active');
  document.querySelector('#menu_btn').classList.remove('fa-times');
}



/************************************************/ 


const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});


/********************************************/


window.addEventListener('scroll', function(){
  const header =document.querySelector('header');
  header.classList.toggle("sticky", window.scrollY > 0 );
});

/*******************************************/
var swiper = new Swiper(".slide-content", {
  slidesPerView: 3,
  spaceBetween: 25,
  loop: true,
  centerSlide: 'true',
  fade: 'true',
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints:{
      0: {
          slidesPerView: 1,
      },
      520: {
          slidesPerView: 2,
      },
      950: {
          slidesPerView: 3,
      },
  },
});