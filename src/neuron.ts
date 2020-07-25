import math from 'math.js';
import * as sciMat from 'mathjs';

export class Neuron {
   public weights : sciMat.Matrix;
   public activation : sciMat.Matrix;

   constructor(inputshape){
       this.activation = sciMat.matrix([0]);
       this.weights = sciMat.matrix([...Array(inputshape).fill(Math.random())]);
   }

   activate(input : sciMat.Matrix){
      this.activation = sciMat.multiply(sciMat.transpose(this.weights),input);
   }
}