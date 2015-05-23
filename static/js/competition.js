    var m = "0";
    var s = "0";
    function gameover()
    {


    }
     function startTime()
    {
    // add a zero in front of numbers<10
    s=checkTime(s);
    //如果超过15分钟
    document.getElementById('timer').innerHTML=m+":"+s;
    t=setTimeout(function(){
        s++;
        if(s>=60)
        {
        s = 0;
        m++;
        }
        if(m >= 1)
        {
        clearTimeout(t);
        alert("时间到");
        $.get("/end/1/0/");
        }
        startTime();
        },1000);
    }

    function checkTime(i)
    {
    if (i<10)
      {
      i="0" + i;
      }
    return i;
    }
    function check_answer(ans,id)
    {
        var xmlhttp;
        if(ans.length==0)
            return;
        if(window.XMLHttpRequest)
        {//code for IE7+,etc
        xmlhttp = new XMLHttpRequest();
        }
        else
        {//code for IE6 IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange=function()
        {
        if(xmlhttp.readyState==4&&xmlhttp.status==200)
        {
            obj = JSON.parse(xmlhttp.responseText);
        if(obj.flag == 1){
            document.getElementsByClassName("yes")[id].style.visibility="visible";
            document.getElementsByClassName("no")[id].style.visibility="hidden";
            //题目答对后无法修改输入框了
            document.getElementsByName("ans")[id].disabled=true;
        }
        else{
            document.getElementsByClassName("yes")[id].style.visibility="hidden";
            document.getElementsByClassName("no")[id].style.visibility="visible";
        }
        }

        }
        xmlhttp.open("POST","/verify/"+ans+"/"+id+"/",true);
        xmlhttp.send();
    }
    function begin()
    {
    alert("比赛开始");
    begin_time = getTime();
    }
    function change_color(x)
    {x.style.background="#FFE4C4";}

    function add_id()
    {
        for(var i=0;i<25;i++)
            document.getElementsByName("ans")[i].id=String(i);
    }
