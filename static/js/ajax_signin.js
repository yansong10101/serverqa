/**
 * Created by yansong on 1/19/2015.
 */


function signinAuth(){
    $.ajax({
        type: "POST",
        url: "/login/",
        dataType: "json"
    }).success()
}