html_code = """
<!DOCTYPE html>
<html>
<head>
	<title>Network Graph Creator</title>
	<style>
		#graph {
			position: relative;
			width: 500px;
			height: 500px;
			border: 1px solid black;
		}
		.node {
			position: absolute;
			width: 30px;
			height: 30px;
			border-radius: 50%;
			background-color: red;
			text-align: center;
			line-height: 30px;
			cursor: pointer;
		}
		#save {
			margin-top: 20px;
			padding: 10px;
			background-color: #4CAF50;
			color: white;
			border: none;
			cursor: pointer;
		}
	</style>
</head>
<body>
	<h1>Network Graph Creator</h1>
	<div id="graph"></div>
	<button id="save">Save</button>
	<script>
	var nodes = {};

function createNode(x, y) {
    var nodeName = prompt('Enter name for node:');
    if (!nodeName) {
        return;
    }
    var node = document.createElement('div');
    node.className = 'node';
    node.style.left = x + 'px';
    node.style.top = y + 'px';
    node.innerText = nodeName;
    
    node.addEventListener('mousedown', function(event) {
        event.stopPropagation();
        var node = event.target;
        var startX = event.clientX - node.offsetLeft;
        var startY = event.clientY - node.offsetTop;
        document.addEventListener('mousemove', moveNode);
        document.addEventListener('mouseup', releaseNode);
        function moveNode(event) {
            node.style.left = event.clientX - startX + 'px';
            node.style.top = event.clientY - startY + 'px';
        }
        function releaseNode(event) {
            document.removeEventListener('mousemove', moveNode);
            document.removeEventListener('mouseup', releaseNode);
 
        }
    });
    document.getElementById('graph').appendChild(node);
    nodes[nodeName] = { x: x, y: y };
 
}

function saveNodes() {
    var data = {};
    var graph = document.getElementById('graph');
    Array.from(graph.children).forEach(function(node) {
        var name = node.innerText;
        var x = node.offsetLeft;
        var y = node.offsetTop;
        data[name] = { x: x, y: y };
    });
   
}
document.getElementById('save').addEventListener('click', function() {
        var filename = prompt('Enter file name:');
        if (filename) {
            var json = JSON.stringify(nodes);
            var blob = new Blob([json], { type: 'application/json' });
            var url = URL.createObjectURL(blob);
            var a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }
    });
document.getElementById('graph').addEventListener('mousedown', function(event) {
    createNode(event.clientX - event.target.offsetLeft, event.clientY - event.target.offsetTop);

});
	</script>
</body>
</html>

"""