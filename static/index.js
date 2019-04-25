layui.use(['element', 'util', 'laydate', 'layer', 'form'], function () {
    var $ = layui.jquery
        , util = layui.util
        , laydate = layui.laydate
        , layer = layui.layer
        , form = layui.form
        , element = layui.element;
        
    form.verify({
            check_length: function(value){
                if(value.length < 1){
                    return '链不能为空！';
              }
            },
            
          });

    let check_link = (str) => {
        var a = str.split('/');
        return a[a.length-1];
    };

    let datefilter = (datatime) => {
        if (datatime) {
            d = new Date(datatime);
            let year = d.getFullYear();
            let month = (d.getMonth()) + 1 < 10 ? "0" + (d.getMonth() + 1) : "" + (d.getMonth() + 1);
            let day = d.getDate() < 10 ? "0" + d.getDate() : "" + d.getDate();
            let hour = d.getHours() < 10 ? "0" + d.getHours() : "" + d.getHours();
            let minutes = d.getMinutes() < 10 ? "0" + d.getMinutes() : "" + d.getMinutes();
            let seconds = d.getSeconds() < 10 ? "0" + d.getSeconds() : "" + d.getSeconds();
            return year + "-" + month + "-" + day+ " " + hour + ":" + minutes + ":" + seconds;
        } else {
            return "";
        }
    }      

    form.on('submit(long2short)', function (data) {
        data.field.url_org = data.field.url_org.trim()
        if (data.field.url_org==""){
            layer.msg("不能为空！")
            return false;
        }
        $.ajax({
            url: "/p"
            , data: data.field
            , type: "post"
            , dataType: "json"
            , success: function (data) {
                console.log (data);
                if (data['status']==-1 || data['status']==0) {
                    layer.open({
                        type: 1
                        ,title: false //不显示标题栏
                        ,closeBtn: false
                        ,area: '400px;'
                        ,shade: 0.8
                        ,id: 'LAY_layuipro1' 
                        ,btn: ['OK']
                        ,btnAlign: 'c'
                        ,moveType: 1 
                        ,content: '<div style="padding: 50px; line-height: 22px; background-color: #393D49; color: #fff; font-weight: 300;">'+'短链接：<a style="color:pink" href="'+location.href+'s/'+data['url_short']+'">'+location.href+'s/'+data['url_short'] +'</a></br>创建时间：'+datefilter(data['generate_time']) +'</div>'
                      });
                    return;
                }
            },
            error: function (err) {
                layer.msg("发生错误,刷新后重试")
            }
        });
        return false;
    });
    

    form.on('submit(short2long)', function (data) {
        data.field.url_short = data.field.url_short.trim()
        if (data.field.url_short==""){
            layer.msg("不能为空！")
            return false;
        }
        data.field.url_short = check_link(data.field.url_short)
        console.log(data)
        $.ajax({
            url: "/info/"+data.field.url_short
            , data: data.field
            , type: "get"
            , dataType: "json"
            , success: function (data) {
                console.log (data);
                if (data['status']==-2) {
                    layer.msg("该短链不存在！");
                }
                if (data['status']!=-2) {
                    layer.open({
                        type: 1
                        ,title: false //不显示标题栏
                        ,closeBtn: false
                        ,area: '400px;'
                        ,shade: 0.8
                        ,id: 'LAY_layuipro' //设定一个id，防止重复弹出
                        ,btn: ['OK']
                        ,btnAlign: 'c'
                        ,moveType: 1 
                        ,content: '<div style="padding: 50px; line-height: 22px; background-color: #393D49; color: #fff; font-weight: 300;">'+'短链接：<a style="color:pink" href="'+location.href+'s/'+data['url_short']+'">'+location.href+'s/'+data['url_short'] +'</a></br>'+'原长链接：<a style="color:pink" href="http://'+data['url_org']+'">'+data['url_org'] +'</a></br>创建时间：'+datefilter(data['generate_time']) +'</div>'
                      });
                    return;
                }
            },
            error: function (err) {
                layer.msg("发生错误,刷新后重试")
            }
        });
        return false;
    });
    
    form.on('submit(querytimes)', function (data) {
        data.field.url_short = data.field.url_short.trim()
        if (data.field.url_short==""){
            layer.msg("不能为空！")
            return false;
        }
        data.field.url_short = check_link(data.field.url_short)
        console.log(data)
        $.ajax({
            url: "/info/"+data.field.url_short
            , type: "get"
            , dataType: "json"
            , success: function (data) {
                console.log (data);
                if (data['status']==-2) {
                    layer.msg("该短链不存在！");
                }
                if (data['status']!=-2) {
                    layer.open({
                        type: 1
                        ,title: false //不显示标题栏
                        ,closeBtn: false
                        ,area: '400px;'
                        ,shade: 0.8
                        ,id: 'LAY_layuipro2' //设定一个id，防止重复弹出
                        ,btn: ['OK']
                        ,btnAlign: 'c'
                        ,moveType: 1 
                        ,content: '<div style="padding: 50px; line-height: 22px; background-color: #393D49; color: #fff; font-weight: 300;">'+'访问共计：'+ data['times']+'次</br>'+'原长链接：<a style="color:pink" href="http://'+data['url_org']+'">'+data['url_org'] +'</a></br>创建时间：'+datefilter(data['generate_time']) +'</div>'
                      });
                    return;
                }
            },
            error: function (err) {
                layer.msg("发生错误,刷新后重试")
            }
        });
        return false;
    });

    form.on('submit(custum)', function (data) {
        data.field.url_short = data.field.url_short.trim()
        if (data.field.url_short==""){
            layer.msg("不能为空！")
            return false;
        }
        data.field.url_org = data.field.url_org.trim()
        if (data.field.url_org==""){
            layer.msg("不能为空！")
            return false;
        }
        $.ajax({
            url: "/p"
            , data: data.field
            , type: "post"
            , dataType: "json"
            , success: function (data) {
                console.log (data);
                if (data['status']==-3) {
                    layer.msg("该短链已存在，请换一个试试！");
                }
                if (data['status']==-1 || data['status']==0) {
                    layer.open({
                        type: 1
                        ,title: false //不显示标题栏
                        ,closeBtn: false
                        ,area: '400px;'
                        ,shade: 0.8
                        ,id: 'LAY_layuipro1' 
                        ,btn: ['OK']
                        ,btnAlign: 'c'
                        ,moveType: 1 
                        ,content: '<div style="padding: 50px; line-height: 22px; background-color: #393D49; color: #fff; font-weight: 300;">'+'长链接：'+data['url_org'] +'</br>'+'短链接：<a style="color:pink" href="'+location.href+'s/'+data['url_short']+'">'+location.href+'s/'+data['url_short'] +'</a></br>创建时间：'+datefilter(data['generate_time']) +'</div>'
                      });
                    return;
                }
            },
            error: function (err) {
                layer.msg("发生错误,刷新后重试")
            }
        });
        return false;
    });
    
})


