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
    var tbsource = "../statics/temp_img/";
 
    var objFSO =new ActiveXObject('Scripting.FileSystemObject');
 
    if(!objFSO.FolderExists(tbsource)){
 
        alert("<"+tbsource+">该文件夹路径不存在，或者路径不能含文件名！");
 
        objFSO = null;}
 
    var objFolder = objFSO.GetFolder(tbsource);
    
    var colFiles = new Enumerator(objFolder.Files);
    
 
    for (; !colFiles.atEnd(); colFiles.moveNext()){
 
        var objFile = colFiles.item();
        
        }
        
    video_pic.src = tbsource + objFile.Name;
}