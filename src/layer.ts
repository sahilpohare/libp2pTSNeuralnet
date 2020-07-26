import { Neuron } from "./neuron";
import math,{Matrix, matrix, size, multiply} from "mathjs";
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
        this.weights = matrix(math.ones(size(this.activations)[0],inputShape));
        this.weights.resize([size(this.activations)[0],inputShape]);
    }

    forward(input : Matrix){
        this.activations = math.map(multiply(this.weights,input),(val)=>this.sigmoid(val));
        this.emit('activated',this.activations);
    }

    sigmoid(val:number){
        return 1/(1 - Math.pow (math.e, val))
    }
}