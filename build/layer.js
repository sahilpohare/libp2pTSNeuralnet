"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Layer = void 0;
var mathjs_1 = __importStar(require("mathjs"));
var events_1 = require("events");
var Layer = /** @class */ (function (_super) {
    __extends(Layer, _super);
    function Layer(noOfNeurons) {
        var _this = _super.call(this) || this;
        _this.activations = mathjs_1.matrix(mathjs_1.default.ones(noOfNeurons));
        _this.weights = mathjs_1.matrix([]);
        return _this;
    }
    Layer.prototype.connectLayer = function (inputShape) {
        this.weights = mathjs_1.matrix();
        this.weights.resize([]);
    };
    Layer.prototype.activateLayer = function (input) {
        console.log('layerActivated');
        this.emit('activated');
    };
    return Layer;
}(events_1.EventEmitter));
exports.Layer = Layer;
