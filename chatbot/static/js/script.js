$(document).ready(function(){
    $("#sub").click(function(){
        var name = $("#Rname").val();
        var email = $("#em").val();
        var password = $("#pass").val();
        var contact = $("#con").val();
        var course = $("#cou").val();
        var adm = $("#adm").val()
        if (name==""){
            alert("Please Enter Name...")
            return false;
        }
        if (email==""){
            alert("Please Enter Email...")
            return false;
        }
        var emailPattern = /^[a-zA-Z0-9._-]+@gmail\.com$/;
        if (!emailPattern.test(email)) {
            alert("Please Enter a Valid Gmail Address...");
            return false;
        }
        if (contact==""){
            alert("Please Enter Contact...")
            return false;
        }
        if (contact.length < 10) {
            alert("Contact Number should have at least 10 digits...");
            return false;
        }
        if (contact.length > 10) {
            alert("Contact Number should have only 10 digits...");
            return false;
        }
        if (password==""){
            alert("Please Enter Password...")
            return false;
        }
        if (course==""){
            alert("Please Enter Course...")
            return false;
        }
        if (adm==""){
            alert("Please Enter Admission Number...")
            return false;
        }
        var admPattern = /^\d+$/;
        if (!admPattern.test(adm)){
            alert("Admission Number should contain only digits...");
            return false;
        }
    })
})
$(document).ready(function(){
    $("#sub1").click(function(){
        var email = $("#em").val();
        var password = $("#pass").val();
        if (email==""){
            alert("Please Enter Email...")
            return false;
        }
        var emailPattern = /^[a-zA-Z0-9._-]+@gmail\.com$/;
        if (!emailPattern.test(email)) {
            alert("Please Enter a Valid Gmail Address...");
            return false;
        }
        if (password==""){
            alert("Please Enter Password...")
            return false;
        }
    })
})
$(document).ready(function(){
    $("#sub2").click(function(){
        var subject = $("#su").val();
        var message = $("#mes").val();
        if (subject==""){
            alert("Please Enter Subject...")
            return false;
        }
        if (message==""){
            alert("Please Enter Message...")
            return false;
        }
    })
})
