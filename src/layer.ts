import { Neuron } from "./neuron";
import math,{Matrix, matrix, size} from "mathjs";
import { EventEmitter } from "events";

export class Layer extends EventEmitter{ 
    public activations : Matrix;
    public weights : Matrix;

    constructor(noOfNeurons : number){
        super()
        this.activations = matrix(math.ones(noOfNeurons));
        this.weights = matrix([]);
    }

    connectLayer(inputShape : number){
        this.weights = matrix();
        this.weights.resize([])
    }

    activateLayer(input : Matrix){
        console.log('layerActivated');
        this.emit('activated');
    }
}