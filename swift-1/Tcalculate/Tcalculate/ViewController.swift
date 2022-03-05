//
//  ViewController.swift
//  Tcalculate
//
//  Created by Sean on 2016/11/20.
//  Copyright © 2016年 Sean. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    private var userIsInTheMiddleTyping = false
    
    @IBOutlet private weak var display: UILabel!
    @IBAction private func touchDigit(sender: UIButton) {
        
        let digit = sender.currentTitle!
        
        if userIsInTheMiddleTyping{
            let textcurrentDisplay = display.text!
            display.text = textcurrentDisplay + digit
        } else {
            userIsInTheMiddleTyping = true
            display.text = digit
            
        }
        
    }
    
   
    
    private var displayValue: Double {
        get {
            //print("get")
            return Double(display.text!)!
        }
        set {
            display.text = String(newValue)
            //print("set")
        }
    }
    
    private var brain = calculateBrain()
    
    
    
    @IBAction private func performOperation(_ sender: UIButton) {
        if userIsInTheMiddleTyping {
            brain.setOperand(operand: displayValue)
            print("setOperand")
            userIsInTheMiddleTyping = false
            
        }
        if let mathmaticSymbol = sender.currentTitle {
            print("performOperation")
            brain.performOperation(symbol: mathmaticSymbol)
        }
        displayValue = brain.result
        
    }
  
   
    
    
}
