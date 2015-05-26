    var m = "0";//分钟
    var s = "0";//秒
     function startTime()
    {
        //进入比赛界面是载入该函数
    s=checkTime(s);//如果秒数小于十就在前面补0
    document.getElementById('timer').innerHTML=m+":"+s;//在网页上显示所用时间
    t=setTimeout(function(){
        s++;
        if(s>=60)
        {
        s = 0;
        m++;
        }
        if(m >= 25)//如果超出规定时间
        {
        clearTimeout(t);
        alert("时间到");
        $.get("/end/25/0/");//向服务器提交时间数据
        }
        startTime();
        },1000);//每隔一秒执行一次该函数
    }

    function checkTime(i)
    {
    if (i<10)
      {
      i="0" + i;
      }
    return i;
    }//小于十就在前面补0
    function check_answer(ans,id)
    {//判断答案正误
        var xmlhttp;
        if(ans.length==0)//如果输入空字符串
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
        if(xmlhttp.readyState==4&&xmlhttp.status==200)//如果服务器响应成功且状态码为4
        {
            obj = JSON.parse(xmlhttp.responseText);
        if(obj.flag == 1){//如果flag为1,即答案正确,显示对钩
            document.getElementsByClassName("yes")[id].style.visibility="visible";
            document.getElementsByClassName("no")[id].style.visibility="hidden";
            //题目答对后无法修改输入框了
            document.getElementsByName("ans")[id].disabled=true;
        }
        else{//如果答案错误,显示叉
            document.getElementsByClassName("yes")[id].style.visibility="hidden";
            document.getElementsByClassName("no")[id].style.visibility="visible";
        }
        }

        }
        xmlhttp.open("POST","/verify/"+ans+"/"+id+"/",true);//向服务器提交答案和题目id
        xmlhttp.send();
    }
    //function begin()
    //{
    //alert("比赛开始");
    //begin_time = getTime();
    //}
    //选中输入框会改变输入框的颜色
    function change_color(x)
    {x.style.background="#FFE4C4";}
//页面加载完成后给每道题标上id
    function add_id()
    {
        for(var i=0;i<25;i++)
            document.getElementsByName("ans")[i].id=String(i);
    }
