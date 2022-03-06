//
//  ViewController.swift
//  HelloWord
//
//  Created by Sean on 2016/11/16.
//  Copyright © 2016年 Sean. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {
    
    let adviceList = [
        "Yes",
        "No",
        "Ray says 'do it!'",
        "Maybe",
        "Try again later",
        "How can I know?",
        "Totally",
        "Never",
        ]
    @IBOutlet weak var nameTextField: NSTextField!
    @IBOutlet weak var welcomeLabel: NSTextField!
    @IBOutlet weak var BallImageView: NSImageView!
    @IBOutlet weak var adviceLabel: NSTextField!
    @IBAction func handleWelcome(_ sender: Any) {
        welcomeLabel.stringValue = "Hello \(nameTextField.stringValue)!"
    }
    
    @IBAction func handleBallClick(_ sender: Any) {
        // 1:
        if(adviceLabel.isHidden) {
            // 2:
            //adviceLabel.isHidden = false
            //BallImageView.image = NSImage(named: "magic8ball")
            let advice = adviceList.randomElement
                adviceLabel.stringValue = advice!
                adviceLabel.isHidden = false
                BallImageView.image = NSImage(named: "magic8ball")
            
        } else {
            // 3:
            adviceLabel.isHidden = true
            BallImageView.image = NSImage(named: "8ball")
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        adviceLabel.isHidden = true
        BallImageView.image = NSImage(named:"8ball")
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}

extension Array {
    var randomElement: Element? {
        if count < 1 { return .none }
        let randomIndex = arc4random_uniform(UInt32(count))
        return self[Int(randomIndex)]
    }
}
