import io from 'socket.io';
import {Layer} from './layer'
import math, { Matrix } from 'mathjs';

const OutputLayerSoc = io().listen(3000);
const layer = new Layer (2);

OutputLayerSoc.on('connection',(socket)=>{
    console.log('input layer connected');
    socket.on('input',(input : Matrix)=>{
        layer.activateLayer(input);
        console.log(math.max(math.flatten(layer.activations)));
    })
})

