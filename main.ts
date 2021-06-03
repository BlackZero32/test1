let x = 0
let y = 0
input.onButtonPressed(Button.A, function () {
    x = randint(0, 10)
    basic.showNumber(x)
    y = x % 2
    if (y == 0) {
        basic.showIcon(IconNames.Yes)
    } else if (y == 1) {
        basic.showIcon(IconNames.No)
    }
})
basic.forever(function () {
	
})
