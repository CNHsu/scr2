//
//  calculateBrain.swift
//  Tcalculate
//
//  Created by Sean on 2016/11/20.
//  Copyright © 2016年 Sean. All rights reserved.
//

import Foundation



class calculateBrain
{
    private var accumulator: Double = 0.0
    func setOperand(operand: Double) {
        accumulator = operand
        print("setOperand:", String(accumulator))
        
    }
    
    private var operations: Dictionary<String,Operation> = [
        "π" : Operation.Constant(M_PI),
        "e" : Operation.Constant(M_E),
        "√" : Operation.UnaryOperation(sqrt),
        "cos":Operation.UnaryOperation(cos),
        "×" : Operation.BinaryOperation({$0 * $1}),
        "−" : Operation.BinaryOperation({$0 - $1}),
        "÷" : Operation.BinaryOperation({$0 / $1}),
        "+" : Operation.BinaryOperation({$0 + $1}),
        "." : Operation.BinaryOperation({$0 + $1/10}),
        "c" : Operation.Constant(0),
        "=" : Operation.Equals
    ]
    
    private enum Operation {
        case Constant(Double)
        case UnaryOperation((Double)->Double)
        case BinaryOperation((Double,Double)->Double)
        case Equals
    }
    
    func performOperation(symbol: String){
        if let operation = operations[symbol] {
            switch operation {
            case .Constant(let value): accumulator = value
            case .UnaryOperation(let foo): accumulator = foo(accumulator)
            case .BinaryOperation(let foo):
                executePendingBinaryOperation()
                pending = pendingBinaryOperationInfo(binaryFunction: foo, firstOperand:accumulator)
            case .Equals : executePendingBinaryOperation()
            }
        }
        
    }
    
    private func executePendingBinaryOperation()
    {
        if pending != nil {
            print(accumulator, pending!.firstOperand)
            accumulator = pending!.binaryFunction(pending!.firstOperand, accumulator)
            pending = nil
        }
    
    }
    
    private var pending: pendingBinaryOperationInfo?
    
    
    private struct pendingBinaryOperationInfo {
        var binaryFunction: (Double,Double) -> Double
        var firstOperand: Double
    }
    
    var result: Double {
        get {
            return accumulator
        }
    }
}
