import {matrix } from "mathjs";

import io from 'socket.io-client';
import readline from 'readline';
import { stdout, stdin } from "process";
const soc = io('localhost:3000');

soc.on('connect',()=>{
    console.log('connected');
    question();
})

const rl = readline.createInterface({
    output : stdout,
    input : stdin
})

function question(){
    rl.question('Press Enter To first input',(input1)=>{
        rl.question('Enter Second Input', (input2)=>{
            soc.emit('input',matrix([parseFloat(input1),parseFloat(input2)]));
        })
    })
}