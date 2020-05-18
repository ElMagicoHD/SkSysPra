var e;
e = document.getElementById("textfeld");
if(e){
e.addEventListener("keyup", charcounter, false);
}

function charcounter(){
    t = document.getElementById("textfeld");
    start = 160;
    remainingchar = 160 - t.value.length;

    document.getElementById("remaining").innerHTML = remainingchar + " characters left";
}

function strikethrough(x){
    let a = 't' + x;
    document.getElementById(a).style.textDecoration = "line-through";
}

function restoring(x){
    let a = 't' + x;
    document.getElementById(a).style.textDecoration = "none";
}