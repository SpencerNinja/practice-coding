//
//  ViewController.swift
//  Random Game Timer
//
//  Created by Spencer Hurd on 3/31/21.
//

import UIKit
import Foundation
import AVFoundation

class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var minTxtField: UITextField!
    @IBOutlet weak var maxTxtField: UITextField!
    @IBOutlet weak var timeWindow: UILabel!
    
    var timer: Timer?
    var secondsLeft = 0
    var alarmSound: AVAudioPlayer?
    let path = Bundle.main.path(forResource: "ninja_turtles_movie", ofType: "mp3")!
    lazy var url = URL(fileURLWithPath: path)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        minTxtField.delegate = self
        maxTxtField.delegate = self
        timeWindow.text = String(getRandomTime())
    }
    
    // Get random number between minimum and maximum
    func getRandomTime() -> Int {
        if let min = Int(minTxtField.text ?? ""), let max = Int(maxTxtField.text ?? "") {
            let randomNum = Int.random(in: min...max)
            return randomNum
        } else {
            return 0
        }
    }
    
    // start countdown on timer
    @objc func fireTimer() {
        secondsLeft -= 1
        timeWindow.text = String(secondsLeft)
        if secondsLeft <= 0 {
            timer?.invalidate()
            do {
                alarmSound = try AVAudioPlayer(contentsOf: url)
                alarmSound?.play()
            } catch {
                // unable to load file
            }
        }
    }
    
    // Start timer
    var timerActive = false
    @IBAction func startTimer(_ sender: UIButton) {
        if timerActive == false {
            timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(fireTimer), userInfo: nil, repeats: true)
            secondsLeft = getRandomTime()
            fireTimer()
            // Disable start button functionality
            timerActive = true
        }
    }
    
    // Pause and continue timer
    var isPaused = false
    @IBAction func pauseTimerTapped(_ sender: UIButton) {
        if self.isPaused == true {
            timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(fireTimer), userInfo: nil, repeats: true)
            fireTimer()
            self.isPaused = false
        } else {
            timer?.invalidate()
            self.isPaused = true
            timerActive = true
        }
    }
    
    // Stop timer
    @IBAction func stopTimer(_ sender: UIButton) {
        timer?.invalidate()
        timerActive = false
        alarmSound?.stop()
    }
    
    // Reset timer
    @IBAction func resetTimer(_ sender: UIButton) {
        timer?.invalidate()
        timerActive = false
        secondsLeft = 0
        timeWindow.text = String(secondsLeft)
        alarmSound?.stop()
    }
    
    // Only accept numbers 0-9 in textField
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        let invalidCharacters = CharacterSet(charactersIn: "0123456789").inverted
        return (string.rangeOfCharacter(from: invalidCharacters) == nil)
    }
}

// override paste so user can only use numbers
class PastelessTextField: UITextField {
    override func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool {
        return super.canPerformAction(action, withSender: sender) && (action == #selector(UIResponderStandardEditActions.cut) || action == #selector(UIResponderStandardEditActions.copy))
    }
} 



/*
 PSUEDO CODE ARCHITECTURE
 - create a var to initialize Timer
 - create a var to store time left on timer
 - link minimum textInput field to new var
 - link maximum textInput field to new var
 - link Outlet var to display seconds left
 - function = start timer
    - start timer
    - subtract one second
    - display seconds left
    - if seconds left <= minimum textInput
        - stop timer
 - function = pause timer
    - pause timer
 - function = stop timer
    - stop timer
 - function = reset timer
    - stop timer
    - time left = 0
 
 */

