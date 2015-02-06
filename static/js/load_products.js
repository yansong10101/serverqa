/**
 * Created by yansong on 1/31/2015.
 */

$.getScript('js/jquery-1.11.1.min.js', function(){
    alert("load success !");
});

var host = window.location.origin;
var product_lite = $('<div class="col-lg-4"><a><img class="img-thumbnail" alt="Generic placeholder image" style="width: 320px; height: 350px;" /></a></div>');
var image_dir = host + "/static/products/";
var container = $(".row");

$("#btn").on('click', function(){

    clearAll();

    $.ajax({
    type: "GET",
    url: host + "/api/products/?format=json",
    dataType: "json"
    }).success(function(data, textStatus, jqXHR){

        var product_list = data.results;

        $.each(product_list, function(i, item){
            var elem = product_lite.clone();
            elem.children('a').eq(0).attr('href', item.url);
            elem.find('img').attr('src', image_dir + item.product_code + "/main.jpg");
            container.append(elem);
        });


    }).fail(function(jqXHR, textStatus){
        alert('Request Failed');
    });
});

function clearAll(){
    container.empty()
}




//$(document).ready(function(){
//
//    $("#btn").on('click', function(){
//        $.ajax({
//        type: "GET",
//        url: host + "/api/products/?format=json",
//        dataType: "json"
//        }).success(function(data, textStatus, jqXHR){
//            $.each(data.results, function(i, item){
//                var elem = $(".product_list").clone();
//                elem.children('p').eq(0).html(item.product_name);
//                elem.children('p').eq(1).html(item.product_code);
//                $("#product_result").append(elem);
//            });
//        }).fail(function(jqXHR, textStatus){
//            console.log(host);
//            alert('Request Failed');
//        });
//    });
//
//});