"use strict"
import { Request } from "./xhr.js";
import {Selector}  from "./xhr.js";





const sound = document.getElementById('audio');
var form = Selector("#form");

/* FUNCTIONS APP ICONS CLICK*/
Selector("#brute-force").onclick=()=>{
 sound.src="sounds/zoom.mp3";
  sound.play();
  form.style.display = "block";
  Selector("#hidden-data").value="brute-force";
}
Selector("#facebook").onclick=()=>{
 sound.src="sounds/zoom.mp3";
  sound.play();
  form.style.display = "block";
  Selector("#hidden-data").value="facebook";
}
Selector("#cross").onclick=()=>{
  form.style.display = "none";
}



/*   SEND DATA    */
Selector("#btn").onclick=(e)=>{
 e.preventDefault();
var hiddenData = Selector("#hidden-data").value;
 var input = Selector("#idName").value;
if( input == ""){
  alert("Please Enter Login Info");
} else {
  switch (hiddenData) {
    case 'brute-force':
      //call brute-force 
      break;
    case 'facebook':
      // call Facebook 
    Request.post({
    url: "/search-victims",
    body: {
      input_value : input 
    },
    getAction: (data) => {
      console.log(data);
    },
  });
    default:
      // code
  }
}
}


setTimeout(()=> {
  sound.src="sounds/zoom.mp3";
  sound.play();
  Selector(".preloader").style.display="none";
  Selector("#table").style.display="block";
}, 13000);

window.onload=()=>{
sound.play();
}
document.addEventListener("touchstart",(e)=>{
  if(e.touches[0]){
  sound.src="sounds/click.wav";
  sound.play();
  } 
});


