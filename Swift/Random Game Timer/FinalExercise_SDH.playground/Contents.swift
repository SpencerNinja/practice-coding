import UIKit

// You are creating a game. The game has a reward system that includes money, trophies and stars. Stars and trophies are awarded one at a time, but money can be added in any amount. Each user is able to track how much cash and how many trophies and stars they have. Create the reward system, and user. Then make at least two users, give them some rewards, and finally print each user along with their rewards. Make the grammar be proper based on how many items the user has.

// Use at least all of the following concepts in your code:
//   X   Enum (with and without associated values)
//   X   Iteration
//   X   Stored Properties
//   X   Computed Properties
//   X   Struct
//   X   Array
//   X   Switch
//   X   Tuple
//   X   Function
//   X   Ternary operator


// VERSION 4
struct User {
    var name: String
    // Array
    // Computed and tuple

    init(name: String) {
        self.name = name
    }

    enum Reward {
        case money(Int)     // Associated Value
        case trophy
        case star
    }
    
    var trophies = 0
    var stars = 0
    var totalMoney = 0
    var allRewards: (Int, Int, Int) {
        return (trophies, stars, totalMoney)
    }

    mutating func addReward(reward: Reward) {
        switch reward {
        case .money(let amount):
            totalMoney += amount
        case .trophy:
            trophies += 1
        case .star:
            stars += 1
        }
    }

    func getName() -> String {
        return name
    }
    func getMoney() -> Int {
        return totalMoney
    }
    func getTrophies() -> Int {
        return trophies
    }
    func getStars() -> Int {
        return stars
    }
    func getAllRewards() -> [Int] {
        return [totalMoney, trophies, stars]
    }
}
var luigi = User(name: "Luigi")
var toad = User(name: "Toad")
print("The user \(luigi.getName()) has the following amount of money, trophies, and stars: \(luigi.getAllRewards())")
print("The user \(toad.getName()) has the following amount of money, trophies, and stars: \(toad.getAllRewards())")
luigi.addReward(reward: .money(70))
luigi.addReward(reward: .trophy)
luigi.addReward(reward: .star)
luigi.addReward(reward: .star)
toad.addReward(reward: .money(60))
toad.addReward(reward: .trophy)
toad.addReward(reward: .trophy)
toad.addReward(reward: .star)
print("The user \(luigi.getName()) has the following amount of money, trophies, and stars: \(luigi.getAllRewards())")
print("The user \(toad.getName()) has the following amount of money, trophies, and stars: \(toad.getAllRewards())")
luigi.addReward(reward: .money(20))
print(luigi.getStars() > toad.getStars() ? "\(luigi.getName()) wins" : "\(toad.getName()) wins")


// VERSION 3
//struct User {
//    private var name: String
//    private var money: Int
//    public var trophies: Int
//    private var stars: Int
////    public var rewards: [Reward] = [.star, .trophy]
//    public var amount: Int = 0
//    init(name: String, money: Int, trophies: Int, stars: Int) {
//        self.name = name
//        self.money = money
//        self.trophies = trophies
//        self.stars = stars
//    }
//    enum Reward {
//        case trophy(Int)
//        case star(Int)
//    }
//    mutating func addReward(reward: Reward) {
//        switch reward {
//        case .trophy:
//            trophies = trophies + 1
//        case .star:
//            stars += 1
//        }
//    }
//    mutating func addMoney(amount: Int) {
//        (amount >= 0 ? money += amount : print("You cannot add a negative amount of money."))
//    }
//    func getName() -> String {
//        return name
//    }
//    func hasXMoney() -> Int {
//        return money
//    }
//    func hasXTrophies() -> Int {
//        return trophies
//    }
//    func hasXStars() -> Int {
//        return stars
//    }
//}
//var luigi = User(name: "Luigi", money: 0, trophies: 0, stars: 0)
//print("The user \(luigi.getName()) has \(luigi.hasXMoney()) dollars, \(luigi.hasXTrophies()) trophies, and \(luigi.hasXStars()) stars.")
//luigi.addMoney(amount: 70)
////luigi.addReward(reward: <#T##User.Reward#>)
//print("The user \(luigi.getName()) NOW has \(luigi.hasXMoney()) dollars, \(luigi.hasXTrophies()) trophies, and \(luigi.hasXStars()) stars.")
//luigi.addMoney(amount: 30)
//print("The user \(luigi.getName()) NOW has \(luigi.hasXMoney()) dollars, \(luigi.hasXTrophies()) trophies, and \(luigi.hasXStars()) stars.")


// VERSION 2
//enum Rewards: Int {
//    case money
//    case trophy
//    case star
//}
//var money = 0
//var amount = 0
//var trophies = 0
//var stars = 0
//var rewards: [Rewards] = [.money, .star, .trophy]
//for reward in rewards {
//    switch reward {
//    case .money:
//        money += amount
//    case .trophy:
//        trophies += 1
//    case .star:
//        stars += 1
//    }
//}


// VERSION 1
// rewards: money, trophies, stars
// trophies += 1
// stars += 1
// money += amount
// track cash
// track trophies and stars
// create user
// create reward system

// make two users
// give them some rewards
// print each user with their awards in proper english

// var money = 0
// var stars = 0
// var trophies = 0
// stars += 1
// trophies += 1
// money += __
// user keeps track of how much case, trophies and stars they have



