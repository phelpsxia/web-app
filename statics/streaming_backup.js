function initMap() {
var map = new BMap.Map("map");          // 创建地图实例
var point = new BMap.Point(116.33696,40.002722);  // 创建点坐标
map.centerAndZoom(point, 11);
map.addControl(new BMap.NavigationControl());
map.addControl(new BMap.ScaleControl());  
}


var myVar = setInterval(function(){ myTimer() }, 1000);
 
function myTimer() {
    var d = new Date();
    var t = d.toLocaleTimeString();
    document.getElementById("date").innerHTML = t;
    video_pic.src = null
    video_pic.src = '../statics/temp_img/temp.jpg'
}