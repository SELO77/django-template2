/* Project specific Javascript goes here. */
$('#menu-area').click(function(){
  $('#navbar').toggleClass('is-active');
});

$(function () {
  tab('#tab', 0);
});

function tab(e, num){
  var num = num || 0;
  var menu = $(e).children();
  var con = $(e+'-con').children();
  var select = $(menu).eq(num);
  var i = num;

  select.addClass('is-active');
  con.eq(num).show();

  menu.click(function(){
    if(select!==null){
      select.removeClass("is-active");
      con.eq(i).hide();
    }
    select = $(this);
    i = $(this).index();
    select.addClass('is-active');
    con.eq(i).show();
  });
}
