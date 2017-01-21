function formatDate(date) {

  var yyyy = date.getFullYear().toString();
  var mm = (date.getMonth()+1).toString(); // getMonth() is zero-based
  var dd  = date.getDate().toString();
  var data = (dd[1]?dd:"0"+dd[0]) + "/" + (mm[1]?mm:"0"+mm[0]) + "/" + yyyy;

  return data;

}

var calendarOptions = {
  language: "pt-BR",
  todayHighlight: true,
  datas: [],
  beforeShowDay: function(date) {
    date.setHours(date.getHours()+1);
    var data = formatDate(date);

    if(this.datas[data])
      return {
        "enabled": true,
        "tooltip": this.datas[data].title
      };
    else
      return {
        "enabled": false,
        "tooltip": "Não há sugestões de músicas para este dia ainda."
      };
  }
};

$(document).ready(function() {

  $.get( "/datas.json", function( datas ) {

    calendarOptions.datas = datas;

    var onClick = function(e){
      var date = e.date;
      date.setHours(date.getHours()+1);
      var data = formatDate(date);
      var url = calendarOptions.datas[data].url;
      //window.open(url);
      document.location = url;
    }

    $('#calendar-navbar').datepicker(calendarOptions).on("changeDate",onClick);
    $('#calendar').datepicker(calendarOptions).on("changeDate",onClick);
    $('#calendar-footer').datepicker(calendarOptions).on("changeDate",onClick);

  });

});
