
var tamFonteLetra = 16;

$('#remove-font-size-letra').on('click', function (e) {
  updateFontSize(--tamFonteLetra, 'div-letra');
});

$('#add-font-size-letra').on('click', function (e) {
  updateFontSize(++tamFonteLetra, 'div-letra');
});

$('#print-letra').on('click', function (e) {
  printPopup($('#titulo-musica').html(), '<div id="letra">'+$('#div-letra').html()+'</div>');
});

var tamFonteCifra = 13;

$('#remove-font-size-cifra').on('click', function (e) {
  updateFontSize(--tamFonteCifra, 'div-cifra');
});

$('#add-font-size-cifra').on('click', function (e) {
  updateFontSize(++tamFonteCifra, 'div-cifra');
});

$('#print-cifra').on('click', function (e) {
  printPopup($('#titulo-musica').html(), '<pre id="cifra">'+$('#div-cifra').html()+'</pre>');
});

$('#remove-meio-tom-cifra').on('click', function (e) {

});

$('#add-meio-tom-cifra').on('click', function (e) {

});

function printPopup(title, data)
{
    var mywindow = window.open('', title);
    mywindow.document.write('<html><head><title>'+title+' - Músicas para Missa</title>');
    mywindow.document.write('<style>');
    mywindow.document.write('#letra {'+
'            font-size: 20px;'+
'            background: white;'+
'            display: block;'+
'            padding-right: 85px;'+
'    }'+
'    #cifra {'+
'    	font-size: 18px;'+
'    	background: white;'+
'    	font-family: monospace;'+
'    	display: block;'+
'    	padding-right: 85px;'+
'    }'+
'    #cifra b {'+
'    	color: #FF0000;'+
'    	font-weight: bold;'+
'    }'+
'    img {'+
'        position: absolute;'+
'        width: 100%;'+
'        padding-top: 200px;'+
'        opacity: 0.1;'+
'        filter: alpha(opacity=10);'+
'    }'+
'    h2 {'+
'    	padding-right: 85px;'+
'    }</style>');
    mywindow.document.write('</head><body>');
    mywindow.document.write("<img src='"+document.location.origin+"/static/images/logo/logoMpM.png' />");
    mywindow.document.write('<h2>'+title+'</h2>');
    mywindow.document.write(data);
    mywindow.document.write('</body></html>');
    mywindow.document.close();
    mywindow.focus();
    setTimeout(function(){
      mywindow.print();
      mywindow.close();
    },100);
    return true;
}

function updateFontSize(size, element){
  document.getElementById(element).style.fontSize = size+"px";
  var ps = document.getElementById(element).getElementsByTagName("p")
  for (i = 0; i < ps.length; i++) {
    ps[i].style.fontSize = size+"px";
  }
}
