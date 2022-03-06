//
//  ViewController.swift
//  test
//
//  Created by Sean on 2017/3/4.
//  Copyright © 2017年 Sean. All rights reserved.
//

import Cocoa

///

protocol ExampleProtocol {
    var simpleDescription: String { get }
    mutating func adjust()
}

class SimpleClass: ExampleProtocol {
    var simpleDescription: String = "A very simple class."
    var anotherProperty: Int = 69105
    func adjust() {
        simpleDescription += "  Now 100% adjusted."
    }
}

var a = SimpleClass()
//a.adjust()
let aDescription = a.simpleDescription

///
class ViewController: NSViewController {

    @IBOutlet weak var math1: NSTextField!
    @IBOutlet weak var show: NSTextField!
    @IBAction func change(_ sender: Any) {
     
        show.stringValue = "\(math1.stringValue) + \(math2.stringValue)"
        let tt = Double(math1.stringValue)! * Double(math2.stringValue)!
        //show.stringValue = String(tt)
        a.adjust()
        show.stringValue = aDescription
    
    }
    @IBOutlet weak var math2: NSTextField!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}


