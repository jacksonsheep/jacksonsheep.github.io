function server(){
    var http = require('http'); // package add to project
    http.createServer(function (request, response) { // callback func
        response.writeHead(200, {'Content-Type': 'text/plain'});
        // 发送响应数据 "Hello World"
        response.end('Hello World\n');
    }).listen(8888);
    console.log('Server running at http://127.0.0.1:8888/');
}
function callback(){
    var fs = require("fs");
    fs.readFile('input', function (err, data) {
        if (err) return console.error(err);
        console.log(data.toString());
    });
    console.log("程序执行结束!");
}
function event(){
    var events = require('events');
    // 创建 eventEmitter 对象
    var eventEmitter = new events.EventEmitter();
    // 创建事件处理程序
    var connectHandler = function connected() {
        console.log('连接成功。');
       // 触发 data_received 事件
       setTimeout(function(){
           eventEmitter.emit('data_received', "tom","jerry");
       }, 1000); // 等待1s触发
    }
    // 绑定 connection 事件处理程序
    eventEmitter.on('connection', connectHandler);
    // 使用匿名函数绑定 data_received 事件
    eventEmitter.on('data_received', function(args1, args2){
        console.log('数据接收成功。', args1, args2);
    });
    // 触发 connection 事件
    eventEmitter.emit('connection');
    console.log("程序执行完毕。");
}
function eventEmixtter(){
    var events = require('events');
    var eventEmitter = new events.EventEmitter();
    // 监听器 #1
    var listener1 = function listener1() {
        console.log('监听器 listener1 执行。');
    }
    // 监听器 #2
    var listener2 = function listener2() {
        console.log('监听器 listener2 执行。');
    }
    // 绑定 connection 事件，处理函数为 listener1 
    eventEmitter.addListener('connection', listener1);
    // 绑定 connection 事件，处理函数为 listener2
    eventEmitter.on('connection', listener2);
    var eventListeners = eventEmitter.listenerCount('connection');
    console.log(eventListeners + " 个监听器监听连接事件。");

    // 处理 connection 事件 
    eventEmitter.emit('connection');

    // 移除监绑定的 listener1 函数
    eventEmitter.removeListener('connection', listener1);
    console.log("listener1 不再受监听。");
    // 触发连接事件
    eventEmitter.emit('connection');
    eventListeners = eventEmitter.listenerCount('connection');
    console.log(eventListeners + " 个监听器监听连接事件。");
    console.log("程序执行完毕。");
}
callback();
event();
server();
