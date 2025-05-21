var cube = document.querySelector('.cube');
var currentClass = "";

function changeSide(side) {
   var showClass = 'show-' + side;
   if ( currentClass ) {
       cube.classList.remove( currentClass );
   }
   cube.classList.add( showClass );
   currentClass = showClass;
}

document.getElementById('icon-fb').addEventListener('click', function() { changeSide("right"); ; });
document.getElementById('icon-ig').addEventListener('click', function() { changeSide("back"); });
document.getElementById('icon-linkedin').addEventListener('click', function() { changeSide("left"); });
document.getElementById('icon-whatsapp').addEventListener('click', function() { changeSide("top"); });
document.getElementById('icon-wechat').addEventListener('click', function() { changeSide("bottom"); });
document.getElementById('cube').addEventListener('click', function() { changeSide("front"); });

document.getElementById('icon-fb').addEventListener('mouseover', function() { changeSide("right"); ; });
document.getElementById('icon-ig').addEventListener('mouseover', function() { changeSide("back"); });
document.getElementById('icon-linkedin').addEventListener('mouseover', function() { changeSide("left"); });
document.getElementById('icon-whatsapp').addEventListener('mouseover', function() { changeSide("top"); });
document.getElementById('icon-wechat').addEventListener('mouseover', function() { changeSide("bottom"); });
document.getElementById('cube').addEventListener('mouseover', function() { changeSide("front"); });