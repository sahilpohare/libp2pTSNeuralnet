"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var socket_io_1 = __importDefault(require("socket.io"));
var layer_1 = require("./layer");
var mathjs_1 = __importDefault(require("mathjs"));
var OutputLayerSoc = socket_io_1.default().listen(3000);
var layer = new layer_1.Layer(2);
OutputLayerSoc.on('connection', function (socket) {
    console.log('input layer connected');
    layer.connectLayer(2);
    socket.on('input', function (input) {
        console.log(mathjs_1.default.max(mathjs_1.default.flatten(layer.activations)));
    });
});
