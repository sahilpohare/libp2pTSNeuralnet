"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var mathjs_1 = require("mathjs");
var socket_io_client_1 = __importDefault(require("socket.io-client"));
var readline_1 = __importDefault(require("readline"));
var process_1 = require("process");
var soc = socket_io_client_1.default('localhost:3000');
soc.on('connect', function () {
    console.log('connected');
});
var rl = readline_1.default.createInterface({
    output: process_1.stdout,
    input: process_1.stdin
});
function question() {
    rl.question('Press Enter To first input', function (input1) {
        rl.question('Enter Second Input', function (input2) {
            soc.emit('input', mathjs_1.matrix([parseFloat(input1), parseFloat(input2)]));
        });
    });
}
